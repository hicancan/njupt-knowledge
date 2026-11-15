---
title: 文件的读写read()与write()系统调用
requires: [Linux系统编程/open和close]
---

# 文件的读写read()与write()系统调用

## 它是什么

想想看：C 语言里已经学过 `fopen / fread / fwrite` 了，为什么 Linux 系统还要单独提供 `open / read / write` 这一套？

因为 `read()` 与 `write()` 是==不带缓冲的 I/O 系统调用==，直接陷入内核操作文件描述符 `fd`。它们的原型是：

$$
\texttt{ssize\_t read(int fd, void *buf, size\_t count);}
$$
$$
\texttt{ssize\_t write(int fd, const void *buf, size\_t count);}
$$

- `fd`：由 `open()` 返回；
- `buf`：用户空间缓冲区首地址；
- `count`：请求读/写的字节数；
- 返回实际传送的字节数，`0` 表示读到文件尾，`-1` 表示出错。

## 为什么需要

库函数 `fwrite` 先写进用户态流缓冲，再由系统择机真正落盘；而 `write()` 每调用一次就发一次系统调用。做底层文件 I/O 编程时，我们关心 “此刻是否真的写了多少字节”，所以要用 `write()` 精确控制。

```mermaid
flowchart LR
  A["用户进程 buf"] --> B["write() 系统调用"]
  B --> C["内核 文件表项"]
  C --> D["磁盘/文件"]
```

## 怎么做

写文件时通常三步：`open()` → `write()` → `close()`。若要把斐波那契前 20 个数写进 `fib.txt`，核心片段如下：

```c
int fd = open("fib.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
long a = 1, b = 1;
for (int i = 0; i < 20; i++) {
    char tmp[32];
    int len = snprintf(tmp, sizeof(tmp), "%ld ", a);
    write(fd, tmp, len);        // 逐个数字写入
    long next = a + b; a = b; b = next;
}
close(fd);
```

> [!IMPORTANT]
> `write()` 返回的是“实际写入字节数”，可能小于 `count`；==不等于请求数不代表出错，要循环补齐==。

## 和相近概念的区别

| 对比项 | `read/write` | `fread/fwrite` |
|---|---|---|
| 层次 | 系统调用 | C 库函数 |
| 缓冲 | 无缓冲 | 带流缓冲 |
| 操作对象 | `fd` | `FILE *` |
| 头文件 | `unistd.h` | `stdio.h` |

## 常见的坑

> [!WARNING]
> 一打开文件忘了 `open()` 的权限参数 `mode`（如 `0644`），`O_CREAT` 时文件权限会随机；二把 `snprintf` 的返回值误当作 `write` 长度（它不含结尾 `\0`，正好合适）；三只用一次 `write` 期望写全，遇到短写就丢数据。

> [!TIP]
> 记住口诀：==“开、写、关；查返回；短写要补完”==。

## 算对了的例子

上面那段 C 程序编译运行：

```bash
gcc fib.c -o fib
./fib
cat fib.txt
# 输出：1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```

这正是复习提纲里“用 C 语言将斐波那契数列前 20 个数写入 `fib.txt`”的标准答案雏形：前两项恒为 $1,1$，之后 $F_n = F_{n-1} + F_{n-2}$，第 20 项为 $6765$。
