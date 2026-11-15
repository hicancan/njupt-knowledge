---
title: 《Web技术（双语）》第三单元 Cascading Style Sheets（Part II）作业答案
kind: 答案
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A6.pdf
---

# 《Web技术（双语）》第三单元 Cascading Style Sheets（Part II）作业答案

原件经识别和整理；“参考解答”是我们补的。

---
title: Web技术（双语）第三单元 Cascading Style Sheets（Part II）作业答案
kind: 答案
course: Web技术（双语）
term: 2018-2019-2
source: <原件地址或来源路径>
---

# Web技术（双语）第三单元 Cascading Style Sheets（Part II）作业答案

本资料由识别工具读取的《Web技术（双语）》第三单元作业答案整理而成，包含专业词汇翻译、复习题解答及编程练习题。

## 一、专业词汇翻译

### 选择 1

请写出下列专业词汇对应的中文：

- comma
- occurrence
- generic
- child
- parent
- descendant
- ancestor
- pseudo
- asterisk
- inherit
- font
- category

答案：
- comma：逗号
- occurrence：出现/发生
- generic：通用的/泛指的
- child：子元素
- parent：父元素
- descendant：后代元素
- ancestor：祖先元素
- pseudo：伪
- asterisk：星号
- inherit：继承
- font：字体
- category：类别


## 二、复习题解答

知识点：[选择器形式（简单选择器、类选择器Class、通用选择器Generic、id选择器、上下文选择器Contextual、伪类Pseudo class、通配符Universal）](../../../topics/Web开发技术/css-selectors.md)、[CSS属性：字体属性（Font Properties）](../../../topics/Web开发技术/css-properties-font.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)

### 简答 1

题干：(Review Questions 3.15) Why is it better to use em than pt for font sizes?

参考解答：使用 `em` 单位比 `pt` 单位更好，因为 `em` 是相对单位，它基于当前元素的字体大小进行计算。这使得网页在不同设备、浏览器设置或用户自定义字体大小的情况下具有更好的可访问性和适应性。而 `pt`（磅）是绝对单位，固定不变，无法随用户偏好或屏幕尺寸自动调整，可能导致在小屏幕或高DPI设备上文字过小或过大，影响阅读体验。

知识点：[CSS属性：字体属性（Font Properties）](../../../topics/Web开发技术/css-properties-font.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)

### 简答 2

题干：(Review Questions 3.21) If you want text to flow around the right side of an image, which value, right or left, must be assigned to the float property of the image?

参考解答：必须将值 `right` 分配给图像的 `float` 属性。当图像向左浮动（`float: left`）时，文本会环绕在图像的右侧；反之，若要让文本环绕在图像的右侧，图像本身应向右浮动（`float: right`），这样文本流会从左侧开始并包裹住图像的右边。（注：题目问的是“text to flow around the right side of an image”，即文本在图像右侧流动，这意味着图像应在左侧占据空间，因此图像应 `float: left`。但根据常见表述歧义，若意指图像位于文本流的右侧且文本在其左侧环绕，则图像需 `float: right`。通常“flow around the right side”指文本出现在图像的右边，这要求图像左浮。此处按标准布局逻辑修正：若希望文本出现在图像的右侧，图像应设置为 `float: left`。若题目意思是图像靠右排列，文本在左边环绕，则是 `float: right`。鉴于题目明确说“text to flow around the right side of an image”，即文本在图像右边，故图像应 `float: left`。）

*更正理解*：如果文本要流经图像的**右侧**（即文本块在图像的右边），那么图像应该位于左侧，因此图像的 `float` 属性应为 `left`。

答案：left

知识点：[CSS属性：边距（Margins）与背景图像（Background images）](../../../topics/Web开发技术/css-properties-margin-bg.md)

### 简答 3

题干：(Review Questions 3.33) Which has higher precedence, an id selector or a universal selector (*)?

参考解答：ID 选择器（id selector）具有更高的优先级。在 CSS 特异性（Specificity）计算中，ID 选择器的权重远高于通用选择器（universal selector）。ID 选择器权重为 (0, 1, 0, 0)，而通用选择器权重为 (0, 0, 0, 0)。因此，当两者冲突时，ID 选择器的样式规则将覆盖通用选择器的规则。

答案：id selector


## 三、编程练习

参考解答：使用 `vertical-align: middle` 可实现行内元素（如图片与文本）的垂直居中对齐。

`vertical-align` 仅对行内级元素（inline / inline-block）或表格单元格生效，其 `middle` 值将元素的垂直中点与父元素基线加上 x-height 一半的位置对齐。示例中为 `<img>` 和 `<span>` 同时设置该属性，使二者中线对齐；容器设为 `inline-block` 以形成独立的行内格式化上下文，避免外部基线干扰。若未给两者都设置相同对齐值，则默认 `baseline` 对齐会导致图片底部与文本基线对齐而非居中。

知识点：[CSS属性：文本对齐（Alignment of text）](../../../topics/Web开发技术/css-properties-text.md)、[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[div和span标签在CSS中的应用](../../../topics/Web开发技术/css-div-span.md)

### 计算 1

题干：(Exercise 3.4) Create and test an HTML document that has at least a half page of text and a small box of text embedded on the left margin, with the main text flowing around the small box. The embedded text must appear in a smaller font and also must be set in italic.

要求：编写HTML代码和CSS代码，实现一个至少半页长的文本页面，左侧边距嵌入一个小文本框，主文本围绕该小框流动。嵌入的文本必须使用较小的字体并设置为斜体。

HTML 代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Float Exercise</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="sidebar">
        <p>This is a small box of text embedded on the left margin.</p>
        <p>It uses a smaller font and is italic.</p>
    </div>
    <div class="main-content">
        <h1>Main Text Flowing Around</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.</p>
        <p>Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?</p>
        <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.</p>
        <p>Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.</p>
    </div>
</body>
</html>
```

CSS 代码：

```css
.sidebar {
    float: left;
    width: 20%;
    background-color: #f0f0f0;
    padding: 10px;
    margin-right: 10px;
    font-size: 0.8em; /* Smaller font */
    font-style: italic; /* Italic */
}

.main-content {
    overflow: auto; /* Clearfix for floating elements */
}

.main-content p {
    line-height: 1.6;
}
```

参考解答：**结论：** 使用 CSS `float: left` 将小文本框浮动到左侧，主文本自然环绕；通过 `font-size` 和 `font-style` 控制嵌入文本的字体大小与斜体。

**关键实现步骤：**

1. **HTML 结构**：侧边栏 `.sidebar` 必须放在主内容 `.main-content` **之前**，这样浮动元素才能被后续文档流中的内容环绕。
2. **CSS 浮动与环绕**：
   ```css
   .sidebar {
       float: left;        /* 核心：向左浮动，使主文本环绕 */
       width: 20%;         /* 设定固定宽度形成"小盒子" */
       margin-right: 10px; /* 与主文本保持间距 */
       font-size: 0.8em;   /* 较小字体 */
       font-style: italic; /* 斜体 */
   }
   ```
3. **清除浮动影响（可选）**：
   ```css
   .main-content {
       overflow: auto; /* 触发 BFC，防止容器高度塌陷 */
   }
   ```
4. **半页文本**：在 `.main-content` 中放置足够多的 `<p>` 段落以满足长度要求。

知识点：[元素定位（绝对定位、相对定位、静态定位）与堆叠元素](../../../topics/Web开发技术/css-positioning.md)、[CSS属性：字体属性（Font Properties）](../../../topics/Web开发技术/css-properties-font.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)

### 计算 2

题干：(Exercise 3.5) Create and test an HTML document that has six short paragraphs of text that describe various aspects of the state in which you live. You must define three different paragraph styles, p1, p2, and p3. The p1 style must use left and right margins of 20 pixels, a background color of pink, and a foreground color of blue. The p2 style must use left and right margins of 30 pixels, a background color of black, and a foreground color of yellow. The p3 style must use a text indent of 1 centimeter, a background color of green, and a foreground color of white. The first and fourth paragraphs must use p1, the second and fifth must use p2, and the third and sixth must use p3.

要求：创建一个包含六个短段的HTML文档，描述你所居住州的各个方面。定义三种段落样式 p1, p2, p3。p1：左右边距20px，背景粉色，前景蓝色；p2：左右边距30px，背景黑色，前景黄色；p3：文本缩进1cm，背景绿色，前景白色。第一、四段用p1，第二、五段用p2，第三、六段用p3。

HTML 代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Paragraph Styles Exercise</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <p class="p1">California is known for its diverse landscape, ranging from beaches to mountains.</p>
    <p class="p2">The economy of California is one of the largest in the world, driven by technology and entertainment.</p>
    <p class="p3">Climate in California varies significantly, with Mediterranean climates in coastal areas and arid conditions inland.</p>
    <p class="p1">Los Angeles is a major cultural hub, famous for Hollywood and its film industry.</p>
    <p class="p2">San Francisco is renowned for its steep hills, iconic Golden Gate Bridge, and cool foggy summers.</p>
    <p class="p3">Agriculture plays a vital role in California's economy, particularly in the Central Valley.</p>
</body>
</html>
```

CSS 代码：

```css
.p1 {
    margin-left: 20px;
    margin-right: 20px;
    background-color: pink;
    color: blue;
}

.p2 {
    margin-left: 30px;
    margin-right: 30px;
    background-color: black;
    color: yellow;
}

.p3 {
    text-indent: 1cm;
    background-color: green;
    color: white;
}
```

参考解答：结论：可通过定义三个 CSS 类 `.p1`、`.p2`、`.p3`，分别设置要求的边距、缩进、背景色和文字颜色，再按顺序将它们应用到六个段落，即可完成并测试该页面。

HTML 代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Paragraph Styles Exercise</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <p class="p1">California is known for its diverse landscape, ranging from beaches to mountains.</p>
    <p class="p2">California has one of the world's largest economies, driven by technology and entertainment.</p>
    <p class="p3">Its climate varies from Mediterranean conditions on the coast to arid conditions inland.</p>
    <p class="p1">Los Angeles is a major cultural center and is famous for Hollywood.</p>
    <p class="p2">San Francisco is known for its steep hills and the Golden Gate Bridge.</p>
    <p class="p3">Agriculture is especially important in California's Central Valley.</p>
</body>
</html>
```

`style.css` 代码：

```css
.p1 {
    margin-left: 20px;
    margin-right: 20px;
    background-color: pink;
    color: blue;
}

.p2 {
    margin-left: 30px;
    margin-right: 30px;
    background-color: black;
    color: yellow;
}

.p3 {
    text-indent: 1cm;
    background-color: green;
    color: white;
}
```

简要说明：

- `.p1`、`.p2`、`.p3` 是**类选择器**，通过 `class` 属性应用到对应的 `<p>` 元素。
- `margin-left` 和 `margin-right` 分别设置段落的左、右外边距。
- `background-color` 设置背景色，`color` 设置前景色，即文字颜色。
- `text-indent: 1cm` 只缩进段落的第一行。
- 第 1、4 段使用 `p1`，第 2、5 段使用 `p2`，第 3、6 段使用 `p3`，符合指定顺序。
- 测试时，将 HTML 文件与 `style.css` 放在同一目录，用浏览器打开 HTML 文件，检查六段的边距、缩进和颜色是否正确。

知识点：[选择器形式（简单选择器、类选择器Class、通用选择器Generic、id选择器、上下文选择器Contextual、伪类Pseudo class、通配符Universal）](../../../topics/Web开发技术/css-selectors.md)、[CSS属性：边距（Margins）与背景图像（Background images）](../../../topics/Web开发技术/css-properties-margin-bg.md)

### 简答 3

题干：请使用 vertical-align 样式属性实现上述图片的内容。写出HTML代码及相应的样式规则。

*注：原题提及“上述图片”，但在提供的文本内容中未包含具体图片描述。根据常见的 vertical-align 应用场景，通常用于对齐行内元素或表格单元格中的内容。以下提供一个通用的示例，假设需要将文本与图片垂直居中对齐。*

HTML 代码：

```html
<div class="container">
    <img src="example.jpg" alt="Example Image" class="aligned-image">
    <span class="aligned-text">This text should be vertically aligned with the image.</span>
</div>
```

CSS 代码：

```css
.container {
    display: inline-block;
    border: 1px solid #ccc;
    padding: 10px;
}

.aligned-image {
    vertical-align: middle;
    height: 50px;
    width: 50px;
}

.aligned-text {
    vertical-align: middle;
    font-size: 16px;
}
```

参考解答：使用 `vertical-align: middle` 可实现行内元素（如图片与文本）的垂直居中对齐。

`vertical-align` 仅对行内级元素（inline / inline-block）或表格单元格生效，其 `middle` 值将元素的垂直中点与父元素基线加上 x-height 一半的位置对齐。示例中为 `<img>` 和 `<span>` 同时设置该属性，使二者中线对齐；容器设为 `inline-block` 以形成独立的行内格式化上下文，避免外部基线干扰。若未给两者都设置相同对齐值，则默认 `baseline` 对齐会导致图片底部与文本基线对齐而非居中。

知识点：[CSS属性：文本对齐（Alignment of text）](../../../topics/Web开发技术/css-properties-text.md)、[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[div和span标签在CSS中的应用](../../../topics/Web开发技术/css-div-span.md)
