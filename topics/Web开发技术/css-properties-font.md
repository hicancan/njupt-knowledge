---
title: CSS属性：字体属性（Font Properties）
requires: [Web开发技术/css-selectors]
---

# CSS属性：字体属性（Font Properties）

## 什么是字体属性

字体属性（Font Properties）用于控制网页文本的字体系列、粗细、倾斜、字号及行高，是 CSS 中最常用的文本排版属性之一。常见属性如下：

| 属性 | 作用 | 常用值 |
|---|---|---|
| `font-family` | 指定字体类别 | `"Microsoft YaHei"`, `serif`, `sans-serif` |
| `font-size` | 设置字号 | `16px`, `1.2em`, `120%` |
| `font-style` | 设置字体样式 | `normal`, `italic`, `oblique` |
| `font-weight` | 设置字体粗细 | `normal`, `bold`, `100`～`900` |
| `font-variant` | 控制小型大写等特殊字形 | `normal`, `small-caps` |
| `line-height` | 设置行高 | `normal`, `1.5`, `24px` |
| `font` | 字体属性的简写 | `italic bold 1.2em/1.5 Arial` |

> [!IMPORTANT]
> 字体属性既可以用独立属性设置，也可以使用 `font` 简写属性一次设置多个字体特征。

## 为什么需要字体属性

浏览器默认字体不一定适合所有页面。如果不进行设置，同一段文字在标题、正文和注释中可能难以区分，也难以保证不同系统上的显示效果。字体属性可以让网页：

- 建立清晰的标题、正文和辅助文字层次；
- 提高阅读体验与可访问性；
- 统一不同浏览器和操作系统中的排版效果；
- 通过相对字号适应用户自定义的默认字体大小。

例如，正文使用 `16px`，标题使用 `1.5em`。当用户增大浏览器默认字号时，基于 `em` 的标题也会随之变化。

## 如何设置字体属性

```css
body {
  font-family: "Microsoft YaHei", Arial, sans-serif;
  font-size: 16px;
  font-weight: normal;
  font-style: normal;
  line-height: 1.6;
}

h1 {
  font-size: 1.5em;
  font-weight: bold;
}

.note {
  font-style: italic;
  font-size: 0.8em;
}
```

`font-family` 通常列出多种字体。浏览器会按从左到右的顺序选择可用字体；如果都不存在，就使用通用类别 `serif`、`sans-serif` 或 `monospace`。这种写法能够减少不同系统造成的显示差异。

也可以使用 `font` 简写：

```css
.note {
  font: italic bold 0.8em/1.5 Arial, sans-serif;
}
```

其基本顺序为：

```text
font-style font-variant font-weight font-size/line-height font-family
```

其中字号和字体名称是必填项，其他项目可以省略。

> [!TIP]
> 记忆顺序：先说“样子和粗细”，再说“多大”，最后说“用哪种字体”。

## 字号与字体样式

字号既可以使用 `px`、`pt` 等绝对单位，也可以使用 `em`、`rem` 等相对单位。`em` 相对于元素继承到的字号计算：

```css
.strong {
  font-size: 2em;
}
```

如果父元素字号是 `16px`，则该元素的字号为 $16 \times 2 = 32\text{px}$。若在元素自身的 `font-size` 规则中再次使用 `em`，它仍以继承得到的字号为基准，而不是以该规则中刚设置的新字号为基准。

`font-style: italic` 表示使用斜体；`font-weight: bold` 表示粗体。若所选字体没有对应字形，浏览器可能进行合成处理，因此“有斜体样式”和“该字体原生包含斜体字形”并不完全相同。

## 相近概念的区别

| 概念 | 控制内容 | 典型属性 |
|---|---|---|
| 字体属性 | 字形、粗细、倾斜、字号 | `font-family`、`font-size` |
| 文本属性 | 对齐、缩进、装饰、空白 | `text-align`、`text-indent` |
| 颜色与背景 | 文字颜色和背景效果 | `color`、`background-color` |
| 列表属性 | 列表标记与编号样式 | `list-style-type` |

`font-style` 控制字形是否倾斜，而 `text-decoration` 控制文字是否带下划线、上划线或删除线，两者不能混用。

## 常见易错点

> [!WARNING]
> `font` 简写会重置未写出的字体子属性。设置 `font` 时若遗漏 `font-size` 或 `font-family`，整条声明可能无效。

其他常见错误包括：

1. 把字体名称写成 CSS 变量形式，例如 `font-family: ${fontName};`。正确写法应为 `font-family: var(--font-name);`。
2. 字体名称包含空格时未加引号，如 `font-family: Microsoft YaHei;`。应写成 `"Microsoft YaHei"`。
3. 认为 `italic` 等于 `<i>`。`<i>` 是语义标签，斜体效果由 CSS 的 `font-style` 决定。
4. 固定使用 `pt` 导致文字不能随用户字号设置同步变化。`pt` 是绝对单位，而 `em`、`rem` 更有利于可访问性。

## 计算正确的例子

下面的页面在左侧放置一个小文本框，正文围绕它浮动。嵌入文字同时使用较小字号和斜体：

```html
<div class="sidebar">
  This note uses a smaller font and italic style.
</div>

<div class="main-content">
  <h1>Main Text</h1>
  <p>Main text flows around the embedded box.</p>
</div>
```

```css
.sidebar {
  float: left;
  width: 200px;
  margin-right: 12px;
  padding: 10px;
  font-family: Georgia, serif;
  font-size: 0.8em;
  font-style: italic;
  line-height: 1.4;
}

.main-content {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
}
```

若 `.main-content` 的字号为 `16px`，则侧栏继承或计算出的字号若以该值为基准，就是 $16 \times 0.8 = 12.8\text{px}$。页面效果同时体现了字体属性的三个要点：字体类别、相对字号和斜体样式。
