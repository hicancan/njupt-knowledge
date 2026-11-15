---
title: OpenGL开发环境配置 (OpenGL Configuration for Windows/Mac)
requires: []
---

# OpenGL开发环境配置 (OpenGL Configuration for Windows/Mac)

## 环境配置前先想清楚一个问题

OpenGL 本身只是一套 **图形 API 规范**，并不负责创建窗口、处理鼠标键盘输入。如果直接下载 OpenGL "SDK"，会发现 Windows 上只有 `opengl32.lib`（固定管线 1.1 版本），macOS 上只有系统自带的 `.framework`（同样老旧且 Apple 已标记废弃）。要使用现代 OpenGL（3.3+ 核心模式），必须借助 **窗口与上下文加载工具**。

> [!IMPORTANT]
> OpenGL 规范 ≠ 可运行的库。真正编程时需要三样东西：**窗口系统接口**（GLFW/GLUT）、**函数指针加载器**（GLAD/GLew）、**OpenGL 驱动**（显卡厂商提供）。

```mermaid
flowchart LR
    A["你的程序"] --> B["GLFW<br/>窗口/输入"]
    A --> C["GLAD<br/>函数指针"]
    B --> D["操作系统<br/>窗口 API"]
    C --> E["显卡驱动<br/>OpenGL 实现"]
```

## Windows 配置流程

以 Visual Studio + GLFW + GLAD 为例：

### 第一步：编译 GLFW

GLFW 官方提供源码，推荐用 CMake 生成 Visual Studio 工程后自行编译，而不是直接下载网上散落的 `.lib`——不同 VS 版本（v142/v143）的运行时库不兼容，编译产物不能混用。

### 第二步：准备 GLAD

访问 [glad.dav1d.de](https://glad.dav1d.de)，选择：
- Language: C/C++
- API: OpenGL
- Version: 3.3（或与课件要求一致）
- Profile: Core
- 勾选 "Generate a loader"

生成后得到 `glad.c` 和两个头文件目录 `glad/`、`KHR/`。

### 第三步：VS 项目配置

| 配置项 | 值 |
|---|---|
| 附加包含目录 | `...\glfw\include`、`...\glad\include` |
| 附加库目录 | `...\glfw\build\src\Release` |
| 附加依赖项 | `glfw3.lib; opengl32.lib` |
| 源文件 | 添加 `glad.c` 到项目 |

`opengl32.lib` 是 Windows 自带的，**不能省略**——GLFW 在 Windows 上底层仍会链接它。

### 第四步：初始化顺序

```cpp
glfwInit();                          // 1. 初始化 GLFW
glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

GLFWwindow* window = glfwCreateWindow(800, 600, "NJUPT CG", NULL, NULL);
glfwMakeContextCurrent(window);      // 2. 绑定 OpenGL 上下文

gladLoadGLLoader((GLADloadproc)glfwGetProcAddress);  // 3. 加载函数指针
```

> [!WARNING]
> ==必须先创建窗口并绑定上下文，再调用 `gladLoadGLLoader`==。否则 GLAD 拿不到任何有效函数地址，后续所有 `glXxx` 调用直接崩溃。

## macOS 配置流程

macOS 上 GLFW 推荐直接用 Homebrew：
```bash
brew install glfw
```
然后 CMake 里 `find_package(glfw3 REQUIRED)` 即可链接。GLAD 的生成方式与 Windows 完全相同。

macOS 的特殊点：
- OpenGL 最高支持 **4.1**，且 Apple 已将其标记为 deprecated（但仍可用）
- 窗口创建时必须添加 `glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);`
- 无需链接任何额外的 OpenGL 框架，GLFW 会处理 `Cocoa` 与 `OpenGL.framework` 的链接

## 常见坑

> [!CAUTION]
> **头文件包含顺序**：必须先 `#include <glad/glad.h>`，再 `#include <GLFW/glfw3.h>`。因为 `glfw3.h` 内部会检测是否已加载 OpenGL 头文件，顺序颠倒会导致类型重定义或 GLFW 误以为你用了系统 `gl.h`。

> [!TIP]
> **验证配置是否成功**：初始化完成后执行
> ```cpp
> std::cout << glGetString(GL_VERSION) << std::endl;
> ```
> 输出 `3.3.0 NVIDIA ...`（或类似）说明函数指针加载正常、驱动工作在核心模式下。如果输出空或崩溃，检查上下文是否已绑定。

## 一个验证例子

假设配置完成后运行以下最小程序，预期结果：

```cpp
// 初始化（如上，略）
glViewport(0, 0, 800, 600);
glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
glClear(GL_COLOR_BUFFER_BIT);
glfwSwapBuffers(window);
```

- 窗口标题栏显示 `NJUPT CG`，内容区域为深青灰色 `(0.2, 0.3, 0.3)`，无闪烁无崩溃 → ==配置完全正确==
- 窗口出现即消失 → 缺少主循环 `while(!glfwWindowShouldClose(window))`
- 编译报 `gladLoadGLLoader` 未定义 → `glad.c` 没加入源文件

**与 GLUT/freeglut 的区别**：GLUT 更老、封装度更高（甚至控制主循环），适合教学演示但已停止维护；GLFW 只管理窗口与输入，渲染逻辑完全由你掌控，是当前工业界与课件推荐的主流选择。
