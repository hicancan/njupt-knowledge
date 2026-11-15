---
title: 关系型数据库基础与逻辑数据模型（Logical Data Model）
requires: []
---

# 关系型数据库基础与逻辑数据模型（Logical Data Model）

## 关系型数据库基础与逻辑数据模型

先想一个问题：一个“二手车销售系统”里，既要存汽车信息（品牌、年份、售价），又要存客户信息（姓名、电话），还要存“哪位客户买了哪辆车”。如果把这些全塞进一张大表，客户“张三”买了三辆车，他的名字和电话就要重复三次。一旦张三换了手机号，你得改三处——漏一处数据就不一致了。

关系型数据库解决这个问题的思路是：==把数据拆到多张相互关联的表中==，每张表只描述一类实体，表之间通过“外键”建立联系。

**逻辑数据模型**就是在不关心具体数据库软件（MySQL、Oracle 都一样）的前提下，用表格形式刻画这些实体、属性和联系。它回答三个问题：有哪些表？每张表有哪些列？表之间怎么连？

以课件中的 **Corvettes（科尔维特跑车）数据库** 为例，它的逻辑模型包含四张表：

| 表名 | 关键列 | 说明 |
|------|--------|------|
| Corvettes | Vette_id, Body_style, Miles, Year, State | 每辆车一行 |
| Equipment | Vette_id, Feature | 某辆车有哪些配置 |
| States | State, State_name | 州代码对应州名 |
| Corvettes_Equipment | Vette_id, Equipment_id | 车与配置的多对多关联 |

下面用 Mermaid 画出表之间的关系：

```mermaid
flowchart LR
    A["Corvettes 车辆表"] -->|"Vette_id"| B["Equipment 配置表"]
    C["States 州表"] -->|"State"| A
    A -->|"Vette_id"| D["Corvettes_Equipment 关联表"]
    B -->|"Equipment_id"| D
```

> [!IMPORTANT]
> 关系模型的核心约束是：每张表有一个**主键**（唯一标识一行，如 `Vette_id`）；表之间的引用通过**外键**实现（如 `Equipment` 表中的 `Vette_id` 引用 `Corvettes` 表）。外键保证了你不能给不存在的车添加配置。

**主键与外键怎么区分？** 主键是“本表的身份证”，一张表只有一个；外键是“指向别人身份证的指针”，一张表可以有多个。拿 `Equipment` 表来说，`Equipment_id` 是主键，`Vette_id` 是外键——它指向 `Corvettes` 表的主键。

常见的一个坑：以为 `Corvettes_Equipment` 这种中间表多余。实际上，一辆车可以有多项配置（空调、皮座椅、天窗），一项配置也可以出现在多辆车上，这是**多对多关系**。关系模型**不允许**直接存多对多，必须拆成两张一对多，中间用关联表连接。少了它，就只能像开头那样制造大量冗余。

算一个例子：查询“加州（CA）里程低于 50000 的车有哪些配置”。

第一步，先按条件筛车：

$$ \text{符合条件的车} = \sigma_{\text{State}=\text{'CA'} \land \text{Miles}<50000}(\text{Corvettes}) $$

假设查得 `Vette_id = 3` 和 `Vette_id = 7` 两辆车。第二步，查它们的配置：

$$ \text{配置} = \pi_{\text{Feature}}\bigl(\sigma_{\text{Vette_id} \in \{3,7\}}(\text{Equipment})\bigr) $$

如果 `Equipment` 表里 `Vette_id=3` 对应“CD Player”，`Vette_id=7` 对应“Leather Seats”，那结果就是 `{CD Player, Leather Seats}`。拆表之后，步骤清晰，不会碰坏其他数据。

> [!WARNING]
> 设计时别把“计算出来的值”也建成一列。比如“这辆车的配置总数”可以通过 `COUNT` 实时算出来，不需要在 `Corvettes` 表里存一个 `Equip_count` 列。存了冗余列，每次增删配置都得同步更新，漏一次数据就错了。

> [!TIP]
> 记三个层次：**物理模型**关心数据怎么存在磁盘上（索引、文件组织）；**逻辑模型**关心表结构和关系（本文内容）；**概念模型**（如 E-R 图）更抽象，面向业务人员。Web 开发里你直接用 SQL 操作的是逻辑模型对应的表。
