---
title: 使用SOIL2加载图像生成纹理 (Loading Textures with SOIL2)
requires: [计算机图形学/SOIL2库, 计算机图形学/纹理坐标]
---

# 使用SOIL2加载图像生成纹理 (Loading Textures with SOIL2)

## 使用 SOIL2 加载图像生成纹理

纹理映射（Texture Mapping）的第一步，是拿到一张图像并把它交给 OpenGL。OpenGL 本身只能处理显存中的纹理对象，它不认识 PNG、JPG 这类文件格式。因此需要一个库把图片文件解码成原始像素数组，再上传给 OpenGL。**SOIL2**（Simple OpenGL Image Library 2）就是为此设计的轻量级库。

> [!NOTE]
> 南邮课件中常把 SOIL2 与 `stb_image.h` 对比：`stb_image` 是纯头文件方案，需要自己封装；SOIL2 封装好了加载、翻转、生成纹理的完整流程，更适合教学演示。

### 为什么需要 SOIL2

自己写 PNG/JPEG 解码器是不现实的。即使手写 BMP 解码，也要处理位深、行对齐、颜色通道顺序等细节。SOIL2 把这一切封装成一个函数调用：

```cpp
GLuint texID = SOIL_load_OGL_texture(
    "wood.png",
    SOIL_LOAD_AUTO,
    SOIL_CREATE_NEW_ID,
    SOIL_FLAG_MIPMAPS | SOIL_FLAG_INVERT_Y
);
```

这一个调用完成了四件事：
1. 读取并解码图片文件；
2. 翻转 Y 轴（图像坐标原点在左上，纹理坐标原点在左下）；
3. 生成 mipmap；
4. 创建并绑定一个 OpenGL 纹理对象，返回其 ID。

### 完整的最小流程

```mermaid
flowchart LR
    A["图片文件"] --> B["SOIL2 解码"]
    B --> C["glTexImage2D"]
    C --> D["设置过滤/环绕"]
    D --> E["纹理对象 ID"]
    E --> F["着色器采样"]
```

更细致地说，SOIL2 内部替你调用了 `glGenTextures` + `glBindTexture` + `glTexImage2D` + `glGenerateMipmap`。你拿到的是一个可直接用于 `glBindTexture(GL_TEXTURE_2D, texID)` 的纹理句柄。

> [!IMPORTANT]
> ==SOIL_load_OGL_texture 返回的已经是 OpenGL 纹理对象 ID==，不需要再手动创建纹理对象。返回 0 表示加载失败。

### 常用加载方式对比

| 加载方式 | 返回内容 | 适用场景 |
|---|---|---|
| `SOIL_load_OGL_texture` | OpenGL 纹理 ID | 直接用于渲染，最常用 |
| `SOIL_load_OGL_cubemap` | OpenGL 立方体贴图 ID | 天空盒 |
| `SOIL_load_image` | 原始像素数组指针 | 需要手动上传或 CPU 处理像素 |

### 常见陷阱

> [!WARNING]
> **Y 轴翻转**：OpenGL 的纹理坐标 $(0,0)$ 在图像左下角，而几乎所有图片格式的像素第 0 行在**顶部**。如果不加 `SOIL_FLAG_INVERT_Y`，贴出来的纹理会上下颠倒。南邮的示例代码里几乎都加了这个 flag。

> [!WARNING]
> **纹理 ID 为 0 的静默失败**：如果文件路径错误或格式不支持，SOIL2 会在控制台打印错误并返回 0。此时若继续用 `glBindTexture(GL_TEXTURE_2D, 0)`，相当于解绑了纹理，模型会显示为黑色或使用默认纹理，非常难排查。务必检查返回值。

> [!TIP]
> 判断加载是否成功的标准写法：
> ```cpp
> GLuint tex = SOIL_load_OGL_texture("brick.png", SOIL_LOAD_AUTO,
>                                    SOIL_CREATE_NEW_ID, SOIL_FLAG_INVERT_Y);
> if (tex == 0) { /* 处理错误：打印路径、检查工作目录 */ }
> ```

### 一个算对了的例子

假设我们加载一张 $2 \times 2$ 的纯红纹理（RGB，每个通道 8 位），用它贴到一个四边形上，并配合 `GL_LINEAR` 过滤：

| 步骤 | 发生了什么 |
|---|---|
| `SOIL_load_OGL_texture("red.png", SOIL_LOAD_AUTO, SOIL_CREATE_NEW_ID, SOIL_FLAG_INVERT_Y)` | 解码出 $2 \times 2 \times 3 = 12$ 字节像素数据，上传到 GPU，返回纹理 ID（如 `1`） |
| `glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)` | 缩小过滤使用三线性插值，mipmap 之间平滑过渡 |
| `glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)` | 放大时双线性插值 |
| 片元着色器 `texture(texSampler, vTexCoord)` | 纹理坐标 $(u,v)$ 经插值后采样 |

当四边形刚好以原始大小显示在屏幕上时，每个片元恰好覆盖一个纹素，采样结果就是纯红色。如果把四边形放大到 $4 \times 4$ 屏幕像素，由于 `GL_LINEAR` 放大过滤，插值结果仍然是纯红（纹素间无变化）；但如果纹理是棋盘格，放大后边缘会出现灰色过渡——这正是双线性插值的效果。

> [!IMPORTANT]
> 对 `SOIL_load_OGL_texture` 来说，==过滤和环绕参数必须在纹理生成之后设置==。SOIL2 默认生成纹理时使用基础的 `GL_LINEAR` 与 `GL_REPEAT`，不满足需求时要在返回后手动调整。

### 与生成纹理对象的流程对应

即使你换用 `stb_image` 或自己解码，核心流程不变：解码得到像素数组 → `glGenTextures` → `glBindTexture` → `glTexImage2D` → 设置参数 → `glGenerateMipmap`。SOIL2 只是把这个流程打包了。理解这个底层顺序有助于你区分“SOIL2 做了什么”和“OpenGL 本身需要什么”。
