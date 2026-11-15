---
title: 屏幕输出与键盘输入（alert、confirm、prompt方法）
requires: [Web开发技术/js-built-in-objects]
---

# 屏幕输出与键盘输入（alert、confirm、prompt方法）

## 三种对话框方法

浏览器提供的 `alert`、`confirm`、`prompt` 都能弹出模态对话框，暂停后续脚本，适合课程示例中的简单输入输出。实际网页通常使用页面元素交互，避免频繁打断用户。

| 方法 | 主要用途 | 用户操作 | 返回值 |
|---|---|---|---|
| `alert(message)` | 输出提示信息 | 只能确定 | `undefined` |
| `confirm(message)` | 请求用户确认 | 确定或取消 | 确定：`true`；取消：`false` |
| `prompt(message[, default])` | 输入一行文本 | 输入后确定，或取消 | 确定：字符串；取消：`null` |

> [!IMPORTANT]
> 三者的核心区别是：==`alert` 只负责输出，`confirm` 返回布尔值，`prompt` 返回字符串或 `null`==。

## 屏幕输出：alert

```javascript
let sum = 12 + 30;
alert("The sum is: " + sum);
alert("第一行\n第二行");
```

`alert` 对话框显示的是普通文本，==不是 XHTML/HTML 内容==。因此换行应写转义字符 `\n`，不能写 `<br/>`；后者通常只会作为字面文本显示。

```mermaid
flowchart LR
    A["调用 alert"] --> B["显示消息"]
    B --> C["用户点击确定"]
    C --> D["继续执行脚本"]
```

## 确认操作：confirm

`confirm` 将参数作为提示消息，并提供 **OK** 和 **Cancel** 两个按钮，可直接放入条件语句：

```javascript
if (confirm("确定要计算吗？")) {
    alert("开始计算");
} else {
    alert("已取消");
}
```

不要把它写成 `confirm(...) === "true"`：其返回值本来就是布尔值，不是字符串。

## 键盘输入：prompt

`prompt` 显示提示信息和文本输入框。第二个可选参数可给出默认输入：

```javascript
let name = prompt("请输入姓名", "张三");
```

其返回规则是考试重点：

- 输入内容并确定：返回输入的**字符串**。
- 未输入内容直接确定：返回空字符串 `""`。
- 点击取消：返回 `null`。

> [!WARNING]
> `prompt` 返回的不是数值。即使输入 `12`，得到的也是字符串 `"12"`；`""` 和 `null` 也不是同一种结果。

## 算对了的例子：求三个数的最大值

题目要求用三次 `prompt` 输入三个数，再用 `Math.max` 输出最大值：

```javascript
let num1 = parseFloat(prompt("请输入第一个数字"));
let num2 = parseFloat(prompt("请输入第二个数字"));
let num3 = parseFloat(prompt("请输入第三个数字"));

let maxNum = Math.max(num1, num2, num3);
alert("最大的数字是：" + maxNum);
```

若依次输入 `12.5`、`8`、`20`，转换后得到三个数值，故

$$
\max(12.5,8,20)=20
$$

最终 `alert` 显示“最大的数字是：20”。

> [!TIP]
> 解题按“`prompt` 取字符串 → `parseFloat` 转数值 → `Math.max` 计算 → `alert` 输出”组织代码。

> [!CAUTION]
> 取消输入会产生 `null`，非数字文本经 `parseFloat` 转换可能得到 `NaN`，进而使结果为 `NaN`。严谨程序应先检查取消操作，并用 `Number.isNaN` 检查转换结果。
