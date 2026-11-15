---
title: 传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）
requires: [数学建模/canshu_queding]
---

# 传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）

## 从 SIR 到 SEIR：为什么要多一个 E？

SIR 模型把人群分为易感者 $S$、感染者 $I$、康复者 $R$ 三类。但像埃博拉这样的传染病，从接触病毒到出现症状之间有一段**潜伏期**——此时人已经被感染（暴露），却还不能传染别人。

如果直接用 SIR 建模，就等于默认"感染立刻具有传染性"，会高估疫情早期增速。所以 SEIR 在 S 和 I 之间插入暴露者 $E$，让模型更贴近真实传播节奏。

## 模型方程

设总人口 $N$ 恒定，$t$ 时刻四类人数为 $S(t),E(t),I(t),R(t)$，则

$$
\left\{
\begin{aligned}
\dot S(t) &= -\frac{\beta S(t)I(t)}{N},\\
\dot E(t) &= \frac{\beta S(t)I(t)}{N}-\sigma E(t),\\
\dot I(t) &= \sigma E(t)-gamma I(t),\\
\dot R(t) &= gamma I(t).
\end{aligned}
\right.
$$

各参数含义：

| 参数 | 含义 | 与病程的对应 |
| :--- | :--- | :--- |
| $\beta$ | 每人每天有效传播率 | 接触传染的"力度" |
| $1/\sigma$ | 平均潜伏期 | 埃博拉约 $5.3$ 天 |
| $1/\gamma$ | 平均传染期 | Chowell 等取 $5.61$ 天 |

> [!IMPORTANT]
> ==只有 $I$ 类个体才能传染 $S$==；$E$ 只是"已感染未发病"，不产生新病人。$\sigma E$ 是"到期转阳"的流出项。

## 人群流转图

```mermaid
flowchart LR
    S["易感者 S"] -- "βSI/N" --> E["暴露者 E"]
    E -- "σE 发病" --> I["感染者 I"]
    I -- "γI 康复/死亡" --> R["移除者 R"]
```

## 基本再生数 $R_0$

对 SEIR 模型，$R_0$ 表示一个感染者在完全易感人群中平均造成的二代病例数：

$$
R_0=\frac{\beta}{\gamma}.
$$

> [!TIP]
> 记忆：$\beta$ 是"每天传染几个"，$1/\gamma$ 是"能传染几天"，两者相乘就是"总共传染几个"。

2015 年 MCM 特等奖论文用该式结合 Chowell 等的数据，给出三国参数估计：

| 参数 | 几内亚 | 塞拉利昂 | 利比里亚 |
| :--- | :--- | :--- | :--- |
| $R_0$ | 1.51 | 2.53 | 1.59 |
| $\beta_0$ | 0.27 | 0.45 | 0.28 |
| $N$（万） | 1200 | 610 | 409 |

例如利比里亚：$\beta_0=0.28$，$1/\gamma=5.61$ 天，则

$$
R_0=\frac{\beta_0}{\gamma}=0.28\times 5.61\approx 1.57\approx1.59
$$

与表中估计一致，说明模型能较好复现早期疫情。

## 加入干预：时变 $\beta$

无干预时 $\beta=\beta_0$ 为常数；$t\geq\tau$ 引入隔离、治疗等措施后，论文假设 $\beta$ 指数衰减：

$$
\beta(t)=
\begin{cases}
\beta_0, & t<\tau,\\
\beta_0 e^{-k(t-\tau)}, & t\geq\tau.
\end{cases}
$$

其中 $k$ 是控制强度（三国均取 $0.048$）。这样 SEIR 就能模拟"疫情先爆发、后被压平"的全过程。

## 常见误区

> [!WARNING]
> - ==别把 $E$ 当成无症状传染者==：SEIR 中 $E$ 不传染，只有 $I$ 才传染。
> - ==别把 $1/\sigma$ 与 $1/\gamma$ 搞混==：前者是"还要多久发病"，后者是"还能传染多久"。
> - $R_0=\beta/\gamma$ 只在**完全易感、无干预**的初始阶段成立；一旦 $\beta(t)$ 随时间衰减，瞬时再生数 $R_t$ 会小于 $R_0$。

> [!NOTE]
> 与 SIR 相比，SEIR 多了一条 $E$ 状态，早期增长更平缓（先"积压"在潜伏箱），更符合埃博拉"潜伏 $5$ 天左右才发病"的流行病学特征。
