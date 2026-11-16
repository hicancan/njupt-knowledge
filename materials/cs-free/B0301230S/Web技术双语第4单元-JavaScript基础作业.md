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

知识点：[基本数据类型（Primitive Types）、字面量（Numeric and String Literals）及布尔类型](../../../topics/Web开发技术/js-primitives.md)、[内置对象的使用（Math对象、Number对象、String属性与方法、Date对象）](../../../topics/Web开发技术/js-built-in-objects.md)、[JavaScript概述、起源与用途（事件驱动计算Event-driven Computation）](../../../topics/Web开发技术/js-overview.md)

### 简答 2

**题目：** （Reviews Questions 4.20）Describe the operation of the prompt method.

**参考解答：**
`prompt()` 方法用于显示一个带有提示信息和输入框的对话框，等待用户输入文本并点击“确定”或“取消”。
- 如果用户点击“确定”，该方法返回用户输入的字符串；如果用户未输入任何内容，则返回空字符串 `""`。
- 如果用户点击“取消”，该方法返回 `null`。

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

知识点：[JavaScript概述、起源与用途（事件驱动计算Event-driven Computation）](../../../topics/Web开发技术/js-overview.md)、[数组（创建、特性、方法、二维数组）、函数基础（局部变量、参数、构造函数Constructor）与动态属性（for-in循环）](../../../topics/Web开发技术/js-arrays-functions.md)、[控制表达式与语句（if/else选择、switch语法与语义、while/for/do-while循环）](../../../topics/Web开发技术/js-control-flow.md)
