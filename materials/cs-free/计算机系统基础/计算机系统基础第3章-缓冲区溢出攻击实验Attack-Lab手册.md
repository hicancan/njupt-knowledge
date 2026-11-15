---
title: 《计算机系统基础》第3章 缓冲区溢出攻击实验（Attack Lab）手册
kind: 实验
course: 计算机系统基础
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90JS140401S%E3%80%91%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F%E5%9F%BA%E7%A1%80%E2%85%A0%EF%BC%88%E6%B7%B7%E5%90%88%E5%BC%8F%EF%BC%89/labs/attacklab/ATTACKLAB%E5%AE%9E%E9%AA%8C%E6%89%8B%E5%86%8C.pdf
---

# 《计算机系统基础》第3章 缓冲区溢出攻击实验（Attack Lab）手册

原件经识别和整理；“参考解答”是我们补的。

## 一、实验目的

通过实现缓冲区溢出攻击，熟悉理解过程调用规则，包括控制的传递、参数的传递以及栈帧结构、缓冲区溢出问题等，了解缓冲区溢出保护，并进一步加深对理论课程中关于程序的机器级表示各方面知识点的理解，以及反汇编、跟踪分析/调试等常用技能的掌握。

## 二、实验内容

作为实验目标的存在缓冲区溢出漏洞的可执行程序共有两个：ctarget 和 rtarget。对目标程序实施缓冲区溢出攻击（buffer overflow attacks）。通过造成缓冲区溢出来破坏目标程序的栈帧结构，继而不再返回原来的调用程序，而是转向执行指定的子程序，要求 level1 转向 touch1 子程序，level2 转向 touch2 子程序，level3 转向 touch3 子程序。

### level1

构造攻击字符串作为目标程序输入，造成缓冲区溢出，使 getbuf() 返回时不返回到原来的调用函数，而是转向执行 touch1。

构造攻击字符串造成缓冲区溢出，使目标程序调用 touch2 函数，并将 cookie 值作为参数传递给 touch2 函数，使 touch 函数中的判断成功，需要在缓冲区中注入指令 movq 将 cookie 传送给 rdi 寄存器作为入口参数。

构造攻击字符串，使目标程序调用 touch3 函数，将数组指针作为入口参数，使相应判断成功。

要求对 ctarget 实施代码注入攻击（code injection），包含 3 个阶段，分别对应三个 level：level1、level2 和 level3。对 rtarget 实施面向返回的编程攻击（return-oriented programming）。rtarget 包含 2 个 level：level2 和 level3。

rtarget 程序开启了栈随机化、栈不可以执行这两个保护策略。所以需要通过面向返回编程来完成第一部分 level 和 level 实验，也就是巧妙地利用程序中的 gadget 指令，gadget 指一段以 ret 指令结尾的指令序列。通过调用这些代码，攻击者可以在拥有更简单攻击防范的程序内执行任意操作（具体请查阅网上相应的资料）。

## 三、实验过程

### 第 1 步、获取炸弹程序

在 ubuntu 上通过浏览器输入 http://10.160.106.190:15513 后，会出现下面炸弹申请页面：

### CS:APP Attack Lab Target Request

Fill in the form and then click the Submit button once to download your unique target.

Hit the Reset button to get a clean form.

Legal characters are spaces, letters, numbers, underscores ('\_'), hyphens ('-'), at signs ('@'), and dots ('.').

Reset

输入您的用户名（即学号）和电子邮箱地址，然后点击提交按钮。服务器会生成你的程序，并在浏览器返回一个名为 target.tar 的 tar 文件，其中 k 是你程序唯一编号。targetk.tar 文件将存储在你的“下载”子目录中。

注意：等待时间比炸弹程序要长，请耐心等待，不要反复按提交按钮。

文件解压后共有以下这些文件，由于目前 CMU 提供的程序依赖较低版本的 glibc，ctarget 在现在高版本的 ubuntu 下无法正确运行，必须在运行时加载一个动态链接库 printf.so，因此请各位同学在 ubuntu 的浏览器输入 http://10.160.106.190/printf.so，下载该文件。

### 第 2 步：程序上传至服务器

（1）在本地虚拟机下载目录下，将缓冲区溢出攻击程序拷贝到服务器你的目录下。

（2）登录您的 10.160.106.190 帐户：

>>>>> 在本地机器上 >>>>>

连接服务器：

```
ssh username@10.160.106.190
```

（3）运行解压命令：

```
tar -xvf targetk.tar
```

解压后，它将创建一个目录 targetk，在此目录下会包含以下三个文件：

- cookie.txt：基于学号产生 4 字节序列，如 0x5f405c9a，称为“cookie”
- ctarget：可执行的二进制程序，易遭受目标代码攻击。
- rtarget：可执行的二进制程序，易遭受面向返回的编程攻击。
- farm.c：用于实施面向返回的编程攻击需要的 gadget 指令。
- hex2raw：可执行程序，字符串格式转换程序。

（4）在本地虚拟机下载目录下，将 printf.so 拷贝到服务器 targetk 目录下：

```
scp printf.so username@10.160.106.190:/home/username/targetk
```

### 第 3 步：进行 ctarget 攻击实验

（1）首先进入服务器 targetk 目录，反汇编 ctarget 程序中的代码，重点阅读 getbuf 子程序和 touch1、touch2、touch3 子程序。

```
objdump -d ctarget
```

（2）构造攻击字符串的 ASCII 码，使用文本编辑器保存在文本文件中（如 ctarget.l1）（十六进制格式），如：

```
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00
01 40 30 40 00 00 00 00
```

（3）使用 hex2raw 程序将 ctarget.l1 文件中数字对序列转化为对应的字节序列保存在另一个文本文件中如 clevel1.txt：

```
./hex2raw < ctarget.l1 > clevel1.txt
```

（4）进行攻击

情况 1：不通知服务器

```
LD_PRELOAD=./printf.so ./ctarget < clevel1.txt -q
```

攻击成功显示如下：

攻击失败可能显示如下：

情况 2：通知服务器，计算成绩

```
LD_PRELOAD=./printf.so ./ctarget < clevel1.txt
```

攻击成功显示如下：

攻击失败可能显示如下：

注意：如果显示如下结果，请查看记分牌成绩，如果计分成功，则表明攻击成功。

通过浏览器输入 http://10.160.106.190:15513/scoreboard，查看记分牌来了解自己的实验成绩。

注：也可如下使用管道操作符“|”连接 hex2raw 和 ctarget：

```
cat ctarget.l1 | ./hex2raw | LD_PRELOAD=./printf.so ./ctarget
```

（5）跟踪调试程序

### 第 4 步：进行 rtarget 攻击实验（不需要 printf.so）

（1）首先进入服务器 targetk 目录，反汇编 rtarget 程序中的代码，重点阅读 getbuf 子程序和 touch2、touch3 子程序。

```
objdump -d ctarget
```

（2）构造攻击字符串的 ASCII 码，使用文本编辑器保存在文本文件中（如 ctarget.l1）（十六进制格式），如：

（3）使用 hex2raw 程序将 rtarget.l2 文件中数字对序列转化为对应的字节序列保存在另一个文本文件中如 rlevel2.txt：

```
./hex2raw < rtarget.l2 > rlevel2.txt
```

## 三、实验程序提交

1. 在个人目录下创建子目录 lab3。

4. 将攻击字符串文件：ctarget.l1, ctarget.l2, ctarget.l3, rtarget.l2, rtarget.l3 和实验报告复制到子目录 lab3 中。

实验报告命名格式：学号姓名 lab3.docx

## 四、通知

1. 截止日期：2024.6.30

2. 当实验室提交日期到期时，我们将从子目录中取走符合命名格式的作业，延迟提交或不符合命名格式的作业将不会被取走。

3. 这个运行于 10.160.106.190 的实验室系统在我们的校园内。如果你在我们的校园外，请使用南邮 VPN 客户端程序 ENWAgent。
