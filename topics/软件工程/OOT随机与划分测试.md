---
title: 面向对象测试方法（OOT Methods）：随机测试（Random Testing）与划分测试（Partition Testing）
requires: [软件工程/面向对象测试]
---

# 面向对象测试方法（OOT Methods）：随机测试（Random Testing）与划分测试（Partition Testing）

面向对象测试（OOT）把测试重心从“单个函数”移到“类及其协作”。在类级测试中，方法应视为不可再分的基本操作，因此重点不是重新做路径覆盖，而是考察：**一个类在各种操作序列与输入下，是否始终满足其规格说明**。Random Testing 与 Partition Testing 正是两种常用的类级测试方法。

## Random Testing：随机排列操作

先找出类提供的操作及约束，再随机生成操作序列，观察对象状态与输出是否正确。例如，一个账户类提供 `open`、`deposit`、`withdraw`、`close`，可生成：

```text
open → deposit(100) → withdraw(40) → deposit(20) → close
```

若余额依次为 $0\rightarrow100\rightarrow60\rightarrow80$，且关闭前无违规操作，则该序列通过。

随机测试的价值在于发现设计者未预料的**操作交互缺陷**，而不只是某个方法的孤立错误。但“随机”不等于任意：若 `withdraw` 要求余额充足，就应生成合法序列，或明确把非法序列作为异常行为测试。

```mermaid
flowchart LR
    A["识别类操作"] --> B["确定前置约束"]
    B --> C["随机生成序列"]
    C --> D["检查状态输出"]
    D --> E["记录失败序列"]
```

## Partition Testing：减少用例数量

若所有输入与状态组合都测试，代价会迅速膨胀。Partition Testing 将输入或状态划分为若干等价集合，从每类选取代表用例，依据是：**同一划分中的用例应以相似方式被处理**。

课件要求掌握的三种划分策略如下：

| 策略 | 划分依据 | 类级测试关注点 |
|---|---|---|
| State-based partitioning | 对象状态 | 操作是否改变状态，状态改变是否符合规格 |
| Attribute-based partitioning | 属性取值类别 | 不同属性组合下操作是否正确 |
| Category-based partitioning | 操作功能类别 | 初始化、查询、修改等操作是否完整正确 |

以账户类为例，按状态可分为“未开户、正常、余额不足、已关闭”；按属性可将余额分为 $balance=0$、$0<balance<amount$、$balance\ge amount$；按功能可分为 `open/close`、`deposit/withdraw`、查询余额三组。

> [!IMPORTANT]
> 三种策略的标准表述是：==State-based、Attribute-based、Category-based partitioning==。答题时先写名称，再说明“依据什么划分、如何选代表用例”。

## 一个划分正确的例子

设 `withdraw(amount)` 要求 $amount>0$，且仅当 $balance\ge amount$ 时成功。对正常状态账户，可划分为：

1. $amount\le0$：拒绝取款；
2. $0<amount\le balance$：成功，$balance'=balance-amount$；
3. $amount>balance$：拒绝取款，余额不变。

若初始余额为 $100$，选代表用例 $amount=0,40,150$，预期结果分别为“拒绝”“成功且余额 $60$”“拒绝且余额 $100$”。这里每个区间只取一个代表，同时另补边界值 $100$ 与 $100.01$，比随意生成大量正数更有针对性。

> [!WARNING]
> ==划分测试不是随机抽几个输入==。划分必须来自规格、状态或属性，并保证各类互不混淆、合起来覆盖讨论范围；只测 $40,50,60$ 实际仍落在同一类。

## 与相近方法的区别

| 方法 | 主要思想 | 常见局限 |
|---|---|---|
| Random Testing | 随机组合操作序列 | 覆盖不可控，可能重复 |
| Partition Testing | 按等价类别选代表 | 划分错误会漏掉缺陷 |
| Equivalence Partitioning | 黑盒中按输入等价类设计用例 | 常偏单操作输入 |
| Inter-Class Testing | 检查多个类的协作 | 不属于单类内部测试 |

实际项目中两者可结合：先用 Partition Testing 覆盖关键状态与属性类别，再用 Random Testing 生成长操作序列，探索类内部难以预见的交互问题。
