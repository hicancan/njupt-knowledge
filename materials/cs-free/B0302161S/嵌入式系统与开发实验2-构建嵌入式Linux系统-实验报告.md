---
title: 《嵌入式系统与开发》实验2 构建嵌入式Linux系统 实验报告
kind: 实验
course: 嵌入式系统与开发
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0302161S%E3%80%91%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%B3%BB%E7%BB%9F%E4%B8%8E%E5%BC%80%E5%8F%91/%E5%AE%9E%E9%AA%8C%E7%AD%94%E6%A1%88/%E5%AE%9E%E9%AA%8C2-%E6%9E%84%E5%BB%BA%E5%B5%8C%E5%85%A5%E5%BC%8FLinux%E7%B3%BB%E7%BB%9F-%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%20.doc
---

# 《嵌入式系统与开发》实验2 构建嵌入式Linux系统 实验报告

原件经识别和整理；“参考解答”是我们补的。

# 实验 2 构建嵌入式 Linux系统

## 一、实验目的

理解嵌入式Linux 内核和文件系统构建过程，掌握 Linux内核裁剪、编译等过程，掌握基于busybox构建嵌入式文件系统命令工具等内容，并利用相关工具制作文件系统。

## 二、实验内容

- 实验 2.1 配置和编译 UBOOT
- 实验 2.2 裁剪和编译内核
- 实验 2.3 制作文件系统

## 三、预备知识

Linux 使用等

## 四、实验设备及工具（包括软件调试工具）

**硬件：** ARM 嵌入式开发平台、PC 机Pentium100 以上、串口线。

**软件：** WinXP 或 UBUNTU 开发环境。

## 五、实验步骤

### 5.1 UBOOT 配置及编译

步骤【参看 04- Tiny6410 Linux 开发指南.pdf 文档 1.5.1 节】：

第一步，解压缩 uboot 源码，命令 `tar xvzf /tmp/linux/u-boot-mini6410-20101106.tar.gz`。在解压后的文件夹下，可以看到 Makefile 文件，是整个 uboot 源码包编译的总 Makefile，负责整个uboot 的裁剪、编译等过程。

第二步，实验设备使用 128M 内存，处理器采用 S3C6410，生成配置文件命令为 `make mini6410_nand_config-ram128`。

第三步，编译 UBOOT 命令为 `make`，编译完成后生成 uboot.bin，该文件存储在 uboot 源码顶层目录 **`_`** 目录下。

### 5.2 内核裁剪及编译

步骤【参看 04- Tiny6410 Linux 开发指南.pdf 文档 1.6.1 节】：

第一步，解压缩 Linux 内核源码，命令 `tar xvzf /tmp/linux/linux-2.6.38-20110325.tar.gz`。在解压缩后的文件夹下，可以看到 Makefile 文件，是整个Linux内核源码包编译的总 Makefile，负责整个Linux内核的裁剪和编译工作。

第二步，内核源码裁剪

**方式1：** 通常情况下 linux根目录下有个 `.config` 文件，该文件是宏文件，每个宏和一定的源码文件关联，如果注释掉相应宏，则对应源码将不会被编译进 linux内核映像文件中。

实验1----打开该文件可以选择注释掉部分宏，如 `CONFIG_NET=y`，重新编译会发现内核文件 zImage 大小约为 **3MB** 字节，或者到 net 目录下发现所有的 c 文件 **A** (A.被编译 B.未被编译) ，且net目录下的所有被编译后的目标文件被连接成一个目标文件 `_built_in.o`。

实验2----重新打开 `.config` 文件，取消注释宏 `CONFIG_NET=y`，重新编译会发现内核文件 zImage 大小为 **2.985MB** 字节，或者到 net 目录下发现所有的 c 文件 **B** (A.被编译 B.未被编译)。

**方式 2：** 在 shell 环境下，进入内核源码顶层目录，执行命令 `make menuconfig` 命令，进入图形环境下裁剪Linux内核。找到“网络支持选项”，按空格键取消选择，并保存退出，重新打开 `.config` 文件，发现宏 `CONFIG_NET` 是否被定义 **B** (A. 被定义 B.被注释 )，重新编译会发现内核文件 zImage 大小为 **2.985MB** 字节，或者到 net 目录下发现所有的 c 文件 **B** (A.被编译 B.未被编译)。

第三步，编译内核，命令为 `make zImage`，编译完成后生成 zImage,该文件存储在 **arch/arm/boot** 目录下。

### 5.3 内核添加自己代码的方式

本例以添加一个RC4 加密算法为例来进行

第四步，执行 `make menuconfig`，在其中找到"RC4 ENCRYPT SUPORT"选项，并选中，退出配置，在 `.config` 文件中， **A** （A.有 B.没有）宏 `CONFIG_RC4ENCRYPT`。

### 5.4 文件系统构建

步骤【参看 04- Tiny6410 Linux 开发指南.pdf 文档 1.7~1.8 节】

第一步，解压缩 busybox，命令为 `tar xvzf /tmp/linux/busybox-1.17.2-20101120.tgz`。解压缩完成后，可以看到在目录下有 Makefile 文件和 `.config` 文件，Makefile 文件负责编译，具体编译哪些文件依据 `.config` 文件。打开 fa.config文件，查看其中宏。

第二步，裁剪命令，执行命令 `make menuconfig`，去除其中部分选项，保存退出，查看 `.config` 文件，可以看到相应宏定义也发生变化了。

第三步，编译文件，命令为 `make`，安装到相应的文件夹，命令为 `make install`，到对应的文件夹下查看生成的命令文件。

第四步，创建配置文件，将 busybox源码目录下的 etc 文件夹拷贝到刚才的文件夹下。

第五步，拷贝已经移植好的 lib 到刚才的文件夹下。

第六步，创建文件夹 dev proc tmp 等。

第七步，利用工具将文件夹制作成根文件系统，命令为 `mkyaffs2image fs fs.img`。

按照文档【03- Tiny6410 刷机指南.pdf 中 2.2.1】进行烧写
