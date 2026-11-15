---
title: GLEW扩展加载与初始化 (Extension Loading with GLEW)
requires: [计算机图形学/GLFW窗口]
---

# GLEW扩展加载与初始化 (Extension Loading with GLEW)

## GLEW 是什么

OpenGL 只规定了函数接口，具体实现由显卡驱动提供。不同平台、不同驱动支持的版本和扩展并不相同，因此程序不能假设 `glGenVertexArrays`、`glCreateShader` 等函数的地址天然可用。

==GLEW（OpenGL Extension Wrangler Library）负责查询并加载这些函数入口==，同时提供版本与扩展支持信息。它解决的是“如何取得 OpenGL 函数”，不负责创建窗口，也不负责生成 OpenGL 上下文。

```mermaid
flowchart LR
    A["创建窗口"] --> B["创建上下文"]
    B --> C["设为当前"]
    C --> D["glewInit"]
    D --> E["检查错误"]
    E --> F["调用 OpenGL"]
```

## 为什么需要它

核心 OpenGL 与扩展功能最终都由驱动实现。GLEW 在运行时检查当前环境，并把函数指针绑定到可用入口。若绕过初始化，代码即使编译、链接成功，运行时仍可能因函数指针为空而崩溃。

可以把三个概念分开：

| 工具或概念 | 主要职责 | 不负责 |
|---|---|---|
| GLFW / GLUT | 窗口、输入、上下文 | 加载全部 OpenGL 函数 |
| OpenGL Context | 保存 OpenGL 状态，决定实际运行环境 | 创建窗口 |
| GLEW | 加载函数入口，查询版本与扩展 | 创建上下文 |

> [!IMPORTANT]
> ==必须先创建并激活 OpenGL 上下文，再调用 `glewInit()`==。没有当前上下文，GLEW 无法可靠查询驱动能力。

## 正确初始化流程

典型顺序如下：

```cpp
if (!glfwInit()) {
    return -1;
}

GLFWwindow* window = glfwCreateWindow(
    800, 600, "OpenGL", nullptr, nullptr
);
if (!window) {
    glfwTerminate();
    return -1;
}

glfwMakeContextCurrent(window);

glewExperimental = GL_TRUE;
GLenum err = glewInit();
if (err != GLEW_OK) {
    fprintf(stderr, "GLEW: %s\n",
            glewGetErrorString(err));
    return -1;
}

// 此后才调用现代 OpenGL 函数
GLuint vao;
glGenVertexArrays(1, &vao);
```

`glewExperimental = GL_TRUE` 常用于核心上下文，使 GLEW 更完整地尝试加载现代入口；`glewInit()` 的返回值必须检查，==返回 `GLEW_OK` 才表示初始化成功==。

初始化后还应确认版本或扩展，而不是只看程序是否启动：

```cpp
if (!GLEW_VERSION_3_3) {
    // 当前环境不支持所需的 OpenGL 3.3
}
```

## 一个正确的判断例子

某程序按以下顺序执行：

```text
glfwInit → glfwCreateWindow → glfwMakeContextCurrent
→ glewInit（返回 GLEW_OK）→ glCreateShader
```

这个顺序正确，因为调用 `glCreateShader` 前已经存在当前上下文，且 GLEW 初始化成功。若把 `glewInit()` 移到 `glfwCreateWindow` 之前，即使编译通过，也不能据此认定函数加载有效。

> [!WARNING]
> 常见错误包括：在上下文前初始化 GLEW、忽略 `glewInit()` 返回值、把 GLEW 当成窗口库，以及看到黑屏就只检查 GLEW。黑屏还可能来自着色器编译、顶点数据、缓冲区绑定或绘制状态错误。

> [!TIP]
> 记忆顺序：==窗口 → 上下文 → 设为当前 → GLEW → OpenGL 调用==。另外，GLEW 初始化可能留下可忽略的 `GL_INVALID_ENUM`，诊断时应结合初始化返回值与后续 `glGetError()`，不要只凭一次旧错误判断失败。
