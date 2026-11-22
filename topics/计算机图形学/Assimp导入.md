---
title: 使用Assimp导入3D模型场景树 (Importing 3D Models with Assimp Scene Graph)
requires: [计算机图形学/Assimp库]
---

# 使用Assimp导入3D模型场景树 (Importing 3D Models with Assimp Scene Graph)

## 场景树是什么

使用 Assimp 导入 3D 模型时，程序得到的不只是网格顶点，还包括一个描述模型组织方式的 **Scene Graph（场景图）**。`aiScene` 保存整场景的数据；节点树从它的 `mRootNode` 开始。每个 `aiNode` 可有子节点，并通过下标引用场景的网格；材质由网格引用。

可以把场景树理解为：模型由哪些部件组成、部件之间如何变换、每个部件使用什么网格与材质。

```mermaid
flowchart TD
    S["aiScene"] --> R["aiNode 根节点"]
    R --> A["aiNode 躯干"]
    R --> B["aiNode 车轮"]
    S --> M["aiMesh 表"]
    S --> T["aiMaterial 表"]
    A -->|网格下标| M
    B -->|网格下标| M
    M -->|材质下标| T
```

## 为什么需要场景树

如果只读取三角形缓冲区，程序会失去模型的整体结构，难以独立移动部件、切换材质或执行骨骼动画。场景树保留了模型导入器解析出的层级和变换关系，因此适合实现角色动画、车辆装配、编辑器编辑等功能。

节点局部变换通常按父节点到子节点累积：

$$
M_{\text{world}}=M_{\text{parent}}M_{\text{local}}
$$

其中 $M_{\text{local}}$ 包含节点的平移、旋转和缩放。它对应 `aiNode::mTransformation`，不是 `aiMesh` 的字段。以列向量作用于顶点为例，同一网格若被不同节点引用，每次绘制使用对应节点的累计矩阵。

## 导入与遍历流程

Assimp 的基本使用方式是创建导入器、读取文件、取得场景，再递归访问节点：

```cpp
void ProcessNode(const aiScene* scene, const aiNode* node,
                 const aiMatrix4x4& parent) {
    aiMatrix4x4 world = parent * node->mTransformation;

    for (unsigned i = 0; i < node->mNumMeshes; ++i) {
        const aiMesh* mesh =
            scene->mMeshes[node->mMeshes[i]];
        // 创建 GPU 网格并使用 world 变换
    }

    for (unsigned i = 0; i < node->mNumChildren; ++i) {
        ProcessNode(scene, node->mChildren[i], world);
    }
}

bool ImportModel(const std::string& path) {
    Assimp::Importer importer;
    const aiScene* scene =
        importer.ReadFile(path, aiProcess_Triangulate |
                               aiProcess_JoinIdenticalVertices |
                               aiProcess_GenSmoothNormals);
    if (!scene) {
        // 读取 importer.GetErrorString() 获取导入失败原因
        return false;
    }
    if ((scene->mFlags & AI_SCENE_FLAGS_INCOMPLETE) || !scene->mRootNode) {
        // 此示例需要一棵可遍历的完整场景树
        return false;
    }
    ProcessNode(scene, scene->mRootNode, aiMatrix4x4{});
    return true;
}
```

根节点从单位矩阵开始遍历。导入器销毁后场景指针失效，需在退出 `ImportModel` 前复制所需数据或创建 GPU 资源。

```mermaid
flowchart TD
    A["读取模型文件"] --> B["检查导入状态"]
    B -->|成功| C["取得 aiScene"]
    B -->|失败| D["读取错误信息"]
    C --> E["访问根节点"]
    E --> F["组合父子变换"]
    F --> G["处理节点网格"]
    G --> H["递归访问子节点"]
```

> [!IMPORTANT]
> `aiNode` 负责组织层级，网格数据实际存放在 `aiScene::mMeshes` 中；节点通常通过 `mMeshes` 下标引用它们。

> [!TIP]
> 常见绘制顺序是：先递归遍历场景树建立节点到网格的对应关系，再遍历 `mMeshes` 上传 GPU 资源；不要假定网格下标就是节点下标。

## 与相近概念的区别

| 概念 | 主要内容 | 典型用途 |
|---|---|---|
| `aiScene` | 一次导入得到的完整场景 | 管理网格、材质、纹理、动画 |
| `aiNode` | 场景树中的层级节点 | 保存名称、变换和子节点 |
| `aiMesh` | 顶点、索引、法线等绘制数据 | 创建 GPU 网格 |
| `aiMaterial` | 材质属性与纹理引用 | 设置着色参数 |
| `aiBone` | 骨骼及权重信息 | 蒙皮与角色动画 |

`aiNode` 不是 `aiMesh` 的子对象；许多节点可以不包含网格，多个节点也可能引用同一个网格。

## 常见坑

> [!WARNING]
> - 文件路径要使用 `std::string`；部分版本不直接接受 `const char*`。
> - `ReadFile` 返回空指针后不要继续解引用。
> - 网格若已按某个节点的累计矩阵烘焙到世界坐标，就不要在该次绘制里再乘同一矩阵；要保留网格共享，则保留网格局部坐标，逐次绘制应用各节点矩阵。
> - 递归遍历要同时处理当前节点的网格和全部子节点。
> - 导入坐标单位不一定与引擎一致；DirectX 风格文件常需要转换 Z 轴方向。
> - 大量模型宜使用 `aiProcess_OptimizeMeshes` 等后处理减少网格数量，但会改变原始结构。

## 一个正确处理的例子

假设根节点平移 $(1,0,0)$，车身节点相对根节点平移 $(2,0,0)$，则车身顶点的世界位置应比网格原始位置多偏移 $(3,0,0)$：

$$
M_{\text{world}}
=M_{\text{root}}M_{\text{body}}
=T(1,0,0)\cdot T(2,0,0)
=T(3,0,0)
$$

如果程序只应用车身节点的局部变换，顶点会错误地停在偏移 $(2,0,0)$ 的位置；若先烘焙累计矩阵，再在绘制时重复应用该矩阵，偏移会变成 $(6,0,0)$。==场景树遍历的核心是按父子层级正确组合变换矩阵。==
