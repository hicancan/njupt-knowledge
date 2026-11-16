---
title: 《Web技术（双语）》第二单元 HTML 入门（第一部分）作业答案
kind: 答案
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A2.pdf
---

# 《Web技术（双语）》第二单元 HTML 入门（第一部分）作业答案

原件经识别和整理；“参考解答”是我们补的。

## 一、专业词汇翻译

### 选择 1

请将下列专业词汇对应的中文写出：

- syntax
- tag
- element
- content
- comment
- line break
- character
- paragraph
- quotation
- subscript
- superscript

答案：
- syntax：语法
- tag：标签
- element：元素
- content：内容
- comment：注释
- line break：换行
- character：字符
- paragraph：段落
- quotation：引用
- subscript：下标
- superscript：上标

## 二、HTML元素与内容分析

知识点：[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[XHTML基本语法规则与大小写敏感性](../../../topics/Web开发技术/xhtml-syntax.md)

### 简答 1

请观察下面的HTML代码，写出其中所有的元素（用标签命名该元素）以及该元素的内容。

*注：原题中提供了HTML代码图片，但识别文本中未包含具体代码内容，仅保留了填写表格的结构。根据题目要求，需对具体HTML代码进行分析。由于缺乏原始代码数据，此处无法提供具体的元素和内容列表。在实际操作中，应参照原图代码进行填写。*

| 元素 | 内容 |
| :--- | :--- |
| (需根据原图代码填写) | (需根据原图代码填写) |
| (需根据原图代码填写) | (需根据原图代码填写) |
| (需根据原图代码填写) | (需根据原图代码填写) |
| (需根据原图代码填写) | (需根据原图代码填写) |

答案：待补充（需依据原图代码）

## 三、HTML代码编写

知识点：[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)、[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)

### 简答 2

请根据下图写出对应的HTML代码。

![图 3](Web技术（双语）.assets/figure_6a756fa0dc95af8f340de994e9fd3e53695e7143fc7c561f31f5f391ed6f283d.jpg)

答案：待补充（需依据原图视觉内容编写HTML代码）

## 四、复习问答

知识点：[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)、[列表（无序列表、有序列表、定义列表）](../../../topics/Web开发技术/lists.md)

### 简答 3

**问题：** （REVIEW QUESTIONS 2.1）WHAT DOES IT MEAN FOR A TAG OR AN ATTRIBUTE OF HTML TO BE DEPRECATED? 除了写出答案外，请标注它在书上的页码。

答案：
Deprecated（过时/废弃）意味着该标签或属性虽然目前可能仍被浏览器支持以兼容旧网页，但不推荐在新开发中使用。它可能在未来的HTML版本中被移除，通常有更现代、更语义化或功能更强的替代方案。

*注：页码需参考指定教材。*

知识点：[HTML的起源与演进（HTML到XHTML/HTML5）](../../../topics/Web开发技术/html-evolution.md)

### 简答 4

**问题：** （REVIEW QUESTIONS 2.3）HOW DOES A BROWSER TREAT LINEBREAKS IN TEXT THAT IS TO BE DISPLAYED?

答案：
浏览器在显示文本时，通常会忽略源代码中的单个换行符和空格，将它们视为一个空格处理。除非使用了`<pre>`标签或CSS样式强制保留空白，否则连续的空白字符（包括换行）会被合并为一个空格。

知识点：[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)

### 简答 5

**问题：** （REVIEW QUESTIONS 2.5）WHICH HEADING ELEMENTS USE FONTS THAT ARE SMALLER THAN THE NORMAL TEXT FONT SIZE?

答案：
在HTML中，`<h1>`到`<h6>`是标题元素。通常情况下，`<h1>`字体最大，`<h6>`字体最小。标准的“正常文本”字体大小通常对应于`<p>`标签默认的大小或`<h6>`的大小。因此，严格来说，所有标准标题元素（`<h1>`至`<h6>`）的字体大小都是由浏览器默认样式定义的，其中`<h6>`是最小的。如果“正常文本”指的是正文默认大小（如16px），那么`<h6>`（通常约1em或稍小）可能与之相近或略小，而其他标题（`<h1>`-`<h5>`）都更大。但在某些上下文或特定浏览器默认样式中，如果没有特别定义，`<h6>`可能是最接近或略小于常规正文大小的标题元素。然而，通常认为标题都比正文大。若题目暗示有比正常文本小的标题，这可能是一个陷阱题或基于特定假设。通常回答：没有标准HTML标题元素的默认字体大小小于正常正文文本；相反，它们都更大。但如果必须指出最小的标题，则是`<h6>`。

*注：此答案基于通用HTML规范，具体可能因浏览器或教材定义略有差异。*

知识点：[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)

### 简答 6

**问题：** CREATE AND TEST AN HTML DOCUMENT FOR YOURSELF, INCLUDING YOUR NAME, ADDRESS, AND ELECTRONIC MAIL ADDRESS. YOU MUST INCLUDE YOUR MAJOR AND YOUR GRADE LEVEL. THIS DOCUMENT MUST USE SEVERAL HEADINGS AND `<EM>`, `<STRONG>`, `<HR />`, `<P>`, AND `<BR />` TAGS. 请写下 HTML 代码。注意缩进和对齐。

答案：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>My Personal Information</title>
</head>
<body>

    <h1>About Me</h1>

    <h2>Name</h2>
    <p><strong>Name:</strong> John Doe</p>

    <h2>Contact Information</h2>
    <p>
        <strong>Address:</strong><br>
        123 Main Street<br>
        City, State, Zip Code
    </p>

    <p><strong>Email:</strong> <em>johndoe@example.com</em></p>

    <hr />

    <h2>Academic Background</h2>
    <p><strong>Major:</strong> Computer Science</p>
    <p><strong>Grade Level:</strong> Junior</p>

</body>
</html>
```

知识点：[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)
