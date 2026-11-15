---
title: 《计算机组成与结构》第6章 MIPS32CPU设计（课件）
kind: 课件
course: 计算机组成与结构
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301581S%E3%80%91%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BB%84%E6%88%90%E4%B8%8E%E7%BB%93%E6%9E%84_CST/%E8%AF%BE%E4%BB%B6/%E7%AC%AC6%E7%AB%A0--deprecated.ppt
---

# 《计算机组成与结构》第6章 MIPS32CPU设计（课件）

原件的每一页，下面附识别出的文字。

### COMPUTER ORGANIZATION AND ARCHITECTURE

![第 1 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第1页.webp)

原文：

COMPUTER ORGANIZATION AND ARCHITECTURE

Chapter 6

MIPS32CPU设计

南京郵電大學 Nanijing O 圆 nons 南京郵電大学 Nanjing University of Posts and Telecommunications ty o Posts and T

### 本章学习目标

![第 2 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第2页.webp)

原文：

本章学习目标

◼ MIPS CPU的实现路线图

◼ 介绍实现处理器的原理和技术

◼ 构造MIPS处理器的简单版本

◼ 支持核心指令集

包括实践应用的流水线处理器

◼ 实现更复杂的指令集所必需的概念，例如x86指令集

◼ 一个基本的MIPS实现

◼ 存储器访问指令：lw, sw

算术逻辑指令：add, sub, and, or, slt

◼ 分支指令：beq, j

Chapter 4 — The Processor — 2

### 指令的执行

![第 3 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第3页.webp)

原文：

指令的执行

◼ 对于MIPS，大多数指令执行流程如下：

◼ 程序计数器PC指向指令所在的存储单元，并从中取出指令。

◼ 通过指令字段的内容，读取一个或两个寄存器

◼ 根据指令的类型完成指令指令的执行

◼ 使用算术逻辑单元ALU

◼ 算术结果

读取/存储数据的内存地址

◼ 分支目标地址

◼ 访问内存以读取/存储数据

◼ PC  目标地址 / PC + 4

### MIPS CPU抽象视图

![第 4 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第4页.webp)

原文：

MIPS CPU抽象视图

◼ 组成部分：

◼ 关键功能单元

◼ 连接各个功能单元的粗线表示总线

箭头用来指示信息的流向

### 执行一条指令

![第 5 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第5页.webp)

原文：

执行一条指令

◼ 所有的指令都开始于使用程序计数器获得指令在指令存储器中的地址

◼ 程序计数器提供地址

◼ MIPS从指令存储器中读取指令

◼ 获取指令后，指令所使用的寄存器操作数由该指令的字段指定

◼ ALU

◼ 为读取/存储计算存储器地址

◼ 计算算术运算、逻辑运算的结果.

◼ 比较分支指令

### 执行一条指令

![第 6 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第6页.webp)

原文：

执行一条指令

◼ 完成ALU之后

◼ 如果指令是算术逻辑指令，则将ALU的结果写入寄存器

◼ 如果操作是读取/存储数据，则ALU的结果用作地址。要么将寄存器中的数据写入内存，要么将内存中的数据写入寄存器

◼ 来自ALU或内存的结果被写回寄存器堆

◼ 分支指令需要ALU的结果确定下一条指令的地址

### 多选器

![第 7 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第7页.webp)

原文：

多选器

◼ 该图显示了流向特定单元的数据来自两个不同的源

◼ 写入PC的值可以来自两个加法器中的一个

◼ 写入寄存器堆的数据可以来自ALU或者数据存储器

◼ ALU的第二个输入可以来自寄存器或指令中的立即数字段

◼ 实际上，不能简单的将这些数据连接在一起

◼ 多选器，一个从多个源中进行选择的逻辑元件

### 多选器

![第 8 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第8页.webp)

原文：

多选器

◼ 多选器(数据选择器)

◼ 多选器的基本功能是接受来自控制器的指令，并相应地选择一个输入同时阻塞另一个输入

### 控制

![第 9 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第9页.webp)

原文：

控制

◼ 单元的控制依赖于当前执行的指令

◼ 存取指令读写数据存储器

◼ ALU执行几种操作中的一种

◼ 多选器选择一个输入

◼ 名为“控制”的关键部分，是处理器的大脑

### 控制

![第 10 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第10页.webp)

原文：

控制

◼ 控制单元将指令作为输入，决定功能单元和两个多选器的控制信号

### 学习目标

![第 11 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第11页.webp)

原文：

学习目标

◼ 我么将进一步研究如何在MIPS处理器中构建数据通路

◼ 我们将逐步构建一个MIPS数据通路

◼ 自顶向下，查看每一个指令需要哪些数据通路部件

◼ 我们把不同的部件组合在一起

§ 4.3 Building a Datapath

Chapter 4 — The Processor

11

### 指令获取

![第 12 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第12页.webp)

原文：

指令获取

执行指令，必须首先从存储单元中取出指令然后，为了准备执行下一条指令，必须增加程序计数器，以便指向4字节后的下一条指令

(指令获取)内存单元存储程序的指令，并通过地址提供指令

### 指令获取

![第 13 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第13页.webp)

原文：

指令获取

Chapter 4 — The Processor

13

### R型指令

![第 14 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第14页.webp)

原文：

R型指令

◼ R型指令包括：add, sub, AND, OR

◼ R型指令的任务：

◼ 读取两个寄存器操作数

◼ 执行算术/逻辑操作

◼ 将结果写回寄存器Wria register

◼ 寄存器堆和ALU是实现R型指令的必须单元

Chapter 4 — The Processor

14

### 读取/存储指令

![第 15 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第15页.webp)

原文：

读取/存储指令

◼ 读取/存储指令的功能：

◼ 读取寄存器操作数

◼ 计算基址寄存器和16位偏移的地址之和

◼ 访问数据

◼ lw：读取内存数据并更新寄存器值

◼ sw：将寄存器值写入内存

Chapter 4 — The Processor

15

### 分支指令

![第 16 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第16页.webp)

原文：

分支指令

◼ 分支指令的功能：

◼ 三个操作数

◼ 两个寄存器用于比较是否相等

◼ 用于计算相对分支指令所在地址的分支目标地址，是16位偏移量

读寄存器操作数

◼ 比较操作数

◼ 使用ALU，操作数相减并检查Zero标志

◼ 计算目标地址

◼ 偏移量左移两位

◼ 将PC+4

Chapter 4 — The Processor

16

### 分支指令

![第 17 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第17页.webp)

原文：

分支指令

### 组成单元

![第 18 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第18页.webp)

原文：

组成单元

◼ 到目前为止…

◼ 我们已经讨论了不同指令类型所需的数据通路部件

◼ 现在，我们可以将它们合并到一起，并添加控制完成最简单的MIPS子集实现方案

Chapter 4 — The Processor

18

### 完整的数据通路

![第 19 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第19页.webp)

原文：

完整的数据通路

Chapter 4 — The Processor —

19

### 主控制单元

![第 20 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第20页.webp)

原文：

主控制单元

◼ 理解如何将指令的各个字段连接到数据通路

<table><tr><td rowspan="2">R-type</td><td>0</td><td>rs</td><td>rt</td><td>rd</td><td>shamt</td><td>funct</td></tr><tr><td>31:26</td><td>25:21</td><td>20:16</td><td>15:11</td><td>10:6</td><td>5:0</td></tr><tr><td rowspan="2">Load/Store</td><td>35 or 43</td><td>rs</td><td>rt</td><td colspan="3">address</td></tr><tr><td>31:26</td><td>25:21</td><td>20:16</td><td colspan="3">15:0</td></tr><tr><td rowspan="3">Branch</td><td>4</td><td>rs</td><td>rt</td><td colspan="3">address</td></tr><tr><td>31:26</td><td>25:21</td><td>20:16</td><td colspan="3">15:0</td></tr><tr><td>opcode</td><td>always read</td><td>read, except for load</td><td colspan="2">write for R-type and load</td><td>sign-extend and add</td></tr></table>

### 包含控制单元的数据通路

![第 21 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第21页.webp)

原文：

包含控制单元的数据通路

• 控制单元的输入为指令的6位操作码

### R型指令

![第 22 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第22页.webp)

原文：

R型指令

◼ add \$t1, \$t2, \$3

◼ 从指令存储器中取出指令，PC+4

◼ 从寄存器堆读取两个寄存器\$t2和\$t3，同时主控制单元计算出各控制信号的状态

◼ ALU对从寄存器堆中读取的数据进行操作

ALU的结果被写回寄存器

### R型指令

![第 23 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第23页.webp)

原文：

R型指令

add \$t1, \$t2, \$3

(高亮部分显示了控制信号、数据通路单元和连接线)

### 读取指令

![第 24 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第24页.webp)

原文：

读取指令

◼ lw \$t1, offset(\$t2)

从指令存储器中取指， $\mathsf { P C } { + 4 }$

◼ 从寄存器堆中读取寄存器 (\$t2)的值

◼ ALU计算计算从寄存器堆中读取的值和符号拓展后的指令低16位(偏移量)的和

◼ 将ALU的结果作为数据存储器的地址

◼ 来自内存单元的数据被写入寄存器堆

### 读取指令

![第 25 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第25页.webp)

原文：

读取指令

lw \$t1, offset(\$t2)

### 相等则分支指令

![第 26 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第26页.webp)

原文：

相等则分支指令

beq \$t1, \$t2, offset

◼ 从指令存储器中取指

◼ 从寄存器堆中读取寄存器\$t1和\$t2的值

◼ ALU将从寄存器堆读取的两数相减

◼ PC+4的值与符号拓展并左移 2位后的低16位相加，结果 即为分支目标地址

◼ 结果是分支目标地址

◼ 新的地址被写回PC中

### 相等则分支指令

![第 27 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第27页.webp)

原文：

相等则分支指令

beq \$t1, \$t2, offset

### 简单但完整的CPU

![第 28 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第28页.webp)

原文：

简单但完整的CPU

### 性能问题

![第 29 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第29页.webp)

原文：

性能问题

◼ 最长的时延决定时钟周期长度

◼ 关键路径：读取指令

◼ 指令存储器→ 寄存器堆→ ALU → 数据存储器→ 寄存 器堆

◼ 对于不同的指令，改变周期是不可行的

◼ 违反设计原则

◼ 加速大概率事件

◼ 我们将通过流水线提高性能

Chapter 4 — The Processor

29

### 简单但完整的CPU

![第 30 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第30页.webp)

原文：

简单但完整的CPU

### 流水线

![第 31 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第31页.webp)

原文：

流水线

◼ 流水线是一种实现多条指令重叠执行的技术

◼ 非流水线方式洗衣过程(类比)

◼ 把一批脏衣服放入洗衣机里清洗

◼ 洗衣机洗完后，把衣服取出并放入烘干机

烘干衣服后，将衣服从烘干机取出，然后放在桌子上叠起来

◼ 叠好衣服后，请你的室友把桌子上的衣服收好

◼ 当你的室友完成任务后，你就可以开始下一个脏活了

§ 4.5 An Overview of Pipelining

### 流水线方式

![第 32 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第32页.webp)

原文：

流水线方式

◼ 非流水线方式洗衣

◼ 非流水线方式是否有效？为什么？

◼ 第二批脏衣服要等到第一批脏衣服晒干、折叠放好后才开始

◼ 不同的机器是按顺序操作的

### 流水线方式

![第 33 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第33页.webp)

原文：

流水线方式

◼ 如何提高？

◼ 流水线方式洗衣

◼ 一旦洗衣机完成清洗第一批衣服并放入烘干机,◼ 把第二批脏衣服装到洗衣机

◼ 相似地，当第一批衣服烘干之后，同时把衣服放在桌上开始折叠

◼ 将洗完的湿衣服放入烘干机,

◼ 然后将下一批脏衣服放入洗衣机

◼ 结论：在流水线过程中使用的机器是并行操作的

### 流水线方式类比

![第 34 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第34页.webp)

原文：

流水线方式类比

◼ 流水线方式洗衣

◼ 所有的工作都是同时进行的，所以每个晚上可以洗完更多的衣服

### 流水线方式总结

![第 35 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第35页.webp)

原文：

流水线方式总结

◼ 流水线不会减少完成一次洗衣任务的时间

◼ 当我们有很多衣服要洗时，流水线操作可以提高吞吐量

### MIPS 流水线

![第 36 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第36页.webp)

原文：

MIPS 流水线

◼ 同样的原则也适用于流水线指令执行的处理器

◼ 我们在本课程中探讨MIPS处理器的五个步骤

1. IF：从指令存储器中读取指令

2. ID：指令译码的同时读取寄存器从

3. EX：执行操作或计算地址

4. MEM：从数据存储器中读取操作数

5. WB：将结果写回寄存器

Chapter 4 — The Processor

36

### MIPS 流水线

![第 37 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第37页.webp)

原文：

MIPS 流水线

◼ 我们在本课程中探讨的MIPS流水线的五个步骤

IF, ID, EX, MEM, WB

### 流水线性能

![第 38 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第38页.webp)

原文：

流水线性能

◼ 假设步骤所用时间：

◼ 寄存器的读写需要100ps

◼ 其他步骤各需要200ps

◼ CPU的设计必须考虑最慢的指令.

◼ 所以每条指令需要的时间是800ps

<table><tr><td>Instr</td><td>Instr fetch</td><td>Register read</td><td>ALU op</td><td>Memory access</td><td>Register write</td><td>Total time</td></tr><tr><td>lw</td><td>200ps</td><td>100 ps</td><td>200ps</td><td>200ps</td><td>100 ps</td><td>800ps</td></tr><tr><td>sw</td><td>200ps</td><td>100 ps</td><td>200ps</td><td>200ps</td><td></td><td>700ps</td></tr><tr><td>R-format</td><td>200ps</td><td>100 ps</td><td>200ps</td><td></td><td>100 ps</td><td>600ps</td></tr><tr><td>beq</td><td>200ps</td><td>100 ps</td><td>200ps</td><td></td><td></td><td>500ps</td></tr></table>

Chapter 4 — The Processor —

38

### 流水线性能

![第 39 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第39页.webp)

原文：

流水线性能

◼ 在流水线的设计中，流水线执行的时钟周期必须选择最坏情况下的200ps，即使某些步骤只需要100ps

<table><tr><td>Iw $1, 100($0)</td><td>Instruction fetch</td><td></td><td>Reg</td><td colspan="2">ALU</td><td>Data access</td><td>Reg</td><td></td><td></td></tr><tr><td>Iw $2, 200($0)</td><td>200 ps</td><td colspan="2">Instruction fetch</td><td></td><td>Reg</td><td>ALU</td><td>Data access</td><td>Reg</td><td></td></tr><tr><td>Iw $3, 300($0)</td><td></td><td>200 ps</td><td colspan="2">Instruction fetch</td><td></td><td>Reg</td><td>ALU</td><td>Data access</td><td>Reg</td></tr></table>

Chapter 4 — The Processor

39

### 流水线加速

![第 40 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第40页.webp)

原文：

流水线加速

◼ 如果所有的步骤都是平衡的

◼ 例，所有步骤所用时间都是一样的

Time between instructionnonpipelined Time between instructionspipelined Number of pipe stages

◼ 加速比与流水线的级数近似相同

◼ 一个五级流水线能获得的加速比接近于5

Chapter 4 — The Processor

40

### 流水线和ISA设计

![第 41 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第41页.webp)

原文：

流水线和ISA设计

◼ MIPS ISA是为流水线设计的

◼ 所有的指令都是32位，长度相同

◼ 在流水线的第一个阶段更容易获取指令，在第二个阶段更容易解码指令

◼ 例外，x86的指令长度1-17字节

◼ MIPS只有几种指令格式，源寄存器位于相同的位置◼ 对称性意味着MIPS可以在一步内进行指令解码和读取寄存器

◼ 内存操作数只出现在读取/存储指令中

◼ 我们可以使用ALU来计算内存地址，然后在下一个步骤访问内存

Chapter 4 — The Processor

41

### 冒险

![第 42 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第42页.webp)

原文：

冒险

\- 在下一个时钟周期中下一条指令不能执行，称为冒险
- 结构冒险
  - 所需的资源繁忙
- 数据冒险
  - 需要等待以前的指令完成它数据的读写
- 控制冒险
  - 决策行动取决于先前指令的结果

Chapter 4 — The Processor

42

### 结构冒险

![第 43 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第43页.webp)

原文：

结构冒险

◼ 硬件不支持多条指令在同一周期执行

◼ (类比)如果我们使用洗衣烘干一体机代替独立的洗衣机和烘干机，就会发生冒险

◼ MIPS流水线结构只有一个存储器

◼ 读取/存储需要访问数据

◼ 指令获取将不得不在那个周期阻塞

◼ 因此，流水线数据通路需要单独的指令/数据存储器

◼ 或者是单独的指令/数据缓存

### 数据冒险

![第 44 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第44页.webp)

原文：

数据冒险

◼ 下列C++代码是否合法？

◼ 下列C++代码是否高效？为什么？

Chapter 4 — The Processor

44

### 数据冒险

![第 45 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第45页.webp)

原文：

数据冒险

◼ 数据冒险发生在由于一条指令必须等待另一条指令完成导致流水线暂停的情况下

add \$s0, \$t0, \$t1 sub \$t2, \$s0, \$t3

Chapter 4 — The Processor

45

### 前推(旁路)

![第 46 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第46页.webp)

原文：

前推(旁路)

◼ 如何解决这个问题？?

◼ 基本发现：在解决数据冒险问题之前不需要等待指令的执行结束

◼ 一旦ALU生成加法运算的结果

◼ 不需要等待它被存储在寄存器中

◼ 直接将它用作减法运算的一个输入项

◼ 一个重要的流水线概念，称为流水线阻塞，但通常被称为气泡

### 装载-使用型数据冒险

![第 47 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第47页.webp)

原文：

装载-使用型数据冒险

◼ 前推能解决所有的数据冒险吗？?

◼ 例， 当R型指令试图在加载之后使用数据.

◼ 即使存在前推也需要阻塞

◼ 数据通路中需要额外的连接

### 指令调度避免阻塞

![第 48 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第48页.webp)

原文：

指令调度避免阻塞

◼ 编译器/软件能帮助避免阻塞吗？?

$$
\begin{array}{l} \text {lw s0, 20(t0)} \\ \text {sub t1, s0, t3} \end{array}
$$

$$
\begin{array}{l} \mathsf {A} = \mathsf {B} + \mathsf {E}; \\ \mathsf {C} = \mathsf {B} + \mathsf {F}; \end{array}
$$

◼ 将第3条lw指令上移到第3条指令的位置则可以进一步消除所有冒险

$$
\begin{array}{c}\text { stall } \rightarrow\\\text { stall } \rightarrow\end{array}\begin{array}{c}1 w \quad t 1, 0 (t 0)\\1 w \quad t 2, 4 (t 0)\\a d d \quad t 3, t 1, t 2\\s w \quad t 3, 1 2 (t 0)\\1 w \quad t 4, 8 (t 0)\\a d d \quad t 5, t 1, t 4\\s w \quad t 5, 1 6 (t 0)\end{array}\tag {13cycles}
$$

$$
\begin{array}{l l} \text {lw} & t 1, 0 (t 0) \\ \text {lw} & t 2, 4 (t 0) \\ \text {lw} & t 4, 8 (t 0) \\ \text {add} & t 3, t 1, t 2 \\ \text {sw} & t 3, 1 2 (t 0) \\ \text {add} & t 5, t 1, t 4 \\ \text {sw} & t 5, 1 6 (t 0) \end{array}
$$

### MIPS CPU完整的数据通路

![第 49 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第49页.webp)

原文：

MIPS CPU完整的数据通路

Chapter 4 — The Processor

49

### 指令获取

![第 50 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第50页.webp)

原文：

指令获取

Chapter 4 — The Processor

50

### 控制冒险

![第 51 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第51页.webp)

原文：

控制冒险

◼ 汇编代码片段：

add \$t4, \$t5, \$t6 beq \$t1, \$t2, 40 addi \$t4, \$t4, 1

or \$t7, \$t8, \$t9

<table><tr><td rowspan="4">Program execution order (in instructions)</td><td>Time</td><td>200</td><td>400</td><td>600</td><td>800</td><td>1000</td><td>1200</td><td>1400</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>add $4, $5, $6</td><td>Instruction fetch</td><td></td><td>Reg</td><td>ALU</td><td>Data access</td><td>Reg</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>beq $1, $2, 40</td><td>Instruction fetch</td><td></td><td>Reg</td><td>ALU</td><td>Data access</td><td>Reg</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>or $7, $8, $9</td><td>Bubble bubbles Bubble bubble Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubblebubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubbles Bubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesbubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubbles Bubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesbubbleBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubble bubblesBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubblebubbleBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubble BubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubble BubbleBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBalanceBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBalanceBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubble bubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubble bubbleBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubble bubblesBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubble bubblesBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubblebubbleBubbleBubbleBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubblebubbleBubblebubbleBubblebubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubbleBubblebubbleBubbleBucketSize3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000x3000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.0000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000.000</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>300</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>155</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>150</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>130</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>125</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>145</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>120</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>135</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>165</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>175</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>195</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>205</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>225</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>235</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>245</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>265</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>275</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>285</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>295</td><td>2</td></tr></table>

Chapter 4 — The Processor

51

### 控制冒险

![第 52 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第52页.webp)

原文：

控制冒险

◼ 当预期的指令不能在预定的流水线时钟周期内执行时：

因为获取的指令不是需要的指令

◼ 例，指令地址的流动不是流水线所期待的

Chapter 4 — The Processor

52

### 分支上的阻塞

![第 53 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第53页.webp)

原文：

分支上的阻塞

◼ 如何解决控制冒险？

◼ 在获取下一条指令之前，等待直到分支结果确定

Chapter 4 — The Processor

53

### 分支预测

![第 54 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第54页.webp)

原文：

分支预测

◼ 有比等待更好的办法吗？

◼ 预测分支结果

◼ 不要等待你得到正确的答案

◼ 如果你是幸运的，并且预测成功，那就继续执行

◼ 如果你不幸地预测失败，重新开始

◼ 优点：只有预测失败时才会阻塞

Chapter 4 — The Processor

54

### MIPS流水线指令预测

![第 55 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第55页.webp)

原文：

MIPS流水线指令预测

Chapter 4 — The Processor

55

### 更加成熟的分支预测

![第 56 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第56页.webp)

原文：

更加成熟的分支预测

◼ 静态分支预测

◼ 由编译器执行

基于典型的分支行为

◼ 动态分支预测

◼ 硬件度量实际的分支行为

◼ 例，记录每个分支最近的分支历史

◼ 假设未来的行为将延续这一趋势

◼ 当预测失败时，阻塞同时重新获取指令并更新分支历史

Chapter 4 — The Processor

56

### 流水线总结

![第 57 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第57页.webp)

原文：

流水线总结

The BIG Picture

◼ 流水线通过增加指令的吞吐量来提升性能

◼ 并行执行多条指令

◼ 每一条指令有相同的延迟

◼ 冒险的种类

◼ 结构、数据和控制

Chapter 4 — The Processor

57

### 推测

![第 58 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第58页.webp)

原文：

推测

寻找和挖掘更大ILP的最重要方法
“猜测”指令的操作结果
- 尽快执行操作
- 检查猜测是否正确
  - 如果正确，则继续完成操作
  - 如果不正确，就回卷并执行正确的操作
- 常见的静态或者动态多发射
- 例
  - 对分支结果进行推测
    - 如果推测结果错误则回卷

### 编译器和硬件都可以推测

![第 59 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第59页.webp)

原文：

编译器和硬件都可以推测  
编译器将指令重新排序  
例，将一条指令移过分支  
硬件可以预先查找需要执行的指令  
缓存推测结果直到推测的结果得到确认  
如果推测错误将清除缓冲区  
程序的执行可以同时受到编译器、操作系统和硬件的影响.

编译器/软件推测

### 指令级并行(ILP)

![第 60 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第60页.webp)

原文：

指令级并行(ILP)

◼ 流水线：并行执行多条指令

◼ 假设我们有一个五步骤流水线MIPS CPU，如何提升性能？

◼ 两种主要的方法：

◼ 更深层次的流水线

◼ 增加流水线的深度以并行执行更多的指令

◼ 例，从一个五阶段的流水线转化为八阶段的流水线

◼ 多发射

◼ 复制计算机内部的组件，因此可以在流水线阶段启动多个指令，这种技术通常称为“多发射”

§ 4.10 Parallelism via Instructions

### 多发射

![第 61 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第61页.webp)

原文：

多发射

◼ 实现多发射处理器的两种主要方法

◼ 静态多发射

◼ 编译器将一起发射的指令分组

◼ 将指令打包到“发射槽”

编译器检测并避免冒险

◼ 动态多发射

◼ CPU检查指令流并在每个周期选择指令发射

◼ CPU在运行时使用先进技术解决冒险

Chapter 4 — The Processor

61

### 静态双发射示例

![第 62 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第62页.webp)

原文：

静态双发射示例

◼ 编译器/硬件将指令分组到“发射包”

将同一周期内发射的指令分组

◼ 两个发射包

◼ 一个 ALU/分支指令

◼ 一个读取/存储指令

<table><tr><td>Address</td><td>Instruction type</td><td colspan="7">Pipeline Stages</td></tr><tr><td>n</td><td>ALU/branch</td><td>IF</td><td>ID</td><td>EX</td><td>MEM</td><td>WB</td><td></td><td></td></tr><tr><td>n + 4</td><td>Load/store</td><td>IF</td><td>ID</td><td>EX</td><td>MEM</td><td>WB</td><td></td><td></td></tr><tr><td>n + 8</td><td>ALU/branch</td><td></td><td>IF</td><td>ID</td><td>EX</td><td>MEM</td><td>WB</td><td></td></tr><tr><td>n + 12</td><td>Load/store</td><td></td><td>IF</td><td>ID</td><td>EX</td><td>MEM</td><td>WB</td><td></td></tr><tr><td>n + 16</td><td>ALU/branch</td><td></td><td></td><td>IF</td><td>ID</td><td>EX</td><td>MEM</td><td>WB</td></tr><tr><td>n + 20</td><td>Load/store</td><td></td><td></td><td>IF</td><td>ID</td><td>EX</td><td>MEM</td><td>WB</td></tr></table>

### MIPS静态双发射

![第 63 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第63页.webp)

原文：

MIPS静态双发射

◼ 并行ALU操作和数据传输操作，这是传统的五步骤流水线不能具备的功能

◼ ALU操作需要读取两个寄存器，存储操作需要读取的寄存器超过两个

◼ 一个用于ALU操作的写端口，一个用于读取的写端口

◼ 由于ALU被ALU操作占用，我们需要一个单独的加法器来计算数据传输地址

### 静态双发射的数据通路

![第 64 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第64页.webp)

原文：

静态双发射的数据通路

◼ 双发射所需的额外硬件高亮显示

### 调度示例

![第 65 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第65页.webp)

原文：

调度示例

◼ MIPS双发射流水线对下面指令的调度

Loop: lw \$t0, 0(\$s1) addu \$t0, \$t0, \$s2 sw \$t0, 0(\$s1) addi \$s1, \$s1,–4 bne \$s1, \$zero, Loop # \$t0=array element # add scalar in \$s2 # store result # decrement pointer # branch \$s1!=0

<table><tr><td></td><td>ALU/branch</td><td>Load/store</td><td>cycle</td></tr><tr><td>Loop:</td><td>nop</td><td>lw $t0, 0($s1)</td><td>1</td></tr><tr><td></td><td>addi $s1, $s1,-4</td><td>nop</td><td>2</td></tr><tr><td></td><td>addu $t0, $t0, $s2</td><td>nop</td><td>3</td></tr><tr><td></td><td>bne $s1, $zero, Loop</td><td>sw $t0, 4($s1)</td><td>4</td></tr></table>

◼ IPC = 5/4 = 1.25 (峰值 IPC = 2)

Chapter 4 — The Processor

65

### 循环展开

![第 66 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第66页.webp)

原文：

循环展开

◼ 复制循环体获取更高的并行

◼ 减少循环控制的开销

◼ 每个复制使用不同的寄存器

◼ 称为“寄存器重命名”

◼ 避免循环展开“反相关”

◼ 存储后，读取相同的寄存器

◼ 也称“名字相关”

◼ 寄存器名的重复使用

Chapter 4 — The Processor

66

### 循环展开示例

![第 67 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第67页.webp)

原文：

循环展开示例

<table><tr><td></td><td>ALU/branch</td><td>Load/store</td><td>cycle</td></tr><tr><td>Loop:</td><td>addi $s1, $s1,-16</td><td>lw $t0, 0($s1)</td><td>1</td></tr><tr><td></td><td>nop</td><td>lw $t1, 12($s1)</td><td>2</td></tr><tr><td></td><td>addu $t0, $t0, $s2</td><td>lw $t2, 8($s1)</td><td>3</td></tr><tr><td></td><td>addu $t1, $t1, $s2</td><td>lw $t3, 4($s1)</td><td>4</td></tr><tr><td></td><td>addu $t2, $t2, $s2</td><td>sw $t0, 16($s1)</td><td>5</td></tr><tr><td></td><td>addu $t3, $t4, $s2</td><td>sw $t1, 12($s1)</td><td>6</td></tr><tr><td></td><td>nop</td><td>sw $t2, 8($s1)</td><td>7</td></tr><tr><td></td><td>bne $s1, $zero, Loop</td><td>sw $t3, 4($s1)</td><td>8</td></tr></table>

◼ IPC = 14/8 = 1.75

接近2，但是代价是寄存器和代码长度的增加

Chapter 4 — The Processor

67

### 动态多发射

![第 68 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第68页.webp)

原文：

动态多发射

◼ “超量”处理器

◼ 每个周期处理器决定是发射0条、1条还是多条指令

◼ 避免结构和数据冒险

◼ 避免编译器调度的需求

◼ 尽管它可能有所帮助

◼ 由CPU保证代码的语义

Chapter 4 — The Processor

68

### 动态流水线调度

![第 69 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第69页.webp)

原文：

动态流水线调度

◼ 允许CPU乱序执行指令以避免阻塞

◼ 但是必须按顺序将结果提交到寄存器中

◼ 示例：

$$
\begin{array}{l l l} \text {lw} & t 0, & 2 0 (s 2) \\ \text {addu} & t 1, & t 0, & t 2 \\ \text {sub} & s 4, & s 4, & t 3 \\ \text {slti} & t 5, & s 4, & 2 0 \end{array}
$$

能够开始执行sub当addu等待lw

Chapter 4 — The Processor

69

### 动态调度CPU

![第 70 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第70页.webp)

原文：

动态调度CPU

70

### 寄存器重命名

![第 71 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第71页.webp)

原文：

寄存器重命名

◼ 保留站和重排序缓冲区有效地提供了寄存器重命名机制

◼ 指令发射到保留站：

◼ 如果它的操作数在寄存器堆或重排缓冲区中可用

◼ 操作数被复制到保留站中

◼ 寄存器中的副本不在需要，其值可以覆盖

◼ 如果操作数不可用

◼ 它将由一个功能单元提供给保留站

◼ 不再需要寄存器更新

Chapter 4 — The Processor

71

### 推测

![第 72 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第72页.webp)

原文：

推测

\- 预测分支继续执行指令
  - 在分支结果确定之前不提交数据
- 读取推测
  - 避免读取和缓存丢失的延迟
    - 预测有效的地址
    - 预测读取的值
    - 在完成存储前读取
    - 绕过存储值读取单元
  - 在推测清除之前不提交负载

Chapter 4 — The Processor

72

### 为什么执行动态调度？

![第 73 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第73页.webp)

原文：

为什么执行动态调度？

◼ 为什么不让编译器调度代码？

◼ 不是所有的状态都是可以预测的

◼ 例如，缓存的丢失

◼ 不能总是围绕分支进行调度

◼ 分支结果总是动态确定的

◼ ISA的不同实现有不同的延迟和危险

Chapter 4 — The Processor

73

### 多发射有效？

![第 74 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第74页.webp)

原文：

多发射有效？

The BIG Picture

◼ 有效，但是低于我们预期的效率

◼ 程序具有限制ILP的实际依赖关系

◼ 某些依赖关系很难消除

◼ 例，指针别名

◼ 一些并行性很难发掘

◼ 指令发射期间限制窗口大小

◼ 内存延迟和带宽限制

◼ 很难保持流水线满负荷

◼ 如果做的好，推测能够有效

Chapter 4 — The Processor

74

### 能耗效率

![第 75 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第75页.webp)

原文：

能耗效率

◼ 动态调度和推测的复杂性需要能耗

◼ 多个简单的处理器可能更好

<table><tr><td>Microprocessor</td><td>Year</td><td>Clock Rate</td><td>Pipeline Stages</td><td>Issue width</td><td>Out-of-order/ Speculation</td><td>Cores</td><td>Power</td></tr><tr><td>i486</td><td>1989</td><td>25MHz</td><td>5</td><td>1</td><td>No</td><td>1</td><td>5W</td></tr><tr><td>Pentium</td><td>1993</td><td>66MHz</td><td>5</td><td>2</td><td>No</td><td>1</td><td>10W</td></tr><tr><td>Pentium Pro</td><td>1997</td><td>200MHz</td><td>10</td><td>3</td><td>Yes</td><td>1</td><td>29W</td></tr><tr><td>P4 Willamette</td><td>2001</td><td>2000MHz</td><td>22</td><td>3</td><td>Yes</td><td>1</td><td>75W</td></tr><tr><td>P4 Prescott</td><td>2004</td><td>3600MHz</td><td>31</td><td>3</td><td>Yes</td><td>1</td><td>103W</td></tr><tr><td>Core</td><td>2006</td><td>2930MHz</td><td>14</td><td>4</td><td>Yes</td><td>2</td><td>75W</td></tr><tr><td>UltraSparc III</td><td>2003</td><td>1950MHz</td><td>14</td><td>4</td><td>No</td><td>1</td><td>90W</td></tr><tr><td>UltraSparc T1</td><td>2005</td><td>1200MHz</td><td>6</td><td>1</td><td>No</td><td>8</td><td>70W</td></tr></table>

Chapter 4 — The Processor

75

### Cortex A8 & Intel i7

![第 76 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第76页.webp)

原文：

Cortex A8 & Intel i7

<table><tr><td>Processor</td><td>ARM A8</td><td>Intel Core i7 920</td></tr><tr><td>Market</td><td>Personal Mobile Device</td><td>Server, cloud</td></tr><tr><td>Thermal design power</td><td>2 Watts</td><td>130 Watts</td></tr><tr><td>Clock rate</td><td>1 GHz</td><td>2.66 GHz</td></tr><tr><td>Cores/Chip</td><td>1</td><td>4</td></tr><tr><td>Floating point?</td><td>No</td><td>Yes</td></tr><tr><td>Multiple issue?</td><td>Dynamic</td><td>Dynamic</td></tr><tr><td>Peak instructions/clock cycle</td><td>2</td><td>4</td></tr><tr><td>Pipeline stages</td><td>14</td><td>14</td></tr><tr><td>Pipeline schedule</td><td>Static in-order</td><td>Dynamic out-of-order with speculation</td></tr><tr><td>Branch prediction</td><td>2-level</td><td>2-level</td></tr><tr><td> $1^{st}$  level caches/core</td><td>32 KiB I, 32 KiB D</td><td>32 KiB I, 32 KiB D</td></tr><tr><td> $2^{nd}$  level caches/core</td><td>128-1024 KiB</td><td>256 KiB</td></tr><tr><td> $3^{rd}$  level caches (shared)</td><td>-</td><td>2-8 MB</td></tr></table>

Chapter 4 — The Processor —

76

§ 4.11 Real Stuff: The ARM Cortex-A8 and Intel Core i7 Pipelines

### ARM Cortex-A8 流水线

![第 77 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第77页.webp)

原文：

ARM Cortex-A8 流水线

Chapter 4 — The Processor

77

### ARM Cortex-A8性能

![第 78 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第78页.webp)

原文：

ARM Cortex-A8性能

Chapter 4 — The Processor

78

### Core i7流水线

![第 79 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第79页.webp)

原文：

Core i7流水线

Chapter 4 — The Processor

79

### Core i7性能

![第 80 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第80页.webp)

原文：

Core i7性能

Chapter 4 — The Processor

80

### 矩阵乘法

![第 81 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第81页.webp)

原文：

矩阵乘法

◼ 展开的C语言代码

§ 4.12 Instruction-Level Parallelism and Matrix Multiply

Chapter 4 — The Processor

81

### 矩阵乘法

![第 82 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第82页.webp)

原文：

矩阵乘法

◼ 汇编代码：

§ 4.12 Instruction-Level Parallelism and Matrix Multiply

Chapter 4 — The Processor

82

### 性能的影响

![第 83 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第83页.webp)

原文：

性能的影响

Chapter 4 — The Processor

83

### 谬论

![第 84 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第84页.webp)

原文：

谬论

◼ 流水线十分简单！

基本的想法简单

◼ 细节决定成败

◼ 例，检测数据冒险

◼ 流水线与技术无关？

◼ 为什么我们不总是使用流水线呢？

◼ 更多的晶体管使更先进的技术成为可能

◼ 与流水线相关的ISA设计需要考虑技术趋势◼ 例，指令的设计

§ 4.14 Fallacies and Pitfalls

Chapter 4 — The Processor

84

### 陷阱

![第 85 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第85页.webp)

原文：

陷阱

◼ 糟糕的ISA设计会使流水线实现更加困难

◼ 例，复杂指令集 (VAX, IA-32)

◼ 复杂指令集合导致流水线开销巨大

◼ IA-32微操作方式

◼ 例，复杂的寻找模式

◼ 寄存器更新的副作用，内存间接化

◼ 例，延迟分支

◼ 先进的流水线有很长的延迟槽

Chapter 4 — The Processor

85

### 总结

![第 86 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第86页.webp)

原文：

总结

ISA影响数据通路和控制的设计
数据通路和控制影响ISA的设计
流水线通过并行提升指令的吞吐量
■ 每秒完成更多的指令
■ 每条指令的延迟并未减少
■ 冒险：结构、数据和控制
■ 多个指令和动态调度 (ILP)
■ 依赖关系限制了可实现的并行性
■ 复杂性导致功耗极限

§ 4.14 Concluding Remarks

Chapter 4 — The Processor

86

### Backup

![第 87 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第87页.webp)

原文：

Backup

Chapter 2 — Instructions: Language of the Computer

87

### 二进制编码信息

![第 88 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第88页.webp)

原文：

二进制编码信息
- 低电压 = 0，高电压 = 1
- 一根线表示一比特
- 在多线总线上编码多位数据
组合单元
- 操作数据
- 输出是输入的函数
状态(时序)单元
- 存储信息

逻辑设计基础知识

§ 4.2 Logic Design Conventions

Chapter 4 — The Processor

88

### 组合单元

![第 89 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第89页.webp)

原文：

组合单元

◼ 与门

◼ Y = A & B

$$
\begin{array}{c} \text { A } \\ \text { B } \end{array} \text {   AND   } \text { Y }
$$

◼ 多选器

◼ $\mathsf { Y } = \mathsf { S } \ ? \ | \uparrow : | 0$

$$
\begin{array}{c}\text { I0 } \rightarrow \text { M }\\\text { I1 } \rightarrow \text { u }\\\text { x }\end{array}\rightarrow \text { Y }
$$

◼ 加法器

◼ 算术/逻辑单元

$$
Y = F (A, B)
$$

Chapter 4 — The Processor

89

### 顺序单元

![第 90 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第90页.webp)

原文：

顺序单元

◼ 寄存器：将数据存储在电路中

使用一个时钟信号决定何时更新存储值

◼ 边沿触发：当CIK从0变成1时进行数据更新

Chapter 4 — The Processor

90

### 顺序单元

![第 91 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第91页.webp)

原文：

顺序单元

◼ 写控制寄存器

◼ 只有当写控制输入为1时，才在时钟边沿触发时更新数据

◼ 当存储的值需要时使用

Chapter 4 — The Processor

91

### Clock cycle

![第 92 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第92页.webp)

原文：

Clock cycle

时钟方法

◼ 组合逻辑在时钟周期内转换数据

◼ 时钟边缘之间

◼ 状态元素的输入，状态元素的输出

◼ 最长的时间延迟决定时钟周期

State element 1

Combinational logic

State element 2

State element

Combinational logic

Chapter 4 — The Processor

92

### R型/读取/存储数据通路

![第 93 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第93页.webp)

原文：

R型/读取/存储数据通路

Chapter 4 — The Processor

93

### ALU控制

![第 94 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第94页.webp)

原文：

ALU控制

◼ ALU运用于：

◼ 读取/存储： $F { = } \mathsf { a d d }$

◼ 分支： $\mathsf { F } = \mathsf { s u b t r a c t }$

◼ R型：F 依赖funct字段

<table><tr><td>ALU control</td><td>Function</td></tr><tr><td>0000</td><td>AND</td></tr><tr><td>0001</td><td>OR</td></tr><tr><td>0010</td><td>add</td></tr><tr><td>0110</td><td>subtract</td></tr><tr><td>0111</td><td>set-on-less-than</td></tr><tr><td>1100</td><td>NOR</td></tr></table>

§ 4.4 A Simple Implementation Scheme

Chapter 4 — The Processor

94

### ALU控制

![第 95 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第95页.webp)

原文：

ALU控制

◼ 假设2位ALUOp从操作码派生

◼ 组合逻辑派生ALU控制

<table><tr><td>opcode</td><td>ALUOp</td><td>Operation</td><td>funct</td><td>ALU function</td><td>ALU control</td></tr><tr><td>lw</td><td>00</td><td>load word</td><td>XXXXXX</td><td>add</td><td>0010</td></tr><tr><td>sw</td><td>00</td><td>store word</td><td>XXXXXX</td><td>add</td><td>0010</td></tr><tr><td>beq</td><td>01</td><td>branch equal</td><td>XXXXXX</td><td>subtract</td><td>0110</td></tr><tr><td rowspan="5">R-type</td><td rowspan="5">10</td><td>add</td><td>100000</td><td>add</td><td>0010</td></tr><tr><td>subtract</td><td>100010</td><td>subtract</td><td>0110</td></tr><tr><td>AND</td><td>100100</td><td>AND</td><td>0000</td></tr><tr><td>OR</td><td>100101</td><td>OR</td><td>0001</td></tr><tr><td>set-on-less-than</td><td>101010</td><td>set-on-less-than</td><td>0111</td></tr></table>

Chapter 4 — The Processor

95

### 实现跳转

![第 96 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第96页.webp)

原文：

实现跳转

<table><tr><td rowspan="2">Jump</td><td>2</td><td>address</td></tr><tr><td>31:26</td><td>25:0</td></tr></table>

◼ 使用字地址跳转

◼ 下列3部分拼接为跳转地址

◼ 旧PC的高4位

◼ 26位跳转地址

◼ 00

◼ 需要一个额外的控制信号从操作码解码

Chapter 4 — The Processor

96

### 添加跳转的数据通路

![第 97 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第97页.webp)

原文：

添加跳转的数据通路

Chapter 4 — The Processor

97

### MIPS流水线数据通路

![第 98 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第98页.webp)

原文：

MIPS流水线数据通路

WB: Write back

§ 4.6 Pipelined Datapath and Contro

Chapter 4 — The Processor

98

### 流水线寄存器

![第 99 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第99页.webp)

原文：

流水线寄存器

◼ 各个步骤之间需要寄存器

◼ 存储上一个周期产生的数据

Chapter 4 — The Processor

99

### 流水线操作

![第 100 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第100页.webp)

原文：

流水线操作

◼ 通过流水线通路的指令周期流

◼ “单个时钟周期”流水线图

◼ 显示单个周期中流水线的使用

◼ 使用的资源高亮显示

◼ 比较“多个时钟周期”流水线图

◼ 随时间的运行图

◼ 我们将观察“单个时钟周期”读取/存储

Chapter 4 — The Processor —

100

### 读取/存储IF

![第 101 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第101页.webp)

原文：

读取/存储IF

Chapter 4 — The Processor —

101

### 读取/存储ID

![第 102 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第102页.webp)

原文：

读取/存储ID

Chapter 4 — The Processor — 102

### 读取EX

![第 103 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第103页.webp)

原文：

读取EX

Chapter 4 — The Processor — 103

### 读取MEM

![第 104 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第104页.webp)

原文：

读取MEM

Chapter 4 — The Processor — 104

### Iw Write back

![第 105 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第105页.webp)

原文：

Iw Write back

读取WB

Chapter 4 — The Processor — 105

### 读取的数据通路

![第 106 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第106页.webp)

原文：

读取的数据通路

Chapter 4 — The Processor — 106

### 存储EX

![第 107 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第107页.webp)

原文：

存储EX

Chapter 4 — The Processor — 107

### 存储MEM

![第 108 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第108页.webp)

原文：

存储MEM

Chapter 4 — The Processor — 108

### 存储WB

![第 109 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第109页.webp)

原文：

存储WB

Chapter 4 — The Processor — 109

### 多时钟周期流水线图

![第 110 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第110页.webp)

原文：

多时钟周期流水线图

◼ 描述每个步骤中使用的物理资源

Chapter 4 — The Processor —

110

### 多时钟周期流水线图

![第 111 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第111页.webp)

原文：

多时钟周期流水线图

◼ 传统描述名称的形式

<table><tr><td colspan="9">Time (in clock cycles)</td></tr><tr><td>CC 1</td><td>CC 2</td><td>CC 3</td><td>CC 4</td><td>CC 5</td><td>CC 6</td><td>CC 7</td><td>CC 8</td><td>CC 9</td></tr></table>
Program execution order (in instructions)

<table><tr><td>lw $10, 20($1)</td><td>Instruction fetch</td><td>Instruction decode</td><td>Execution</td><td>Data access</td><td>Write back</td><td colspan="3"></td></tr><tr><td>sub $11, $2, $3</td><td></td><td>Instruction fetch</td><td>Instruction decode</td><td>Execution</td><td>Data access</td><td>Write back</td><td colspan="2"></td></tr><tr><td>add $12, $3, $4</td><td></td><td></td><td>Instruction fetch</td><td>Instruction decode</td><td>Execution</td><td>Data access</td><td>Write back</td><td></td></tr><tr><td>lw $13, 24($1)</td><td></td><td></td><td></td><td>Instruction fetch</td><td>Instruction decode</td><td>Execution</td><td>Data access</td><td>Write back</td></tr><tr><td>add $14, $5, $6</td><td></td><td></td><td></td><td></td><td>Instruction fetch</td><td>Instruction decode</td><td>Execution</td><td>Data access</td></tr></table>

Chapter 4 — The Processor

111

### 单时钟周期流水线图

![第 112 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第112页.webp)

原文：

单时钟周期流水线图

◼ 在给定周期内流水线状态

<table><tr><td>add $14, $5, $6</td><td>lw $13, 24 ($1)</td><td>add $12, $3, $4</td><td>sub $11, $2, $3</td><td>lw $10, 20($1)</td></tr><tr><td>Instruction fetch</td><td>Instruction decode</td><td>Execution</td><td>Memory</td><td>Write-back</td></tr></table>

Chapter 4 — The Processor —

112

### 流水线控制(简化)

![第 113 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第113页.webp)

原文：

流水线控制(简化)

Chapter 4 — The Processor —

113

### 流水线控制

![第 114 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第114页.webp)

原文：

流水线控制

◼ 指令派生控制信号

◼ 像在一个时钟周期内实现

Chapter 4 — The Processor

114

### 流水线控制

![第 115 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第115页.webp)

原文：

流水线控制

Chapter 4 — The Processor —

115

### ALU指令中数据冒险

![第 116 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第116页.webp)

原文：

ALU指令中数据冒险

◼ 考虑下面汇编代码序列：

◼ 我们使用前推解决冒险◼ 前推时如何检测冒险？

§ 4.7 Data Hazards: Forwarding vs. Stalling

Chapter 4 — The Processor

116

### 依赖 & 前推

![第 117 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第117页.webp)

原文：

依赖 & 前推

Chapter 4 — The Processor —

117

### 检测需要前推的

![第 118 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第118页.webp)

原文：

检测需要前推的

◼ 沿流水线传递寄存器号

◼ 例，ID/EX.RegisterRs 表示一个需要流水线寄存器ID/EX获得的原寄存器号

◼ 在EX步骤中ALU操作数寄存器编号由下列方法给定：

◼ ID/EX.RegisterRs, ID/EX.RegisterRt

◼ 发生数据冒险的情况：

1a. EX/MEM.RegisterRd = ID/EX.RegisterRs

1b. EX/MEM.RegisterRd = ID/EX.RegisterRt

2a. MEM/WB.RegisterRd = ID/EX.RegisterRs

2b. MEM/WB.RegisterRd = ID/EX.RegisterRt

Fwd from EX/MEM pipeline reg

Fwd from MEM/WB pipeline reg

Chapter 4 — The Processor —

118

### 检测需要前推的

![第 119 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第119页.webp)

原文：

检测需要前推的

◼ 但是只有当前推指令写入寄存器！

◼ EX/MEM.RegWrite, MEM/WB.RegWrite

◼ 并且只有指令的Rd不为\$zero

◼ EX/MEM.RegisterRd ≠ 0, MEM/WB.RegisterRd ≠ 0

Chapter 4 — The Processor

119

### 前推路径

![第 120 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第120页.webp)

原文：

前推路径

Chapter 4 — The Processor —

120

### 前推条件

![第 121 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第121页.webp)

原文：

前推条件

◼ EX冒险

◼ if (EX/MEM.RegWrite and (EX/MEM.RegisterRd ≠ 0) and (EX/MEM.RegisterRd = ID/EX.RegisterRs)) ForwardA = 10

◼ if (EX/MEM.RegWrite and (EX/MEM.RegisterRd ≠ 0) and (EX/MEM.RegisterRd = ID/EX.RegisterRt)) ForwardB = 10

MEM冒险

◼ if (MEM/WB.RegWrite and (MEM/WB.RegisterRd ≠ 0) and (MEM/WB.RegisterRd = ID/EX.RegisterRs)) ForwardA = 01

◼ if (MEM/WB.RegWrite and (MEM/WB.RegisterRd ≠ 0) and (MEM/WB.RegisterRd = ID/EX.RegisterRt)) ForwardB = 01

Chapter 4 — The Processor —

121

### 多个数据冒险

![第 122 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第122页.webp)

原文：

多个数据冒险

◼ 考虑下列汇编序列：

add \$1,\$1,\$2 add \$1,\$1,\$3 add \$1,\$1,\$4

◼ 两种冒险都发生：

◼ 想要使用最新的结果

◼ 修订MEM冒险条件

◼ 只有EX冒险情况不正确才前推

Chapter 4 — The Processor

122

### 修改的前推条件

![第 123 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第123页.webp)

原文：

修改的前推条件

◼ MEM冒险

Chapter 4 — The Processor —

123

### 使用前推的数据通路

![第 124 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第124页.webp)

原文：

使用前推的数据通路

Chapter 4 — The Processor —

124

### 装载-使用数据冒险

![第 125 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第125页.webp)

原文：

装载-使用数据冒险

Chapter 4 — The Processor —

125

### 装载-使用冒险检测

![第 126 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第126页.webp)

原文：

装载-使用冒险检测

◼ 当使用的指令在ID步骤内解码时进行检查

◼ 在ID步骤中，ALU操作数寄存器编号确定方式：

◼ IF/ID.RegisterRs, IF/ID.RegisterRt

◼ 发生装载-使用冒险的条件

◼ ID/EX.MemRead and

((ID/EX.RegisterRt = IF/ID.RegisterRs) or

(ID/EX.RegisterRt = IF/ID.RegisterRt))

◼ 如果检测到，阻塞流水线并插入气泡

Chapter 4 — The Processor —

126

### 如何阻塞流水线

![第 127 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第127页.webp)

原文：

如何阻塞流水线

◼ 使得寄存器ID/EX中的控制值为0

◼ EX,、MEM和WB指令不产生任何效果，空指令

◼ 避免PC和IF/ID寄存器的更新

◼ 再次解码使用的指令

◼ 再次获取后面的指令

◼ 1周期的阻塞允许MEM从lw指令读取数据

◼ 能够立即前推到EX步骤

Chapter 4 — The Processor —

127

### 流水线中的阻塞/气泡

![第 128 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第128页.webp)

原文：

流水线中的阻塞/气泡

Chapter 4 — The Processor —

128

### 流水线中的阻塞和气泡

![第 129 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第129页.webp)

原文：

流水线中的阻塞和气泡

Chapter 4 — The Processor —

129

### 冒险检测的数据通路

![第 130 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第130页.webp)

原文：

冒险检测的数据通路

Chapter 4 — The Processor —

130

### 阻塞和性能

![第 131 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第131页.webp)

原文：

阻塞和性能

The BIG Picture

◼ 阻塞降低性能

◼ 但为了得到正确的结果需要阻塞

◼ 编译能够重新排列代码以避免冒险和阻塞 ◼ 需要流水线结构的知识

Chapter 4 — The Processor

131

### 分支冒险

![第 132 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第132页.webp)

原文：

分支冒险

◼ 如果分支结果在MEM级确定

Flush these instructions (Set control values to 0)

§ 4.8 Control Hazards

Chapter 4 — The Processor

132

### 缩短分支延迟

![第 133 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第133页.webp)

原文：

缩短分支延迟

◼ 分支结果提前到ID步骤确定

◼ 目标地址加法器

◼ 寄存器比较器

◼ 例：分支发生

Chapter 4 — The Processor

133

### 分支发生示例

![第 134 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第134页.webp)

原文：

分支发生示例

Chapter 4 — The Processor —

134

### 分支发生示例

![第 135 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第135页.webp)

原文：

分支发生示例

Chapter 4 — The Processor —

135

### 分支数据冒险

![第 136 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第136页.webp)

原文：

分支数据冒险

◼ 如果比较寄存器是ALU指令之前的第2或第3 条指令的目的地

add \$1, \$2, \$3 IF ID EX MEM WB add \$4, \$5, \$6 IF ID EX MEM WB IF ID EX MEM WB beq \$1, \$4, target IF ID EX MEM WB

◼ 能够使用前推解决

Chapter 4 — The Processor —

136

### 分支数据冒险

![第 137 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第137页.webp)

原文：

分支数据冒险

◼ 如果比较寄存器是ALU指令之前的第2或第3 条指令的目的地

需要阻塞一个周期

lw \$1, addr

add \$4, \$5, \$6

beq stalled

beq \$1, \$4, target

Chapter 4 — The Processor

137

### 分支数据冒险

![第 138 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第138页.webp)

原文：

分支数据冒险

◼ 如果比较寄存器是紧靠前的读取指令的目的地◼ 需要阻塞两个周期

lw \$1, addr

beq stalled

beq stalled

beq \$1, \$0, target

Chapter 4 — The Processor

138

### 动态分支预测

![第 139 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第139页.webp)

原文：

动态分支预测

◼ 使用更深和超标量的流水线时，分支的代价也越大

◼ 使用动态分支

◼ 分支预测缓存 (分支历史记录表)

◼ 由最近的分支指令地址索引

◼ 存储输出 (取/未取)

◼ 执行分支

◼ 检查表，期望相同的输出

◼ 开始从目标或失败处获取

◼ 如果失败，刷新流水线并翻转预测位

Chapter 4 — The Processor

139

### 1-Bit预测位的缺点

![第 140 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第140页.webp)

原文：

1-Bit预测位的缺点

◼ 内部循环分支两次错误预测

$$
\begin{array}{c} \text {outer: ... } \\ \text {inner: ... } \\ \text {...} \\ \text {beq ..., ..., inner} \\ \text {...} \\ \text {beq ..., ..., outer} \end{array}
$$

◼ 内部循环的最后一次迭代中出现错误预测

◼ 然后，错误预测并没有出现在下一次内部循环的第一次迭代周围

Chapter 4 — The Processor —

140

### 2-Bit预测位

![第 141 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第141页.webp)

原文：

2-Bit预测位

◼ 只有连续两次错误预测才会改变预测

Taken

Predict taken

Not taken

Taken

Predict not taken

Not taken

Taken

Predict taken

Not taken

Taken

Predict not taken

Not taken

Chapter 4 — The Processor

141

### 计算分支目标

![第 142 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第142页.webp)

原文：

计算分支目标

◼ 即使有了预测器，仍然需要计算目标地址◼ 一个分支需要一个时钟周期为代价

◼ 分支目标缓冲区

◼ 目标地址的缓存

◼ 指令获取时PC索引

◼ 如果命中并指令是分支预测发生，则可以立即获取目标

Chapter 4 — The Processor —

142

### 异常和中断

![第 143 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第143页.webp)

原文：

异常和中断

◼ “异常”事件要求控制流的变化

◼ 不同的ISA使用不同的术语

◼ 异常

出现在CPU内部

◼ 例，未定义的操作码、溢出、系统调用…

◼ 中断

◼ 来自外部的I/O控制器

◼ 在不牺牲性能的前提下处理中断和异常是困难的

§ 4.9 Exceptions

Chapter 4 — The Processor —

143

### 解决异常

![第 144 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第144页.webp)

原文：

解决异常

◼ 在MIPS中，由系统控制协处理器(CP0)管理异常

◼ 保存违规(中断)指令的PC

◼ 在MIPS中：异常程序计数器(EPC)

◼ 记录异常产生的原因

◼ 在MIPS中，Cause寄存器

◼ 我们使用1位数据：

0表示未定义操作码，1表示溢出

◼ 跳转到地址为8000 00180的中断处理系统

Chapter 4 — The Processor —

144

### An Alternate Mechanism

![第 145 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第145页.webp)

原文：

An Alternate Mechanism

◼ 向量中断

◼ 由异常原因决定中断控制转移地址的中断

◼ 例子：

◼ 未定义指令： C000 0000

◼ 算术溢出： C000 0020

◼ C000 0040

◼ 指令的行为：

◼ 处理中断，或者

◼ 跳转到实际处理系统

Chapter 4 — The Processor

145

### 处理程序

![第 146 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第146页.webp)

原文：

处理程序

◼ 读取异常原因，跳转到相应的处理程序

◼ 决定需要的处理行动

◼ 如果可以重新开始

◼ 采取正确的行动

◼ 使用EPC返回程序

◼ 否则

◼ 终止程序

◼ 使用EPC、cause…寄存器报告错误原因

Chapter 4 — The Processor —

146

### 流水线中的异常

![第 147 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第147页.webp)

原文：

流水线中的异常

◼ 另一种形式的控制冒险

◼ 考虑add在EX步骤的算术溢出 add \$1, \$2, \$1

◼ 防止寄存器\$1被冲掉

◼ 完成先前的指令

◼ 刷新add和后续指令

◼ 设置Cause和EPC寄存器值

◼ 将控制转交给处理程序

◼ 类似于错误预测分支

◼ 使用大量相同的硬件

Chapter 4 — The Processor —

147

### 处理异常的数据通路

![第 148 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第148页.webp)

原文：

处理异常的数据通路

Chapter 4 — The Processor —

148

### 异常属性

![第 149 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第149页.webp)

原文：

异常属性

◼ 可重新开始的异常

◼ 流水线刷新指令

◼ 处理程序执行，然后返回到指令

◼ 重新获取并重新执行

◼ PC保存在寄存器EPC中

◼ 识别指令异常的原因

◼ 实际上保存的是PC+4

◼ 处理程序必须对地址进行调整

Chapter 4 — The Processor

149

### 异常示例

![第 150 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第150页.webp)

原文：

异常示例

◼ 程序中add指令的异常：

$$
\begin{array}{l l l l l} 4 0 & \text {sub} & \mathbb {S} 1 1, & \mathbb {S} 2, & \mathbb {S} 4 \\ 4 4 & \text {and} & \mathbb {S} 1 2, & \mathbb {S} 2, & \mathbb {S} 5 \\ 4 8 & \text {or} & \mathbb {S} 1 3, & \mathbb {S} 2, & \mathbb {S} 6 \\ 4 C & \text {add} & \mathbb {S} 1, & \mathbb {S} 2, & \mathbb {S} 1 \\ 5 0 & \text {slt} & \mathbb {S} 1 5, & \mathbb {S} 6, & \mathbb {S} 7 \\ 5 4 & \text {lw} & \mathbb {S} 1 6, & \mathbb {S} 0 (\mathbb {S} 7) \end{array}
$$

◼ 异常处理程序

$$
\begin{array}{l l l l} 8 0 0 0 0 1 8 0 & \text {sw} & \mathbb {S} 2 5, & 1 0 0 0 (\mathbb {S} 0) \\ 8 0 0 0 0 1 8 4 & \text {sw} & \mathbb {S} 2 6, & 1 0 0 4 (\mathbb {S} 0) \end{array}
$$

Chapter 4 — The Processor —

150

### 异常示例

![第 151 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第151页.webp)

原文：

异常示例

Chapter 4 — The Processor —

151

### 异常示例

![第 152 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第152页.webp)

原文：

异常示例

Chapter 4 — The Processor —

152

### 多个异常

![第 153 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第153页.webp)

原文：

多个异常

\- 流水线中有5条活动的指令
  - 可能同时发生多个异常
- 简单的方法：从最早执行的指令开始处理异常
  - 缓冲后续指令
  - “精确”异常“
- 在复杂的流水线中
  - 每个周期多条指令发射
  - 无序完成
  - 维护精确的异常是困难的

Chapter 4 — The Processor —

153

### 非精确异常

![第 154 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第154页.webp)

原文：

非精确异常

◼ 停止流水线并保存状态

◼ 包括异常原因

◼ 让处理程序处理

◼ 哪一条指令发生异常

◼ 哪一个需要完成或者刷新

◼ 可能需要“手动”完成

◼ 简化硬件，但是需要更加复杂的处理软件

◼ 对于复杂多指令无序流水线无效

Chapter 4 — The Processor —

154

### 双发射MIPS冒险

![第 155 页](计算机组成与结构第6章-MIPS32CPU设计课件.assets/第155页.webp)

原文：

双发射MIPS冒险

◼ 更多的指令并行执行

◼ EX数据冒险

◼ 前推避免了单发射的阻塞

现在不能使用ALU结果在相同的包读取/存储

◼ add \$t0, \$s0, \$s1 load \$s2, 0(\$t0)

◼ 切割成两个包，只有一个阻塞周期

◼ 装载-使用冒险

◼ 两条指令，但是一周期使用延迟

◼ 需要更多激进的调度方案

Chapter 4 — The Processor —

155
