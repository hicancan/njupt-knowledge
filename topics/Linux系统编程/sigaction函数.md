---
title: sigaction()函数进行可靠的信号处理
requires: [Linux系统编程/信号机制]
---

# sigaction()函数进行可靠的信号处理

## 为什么需要 sigaction

早期的 `signal()` 函数存在严重的可靠性问题：信号处理函数执行期间，若同一信号再次到达，可能导致处理函数被重入或信号丢失；且每次触发后信号处置常被重置为默认值。这引出一个关键问题：==如何在处理信号时既阻塞同类信号防止重入，又保持自定义处理器持久生效？== `sigaction()` 正是为解决此问题而设计的可靠信号处理接口。

> [!IMPORTANT]
> `sigaction()` 是 POSIX 标准推荐的==可靠信号处理==唯一方式，`signal()` 仅用于简单兼容场景。

## 核心机制与参数

`sigaction()` 通过三个参数实现精确控制：

```c
int sigaction(int signum, const struct sigaction *act,
              struct sigaction *oldact);
```

-   `signum`：指定要捕获或忽略的信号编号（不能为 `SIGKILL` / `SIGSTOP`）。
-   `act`：指向新动作的结构体指针，定义处理函数、掩码及标志位。
-   `oldact`：非空时保存该信号之前的动作，便于后续恢复。

`struct sigaction` 中关键字段如下：

| 字段 | 作用 | 注意事项 |
| :--- | :--- | :--- |
| `sa_handler` | 简单处理函数指针 | 与 `sa_sigaction` 互斥 |
| `sa_sigaction` | 带上下文处理函数 | 需设置 `SA_SIGINFO` 标志 |
| `sa_mask` | 处理期间额外阻塞的信号集 | ==自动包含当前信号== |
| `sa_flags` | 行为控制标志 | 常用 `SA_RESTART`、`SA_SIGINFO` |

> [!NOTE]
> `sa_mask` 中的信号仅在==处理函数执行期间==被阻塞，返回后自动解除，不影响进程其他时段。

## 与 signal() 的关键区别

| 特性 | `signal()` | `sigaction()` |
| :--- | :--- | :--- |
| 信号阻塞 | 不自动阻塞同类信号 | ==自动阻塞当前信号== |
| 处理器持久性 | 可能重置为 `SIG_DFL` | 始终保持设定动作 |
| 附加信息 | 无 | 可通过 `SA_SIGINFO` 获取 |
| 系统调用重启 | 不可控 | 由 `SA_RESTART` 显式控制 |
| 可移植性 | 各 UNIX 实现差异大 | ==POSIX 标准统一== |

## 正确示例：可靠捕获 SIGINT

以下代码安全地处理 Ctrl+C，避免重入并保留处理器：

```c
#include <signal.h>
#include <stdio.h>

void handler(int sig) {
    printf("Caught SIGINT safely\n");
}

int main() {
    struct sigaction sa;
    sa.sa_handler = handler;
    sigemptyset(&sa.sa_mask);      // 清空掩码，当前信号已自动加入
    sa.sa_flags = SA_RESTART;      // 中断的系统调用自动重启

    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    while (1) pause(); // 等待信号
}
```

> [!WARNING]
> 切勿在信号处理函数中调用==非异步信号安全==函数（如 `printf`、`malloc`），上述示例仅为演示，生产环境应改用 `write()`。

> [!TIP]
> 初始化 `sa_mask` 必须用 `sigemptyset()`，==禁止直接赋值 0==，因信号集内部结构未标准化。

## 常见陷阱

-   忘记初始化 `sa_mask`：导致未定义行为，可能意外阻塞无关信号。
-   混淆 `sa_handler` 与 `sa_sigaction`：同时设置二者将产生不确定结果。
-   误以为 `sa_mask` 永久生效：它==仅作用于处理函数执行期==，长期阻塞需用 `sigprocmask()`。
-   忽略返回值检查：`sigaction()` 失败时不会修改旧动作，静默错误易引发逻辑漏洞。
