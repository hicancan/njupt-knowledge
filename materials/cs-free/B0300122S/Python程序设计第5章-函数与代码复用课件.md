---
title: 《Python程序设计》第5章 函数与代码复用（课件）
kind: 课件
course: Python程序设计
term: 2022-2023-1
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0300122S%E3%80%91Python%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/22-23-1Python%E8%AF%BE%E4%BB%B6/%E7%AC%AC5%E7%AB%A0%20%E5%87%BD%E6%95%B0%E4%B8%8E%E4%BB%A3%E7%A0%81%E5%A4%8D%E7%94%A8.pdf
---

# 《Python程序设计》第5章 函数与代码复用（课件）

原件的每一页，下面附识别出的文字。

### Python 程序设计

![第 1 页](Python程序设计第5章-函数与代码复用课件.assets/第1页.webp)

原文：

Python 程序设计

第 5章 函数与代码复用

南京郵電大学

### 数字类型及操作

![第 2 页](Python程序设计第5章-函数与代码复用课件.assets/第2页.webp)

原文：

数字类型及操作

\- 整数类型的无限范围及4种进制表示

\- 浮点数类型的近似无限范围、小尾数及科学计数法

\- +、-、\*、/、//、%、\*\*、二元增强赋值操作符

\- abs()、divmod()、pow()、round()、max()、min()

\- int()、float()、complex()

### 第 3 页

![第 3 页](Python程序设计第5章-函数与代码复用课件.assets/第3页.webp)

### 第 4 页

![第 4 页](Python程序设计第5章-函数与代码复用课件.assets/第4页.webp)

### 字符串类型及操作

![第 5 页](Python程序设计第5章-函数与代码复用课件.assets/第5页.webp)

原文：

字符串类型及操作

\- 正向递增序号、反向递减序号、<字符串>[M:N:K]

\- +、\*、len()、str()、hex()、oct()、ord()、chr()

\- .lower()、.upper()、.split()、.count()、.replace()

\- .center()、.strip()、.join(）、.format()格式化

### 第 6 页

![第 6 页](Python程序设计第5章-函数与代码复用课件.assets/第6页.webp)

### 程序的分支结构

![第 7 页](Python程序设计第5章-函数与代码复用课件.assets/第7页.webp)

原文：

程序的分支结构

\- 单分支 if 二分支 if-else 及紧凑形式

\- 多分支 if-elif-else 及条件之间关系

\- not and or > >= == <= < !=

\- 异常处理 try-except-else-finally

### python

![第 8 页](Python程序设计第5章-函数与代码复用课件.assets/第8页.webp)

原文：

python

### 程序的循环结构

![第 9 页](Python程序设计第5章-函数与代码复用课件.assets/第9页.webp)

原文：

程序的循环结构

-for…in 遍历循环: 计数、字符串、列表、文件…

\- while无限循环

\- continue和break保留字: 退出当前循环层次

\- 循环else的高级用法: 与break有关

### 第 10 页

![第 10 页](Python程序设计第5章-函数与代码复用课件.assets/第10页.webp)

### 第5章 函数和代码复用

![第 11 页](Python程序设计第5章-函数与代码复用课件.assets/第11页.webp)

原文：

第5章 函数和代码复用

\- 5.1 函数的定义与使用
- 5.2 实例7: 七段数码管绘制
- 5.3 代码复用与函数递归
- 5.4 模块4: PyInstaller库的使用
- 5.5 实例8: 科赫雪花小包裹

### 第5章 函数和代码复用

![第 12 页](Python程序设计第5章-函数与代码复用课件.assets/第12页.webp)

原文：

第5章 函数和代码复用

方法论

\- Python基本代码抽象即函数的使用方法

实践能力

\- 学会编写带有函数并复用代码的程序

### Python语言程序设计

![第 13 页](Python程序设计第5章-函数与代码复用课件.assets/第13页.webp)

原文：

Python语言程序设计

函数的定义与使用

### 函数的定义与使用

![第 14 页](Python程序设计第5章-函数与代码复用课件.assets/第14页.webp)

原文：

函数的定义与使用

\- 函数的理解与定义
- 函数的使用及调用过程
- 函数的参数传递
- 函数的返回值
- 局部变量和全局变量
- lambda函数

### 函数的理解和定义

![第 15 页](Python程序设计第5章-函数与代码复用课件.assets/第15页.webp)

原文：

函数的理解和定义

### 第 16 页

![第 16 页](Python程序设计第5章-函数与代码复用课件.assets/第16页.webp)

### 函数的定义

![第 17 页](Python程序设计第5章-函数与代码复用课件.assets/第17页.webp)

原文：

函数的定义

函数是一段代码的表示

\- 函数是一段具有特定功能的、可重用的语句组

\- 函数是一种功能的抽象，一般函数表达特定功能

\- 两个作用：降低编程难度 和 代码复用

### 函数的定义

![第 18 页](Python程序设计第5章-函数与代码复用课件.assets/第18页.webp)

原文：

函数的定义

函数是一段代码的表示

def <函数名>(<参数(0个或多个)>) :

<函数体>

return <返回值>

### 函数的定义

![第 19 页](Python程序设计第5章-函数与代码复用课件.assets/第19页.webp)

原文：

函数的定义

### 函数的定义

![第 20 页](Python程序设计第5章-函数与代码复用课件.assets/第20页.webp)

原文：

函数的定义

$$
\mathbf {y} = f (\mathbf {x})
$$

\- 函数定义时，所指定的参数是一种占位符

\- 函数定义后，如果不经过调用，不会被执行

\- 函数定义时，参数是输入、函数体是处理、结果是输出 (IPO)

### 函数的使用及调用过程

![第 21 页](Python程序设计第5章-函数与代码复用课件.assets/第21页.webp)

原文：

函数的使用及调用过程

### 函数的调用

![第 22 页](Python程序设计第5章-函数与代码复用课件.assets/第22页.webp)

原文：

函数的调用

调用是运行函数代码的方式

函数的调用

### 函数的调用过程

![第 23 页](Python程序设计第5章-函数与代码复用课件.assets/第23页.webp)

原文：

函数的调用过程

### 函数的参数传递

![第 24 页](Python程序设计第5章-函数与代码复用课件.assets/第24页.webp)

原文：

函数的参数传递

### 参数个数

![第 25 页](Python程序设计第5章-函数与代码复用课件.assets/第25页.webp)

原文：

参数个数

函数可以有参数，也可以没有，但必须保留括号

def <函数名>() :

<函数体>

return <返回值>def fact() :print("我也是函数")

### 可选参数传递

![第 26 页](Python程序设计第5章-函数与代码复用课件.assets/第26页.webp)

原文：

可选参数传递

函数定义时可以为某些参数指定默认值，构成可选参数

def <函数名>(<非可选参数>, <可选参数>) :

<函数体>

return <返回值>

### 可选参数传递

![第 27 页](Python程序设计第5章-函数与代码复用课件.assets/第27页.webp)

原文：

可选参数传递

### 可变参数传递

![第 28 页](Python程序设计第5章-函数与代码复用课件.assets/第28页.webp)

原文：

可变参数传递

函数定义时可以设计可变数量参数，既不确定参数总数量

def <函数名>(<参数>, \*b ) :

<函数体>

return <返回值>

### 可变参数传递

![第 29 页](Python程序设计第5章-函数与代码复用课件.assets/第29页.webp)

原文：

可变参数传递

### 参数传递的两种方式

![第 30 页](Python程序设计第5章-函数与代码复用课件.assets/第30页.webp)

原文：

参数传递的两种方式

函数调用时，参数可以按照位置或名称方式传递

### 函数的返回值

![第 31 页](Python程序设计第5章-函数与代码复用课件.assets/第31页.webp)

原文：

函数的返回值

### 函数的返回值

![第 32 页](Python程序设计第5章-函数与代码复用课件.assets/第32页.webp)

原文：

函数的返回值

函数可以返回0个或多个结果

\- return保留字用来传递返回值

函数可以有返回值，也可以没有，可以有return，也可以没有

\- return可以传递0个返回值，也可以传递任意多个返回值

### 函数的返回值

![第 33 页](Python程序设计第5章-函数与代码复用课件.assets/第33页.webp)

原文：

函数的返回值

函数调用时，参数可以按照位置或名称方式传递

### 局部变量和全局变量

![第 34 页](Python程序设计第5章-函数与代码复用课件.assets/第34页.webp)

原文：

局部变量和全局变量

### 局部变量和全局变量

![第 35 页](Python程序设计第5章-函数与代码复用课件.assets/第35页.webp)

原文：

局部变量和全局变量

程序全局变量

函数局部变量

### 局部变量和全局变量

![第 36 页](Python程序设计第5章-函数与代码复用课件.assets/第36页.webp)

原文：

局部变量和全局变量

### 局部变量和全局变量

![第 37 页](Python程序设计第5章-函数与代码复用课件.assets/第37页.webp)

原文：

局部变量和全局变量

规则1: 局部变量和全局变量是不同变量

\- 局部变量是函数内部的占位符，与全局变量可能重名但不同

\- 函数运算结束后，局部变量被释放

\- 可以使用global保留字在函数内部使用全局变量

### 局部变量和全局变量

![第 38 页](Python程序设计第5章-函数与代码复用课件.assets/第38页.webp)

原文：

局部变量和全局变量

### 局部变量和全局变量

![第 39 页](Python程序设计第5章-函数与代码复用课件.assets/第39页.webp)

原文：

局部变量和全局变量

### 局部变量和全局变量

![第 40 页](Python程序设计第5章-函数与代码复用课件.assets/第40页.webp)

原文：

局部变量和全局变量

规则2: 局部变量为组合数据类型且未创建，等同于全局变量

运行结果

全局变量ls被修改

### 局部变量和全局变量

![第 41 页](Python程序设计第5章-函数与代码复用课件.assets/第41页.webp)

原文：

局部变量和全局变量

通过使用[]真实创建了一个全局变量列表ls

此处ls是列表类型，真实创建

ls是局部变量

ls.append(a)

return

print(ls)

局部变量ls被修改

运行结果

>>>

### 局部变量和全局变量

![第 42 页](Python程序设计第5章-函数与代码复用课件.assets/第42页.webp)

原文：

局部变量和全局变量

使用规则

\- 基本数据类型，无论是否重名，局部变量与全局变量不同

\- 可以通过global保留字在函数内部声明全局变量

\- 组合数据类型，如果局部变量未真实创建，则是全局变量

### lambda函数

![第 43 页](Python程序设计第5章-函数与代码复用课件.assets/第43页.webp)

原文：

lambda函数

### lambda函数

![第 44 页](Python程序设计第5章-函数与代码复用课件.assets/第44页.webp)

原文：

lambda函数

lambda函数返回函数名作为结果

\- lambda函数是一种匿名函数，即没有名字的函数

\- 使用lambda保留字定义，函数名是返回结果

\- lambda函数用于定义简单的、能够在一行内表示的函数

### lambda函数

![第 45 页](Python程序设计第5章-函数与代码复用课件.assets/第45页.webp)

原文：

lambda函数

<函数名> = lambda <参数>: <表达式>

def <函数名>(<参数>) :

等价于 <函数体>

return <返回值>

### lambda函数

![第 46 页](Python程序设计第5章-函数与代码复用课件.assets/第46页.webp)

原文：

lambda函数

### lambda函数的应用

![第 47 页](Python程序设计第5章-函数与代码复用课件.assets/第47页.webp)

原文：

lambda函数的应用

谨慎使用lambda函数

\- lambda函数主要用作一些特定函数或方法的参数

\- lambda函数有一些固定使用方式，建议逐步掌握

\- 一般情况，建议使用def定义的普通函数

### 函数的定义与使用

![第 48 页](Python程序设计第5章-函数与代码复用课件.assets/第48页.webp)

原文：

函数的定义与使用

\- 使用保留字def定义函数，lambda定义匿名函数

\- 可选参数(赋初值)、可变参数(\*b)、名称传递

\- 保留字return可以返回任意多个结果

\- 保留字global声明使用全局变量，一些隐式规则

### Python语言程序设计

![第 49 页](Python程序设计第5章-函数与代码复用课件.assets/第49页.webp)

原文：

Python语言程序设计

实例7: 七段数码管绘制

### "七段数码管绘制"问题分析

![第 50 页](Python程序设计第5章-函数与代码复用课件.assets/第50页.webp)

原文：

"七段数码管绘制"问题分析

### 问题分析

![第 51 页](Python程序设计第5章-函数与代码复用课件.assets/第51页.webp)

原文：

问题分析

七段数码管

0123456789 AbCdEF

### 问题分析

![第 52 页](Python程序设计第5章-函数与代码复用课件.assets/第52页.webp)

原文：

问题分析

七段数码管绘制

\- 需求：用程序绘制七段数码管

\- 该怎么做呢？

turtle绘图体系

七段数码管绘制

### 问题分析

![第 53 页](Python程序设计第5章-函数与代码复用课件.assets/第53页.webp)

原文：

问题分析

七段数码管绘制时间

### 七段数码管绘制

![第 54 页](Python程序设计第5章-函数与代码复用课件.assets/第54页.webp)

原文：

七段数码管绘制

基本思路

\- 步骤1：绘制单个数字对应的数码管

\- 步骤2：获得一串数字，绘制对应的数码管

\- 步骤3：获得当前系统时间，绘制对应的数码管

### 七段数码管绘制

![第 55 页](Python程序设计第5章-函数与代码复用课件.assets/第55页.webp)

原文：

七段数码管绘制

步骤1: 绘制单个数码管

\- 七段数码管由7个基本线条组成

\- 七段数码管可以有固定顺序

\- 不同数字显示不同的线条import turtledef drawLine(draw): #绘制单段数码管turtle.pendown() if draw else turtle.penup()turtle.fd(40)turtle.right(90)

### 第 56 页

![第 56 页](Python程序设计第5章-函数与代码复用课件.assets/第56页.webp)

原文：

def drawDigit(digit): #根据数字绘制七段数码管 3 drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False) drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False) drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False) drawLine(True) if digit in [0,2,6,8] else drawLine(False) turtle.left(90) drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False) drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False) drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False) turtle.left(180) turtle.penup() #为绘制后续数字确定位置 turtle.fd(20) #为绘制后续数字确定位置

### 七段数码管绘制

![第 57 页](Python程序设计第5章-函数与代码复用课件.assets/第57页.webp)

原文：

七段数码管绘制

步骤2: 获取一段数字，绘制多个数码管

### 第 58 页

![第 58 页](Python程序设计第5章-函数与代码复用课件.assets/第58页.webp)

### 七段数码管绘制

![第 59 页](Python程序设计第5章-函数与代码复用课件.assets/第59页.webp)

原文：

七段数码管绘制

基本思路

\- 步骤1：绘制单个数字对应的数码管

\- 步骤2：获得一串数字，绘制对应的数码管

\- 步骤3：获得当前系统时间，绘制对应的数码管

### 七段数码管绘制

![第 60 页](Python程序设计第5章-函数与代码复用课件.assets/第60页.webp)

原文：

七段数码管绘制

绘制漂亮的七段数码管

\- 增加七段数码管之间线条间隔

### 第 61 页

![第 61 页](Python程序设计第5章-函数与代码复用课件.assets/第61页.webp)

### 七段数码管绘制

![第 62 页](Python程序设计第5章-函数与代码复用课件.assets/第62页.webp)

原文：

七段数码管绘制

步骤3:获取系统时间，绘制七段数码管

\- 使用time库获得系统当前时间

\- 增加年月日标记

\- 年月日颜色不同

### 第 63 页

![第 63 页](Python程序设计第5章-函数与代码复用课件.assets/第63页.webp)

### 第 64 页

![第 64 页](Python程序设计第5章-函数与代码复用课件.assets/第64页.webp)

### "七段数码管绘制"举一反三

![第 65 页](Python程序设计第5章-函数与代码复用课件.assets/第65页.webp)

原文：

"七段数码管绘制"举一反三

### 第 66 页

![第 66 页](Python程序设计第5章-函数与代码复用课件.assets/第66页.webp)

### 举一反三

![第 67 页](Python程序设计第5章-函数与代码复用课件.assets/第67页.webp)

原文：

举一反三

理解方法思维

\- 模块化思维：确定模块接口，封装功能

\- 规则化思维：抽象过程为规则，计算机自动执行

\- 化繁为简：将大功能变为小功能组合，分而治之

### 举一反三

![第 68 页](Python程序设计第5章-函数与代码复用课件.assets/第68页.webp)

原文：

举一反三

应用问题的扩展

\- 绘制带小数点的七段数码管

\- 带刷新的时间倒计时效果

\- 绘制高级的数码管

### Python语言程序设计

![第 69 页](Python程序设计第5章-函数与代码复用课件.assets/第69页.webp)

原文：

Python语言程序设计

代码复用与函数递归

### 代码复用与函数递归

![第 70 页](Python程序设计第5章-函数与代码复用课件.assets/第70页.webp)

原文：

代码复用与函数递归

\- 代码复用与模块化设计
- 函数递归的理解
- 函数递归的调用过程
- 函数递归实例解析

### 代码复用与模块化设计

![第 71 页](Python程序设计第5章-函数与代码复用课件.assets/第71页.webp)

原文：

代码复用与模块化设计

### 代码复用

![第 72 页](Python程序设计第5章-函数与代码复用课件.assets/第72页.webp)

原文：

代码复用

把代码当成资源进行抽象

\- 代码资源化：程序代码是一种用来表达计算的"资源"

\- 代码抽象化：使用函数等方法对代码赋予更高级别的定义

\- 代码复用：同一份代码在需要时可以被重复使用

### 代码复用

![第 73 页](Python程序设计第5章-函数与代码复用课件.assets/第73页.webp)

原文：

代码复用

函数 和 对象 是代码复用的两种主要形式

函数：将代码命名在代码层面建立了初步抽象对象：属性和方法

<a>.<b> 和 <a>.<b>()

在函数之上再次组织进行抽象

抽象级别

### 模块化设计

![第 74 页](Python程序设计第5章-函数与代码复用课件.assets/第74页.webp)

原文：

模块化设计

分而治之

\- 通过函数或对象封装将程序划分为模块及模块间的表达

\- 具体包括：主程序、子程序和子程序间关系

\- 分而治之：一种分而治之、分层抽象、体系化的设计思想

### 模块化设计

![第 75 页](Python程序设计第5章-函数与代码复用课件.assets/第75页.webp)

原文：

模块化设计

紧耦合 松耦合

\- 紧耦合：两个部分之间交流很多，无法独立存在

\- 松耦合：两个部分之间交流较少，可以独立存在

\- 模块内部紧耦合、模块之间松耦合

### 函数递归的理解

![第 76 页](Python程序设计第5章-函数与代码复用课件.assets/第76页.webp)

原文：

函数递归的理解

### 递归的定义

![第 77 页](Python程序设计第5章-函数与代码复用课件.assets/第77页.webp)

原文：

递归的定义

函数定义中调用函数自身的方式

$$
\boxed {n! = \left\{ \begin{array}{c c} 1 & n = 0 \\ n (n - 1)! & o t h e r w i s e \end{array} \right.}
$$

### 递归的定义

![第 78 页](Python程序设计第5章-函数与代码复用课件.assets/第78页.webp)

原文：

递归的定义

两个关键特征

\- 链条：计算过程存在递归链条

\- 基例：存在一个或多个不需要再次递归的基例

$$
n! = \left\{ \begin{array}{c} 1 \\ n (n - 1)! \end{array} \right.
$$

$$
n = 0
$$

otherwise

### 递归的定义

![第 79 页](Python程序设计第5章-函数与代码复用课件.assets/第79页.webp)

原文：

递归的定义

类似数学归纳法

- 数学归纳法

\- 证明当n取第一个值 $n _ { \alpha }$ 时命题成立

\- 假设当 $n _ { k }$ 时命题成立，证明当 $\boldsymbol { \mathsf { n } } { = } \boldsymbol { \mathsf { n } } _ { } _ { } { } _ { k + 1 }$ 时命题也成立

\- 递归是数学归纳法思维的编程体现

### 函数递归的调用过程

![第 80 页](Python程序设计第5章-函数与代码复用课件.assets/第80页.webp)

原文：

函数递归的调用过程

### 递归的实现

![第 81 页](Python程序设计第5章-函数与代码复用课件.assets/第81页.webp)

原文：

递归的实现

### 递归的实现

![第 82 页](Python程序设计第5章-函数与代码复用课件.assets/第82页.webp)

原文：

递归的实现

函数 + 分支语句

\- 递归本身是一个函数，需要函数定义方式描述

\- 函数内部，采用分支语句对输入参数进行判断

\- 基例和链条，分别编写对应代码

### 递归的调用过程

![第 83 页](Python程序设计第5章-函数与代码复用课件.assets/第83页.webp)

原文：

递归的调用过程

### 函数递归实例解析

![第 84 页](Python程序设计第5章-函数与代码复用课件.assets/第84页.webp)

原文：

函数递归实例解析

### 字符串反转

![第 85 页](Python程序设计第5章-函数与代码复用课件.assets/第85页.webp)

原文：

字符串反转

将字符串s反转后输出 >>> s[::-1]

### 斐波那契数列

![第 86 页](Python程序设计第5章-函数与代码复用课件.assets/第86页.webp)

原文：

斐波那契数列

一个经典数列

$$
\boxed { \begin{array}{c c} F (n) = \left\{ \begin{array}{c c} 1 & n = 1 \\ 1 & n = 2 \\ F (n - 1) + F (n - 2) & o t h e r w i s e \end{array} \right. \end{array} }
$$

### 斐波那契数列

![第 87 页](Python程序设计第5章-函数与代码复用课件.assets/第87页.webp)

原文：

斐波那契数列

F(n) = F(n-1) + F(n-2)

### 汉诺塔

![第 88 页](Python程序设计第5章-函数与代码复用课件.assets/第88页.webp)

原文：

汉诺塔

$$
\mathsf {P 1} = <   3, 4, 5, 8 >
$$

4 disks here.

2 disks here.

$$
P 2 = <   6, 7 >
$$

2 disks here.

### 第 89 页

![第 89 页](Python程序设计第5章-函数与代码复用课件.assets/第89页.webp)

### 汉诺塔

![第 90 页](Python程序设计第5章-函数与代码复用课件.assets/第90页.webp)

原文：

汉诺塔

### 代码复用与函数递归

![第 91 页](Python程序设计第5章-函数与代码复用课件.assets/第91页.webp)

原文：

代码复用与函数递归

\- 模块化设计：松耦合、紧耦合

-函数递归的2个特征：基例和链条

\- 函数递归的实现：函数 + 分支结构

### PyInstaller库基本介绍

![第 92 页](Python程序设计第5章-函数与代码复用课件.assets/第92页.webp)

原文：

PyInstaller库基本介绍

### PyInstaller库概述

![第 93 页](Python程序设计第5章-函数与代码复用课件.assets/第93页.webp)

原文：

PyInstaller库概述

将.py源代码转换成无需源代码的可执行文件

\- Windows (exe文件)

.py文件

PyInstaller

\- Linux

\- Mac OS X

### PyInstaller库概述

![第 94 页](Python程序设计第5章-函数与代码复用课件.assets/第94页.webp)

原文：

PyInstaller库概述

PyInstaller库是第三方库

\- 官方网站：http://www.pyinstaller.org

\- 第三方库：使用前需要额外安装

\- 安装第三方库需要使用pip工具

### PyInstaller库的安装

![第 95 页](Python程序设计第5章-函数与代码复用课件.assets/第95页.webp)

原文：

PyInstaller库的安装

(cmd命令行) pip install pyinstaller

命令提示符- pip install pyinstaller

C:\Users\Tian Song>pip installpyinstaller Collecting pyinstaller Downloading PyInstaller-3.3.1.tar.gz(3.5MB)

100% 8.3MB 11kB/ Installing collectedpackages: pefile, altgraph, macholib, py win32, pypiwin32, pyinstaller Running setup.py install for pefile ... done 11 for pyinstaller ... done Successfully installed 1tgraph-0.15macholib-1.9pefile-2017 pypiwin32-223 pywin32-223

C:\Users\Tian Song>

### PyInstaller库使用说明

![第 96 页](Python程序设计第5章-函数与代码复用课件.assets/第96页.webp)

原文：

PyInstaller库使用说明

### 简单的使用

![第 97 页](Python程序设计第5章-函数与代码复用课件.assets/第97页.webp)

原文：

简单的使用

(cmd命令行) pyinstaller -F <文件名.py>

### PyInstaller库常用参数

![第 98 页](Python程序设计第5章-函数与代码复用课件.assets/第98页.webp)

原文：

PyInstaller库常用参数

<table><tr><td>参数</td><td>描述</td></tr><tr><td>-h</td><td>查看帮助</td></tr><tr><td>--clean</td><td>清理打包过程中的临时文件</td></tr><tr><td>-D, --onedir</td><td>默认值,生成dist文件夹</td></tr><tr><td>-F, --onefile</td><td>在dist文件夹中只生成独立的打包文件</td></tr><tr><td>-i &lt;图标文件名.ico&gt;</td><td>指定打包程序使用的图标(icon)文件</td></tr></table>

### 使用举例

![第 99 页](Python程序设计第5章-函数与代码复用课件.assets/第99页.webp)

原文：

使用举例

pyinstaller –i curve.ico –F SevenDigitsDrawV2.py

### 实例8: 科赫雪花小包裹

![第 100 页](Python程序设计第5章-函数与代码复用课件.assets/第100页.webp)

原文：

实例8: 科赫雪花小包裹

Python语言程序设计

### 科赫雪花

![第 101 页](Python程序设计第5章-函数与代码复用课件.assets/第101页.webp)

原文：

科赫雪花

分形几何

### 科赫雪花

![第 102 页](Python程序设计第5章-函数与代码复用课件.assets/第102页.webp)

原文：

科赫雪花

雪花曲线

### 科赫雪花绘制

![第 103 页](Python程序设计第5章-函数与代码复用课件.assets/第103页.webp)

原文：

科赫雪花绘制

取1/3长

每分隔一次为一阶

60度

### "科赫雪花小包裹"

![第 104 页](Python程序设计第5章-函数与代码复用课件.assets/第104页.webp)

原文：

"科赫雪花小包裹"

### 科赫雪花小包裹

![第 105 页](Python程序设计第5章-函数与代码复用课件.assets/第105页.webp)

原文：

科赫雪花小包裹

科赫曲线的绘制

### 科赫雪花小包裹

![第 106 页](Python程序设计第5章-函数与代码复用课件.assets/第106页.webp)

原文：

科赫雪花小包裹

### 第 107 页

![第 107 页](Python程序设计第5章-函数与代码复用课件.assets/第107页.webp)

### 第 108 页

![第 108 页](Python程序设计第5章-函数与代码复用课件.assets/第108页.webp)

### 科赫雪花小包裹

![第 109 页](Python程序设计第5章-函数与代码复用课件.assets/第109页.webp)

原文：

科赫雪花小包裹

### 科赫雪花小包裹

![第 110 页](Python程序设计第5章-函数与代码复用课件.assets/第110页.webp)

原文：

科赫雪花小包裹

pyinstaller –i curve.ico –F KochDrawV2.py

$$
\begin{array}{c c c} \text {   +   } & \text {   KochDrawV2   } & = \\ \hline \end{array}
$$

\- 对编写后的科赫雪花代码进行打包处理

### 科赫雪花小包裹(下)

![第 111 页](Python程序设计第5章-函数与代码复用课件.assets/第111页.webp)

原文：

科赫雪花小包裹(下)

命令提示符- pyinstaller -i curve.ico -F KochDrawV2.py

### "科赫雪花小包裹"举一反三

![第 112 页](Python程序设计第5章-函数与代码复用课件.assets/第112页.webp)

原文：

"科赫雪花小包裹"举一反三

### 第 113 页

![第 113 页](Python程序设计第5章-函数与代码复用课件.assets/第113页.webp)

### 举一反三

![第 114 页](Python程序设计第5章-函数与代码复用课件.assets/第114页.webp)

原文：

举一反三

绘制条件的扩展

\- 修改分形几何绘制阶数

\- 修改科赫曲线的基本定义及旋转角度

\- 修改绘制科赫雪花的基础框架图形

### 康托尔集

![第 115 页](Python程序设计第5章-函数与代码复用课件.assets/第115页.webp)

原文：

康托尔集

举一反三

$$
\begin{array}{c c} \hline & \\ \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline \hline 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2. \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \hline \dots \\ \h line {{\dots}} \\ \end{array}
$$

### 举一反三

![第 116 页](Python程序设计第5章-函数与代码复用课件.assets/第116页.webp)

原文：

举一反三

- 谢尔宾斯基三角形

### 举一反三

![第 117 页](Python程序设计第5章-函数与代码复用课件.assets/第117页.webp)

原文：

举一反三

\- 门格海绵

### 举一反三

![第 118 页](Python程序设计第5章-函数与代码复用课件.assets/第118页.webp)

原文：

举一反三

\- 龙形曲线

### 举一反三

![第 119 页](Python程序设计第5章-函数与代码复用课件.assets/第119页.webp)

原文：

举一反三

- 空间填充曲线

<table><tr><td>6</td><td>7</td><td>10</td><td>11</td></tr><tr><td>5</td><td>8</td><td>9</td><td>12</td></tr><tr><td>4</td><td>3</td><td>14</td><td>13</td></tr><tr><td>1</td><td>2</td><td>15</td><td>16</td></tr></table>

14
