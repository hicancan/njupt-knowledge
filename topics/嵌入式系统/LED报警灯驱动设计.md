---
title: S3C6410 LED报警灯字符设备驱动代码（s3c6410_leddrv.c）设计实例
requires: [嵌入式系统/驱动与应用交互接口]
---

# S3C6410 LED报警灯字符设备驱动代码（s3c6410_leddrv.c）设计实例

## 驱动要解决的问题

LED 报警灯接在 S3C6410 的 GPIO 引脚上。应用程序不能直接操作硬件寄存器，而应通过设备文件 `/dev/led` 请求内核完成控制。`s3c6410_leddrv.c` 的任务就是：**注册字符设备，提供文件操作接口，并把 `ioctl` 命令转换为 GPIO 电平变化**。

调用链如下：

```mermaid
flowchart LR
    A["Qt 按钮槽函数"] --> B["ioctl 系统调用"]
    B --> C["字符设备驱动"]
    C --> D["GPIO 寄存器"]
    D --> E["LED 亮或灭"]
```

## GPIO 控制原理

以 LED 接在 `GPK4`、低电平点亮为例，驱动主要操作三类寄存器：

| 寄存器 | 作用 | 本例设置 |
|---|---|---|
| `GPKCON0` | 配置引脚功能 | 将 GPK4 配置为输出 |
| `GPKDAT` | 读写引脚数据 | 写 0 点亮，写 1 熄灭 |
| `GPKPUD` | 配置上拉、下拉 | 按硬件电路设置 |

配置输出时，==不能直接把整个控制寄存器赋成固定值==，否则可能破坏同组其他引脚。通常先清除对应位段，再写入输出模式：

```c
reg = readl(GPKCON0);
reg &= ~(0xf << 16);       /* 清除 GPK4 的 4 位配置 */
reg |=  (0x1 << 16);       /* 0001：输出 */
writel(reg, GPKCON0);
```

数据寄存器也应采用“读—修改—写”，只改变 LED 对应位。若实验板是高电平点亮，则亮、灭命令必须反过来，最终以原理图为准。

## 字符设备驱动的骨架

驱动通常包含以下部分：

```c
static int led_open(struct inode *inode, struct file *file)
{
    return 0;
}

static long led_ioctl(struct file *file,
                      unsigned int cmd, unsigned long arg)
{
    switch (cmd) {
    case LEDON:
        led_set(1);
        break;
    case LEDOFF:
        led_set(0);
        break;
    default:
        return -EINVAL;
    }
    return 0;
}

static struct file_operations led_fops = {
    .owner          = THIS_MODULE,
    .open           = led_open,
    .unlocked_ioctl = led_ioctl,
};
```

模块加载时申请设备号、注册字符设备并初始化 GPIO；卸载时注销设备、释放设备号。若实验环境使用旧内核，接口可能写作 `.ioctl`，而不是 `.unlocked_ioctl`，应按实验代码和内核版本填写。

> [!IMPORTANT]
> 驱动设计的核心是：**`LEDON`、`LEDOFF` 是命令编号，`file_operations` 建立接口联系，GPIO 写操作才真正改变灯的状态。**

> [!WARNING]
> 常见失分点：只写 `ioctl` 而不写 GPIO 配置；忘记 `default` 返回错误；亮灭电平写反；把字符设备驱动误写成 Qt 界面程序；卸载模块时未释放资源。

## Qt 综合题示例

题目要求点击 ON 按钮点灯、点击 OFF 按钮灭灯。先建立信号与槽的连接：

```cpp
connect(m_on,  SIGNAL(clicked()), this, SLOT(ledOn()));
connect(m_off, SIGNAL(clicked()), this, SLOT(ledOff()));
```

两个槽函数可写为：

```cpp
void MainWindow::ledOn()
{
    int fd = open("/dev/led", O_RDWR);
    if (fd < 0)
        return;
    ioctl(fd, LEDON);
    close(fd);
}

void MainWindow::ledOff()
{
    int fd = open("/dev/led", O_RDWR);
    if (fd < 0)
        return;
    ioctl(fd, LEDOFF);
    close(fd);
}
```

这里 `m_on`、`m_off` 是按钮对象，`clicked()` 是信号，`ledOn()`、`ledOff()` 是槽函数。若程序已在初始化阶段打开设备并保存 `fd`，槽函数中可直接调用 `ioctl`，不必重复打开。

> [!TIP]
> 设计题按“**打开设备—发送命令—关闭设备**”组织答案，再补上信号与槽，逻辑最完整。看门狗用于系统异常后的复位恢复，LED 驱动用于 GPIO 输出控制，二者不要混写。
