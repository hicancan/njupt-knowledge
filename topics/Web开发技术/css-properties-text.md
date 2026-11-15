---
title: CSS属性：文本对齐（Alignment of text）
requires: [Web开发技术/css-selectors]
---

# CSS属性：文本对齐（Alignment of text）

## 文本对齐是什么

CSS 中的文本对齐（Alignment of text）用于控制文字或行内内容在容器中的位置。它并不改变文字内容，而是改变其排版方式。例如，段落可以左对齐、居中或两端对齐，图片与相邻文字也可以在垂直方向上对齐。

本知识点主要涉及两个属性：

- `text-align`：控制块级元素内部内容的**水平对齐**。
- `vertical-align`：控制行内元素或表格单元格内容的**垂直对齐**。

## 水平对齐：text-align

常见取值如下：

| 属性值 | 效果 | 典型用途 |
| --- | --- | --- |
| `left` | 左对齐 | 英文正文，通常为默认值 |
| `right` | 右对齐 | 数字、日期或辅助信息 |
| `center` | 居中对齐 | 标题、提示语 |
| `justify` | 两端对齐 | 多行正式正文 |

例如：

```css
h1 {
    text-align: center;
}

p {
    text-align: justify;
}
```

`text-align` 设置在**父元素**上，影响的是父元素内部的行内内容，而不是简单地把父元素自身移到页面中央。若要让一个固定宽度的块级元素整体水平居中，通常使用：

```css
.box {
    width: 600px;
    margin-left: auto;
    margin-right: auto;
}
```

> [!IMPORTANT]
> ==`text-align: center` 是内容居中，`margin: auto` 常用于块级盒子自身居中==，两者不要混淆。

## 垂直对齐：vertical-align

`vertical-align` 常用于图片、行内元素以及表格单元格，常见取值包括：

| 属性值 | 对齐位置 |
| --- | --- |
| `baseline` | 按基线对齐，通常为默认值 |
| `top` | 顶部对齐 |
| `middle` | 中部对齐 |
| `bottom` | 底部对齐 |
| `text-top` | 与父元素文本顶部对齐 |
| `text-bottom` | 与父元素文本底部对齐 |

例如，要使图片与旁边的文字在垂直方向上居中，可写为：

```html
<div class="container">
    <img src="example.jpg" alt="Example" class="pic">
    <span class="words">Aligned text</span>
</div>
```

```css
.pic {
    width: 50px;
    height: 50px;
    vertical-align: middle;
}

.words {
    font-size: 16px;
    vertical-align: middle;
}
```

这里图片和文字都是行内内容，分别设置 `vertical-align: middle`，可避免图片按默认基线放置而产生视觉偏移。

## 相近概念与常见误区

文本对齐还可能与下列属性同时出现，但作用不同：

| 属性 | 控制内容 |
| --- | --- |
| `text-align` | 水平对齐 |
| `vertical-align` | 行内内容或单元格的垂直对齐 |
| `text-indent` | 首行缩进 |
| `line-height` | 行高，可间接影响单行文字的垂直位置 |
| HTML 的 `align`、`valign` | 早期表格对齐属性，现代页面宜改用 CSS |

> [!WARNING]
> `vertical-align` ==通常不能直接把普通块级元素内部的文字垂直居中==。它主要适用于行内级元素和表格单元格；若处理弹性布局，可考虑 `align-items`，不要机械套用。

另一个易混点是 `text-transform`。例如把文本显示为 `This Is A Sentence.`，对应：

```css
p {
    text-transform: capitalize;
}
```

它表示将各单词首字母大写，属于**大小写转换**，并不属于对齐。专业词汇中，`alignment` 意为“对齐”，`vertical-align` 即“垂直对齐”。
