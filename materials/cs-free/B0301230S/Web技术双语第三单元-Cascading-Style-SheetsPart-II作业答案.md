---
title: 《Web技术（双语）》第三单元 Cascading Style Sheets（Part II）作业答案
kind: 答案
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A6.pdf
---

# 《Web技术（双语）》第三单元 Cascading Style Sheets（Part II）作业答案

原件经识别和整理；“参考解答”是我们补的。

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

知识点：[CSS属性：字体属性（Font Properties）](../../../topics/Web开发技术/css-properties-font.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)

### 简答 2

题干：(Review Questions 3.21) If you want text to flow around the right side of an image, which value, right or left, must be assigned to the float property of the image?

知识点：[CSS属性：边距（Margins）与背景图像（Background images）](../../../topics/Web开发技术/css-properties-margin-bg.md)

### 简答 3

题干：(Review Questions 3.33) Which has higher precedence, an id selector or a universal selector (*)?

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

知识点：[CSS属性：文本对齐（Alignment of text）](../../../topics/Web开发技术/css-properties-text.md)、[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)、[div和span标签在CSS中的应用](../../../topics/Web开发技术/css-div-span.md)
