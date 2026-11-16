---
title: 《Web技术（双语）》第4单元 JavaScript基础作业
kind: 习题
course: Web技术（双语）
term: 2018-2019-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/%E4%BD%9C%E4%B8%9A%E7%AD%94%E6%A1%88/web%E6%8A%80%E6%9C%AF%E4%BD%9C%E4%B8%9A8.pdf
---

# 《Web技术（双语）》第4单元 JavaScript基础作业

原件经识别和整理；“参考解答”是我们补的。

# Web技术（双语）第4单元 JavaScript基础作业

本资料为《Web技术（双语）》课程第四单元“JavaScript基础”的作业习题，由识别工具提取整理。

## 一、专业词汇翻译

### 选择 1

请将下列专业词汇对应的中文写出：

- operator
- operand
- expression
- statement
- scripting language
- object-oriented
- strongly typed
- dialog window
- interpreter
- execute
- dynamic
- primitives
- identifier
- variables
- dollar sign
- reserved words
- catenation
- type conversion
- assignment
- array
- constructors
- regular expression

答案：
- operator: 运算符
- operand: 操作数
- expression: 表达式
- statement: 语句
- scripting language: 脚本语言
- object-oriented: 面向对象
- strongly typed: 强类型
- dialog window: 对话框窗口
- interpreter: 解释器
- execute: 执行
- dynamic: 动态
- primitives: 基本类型/原始值
- identifier: 标识符
- variables: 变量
- dollar sign: 美元符号
- reserved words: 保留字
- catenation: 连接（通常指字符串连接）
- type conversion: 类型转换
- assignment: 赋值
- array: 数组
- constructors: 构造函数
- regular expression: 正则表达式

## 二、简答题

知识点：[基本数据类型（Primitive Types）、字面量（Numeric and String Literals）及布尔类型](../../../topics/Web开发技术/js-primitives.md)、[变量声明、数值运算符、字符串连接与赋值语句](../../../topics/Web开发技术/js-vars-operators.md)、[内置对象的使用（Math对象、Number对象、String属性与方法、Date对象）](../../../topics/Web开发技术/js-built-in-objects.md)

### 简答 1

**题目：** （Reviews Questions 4.11）In what circumstances would a variable have the value undefined?

**参考解答：**
变量具有 `undefined` 值的常见情况包括：
1. 变量已声明但尚未初始化或赋值。
2. 函数参数在调用时未提供实参。
3. 对象中不存在的属性访问。
4. 函数没有显式返回值（即返回 `void`）。

参考解答：结论：  
一个变量具有值 `undefined` 的典型情况包括：声明但未赋值、函数参数未传入、访问对象不存在的属性，以及函数体无 `return` 语句返回的值。

推理说明：  
- **声明未赋值**：`var a;` 后 `a` 的值是 `undefined`，因为只创建了变量尚未写入值。  
- **参数未提供**：函数 `function f(x) {}` 在调用 `f()` 时，形参 `x` 在函数体内为 `undefined`。  
- **对象不存在属性**：`obj.nonExist` 若属性不存在则结果为 `undefined`。  
- **函数无返回值**：若函数内没有 `return` 或有 `return;`，实际返回值是 `undefined`。

知识点：[基本数据类型（Primitive Types）、字面量（Numeric and String Literals）及布尔类型](../../../topics/Web开发技术/js-primitives.md)、[内置对象的使用（Math对象、Number对象、String属性与方法、Date对象）](../../../topics/Web开发技术/js-built-in-objects.md)、[JavaScript概述、起源与用途（事件驱动计算Event-driven Computation）](../../../topics/Web开发技术/js-overview.md)

### 简答 2

**题目：** （Reviews Questions 4.20）Describe the operation of the prompt method.

**参考解答：**
`prompt()` 方法用于显示一个带有提示信息和输入框的对话框，等待用户输入文本并点击“确定”或“取消”。
- 如果用户点击“确定”，该方法返回用户输入的字符串；如果用户未输入任何内容，则返回空字符串 `""`。
- 如果用户点击“取消”，该方法返回 `null`。

参考解答：### 结论
`prompt()` 方法显示一个带有文本输入框的模态对话框，提醒用户进行输入。它返回一个字符串或 `null`。

### 简明推理
1.  **操作机制**：`prompt(text, defaultText)` 会阻塞脚本执行，弹出一个包含提示信息、输入框、“确定”和“取消”按钮的对话框。
2.  **返回值逻辑**：
    - 用户点击 **“确定”**：返回输入框中的 **字符串值**。若未输入内容，返回空字符串 `""`。
    - 用户点击 **“取消”** 或关闭对话框：返回 **`null`**。

知识点：[屏幕输出与键盘输入（alert、confirm、prompt方法）](../../../topics/Web开发技术/js-io.md)

### 简答 3

**题目：** （Reviews Questions 4.31）How is a new property of an object created?

**参考解答：**
在 JavaScript 中，可以通过直接给对象的属性赋值来创建新属性。语法如下：
```javascript
objectName.newProperty = value;
```
例如：
```javascript
let person = {};
person.name = "Alice"; // 创建并赋值 name 属性
```

参考解答：**结论**

在 JavaScript 中，通过直接对对象的不存在属性进行赋值操作即可创建新属性。

**推理过程**

1.  **动态特性**：JavaScript 对象是动态的，允许在运行时随时添加或删除属性。
2.  **赋值即创建**：当使用点符号（`object.prop = value`）或方括号符号（`object['prop'] = value`）访问一个尚不存在的属性并为其赋值时，引擎会自动在该对象上创建该属性。
3.  **示例**：
    ```javascript
    let obj = {};       // 创建一个空对象
    obj.newProp = 10;   // 'newProp' 之前不存在，此操作创建了它并赋值为 10
    ```

知识点：[基于对象的概念与JavaScript内置对象](../../../topics/Web开发技术/js-objects.md)、[变量声明、数值运算符、字符串连接与赋值语句](../../../topics/Web开发技术/js-vars-operators.md)

### 简答 4

**题目：** （Reviews Questions 4.33）Describe the two ways an Array object can be created.

**参考解答：**
创建 Array 对象主要有两种方式：
1. **使用 Array 构造函数**：
   - `new Array()`
   - `new Array(length)`
   - `new Array(element0, element1, ..., elementN)`
2. **使用数组字面量（Array Literal）**：
   - `[element0, element1, ..., elementN]`

## 三、编程题

参考解答：创建 Array 对象主要有两种方式：

1. **使用数组字面量（Array Literal）**：通过方括号 `[]` 直接创建，元素在括号内列出。
   ```javascript
   let arr1 = [];                     // 空数组
   let arr2 = [1, 2, 3];              // 含初始元素的数组
   ```

2. **使用 `Array` 构造函数**：通过 `new Array()` 创建。
   ```javascript
   let arr3 = new Array();            // 空数组
   let arr4 = new Array(5);           // 指定长度为 5 的数组
   let arr5 = new Array(1, 2, 3);     // 含初始元素的数组
   ```

> 实际开发中推荐使用**数组字面量**方式，因其更简洁、直观，且避免了单参数时可能产生的歧义（如 `new Array(3)` 创建的是长度为 3 的空数组，而非包含元素 `3` 的数组）。

知识点：[数组（创建、特性、方法、二维数组）、函数基础（局部变量、参数、构造函数Constructor）与动态属性（for-in循环）](../../../topics/Web开发技术/js-arrays-functions.md)

### 计算 1

**题目：** （Exercise 4.3）Input: Three numbers, using prompt to get each. Output: The largest of the three input numbers. Hint: Use the predefined function Math.max.

**参考解答：**

JavaScript 代码：

```javascript
// 获取三个输入数字
let num1 = parseFloat(prompt("请输入第一个数字"));
let num2 = parseFloat(prompt("请输入第二个数字"));
let num3 = parseFloat(prompt("请输入第三个数字"));

// 使用 Math.max 找出最大值
let maxNum = Math.max(num1, num2, num3);

// 输出结果
console.log("最大的数字是：" + maxNum);
alert("最大的数字是：" + maxNum);
```

参考解答：`Math.max(...nums)` 可取出若干数中的最大值；关键是先用 `parseFloat` 把 `prompt` 返回的字符串转为数字，否则会按字符串比较，或得到 `NaN`。

```javascript
const n1 = parseFloat(prompt("Enter first number"));
const n2 = parseFloat(prompt("Enter second number"));
const n3 = parseFloat(prompt("Enter third number"));

const largest = Math.max(n1, n2, n3);
console.log("The largest number is " + largest);
```

推理与关键步骤：
- `prompt` 返回值类型为 `string`，直接比较会得到错误结果（如 `"9" > "10"` 为 `true`），故需 `parseFloat` 转成 `number`。
- 数学上要求

  $$
  \text{largest} = \max(n_1, n_2, n_3) = 
  \begin{cases}
  n_1, & n_1 \ge n_2 \land n_1 \ge n_3 \\
  n_2, & n_2 > n_1 \land n_2 \ge n_3 \\
  n_3, & n_3 > n_1 \land n_3 > n_2
  \end{cases}
  $$

  `Math.max` 正是该运算的预定义函数，直接调用即可，无需写分支。
- `Math.max` 中出现 `NaN` 时结果为 `NaN`，若输入可能非法，可再加校验（如 `Number.isNaN` 判断）。

知识点：[屏幕输出与键盘输入（alert、confirm、prompt方法）](../../../topics/Web开发技术/js-io.md)、[内置对象的使用（Math对象、Number对象、String属性与方法、Date对象）](../../../topics/Web开发技术/js-built-in-objects.md)、[变量声明、数值运算符、字符串连接与赋值语句](../../../topics/Web开发技术/js-vars-operators.md)

### 计算 2

**题目：** （Exercise 4.8）Function: no_zeros Parameter: An array of numbers. Result: The given array must be modified to remove all zero values. Returns: true if the given array included zero values; false otherwise.

**参考解答：**

JavaScript 代码：

```javascript
function no_zeros(arr) {
    let hasZero = false;
    
    // 过滤掉零值
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            hasZero = true;
        }
    }
    
    // 创建新数组去除零值并替换原数组（注意：直接修改原数组可能需要更复杂的逻辑，这里演示通过 filter 生成新数组并假设允许重新赋值或引用修改）
    // 为了严格符合“modify the given array”，可以使用 splice 或重新赋值索引
    // 简单实现：使用 filter 生成非零数组，然后清空原数组并 push 回去，或者重新赋值（取决于上下文是否允许改变引用）
    // 这里采用一种常见的原地修改方式：
    
    let nonZeroElements = arr.filter(item => item !== 0);
    
    // 清空原数组
    arr.length = 0;
    
    // 将非零元素推入原数组
    for (let val of nonZeroElements) {
        arr.push(val);
    }
    
    return hasZero;
}

// 测试示例
let myArray = [1, 0, 2, 0, 3];
let result = no_zeros(myArray);
console.log(result); // true
console.log(myArray); // [1, 2, 3]
```

HTML 代码（用于测试界面，可选）：

```html
<!DOCTYPE html>
<html>
<head>
    <title>Test no_zeros</title>
</head>
<body>
    <h1>Test Array Zero Removal</h1>
    <button onclick="testNoZeros()">Run Test</button>
    <p id="output"></p>

    <script>
        function no_zeros(arr) {
            let hasZero = false;
            for (let i = 0; i < arr.length; i++) {
                if (arr[i] === 0) {
                    hasZero = true;
                }
            }
            
            let nonZeroElements = arr.filter(item => item !== 0);
            arr.length = 0;
            for (let val of nonZeroElements) {
                arr.push(val);
            }
            
            return hasZero;
        }

        function testNoZeros() {
            let testArr = [5, 0, 3, 0, 7];
            let hadZeros = no_zeros(testArr);
            document.getElementById("output").innerText = 
                "Had zeros: " + hadZeros + ", New Array: [" + testArr.join(", ") + "]";
        }
    </script>
</body>
</html>
```

参考解答：**结论：** 函数需遍历数组检测零值，随后原地删除所有零元素，并返回布尔值表示原数组是否包含零。

**实现思路：**
1. 遍历原数组，若发现零值则标记 `hasZero = true`。
2. 使用 `filter()` 生成不含零的新数组。
3. 通过 `arr.length = 0` 清空原数组，再逐元素 `push` 回去，实现原地修改（保持引用不变）。
4. 返回 `hasZero`。

**JavaScript 代码：**

```javascript
function no_zeros(arr) {
    let hasZero = false;
    
    // 检测是否包含零
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            hasZero = true;
            break; // 找到即可停止检测
        }
    }
    
    // 原地修改：移除所有零值
    let nonZeroElements = arr.filter(item => item !== 0);
    arr.length = 0;                    // 清空原数组
    for (let val of nonZeroElements) {
        arr.push(val);                 // 回填非零元素
    }
    
    return hasZero;
}

// 测试
let arr1 = [1, 0, 2, 0, 3];
console.log(no_zeros(arr1)); // true
console.log(arr1);           // [1, 2, 3]

let arr2 = [4, 5, 6];
console.log(no_zeros(arr2)); // false
console.log(arr2);           // [4, 5, 6]
```

**关键说明：**
- **原地修改**：`arr.length = 0` 与后续 `push` 确保原数组引用被修改，而非指向新数组。
- **返回值逻辑**：只要检测到至少一个零即返回 `true`，否则返回 `false`。
- **严格比较**：使用 `===` 避免将字符串 `"0"` 误判为零。

知识点：[JavaScript概述、起源与用途（事件驱动计算Event-driven Computation）](../../../topics/Web开发技术/js-overview.md)、[数组（创建、特性、方法、二维数组）、函数基础（局部变量、参数、构造函数Constructor）与动态属性（for-in循环）](../../../topics/Web开发技术/js-arrays-functions.md)、[控制表达式与语句（if/else选择、switch语法与语义、while/for/do-while循环）](../../../topics/Web开发技术/js-control-flow.md)
