---
title: 《计算机系统基础Ⅰ》DATALAB实验手册
kind: 实验
course: 计算机系统基础
term: 2023-2024-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90JS140401S%E3%80%91%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F%E5%9F%BA%E7%A1%80%E2%85%A0%EF%BC%88%E6%B7%B7%E5%90%88%E5%BC%8F%EF%BC%89/labs/datalab/DATALAB%E5%AE%9E%E9%AA%8C%E6%89%8B%E5%86%8C.pdf
---

# 《计算机系统基础Ⅰ》DATALAB实验手册

原件经识别和整理；“参考解答”是我们补的。

# 一、实验目的

熟悉整数的位级表示和浮点数字，具体内容是实现 C 程序中空缺的部分代码。

## 二、实验过程

1. **登录您的 10.160.106.190 帐户**

   username=学号

   >>>>>在本地机器上>>>>>

   连接服务器:

   ```bash
   ssh username@10.160.106.190
   ```

   默认密码:

   ```text
   2024ics1
   ```

   >>>>>在服务器上>>>>>

   修改密码:

   ```bash
   passwd username
   ```

2. **下载实验程序**

   在 ubuntu 的浏览器输入 `http://10.160.106.190/datalab-handout.tar`

   或在命令行:

   ```bash
   wget http://10.160.106.190/datalab-handout.tar
   ```

3. **解压代码**

   使用以下命令解压刚下载的代码：

   ```bash
   tar -xvf datalab-handout.tar
   ```

   然后检查是否有名为 `datalab-handout` 目录。

4. **进入目录并检查文件**

   进入目录，检查是否存在以下代码（总共 14 个文件）：

   - `bits.c`
   - `bits.h`
   - `btest.c`
   - `btest.h`
   - `decl.c`
   - `dlc`
   - `Driverhdrs.pm`
   - `Driverlib.pm`
   - `driver.pl`
   - `fshow.c`
   - `ishow.c`
   - `Makefile`
   - `README`
   - `tests.c`

5. **编辑实现文件**

   要实现的文件是 `bits.c`。使用文本编辑器，如 `gedit`、`nano`、`vi` 等。在您完成程序后编辑、修改和保存 `bits.c`。

## 三、任务描述

- `bits.c` 文件包含 15 个编程谜题中每个谜题的框架。这个实验用我们刚刚在第 2 章中学到的知识来完成这些程序中缺失的部分。
- DATALAB 实验每个谜题开头注释部分给出了题目的要求、限制条件，请仔细阅读。

## 四、测试

你可以在完成程序每个谜题后立即测试你编写程序完成情况。

1. **dlc 测试**：目的是检查是否符合编码规则。
   
   用法：
   ```bash
   ./dlc bits.c
   ```

2. **btest 测试**：目的是测试函数的功能是否正确实现。
   
   用法：
   ```bash
   make
   # 会有警告信息，忽略，继续下一步
   ./btest
   ```

3. **driver.pl 测试**：目的是计算你的分数。

## 五、实验程序提交

1. 确保文件 `bits.c` 已被修改并保存。
2. 以 C 语言注释的形式在 `bits.c` 上方写下你的姓名和学号。
3. 在个人目录下创建子目录 `lab1`。
4. 将文件 `bits.c` 和实验报告复制到子目录 `lab1` 中。

   实验报告命名格式：`学号姓名 lab1.doc(x)`

   >>>>>在本地机器上>>>>>

## 七、通知

1. **截止日期**：2024.4.7
2. 由于正在使用实验室作业自动收集系统，如果出现以下情况之一，系统会认为你没有提交作业：
   - （1）子目录 `lab1` 及其文件 `bits.c` 没有被发现；
   - （2）存在文件 `bits.c`，但没有子目录 `lab1`。
3. 当实验室提交日期过期时，您不能在子目录上写任何内容。
4. 这个运行于 `10.160.106.190` 的实验室系统在我们的校园内。如果你在我们的外面校园，请使用南邮 VPN 客户端程序 ENWAgent。
