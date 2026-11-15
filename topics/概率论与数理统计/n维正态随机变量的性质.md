---
title: n维正态随机变量的概率密度与重要性质
requires: [概率论与数理统计/矩与协方差矩阵]
---

# n维正态随机变量的概率密度与重要性质

# n 维正态随机变量的概率密度

## 从一维到多维：为什么要推广

一维正态分布能描述单个随机变量的集中趋势和波动。但在工程与通信问题中，==多个随机变量往往相互关联==。信号检测中的噪声可能同时影响多个接收端，且彼此相关——仅用多个独立的一维正态无法刻画这种相关性。

这就引出一个问题：能不能用一个联合分布，把多个正态变量的依赖关系统一表达？

## 概率密度的形式

设 $\mathbf{X} = (X_1, X_2, \dots, X_n)^T$ 服从 $n$ 维正态分布，记均值向量为 $\boldsymbol{\mu} = E(\mathbf{X}) = (\mu_1, \dots, \mu_n)^T$，==协方差矩阵==为

$$
\mathbf{C} = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T]
= 
\begin{bmatrix}
\sigma_1^2 & \text{Cov}(X_1,X_2) & \dots & \text{Cov}(X_1,X_n) \\
\text{Cov}(X_2,X_1) & \sigma_2^2 & \dots & \text{Cov}(X_2,X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(X_n,X_1) & \text{Cov}(X_n,X_2) & \dots & \sigma_n^2
\end{bmatrix}
$$

若 $\mathbf{C}$ **正定**（可逆），则 $n$ 维正态随机变量的概率密度为：

> [!IMPORTANT]
> $$
> f(\mathbf{x}) = \frac{1}{(2\pi)^{n/2} |\mathbf{C}|^{1/2}}
> \exp\left\{ -\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})^T \mathbf{C}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right\}
> $$

其中 $|\mathbf{C}|$ 是协方差矩阵的行列式。$\mathbf{C}$ 必须正定以保证密度函数可积归一。

## 重要性质的层次分解

以下四条性质构成了考试的核心：

> [!IMPORTANT]
> **性质 1（线性变换保持正态性）**
> 若 $\mathbf{X} \sim N_n(\boldsymbol{\mu}, \mathbf{C})$，对任意 $m \times n$ 矩阵 $\mathbf{A}$，有
> $\mathbf{Y} = \mathbf{A}\mathbf{X} \sim N_m(\mathbf{A}\boldsymbol{\mu}, \mathbf{A}\mathbf{C}\mathbf{A}^T)$。

==正态分布在线性变换下仍然保持正态，这在工程中极其实用==——这意味着只要输入是联合正态的，任何线性系统的输出也是联合正态。

> [!IMPORTANT]
> **性质 2（不相关与独立等价）**
> 在 $n$ 维正态分布中，==$X_1, \dots, X_n$ 相互独立 $\iff$ 它们两两不相关==（即 $\mathbf{C}$ 为对角阵）。

> [!WARNING]
> 这一等价性**仅对联合正态成立**。一般情形下，"不相关" 远弱于 "独立"。这是常见陷阱。

> [!NOTE]
> **性质 3（子向量仍正态）**
> 从 $\mathbf{X}$ 中任取一些分量构成子向量，该子向量的边际分布仍是多维正态。且条件分布也保持正态。

> [!TIP]
> **性质 4（条件均值是线性函数）**
> 在给定 $\mathbf{X}$ 的一部分分量后，另一部分分量的条件期望是已给分量的**线性函数**。这是进行最优线性预测的理论基础。

## 典型例题：性质 1 的直接应用

（取自南邮考题）已知 $\mathbf{X} \sim N_3(\boldsymbol{\mu}, \mathbf{C})$，其中

$$
\boldsymbol{\mu} = 
\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}, \quad
\mathbf{C} = 
\begin{pmatrix} 1 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 2 \end{pmatrix}
$$

求 $Y = X_1 - 2X_2 + X_3$ 的分布。

**解**：令 $\mathbf{A} = (1, -2, 1)$。则 $Y = \mathbf{A}\mathbf{X}$，由**性质 1**：

- 均值：$E(Y) = \mathbf{A}\boldsymbol{\mu} = 1 \times 1 + (-2) \times 2 + 1 \times (-1) = 1 - 4 - 1 = -4$
- 方差：$D(Y) = \mathbf{A}\mathbf{C}\mathbf{A}^T$

计算：
$$
\mathbf{A}\mathbf{C} = (1,-2,1) 
\begin{pmatrix} 1 & 1 & 1 \\ 1 & 3 & 1 \\ 1 & 1 & 2 \end{pmatrix}
= (1-2+1,\; 1-6+1,\; 1-2+2) = (0, -4, 1)
$$

$$
D(Y) = (0, -4, 1) \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix}
= 0 + 8 + 1 = 9
$$

于是 $Y \sim N(-4, 9)$。

> [!TIP]
> 这一方法的核心在于 ==**无须求出联合密度的显式表达**==，直接用均值向量与协方差矩阵做线性变换即可得到任意线性组合的分布。
