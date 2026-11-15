---
title: 公钥数据加密系统定义与RSA公钥加密算法（数论基础、加解密过程、密钥产生、证明、软件实现与分析）
requires: [信息安全技术/数据加密分类]
---

# 公钥数据加密系统定义与RSA公钥加密算法（数论基础、加解密过程、密钥产生、证明、软件实现与分析）

## 公钥加密与 RSA 算法核心解析

==公钥密码体制==（Public-Key Cryptosystem）由 Diffie 和 Hellman 于 1976 年提出，解决了对称加密中密钥分发困难的问题。其核心在于使用一对数学相关的密钥：公开的==公钥==用于加密或验证签名，保密的==私钥==用于解密或生成签名。

> [!IMPORTANT]
> RSA 安全性基于==大整数分解困难性==。若攻击者能分解模数 $n$，即可推算出私钥。

### RSA 算法流程与数论基础

RSA 由 Rivest, Shamir, Adleman 于 1978 年提出，基于欧拉定理。其过程包含密钥生成、加密和解密三步。

```mermaid
flowchart TD
    Start[开始] --> KeyGen[密钥生成]
    KeyGen -->|选素数 p,q| CalcN[计算 n=p*q]
    CalcN --> CalcPhi[计算 φ(n)]
    CalcPhi --> SelE[选公钥 e]
    SelE --> CalcD[算私钥 d]
    CalcD --> PubKey[公钥: {e,n}]
    CalcD --> PrivKey[私钥: {d,n}]
    
    Enc[加密: C=M^e mod n] -.->|使用公钥| Sender[发送方]
    Dec[解密: M=C^d mod n] -.->|使用私钥| Receiver[接收方]
    
    Sender -->|密文 C| Channel[公开信道]
    Channel --> Receiver
```

#### 1. 密钥产生
1.  选取两个大素数 $p, q$，计算 $n = p \times q$。
2.  计算欧拉函数 $\phi(n) = (p-1)(q-1)$。
3.  选择整数 $e$，满足 $1 < e < \phi(n)$ 且 $\gcd(e, \phi(n)) = 1$。
4.  计算 $d$，使得 $e \cdot d \equiv 1 \pmod{\phi(n)}$。
5.  公钥为 $(e, n)$，私钥为 $(d, n)$。

#### 2. 加解密过程
*   **加密**：$C = M^e \bmod n$
*   **解密**：$M = C^d \bmod n$

> [!TIP]
> 记忆口诀：**公加私解**。加密用对方公钥，解密用自己私钥。

### 正确性证明简述

为何 $M = (M^e)^d \bmod n$？
根据密钥生成条件，$ed = k\phi(n) + 1$。
由欧拉定理，若 $\gcd(M, n)=1$，则 $M^{\phi(n)} \equiv 1 \pmod n$。
故 $M^{ed} = M^{k\phi(n)+1} = (M^{\phi(n)})^k \cdot M \equiv 1^k \cdot M \equiv M \pmod n$。
即使 $\gcd(M, n) \neq 1$，通过中国剩余定理亦可证明成立。

### 实例演算

假设 $p=3, q=11$：
1.  $n = 33$, $\phi(n) = 2 \times 10 = 20$。
2.  选 $e=3$（与 20 互素）。
3.  求 $d$：$3d \equiv 1 \pmod{20} \Rightarrow d=7$（因 $21 \div 20$ 余 1）。
4.  公钥 $(3, 33)$，私钥 $(7, 33)$。
5.  若明文 $M=2$，加密 $C = 2^3 \bmod 33 = 8$。
6.  解密 $M = 8^7 \bmod 33$。
    *   $8^2 = 64 \equiv 31 \equiv -2$
    *   $8^4 \equiv (-2)^2 = 4$
    *   $8^7 = 8^4 \cdot 8^2 \cdot 8 \equiv 4 \cdot (-2) \cdot 8 = -64 \equiv 2 \pmod{33}$。
    *   结果正确。

### 常见误区与分析

| 特性 | 对称加密 (如 DES/AES) | 公钥加密 (如 RSA) |
| :--- | :--- | :--- |
| **密钥数量** | 1 个共享密钥 | 1 对密钥 (公/私) |
| **速度** | 快，适合大数据量 | 慢，适合小数据/密钥交换 |
| **安全性基础** | 混淆与扩散 | 数学难题 (大数分解) |

> [!WARNING]
> **填充必要性**：实际应用中严禁直接对短明文进行 RSA 加密（如 $M=1$ 时 $C=1$），必须使用 OAEP 等填充方案，否则易受选择明文攻击。

> [!NOTE]
> **软件实现**：由于涉及大数幂模运算，需采用“平方-乘”算法优化性能，并防范侧信道攻击。
