---
title: CSS属性：边距（Margins）与背景图像（Background images）
requires: [Web开发技术/css-selectors]
---

# CSS属性：边距（Margins）与背景图像（Background images）

我们在写《Web技术（双语）》第3章的表格样式时，常把表格画得很挤：字全贴在格线上、看不出哪行是标题行。怎么让表格“透气”且专业？关键就在两个CSS属性：边距（Margins）与背景图像（Background images / 背景色）。

## 它是什么

边距用来控制元素外缘和相邻元素之间的距离；背景则铺在元素内容后面。课件里写 Hypermedia 不只是文字，还有 images、sound；同时还要考虑“Browsers with images turned off”——背景图只是装饰，真正内容必须在 HTML 里。

| 属性 | 作用位置 | 双语关键词 |
| --- | --- | --- |
| margin | 边框外空隙 | margin / 边距 |
| padding | 边框内空隙 | padding / 内边距 |
| background-color | 背景色 | background color |
| background-image | 背景图 | background image |

> [!WARNING]
> 边距和 padding 不是一回事：==margin 是元素外空白，padding 是内容和边框之间空白==，考题让你“左右留边”通常指 margin。

## 为什么需要

没有边距，表格单元格文字会紧贴线框；没有背景色，表头行（如 Top Three Performers）和 Total 行难以区分。课件 3.10.2 讲 Margins、3.11 讲 Background images，就是教我们通过留白和背景提升可读性，即使图片关闭，背景色仍可由 CSS 提供视觉分层。

## 怎么做（算对了的例子）

看考过的简答 8：表格含标题“Test Results”、表头行、三行成绩与汇总行。HTML 用 `table / caption / tr / td`，CSS 给 table 设边框、给 caption 与 total 行设背景和 margin。

```html
<table class="tbl">
  <caption>Test Results</caption>
  <tr><td colspan="4">Top Three Performers</td></tr>
  <tr><td>Name</td><td>Login ID</td><td>Course Name</td><td>Marks</td></tr>
  <tr><td>Joseph</td><td>01236</td><td>MySQL...</td><td>98</td></tr>
  <tr class="total"><td colspan="3">Total number of students</td><td>3</td></tr>
</table>
```

```css
.tbl {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 10px;              /* 表格外边距 */
}
.tbl td {
  border: 1px solid #333;
  padding: 4px;              /* 单元格内边距，别写成 margin */
}
.tbl caption {
  margin-bottom: 6px;        /* 标题下方留空 */
  font-weight: bold;
}
.total {
  background-color: #eee;    /* 总行背景，图片关也可见 */
}
```

> [!TIP]
> 记忆：`border-collapse: collapse` 先合并边框；再用 `padding` 把字推离线，`margin` 把整块推开。

## 相近概念与常见坑

课件 Review 3.21 还考过图像浮动：`float: left` 让文本绕到图右侧。这和背景不同——背景图在元素之下，而 `<img>` 是替换元素、可被浮动。另一个练习（Exercise 3.5）要求 p1 左右 margin 20px、背景粉前景蓝，说明背景色与前景色 `color` 要同时给，且图片关闭时不依赖 `background-image`。

下面用一张图理清盒子关系：

```mermaid
flowchart LR
  A["margin 外边距"] --> B["border 边框"]
  B --> C["padding 内边距"]
  C --> D["content 内容"]
  D --> E["background 底层"]
```

> [!IMPORTANT]
> 核心写法：==表格先用 padding 撑开格子，再用 margin 拉开整体，用 background-color 做不可丢失的背景层==。

> [!CAUTION]
> 高危误区：把单元格留白写成 `margin` 却看不到线框移动；或只写 `background-image` 不给 fallback 背景色，在关闭图片浏览器中一片空白。
