---
title: 《数据库系统》试卷（A卷）
kind: 期末试卷
course: 数据库系统
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301114S%E3%80%91%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/%E8%AF%95%E5%8D%B7/%E5%81%87%E5%8D%B7%E5%AD%90/1.4.jpg
---

# 《数据库系统》试卷（A卷）

原件经识别和整理；“参考解答”是我们补的。

## 五、实验及现象分析（10 分）

### 实验及现象分析 1

设 U1（口令 p1）和 U2（口令 p2）是 Oracle 的合法用户，拥有 connect 和 resource 特权；U1 是第三题中 3 个基表的拥有者。写出下列操作的含义：

(1) `SQLPLUS> connect U1/p1;`

(2) `SQLPLUS> grant update(库存量) on 图书 to U2;`

(3) `SQLPLUS> set auto off;`

(4) `SQLPLUS> update 图书 set 库存量=库存量+10;`

(5) `SQLPLUS> rollback;`

知识点：[自主存取控制（GRANT、REVOKE、数据库角色）](../../../topics/数据库系统/自主存取控制.md)、[数据更新（INSERT、UPDATE、DELETE）](../../../topics/数据库系统/数据更新.md)、[事务的基本概念与ACID特性（原子性、一致性、隔离性、持续性）](../../../topics/数据库系统/事务.md)

### 实验及现象分析 2

U1 和 U2 代表的含义同上，U2 也以自己的身份进入一个 SQLPLUS 界面，U1 和 U2 的以下操作都在各自的 SQLPLUS 界面进行。试简述下列操作（这些操作都发生在上述操作之后）产生的现象或结果，并分析原因：

(1) U1 的操作：`SQLPLUS> update 图书 set 库存量=库存量+10;`

现象：

(2) U2 的操作：

```sql
SQLPLUS> set auto off;
SQLPLUS> update 图书 set 库存量=库存量-10;
```

现象：

原因：

(3) U1 的操作：`SQLPLUS> commit;`

现象：

原因：

(4) U2 的操作：`SQLPLUS> commit;`

结果：数据库中基表图书的库存量　无变化（填“有”或“无”）；

原因：

知识点：[事务的基本概念与ACID特性（原子性、一致性、隔离性、持续性）](../../../topics/数据库系统/事务.md)、[封锁（排它锁X、共享锁S、锁相容矩阵）](../../../topics/数据库系统/封锁.md)、[并发控制概述（丢失修改、脏读、不可重复读、幻读）](../../../topics/数据库系统/并发控制概述.md)
