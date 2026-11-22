---
title: 《计算机图形学（全英文）》OpenGL Assimp库配置实验指南
kind: 实验
course: 计算机图形学全英文
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301312C%E3%80%91%E8%AE%A1%E7%AE%97%E6%9C%BA%E5%9B%BE%E5%BD%A2%E5%AD%A6%EF%BC%88%E5%85%A8%E8%8B%B1%E6%96%87%EF%BC%89/OpenGL%20Assimp.pdf
---

# OpenGL 实验伴读：先用 Assimp 验证网格导入

原件是历史实验环境指南：第 1 页给出 macOS 的安装入口和 Windows 的源目录、构建目录设置；第 2 页用旧版 Visual Studio 和旧 DirectX SDK 展示编译及链接。下面保留它的安装学习目标，用独立的小模型检验导入，不依赖原件截图或旧工具版本。

## 先认清源目录、构建目录与应用项目

原件中 CMake 界面的两个目录不是同一件事：源目录指向 Assimp 最外层含 `CMakeLists.txt` 的目录；构建目录存放本机生成器、缓存和产物。应用项目是第三处，它编译自己的程序并链接已经可用的 Assimp。切换编译器、架构或生成器时，换一个空的构建目录，避免沿用与新选择不匹配的缓存。

- macOS 可以从 [Homebrew 的 Assimp 配方](https://formulae.brew.sh/formula/assimp)安装。若 CMake 搜不到包，检查所选工具链、Assimp 所在前缀以及二进制架构是否一致，不把另一台机器的头文件路径写死在项目中。
- Windows 可以使用已安装的 Assimp 开发包；如从源码构建，参照 [Assimp 官方构建说明](https://github.com/assimp/assimp/blob/master/Build.md)，按本机已安装的编译器配置。例如给构建目录选用与应用一致的目标架构。产生 `.sln` 是 Visual Studio 生成器的行为，不是判断库是否可用的必要条件。

**订正（适用于当前版本）。** 原件的 DirectX 报错属于旧配置；当前 [Assimp 构建脚本](https://github.com/assimp/assimp/blob/master/CMakeLists.txt)把 Windows 查看器的旧 DirectX 依赖放在可选工具分支。只需要模型导入库时，可使用 `ASSIMP_BUILD_ASSIMP_TOOLS=OFF`，不必为了导入 OBJ 安装旧 SDK。这不代表查看器也能脱离它运行，也不代表旧源码拥有完全相同的选项。

| 卡在哪一步 | 典型现象 | 应核对的边界 |
| --- | --- | --- |
| 编译 | 找不到 `assimp/cimport.h` | 开发头文件及编译目标的包含目录 |
| 链接 | `aiImportFile` 未定义 | 实际链接的库、架构和构建配置 |
| 启动 | 找不到 Assimp 动态库 | 运行时库部署及系统的搜索路径；Windows 的 DLL 与链接用导入库不能互相替代 |
| 导入 | 程序能启动，但模型读不进来 | 文件路径、格式支持、导入错误；不再先改链接设置 |
| 绘制 | 已得到网格，但屏幕没有几何 | [顶点数据与缓冲](../../../topics/计算机图形学/顶点数据.md)、着色器和图形上下文 |

```mermaid
flowchart LR
    A["Assimp 开发包"] --> B["编译并链接小程序"]
    B --> C["独立读入本地 OBJ"]
    C --> D["核对网格、三角形及索引"]
    D --> E["再把数据交给渲染管线"]
```

## 补充：拿一个四边形分离导入和绘制的错误

几何如果一开始就交给 OpenGL，黑屏可能由模型、着色器、视口或 GPU 数据传递导致。先用一个已知结果的文件：边长为 1 的平面四边形。拆成两个三角形，两者面积各是二分之一，合计应保持 1。OBJ 中面索引写作 `1 2 3 4`，但程序看到的是 Assimp 输出的零起点网格索引。

把下列内容保存为 `quad.obj`：

```obj
o quad
v 0 0 0
v 1 0 0
v 1 1 0
v 0 1 0
f 1 2 3 4
```

如果已安装提供 CMake Config 包的 Assimp，可这样链接下面的 `probe.c`：

```cmake
cmake_minimum_required(VERSION 3.16)
project(assimp_probe C)
find_package(assimp CONFIG REQUIRED)
add_executable(assimp_probe probe.c)
target_compile_features(assimp_probe PRIVATE c_std_99)
target_link_libraries(assimp_probe PRIVATE assimp::assimp)
```

同一目录可用 `cmake -S . -B build` 和 `cmake --build build --config Release` 配置、构建；可执行文件的位置随生成器而异。运行它时传入 `quad.obj` 的路径：

```c
#include <assimp/cimport.h>
#include <assimp/scene.h>
#include <assimp/postprocess.h>
#include <stdio.h>

int main(int argc, char **argv) {
    if (argc != 2) return 2;
    const struct aiScene *scene = aiImportFile(argv[1], aiProcess_Triangulate);
    if (!scene) {
        fprintf(stderr, "%s\n", aiGetErrorString());
        return 1;
    }
    if ((scene->mFlags & AI_SCENE_FLAGS_INCOMPLETE) ||
        !scene->mRootNode || scene->mNumMeshes != 1) {
        aiReleaseImport(scene);
        return 1;
    }
    const struct aiMesh *mesh = scene->mMeshes[0];
    int ok = mesh->mNumFaces == 2;
    unsigned min_index = mesh->mNumVertices;
    for (unsigned i = 0; i < mesh->mNumFaces; ++i) {
        const struct aiFace *face = &mesh->mFaces[i];
        if (face->mNumIndices != 3) ok = 0;
        for (unsigned j = 0; j < face->mNumIndices; ++j) {
            const unsigned k = face->mIndices[j];
            if (k >= mesh->mNumVertices) ok = 0;
            if (k < min_index) min_index = k;
        }
    }
    printf("meshes=%u faces=%u min_index=%u\n",
           scene->mNumMeshes, mesh->mNumFaces, min_index);
    aiReleaseImport(scene);
    return (ok && min_index == 0) ? 0 : 1;
}
```

这个文件应得到 `meshes=1 faces=2 min_index=0`。把输入路径改为不存在的文件，则应在导入阶段失败。这里检查的是自制测试件，不是通用遍历器：真实模型可有多个网格，也不能假定所有面都是三角形。

> [!WARNING]
> ==不要给 Assimp 输出的索引再次减一==。OBJ 文本写出的索引和导入后的网格索引属于不同表示；输出已经能直接下标访问顶点数组。这个小例子的最小索引是 0，再减一会变成负数，或在无符号整数中绕回很大的值。

> [!TIP]
> [Assimp 的三角化选项](https://github.com/assimp/assimp/blob/v5.4.3/include/assimp/postprocess.h)不改变点、线图元。要通过三角形列表绘制，仍应检查面元素数或明确过滤非三角图元。进一步使用[模型场景树](../../../topics/计算机图形学/Assimp导入.md)和[节点递归](../../../topics/计算机图形学/Model类.md)时，注意变换属于引用网格的节点，不能从某个网格假设唯一世界变换。C 接口释放场景后，借用的网格和索引指针也不能继续使用。
