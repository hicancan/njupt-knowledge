---
title: 基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）
requires: [Web开发技术/html-doc-structure]
---

# 基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）

## 基本文本标记

### 为什么需要这些标记

纯文本在浏览器里会被“压扁”：换行和多个空格会被合并成一个空格。想让段落分明、标题醒目、引用清晰，就必须用标记告诉浏览器“这是什么内容”。

> [!IMPORTANT]
> 浏览器默认忽略源代码中的单个换行与多余空格，==只有用标记才能表达真实排版意图==。

### 常用标记一览

| 标记 | 写法 | 作用 | 关键区别 |
| :--- | :--- | :--- | :--- |
| 段落 | `<p>...</p>` | 块级段落，前后自动留白 | 与 `<br />` 不同，`<p>` 是结构 |
| 换行 | `<br />` | 强制换行，不新增段落 | 空元素，无内容 |
| 标题 | `<h1>`~`<h6>` | 六级标题，`<h1>` 最大 | 都默认比正文大；`<h6>` 最小 |
| 块引用 | `<blockquote>...</blockquote>` | 长引用，块级缩进 | 行内引用用 `<q>` |
| 水平线 | `<hr />` | 分隔主题 | 空元素，仅表示语义分隔 |
| 上标 | `<sup>...</sup>` | 上标，如 $x^2$ | 与 `<sub>` 相反 |
| 下标 | `<sub>...</sub>` | 下标，如 $H_2O$ | 常用于化学式 |

### 字符实体

有些字符不能直接写，或写了会被浏览器当成标记：

| 字符 | 实体 | 用途 |
| :--- | :--- | :--- |
| `<` | `&lt;` | 避免被当成标签开始 |
| `>` | `&gt;` | 同上 |
| `&` | `&amp;` | 避免被当成实体开始 |
| 空格 | `&nbsp;` | 不换行空格 |
| © | `&copy;` | 版权符号 |

> [!WARNING]
> 常见坑：直接写 `a < b` 会被浏览器误认为标签开始；写多个空格想缩进，结果全被合并。==要显示 `<` 必须写 `&lt;`，要保留空格用 `&nbsp;`==。

### 元素与内容

一个元素通常由开始标签、内容、结束标签组成：

```html
<p>Hello <strong>Web</strong></p>
```

这里 `<p>` 元素的内容是 `Hello <strong>Web</strong>`，其中又嵌套了 `<strong>` 元素。

### 一个完整例子

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>My Info</title>
</head>
<body>
    <h1>About Me</h1>

    <h2>Name</h2>
    <p><strong>Name:</strong> John Doe</p>

    <h2>Contact</h2>
    <p>
        <strong>Address:</strong><br>
        123 Main Street<br>
        City, State
    </p>

    <hr />

    <h2>Academic</h2>
    <p><strong>Major:</strong> Computer Science</p>
    <p>Grade Level: Junior</p>
</body>
</html>
```

> [!TIP]
> 记忆口诀：==段落 `p` 分块，换行 `br` 断行；标题 `h1` 到 `h6`，引用 `blockquote`，水平线 `hr` 分隔；上下标 `sup`/`sub`，特殊字符用实体==。
