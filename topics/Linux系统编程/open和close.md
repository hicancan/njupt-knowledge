---
title: 文件的打开open()与关闭close()系统调用
requires: [Linux系统编程/文件描述符]
---

# 文件的打开open()与关闭close()系统调用

## 文件描述符与系统调用基础

在 Linux 中，一切皆文件。要对文件进行读写，首先必须建立进程与文件之间的连接。`open()` 和 `close()` 是这一过程的入口与出口。

> [!IMPORTANT]
> `open()` 返回的是**文件描述符（fd）**，它是一个非负整数，指向内核中维护的文件表项。==fd 是后续所有 I/O 操作（read/write）的唯一句柄==。

为什么需要显式打开？因为内核需要通过 `open` 检查权限、分配资源并返回一个轻量级的索引（fd），避免每次 I/O 都传递冗长的路径名。

```mermaid
flowchart LR
    A["用户进程"] -->|open(path)| B("内核 VFS")
    B -->|检查权限| C{是否成功?}
    C -->|Yes| D["分配 fd"]
    C -->|No| E["返回 -1"]
    D --> F["返回 fd >= 0"]
    F --> G["后续 read/write"]
    G --> H["close(fd)"]
    H --> I["释放资源"]
```

## open() 系统调用详解

函数原型：
```c
#include <fcntl.h>
int open(const char *pathname, int flags, ... /* mode_t mode */);
```

- **pathname**：文件路径。
- **flags**：访问模式与控制标志的组合。
    - 访问模式（必选其一）：`O_RDONLY`, `O_WRONLY`, `O_RDWR`。
    - 控制标志（可选组合）：`O_CREAT`（不存在则创建）, `O_TRUNC`（截断为零）, `O_APPEND`（追加）。
- **mode**：仅当使用 `O_CREAT` 时有效，指定新文件的权限（如 `0644`）。

> [!TIP]
> 若使用 `O_CREAT`，必须提供第三个参数 `mode`。最终权限受 `umask` 影响：$最终权限 = mode \& \sim umask$。

## close() 系统调用详解

函数原型：
```c
#include <unistd.h>
int close(int fd);
```

关闭文件会释放进程文件表中的记录，并减少内核 inode 引用计数。当引用计数归零且无硬链接时，磁盘空间才被真正释放。

> [!WARNING]
> ==忘记 close() 会导致文件描述符泄漏==。Linux 对每个进程打开的 fd 数量有限制（通常 1024），耗尽后将无法打开新文件。

## 常见误区与辨析

| 特性 | open()/close() | fopen()/fclose() |
| :--- | :--- | :--- |
| **层级** | 系统调用（内核态） | 标准库函数（用户态） |
| **返回值** | int (fd) | FILE* (流指针) |
| **缓冲** | 无缓冲（Unbuffered） | 全缓冲/行缓冲（Buffered） |
| **适用场景** | 底层驱动、高性能 I/O | 常规文本处理、跨平台移植 |

> [!CAUTION]
> 不要混用！对同一个文件，若既用 `open` 又用 `fdopen` 转成流，需注意缓冲区同步问题，否则可能导致数据丢失或顺序混乱。

## 实战示例：斐波那契数列写入

结合复习提纲中的设计题，以下是使用 `open/close` 的核心逻辑片段：

```c
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    // 1. 打开文件：若不存在则创建，存在则截断，权限 0644
    int fd = open("fib.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open failed");
        return 1;
    }

    // 2. 计算并写入
    long f1 = 1, f2 = 1, temp;
    char buf[20];
    int len;
    
    // 写入前两个数
    len = sprintf(buf, "%ld\n%ld\n", f1, f2);
    write(fd, buf, len);

    for (int i = 3; i <= 20; i++) {
        temp = f1 + f2;
        len = sprintf(buf, "%ld\n", temp);
        write(fd, buf, len); // 系统调用写入
        f1 = f2;
        f2 = temp;
    }

    // 3. 关闭文件
    close(fd); 
    return 0;
}
```

此例展示了从 `open` 获取 fd，到 `write` 传输数据，最后 `close` 释放资源的完整闭环。
