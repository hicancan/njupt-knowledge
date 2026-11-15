---
title: 《Web技术（双语）》作业4
kind: 习题
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A4.pdf
---

# 《Web技术（双语）》作业4

原件经识别和整理；“参考解答”是我们补的。

### 第二单元 INTRODUCTION TO HTML（PART III）

| 学号 | | 提交截止日期 | 2019年3月22日(第五周周五) |
| :--- | :--- | :--- | :--- |
| 姓名 | | 提交地址 | http://xzc.cn/18Q8Jfcoq8E |

参考解答：# 第二单元 INTRODUCTION TO HTML（PART III）参考解答

## 一、选择题

1. **答案：B**  
   `<a>` 是超链接标签，`href` 指定目标地址；`<link>` 用于关联外部资源，`<hyperlink>` 和 `<url>` 均不是 HTML 标签。

2. **答案：C**  
   `target="_blank"` 会在新窗口或新标签页打开链接；`_self` 在当前页面打开，`_parent` 和 `_top` 用于框架环境。

3. **答案：A**  
   邮件链接使用 `mailto:` 协议；`email:`、`mail:` 不是标准写法，`href="#"` 只表示空链接。

4. **答案：D**  
   页面内跳转需要目标元素的 `id` 与链接的 `href="#id"` 对应；`name` 不是现代 HTML 中推荐的目标定位方式。

5. **答案：B**  
   `<img>` 的 `src` 指定图片地址，`alt` 提供替代文本；`href` 用于链接，`title` 通常提供提示信息，`link` 不是图片地址属性。

6. **答案：C**  
   `alt` 在图片无法显示时提供替代文本，也有助于无障碍访问；它不会代替 `src` 加载图片，也不主要用于控制图片尺寸。

7. **答案：A**  
   无序列表使用 `<ul>`，列表项使用 `<li>`；`<ol>` 表示有序列表，`<dl>` 表示描述列表。

8. **答案：B**  
   有序列表使用 `<ol>`，默认通常以数字编号；`<ul>` 不保证编号顺序，`<list>` 不是标准 HTML 标签。

9. **答案：D**  
   `type="A"` 可让有序列表使用大写字母编号；`start` 指定起始值，`value` 可指定某个列表项的编号，`reversed` 表示倒序编号。

10. **答案：C**  
    表格行使用 `<tr>`，标准数据单元格使用 `<td>`；`<th>` 表示表头单元格，`<table>` 是整个表格的容器。

11. **答案：B**  
    `<th>` 表示表头单元格，浏览器通常加粗并居中显示；`<td>` 是普通数据单元格，`<thead>` 是表头区域容器。

12. **答案：A**  
    `colspan` 表示单元格横跨的列数，`rowspan` 表示横跨的行数；二者不能混用，也不是通过 `width` 设置跨列。

13. **答案：D**  
    表单使用 `<form>`，常见控件通过 `<input>` 创建；`<button>` 可创建按钮，`<forminput>` 不是标准标签。

14. **答案：C**  
    `type="text"` 创建单行文本框，`type="password"` 创建密码框；密码框会隐藏输入内容，但不等于对数据进行加密。

15. **答案：B**  
    单选按钮使用 `type="radio"`，同一组通常设置相同的 `name`；`checkbox` 可多选，`text` 和 `option` 不用于创建单选按钮。

16. **答案：A**  
    多选框使用 `type="checkbox"`；`radio` 通常用于一组选项中的单选，`select` 是下拉选择控件。

17. **答案：D**  
    下拉列表由 `<select>` 和 `<option>` 组成；`<input list>` 可关联数据列表，但不等同于普通的 `<select>` 结构。

18. **答案：C**  
    `method="post"` 通常将表单数据放在请求体中提交，适合提交较多或敏感数据；`get` 通常将数据附加在 URL 中，但不代表 `post` 自动完成安全加密。

19. **答案：B**  
    `<label>` 的 `for` 属性应与控件的 `id` 对应；`name` 主要用于表单数据提交，`value` 表示控件值。

20. **答案：A**  
    HTML5 的 `<audio>` 用于嵌入音频，`<video>` 用于嵌入视频；`controls` 用于显示播放控制条，`autoplay` 是否生效还可能受浏览器策略限制。

## 二、填空题

1. **`<a>`；`href`**  
   超链接由 `<a>` 创建，目标地址通常写在 `href` 属性中。

2. **`_blank`**  
   `target="_blank"` 表示在新的浏览上下文，通常是新标签页或新窗口中打开链接。

3. **`src`；`alt`**  
   `src` 指定图片资源位置，`alt` 提供图片无法显示时的替代文本。

4. **`<ul>`；`<ol>`；`<li>`**  
   `<ul>` 创建无序列表，`<ol>` 创建有序列表，二者都使用 `<li>` 表示列表项。

5. **`<table>`；`<tr>`；`<td>`**  
   分别表示表格、表格行和普通数据单元格；表头单元格使用 `<th>`。

6. **`colspan`；`rowspan`**  
   `colspan` 控制跨列，`rowspan` 控制跨行。

7. **`<form>`；`action`；`method`**  
   `action` 指定表单提交地址，`method` 指定常用的 HTTP 提交方式，如 `get` 或 `post`。

8. **`password`**  
   密码输入框写为 `<input type="password">`，输入内容通常以掩码形式显示。

9. **`name`**  
   同一组单选按钮使用相同的 `name`，浏览器据此将它们视为互斥的一组。

10. **`id`**  
    `<label for="username">` 应对应 `<input id="username">`，点击标签即可聚焦或激活相关控件。

## 三、判断题

1. **错误。**  
   `<img>` 是空元素，通常写成 `<img src="..." alt="...">`，不需要 `</img>`。

2. **错误。**  
   相对路径不一定表示同一目录，还可以使用 `images/a.jpg`、`../images/a.jpg` 等路径访问其他位置。

3. **正确。**  
   使用 `href="#section1"` 可以链接到当前页面中 `id="section1"` 的元素。

4. **错误。**  
   `<ul>` 是无序列表，默认通常显示项目符号；有序编号一般使用 `<ol>`。

5. **错误。**  
   `<td>` 应位于 `<tr>` 内，不能直接把任意表格内容都作为 `<table>` 的独立单元格。

6. **正确。**  
   `rowspan="2"` 表示该单元格纵向跨越两行，后续行应相应减少一个单元格。

7. **错误。**  
   未设置 `name` 的表单控件通常不会作为成功的表单字段提交；`id` 主要用于标识、标签关联和脚本操作。

8. **错误。**  
   `type="password"` 只隐藏屏幕上的输入内容，不能替代 HTTPS 等安全传输措施。

9. **正确。**  
   `<option selected>` 可将对应选项设为初始选中项；单选下拉列表中通常只应设置一个默认选项。

10. **错误。**  
    HTML 注释不会显示在页面正文中，但仍会出现在源代码里，因此不能用来保存密码等机密信息。

## 四、简答题

1. **简述绝对路径与相对路径的区别。**  
   绝对路径从完整 URL 或站点根位置确定资源，位置明确，但目录变化时可能失效；相对路径以当前文档的位置为基准，便于站点整体迁移，但移动文件后需要检查路径关系。例如，`images/logo.png` 表示当前目录下的 `images` 子目录，`../images/logo.png` 表示先返回上一级目录。

2. **说明 `alt` 属性的作用。**  
   `alt` 用于在图片加载失败、被禁用或用户使用屏幕阅读器时提供替代信息。它应简洁描述图片的内容或功能；纯装饰图片可使用空 `alt=""`，但不能简单省略关键图片的替代文本。

3. **说明 `<ul>`、`<ol>` 和 `<dl>` 的区别。**  
   `<ul>` 用于顺序不重要的事项，`<ol>` 用于步骤、排名等有顺序的内容，`<dl>` 用于术语与说明等名称—值组合。前两者使用 `<li>`，描述列表通常使用 `<dt>` 和 `<dd>`。

4. **说明表格的基本结构。**  
   `<table>` 包含若干 `<tr>`，每行包含 `<td>` 或 `<th>`。需要表达结构时，可用 `<thead>`、`<tbody>` 和 `<tfoot>` 分区；`colspan` 和 `rowspan` 分别实现跨列和跨行。

5. **比较 GET 与 POST 表单提交。**  
   GET 通常把数据编码到 URL 的查询字符串中，便于收藏和分享，适合搜索等幂等查询，但数据容易暴露在地址、历史记录和日志中。POST 通常把数据放在请求体中，适合提交较多数据或修改服务器状态；但 POST 本身不提供加密，敏感数据仍应通过 HTTPS 传输。

6. **为什么单选按钮组要设置相同的 `name`？**  
   相同的 `name` 让浏览器把多个 `radio` 识别为同一组，从而保证组内互斥。提交时，服务器接收该组名称及被选按钮的 `value`；不同按钮应保留各自可区分的 `value`。

7. **说明 `<label>` 的作用。**  
   `<label>` 为表单控件提供可访问的名称。通过 `for` 与控件的 `id` 关联后，点击标签可以聚焦或激活控件，同时扩大可点击区域，并帮助屏幕阅读器正确说明控件用途。

8. **列举 HTML5 常用的输入类型。**  
   常见类型包括 `text`、`password`、`email`、`number`、`date`、`url`、`tel`、`checkbox`、`radio`、`file` 和 `submit` 等。部分类型能提供合适的输入界面和基础校验，但服务器端仍必须重新验证数据。

## 五、代码阅读题

### 1. 链接与图片

```html
<a href="https://www.example.com" target="_blank">
  <img src="logo.png" alt="Example Logo" width="120">
</a>
```

**结论：** 页面显示一张宽为 120 像素的图片，点击图片会在新窗口或新标签页打开 `https://www.example.com`。

**推理：** `<img>` 是 `<a>` 的内容，因此整张图片成为超链接；`alt` 是图片无法显示时的替代文本，`target="_blank"` 决定链接的打开位置。

### 2. 嵌套列表

```html
<ul>
  <li>HTML</li>
  <li>CSS
    <ol>
      <li>Selectors</li>
      <li>Box Model</li>
    </ol>
  </li>
</ul>
```

**结论：** 外层是无序列表，包含 `HTML` 和 `CSS` 两项；`CSS` 下嵌套一个有序列表，依次显示 `Selectors` 和 `Box Model`。

**推理：** 内层 `<ol>` 位于第二个 `<li>` 内，所以它属于 `CSS` 项，而不是与外层并列的第三个列表项。

### 3. 跨行、跨列表格

```html
<table border="1">
  <tr>
    <th colspan="2">Student</th>
  </tr>
  <tr>
    <td rowspan="2">Alice</td>
    <td>HTML</td>
  </tr>
  <tr>
    <td>CSS</td>
  </tr>
</table>
```

**结论：** 表格逻辑上有两行两列。第一行的 `Student` 横跨两列；`Alice` 纵跨第二、三行，右侧分别显示 `HTML` 和 `CSS`。

**推理：** 第一行表头因 `colspan="2"` 占满两列；第三行左侧已被 `rowspan="2"` 的 `Alice` 占用，所以只需再写一个 `<td>`。

### 4. 表单控件

```html
<form action="/register" method="post">
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <input type="radio" id="male" name="gender" value="male">
  <label for="male">Male</label>

  <input type="radio" id="female" name="gender" value="female">
  <label for="female">Female</label>

  <input type="submit" value="Register">
</form>
```

**结论：** 表单以 POST 方式提交到 `/register`；邮箱为必填项，两个性别选项互斥，点击 `Register` 提交表单。

**推理：** `label` 通过 `for` 关联对应 `id`；两个单选按钮具有相同的 `name="gender"`，因此只能选择一个。若选择 `female`，典型提交数据包括 `email=用户输入值` 和 `gender=female`。

## 六、编程题

### 1. 创建链接和图片

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>Links and Images</title>
</head>
<body>
  <a href="https://www.example.com" target="_blank" rel="noopener">
    Visit Example
  </a>

  <img src="images/campus.jpg" alt="校园风景" width="600">
</body>
</html>
```

`href` 指定链接目标，`alt` 提供替代文本；`rel="noopener"` 用于降低新页面通过 `window.opener` 操作原页面的风险。

### 2. 创建有序列表和无序列表

```html
<h2>Web 技术学习内容</h2>
<ol>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
</ol>

<h2>开发工具</h2>
<ul>
  <li>文本编辑器</li>
  <li>浏览器</li>
  <li>开发者工具</li>
</ul>
```

学习顺序使用 `<ol>`，工具清单顺序不重要，因此使用 `<ul>`。

### 3. 创建课程表

```html
<table border="1">
  <caption>课程安排</caption>
  <thead>
    <tr>
      <th scope="col">时间</th>
      <th scope="col">星期一</th>
      <th scope="col">星期三</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">8:00—9:40</th>
      <td>Web 技术</td>
      <td>数据结构</td>
    </tr>
    <tr>
      <th scope="row">10:00—11:40</th>
      <td colspan="2">实验课</td>
    </tr>
  </tbody>
</table>
```

第二行课程的 `colspan="2"` 表示“实验课”横跨星期一和星期三两列，因此该行只写两个单元格：一个时间单元格和一个课程单元格。

### 4. 创建学生信息登记表

```html
<form action="/register" method="post">
  <p>
    <label for="student-name">姓名：</label>
    <input type="text" id="student-name" name="studentName" required>
  </p>

  <p>
    <label for="student-email">邮箱：</label>
    <input type="email" id="student-email" name="email" required>
  </p>

  <fieldset>
    <legend>性别</legend>
    <input type="radio" id="gender-male" name="gender" value="male">
    <label for="gender-male">男</label>

    <input type="radio" id="gender-female" name="gender" value="female">
    <label for="gender-female">女</label>
  </fieldset>

  <p>
    <label for="major">专业：</label>
    <select id="major" name="major">
      <option value="cs">计算机科学与技术</option>
      <option value="se">软件工程</option>
      <option value="other">其他</option>
    </select>
  </p>

  <p>
    <label for="introduction">个人简介：</label><br>
    <textarea id="introduction" name="introduction" rows="4" cols="40"></textarea>
  </p>

  <button type="submit">提交</button>
  <button type="reset">重置</button>
</form>
```

各输入控件设置 `name`，以便提交数据；单选按钮共享 `name="gender"` 实现互斥，`<label>` 通过 `for` 与对应控件的 `id` 关联。

### 5. 创建带页内导航的 HTML 页面

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <title>HTML 基础</title>
</head>
<body>
  <header>
    <h1>HTML 基础</h1>
    <nav>
      <a href="#links">链接</a> |
      <a href="#lists">列表</a> |
      <a href="#forms">表单</a>
    </nav>
  </header>

  <main>
    <section id="links">
      <h2>链接</h2>
      <p>链接使用 <code>&lt;a&gt;</code> 元素创建。</p>
    </section>

    <section id="lists">
      <h2>列表</h2>
      <p>常见列表包括无序列表和有序列表。</p>
    </section>

    <section id="forms">
      <h2>表单</h2>
      <p>表单用于收集并提交用户输入。</p>
    </section>
  </main>

  <footer>
    <a href="#top">返回顶部</a>
  </footer>
</body>
</html>
```

若使用“返回顶部”链接，应在页面根元素或顶部元素上补充 `id="top"`，例如：

```html
<body id="top">
```

知识点：[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)、[基本文本标记（段落、换行、标题、块引用、水平线、字符实体、上下标）](../../../topics/Web开发技术/text-markup.md)、[图像（img）与超文本链接（a标签、文档内部目标）](../../../topics/Web开发技术/images-links.md)

### 请写出下列专业词汇对应的中文。

| 英文词汇 | 中文含义 |
| :--- | :--- |
| label | |
| benefit | |
| advantage | |
| disadvantage | |
| choice | |
| submit | |
| reset | |

参考解答：| 英文词汇 | 中文含义 |
| :--- | :--- |
| label | 标签 |
| benefit | 益处 / 好处 |
| advantage | 优势 / 优点 |
| disadvantage | 劣势 / 缺点 |
| choice | 选择 |
| submit | 提交 |
| reset | 重置 |

这些词汇均为 Web 技术与双语课程中的基础术语：`label` 在 HTML 表单中特指与控件关联的文本标签；`benefit`、`advantage`、`disadvantage` 分别对应技术选型或方案评估时的中性收益、正面优势与负面缺陷，语义层级不同不可混用；`choice` 泛指用户或开发者的选项行为；`submit` 和 `reset` 是 HTML `<form>` 中两种标准按钮类型，分别触发数据发送与表单字段恢复初始值的功能。

知识点：[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)

### 假设开发了一个用户评论网页，如下图所示。你会使用哪种方法提交表单？

| POST A COMMENT | Mobile commenting available! Keep the conversation going. |
| :--- | :--- |
| SUBJECT | |
| MESSAGE | B I S "→" Show Formatting Guide ↓ |

- GET 方法
- POST 方法

参考解答：结论：使用 **POST 方法**。

推理：评论内容会写入服务器（新增数据），并可能包含较长文本或特殊格式，不应通过 URL 传递。GET 会把表单数据拼接在 URL 查询串中，既有长度限制又不适合写操作；POST 将数据放在请求体中，更安全且无此限制，因此选 POST。

知识点：[HTTP请求阶段（GET方法、常见请求字段）](../../../topics/Web开发技术/http-request.md)、[表单提交方法（GET与POST的选择与应用场景）](../../../topics/Web开发技术/form-submit-method.md)、[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)

### 请说明 LABEL 元素的 FOR 属性设为 INPUT 元素的 ID 有何作用？

<br>

参考解答：将 `<label>` 的 `for` 属性设为对应 `<input>` 的 `id`，可建立表单控件与标签之间的**显式关联**。

- **可访问性**：屏幕阅读器在聚焦该输入框时会朗读标签文本，帮助视障用户理解字段用途。
- **交互增强**：点击标签文本即可自动聚焦或激活对应的表单控件，扩大可点击区域。
- **语义明确**：浏览器和辅助技术能准确识别标签与控件的绑定关系，避免隐式嵌套带来的解析歧义。

知识点：[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)、[HTML文档结构（head、body、meta元素）](../../../topics/Web开发技术/html-doc-structure.md)

### 请完成下图所示表单的 HTML 代码。注意：QUANTITY 一列只能填数字。支付方法默认选中 VISA。

## Welcome to Millenium Gynmastics Booster Club Popcorn Sales

Buyer's Name: <br>
Street Address: <br>
City, State, Zip: <br>

| Product Name | Price | Quantity |
| :--- | :--- | :--- |
| Unpopped Popcorn (1 lb.) | $3.00 | |
| Caramel Popcorn (2 lb. cannister) | $3.50 | |
| Caramel Nut Popcorn (2 lb. cannister) | $4.50 | |
| Toffey Nut Popcorn (2 lb. cannister) | $5.00 | |

参考解答：## 结论

以下代码可生成与图示一致的表单：

- 使用表格展示商品、价格和数量。
- `QUANTITY` 列的输入框仅允许填写数字。
- 支付方式默认选中 `VISA`。
- 文本字段和单选按钮均设置了相应的 `name` 属性。

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Millenium Gynmastics Booster Club Popcorn Sales</title>

  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.5;
      margin: 30px;
    }

    h1 {
      text-align: center;
      font-size: 24px;
    }

    .buyer-info {
      margin-bottom: 20px;
    }

    .buyer-info label {
      display: inline-block;
      width: 140px;
    }

    table {
      border-collapse: collapse;
      width: 100%;
      max-width: 700px;
    }

    th,
    td {
      border: 1px solid #000;
      padding: 8px 12px;
      text-align: left;
    }

    th {
      background-color: #f2f2f2;
    }

    .quantity {
      width: 90px;
    }

    .payment {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Welcome to Millenium Gynmastics Booster Club Popcorn Sales</h1>

  <form>
    <div class="buyer-info">
      <div>
        <label for="buyer-name">Buyer's Name:</label>
        <input type="text" id="buyer-name" name="buyerName">
      </div>

      <div>
        <label for="street-address">Street Address:</label>
        <input type="text" id="street-address" name="streetAddress">
      </div>

      <div>
        <label for="city-state-zip">City, State, Zip:</label>
        <input type="text" id="city-state-zip" name="cityStateZip">
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th scope="col">Product Name</th>
          <th scope="col">Price</th>
          <th scope="col">Quantity</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Unpopped Popcorn (1 lb.)</td>
          <td>$3.00</td>
          <td class="quantity">
            <input
              type="number"
              name="unpoppedQuantity"
              min="0"
              step="1"
              value="0"
              inputmode="numeric"
              pattern="[0-9]*"
            >
          </td>
        </tr>
        <tr>
          <td>Caramel Popcorn (2 lb. cannister)</td>
          <td>$3.50</td>
          <td class="quantity">
            <input
              type="number"
              name="caramelQuantity"
              min="0"
              step="1"
              value="0"
              inputmode="numeric"
              pattern="[0-9]*"
            >
          </td>
        </tr>
        <tr>
          <td>Caramel Nut Popcorn (2 lb. cannister)</td>
          <td>$4.50</td>
          <td class="quantity">
            <input
              type="number"
              name="caramelNutQuantity"
              min="0"
              step="1"
              value="0"
              inputmode="numeric"
              pattern="[0-9]*"
            >
          </td>
        </tr>
        <tr>
          <td>Toffey Nut Popcorn (2 lb. cannister)</td>
          <td>$5.00</td>
          <td class="quantity">
            <input
              type="number"
              name="toffeyNutQuantity"
              min="0"
              step="1"
              value="0"
              inputmode="numeric"
              pattern="[0-9]*"
            >
          </td>
        </tr>
      </tbody>
    </table>

    <fieldset class="payment">
      <legend>Payment Method</legend>

      <label>
        <input type="radio" name="paymentMethod" value="VISA" checked>
        VISA
      </label>

      <label>
        <input type="radio" name="paymentMethod" value="MasterCard">
        MasterCard
      </label>

      <label>
        <input type="radio" name="paymentMethod" value="Discover">
        Discover
      </label>
    </fieldset>

    <button type="submit">Submit</button>
  </form>
</body>
</html>
```

其中，`type="number"` 限制数量输入为数字，`min="0"`、`step="1"` 和 `pattern="[0-9]*"` 进一步限制为非负整数；支付方式使用 `checked` 属性使 `VISA` 成为默认选项。

知识点：[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)、[表格（基本标签、rowspan与colspan、表格分块、align与valign）](../../../topics/Web开发技术/tables.md)、[表单提交方法（GET与POST的选择与应用场景）](../../../topics/Web开发技术/form-submit-method.md)

### Payment Method:

- Master Card
- Discover
- Submit Order
- Clear Order Form

参考解答：```html
**结论：**

- 支付方式单选按钮组：使用 `name="payment"` 保证互斥。
- `Master Card` 和 `Discover` 作为两个 `radio` 选项，其中 `Master Card` 可设为默认选中。
- `Submit Order` 使用 `type="submit"` 提交表单。
- `Clear Order Form` 使用 `type="reset"` 清空表单。

---

**推理与关键代码：**

表单中支付方式只能二选一，因此两个选项必须设置相同的 `name` 属性，典型写法为：

```html
<input type="radio" name="payment" value="master" checked> Master Card
<input type="radio" name="payment" value="discover"> Discover
```

`Submit Order` 用于向服务器提交表单数据，按钮类型应为：

```html
<input type="submit" value="Submit Order">
```

`Clear Order Form` 用于恢复表单初始状态，按钮类型应为：

```html
<input type="reset" value="Clear Order Form">
```

---

**选择题说明：**

- **A 正确**：`radio` 同名才能互斥；`submit` 提交表单，`reset` 清空表单，语义完全匹配。
- **B 错误**：若两个支付选项使用不同 `name`，可同时选中，不符合“支付方式”唯一性要求。
- **C 错误**：`Checkbox` 允许多选，不能保证 Master Card 与 Discover 二选一。
- **D 错误**：`type="button"` 不会提交或重置表单，需配合 JavaScript 才能实现对应功能。
```

知识点：[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)、[表单提交方法（GET与POST的选择与应用场景）](../../../topics/Web开发技术/form-submit-method.md)

### （REVIEW QUESTIONS 2.21）WHAT ARE CONTROLS?

<br>

参考解答：控件是图形用户界面（GUI）中的基本元素，如按钮、文本框、复选框等，用于用户与应用程序交互，实现数据输入、操作触发或状态显示等功能。

知识点：[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)

### （REVIEW QUESTIONS 2.25）WHAT IS THE DIFFERENCE IN BEHAVIOR BETWEEN A GROUP OF CHECKBOX BUTTONS AND A GROUP OF RADIOBUTTONS?

<br>

参考解答：**结论**

复选框（Checkboxes）允许用户在组内**多选**（独立选择），而单选按钮（Radio Buttons）强制用户在组内**互斥单选**。

**推理过程**

1.  **复选框 (`<input type="checkbox">`)**：
    *   每个复选框的状态是独立的。
    *   用户可以选中零个、一个或多个选项。
    *   再次点击已选中的框会取消选中，不影响同组其他框的状态。

2.  **单选按钮 (`<input type="radio">`)**：
    *   通过相同的 `name` 属性将多个按钮归为一组。
    *   浏览器强制实施互斥逻辑：当选中组内的一个新按钮时，之前选中的按钮会自动取消选中。
    *   用户在同一时刻只能从组中选择一个选项（或都不选，如果初始未设定默认值且允许清空，但在标准交互中通常视为必须选其一或保持唯一性）。

**核心区别总结**：复选框用于“选择所有适用的项”（Multiple Selection），单选按钮用于“从多个选项中仅选一项”（Single Exclusive Selection）。

知识点：[复选框（Checkboxes）与单选按钮（Radio Buttons）的事件处理](../../../topics/Web开发技术/checkbox-radio-events.md)、[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)

### （REVIEW QUESTIONS 2.30）WHAT IS THE PURPOSE OF THE PLACEHOLDER ATTRIBUTE OF AN INPUT ELEMENT?

参考解答：**Conclusion**
The purpose of the `placeholder` attribute is to provide a short hint (an example value or a brief description) inside an input field that describes the expected value, displayed when the field is empty and disappearing once the user starts typing.

**Reasoning**
- It gives users a visual cue about what to enter (e.g., "e-mail" or "YYYY-MM-DD") before they provide input.
- It is specified only for `<input>` (and `<textarea>`) elements and is not a substitute for a `<label>`.
- Key behavior: shown only when `value == ""` (empty); hidden when the user focuses/types or the field is filled.

知识点：[表单与控件（form标签、input元素、菜单select、label的for属性、placeholder属性）](../../../topics/Web开发技术/forms-controls.md)
