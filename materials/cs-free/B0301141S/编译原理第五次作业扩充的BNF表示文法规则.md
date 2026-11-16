---
title: 《编译原理》第五次作业（扩充的BNF表示文法规则）
kind: 习题
course: 编译原理
term: 2020-2021-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301141S%E3%80%91%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86/%E4%B9%A0%E9%A2%98/2020-2021-2%20%E4%BD%9C%E4%B8%9A_jly/%E7%AC%AC%E4%BA%94%E6%AC%A1%E4%BD%9C%E4%B8%9A.pptx
---

# 《编译原理》第五次作业（扩充的BNF表示文法规则）

原件经识别和整理；“参考解答”是我们补的。

用扩充的 BNF 表示以下文法规则：

$$
Z ::= A B \mid A C \mid A
$$

$$
Z := A [ B \mid C ]
$$

$$
A ::= B C \mid B C D \mid A X Z \mid A X Y
$$

$$
A := B C [ D ] \mid \{ X ( Z \mid Y ) \}
$$

$$
A ::= a A B b \mid a b
$$

$$
A ::= A a b \mid \varepsilon
$$

$$
A := a [ A B ] b
$$

$$
A := \{ a b \}
$$

### 解 1

$$
Z ::= A ( B \mid C \mid \varepsilon ) ::= A [ B \mid C ]
$$

知识点：[文法的其他表示法（扩充BNF、语法图）](../../../topics/编译原理/文法其他表示法.md)、[文法产生式、推导与规约](../../../topics/编译原理/文法产生式与推导.md)、[字母表与符号串的基本概念](../../../topics/编译原理/字母表与符号串.md)

### 解 2

$$
A ::= B C ( \varepsilon \mid D ) \{ X ( Z \mid Y ) \} ::= B C [ D ] \{ X ( Z \mid Y ) \}
$$

知识点：[文法产生式、推导与规约](../../../topics/编译原理/文法产生式与推导.md)、[语法树、最左/最右推导与文法的二义性](../../../topics/编译原理/语法树与二义性.md)、[乔姆斯基文法分类（0型、1型、2型、3型）](../../../topics/编译原理/文法分类.md)

### 解 3

$$
S ::= a ( ( A B \mid \varepsilon ) b ) ::= a [ A B ] b
$$

知识点：[文法的其他表示法（扩充BNF、语法图）](../../../topics/编译原理/文法其他表示法.md)、[字母表与符号串的基本概念](../../../topics/编译原理/字母表与符号串.md)

### 解 4

$$
A ::= \{ a b \mid \varepsilon \} ::= \{ a b \}
$$

补充：

- `[ t ]`：$t$ 或 $\varepsilon$（$t$ 可出现可不出现）
- `{ t }`：$t$ 不出现或出现任意多次
- `( )`：提取因子

所谓超前读字符（也称超前搜索），是指仅向前读取字符，判别该字符是什么，不做别的处理工作。当判明情况以后，再回过头来处理已读过的字符。

知识点：[词法分析器的功能与在编译器中的地位](../../../topics/编译原理/词法分析器功能.md)、[DFA与NFA的关系及转换（子集法）](../../../topics/编译原理/DFA与NFA等价转换.md)
