---
title: 《Web技术（双语）》第三单元 Cascading Style Sheets（Part I）作业及答案
kind: 习题
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A5.pdf
---

# 《Web技术（双语）》第三单元 Cascading Style Sheets（Part I）作业及答案

原件经识别和整理；“参考解答”是我们补的。

## 专业词汇中译

| 专业词汇 | 中文 |
| --- | --- |
| presentation | 呈现（表示） |
| style sheet | 样式表 |
| property | 属性 |
| cascading | 层叠 |
| level | 层（级） |
| precedence | 优先级 |
| conflict | 冲突 |
| selector | 选择器 |
| rule | 规则 |

## 简答

### 简答 1

（Review Questions 3.1）What is the advantage of document-level style sheets over inline style sheets?

参考解答：**结论**  
文档级样式表相比内联样式表的主要优势在于：实现内容与表现的分离，提高代码复用性和可维护性，减少冗余，便于统一修改。

**推理过程**  
- 内联样式将 CSS 规则直接写在 HTML 元素的 `style` 属性中，样式与结构紧密耦合，每个元素需要单独设置，导致大量重复代码。  
- 文档级样式表（通常写在 `<style>` 标签内）将样式集中定义在文档头部或独立区域，可一次性为多个元素甚至整个页面设定规则。修改样式时只需调整一处，无需逐一遍历元素，极大降低维护成本，并保持 HTML 结构清晰。

知识点：[样式表的三个级别（内联级Inline、文档级Document、外部External）](../../../topics/Web开发技术/style-levels.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)

### 简答 2

（Review Questions 3.8）What is the purpose of a style class selector?

参考解答：**结论**：样式类选择器（class selector）的目的是**将同一套样式规则应用到文档中多个不同的元素上，无论这些元素是同类型还是不同类型**，从而实现样式复用与批量控制。

**推理**：
- 在 CSS 中，类选择器以“`.`”开头，例如 `.highlight`。
- 它基于 HTML 元素 `class` 属性的值进行匹配，一个元素可以有多个类（空格分隔），同一个类名可被任意数量的元素使用。
- 这弥补了元素选择器只能按标签名统一设置、或 ID 选择器只能唯一使用的局限，使样式与元素解耦，增强了灵活性和可维护性。

知识点：[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)、[选择器形式（简单选择器、类选择器Class、通用选择器Generic、id选择器、上下文选择器Contextual、伪类Pseudo class、通配符Universal）](../../../topics/Web开发技术/css-selectors.md)

### 简答 3

（Review Questions 3.10）What is the difference between the two selectors `ol ul` and `ol > ul`?

参考解答：**结论**

`ol ul` 是**后代选择器**（Descendant Selector），匹配 `<ol>` 元素内部任意层级的 `<ul>` 元素；而 `ol > ul` 是**子代选择器**（Child Selector），仅匹配作为 `<ol>` **直接子元素**的 `<ul>` 元素。

**推理与分析**

1.  **`ol ul` (后代选择器)**：
    *   空格表示后代关系。
    *   只要 `<ul>` 出现在 `<ol>` 的开始标签和结束标签之间，无论嵌套多深，都会被选中。
    *   例如：`<ol><li><ul>...</ul></li></ol>` 中的 `<ul>` **会被**选中。

2.  **`ol > ul` (子代选择器)**：
    *   `>` 表示直接父子关系。
    *   只有当 `<ul>` 的父元素直接是 `<ol>` 时，才会被选中。
    *   例如：`<ol><li><ul>...</ul></li></ol>` 中的 `<ul>` **不会被**选中，因为其直接父元素是 `<li>` 而非 `<ol>`。
    *   例如：`<ol><ul>...</ul></ol>` 中的 `<ul>` **会被**选中。

**示例对比**

对于以下 HTML 结构：

```html
<ol>
  <li>
    Item 1
    <ul>
      <li>Nested Item</li>
    </ul>
  </li>
</ol>
```

*   `ol ul`：选中内部的 `<ul>`。
*   `ol > ul`：**不选中**任何元素（因为 `<ul>` 不是 `<ol>` 的直接子节点）。

知识点：[选择器形式（简单选择器、类选择器Class、通用选择器Generic、id选择器、上下文选择器Contextual、伪类Pseudo class、通配符Universal）](../../../topics/Web开发技术/css-selectors.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)、[Web浏览器的工作原理](../../../topics/Web开发技术/web-browsers.md)

### 简答 4

（Exercise 3.1）Create an external style sheet for the chapters of this book.

补充：请编写一个 HTML 文档呈现教材的二级目录结构，然后写一个外部 CSS 文件定义其外观。

HTML 代码

```html

```

CSS 代码

```css

```

参考解答：**结论：**  
外部样式表通过 `.css` 文件定义样式，HTML 通过 `<link>` 标签引入；二级目录用嵌套 `<ul>` 表示，CSS 控制层级缩进、字体、颜色及链接交互效果。

**HTML 代码：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Web技术（双语）教材目录</title>
    <!-- 引入外部样式表 -->
    <link rel="stylesheet" href="book-styles.css">
</head>
<body>
    <h1>Web Technologies (Bilingual)</h1>
    <h2>Table of Contents</h2>
    
    <ul class="toc">
        <li class="chapter">
            <span class="chapter-title">Chapter 1: Introduction to the Web</span>
            <ul class="sections">
                <li><a href="#s1-1">1.1 History of the Internet</a></li>
                <li><a href="#s1-2">1.2 Web Standards and Protocols</a></li>
                <li><a href="#s1-3">1.3 Basic Architecture</a></li>
            </ul>
        </li>
        
        <li class="chapter">
            <span class="chapter-title">Chapter 2: HTML Fundamentals</span>
            <ul class="sections">
                <li><a href="#s2-1">2.1 Document Structure</a></li>
                <li><a href="#s2-2">2.2 Text Elements and Formatting</a></li>
                <li><a href="#s2-3">2.3 Lists and Tables</a></li>
            </ul>
        </li>
        
        <li class="chapter">
            <span class="chapter-title">Chapter 3: CSS Styling</span>
            <ul class="sections">
                <li><a href="#s3-1">3.1 Selectors and Properties</a></li>
                <li><a href="#s3-2">3.2 Box Model</a></li>
                <li><a href="#s3-3">3.3 Layout and Positioning</a></li>
            </ul>
        </li>
    </ul>
</body>
</html>
```

**CSS 代码：**

```css
/* 全局基础样式 */
body {
    font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    color: #333;
}

/* 主标题 */
h1 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
}

/* 副标题 */
h2 {
    color: #34495e;
    font-weight: normal;
    margin-top: 30px;
}

/* 一级目录（章节） */
ul.toc {
    list-style-type: none;
    padding-left: 0;
}

li.chapter {
    margin-bottom: 25px;
    background: white;
    padding: 15px 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.chapter-title {
    font-weight: bold;
    font-size: 1.2em;
    color: #2980b9;
    display: block;
    margin-bottom: 10px;
}

/* 二级目录（小节） */
ul.sections {
    list-style-type: none;
    padding-left: 20px;  /* 实现层级缩进 */
    margin-top: 5px;
}

ul.sections li {
    padding: 5px 0;
    border-bottom: 1px dotted #ddd;
}

ul.sections li:last-child {
    border-bottom: none;
}

/* 链接样式 */
ul.sections a {
    color: #555;
    text-decoration: none;
    transition: color 0.3s ease;
}

ul.sections a:hover {
    color: #e74c3c;
    text-decoration: underline;
}

/* 访问过的链接 */
ul.sections a:visited {
    color: #8e44ad;
}
```

**关键说明：**
- **外部样式表**：CSS 保存在独立 `.css` 文件中，通过 `<link rel="stylesheet" href="...">` 引入，实现结构与表现分离
- **二级结构**：`<ul>` 嵌套 `<ul>` 表示层级，内层 `padding-left` 产生缩进
- **选择器**：使用类选择器（`.chapter`）和后代选择器（`ul.sections a`）精准控制不同层级样式

知识点：[样式表的三个级别（内联级Inline、文档级Document、外部External）](../../../topics/Web开发技术/style-levels.md)、[选择器形式（简单选择器、类选择器Class、通用选择器Generic、id选择器、上下文选择器Contextual、伪类Pseudo class、通配符Universal）](../../../topics/Web开发技术/css-selectors.md)、[列表（无序列表、有序列表、定义列表）](../../../topics/Web开发技术/lists.md)

### 简答 5

请问下面的选择器分别选中哪些元素？

```css
p.specials {color: red;}
p#footer {color: red;}
p.featured.new { }
```

参考解答：结论：

- `p.specials`：选中所有 class 包含 `specials` 的 `<p>` 元素。
- `p#footer`：选中 id 为 `footer` 的 `<p>` 元素。
- `p.featured.new`：选中 class 同时包含 `featured` 和 `new` 的 `<p>` 元素。

推理过程：

1. `p.specials`：元素选择器 `p` 与类选择器 `.specials` 的**交集**（无空格），表示 `<p>` 元素且类含 `specials`。
2. `p#footer`：`p` 与 ID 选择器 `#footer` 的交集，ID 唯一，故最多选中一个 `<p id="footer">`。
3. `p.featured.new`：`p` 与两个类选择器 `.featured`、`.new` 的交集，要求 `<p>` 的 class 属性同时含 `featured` 和 `new`，如 `<p class="featured new">`。注意这里的空格不是组合器，class 属性中用空格分隔多个类。

$$\text{选择器的多个部分是“与”关系（交集），必须同时满足所有条件。}$$

知识点：[选择器形式（简单选择器、类选择器Class、通用选择器Generic、id选择器、上下文选择器Contextual、伪类Pseudo class、通配符Universal）](../../../topics/Web开发技术/css-selectors.md)

### 简答 6

请问如何将右侧数字表示为分数形式？写出 HTML 代码和 CSS 样式规则。

HTML 代码

```html

```

CSS 代码

```css

```

参考解答：**结论：**  
使用 MathML 标记，在 HTML 中通过 `<math>`、`<mfrac>` 标签表示分数；CSS 主要设置字体、字号和样式。

**推理过程：**

1.  HTML5 原生支持 **MathML**（Mathematical Markup Language），无需外部库即可渲染数学公式。
2.  表示分数的核心标签是 `<mfrac>`，它包含两个子元素：第一个为分子，第二个为分母。
3.  数字使用 `<mn>` 标签包裹，整个公式放在 `<math>` 标签内。
4.  CSS 用于控制 `math` 元素的字体、大小等外观样式。

**HTML 代码**

```html
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>
    <mn>2</mn>
  </mfrac>
</math>
```

**CSS 代码**

```css
math {
  font-family: "Cambria Math", "STIX Two Math", serif;
  font-size: 24px;
  color: #333;
}
```

*注：若需表示其他分数，只需修改 `<mfrac>` 中两个 `<mn>` 标签内的数字即可。*

知识点：[CSS属性：字体属性（Font Properties）](../../../topics/Web开发技术/css-properties-font.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)

### 简答 7

请写出右侧图片对应的 HTML 代码及 CSS 样式规则。

This is my first web page!

| HTML 代码 |
| --- |
|  |

| CSS 代码 |
| --- |
|  |

参考解答：**结论**

由于无法直接查看图片，基于题目中给出的文本内容 `"This is my first web page!"` 以及《Web技术》课程中最基础、最典型的首个网页示例，推断该图片展示的是一个包含此标题/文本的简单网页。以下为对应的标准 HTML 与 CSS 代码：

| HTML 代码 |
| --- |
| ```html<br><!DOCTYPE html><br><html lang="en"><br><head><br>    <meta charset="UTF-8"><br>    <title>My First Web Page</title><br>    <link rel="stylesheet" href="style.css"><br></head><br><body><br>    <h1>This is my first web page!</h1><br></body><br></html><br>``` |

| CSS 代码 |
| --- |
| ```css<br>/* style.css */<br>body {<br>    font-family: Arial, sans-serif;<br>    text-align: center;<br>    margin-top: 50px;<br>}<br><br>h1 {<br>    color: #333333;<br>}<br>``` |

**推理过程**

1. **HTML 结构**：
   - 任何标准的 HTML5 页面必须以 `<!DOCTYPE html>` 声明开头。
   - 根元素为 `<html>`，头部 `<head>` 中包含字符编码 `<meta charset="UTF-8">` 和页面标题 `<title>`。
   - 引入外部 CSS 文件使用 `<link rel="stylesheet" href="style.css">`（若图片中是内联样式则写在 `<style>` 标签内，但双语课程通常要求分离）。
   - 核心文本 `"This is my first web page!"` 作为页面主要信息，语义化标签应使用 `<h1>`（一级标题）或 `<p>`（段落）。此处以 `<h1>` 为例。

2. **CSS 样式规则**：
   - 针对 `body` 设置基础排版：`text-align: center;` 使文本居中显示（这是入门示例最常见的布局），`font-family` 设置无衬线字体，`margin-top` 提供顶部留白。
   - 针对 `h1` 设置颜色等修饰属性。
   - *注：若原图中有特定的背景色（如 `background-color`）、字体大小（如 `font-size: 24px;`）或边框，只需在对应选择器中添加相应属性即可。*

知识点：[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)

### 简答 8

请写出下图所示表格的 HTML 代码及 CSS 样式规则。

Test Results

| Top Three Performers | | | |
| --- | --- | --- | --- |
| Name | Login ID | Course Name | Marks |
| Joseph | 01236 | MySQL 5 Database Administrator Certified Professional Exam, Part I | 98 |
| Steve | 01234 | MySQL 5 Developer Certified Professional Exam, Part I | 92 |
| John | 01235 | MySQL 5 Developer Certified Professional Exam, Part II | 85 |
| Total number of students | | | 3 |

| HTML 代码 |
| --- |
|  |

CSS 代码

```css

参考解答：```html
<table>
  <caption>Test Results</caption>
  <thead>
    <tr>
      <th colspan="4">Top Three Performers</th>
    </tr>
    <tr>
      <th>Name</th>
      <th>Login ID</th>
      <th>Course Name</th>
      <th>Marks</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Joseph</td>
      <td>01236</td>
      <td>MySQL 5 Database Administrator Certified Professional Exam, Part I</td>
      <td>98</td>
    </tr>
    <tr>
      <td>Steve</td>
      <td>01234</td>
      <td>MySQL 5 Developer Certified Professional Exam, Part I</td>
      <td>92</td>
    </tr>
    <tr>
      <td>John</td>
      <td>01235</td>
      <td>MySQL 5 Developer Certified Professional Exam, Part II</td>
      <td>85</td>
    </tr>
    <tr>
      <td colspan="3">Total number of students</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
```

```css
table {
  border-collapse: collapse;
  width: 100%;
  font-family: Arial, sans-serif;
}
caption {
  font-size: 1.5em;
  font-weight: bold;
  margin-bottom: 0.5em;
}
th, td {
  border: 1px solid #333;
  padding: 8px;
  text-align: left;
}
thead th {
  background-color: #f2f2f2;
  text-align: center;
}
tbody tr:last-child td {
  font-weight: bold;
}
```

知识点：[表格（基本标签、rowspan与colspan、表格分块、align与valign）](../../../topics/Web开发技术/tables.md)、[CSS属性：边距（Margins）与背景图像（Background images）](../../../topics/Web开发技术/css-properties-margin-bg.md)
