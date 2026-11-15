---
title: HTML5新增元素（如canvas等）
requires: [Web开发技术/html-evolution]
---

# HTML5新增元素（如canvas等）

## 为什么需要 HTML5 新元素

XHTML 早期页面主要依赖 `<div>`、`<span>` 和 `<table>` 组织内容，但 `<div id="header">` 只能表达“一个容器”，不能表达“页眉”；绘图、音视频也往往需要 Flash 等插件。HTML5 的思路是：**结构用语义元素表达，媒体用原生元素嵌入，动态图形用 JavaScript 绘制**。

> [!IMPORTANT]
> HTML5 新元素不是单纯换了标签名，而是让浏览器理解页面结构与媒体内容。==`<canvas>` 只提供画布，真正绘图依靠 JavaScript。==

## 常用新增元素

| 类别 | 代表元素 | 主要作用 |
|---|---|---|
| 语义结构 | `<header>`、`<nav>`、`<section>`、`<article>`、`<aside>`、`<footer>` | 描述页眉、导航、章节、独立内容、侧栏和页脚 |
| 原生媒体 | `<audio>`、`<video>` | 不依赖插件播放音频、视频 |
| 图形绘制 | `<canvas>` | 通过脚本绘制图形、动画和游戏画面 |
| 表单增强 | 新的 `input` 类型及属性 | 提供日期、邮箱等输入与校验能力 |

语义结构可写为：

```html
<article>
  <header><h1>Web 技术</h1></header>
  <section><p>HTML5 新增元素。</p></section>
  <footer>南京邮电大学</footer>
</article>
```

其中 `<section>` 表示文档中的主题分区，通常应有标题；`<article>` 表示可独立分发、仍具有完整意义的内容。==只是需要布局或样式容器时，仍应使用 `<div>`，不要为“显得语义化”而乱套新标签。==

## canvas 怎么用

使用 `<canvas>` 要经历“放置画布—取得元素—获取上下文—调用接口绘图”四步：

```mermaid
flowchart LR
    A["放置 canvas"] --> B["取得元素"]
    B --> C["获取 2D 上下文"]
    C --> D["调用接口绘图"]
```

下面是一个完整且结果正确的例子，它在画布上绘制一个 $100\times60$ 的蓝色矩形：

```html
<canvas id="demo" width="300" height="150">
  浏览器不支持 canvas。
</canvas>
<script>
  const canvas = document.getElementById("demo");
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "blue";
  ctx.fillRect(20, 30, 100, 60);
</script>
```

`fillRect(x, y, width, height)` 的前两个参数是左上角坐标，后两个是宽和高，因此矩形范围为 $x\in[20,120]$、$y\in[30,90]$，没有超出画布。

> [!WARNING]
> `width`、`height` 设置的是==绘图坐标空间==，CSS 的宽高设置的是显示尺寸。只用 CSS 拉伸画布，可能造成模糊或比例失真；也不要把结束标签写成自闭合形式。

## 与相近技术的区别

| 技术 | 内容形态 | 典型特点 |
|---|---|---|
| `<canvas>` | 位图 | 逐像素绘制，适合高频动画、游戏 |
| SVG | 矢量图 | 图形是 DOM 对象，缩放清晰，便于单独绑定事件 |
| `<img>` | 展示已有图片 | 本身不是实时绘图接口 |
| `<div>` | 通用容器 | 无语义，不等于 `<section>` |

`<canvas>` 与 SVG 都可画图，但并非同一技术：前者重绘方便，后者保留图形对象。若只是显示一张现成图片，优先用 `<img>`，没有必要使用画布。

> [!TIP]
> 记忆主线：==语义标签管结构，媒体标签管播放，canvas 管脚本绘图==。答题时写出“元素作用 + 必要属性或 API + 与旧方式的区别”，比只罗列标签更完整。
