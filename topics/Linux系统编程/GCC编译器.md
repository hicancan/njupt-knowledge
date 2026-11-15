---
title: GCC编译器的使用与编译过程（预处理、编译、汇编、链接）
requires: []
---

# GCC编译器的使用与编译过程（预处理、编译、汇编、链接）

## 从一个问题开始

如果让你把 `hello.c` 变成一个可以直接运行的程序，你猜中间会发生什么？

其实 GCC 并不是“一步”把它翻译成可执行文件的。它内部悄悄走了四步：预处理、编译、汇编、链接。理解这四步，是后面写 Makefile、调库、排错的基础。

```mermaid
flowchart LR
    A["hello.c<br>源文件"] -->|预处理| B["hello.i<br>展开宏/头文件"]
    B -->|编译| C["hello.s<br>汇编代码"]
    C -->|汇编| D["hello.o<br>目标文件"]
    D -->|链接| E["hello<br>可执行文件"]
```

## GCC 是什么

GCC（GNU Compiler Collection）是 Linux 下最常用的编译器，支持 C、C++ 等语言。

> [!IMPORTANT]
> GCC 在 Linux 中的地位类似 Windows 下的 Visual Studio 中的编译器部分，但 ==GCC 本身只是命令行编译器==，不带 IDE 图形界面。

## 四步编译过程

### 预处理（Preprocessing）

处理 `#include`、`#define`、`#ifdef` 等以 `#` 开头的指令，展开宏和头文件，输出 `.i` 文件。

```bash
gcc -E hello.c -o hello.i
```

### 编译（Compilation）

把预处理后的代码翻译成汇编代码，输出 `.s` 文件。

```bash
gcc -S hello.i -o hello.s
```

### 汇编（Assembly）

把汇编代码翻译成机器指令，输出 `.o` 目标文件（二进制，但还不能运行）。

```bash
gcc -c hello.s -o hello.o
```

### 链接（Linking）

把 `.o` 文件和库文件合并，解决符号引用，生成最终可执行文件。

```bash
gcc hello.o -o hello
```

所以判断 3 是对的——`gcc -o hello hello.c` 会把这四步一次性做完，但这只是“表面上的一步”。

## 静态库与共享库

链接阶段要用到库。Linux 下有两种主要形式：

| 类型 | 扩展名 | 链接时机 | 产物依赖 | 运行速度 | 更新维护 |
|------|--------|----------|----------|----------|----------|
| 静态库 | `.a` | 编译链接时嵌入 | 不需带库 | 较快 | 需重新编译 |
| 共享库 | `.so` | 运行时动态加载 | 需带 `.so` | 稍慢 | 替换 `.so` 即可 |

> [!TIP]
> 记忆：`.a` = archive（归档），就是一堆 `.o` 打成的包；`.so` = shared object。

> [!WARNING]
> 做选择题时注意看问的是“静态库”还是“共享库”：静态库选 `.a`，共享库选 `.so`。Windows 的 DLL 在 Linux 下不适用。

### 三个概念的辨析

- **静态库**：链接时把库代码直接复制进可执行文件。
- **共享库**：Linux 下的动态库，后缀 `.so`，运行时由动态链接器加载。
- **动态链接库**：Windows 中的概念（DLL），机制与 Linux 共享库类似，但不是同一文件格式。

> [!NOTE]
> 共享库就是 Linux 下的“动态链接库”对应物，但考试如果考扩展名，Linux 下只认 `.so`。

### 各自优缺点

**静态库 `.a`**

- 优点：运行时不依赖外部库，部署简单。
- 缺点：可执行文件体积大，库更新后必须重新编译所有用到它的程序。

**共享库 `.so`**

- 优点：可执行文件小，多个进程可共享同一份库代码，节省内存；库升级无需重新编译程序。
- 缺点：运行时必须能找到 `.so` 文件，否则报 `cannot open shared object file`；存在版本兼容问题。

> [!IMPORTANT]
> ==静态库链接进可执行文件，共享库运行时才加载。== 这是两者的根本区别。

## 和 Makefile 的关系

当项目有几十上百个 `.c` 文件时，手动一条条敲 `gcc` 不现实，而且改一个文件不想全部重新编译。Makefile 就是用来管理“哪些文件需要重新编译、链接命令怎么执行”的脚本。

> [!NOTE]
> 判断 7 是对的：Linux 下用 C++ 开发大规模软件时，编译和连接常使用 Makefile。

## 一个算对的例子

有 `hello.c`，内容含 `#include <stdio.h>` 和 `printf`。执行：

```bash
gcc -o hello hello.c
./hello
```

输出 `Hello, Linux!`

解析：`gcc -o hello hello.c` 经历了预处理（展开 `stdio.h`，产生 `.i`）→ 编译（生成 `.s` 汇编）→ 汇编（生成 `.o`）→ 链接（把 `printf` 的实现从共享库 `libc.so` 中关联进来，生成 `hello`）。因为 `printf` 位于标准 C 共享库 `libc.so` 中，所以最终 `hello` 体积很小，运行时才去加载这个 `.so`。
