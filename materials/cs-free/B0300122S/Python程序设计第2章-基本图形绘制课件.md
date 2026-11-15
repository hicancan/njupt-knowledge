---
title: 《Python程序设计》第2章 基本图形绘制（课件）
kind: 课件
course: Python程序设计
term: 2022-2023-1
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0300122S%E3%80%91Python%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/22-23-1Python%E8%AF%BE%E4%BB%B6/%E7%AC%AC2%E7%AB%A0%20%E5%9F%BA%E6%9C%AC%E5%9B%BE%E5%BD%A2%E7%BB%98%E5%88%B6.pdf
---

# 《Python程序设计》第2章 基本图形绘制（课件）

原件的每一页，下面附识别出的文字。

### Python 程序设计

![第 1 页](Python程序设计第2章-基本图形绘制课件.assets/第1页.webp)

原文：

Python 程序设计

第 2 章 基本图形绘制

南京邮电大学
Nanjing University of Posts and Telecommunications

### Python基本语法元素

![第 2 页](Python程序设计第2章-基本图形绘制课件.assets/第2页.webp)

原文：

Python基本语法元素

\- 缩进、注释、命名、变量、保留字

\- 数据类型、字符串、整数、浮点数、列表

\- 赋值语句、分支语句、函数

\- input()、print()、eval()、print()格式化

python 语言程序设计

### 保留字

![第 3 页](Python程序设计第2章-基本图形绘制课件.assets/第3页.webp)

原文：

<table><tr><td>and</td><td>elif</td><td>import</td><td>raise</td><td>global</td></tr><tr><td>as</td><td>else</td><td>in</td><td>return</td><td>nonlocal</td></tr><tr><td>assert</td><td>except</td><td>is</td><td>try</td><td>True</td></tr><tr><td>break</td><td>finally</td><td>lambda</td><td>while</td><td>False</td></tr><tr><td>class</td><td>for</td><td>not</td><td>with</td><td>None</td></tr><tr><td>continue</td><td>from</td><td>or</td><td>yield</td><td></td></tr><tr><td>def</td><td>if</td><td>pass</td><td>del</td><td></td></tr></table>

保留字

python

语言程序设计

### python

![第 4 页](Python程序设计第2章-基本图形绘制课件.assets/第4页.webp)

原文：

python

语言程序设计

### \- 2.1 深入理解Python语言

![第 5 页](Python程序设计第2章-基本图形绘制课件.assets/第5页.webp)

原文：

\- 2.1 深入理解Python语言
- 2.2 实例2: Python蟒蛇绘制
- 2.3 模块1: turtle库的使用
- 2.4 turtle程序语法元素分析

第2章 Python基本图形绘制

python 语言程序设计

### 第2章 Python基本图形绘制

![第 6 页](Python程序设计第2章-基本图形绘制课件.assets/第6页.webp)

原文：

第2章 Python基本图形绘制

方法论

\- Python语言及海龟绘图体系

实践能力

\- 初步学会使用Python绘制简单图形

python 语言程序设计

### 深入理解Python语言

![第 7 页](Python程序设计第2章-基本图形绘制课件.assets/第7页.webp)

原文：

深入理解Python语言

python

python

Python语言程序设计

### 深入理解Python语言

![第 8 页](Python程序设计第2章-基本图形绘制课件.assets/第8页.webp)

原文：

深入理解Python语言

\- 计算机技术的演进
- 编程语言的多样性
- Python语言的特点
- "超级语言"的诞生

python 语言程序设计

### 计算机技术的演进

![第 9 页](Python程序设计第2章-基本图形绘制课件.assets/第9页.webp)

原文：

计算机技术的演进

CC

### 计算机技术的演进过程

![第 10 页](Python程序设计第2章-基本图形绘制课件.assets/第10页.webp)

原文：

计算机技术的演进过程

1981-2008
网络和视窗时代 (27年)

1946-1981
计算机系统结构时代 (35年)

2008-2016
复杂信息系统时代 (8年)

2016-

人工智能时代

### 计算机技术的演进过程

![第 11 页](Python程序设计第2章-基本图形绘制课件.assets/第11页.webp)

原文：

计算机技术的演进过程

2017- 人工智能时代 人类的问题

新计算时代

2008-2016 复杂信息系统时代 数据问题

1981-2008

网络和视窗时代

交互问题

1946-1981

计算机系统结构时代

计算能力问题

### 编程语言多样性

![第 12 页](Python程序设计第2章-基本图形绘制课件.assets/第12页.webp)

原文：

编程语言多样性

CC

### 编程语言有哪些？

![第 13 页](Python程序设计第2章-基本图形绘制课件.assets/第13页.webp)

原文：

编程语言有哪些？

Basic, C, C++, C#, CSS, Fortran, Go, HTML, Java,

JavaScript, Lisp, Lua, Matlab, Object C, Pascal, Perl, PHP,

PostScript, Python, Ruby, Scala, SQL, Swift, VBA,

VB.NET, Verilog, VHDL, Visual Basic

### 不同编程语言和适用对象

![第 14 页](Python程序设计第2章-基本图形绘制课件.assets/第14页.webp)

原文：

不同编程语言和适用对象

<table><tr><td>编程语言</td><td>学习内容</td><td>语言本质</td><td>解决问题</td><td>适用对象</td></tr><tr><td>C</td><td>指针、内存、数据类型</td><td>理解计算机系统结构</td><td>性能</td><td>计算机类专业</td></tr><tr><td>Java</td><td>对象、跨平台、运行时</td><td>理解主客体关系</td><td>跨平台</td><td>软件类专业</td></tr><tr><td>C++</td><td>对象、多态、继承</td><td>理解主客体关系</td><td>大规模程序</td><td>计算机类专业</td></tr><tr><td>VB</td><td>对象、按钮、文本框</td><td>理解交互逻辑</td><td>桌面应用</td><td>不确定</td></tr><tr><td>Python</td><td>编程逻辑、第三方库</td><td>理解问题求解</td><td>各类问题</td><td>所有专业</td></tr></table>

各编程语言所处历史时期和使命不同，Python是计算时代演进的选择！

### 2018年以后的计算环境...

![第 15 页](Python程序设计第2章-基本图形绘制课件.assets/第15页.webp)

原文：

2018年以后的计算环境...

计算机性能不再是解决一般问题的瓶颈

移动互联网广泛普及

大数据、云计算、物联网、信息安全、人工智能等需求爆发

解决日益增长的计算需求，用什么语言？

### Python语言的特点

![第 16 页](Python程序设计第2章-基本图形绘制课件.assets/第16页.webp)

原文：

Python语言的特点

CC

### python

![第 17 页](Python程序设计第2章-基本图形绘制课件.assets/第17页.webp)

原文：

python

\- Python语言是通用语言

\- Python语言是脚本语言

\- Python语言是开源语言

\- Python语言是跨平台语言

\- Python语言是多模型语言

Guido van Rossum

Python语言创立者

2002年，Python 2.x

2008年，Python 3.x

### Python特点与优势

![第 18 页](Python程序设计第2章-基本图形绘制课件.assets/第18页.webp)

原文：

Python特点与优势

语法简洁

10x

\- C代码量的10%

\- 强制可读性

\- 较少的底层语法元素

\- 多种编程方式

\- 支持中文字符

10x

生态高产

\- >13万第三方库

\- 快速增长的计算生态

\- 避免重复造轮子

\- 开放共享

\- 跨操作系统平台

### 第 19 页

![第 19 页](Python程序设计第2章-基本图形绘制课件.assets/第19页.webp)

### 第 20 页

![第 20 页](Python程序设计第2章-基本图形绘制课件.assets/第20页.webp)

### 如何看待Python语言？

![第 21 页](Python程序设计第2章-基本图形绘制课件.assets/第21页.webp)

原文：

如何看待Python语言？

人生苦短，我学Python

\- C/C++: Python归Python，C归C

\- Java：针对特定开发和岗位需求

\- HTML/CSS/JS：不可替代的前端技术，全栈能力

\- 其他语言：R/Go/Matlab等，特定领域

### 如何看待Python语言？

![第 22 页](Python程序设计第2章-基本图形绘制课件.assets/第22页.webp)

原文：

如何看待Python语言？

Python是最高产的程序设计语言及……

\- 掌握抽象并求解计算问题综合能力的语言

\- 了解产业界解决复杂计算问题方法的语言

\- 享受利用编程将创新变为实现乐趣的语言

### 如何看待Python语言？

![第 23 页](Python程序设计第2章-基本图形绘制课件.assets/第23页.webp)

原文：

如何看待Python语言？

工具决定思维：关注工具变革的力量！

### "超级语言"的诞生

![第 24 页](Python程序设计第2章-基本图形绘制课件.assets/第24页.webp)

原文：

"超级语言"的诞生

CC

### 编程语言的种类

![第 25 页](Python程序设计第2章-基本图形绘制课件.assets/第25页.webp)

原文：

编程语言的种类

机器语言

\- 一种二进制语言，直接使用二进制代码表达指令

\- 计算机硬件(CPU)可以直接执行，与具体CPU型号有关

\- 完成 2+3 功能的机器语言

11010010 00111011

### 编程语言的种类

![第 26 页](Python程序设计第2章-基本图形绘制课件.assets/第26页.webp)

原文：

编程语言的种类

汇编语言

\- 一种将二进制代码直接对应助记符的编程语言

\- 汇编语言与CPU型号有关，程序不通用，需要汇编器转换

\- 完成 2+3 功能的汇编语言

add 2,3,result

### 编程语言的种类

![第 27 页](Python程序设计第2章-基本图形绘制课件.assets/第27页.webp)

原文：

编程语言的种类

高级语言

\- 更接近自然语言，同时更容易描述计算问题

\- 高级语言代码与具体CPU型号无关，编译后运行

\- 完成 $2 + 3$ 功能的高级语言

$$
\text { result } = 2 + 3
$$

### 编程语言种类的发展

![第 28 页](Python程序设计第2章-基本图形绘制课件.assets/第28页.webp)

原文：

编程语言种类的发展
超级语言 - 粘性整合已有程序，具备庞大计算生态
高级语言 - 接近自然语言，编译器，与CPU型号无关
汇编语言 - 有助记符，汇编器，与CPU型号有关
机器语言 - 代码直接执行，与CPU型号有关

### 编程语言的种类

![第 29 页](Python程序设计第2章-基本图形绘制课件.assets/第29页.webp)

原文：

编程语言的种类

超级语言

具有庞大计算生态，可以很容易利用已有代码功能

\- 编程思维不再是刀耕火种，而是集成开发

\- 完成 $2 + 3$ 功能的超级语言

$$
\text { result } = \text { sum } (2, 3)
$$

### Python: 唯一的"超级语言"!

![第 30 页](Python程序设计第2章-基本图形绘制课件.assets/第30页.webp)

原文：

Python: 唯一的"超级语言"!

### Python前进的步伐不可阻挡

![第 31 页](Python程序设计第2章-基本图形绘制课件.assets/第31页.webp)

原文：

Python前进的步伐不可阻挡

### 深入理解Python语言

![第 32 页](Python程序设计第2章-基本图形绘制课件.assets/第32页.webp)

原文：

深入理解Python语言

\- 计算机系统结构时代到人工智能时代的演进路线

\- 五种编程语言和历史使命

\- Python语言的通用性、简洁性和生态性

\- Python是以计算生态为标志的"超级语言"

python 语言程序设计

### 实例2: Python蟒蛇绘制

![第 33 页](Python程序设计第2章-基本图形绘制课件.assets/第33页.webp)

原文：

实例2: Python蟒蛇绘制

python

python

Python语言程序设计

### "Python蟒蛇绘制"问题分析

![第 34 页](Python程序设计第2章-基本图形绘制课件.assets/第34页.webp)

原文：

"Python蟒蛇绘制"问题分析

CC

### Python蟒蛇绘制

![第 35 页](Python程序设计第2章-基本图形绘制课件.assets/第35页.webp)

原文：

Python蟒蛇绘制

设计蟒蛇的基本形状

### Python蟒蛇绘制

![第 36 页](Python程序设计第2章-基本图形绘制课件.assets/第36页.webp)

原文：

Python蟒蛇绘制

用程序绘制一条蟒蛇

\- 问题1: 计算机绘图是什么原理?

一段程序为何能够产生窗体？为何能在窗体上绘制图形？

\- 问题2: Python蟒蛇绘制从哪里开始呢?

如何绘制一条线？如何绘制一个弧形？如何绘制一个蟒蛇？

### Python蟒蛇绘制

![第 37 页](Python程序设计第2章-基本图形绘制课件.assets/第37页.webp)

原文：

Python蟒蛇绘制

用程序绘制一条蟒蛇

实例1: 温度转换

Python蟒蛇绘制

能否借鉴？

### "Python蟒蛇绘制"实例编写

![第 38 页](Python程序设计第2章-基本图形绘制课件.assets/第38页.webp)

原文：

"Python蟒蛇绘制"实例编写

CC

### 第 39 页

![第 39 页](Python程序设计第2章-基本图形绘制课件.assets/第39页.webp)

### 运行效果

![第 40 页](Python程序设计第2章-基本图形绘制课件.assets/第40页.webp)

原文：

运行效果

IDLE打开文件，按F5运行

Python Turtle Graphics

### 第 41 页

![第 41 页](Python程序设计第2章-基本图形绘制课件.assets/第41页.webp)

### "Python蟒蛇绘制"举一反三

![第 42 页](Python程序设计第2章-基本图形绘制课件.assets/第42页.webp)

原文：

"Python蟒蛇绘制"举一反三

CC

### 第 43 页

![第 43 页](Python程序设计第2章-基本图形绘制课件.assets/第43页.webp)

### 举一反三

![第 44 页](Python程序设计第2章-基本图形绘制课件.assets/第44页.webp)

原文：

举一反三

Python语法元素理解

\- Python蟒蛇绘制共17行代码，但很多行类似

\- 清楚理解这17行代码能够掌握Python基本绘图方法

\- 参考框架结构、逐行分析、逐词理解

### 举一反三

![第 45 页](Python程序设计第2章-基本图形绘制课件.assets/第45页.webp)

原文：

举一反三

程序参数的改变

\- Python蟒蛇的颜色：黑色、白色、七彩色...

\- Python蟒蛇的长度：1节、3节、10节...

\- Python蟒蛇的方向：向左走、斜着走...

### 举一反三

![第 46 页](Python程序设计第2章-基本图形绘制课件.assets/第46页.webp)

原文：

举一反三

计算问题的扩展

\- Python蟒蛇绘制问题是各类图像绘制问题的代表

\- 圆形绘制、五角星绘制、国旗绘制、机器猫绘制...

\- 掌握绘制一条线的方法，就可以绘制整个世界

### 模块1: turtle库的使用

![第 47 页](Python程序设计第2章-基本图形绘制课件.assets/第47页.webp)

原文：

模块1: turtle库的使用

python

python

Python语言程序设计

### 模块1: turtle库的使用

![第 48 页](Python程序设计第2章-基本图形绘制课件.assets/第48页.webp)

原文：

模块1: turtle库的使用

\- turtle库基本介绍
- turtle绘图窗体布局
- turtle空间坐标体系
- turtle角度坐标体系
- RGB色彩体系

python 语言程序设计

### turtle库基本介绍

![第 49 页](Python程序设计第2章-基本图形绘制课件.assets/第49页.webp)

原文：

turtle库基本介绍

CC

### turtle库概述

![第 50 页](Python程序设计第2章-基本图形绘制课件.assets/第50页.webp)

原文：

turtle库概述

turtle(海龟)库是turtle绘图体系的Python实现

\- turtle绘图体系：1969年诞生，主要用于程序设计入门

\- Python语言的标准库之一

\- 入门级的图形绘制函数库

### 标准库

![第 51 页](Python程序设计第2章-基本图形绘制课件.assets/第51页.webp)

原文：

标准库

Python计算生态 = 标准库 + 第三方库

\- 标准库：随解释器直接安装到操作系统中的功能模块

\- 第三方库：需要经过安装才能使用的功能模块

\- 库Library、包Package、模块Module，统称模块

### turtle的原理

![第 52 页](Python程序设计第2章-基本图形绘制课件.assets/第52页.webp)

原文：

turtle的原理

turtle(海龟)是一种真实的存在

\- 有一只海龟，其实在窗体正中心，在画布上游走

\- 走过的轨迹形成了绘制的图形

\- 海龟由程序控制，可以变换颜色、改变宽度等

### turtle绘图窗体布局

![第 53 页](Python程序设计第2章-基本图形绘制课件.assets/第53页.webp)

原文：

turtle绘图窗体布局

CC

### turtle的绘图窗体

![第 54 页](Python程序设计第2章-基本图形绘制课件.assets/第54页.webp)

原文：

turtle的绘图窗体

最小单位是像素

### turtle的绘图窗体

![第 55 页](Python程序设计第2章-基本图形绘制课件.assets/第55页.webp)

原文：

turtle的绘图窗体

### turtle的绘图窗体

![第 56 页](Python程序设计第2章-基本图形绘制课件.assets/第56页.webp)

原文：

turtle的绘图窗体

turtle.setup(width, height, startx, starty)

\- setup()设置窗体大小及位置

\- 4个参数中后两个可选

\- setup()不是必须的

### turtle的绘图窗体

![第 57 页](Python程序设计第2章-基本图形绘制课件.assets/第57页.webp)

原文：

turtle的绘图窗体

turtle.setup(800, 800, 0, 0)

### turtle空间坐标体系

![第 58 页](Python程序设计第2章-基本图形绘制课件.assets/第58页.webp)

原文：

turtle空间坐标体系

CC

### turtle空间坐标体系

![第 59 页](Python程序设计第2章-基本图形绘制课件.assets/第59页.webp)

原文：

turtle空间坐标体系

### turtle空间坐标体系

![第 60 页](Python程序设计第2章-基本图形绘制课件.assets/第60页.webp)

原文：

turtle空间坐标体系

turtle.goto(x, y)

### turtle空间坐标体系

![第 61 页](Python程序设计第2章-基本图形绘制课件.assets/第61页.webp)

原文：

turtle空间坐标体系

### turtle空间坐标体系

![第 62 页](Python程序设计第2章-基本图形绘制课件.assets/第62页.webp)

原文：

turtle空间坐标体系

### turtle空间坐标体系

![第 63 页](Python程序设计第2章-基本图形绘制课件.assets/第63页.webp)

原文：

turtle空间坐标体系

### turtle角度坐标体系

![第 64 页](Python程序设计第2章-基本图形绘制课件.assets/第64页.webp)

原文：

turtle角度坐标体系

CC

### turtle角度坐标体系

![第 65 页](Python程序设计第2章-基本图形绘制课件.assets/第65页.webp)

原文：

turtle角度坐标体系

### turtle角度坐标体系

![第 66 页](Python程序设计第2章-基本图形绘制课件.assets/第66页.webp)

原文：

turtle角度坐标体系

turtle.seth(angle)

\- seth()改变海龟行进方向

\- angle为绝对度数

\- seth()只改变方向但不行进

### turtle角度坐标体系

![第 67 页](Python程序设计第2章-基本图形绘制课件.assets/第67页.webp)

原文：

turtle角度坐标体系

turtle.seth(45)

### Turtle角度坐标体系

![第 68 页](Python程序设计第2章-基本图形绘制课件.assets/第68页.webp)

原文：

Turtle角度坐标体系

### Turtle角度坐标体系

![第 69 页](Python程序设计第2章-基本图形绘制课件.assets/第69页.webp)

原文：

Turtle角度坐标体系

import turtle

turtle.left(45)

turtle.fd(150)

turtle.right(135)

turtle.fd(300)

turtle.left(135)

turtle.fd(150)

Python Turtle Graphics

### RGB色彩体系

![第 70 页](Python程序设计第2章-基本图形绘制课件.assets/第70页.webp)

原文：

RGB色彩体系

CC

### RGB色彩模式

![第 71 页](Python程序设计第2章-基本图形绘制课件.assets/第71页.webp)

原文：

RGB色彩模式

由三种颜色构成的万物色

\- RGB指红蓝绿三个通道的颜色组合

\- 覆盖视力所能感知的所有颜色

\- RGB每色取值范围0-255整数或0-1小数

### 常用RGB色彩

![第 72 页](Python程序设计第2章-基本图形绘制课件.assets/第72页.webp)

原文：

常用RGB色彩

<table><tr><td>英文名称</td><td>RGB整数值</td><td>RGB小数值</td><td>中文名称</td></tr><tr><td>white</td><td>255, 255, 255</td><td>1, 1, 1</td><td>白色</td></tr><tr><td>yellow</td><td>255, 255, 0</td><td>1, 1, 0</td><td>黄色</td></tr><tr><td>magenta</td><td>255, 0, 255</td><td>1, 0, 1</td><td>洋红</td></tr><tr><td>cyan</td><td>0, 255, 255</td><td>0, 1, 1</td><td>青色</td></tr><tr><td>blue</td><td>0, 0, 255</td><td>0, 0, 1</td><td>蓝色</td></tr><tr><td>black</td><td>0, 0, 0</td><td>0, 0, 0</td><td>黑色</td></tr></table>

### 常用RGB色彩

![第 73 页](Python程序设计第2章-基本图形绘制课件.assets/第73页.webp)

原文：

常用RGB色彩

<table><tr><td>英文名称</td><td>RGB整数值</td><td>RGB小数值</td><td>中文名称</td></tr><tr><td>seashell</td><td>255, 245, 238</td><td>1, 0.96, 0.93</td><td>海贝色</td></tr><tr><td>gold</td><td>255, 215, 0</td><td>1, 0.84, 0</td><td>金色</td></tr><tr><td>pink</td><td>255, 192, 203</td><td>1, 0.75, 0.80</td><td>粉红色</td></tr><tr><td>brown</td><td>165, 42, 42</td><td>0.65, 0.16, 0.16</td><td>棕色</td></tr><tr><td>purple</td><td>160, 32, 240</td><td>0.63, 0.13, 0.94</td><td>紫色</td></tr><tr><td>tomato</td><td>255, 99, 71</td><td>1, 0.39, 0.28</td><td>番茄色</td></tr></table>

### turtle的RGB色彩模式

![第 74 页](Python程序设计第2章-基本图形绘制课件.assets/第74页.webp)

原文：

turtle的RGB色彩模式

默认采用小数值 可切换为整数值

turtle.colormode(mode)

\- 1.0: RGB小数值模式

\- 255: RGB整数值模式

### 模块1: turtle库的使用

![第 75 页](Python程序设计第2章-基本图形绘制课件.assets/第75页.webp)

原文：

模块1: turtle库的使用

\- turtle库的海龟绘图法

\- turtle.setup()调整绘图窗体在电脑屏幕中的布局

\- 画布上以中心为原点的空间坐标系: 绝对坐标&海龟坐标

\- 画布上以空间x轴为0度的角度坐标系: 绝对角度&海龟角度

\- RGB色彩体系，整数值&小数值，色彩模式切换

python 语言程序设计

### Python语言程序设计

![第 76 页](Python程序设计第2章-基本图形绘制课件.assets/第76页.webp)

原文：

Python语言程序设计

turtle程序语法元素分析

python

python

### turtle程序语法元素分析

![第 77 页](Python程序设计第2章-基本图形绘制课件.assets/第77页.webp)

原文：

turtle程序语法元素分析

\- 库引用与import
- turtle画笔控制函数
- turtle运动控制函数
- turtle方向控制函数
- 基本循环语句
- "Python蟒蛇绘制"代码分析

python 语言程序设计

### 库引用与import

![第 78 页](Python程序设计第2章-基本图形绘制课件.assets/第78页.webp)

原文：

库引用与import

CC

### import turtle

![第 79 页](Python程序设计第2章-基本图形绘制课件.assets/第79页.webp)

原文：

import turtle

turtle.setup(650, 350, 200, 200)

turtle.penup()

turtle.fd(-250)

turtle.pendown()

turtle.pensize(25)

turtle.pencolor("purple")

turtle.seth(-40)

turtle.circle(40, 80)

turtle.circle(-40, 80)

turtle.circle(40, 80/2)

turtle.fd(40)

turtle.circle(16, 180)

turtle.fd(40 \* 2/3)

turtle.done()

<a>.<b>()的编码风格

python

### 库引用

![第 80 页](Python程序设计第2章-基本图形绘制课件.assets/第80页.webp)

原文：

库引用

扩充Python程序功能的方式

\- 使用import保留字完成，采用<a>.<b>()编码风格

import <库名>

<库名>.<函数名>(<函数参数>)

### 引入turtle库

![第 81 页](Python程序设计第2章-基本图形绘制课件.assets/第81页.webp)

原文：

引入turtle库

使用turtle库函数 完成功能

### import更多用法

![第 82 页](Python程序设计第2章-基本图形绘制课件.assets/第82页.webp)

原文：

import更多用法

使用from和import保留字共同完成

from <库名> import <函数名>

from <库名> import \*

<函数名>(<函数参数>)

### import turtle

![第 83 页](Python程序设计第2章-基本图形绘制课件.assets/第83页.webp)

原文：

import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 \* 2/3)
turtle.done()

from turtle import \*

setup(650, 350, 200, 200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)
circle(16, 180)
fd(40 \* 2/3)
done()

### import更多用法

![第 84 页](Python程序设计第2章-基本图形绘制课件.assets/第84页.webp)

原文：

import更多用法

两种方法比较

import <库名>

from <库名> import <函数名>

<库名>.<函数名>(<函数参数>)

from <库名> import \*

<函数名>(<函数参数>)

第一种方法不会出现函数重名问题，第二种方法则会出现

### import更多用法

![第 85 页](Python程序设计第2章-基本图形绘制课件.assets/第85页.webp)

原文：

import更多用法

使用import和as保留字共同完成

import <库名> as <库别名>

<库别名>.<函数名>(<函数参数>)

给调用的外部库关联一个更短、更适合自己的名字

### import turtle

![第 86 页](Python程序设计第2章-基本图形绘制课件.assets/第86页.webp)

原文：

import turtle

turtle.setup(650, 350, 200, 200)

turtle.penup()

turtle.fd(-250)

turtle.pendown()

turtle.pensize(25)

turtle.pencolor("purple")

turtle.seth(-40)

for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)

turtle.circle(40, 80/2)

turtle.fd(40)

turtle.circle(16, 180)

turtle.fd(40 \* 2/3)

turtle.done()

import turtle as t

t. setup(650, 350, 200, 200)

t. penup()

t.fd(-250)

t.pendown()

t.pensize(25)

t.pencolor("purple")

t. seth(-40)

for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)

t.circle(40, 80/2)

t.fd(40)

t.circle(16, 180)

t.fd(40 \* 2/3)

t. done()

### turtle画笔控制函数

![第 87 页](Python程序设计第2章-基本图形绘制课件.assets/第87页.webp)

原文：

turtle画笔控制函数

CC

### python

![第 88 页](Python程序设计第2章-基本图形绘制课件.assets/第88页.webp)

原文：

python

### 画笔控制函数

![第 89 页](Python程序设计第2章-基本图形绘制课件.assets/第89页.webp)

原文：

画笔控制函数

画笔操作后一直有效，一般成对出现

\- turtle.penup()

别名 turtle.pu()

抬起画笔，海龟在飞行

\- turtle.pendown() 别名 turtle.pd()

落下画笔，海龟在爬行

### 画笔控制函数

![第 90 页](Python程序设计第2章-基本图形绘制课件.assets/第90页.webp)

原文：

画笔控制函数

画笔设置后一直有效，直至下次重新设置

\- turtle.pensize(width) 别名 turtle.width(width)

画笔宽度，海龟的腰围

\- turtle.pencolor(color) color为颜色字符串或r,g,b值

画笔颜色，海龟在涂装

### 画笔控制函数

![第 91 页](Python程序设计第2章-基本图形绘制课件.assets/第91页.webp)

原文：

画笔控制函数

pencolor(color)的color参与可以有三种形式

\- 颜色字符串 : turtle.pencolor("purple")

\- RGB的小数值：turtle.pencolor(0.63, 0.13, 0.94)

\- RGB的元组值：turtle.pencolor((0.63, 0.13, 0.94))

### python

![第 92 页](Python程序设计第2章-基本图形绘制课件.assets/第92页.webp)

原文：

python

### turtle运动控制函数

![第 93 页](Python程序设计第2章-基本图形绘制课件.assets/第93页.webp)

原文：

turtle运动控制函数

CC

### 第 94 页

![第 94 页](Python程序设计第2章-基本图形绘制课件.assets/第94页.webp)

### 运动控制函数

![第 95 页](Python程序设计第2章-基本图形绘制课件.assets/第95页.webp)

原文：

运动控制函数

控制海龟行进：走直线 & 走曲线

\- turtle.forward(d) 别名 turtle.fd(d)

向前行进，海龟走直线

\- d: 行进距离，可以为负数

### 运动控制函数

![第 96 页](Python程序设计第2章-基本图形绘制课件.assets/第96页.webp)

原文：

运动控制函数

控制海龟行进：走直线 & 走曲线

\- turtle.circle(r, extent=None)

根据半径r绘制extent角度的弧形

\- r: 默认圆心在海龟左侧r距离的位置

\- extent: 绘制角度，默认是360度整圆

### 运动控制函数

![第 97 页](Python程序设计第2章-基本图形绘制课件.assets/第97页.webp)

原文：

运动控制函数

turtle.circle(100)

### 第 98 页

![第 98 页](Python程序设计第2章-基本图形绘制课件.assets/第98页.webp)

### 运动控制函数

![第 99 页](Python程序设计第2章-基本图形绘制课件.assets/第99页.webp)

原文：

运动控制函数

画笔设置后一直有效，直至下次重新设置

\- turtle.forward(d) 别名 turtle.fd(d)

向前行进，海龟走直线

\- d: 行进距离，可以为负数

### turtle方向控制函数

![第 100 页](Python程序设计第2章-基本图形绘制课件.assets/第100页.webp)

原文：

turtle方向控制函数

CC

### 第 101 页

![第 101 页](Python程序设计第2章-基本图形绘制课件.assets/第101页.webp)

### 方向控制函数

![第 102 页](Python程序设计第2章-基本图形绘制课件.assets/第102页.webp)

原文：

方向控制函数

控制海龟面对方向: 绝对角度 & 海龟角度

\- turtle.setheading(angle) 别名 turtle.seth(angle)

改变行进方向，海龟走角度

\- angle: 行进方向的绝对角度

### 方向控制函数

![第 103 页](Python程序设计第2章-基本图形绘制课件.assets/第103页.webp)

原文：

方向控制函数

turtle.seth(45)

### 方向控制函数

![第 104 页](Python程序设计第2章-基本图形绘制课件.assets/第104页.webp)

原文：

方向控制函数

控制海龟面对方向: 绝对角度 & 海龟角度

\- turtle.left(angle)

海龟向左转

\- turtle.right(angle)

海龟向右转

\- angle: 在海龟当前行进方向上旋转的角度

### 第 105 页

![第 105 页](Python程序设计第2章-基本图形绘制课件.assets/第105页.webp)

### 循环语句与range()函数

![第 106 页](Python程序设计第2章-基本图形绘制课件.assets/第106页.webp)

原文：

循环语句与range()函数

CC

### 第 107 页

![第 107 页](Python程序设计第2章-基本图形绘制课件.assets/第107页.webp)

### 循环语句

![第 108 页](Python程序设计第2章-基本图形绘制课件.assets/第108页.webp)

原文：

循环语句

按照一定次数循环执行一组语句

for <变量> in range(<次数>):

<被循环执行的语句>

\- <变量>表示每次循环的计数，0到<次数>-1

### 循环语句

![第 109 页](Python程序设计第2章-基本图形绘制课件.assets/第109页.webp)

原文：

循环语句

>>> for i in range(5):
    print(i)

>>> for i in range(5):
    print("Hello:",i)

θ

1

2

3

4

Hello: 0

Hello: 1

Hello: 2

Hello: 3

Hello: 4

### range()函数

![第 110 页](Python程序设计第2章-基本图形绘制课件.assets/第110页.webp)

原文：

range()函数

产生循环计数序列

range(5)
0, 1, 2, 3, 4
range(2, 5)
2, 3, 4

产生 M 到 N-1 的整数序列，共 N-M 个

### 第 111 页

![第 111 页](Python程序设计第2章-基本图形绘制课件.assets/第111页.webp)

### "Python蟒蛇绘制"代码分析

![第 112 页](Python程序设计第2章-基本图形绘制课件.assets/第112页.webp)

原文：

"Python蟒蛇绘制"代码分析

CC

### 第 113 页

![第 113 页](Python程序设计第2章-基本图形绘制课件.assets/第113页.webp)

### 第 114 页

![第 114 页](Python程序设计第2章-基本图形绘制课件.assets/第114页.webp)

### 第 115 页

![第 115 页](Python程序设计第2章-基本图形绘制课件.assets/第115页.webp)

### 第 116 页

![第 116 页](Python程序设计第2章-基本图形绘制课件.assets/第116页.webp)

### turtle程序语法元素分析

![第 117 页](Python程序设计第2章-基本图形绘制课件.assets/第117页.webp)

原文：

turtle程序语法元素分析

\- 库引用: import、from...import、import...as...

\- penup()、pendown()、pensize()、pencolor()

\- fd()、 circle()、 seth()

\- 循环语句：for和in、range()函数

python 语言程序设计
