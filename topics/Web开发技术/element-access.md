---
title: JavaScript中的元素访问方式（forms数组、name属性、id属性、隐式数组implicit arrays）
requires: [Web开发技术/dom-model]
---

# JavaScript中的元素访问方式（forms数组、name属性、id属性、隐式数组implicit arrays）

## 元素在 JavaScript 中如何访问

在浏览器中，HTML 文档由 DOM（Document Object Model）表示。JavaScript 绑定到 DOM 后，==HTML 元素表示为对象，元素的属性表示为该对象的属性==。因此，可以通过访问文档中的元素对象，再读取或修改它的属性来操作页面。

例如：

```html
<input id="username" name="user" type="text">
```

对应的 DOM 对象可理解为：

```javascript
document.getElementById("username").value = "Alice";
```

其中，元素是对象，`type`、`name`、`value` 等是该对象的属性。

## 为什么需要元素访问方式

页面通常包含多个表单、文本框、按钮等元素。JavaScript 必须先找到目标元素，才能：

- 读取用户输入，如取得文本框的 `value`；
- 修改元素属性，如设置 `checked`、`disabled`；
- 绑定事件，如响应按钮的 `click`；
- 改变页面内容或样式。

课件中的 **implicit arrays（隐式数组）** 是较早常见的访问方式。它利用浏览器自动为文档中的表单控件和部分元素建立集合，再通过索引或名称定位元素。

## 使用隐式数组访问元素

### 通过 forms 数组访问表单

`document.forms` 是表单的隐式数组，集合中的每个表单都是一个对象：

```javascript
const form = document.forms[0];
```

若要取得某个表单中的元素，可以继续使用该表单的元素集合：

```javascript
const input = document.forms[0].elements["user"];
input.value = "Alice";
```

这里，`forms[0]` 表示文档中的第一个表单，`elements["user"]` 表示该表单中 `name="user"` 的控件。

### 通过 name 属性访问

在传统写法中，常用 `name` 作为元素或控件的查找键：

```javascript
const input = document.forms[0]["user"];
```

若控件位于页面顶层，部分浏览器也允许使用较短形式：

```javascript
const input = document["user"];
```

但这种顶层访问依赖浏览器对元素名称的全局暴露，容易与同名变量或其他对象属性冲突，==不应当作为现代项目中的首选方案==。

### 通过 id 属性访问

具有唯一 `id` 的元素通常通过：

```javascript
const input = document.getElementById("username");
```

进行访问。`id` 在文档中应保持唯一，因此定位结果明确。这也是现代 JavaScript 中常用的 DOM 查询方式。

## 各种方式的区别

| 访问方式 | 定位依据 | 特点 | 主要问题 |
|---|---|---|---|
| `document.forms[0]` | 表单顺序 | 可直接取得表单对象 | 依赖页面排列，插入表单后索引可能变化 |
| `forms[0].elements["user"]` | 表单内 `name` | 适合操作表单控件 | `name` 重复时可能得到集合 |
| `document["user"]` | 顶层 `name` | 写法较短 | 全局污染、兼容性依赖 |
| `getElementById("username")` | 唯一 `id` | 定位明确、现代浏览器普遍支持 | 必须确保 `id` 唯一 |
| `querySelector("#username")` | CSS 选择器 | 灵活、支持复杂选择器 | 语法更复杂，性能通常低于按 ID 查询 |

## 常见易错点

> [!WARNING]
> `document.forms[0]` 取得的是“表单”，不是表单中的第一个输入框。

表单内控件应通过 `forms[0].elements[...]` 访问。否则容易把表单自身的属性误认为输入框属性。

> [!CAUTION]
> 不要用 `getElementById()` 的返回值直接修改表单的 `value`。

对于 `<input>`、`<textarea>` 等用户输入控件，应读取或设置其 `value` 属性；`value` 反映当前值，而 `defaultValue` 通常对应 HTML 中最初写入的值。

> [!TIP]
> 记忆：`forms` 找表单，`elements` 找控件，`id` 精确找元素，`querySelector` 按 CSS 规则找元素。

## 一个算对了的例子

假设页面有如下表单：

```html
<form name="loginForm">
  <input name="username" value="Tom">
  <input type="submit">
</form>
```

使用隐式数组取得用户名输入框，并读取其值：

```javascript
const username = document.forms["loginForm"].elements["username"];
console.log(username.value);
```

结果为：

```text
Tom
```

这里，`document.forms["loginForm"]` 按表单的 `name` 找到登录表单，`elements["username"]` 再找到其中的用户名控件，最后通过该对象的 `value` 属性取得用户当前输入值。
