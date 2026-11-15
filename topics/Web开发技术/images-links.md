---
title: 图像（img）与超文本链接（a标签、文档内部目标）
requires: [Web开发技术/html-doc-structure]
---

# 图像（img）与超文本链接（a标签、文档内部目标）

## 它是什么

在网页里，**图像**和**超链接**是两类"块外"的补充元素：`<img />` 把一张图片嵌入文档，`<a>` 把一段内容变成可点击的跳转入口。XHTML 中 `<img />` 是==空元素==（self-closing），没有内容，只有属性；`<a>` 则是成对标签，它的"内容"就是用户看得见、点得到的那段文字或图片。

为什么需要？文档只靠文字与标题，信息密度太低、导航也很弱；图片提升可读性，超链接把孤立的 HTML 文档连成一张 Web。

## 图像 `<img />`

最小形式：`<img src="logo.png" alt="校徽" />`。

- `src`（图片的 URL）和 `alt`（替代文本）是==必须的两个属性==。
- `width` / `height` 以**像素**为单位指定显示尺寸（如 `width="200"`）。
- `alt` 在图片加载失败、或用户使用屏幕阅读器时显示/朗读，对可访问性非常重要。

> [!IMPORTANT]
> `<img />` 无内容，但有属性；属性值一律用引号包住。考点：`src` 与 `alt` 是两个必需属性。

## 超链接 `<a>`

`<a>` 的必选属性是 `href`（目标地址）。写法：

```html
<a href="loung.html">休息室</a>
```

链接目标有三类：

| 目标 | `href` 形式 | 例 |
| :-- | :-- | :-- |
| 其它文档 | 相对/绝对路径 | `href="loung.html"` |
| 本文档片段 | `#片段ID` | `href="#intro"` |
| 其它文档片段 | `文件名#片段ID` | `href="loung.html#seat"` |

片段（fragment）由目标元素的 `id` 属性定义，例如 `<h1 id="intro">`。

> [!WARNING]
> 链接==不允许嵌套==：`<a>` 里不能再套 `<a>`。浏览器解析到第二个 `<a>` 时会先关闭前一个，结构会塌掉。

## 文档内部目标（同文档目录）

一篇文档里有三个一级标题，想做一份可点击的目录，常见做法是给标题加 `id`，目录用 `href="#id"` 指过去：

**方案一：目录和内容在同一 HTML 文档**

```html
<nav>
  <a href="#t1">第一章</a>
  <a href="#t2">第二章</a>
  <a href="#t3">第三章</a>
</nav>
<h1 id="t1">第一章</h1>
<h1 id="t2">第二章</h1>
<h1 id="t3">第三章</h1>
```

**方案二：目录在 `index.html`，内容在 `content.html`**

```html
<!-- index.html -->
<a href="content.html#t1">第一章</a>
<a href="content.html#t2">第二章</a>
<a href="content.html#t3">第三章</a>

<!-- content.html -->
<h1 id="t1">第一章</h1>
<h1 id="t2">第二章</h1>
<h1 id="t3">第三章</h1>
```

> [!TIP]
> 记忆：**同文档用 `#id`，跨文档用 `文件#id`**。片段值是 `URL#fragment` 形式。

## 链接路径怎么写

链接写的是**相对当前文档**的路径，要先弄清目录结构再下笔。假设：

```
site/
├── elixir.html
└── rooms/
    └── loung.html
```

从 `elixir.html` 指向 `loung.html`，`href` 应写成：

```html
<a href="rooms/loung.html">休息室</a>
```

若两者在同级目录，直接 `href="loung.html"`；若要回到上一级，用 `../`，如 `href="../elixir.html"`。

> [!NOTE]
> `<img>` 的 `src` 与 `<a>` 的 `href` 都是相对当前 HTML 文档所在目录解析的，两者计算规则一致。

## 常见坑速查

| 坑 | 说明 |
| :-- | :-- |
| `<img>` 忘写 `alt` | 违反 XHTML 必选属性规定 |
| 把 `width="200px"` 写成带单位 | 值应为纯数字像素 |
| `<a>` 嵌套 `<a>` | 不允许，会截断 |
| 同文档片段写成 `href="/#id"` | 多了 `/`，含义变成站点根；应写 `#id` |
| 跨文档片段漏掉文件名 | `#id` 只指当前文档，跨文档须 `file.html#id` |

> [!CAUTION]
> "==是否允许嵌套链接==" 是常考点，答案是**不允许**；==`<img />` 的两个必需属性==答案是 `src` 和 `alt`，别答成 `width`/`height`。
