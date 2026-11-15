---
title: 《Web技术（双语）》第三单元 CSS 样式表作业（七）
kind: 习题
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A7.pdf
---

# 《Web技术（双语）》第三单元 CSS 样式表作业（七）

原件经识别和整理；“参考解答”是我们补的。

### 词汇 1

请写出下列专业词汇对应的中文。

| 词汇 | 中文 |
| --- | --- |
| order | |
| degree | |
| decoration | |
| spacing | |
| alignment | |
| predefined | |
| border | |
| padding | |
| margin | |
| sorting | |

参考解答：| 词汇 | 中文 |
| --- | --- |
| order | 顺序；次序 |
| degree | 程度；度；级 |
| decoration | 装饰 |
| spacing | 间距 |
| alignment | 对齐 |
| predefined | 预定义的 |
| border | 边框 |
| padding | 内边距 |
| margin | 外边距 |
| sorting | 排序 |

知识点：[CSS属性：文本对齐（Alignment of text）](../../../topics/Web开发技术/css-properties-text.md)、[CSS属性：边距（Margins）与背景图像（Background images）](../../../topics/Web开发技术/css-properties-margin-bg.md)、[PHP数组（创建、访问元素、作为函数参数、作为栈Stacks、遍历Iterating、排序Sorting）](../../../topics/Web开发技术/php-arrays.md)

### 简答 2

请观察右侧 HTML 代码在浏览器的显示效果，说明为什么两个段落会显示为红色。

参考解答：两个段落显示为红色是因为 CSS 样式通过类选择器或元素选择器将 `color` 属性设置为红色，并被这两个 `<p>` 元素继承或直接应用。

若代码中定义了如 `.red { color: red; }` 且两个段落均带有 `class="red"`，则类选择器直接匹配并应用红色；若定义为 `p { color: red; }`，则所有 `<p>` 元素默认继承该样式。其他颜色未生效的原因可能是：内联样式缺失、ID 选择器未绑定到这两个段落，或更高优先级的样式被当前规则覆盖（如类选择器优先级高于元素选择器但低于内联样式，而此处无更高优先级规则存在）。

知识点：[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)、[样式表的三个级别（内联级Inline、文档级Document、外部External）](../../../topics/Web开发技术/style-levels.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)

### 综合 3

(Exercise 3.6) Create and test an HTML document that describes nested ordered lists of cars. The outer list must have three entries: compact, midsize, and sports. Inside each of these three lists there must be two sublists of body styles. The compact- and midsize-car sublists are two door and four door; the sports-car sublists are coupe and convertible. Each body-style sublist must have at least three entries, each of which is the make and model of a particular car that fits the category. The outer list must use uppercase Roman numerals, the middle lists must use uppercase letters, and the inner lists must use Arabic numerals. The background color for the compact-car list must be pink; for the midsize-car list, it must be blue; for the sports-car list, it must be red. All the styles must be in a document style sheet.

参考解答：## 结论

可使用三个嵌套层级的 `<ol>`，并通过外层 `<ol>` 的 `type` 属性分别设置列表编号格式：

- 外层：大写罗马数字 `I`
- 中层：大写英文字母 `A`
- 内层：阿拉伯数字 `1`

外层三个列表项分别设置不同的背景色，并在文档样式表中统一定义样式。

## 参考实现

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Nested Ordered Lists of Cars</title>

  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.5;
    }

    ol {
      margin-top: 0.5em;
      margin-bottom: 0.5em;
    }

    /* 外层：I、II、III */
    .car-types {
      list-style-type: upper-roman;
    }

    /* 中层：A、B、C…… */
    .body-styles {
      list-style-type: upper-alpha;
    }

    /* 内层：1、2、3…… */
    .car-models {
      list-style-type: decimal;
    }

    .compact {
      background-color: pink;
    }

    .midsize {
      background-color: blue;
    }

    .sports {
      background-color: red;
    }
  </style>
</head>

<body>
  <h1>Cars by Type and Body Style</h1>

  <ol class="car-types">
    <li class="compact">
      Compact
      <ol class="body-styles">
        <li>
          Two Door
          <ol class="car-models">
            <li>Honda Civic</li>
            <li>Toyota Corolla</li>
            <li>Volkswagen Golf</li>
          </ol>
        </li>
        <li>
          Four Door
          <ol class="car-models">
            <li>Honda Accord</li>
            <li>Toyota Camry</li>
            <li>Nissan Sentra</li>
          </ol>
        </li>
      </ol>
    </li>

    <li class="midsize">
      Midsize
      <ol class="body-styles">
        <li>
          Two Door
          <ol class="car-models">
            <li>Ford Mustang</li>
            <li>Chevrolet Camaro</li>
            <li>Nissan Altima</li>
          </ol>
        </li>
        <li>
          Four Door
          <ol class="car-models">
            <li>Honda Accord</li>
            <li>Toyota Camry</li>
            <li>Chevrolet Malibu</li>
          </ol>
        </li>
      </ol>
    </li>

    <li class="sports">
      Sports
      <ol class="body-styles">
        <li>
          Coupe
          <ol class="car-models">
            <li>Ferrari 488</li>
            <li>Porsche 911</li>
            <li>Chevrolet Corvette</li>
          </ol>
        </li>
        <li>
          Convertible
          <ol class="car-models">
            <li>Ford Mustang Convertible</li>
            <li>Porsche 718 Spyder</li>
            <li>BMW 4 Series Convertible</li>
          </ol>
        </li>
      </ol>
    </li>
  </ol>
</body>
</html>
```

## 核对与测试

1. 外层列表包含三个项目：`Compact`、`Midsize`、`Sports`。
2. 每个外层项目包含两个车身样式子列表：
   - Compact：Two Door、Four Door
   - Midsize：Two Door、Four Door
   - Sports：Coupe、Convertible
3. 每个车身样式列表都包含至少三款具体车型。
4. 编号格式分别为：
   - 外层：`I`、`II`、`III`
   - 中层：`A`、`B`……
   - 内层：`1`、`2`、`3`……
5. 背景色分别为：
   - Compact：`pink`
   - Midsize：`blue`
   - Sports：`red`
6. 所有样式均定义在 `<style>` 文档样式表中。

也可以在 `<ol>` 元素上直接使用 `type` 属性，例如：

```html
<ol type="I">
<ol type="A">
<ol type="1">
```

不过，将这些规则集中定义在文档样式表中更符合题目要求。

知识点：[列表（无序列表、有序列表、定义列表）](../../../topics/Web开发技术/lists.md)、[样式表的三个级别（内联级Inline、文档级Document、外部External）](../../../topics/Web开发技术/style-levels.md)、[CSS属性：边距（Margins）与背景图像（Background images）](../../../topics/Web开发技术/css-properties-margin-bg.md)

### 简答 4

This Is A Sentence. 请问该样式对应 `text-transform` 样式属性的哪个选项？

参考解答：`capitalize`

**推理**：`text-transform: capitalize` 会将每个单词的首字母转为大写，其余字母保持原样。句子 “This Is A Sentence.” 中每个单词首字母均大写，符合该效果。其他选项如 `uppercase` 会将所有字母全大写，`lowercase` 则全小写，均不匹配。

知识点：[CSS属性：文本对齐（Alignment of text）](../../../topics/Web开发技术/css-properties-text.md)

### 填空 5

很多样式属性的值都需要用到单位，例如字体大小是多少 px、多少 em 等。请写出 1 inch 等于多少 picas(pc)，多少 points(pt)，多少 pixels(px)？

参考解答：**结论**

$$
1\ \text{inch} = 6\ \text{pc} = 72\ \text{pt} = 96\ \text{px}
$$

**推理过程**

- 1 pica（pc）定义为 12 points（pt），而 1 inch 等于 72 pt，因此：

$$
1\ \text{inch} = \frac{72}{12} = 6\ \text{pc}
$$

- CSS 规范中规定，1 inch 固定等于 96 pixels（px），与设备实际物理 DPI 无关。

知识点：[CSS属性：字体属性（Font Properties）](../../../topics/Web开发技术/css-properties-font.md)

### 简答 6

请问下面的代码为什么要定义两个外部样式表，它们的作用是什么？

参考解答：**结论**

定义两个外部样式表通常是为了实现**关注点分离（Separation of Concerns）**，具体是将**布局结构（Layout）**与**视觉表现（Presentation/Theme）**解耦。

**推理与分析**

1.  **第一个样式表（通常为 `layout.css` 或 `base.css`）：**
    *   **作用**：负责页面的宏观结构和定位。
    *   **内容**：包含盒模型设置、网格系统（Grid/Flexbox）、响应式断点、主要区域的位置等。
    *   **目的**：确保页面在不同屏幕尺寸下的结构稳定性和可用性，不随主题变化而改变。

2.  **第二个样式表（通常为 `theme.css` 或 `style.css`）：**
    *   **作用**：负责页面的视觉装饰和品牌风格。
    *   **内容**：包含颜色（colors）、字体（fonts）、边框样式、背景图片、阴影等。
    *   **目的**：便于快速切换皮肤（Skinning）或维护品牌一致性。修改此文件不会影响页面布局结构。

**优势总结**

*   **可维护性**：开发者可以独立修改布局或主题，互不干扰。
*   **复用性**：同一套布局样式表可以被多个不同主题的项目复用；同一套主题样式表也可以应用于不同的布局结构。
*   **缓存优化**：当仅更新网站配色时，用户浏览器只需重新下载较小的主题 CSS 文件，而无需重新下载未变动的布局 CSS 文件。

知识点：[样式表的三个级别（内联级Inline、文档级Document、外部External）](../../../topics/Web开发技术/style-levels.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)

### 综合 7

请写出下图所示表格的 HTML 代码和样式表规则。

参考解答：由于题目未提供原图，以下给出一个**典型“综合 7”表格**的参考实现：假设要求表格宽 `300px`、居中、边框为 `1px solid black`、单元格之间**无间隙**（即边框合并），且**标题行**与**第一列**均水平居中。

```html
<table class="mytable">
  <tr>
    <th>Header 1</th>
    <th>Header 2</th>
  </tr>
  <tr>
    <th>Row 1 Head</th>
    <td>Data 1</td>
  </tr>
  <tr>
    <th>Row 2 Head</th>
    <td>Data 2</td>
  </tr>
</table>
```

```css
.mytable {
  width: 300px;
  margin: 0 auto;              /* 表格居中 */
  border: 1px solid black;     /* 外边框 */
  border-collapse: collapse;   /* 边框合并、去除单元格间隙 */
}

.mytable th,
.mytable td {
  border: 1px solid black;     /* 单元格边框 */
  padding: 4px 8px;            /* 内容与边框的间距 */
}

.mytable th {
  text-align: center;          /* 标题行与第一列表头居中 */
}
```

要点说明：
- 用 `border-collapse: collapse` 才能得到“单线边框、无间隙”的常见考试表格效果。
- 用 `margin: 0 auto` 实现表格整体居中。
- 第一列若是行标题应使用 `<th>`，默认加粗并配合上述规则居中。

知识点：[表格（基本标签、rowspan与colspan、表格分块、align与valign）](../../../topics/Web开发技术/tables.md)、[CSS简介与作用](../../../topics/Web开发技术/css-intro.md)、[样式表的三个级别（内联级Inline、文档级Document、外部External）](../../../topics/Web开发技术/style-levels.md)
