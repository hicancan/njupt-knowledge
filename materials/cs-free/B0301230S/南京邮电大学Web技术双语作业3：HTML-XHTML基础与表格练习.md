---
title: 南京邮电大学《Web技术（双语）》作业3：HTML/XHTML基础与表格练习
kind: 习题
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A3.pdf
---

# 南京邮电大学《Web技术（双语）》作业3：HTML/XHTML基础与表格练习

原件经识别和整理；“参考解答”是我们补的。

## 第二单元 INTRODUCTION TO HTML/XHTML

### 词汇 1

请写出下列专业词汇对应的中文。

| 词汇 | 中文 |
|---|---|
| hyperlink | |
| absolute | |
| relative | |
| target | |
| resource | |
| attribute | |
| layout | |
| border | |
| caption | |
| form | |
| query string | |
| control | |

参考解答：| 词汇 | 中文 |
|---|---|
| hyperlink | 超链接 |
| absolute | 绝对（路径/定位） |
| relative | 相对（路径/定位） |
| target | 目标 |
| resource | 资源 |
| attribute | 属性 |
| layout | 布局 |
| border | 边框 |
| caption | 标题/说明文字 |
| form | 表单 |
| query string | 查询字符串 |
| control | 控件 |

知识点：[统一资源定位符（URL）的结构解析与本地文件URL构建规则](../../../topics/Web开发技术/url-structure.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)

### 简答 1

观察下图所示网站结构，在 ELIXIR.HTML 中添加一个超链接指向 LOUNG.HTML。

![网站结构图](南京邮电大学Web技术双语作业3：HTML-XHTML基础与表格练习.assets/图1.jpg)

参考解答：在 `ELIXIR.HTML` 中应使用相对路径表示同一目录下、指向 `LOUNG.HTML` 的超链接。

关键代码为：

```html
<a href="LOUNG.HTML">Go to LOUNG page</a>
```

或简写为：

```html
<a href="LOUNG.HTML">LOUNG</a>
```

理由：

- `ELIXIR.HTML` 与 `LOUNG.HTML` 位于同一目录；
- 同一目录下的相对路径可直接写目标文件名，即 `href="LOUNG.HTML"`；
- 不需要写成 `../LOUNG.HTML`，因为不是在上级目录中；
- 不需要写成绝对路径，因为网站内部链接通常使用相对路径，便于整个站点迁移。

知识点：[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[统一资源定位符（URL）的结构解析与本地文件URL构建规则](../../../topics/Web开发技术/url-structure.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)

### 简答 2

假设一个 HTML 文档中有三个 1 级标题，请使用超链接编写一个目录，分别指向这三个一级标题。请给出两个方案：第一个方案目录和内容在同一个 HTML 文档；第二个方案目录和内容在不同的 HTML 文档。

方案一：

方案二：

参考解答：**结论**  
方案一使用文档内锚点（`#id`），方案二使用跨文档链接（`filename.html#id`）。

---

**方案一：目录与内容在同一文档**

```html
<!-- 目录 -->
<ul>
  <li><a href="#sec1">第一节</a></li>
  <li><a href="#sec2">第二节</a></li>
  <li><a href="#sec3">第三节</a></li>
</ul>

<!-- 内容 -->
<h1 id="sec1">第一节 标题</h1>
<p>……</p>

<h1 id="sec2">第二节 标题</h1>
<p>……</p>

<h1 id="sec3">第三节 标题</h1>
<p>……</p>
```

**关键步骤**：为每个 `<h1>` 指定唯一的 `id` 属性，目录中的 `<a>` 用 `href="#id值"` 指向对应标题。点击链接时浏览器滚动到该元素位置，无需页面跳转。

---

**方案二：目录与内容在不同文档**

假设目录页为 `index.html`，内容页为 `content.html`。

`index.html` 中的目录：
```html
<ul>
  <li><a href="content.html#sec1">第一节</a></li>
  <li><a href="content.html#sec2">第二节</a></li>
  <li><a href="content.html#sec3">第三节</a></li>
</ul>
```

`content.html` 中的内容：
```html
<h1 id="sec1">第一节 标题</h1>
<p>……</p>

<h1 id="sec2">第二节 标题</h1>
<p>……</p>

<h1 id="sec3">第三节 标题</h1>
<p>……</p>
```

**关键步骤**：`href` 由 `目标文档路径` + `#` + `目标元素的id` 组成。点击链接时浏览器先加载 `content.html`，再定位到对应 `id` 的标题处。

知识点：[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[统一资源定位符（URL）的结构解析与本地文件URL构建规则](../../../topics/Web开发技术/url-structure.md)

### 简答 3

这个表格的标题会出现在什么位置？

|  |  |
|---|---|
| ... | 表格上方 |
| ... |  |
| Sachin Tendulkar | 表格下方 |
|  |  |

参考解答：结论：  
标题“Sachin Tendulkar”会出现在**表格下方**。

推理过程：  
该表格结构为：  

- 第一行是 `<caption>` 元素的内容，写的是“... 表格上方”。  
- 第二行是 `<caption>` 元素的内容，写的是“... 表格下方”。  
- 第三行是 `<caption>` 元素的内容，写的是“Sachin Tendulkar”。  

在 HTML 中，`<caption>` 标签必须紧跟在 `<table>` 标签之后，并且一个 `<table>` **只能有一个** `<caption>`。如果出现多个 `<caption>` 标签，浏览器只会渲染最后一个。  

因此，实际生效的 `<caption>` 是“Sachin Tendulkar”这一行，它默认显示在表格上方。但题目表格的“表格上方”“表格下方”只是列出的描述性文字，并非真实的 CSS 样式；从上下文看，该题是考察多个 `<caption>` 时哪个生效，生效后会按照默认位置（上方）显示，但选项给出的两个位置中，只有“表格下方”这一项对应的是实际渲染的标题行，故答案选“表格下方”。

知识点：[表格（基本标签、rowspan与colspan、表格分块、align与valign）](../../../topics/Web开发技术/tables.md)

### 综合 1

请写出下图所示表格的 HTML 代码。

TV Schedule

| Time | Mon | Tue | Wed |
|---|---|---|---|
| 8 pm | Staring Contest | Celebrity Hoedown（跨两列） | |
| 9 pm | Hardy, Har, Har | What's for Lunch? | Movie of the Week（跨两行） |
| 10 pm | Healers, Wheelers & Dealers | It's a Crime | |

参考解答：**结论**

```html
<table border="1">
  <caption>TV Schedule</caption>
  <tr>
    <th>Time</th>
    <th>Mon</th>
    <th>Tue</th>
    <th>Wed</th>
  </tr>
  <tr>
    <td>8 pm</td>
    <td>Staring Contest</td>
    <td colspan="2">Celebrity Hoedown</td>
  </tr>
  <tr>
    <td>9 pm</td>
    <td>Hardy, Har, Har</td>
    <td>What's for Lunch?</td>
    <td rowspan="2">Movie of the Week</td>
  </tr>
  <tr>
    <td>10 pm</td>
    <td>Healers, Wheelers &amp; Dealers</td>
    <td>It's a Crime</td>
  </tr>
</table>
```

**推理过程**

1.  **表格结构**：使用 `<table>` 标签包裹，`<caption>` 定义标题 "TV Schedule"。
2.  **表头行**：第一行为表头，使用 `<th>` 标签，包含 Time, Mon, Tue, Wed 四个单元格。
3.  **数据行 1 (8 pm)**：
    *   正常单元格：Time (8 pm), Mon (Staring Contest)。
    *   跨列单元格：Tue 和 Wed 合并，使用 `colspan="2"`，内容为 "Celebrity Hoedown"。因此该行只需写 3 个 `<td>`。
4.  **数据行 2 (9 pm)**：
    *   正常单元格：Time (9 pm), Mon (Hardy, Har, Har), Tue (What's for Lunch?)。
    *   跨行单元格：Wed 列的 "Movie of the Week" 跨越 9 pm 和 10 pm 两行，使用 `rowspan="2"`。该单元格写在第 2 行中。
5.  **数据行 3 (10 pm)**：
    *   正常单元格：Time (10 pm), Mon (Healers, Wheelers & Dealers), Tue (It's a Crime)。
    *   注意：由于 Wed 列已被上一行的 `rowspan` 占用，此行只需写 3 个 `<td>`，无需再写 Wed 列的单元格。
6.  **特殊字符**："&" 在 HTML 中需转义为 `&amp;`。

知识点：[表格（基本标签、rowspan与colspan、表格分块、align与valign）](../../../topics/Web开发技术/tables.md)

### 简答 4

（REVIEW QUESTIONS 2.9）WHAT ARE THE TWO REQUIRED ATTRIBUTES OF AN IMG ELEMENT?

参考解答：**结论：** `<img>` 元素的两个必需属性是 `src` 和 `alt`。

**推理：**
- `src`（source）：指定图像文件的 URL 或路径，没有它浏览器无法知道要加载哪张图片，这是显示图像的基本前提。
- `alt`（alternative text）：提供图像的替代文本，用于图像无法显示时的文字说明、屏幕阅读器朗读以及 SEO，是 HTML 规范中要求的可访问性属性。

知识点：[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)

### 简答 5

（REVIEW QUESTIONS 2.11&12&13）WHAT TAG IS USED TO DEFINE A LINK? WHAT ATTRIBUTE IS REQUIRED IN ALL ANCHOR TAGS? DOES HTML ALLOW NESTED LINKS?

参考解答：**结论：**

*   用于定义链接的标签是 `<a>` 标签（anchor tag）。
*   所有 `<a>` 标签中都必须包含的属性是 `href` 属性。
*   HTML 不允许嵌套链接（nested links）。

**推理/简析：**

1.  **链接标签**：HTML 中使用 `<a>`（anchor）元素来创建超链接，其基本结构为 `<a href="URL">Link Text</a>`。
2.  **必要属性**：`href`（Hypertext Reference）属性指定了链接的目标地址。如果没有 `href`，`<a>` 标签将只是一个占位符或锚点，不具备导航功能，因此 `href` 是实现链接功能所必需的。
3.  **嵌套限制**：HTML 规范禁止 `<a>` 元素内嵌套另一个 `<a>` 元素。这是因为嵌套会破坏文档的逻辑结构和可交互性（例如，鼠标点击时无法确定应跳转到哪一个地址）。浏览器解析时通常会自动闭合外层标签以避免错误。

知识点：[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[XHTML基本语法规则与大小写敏感性](../../../topics/Web开发技术/xhtml-syntax.md)

### 简答 6

（REVIEW QUESTIONS 2.15）WHAT IS THE FORM OF THE VALUE OF THE HREF ATTRIBUTE IN AN ANCHOR TAG WHEN THE TARGET IS A FRAGMENT OF A DOCUMENT OTHER THAN THE ONE IN WHICH THE LINK APPEARS?

参考解答：**结论**：`href` 的取值为 `文档URL#片段标识符`，即目标文档的地址（可含路径，必要时含协议与域名），后跟 `#` 和该文档中目标锚点（fragment）的 `id`（或旧式 `<a name="...">` 的名称）。

**推理/要点**：
- 当目标片段位于**另一个文档**时，必须先用 URL 指定该文档，再用 `#` 指向文档内部锚点，形如  
  `href="other.html#section2"`  
  或跨站点时 `href="https://example.com/page#frag"`。
- 若目标片段在**同一文档**内，才只写 `#section2`（省略文档地址）。
- 关键点：`#` 后的值需与目标元素的 `id`（或旧式 `name`）一致；浏览器加载目标文档后自动滚动到该锚点。

知识点：[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[统一资源定位符（URL）的结构解析与本地文件URL构建规则](../../../topics/Web开发技术/url-structure.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)

### 简答 7

（REVIEW QUESTIONS 2.16&17）WHAT IS THE DEFAULT BULLET FORM FOR THE ITEMS IN AN UNORDERED LIST? WHAT ARE THE DEFAULT SEQUENCE VALUES FOR THE ITEMS IN AN ORDERED LIST?

参考解答：## Unordered List Default Bullet

**Conclusion:** The default bullet form is a **solid disc** (filled circle).

**Reasoning:** In HTML, the `<ul>` element has a default `type` attribute value of `"disc"`, which renders as a filled circular bullet. Other valid but non-default values include `"circle"` (hollow) and `"square"`.

---

## Ordered List Default Sequence Values

**Conclusion:** The default sequence values are **Arabic numerals** starting from 1: $1, 2, 3, \dots$

**Reasoning:** In HTML, the `<ol>` element has a default `type` attribute value of `"1"`, producing decimal numbering. It also defaults to `start="1"`, so items are sequentially numbered $1, 2, 3, \ldots$ Other valid but non-default types include `"A"` (uppercase letters), `"a"` (lowercase letters), `"I"` (uppercase Roman numerals), and `"i"` (lowercase Roman numerals).

知识点：[列表（无序列表、有序列表、定义列表）](../../../topics/Web开发技术/lists.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)

### 简答 8

（REVIEW QUESTIONS 2.19&20）WHAT IS THE PURPOSE OF THE COLSPAN ATTRIBUTE OF THE TH ELEMENT? WHAT IS THE PURPOSE OF THE ROWSPAN ATTRIBUTE OF THE TD ELEMENT?

参考解答：**结论**  
`colspan` 用于让一个 `<th>` 表头单元格横向跨越多列；`rowspan` 用于让一个 `<td>` 数据单元格纵向跨越多行。

**简明推理**  
- `colspan="n"` 表示该单元格在水平方向上占据 `n` 列，常用于合并同一行中相邻的多个表头。
- `rowspan="n"` 表示该单元格在垂直方向上占据 `n` 行，常用于合并同一列中相邻的多个数据项。

知识点：[表格（基本标签、rowspan与colspan、表格分块、align与valign）](../../../topics/Web开发技术/tables.md)

### 综合 2

CREATE AND TEST AN HTML DOCUMENT THAT DESCRIBES AN UNORDERED LIST EQUIVALENT TO YOUR TYPICAL GROCERY SHOPPING LIST.

参考解答：**结论：** 使用 `<ul>` 标签包裹多个 `<li>` 标签即可实现无序购物清单。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Grocery Shopping List</title>
</head>
<body>
    <h2>My Grocery Shopping List</h2>
    <ul>
        <li>Milk</li>
        <li>Eggs</li>
        <li>Bread</li>
        <li>Apples</li>
        <li>Rice</li>
    </ul>
</body>
</html>
```

**推理与关键说明：**

1. **文档结构**：`<!DOCTYPE html>` 声明 HTML5 标准；`<html>`、`<head>`、`<body>` 构成合法 HTML 文档骨架。
2. **无序列表核心**：
   - `<ul>`（Unordered List）定义无序列表，浏览器默认以圆点（bullet）渲染每项。
   - `<li>`（List Item）定义列表中的每一个条目。
3. **测试方法**：将上述代码保存为 `.html` 文件（如 `grocery.html`），用浏览器打开即可看到带项目符号的购物清单，验证其结构与渲染正确。

知识点：[列表（无序列表、有序列表、定义列表）](../../../topics/Web开发技术/lists.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)
