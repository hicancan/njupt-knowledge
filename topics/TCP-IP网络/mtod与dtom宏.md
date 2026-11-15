---
title: 宏 mtod 和 dtom 的作用
requires: [TCP-IP网络/mbuf用途与结构]
---

# 宏 mtod 和 dtom 的作用

## 它是什么

在 mbuf（memory buffer，内存缓冲区）机制里，我们常常需要在这两种东西之间来回跳：一个是 **mbuf 结构本身**（里面有 `m_next`、`m_len`、`m_data`、`m_type` 等管理信息），另一个是这个 mbuf 实际装着的 **数据区**（可能是 mbuf 自带的小缓冲区，也可能是外部的 cluster 簇）。

先想一个问题：如果你手里有一个 `struct mbuf *m`，怎么拿到它里面数据的起始地址，并且直接当成某种协议头（比如 `struct ip *`）来用？

这就是 `mtod` 的作用。

> [!IMPORTANT]
> 宏 `mtod` 返回指向该 mbuf 所关联数据的指针，并把该指针转换成你指定的类型。
> 常见写法类似：`mtod(m, struct ip *)`，意思是“取 `m` 的数据指针，并当成 IP 头来解释”。

反过来，再想一个问题：如果你在处理数据时，手里只有一个指向数据区内部某个位置的指针（例如已经偏移到了 TCP 头中间），你怎么找回“这个数据属于哪个 mbuf”？

这就是 `dtom` 的作用。

> [!IMPORTANT]
> 宏 `dtom` 接受指向 mbuf 数据部分中任意位置的指针，返回指向该 **mbuf 结构本身** 的指针。
> 也就是从 `data pointer` 反推回 `mbuf header`。

## 为什么需要它们

因为协议栈代码不想一直做繁琐的指针算术。`mtod` 让我们从 `m` 快速得到“可当作协议头使用的数据地址”；`dtom` 让我们在只有数据地址时，还能找回管理结构，从而访问 `m_len`、`m_next`、`m_nextpkt` 等字段。

但这里有个前提：`dtom` 能工作的关键是——**数据指针必须真正落在该 mbuf 自己的数据缓冲区范围内**。如果数据放在外部 cluster 里，多个 mbuf 可能引用同一个 cluster，这时从 cluster 内的数据指针反推 mbuf 就会出问题。

## 和相近概念的区别

| 项目 | `mtod` | `dtom` |
|---|---|---|
| 输入 | `struct mbuf *m` + 目标类型 | 数据区内任意位置指针 |
| 输出 | `m` 的数据起始地址（已转类型） | 所属的 `struct mbuf *` |
| 方向 | mbuf → data | data → mbuf |
| 典型用途 | 把数据当 IP/TCP/UDP 头解析 | 从数据指针找回 mbuf 头部 |

## 常见坑与边界条件

> [!WARNING]
> `dtom` 之所以在 cluster 场景有麻烦，不是因为忘了加“反向指针”就行。
> 不能简单地给每个 cluster 加一个指回 mbuf 的 back pointer，因为：
> 1. **一个 cluster 可能被多个 mbuf 同时指向**（见教材 Figure 2.26），此时 back pointer 该指哪一个？
> 2. cluster 本身没有多余空间存放这个 back pointer。

那怎么保证这两个宏能安全用？答案就是 `m_pullup`。

当协议（IP、ICMP、IGMP、UDP、TCP）发现第一个 mbuf 里的 `m_len` 小于最小协议头长度（如 IP 是 20、UDP 是 8、TCP 是 20）时，会调用 `m_pullup`。它假定剩余头部在链上下一个 mbuf 中，并重新安排 mbuf 链，使前 `N` 字节数据在第一个 mbuf 里连续存放。这里 `N` 是函数参数，且必须 `N <= 100`（即 `MHLEN`）。

> [!TIP]
> 记忆点：`m_pullup` 把前 $N$ 字节“拉平”到第一个 mbuf；一旦前 $N$ 字节连续，`mtod` 和 `dtom` 就都能正常工作。

```mermaid
flowchart LR
  A["原链: m1 不足+ m2"] --> B["m_pullup(N)"]
  B --> C["前N字节连续在 m1"]
  C --> D["mtod / dtom 可用"]
```

## 一个算对了的例子

题目：为什么不在每个 cluster 里加 back pointer 来避免 `dtom` 的问题？

正确回答应是：

> This is infeasible since clusters can be pointed to by multiple mbufs. Also, there is no room in a cluster for a back pointer.

也就是：**不可行，因为多个 mbuf 可指向同一 cluster，且 cluster 中没有空间放反向指针**。答到这两点，就抓住了本题核心。
