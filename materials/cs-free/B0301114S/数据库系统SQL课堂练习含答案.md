---
title: 《数据库系统》SQL课堂练习（含答案）
kind: 习题
course: 数据库系统
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301114S%E3%80%91%E6%95%B0%E6%8D%AE%E5%BA%93%E7%B3%BB%E7%BB%9F/%E8%AF%BE%E5%A0%82%E7%BB%83%E4%B9%A0/SQL%E8%AF%BE%E5%A0%82%E7%BB%83%E4%B9%A0.pdf
---

# 《数据库系统》SQL课堂练习（含答案）

原件经识别和整理；“参考解答”是我们补的。

## 习题 1

如图所示成绩管理系统的部分表中，S 存储学生数据，C 存储课程数据，SC 存储学生选修课程的数据，假设 S 表、C 表和 SC 表的定义如下：

```sql
Create Table S (
    SNO CHAR(3), 
    SNAME CHAR(8) NOT NULL, 
    AGE Integer,
    SEX CHAR(1) DEFAULT 'M',
    Primary Key (SNO)
);

Create Table C (
    CNO CHAR(3), 
    CNAME CHAR(20) NOT NULL, -- 根据错误答案推断存在非空约束，原题未完整显示C表定义，但隐含在后续分析中
    Credit Integer,
    CHours Integer,
    Primary Key (CNO)
);

Create Table SC (
    SNO CHAR(3), 
    CNO CHAR(3), 
    GRADE Integer, 
    Primary Key (SNO, CNO), 
    Foreign Key (SNO) References S(SNO), 
    Foreign Key (CNO) References C(CNO), 
    Check (GRADE Between 0 And 100) 
);
```

**S 表实例：**

| SNO | SNAME | AGE | SEX |
| :--- | :--- | :--- | :--- |
| S1 | WANG | 20 | M |
| S2 | ZHAO | 18 | F |
| S3 | HU | 17 | M |
| NULL | XIA | 19 | F |

**C 表实例：**

| CNO | CNAME | Credit | CHours |
| :--- | :--- | :--- | :--- |
| C1 | Math | 3 | 48 |
| C2 | NULL | 4 | 64 |
| C3 | PM | 2 | 32 |
| C4 | DB | 3 | 48 |

**SC 表实例：**

| SNO | CNO | Grade |
| :--- | :--- | :--- |
| S1 | C2 | 80 |
| S1 | C3 | 70 |
| S1 | C4 | 115 |
| S2 | C1 | 60 |
| S2 | C2 | 75 |
| S2 | C2 | 90 |
| S2 | C4 | 80 |
| S3 | C1 | 85 |
| S3 | C2 | 80 |
| S3 | C4 | 85 |
| S4 | C4 | 75 |

问：请指出上述表实例的数据中存在的 5 处错误，并简述理由？

答案：

| 序号 | 表名 | 行号/序号 | 属性 | 错误之处 | 理由 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | S | 4 | SNO | 取值 NULL | S 表中的 SNO 为主键，按照实体完整性要求，不能取空值 NULL |
| 2 | C | 2 | CNAME | 取值 NULL | 按照创建 C 表的完整性约束要求，CNAME 非空（注：虽题目未显式给出 C 表建表语句，但依据参考答案及常规数据库设计原则，课程名称通常设为 NOT NULL） |
| 3 | SC | 3 | Grade | 取值 115 | SC 表的定义中定义了对 Grade 的域完整性约束，要求 Grade 取值在 0 到 100 之间 |
| 4 | SC | 5 和 6 | SNO, CNO | 主键取值重复 | SC 表定义了 (SNO, CNO) 为主键，主键的取值在整个表中应唯一、非空。第 5 行和第 6 行的 (S2, C2) 组合重复 |
| 5 | SC | 11 | SNO | 取值 S4 | SC 表定义 SNO 为外键，取值应为 S 表中已存在的 SNO 值，即 SC 表的 SNO 值应在 S1~S3 之间取值，值为 S4 则违反了参照完整性约束 |
