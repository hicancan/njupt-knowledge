---
title: 《嵌入式系统与开发》实验5 嵌入式 Linux 下 LED 报警灯驱动设计及编程（答案）
kind: 实验
course: 嵌入式系统与开发
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0302161S%E3%80%91%E5%B5%8C%E5%85%A5%E5%BC%8F%E7%B3%BB%E7%BB%9F%E4%B8%8E%E5%BC%80%E5%8F%91/%E5%AE%9E%E9%AA%8C%E7%AD%94%E6%A1%88/%E5%AE%9E%E9%AA%8C5-%E9%A9%B1%E5%8A%A8%E5%BC%80%E5%8F%91-%E5%AE%9E%E9%AA%8C%E6%8A%A5%E5%91%8A%20-%20%E7%AD%94%E6%A1%88.doc
---

# 《嵌入式系统与开发》实验5 嵌入式 Linux 下 LED 报警灯驱动设计及编程（答案）

原件经识别和整理；“参考解答”是我们补的。

---
title: 《嵌入式系统与开发》实验5 嵌入式 Linux 下 LED 报警灯驱动设计及编程（答案）
kind: 实验
course: 嵌入式系统与开发
term: 
source: 
---

# 《嵌入式系统与开发》实验5 嵌入式 Linux 下 LED 报警灯驱动设计及编程（答案）

本资料为《嵌入式系统与开发》课程实验 5 的参考答案及指导，涵盖 LED 报警灯驱动设计、跑马灯应用编程及看门狗功能集成。

## 一、实验目的

理解驱动本质，掌握嵌入式 Linux 系统下驱动开发相关知识，包括端口寄存器访问、接口函数编写、和文件系统挂接、注册及相关应用编程等知识点。

## 二、实验内容

1. 实验 5.1 嵌入式 Linux 下 LED 报警灯驱动设计及跑马灯应用编程
2. 实验 5.2 添加看门狗功能的跑马灯应用编程

## 三、预备知识

Linux 使用、驱动相关知识等。

## 四、实验设备及工具（包括软件调试工具）

**硬件：**
- ARM 嵌入式开发平台
- PC 机 Pentium 100 以上
- 串口线

**软件：**
- WinXP 或 UBUNTU 开发环境

## 五、实验 5.1 步骤

### 5.1 前期准备

(1) 看懂相关硬件电路图【见 S3C6410 实验箱电路图-底板.pdf】，以 LED 报警灯为例进行设计。打开 PDF 硬件电路图，明确 LED 灯用到的多个 GPIO 及其控制器。

**得出结论：** 8 个 LED 灯使用到的硬件控制器分别为 GPM 和 GPQ 两个硬件控制器。

(2) 在芯片手册中找到相应的硬件控制器部分，重心是看懂端口寄存器。本实验要求完成 LED 流水灯设计，所以需要设置控制器中端口寄存器：`GPMCON` ---- 设置相应位为输出口控制相应位输出高电平点亮灯，输出低电平熄灭 LED 灯。

(3) Linux 内核中相关寄存器读写函数：

```c
writel(值(无符号整型), 寄存器虚地址);
```

具体端口寄存器地址宏定义在 `/opt/FriendlyARM/linux-2.6.38/arch/arm/mach-s3c64xx/include/mach` 文件夹下的文件中，如端口 M 寄存器在 `gpio-bank-m.h` 文件中有定义：

```c
#define S3C64XX_GPMCON (S3C64XX_GPM_BASE + 0x00)
#define S3C64XX_GPMDAT (S3C64XX_GPM_BASE + 0x04)
```

**注意：** 上面斜体部分原代码有错误，请找到该文件并修改。

### 5.2 LED 报警灯驱动设计 s3c6410_leddrv.c

**(1) 头文件包含和相关宏定义**

```c
#include <linux/miscdevice.h>
#include <linux/delay.h>
#include <asm/irq.h>
//#include <mach/regs-gpio.h>
#include <mach/hardware.h>
#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/mm.h>
#include <linux/fs.h>
#include <linux/types.h>
#include <linux/delay.h>
#include <linux/moduleparam.h>
#include <linux/slab.h>
#include <linux/errno.h>
#include <linux/ioctl.h>
#include <linux/cdev.h>
#include <linux/string.h>
#include <linux/list.h>
#include <linux/pci.h>
#include <asm/uaccess.h>
#include <asm/atomic.h>
#include <asm/unistd.h>

#include <mach/map.h>
#include <mach/regs-clock.h>
#include <mach/regs-gpio.h>

#include <plat/gpio-cfg.h>
#include <mach/gpio-bank-m.h>

#define ON 1
#define OFF 0

unsigned int old_gpmcon_val;
int leddevNo;
```

**(2) 编写驱动接口函数**

*(此处原文档缺失具体代码实现，仅保留标题)*

### 5.3 编写应用程序

**任务：** 要求每 5 秒点亮所有的 LED 灯，然后熄灭，过 5 秒再点亮 LED 灯。

```c
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/ioctl.h>
```

将应用程序加载到开发板上【具体方法参考文档 04-Tiny6410 Linux 开发指南.pdf 的 1.9.1 节】，并修改权限，命令为：

```bash
chmod +x ledapp
```

测试应用程序，命令为：

```bash
./ledapp
```

测试 LED 灯变化规律为：

*(此处原文档缺失具体现象描述)*

### 5.4 按照现在的驱动设计，假设要完成 LED 跑马灯实验，请问是否可行？

答案：B [A.可行 B.不可行]。

如果不可行的话，应该怎样改造驱动代码和应用程序。

**驱动代码修改部分：**

略

**应用程序修改部分：**



## 六、实验 5.2 步骤

### 6.1 实验预备知识

**(1) 相关硬件**

看门狗硬件主要用于监控系统软件或者应用软件是否发生故障，如发生故障则可以通过发出硬件复位信号，使得系统能够重启，如果再配合相关自动加载应用程序等措施，则可以保证应用程序在发生故障后能够自恢复和重启。

看门狗硬件由看门狗控制器组成，位于 S3C6410 处理器内部，无须处理器外其它硬件配合，因此仅需直接编程端口寄存器，并封装成文件系统接口即可。

**(2) 端口寄存器及相关操作**

在内核代码文件中已经定义好看门狗相关端口寄存器对应的虚地址，见 `/opt/FriendlyARM/linux-2.6.38/arch/arm/plat-samsung/include/plat/regs-watchdog.h`，如下：

```c
#define S3C2410_WTCON S3C_WDOGREG(0x00)
#define S3C2410_WTDAT S3C_WDOGREG(0x04)
#define S3C2410_WTCNT S3C_WDOGREG(0x08)
```

读寄存器函数：

```c
readl(寄存器虚地址);
```

写寄存器函数：

```c
writel(值(无符号整型), 寄存器虚地址);
```

### 6.2 看门狗驱动代码（s3c6410_wdtdrv.c）设计

**(1) 头文件包含和相关宏定义**

```c
#include <linux/module.h>
#include <linux/moduleparam.h>
#include <linux/types.h>
#include <linux/timer.h>
#include <linux/miscdevice.h>
#include <linux/watchdog.h>
#include <linux/fs.h>
#include <linux/init.h>
#include <linux/platform_device.h>
#include <linux/interrupt.h>
#include <linux/clk.h>
#include <linux/uaccess.h>
#include <linux/io.h>
#include <linux/cpufreq.h>
#include <linux/slab.h>
#include <mach/map.h>
#include <plat/regs-watchdog.h>

unsigned int old_wdtcon_val;
```

使用命令进行驱动加载：

```bash
insmod wdtdrv.ko
```

**(4) 创建设备文件，将驱动设备号和设备文件名关联**

相关命令为：

*(此处原文档缺失具体 mknod 命令)*

### 5.3 编写应用程序

**任务：** 要求每 5 秒点亮所有的 LED 灯，然后熄灭，过 5 秒再点亮 LED 灯，要求能够添加看门狗支持。
