---
title: LL(1)分析法（FIRST/FOLLOW集、分析表构造）
requires: [编译原理/自顶向下问题与解决]
---

# LL(1)分析法（FIRST/FOLLOW集、分析表构造）

## LL(1) 分析法核心概念

LL(1) 是一种**自顶向下**、**不带回溯**的语法分析方法。
- **第一个 L**：从左到右扫描输入串 (Left-to-right)。
- **第二个 L**：产生最左推导 (Leftmost derivation)。
- **1**：只需向前看 **1** 个符号即可确定使用哪条产生式。

> [!IMPORTANT]
> ==核心要求==：文法必须消除**左递归**并提取**左公因子**，否则无法构造确定的 LL(1) 分析表。

## 为什么需要 FIRST 和 FOLLOW 集？

在分析非终结符 $A$ 时，若有多个候选式 $A \to \alpha_1 \mid \alpha_2$，如何决定选哪个？
1. 若 $\alpha_i$ 能推导出以终结符 $a$ 开头的串，且当前输入是 $a$，则选 $\alpha_i$。这需要 **FIRST** 集。
2. 若 $\alpha_i \Rightarrow^* \varepsilon$（可空），则需看 $A$ 后面能跟什么符号。若当前输入在 $A$ 的 **FOLLOW** 集中，则选 $\alpha_i$（即执行 $\varepsilon$ 产生式）。

## 集合构造规则

### FIRST 集构造
对于文法符号串 $\alpha = X_1 X_2 \dots X_n$：
1. 若 $X_1$ 是终结符，$\text{FIRST}(\alpha) = \{X_1\}$。
2. 若 $X_1 \Rightarrow^* \varepsilon$，则把 $\text{FIRST}(X_2)$ 加入；若 $X_2$ 也可空，继续看 $X_3$，以此类推。
3. 若所有 $X_i$ 都可空，则 $\varepsilon \in \text{FIRST}(\alpha)$。

### FOLLOW 集构造
对于非终结符 $A$：
1. 开始符号 $S$ 的 FOLLOW 集包含结束符 $\#$。
2. 若有产生式 $B \to \alpha A \beta$，则将 $\text{FIRST}(\beta) - \{\varepsilon\}$ 加入 $\text{FOLLOW}(A)$。
3. 若 $\beta \Rightarrow^* \varepsilon$ 或产生式为 $B \to \alpha A$，则将 $\text{FOLLOW}(B)$ 加入 $\text{FOLLOW}(A)$。

> [!TIP]
> 记忆口诀：FIRST 看“打头”，FOLLOW 看“后随”。$\varepsilon$ 是桥梁，连接前后集合。

## LL(1) 分析表构造

对每个产生式 $A \to \alpha$：
1. 对 $\forall a \in \text{FIRST}(\alpha)$，置 $M[A, a] = A \to \alpha$。
2. 若 $\varepsilon \in \text{FIRST}(\alpha)$，则对 $\forall b \in \text{FOLLOW}(A)$，置 $M[A, b] = A \to \alpha$。

> [!WARNING]
> 若表中某单元格被填入多次（多重定义），说明该文法**不是** LL(1) 文法。常见原因：左递归未消除或左公因子未提取。

## 实例演示

考虑文法 $G[E]$：
$$
\begin{aligned}
E &\to TE' \\
E' &\to +TE' \mid \varepsilon \\
T &\to FT' \\
T' &\to *FT' \mid \varepsilon \\
F &\to (E) \mid i
\end{aligned}
$$

**关键集合计算：**
- $\text{FIRST}(E) = \{(, i\}$
- $\text{FOLLOW}(E) = \{), \#\}$
- $\text{FIRST}(E') = \{+, \varepsilon\}$
- $\text{FOLLOW}(E') = \{), \#\}$ （因为 $E \to TE'$，$E'$ 后随符号同 $E$）

**分析表片段：**

| | i | + | * | ( | ) | # |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **E** | $E \to TE'$ | | | $E \to TE'$ | | |
| **E'** | | $E' \to +TE'$ | | | $E' \to \varepsilon$ | $E' \to \varepsilon$ |

**分析过程示例：输入 `(i)#`**

```mermaid
flowchart TD
    Start[开始: 栈#E, 输入(i)#] --> Step1[查表 M[E,(]: E->TE']
    Step1 --> Step2[栈: #E'T, 输入不变]
    Step2 --> Step3[查表 M[T,(]: T->FT']
    Step3 --> Step4[栈: #E'T'F, 输入不变]
    Step4 --> Step5[查表 M[F,(]: F->(E)]
    Step5 --> Match1[匹配 '(': 弹出栈顶(, 消费输入(]
    Match1 --> Step6[栈: #E'T')E, 输入: i)#]
    Step6 --> Step7[查表 M[E,i]: E->TE']
    Step7 --> Step8[...后续推导...]
    Step8 --> End[成功接受]
```

> [!NOTE]
> LL(1) 与 LR(1) 区别：LL(1) 是自顶向下（预测分析），适合手工构造；LR(1) 是自底向上（移进-归约），能力更强但状态多。南邮考试中，LL(1) 重点在于**集合计算**与**表构造**的正确性。
