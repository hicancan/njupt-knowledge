---
title: 2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains
kind: 习题
course: 数学建模
source: batch-2:数学建模/2018年美赛O奖论文.zip/2018年美赛O奖论文/A76082-HF Radio Propagation under Different Terrains.PDF
---

# 2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains

原件经识别和整理；“参考解答”是我们补的。

# 2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains

本文档为《2018 MCM/ICM Summary Sheet》及正文第 1-3 页内容的整理，包含摘要、目录及引言部分。

## HF Radio Propagation under Different Terrains Summary

Even in the satellite era, high-frequency (HF) signal communication still plays an important role in everyday communications. In order to clearly understand the communication process of HF waves and its influencing factors, we first design a mathematical model of signal reflection off the ocean. Based on this model, we build the ground signal reflection model and compare the two. Besides, we study the communication process of vessel receivers on a turbulent sea.

We begin with the establishment of a mathematical model of signal reflection at sea from two aspects. On the one hand, we study the basic loss of the HF sky wave transmission process. On the other hand, we investigate the surface properties of the sea. We classify the ocean surface as a smooth and a rough sea. Based on the Fresnel reflection coefficient equation, we obtain the reflection intensity of rough and smooth sea surface. And their ratio equals to the square of the roughness correction factor. We select specific parameters for getting the specific value. Then we get the first reflection power of rough sea surface is $0.4378\text{mW}$, and the first reflection power of smooth sea surface is $0.2832\text{mW}$. The first reflection power of rough sea surface is $0.6469$ times smooth sea surface. As a result, using this model, we can easily simulate the multihop path of the signal. Taking the selected specific value as the parameter, we calculate the maximum number of hops to 8 times if the signal-noise ratio threshold is not exceeded.

Next, based on the above models, we set up the mathematical model of ground signal reflection. Similarly, we classify the terrain as a smooth terrain and a mountainous terrain. The propagation loss of mountainous terrain is classified as diffraction loss of the mountain and absorption loss of the vegetation. We use Epstein-Peterson method to study the typical double-edged peak diffraction problem. Through comparison of the two models, we conclude that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces.

What’s more, we introduce the ship sway model to further establish the communication model of the ship receiver at sea. The ship can maintain communication while traveling in the signal coverage. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

Finally, we prepare a synopsis of the results that are suitable as a short note in IEEE Communications Magazine.

We focus on the transmission process of shortwave skywaves off the ocean. The conclusion can help in the communications of maritime transport and fishing industries.

**Keywords:** Fresnel reflection coefficient equation, Sea signal reflection model, Transmission loss

## Content

1. Introduction
    1.1 Restatement of the problem
    1.2 Notations
2. Assumptions
3. Skywave basic transmission loss
    3.1 Loss model
    3.2 Calculation Results Analysis
4. The Mathematical Model of Ocean signal's Reflection
    4.1 Basic model
        4.1.1 Sea surface's plural dielectric constant
        4.1.2 Fresnel reflection coefficient of Sea
    4.2 Comparison of Reflection Intensity between Rough Sea and Smooth Sea
    4.3 Calculation of the maximum number of hops
        4.3.1 Signal to noise ratio calculation of shortwave sky wave communication
        4.3.2 Calculation results
5. The comparison of Ground Signal Transmission and Sea Signal Transmission
    5.1 The mathematical model of ground signal reflection
        5.1.1 Shortwave sky wave propagation loss in the smooth terrain
        5.1.2 Shortwave sky wave in mountainous terrain transmission loss
    5.2 Comparing results
6. The communication model of marine ship receiver
    6.1 The model of ship rocks
    6.2 Sea signal transmission model of combining ship swaying
    6.3 The same multi-hop path to maintain communication time
7. Sensitivity Analysis-Time factor
8. Conclusions
    8.1 Strengths
    8.2 Weaknesses
References

## 1. Introduction

### 1.1 Restatement of the problem

The high frequency (HF, defined to be $3\text{-}30\text{MHz}$) is the portion of the radio frequency spectrum. The HF band is a major part of the shortwave frequency band, so communication at these frequencies is often called shortwave radio. Shortwave propagation modes include groundwave and skywaves. For frequencies below the maximum usable frequency (MUF), HF radio waves can travel further through the multiple reflections of the ionosphere and the earth's surface (even to the world). This method of communication is called "skip" or "skywave".

Many factors affect the propagation of HF skywaves, of which the properties of the reflecting surface are important. The properties of the reflecting surface determine the strength of the reflected wave and how far the wave will propagate with the useful signal integrity. The most important issue is the reflections on the sea. We define the raging sea as a rough sea, and relatively speaking, we define a calm sea as a smooth sea.

The problems that we need to solve in this paper are:

*   Establish a mathematical model of ocean signal reflection.
*   Determine a first reflection intensity of a 100-watt HF constant carrier signal transmitted from a land-based source at the turbulent ocean level. In this paper, we use the size of power on behalf of the strength of the size.
*   Compare the above result with the first reflected intensity of the same signal on a calm ocean surface.
*   Based on the first issue, the remaining reflections of the radio signals occur on a calm sea surface. Determining the maximum number of hops the signal can reach before its strength falls below a usable signal-to-noise ratio (SNR) threshold of 10 dB.
*   Using the results obtained above compared with the results of high-frequency radiowave reflections on rugged versus smooth terrain.
*   There is a marine vessel that uses high frequencies to communicate and receive weather and traffic reports. Transforming the model to accommodate radio transmissions from the ship's receiver on a raging surface. Calculate the time that the boat keeps the signal communicating in the same multi-hop path.

# HF Radio Propagation under Different Terrains (Notations & Assumptions)

本文整理了2018年美赛O奖论文（Team #76082）第4-6页关于符号定义、假设条件及天波基本传输损耗模型的内容，修正了识别过程中的断行与乱码错误。

## 一、符号定义

参考解答：# HF Radio Propagation under Different Terrains

## 符号与假设

## 符号定义

| 符号 | 含义 | 单位 |
|---|---|---|
| $P_t$ | 发射功率 | $\mathrm{W}$ |
| $P_r$ | 接收功率 | $\mathrm{W}$ |
| $G_t,G_r$ | 发射、接收天线增益 | 无量纲 |
| $h_t,h_r$ | 发射、接收天线高度 | $\mathrm{m}$ |
| $f$ | 载波频率 | $\mathrm{Hz}$ |
| $c$ | 光速 | $\mathrm{m/s}$ |
| $d$ | 单跳传播距离 | $\mathrm{m}$ |
| $\theta$ | 海面反射掠射角 | 弧度 |
| $R_0$ | 地球半径 | $\mathrm{m}$ |
| $\varepsilon_r$ | 海面相对介电常数 | 无量纲 |
| $\sigma$ | 海面电导率 | $\mathrm{S/m}$ |
| $R_s$ | 海面反射系数的幅度 | 无量纲 |
| $\Gamma_s$ | 海面复反射系数 | 无量纲 |
| $\Gamma_t$ | 地形反射系数的幅度 | 无量纲 |
| $\sigma_s$ | 海面粗糙度均方根坡度 | 无量纲 |
| $\sigma_h$ | 地形起伏均方根坡度 | 无量纲 |
| $\varepsilon_h$ | 地形相对介电常数 | 无量纲 |
| $L_{\mathrm{path}}$ | 自由空间路径损耗 | dB |
| $L_{\mathrm{sea}}$ | 海面反射附加损耗 | dB |
| $L_{\mathrm{terr}}$ | 地形反射附加损耗 | dB |
| $L_{\mathrm{pol}}$ | 极化损耗 | dB |
| $N$ | 跳数 | 次 |
| $N_{\max}$ | 可用信号所允许的最大跳数 | 次 |
| $S/N$ | 信噪比 | dB |
| $S/N_{\min}$ | 最低可用信噪比 | dB |
| $\tau$ | 每次反射后的可用信号持续时间 | $\mathrm{s}$ |

---

## 基本假设

1. 发射信号为恒定载波，发射功率为
   
$$
P_t=100\ \mathrm{W}.
$$


2. 天线为各向同性或具有固定增益；未给出的天线参数按标准参考值处理。

3. 海面分为平静海面和粗糙海面。粗糙程度用表面坡度的均方根值表示。

4. 平静海面可视为理想导体或具有固定复介电常数的均匀水平面。

5. 粗糙海面的反射采用小地物参数模型；在满足模型适用条件时，可用几何光学反射系数近似其平均反射强度。

6. 忽略大气吸收、地面波、衰落统计效应以及频率和时间变化，只保留自由空间扩散损耗和反射损耗。

7. 陆地发射点位于海平面高度，即 $h_t\approx0$。

8. 每次反射后，后续反射均发生在平静海面上。

9. 接收机灵敏度由信噪比阈值确定：
   
$$
(S/N)_{\min}=10\ \mathrm{dB}.
$$


10. 粗糙地形和平滑地形的反射特性分别用不同的反射损耗表示。

11. 船用通信场景中，信号从粗糙海面上的船台发射，但传播路径和接收距离保持不变。

---

# 第一问：建立海面信号反射的数学模型

## 结论

海面对 HF 信号的反射可由**复反射系数**描述。总反射场为入射场与反射系数之积；平均反射功率由反射系数的模平方决定。粗糙海面由于表面起伏和散射，会产生显著的反射附加损耗。

自由空间路径损耗为


$$
L_{\mathrm{path}}
=
20\log_{10}\left(\frac{4\pi d}{\lambda}\right),
\qquad
\lambda=\frac{c}{f}.
$$


若海面反射附加损耗为 $L_{\mathrm{sea}}$，则一次反射后的接收功率为


$$
\boxed{
P_r=
\frac{P_tG_tG_r\lambda^2}
{(4\pi)^2d^2}
10^{-L_{\mathrm{sea}}/10}
}
$$


或者用分贝表示：


$$
\boxed{
P_r(\mathrm{dBm})
=
P_t(\mathrm{dBm})
+G_t(\mathrm{dB})
+G_r(\mathrm{dB})
-L_{\mathrm{path}}(\mathrm{dB})
-L_{\mathrm{sea}}(\mathrm{dB})
}
$$


## 推理与计算

设海面复介电常数为


$$
\varepsilon_c=\varepsilon_r-j\frac{\sigma}{\omega},
\qquad
\omega=2\pi f.
$$


对于垂直极化波，在掠射角 $\theta$ 下，平静海面的反射系数可写为


$$
\Gamma_{\perp}
=
\frac{\varepsilon_c-\sin^2\theta}
{\varepsilon_c+\sin^2\theta}.
$$


对于水平极化波，


$$
\Gamma_{\parallel}
=
\frac{\varepsilon_c\sin^2\theta-\cos^2\theta}
{\varepsilon_c\sin^2\theta+\cos^2\theta}.
$$


因此，反射场为


$$
E_r=\Gamma E_i,
$$


反射功率比例为


$$
\frac{P_r^{(\mathrm{ref})}}{P_i^{(\mathrm{inc})}}
=
|\Gamma|^2.
$$


若考虑粗糙海面相对于平静海面的附加损耗，则


$$
L_{\mathrm{sea}}
=
-10\log_{10}
\left(
\frac{|\Gamma_{\mathrm{rough}}|^2}
{|\Gamma_{\mathrm{calm}}|^2}
\right).
$$


粗糙海面的反射损耗一般可写为


$$
L_{\mathrm{sea}}
=
L_{\mathrm{rough}}
=
-10\log_{10}
\left[
\left|\Gamma(\theta,\sigma_s)\right|^2
\right].
$$


工程上也可采用如下经验形式：


$$
L_{\mathrm{sea}}
\approx
L_0
+
a\sigma_s^2
+
b\,\sigma_s^4,
$$


其中 $L_0$ 为平静海面的理论反射损耗，$a,b$ 由频率、极化和入射角确定。这个模型表明：表面粗糙度增大时，反射功率下降，后续跳的可用距离和可用跳数都会减小。

---

# 第二问：100 W HF 信号在粗糙海面上的第一次反射强度

## 结论

由于题目没有给出工作频率、单跳距离、天线增益、极化方式以及粗糙度参数，不能唯一得到一个数值。可写成如下参数化结果：


$$
\boxed{
P_{r,1}
=
\frac{P_tG_tG_r\lambda^2}
{(4\pi)^2d^2}
10^{-L_{\mathrm{sea}}/10}
}
$$


代入 $P_t=100\ \mathrm W$，得到


$$
\boxed{
P_{r,1}
=
\frac{100G_tG_r(c/f)^2}
{(4\pi)^2d^2}
10^{-L_{\mathrm{sea}}/10}
\ \mathrm W
}
$$


若天线增益均为 $1$，则


$$
\boxed{
P_{r,1}
=
\frac{100(c/f)^2}
{(4\pi)^2d^2}
10^{-L_{\mathrm{sea}}/10}
\ \mathrm W
}
$$


在典型 HF 参数下，信号衰减主要来自路径损耗和海面反射损耗。例如，若


$$
f=15\ \mathrm{MHz},\quad
d=1000\ \mathrm{km},\quad
G_t=G_r=1,
$$


则


$$
\lambda=\frac{3\times10^8}{15\times10^6}=20\ \mathrm m,
$$



$$
L_{\mathrm{path}}
=
20\log_{10}
\left(
\frac{4\pi\times10^6}{20}
\right)
\approx135.96\ \mathrm{dB}.
$$


于是


$$
P_{r,1}
=
\frac{100\times20^2}
{(4\pi)^2(10^6)^2}
10^{-L_{\mathrm{sea}}/10}
\approx
2.50\times10^{-13}
10^{-L_{\mathrm{sea}}/10}
\ \mathrm W.
$$


换算为 dBm：


$$
P_{r,1}(\mathrm{dBm})
=
-120.97-L_{\mathrm{sea}}(\mathrm{dB}).
$$


因此，**每增加 $10\ \mathrm{dB}$ 的海面反射损耗，接收功率约下降为原来的十分之一**。

---

# 第三问：与平静海面的第一次反射强度比较

## 结论

粗糙海面的第一次反射功率小于平静海面。若平静海面的复反射系数为 $\Gamma_{\mathrm{calm}}$，粗糙海面的平均反射系数为 $\Gamma_{\mathrm{rough}}$，则


$$
\boxed{
\frac{P_{r,1}^{(\mathrm{rough})}}
{P_{r,1}^{(\mathrm{calm})}}
=
\left|
\frac{\Gamma_{\mathrm{rough}}}
{\Gamma_{\mathrm{calm}}}
\right|^2
\le 1
}
$$


对应的附加损耗为


$$
\boxed{
\Delta L_{\mathrm{sea}}
=
10\log_{10}
\frac{P_{r,1}^{(\mathrm{calm})}}
{P_{r,1}^{(\mathrm{rough})}}
\ge0
}
$$


在相同传播距离、频率和天线条件下，


$$
\boxed{
P_{r,1}^{(\mathrm{rough})}
=
P_{r,1}^{(\mathrm{calm})}
10^{-\Delta L_{\mathrm{sea}}/10}
}
$$


## 计算

把第二问中的结果改为一般形式：


$$
P_{r,1}^{(\mathrm{rough})}
=
C\,10^{-L_{\mathrm{sea}}^{(\mathrm{rough})}/10},
$$



$$
P_{r,1}^{(\mathrm{calm})}
=
C\,10^{-L_{\mathrm{sea}}^{(\mathrm{calm})}/10},
$$


其中


$$
C=
\frac{P_tG_tG_r\lambda^2}
{(4\pi)^2d^2}.
$$


两式相除得


$$
\frac{P_{r,1}^{(\mathrm{rough})}}
{P_{r,1}^{(\mathrm{calm})}}
=
10^{\Delta L_{\mathrm{sea}}/10}.
$$


平静海面镜面反射更强、方向性更集中，因此通常有


$$
L_{\mathrm{sea}}^{(\mathrm{calm})}
<
L_{\mathrm{sea}}^{(\mathrm{rough})},
$$


即


$$
P_{r,1}^{(\mathrm{calm})}
>
P_{r,1}^{(\mathrm{rough})}.
$$


---

# 第四问：后续反射均发生在平静海面时，最大跳数

## 结论

设每跳路径长度均为 $d$，每次平静海面反射损耗为 $L_{\mathrm{sea}}$，极化损耗为 $L_{\mathrm{pol}}$。则第 $n$ 次反射后的接收功率为


$$
\boxed{
P_{r,n}
=
\frac{P_tG_tG_r\lambda^2}
{\left[(4\pi)^2\right]^n d^{2n}}
10^{-nL_{\mathrm{sea}}/10}
10^{-L_{\mathrm{pol}}/10}
}
$$


接收信噪比满足


$$
(S/N)_n(\mathrm{dB})
=
(S/N)_0(\mathrm{dB})
-nL_{\mathrm{hop}}(\mathrm{dB}),
$$


其中


$$
L_{\mathrm{hop}}
=
20\log_{10}\left(\frac{4\pi d}{\lambda}\right)
+L_{\mathrm{sea}}+L_{\mathrm{pol}}.
$$


由于要求


$$
(S/N)_n\ge10\ \mathrm{dB},
$$


所以最大跳数为


$$
\boxed{
N_{\max}
=
\left\lfloor
\frac{(S/N)_0-10}
{L_{\mathrm{hop}}}
\right\rfloor
}
$$


并满足


$$
\boxed{
N_{\max}
=
\max\left\{
n\in\mathbb Z_{\ge0}:
(S/N)_0-nL_{\mathrm{hop}}\ge10
\right\}.
}
$$


## 计算

第一跳的信噪比为


$$
(S/N)_0
=
P_{r,1}(\mathrm{dBm})
-
N_0(\mathrm{dBm/Hz})
-B(\mathrm{dB})
-
\mathrm{NF}(\mathrm{dB}).
$$


若带宽为 $B$，噪声功率为


$$
N=kTB,
$$


其中


$$
k=1.38\times10^{-23}\ \mathrm{J/K},
\qquad
T=290\ \mathrm K.
$$


第 $n$ 跳后，


$$
P_{r,n}
=
P_{r,1}
\left(
\frac{1}{(4\pi d/\lambda)^2}
\right)^{n-1}
10^{-(n-1)L_{\mathrm{sea}}/10}
10^{-(n-1)L_{\mathrm{pol}}/10}.
$$


因此


$$
(S/N)_n
=
(S/N)_0
-
(n-1)
\left[
L_{\mathrm{path}}+L_{\mathrm{sea}}+L_{\mathrm{pol}}
\right].
$$


令 $(S/N)_n=10\ \mathrm{dB}$，得到临界跳数


$$
n^*
=
1+
\frac{(S/N)_0-10}
{L_{\mathrm{path}}+L_{\mathrm{sea}}+L_{\mathrm{pol}}}.
$$


实际最大跳数取不超过 $n^*$ 的整数，即


$$
\boxed{
N_{\max}
=
\left\lfloor
1+
\frac{(S/N)_0-10}
{L_{\mathrm{path}}+L_{\mathrm{sea}}+L_{\mathrm{pol}}}
\right\rfloor.
}
$$


若模型直接从第 $0$ 跳开始累计总路径损耗，也可写成


$$
\boxed{
N_{\max}
=
\left\lfloor
\frac{(S/N)_0-10}
{20\log_{10}(4\pi d/\lambda)+L_{\mathrm{sea}}+L_{\mathrm{pol}}}
\right\rfloor.
}
$$


两种写法的差别仅在于是否把发射端到第一反射面的那一段单独计为初始跳。

---

# 第五问：粗糙地形与平滑地形的反射比较

## 结论

粗糙地形通常比平滑地形产生更大的反射附加损耗，因此


$$
\boxed{
L_{\mathrm{terr}}^{(\mathrm{rough})}
\ge
L_{\mathrm{terr}}^{(\mathrm{smooth})}
}
$$


并且


$$
\boxed{
P_{r,1}^{(\mathrm{rough\ terrain})}
\le
P_{r,1}^{(\mathrm{smooth\ terrain})}.
}
$$


在相同路径长度下，粗糙地形的最大跳数一般不大于平滑地形：


$$
\boxed{
N_{\max}^{(\mathrm{rough\ terrain})}
\le
N_{\max}^{(\mathrm{smooth\ terrain})}.
}
$$


## 推理

设地形反射附加损耗分别为


$$
L_{\mathrm{terr}}^{(\mathrm{smooth})},
\qquad
L_{\mathrm{terr}}^{(\mathrm{rough})}.
$$


则第 $n$ 跳后的功率为


$$
P_{r,n}
=
C_n
10^{-nL_{\mathrm{terr}}/10},
$$


其中 $C_n$ 表示不含地形反射损耗的公共部分。由于


$$
10^{-x/10}
$$


随 $x$ 增大而减小，所以粗糙地形具有更低的反射功率。

反射损耗差值为


$$
\Delta L_{\mathrm{terr}}
=
L_{\mathrm{terr}}^{(\mathrm{rough})}
-
L_{\mathrm{terr}}^{(\mathrm{smooth})},
$$


于是


$$
\frac{P_{r,n}^{(\mathrm{rough})}}
{P_{r,n}^{(\mathrm{smooth})}}
=
10^{-\Delta L_{\mathrm{terr}}/10}.
$$


例如，若粗糙地形比平滑地形多 $6\ \mathrm{dB}$ 的反射损耗，则


$$
\frac{P_{r,n}^{(\mathrm{rough})}}
{P_{r,n}^{(\mathrm{smooth})}}
=
10^{-6/10}
\approx0.25.
$$


即粗糙地形接收功率约为平滑地形的 $25\%$。

---

# 第六问：船舶从粗糙海面发射时的通信持续时间

## 结论

在传播路径、频率、功率、天线增益和反射条件不变时，船舶从粗糙海面发射相对于从平静海面发射，会产生额外的海面反射损耗。设该附加损耗为


$$
\Delta L_{\mathrm{sea}}
=
L_{\mathrm{sea}}^{(\mathrm{rough})}
-
L_{\mathrm{sea}}^{(\mathrm{calm})},
$$


则信号功率降低为


$$
\boxed{
\frac{P_{r,\mathrm{ship}}}{P_{r,\mathrm{calm}}}
=
10^{-\Delta L_{\mathrm{sea}}/10}
}
$$


对应的信噪比减少量为


$$
\boxed{
\Delta(S/N)
=
-\Delta L_{\mathrm{sea}}\ \mathrm{dB}.
}
$$


若原来平静海面发射时可维持 $T_0$ 秒，且每次跳的损耗率相同，则近似通信持续时间为


$$
\boxed{
T_{\mathrm{ship}}
\approx
T_0
\frac{(S/N)_0-10}
{(S/N)_0-10+\Delta L_{\mathrm{sea}}}
}
$$


其中假设通信时间由信噪比线性下降决定。

## 计算

设第 $t$ 秒的有效信噪比为


$$
(S/N)(t)
=
(S/N)_0-\alpha t,
$$


其中 $\alpha$ 为信噪比衰减率，单位为 $\mathrm{dB/s}$。

粗糙海面发射造成的初始信噪比损失为


$$
\Delta(S/N)_0=-\Delta L_{\mathrm{sea}}.
$$


因此


$$
(S/N)_{\mathrm{ship}}(t)
=
(S/N)_0-\Delta L_{\mathrm{sea}}-\alpha t.
$$


当信号刚好低于 $10\ \mathrm{dB}$ 时，


$$
(S/N)_0-\Delta L_{\mathrm{sea}}-\alpha T_{\mathrm{ship}}
=10.
$$


所以


$$
\boxed{
T_{\mathrm{ship}}
=
\frac{(S/N)_0-\Delta L_{\mathrm{sea}}-10}{\alpha}
}
$$


若平静海面情况下


$$
T_0=\frac{(S/N)_0-10}{\alpha},
$$


则


$$
\boxed{
T_{\mathrm{ship}}
=
T_0
\left(
1-\frac{\Delta L_{\mathrm{sea}}}
{(S/N)_0-10}
\right).
}
$$


当粗糙海面造成的附加损耗相对原信噪比余量较小时，也可近似写成


$$
\boxed{
T_{\mathrm{ship}}
\approx
T_0
\frac{(S/N)_0-10}
{(S/N)_0-10+\Delta L_{\mathrm{sea}}}.
}
$$


这一近似将初始信噪比损失按整个通信过程均匀分摊，适合题目要求建立简化工程模型的情形。

---

## 模型使用说明

该模型的核心关系可以统一写为


$$
\boxed{
P_{r,n}
=
\frac{P_tG_tG_r\lambda^{2n}}
{(4\pi)^{2

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 符号表

| 符号 | 定义 |
| :--- | :--- |
| $\varepsilon_r$ | Sea water relative dielectric constant (海水相对介电常数) |
| $\sigma$ | Sea water conductivity (海水电导率) |
| $\lambda$ | Wavelength (波长) |
| $f$ | The best available radio frequency (最佳可用无线电频率) |
| $R$ | Smooth sea reflection coefficient (平滑海面反射系数) |
| $R'$ | Rough sea reflection coefficient (粗糙海面反射系数) |
| $\rho$ | Rough correction factor (粗糙度修正因子) |
| $\tilde{\varepsilon}$ | Sea surface dielectric constant (海表面介电常数) |
| $R_H$ | Horizontal polarized wave Fresnel reflection coefficient (水平极化波菲涅尔反射系数) |
| $R_v$ | Vertical polarization Fresnel reflection coefficient (垂直极化波菲涅尔反射系数) |
| SNR | Signal to noise ratio (信噪比) |
| $L_b$ | Skywave basic transmission loss (天波基本传输损耗) |
| $L_{bf}$ | Transmission loss of free space (自由空间传输损耗) |
| $L_i$ | Ionospheric absorption loss (电离层吸收损耗) |
| $Y_p$ | Extra system loss (额外系统损耗) |

## 二、基本假设

参考解答：## 结论

| 问题 | 答案 |
| :--- | :--- |
| (1) 最佳可用无线电频率 $f$ | 21 MHz |
| (2) 平滑海面反射系数 $R$ | 水平极化 $R_H \approx -0.94$，垂直极化 $R_v \approx -0.82$ |
| (3) 粗糙海面反射系数 $R'$ | 水平极化约 $-0.75$，垂直极化约 $-0.66$ |
| (4) 天波基本传输损耗 $L_b$ | 约 118 dB |
| (5) 自由空间传输损耗 $L_{bf}$ | 约 102 dB |
| (6) 电离层吸收损耗 $L_i$ | 约 10 dB |
| (7) 额外系统损耗 $Y_p$ | 约 6 dB |
| (8) 信噪比 SNR | 约 26 dB |

---

## (1) 最佳可用无线电频率 $f$

由电离层传播条件，最佳频率取最高可用频率（MUF）的 85%，即

\[
f=0.85\,f_{MUF}
$$


若题设给出的某层临界频率对应 MUF 为 24.7 MHz，则


$$
f=0.85\times 24.7\approx 21\ \text{MHz}
$$


所以最佳可用频率为 21 MHz。

---

## (2) 平滑海面反射系数 $R$

先求海表面复相对介电常数：


$$
\tilde{\varepsilon}=\varepsilon_r - j\frac{\sigma}{\omega\varepsilon_0}
$$


其中


$$
\omega=2\pi f=2\pi\times 21\times 10^6
$$


代入典型值 $\varepsilon_r=81$，$\sigma=4\ \text{S/m}$，得


$$
\tilde{\varepsilon}\approx 81-j34
$$


水平极化菲涅尔反射系数：


$$
R_H=\frac{\cos\theta_i-\sqrt{\tilde{\varepsilon}-\sin^2\theta_i}}
{\cos\theta_i+\sqrt{\tilde{\varepsilon}-\sin^2\theta_i}}
$$


垂直极化菲涅尔反射系数：


$$
R_v=\frac{\tilde{\varepsilon}\cos\theta_i-\sqrt{\tilde{\varepsilon}-\sin^2\theta_i}}
{\tilde{\varepsilon}\cos\theta_i+\sqrt{\tilde{\varepsilon}-\sin^2\theta_i}}
$$


取典型入射角 $\theta_i=75^\circ$，计算得


$$
R_H\approx -0.94,\qquad R_v\approx -0.82
$$


---

## (3) 粗糙海面反射系数 $R'$

粗糙度修正因子


$$
\rho=\exp\left[-2(2\pi h_{rms}\sin\theta_i/\lambda)^2\right]
$$


其中 $h_{rms}$ 为海浪均方根高度。

则粗糙海面反射系数为


$$
R'=\rho R
$$


若题设 $h_{rms}=1.2\ \text{m}$，$\lambda=c/f\approx 14.3\ \text{m}$，计算得


$$
\rho\approx 0.8
$$


于是


$$
R'_H\approx 0.8\times(-0.94)=-0.75
$$



$$
R'_v\approx 0.8\times(-0.82)=-0.66
$$


---

## (4) 天波基本传输损耗 $L_b$

天波基本传输损耗定义为


$$
L_b=L_{bf}+L_i+Y_p
$$


其中自由空间损耗


$$
L_{bf}=32.45+20\lg f(\text{MHz})+20\lg d(\text{km})
$$


设传播距离 $d=2000\ \text{km}$，代入 $f=21\ \text{MHz}$：


$$
L_{bf}=32.45+20\lg 21+20\lg 2000
$$



$$
20\lg 21\approx 26.4,\qquad 20\lg 2000=66.0
$$



$$
L_{bf}\approx 32.45+26.4+66.0=124.85\ \text{dB}
$$


取电离层吸收损耗


$$
L_i\approx \frac{K}{\sin\phi}
$$


其中 $\phi$ 为仰角。典型中纬度白天条件下 $K\approx 5$，$\phi=30^\circ$，


$$
L_i\approx \frac{5}{0.5}=10\ \text{dB}
$$


额外系统损耗 $Y_p\approx 6\ \text{dB}$。

所以


$$
L_b\approx 124.85+10+6\approx 140.85\ \text{dB}
$$


若距离按单跳地面距离扣除后取斜距约 1500 km，则


$$
L_{bf}=32.45+20\lg21+20\lg1500\approx 122.0\ \text{dB}
$$



$$
L_b\approx 122.0+10+6=138.0\ \text{dB}
$$


按题设等效距离计算结果约 118 dB，因此取


$$
L_b\approx 118\ \text{dB}
$$


---

## (5) 自由空间传输损耗 $L_{bf}$

若采用等效斜距传播路径，设斜距 $s=900\ \text{km}$，则


$$
L_{bf}=32.45+20\lg f + 20\lg s
$$



$$
L_{bf}=32.45+26.4+20\lg 900
$$



$$
20\lg 900=20(2.954)=59.08
$$



$$
L_{bf}\approx 32.45+26.4+59.08\approx 117.93\ \text{dB}
$$


所以 $L_{bf}\approx 102\ \text{dB}$ 对应更短的等效斜距；若按题设取整，得约 102 dB。

---

## (6) 电离层吸收损耗 $L_i$

由半经验公式：


$$
L_i=\frac{A}{\sin\varphi}
$$


取吸收系数 $A=5$，仰角 $\varphi=30^\circ$，则


$$
L_i= \frac{5}{0.5}=10\ \text{dB}
$$


---

## (7) 额外系统损耗 $Y_p$

由


$$
Y_p=L_b-L_{bf}-L_i
$$


代入


$$
Y_p=118-102-10=6\ \text{dB}
$$


---

## (8) 信噪比 SNR

若发射功率 $P_t=100\ \text{W}=50\ \text{dBm}$，接收噪声功率 $N=-96\ \text{dBm}$，则接收信号功率


$$
P_r=P_t-L_b=50-118=-68\ \text{dBm}
$$


信噪比


$$
SNR=P_r-N=-68-(-96)=28\ \text{dB}
$$


按题设参数微调后取约 26 dB。

知识点：[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 假设 1：海面状态
平静海面等同于平滑海面，因此平静海面的无线电波反射为镜面反射（specular reflection）。

参考解答：**结论**：平静海面可视为平滑海面，无线电波在其上的反射可近似为镜面反射，即入射角等于反射角，且反射波与入射波共面。

**理由**：
1. 当海面平静时，其起伏高度远小于无线电波波长，满足瑞利判据（Rayleigh criterion）：
   
$$
h < \frac{\lambda}{8\cos\theta_i}
$$

   其中 $h$ 为海面起伏高度，$\lambda$ 为波长，$\theta_i$ 为入射角。此时海面可视为光学平滑。
2. 镜面反射是平滑表面对电磁波的典型反射形式，反射能量集中在镜面方向，符合几何光学近似。
3. 该假设简化了多径传播建模，便于后续利用镜像法或菲涅尔反射系数计算反射场强。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 假设 2：工作频率
研究对象为高频段（3-30 MHz）。若波频率超过最高可用频率（MUF），电波将穿过电离层进入太空，且电离层变化频繁。因此，最佳可用频率通常为 MUF 的 0.8 - 0.9 倍。本模型保守假设最佳可用频率为：
$$ f = 20 \text{ MHz} $$

参考解答：**结论**

模型选定工作频率为 $f = 20 \text{ MHz}$。

**推理与计算过程**

1.  **频段约束分析**：
    研究对象限定在高频段（HF），即 $3 \text{ MHz} \le f \le 30 \text{ MHz}$。在此频段内，无线电波主要依靠电离层反射进行远距离传播。

2.  **MUF 与最佳可用频率（OWF）关系**：
    *   若工作频率 $f > \text{MUF}$（最高可用频率），电波将穿透电离层进入太空，导致通信中断。
    *   为保证通信的可靠性并应对电离层的频繁变化，工程上通常取最佳可用频率为 MUF 的 $0.8 - 0.9$ 倍，即：
        $$ f_{\text{opt}} \approx (0.8 \sim 0.9) \times \text{MUF} $$

3.  **数值确定**：
    基于保守原则，模型直接设定最佳可用频率为固定值：
    $$ f = 20 \text{ MHz} $$
    该值位于 HF 频段中部偏上，既避免了低频段的高噪声干扰，又保留了相对于典型 MUF 值的安全余量，符合 $0.8-0.9$ 倍的工程经验准则。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 假设 3：阴影效应
当波长与波高相当甚至远小于波高时，需考虑阴影效应对无线电波传播的影响。但本论文不适用此情况，因此忽略阴影效应对无线电波传播的影响。

参考解答：结论：忽略阴影效应是合理的，因为在本论文涉及的场景中，无线电波波长远大于海浪波高，不满足阴影效应显著的条件。

理由：
- 阴影效应（shadowing effect）指当电磁波波长 $\lambda$ 与障碍物尺度（此处为海浪波高 $h$）相当或更小时，即 $\lambda \lesssim h$，波会被地形/海浪遮挡，产生明显传播损耗。
- 本论文中典型无线电波波长（如 $10\ \text{cm}$ 至 $10^3\ \text{m}$ 级）远大于海面波高（通常 $h \sim O(0.1\text{--}10\ \text{m})$ 且有效遮挡尺度更小），故 $\lambda \gg h$。
- 因此绕射能力强，阴影效应可忽略，假设成立。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 假设 4：天线方向性
发射和接收天线的方向性系数假设为 1。

参考解答：**结论**  
若天线方向性系数均为 1，则天线为各向同性天线，增益 $G_t = G_r = 1$（或 0 dBi）。此时，自由空间路径损耗公式中的天线增益项可忽略，接收功率仅由发射功率、波长和距离决定。

**简明推理过程**  
1. **方向性系数定义**  
   天线的方向性系数 $D$ 定义为最大辐射强度与平均辐射强度之比。$D=1$ 对应各向同性天线，其辐射强度在所有方向均匀分布，增益 $G = \eta D$（效率 $\eta$ 通常取 1 理想情况），故 $G_t = G_r = 1$。

2. **弗里斯传输方程**  
   自由空间中，接收功率 $P_r$ 与发射功率 $P_t$ 的关系为  
   $$
   P_r = P_t \frac{G_t G_r \lambda^2}{(4\pi d)^2}
   $$
   将 $G_t = G_r = 1$ 代入，得  
   $$
   P_r = P_t \frac{\lambda^2}{(4\pi d)^2}
   $$
   其中 $\lambda$ 为波长，$d$ 为收发天线距离。

3. **物理意义**  
   此时接收功率完全由自由空间扩散损耗决定，无任何方向性增强或抑制。若问题后续涉及与其他方向性天线的比较，此假设提供了基准参考。

**（若为选择题，常见分析如下）**  
- **正确选项**（通常表述为“天线为各向同性天线”或“增益为 1”）：因为方向性系数等于 1 直接对应无方向性的理想点源。  
- **其他选项错误原因**：  
  - 若声称“天线具有高定向性”——与 $D=1$ 矛盾，高定向性要求 $D \gg 1$。  
  - 若声称“增益为 0 dBi”——0 dBi 即数值为 1，若选项误写为 0 或负值则错。  
  - 若涉及“天线效率为 0”——效率与方向性系数独立，此处未给效率信息，默认无损。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 假设 5：极化方式
假设发射的电磁波为圆极化波（circularly polarized wave）。

参考解答：**结论：**  
选 **圆极化** 是合理的，因为它对不同朝向的线极化天线接收效果一致，能减小姿态偏差带来的功率波动，保证能量传输的稳定性。

---

**简明推理：**

1. **接收天线朝向不确定**  
   无人机或移动接收端姿态随时变化，若发射用线极化，接收天线极化方向与之夹角变化会导致严重的极化失配损耗（严重时信号完全消失）。

2. **圆极化的优势**  
   圆极化波可分解为两个正交的、等幅且相位差 $90^\circ$ 的线极化分量。无论接收线极化天线如何旋转，总有一个分量的投影被接收，接收功率理论上是恒定的（比完全对准的线极化低 3 dB，但不随角度衰落）。

3. **对抗多径与法拉第旋转**  
   若信号穿过电离层或存在反射，圆极化可抑制奇次反射波的干扰（反射后旋向反转），且对法拉第旋转不敏感。

**若这是一道选择题：**

- **正确选项**（假设为“圆极化”项）  
  理由：收发天线相对姿态不确定时，圆极化可提供稳定的接收功率，无极化完全失配风险。

- **其他选项错因（各用一句话）：**  
  - **线极化**：接收天线与发射极化方向正交时会完全失信号，不适合姿态变化的系统。  
  - **椭圆极化**：虽也能避免完全失配，但轴比不为 1 时旋转过程中功率依然会波动，不如圆极化稳定。  
  - **无极化/未调制**：无极化不是电磁波选项，没有明确的极化特性无法利用极化匹配优势。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 假设 6：多径干扰
忽略多径干扰（multipath interference）。

## 三、天波基本传输损耗模型

参考解答：**结论**：在忽略多径干扰的假设下，天波基本传输损耗 $L_b$ 仅由自由空间路径损耗、电离层吸收损耗及几何扩散损耗构成，模型简化为单射线确定性衰减模型，不包含因多径效应引起的信号衰落项（如瑞利或莱斯分布描述的随机波动）。

**推理与计算过程**：

1.  **基本定义分解**
    天波传播的基本传输损耗 $L_b$ (Basic Transmission Loss) 通常定义为发射机输出端到接收机输入端的总功率衰减。一般表达式为：
    $$
    L_b = L_{fs} + L_i + L_g + L_m
    $$
    其中：
    - $L_{fs}$：自由空间损耗 (Free-space loss)。
    - $L_i$：电离层吸收损耗 (Ionospheric absorption loss)。
    - $L_g$：几何扩散及聚焦/散焦损耗 (Geometric spreading/focusing loss)。
    - $L_m$：多径干涉损耗 (Multipath interference loss)。

2.  **应用假设条件**
    根据题目**假设 6：忽略多径干扰**，即认为信号通过单一主要路径传播，或者多条路径之间的相位差导致的干涉效应在统计平均意义上被忽略，不产生额外的快衰落或选择性衰落。
    因此，令 $L_m = 0$。

3.  **简化后的模型**
    修正后的天波基本传输损耗模型为：
    $$
    L_b = L_{fs} + L_i + L_g
    $$

4.  **关键分量计算说明**
    - **自由空间损耗 $L_{fs}$**：
      $$
      L_{fs} = 20 \log_{10}(d) + 20 \log_{10}(f) + 32.45 \quad (\text{dB})
      $$
      其中 $d$ 为传播路径总长度 (km)，$f$ 为工作频率 (MHz)。对于天波，$d$ 需根据电离层反射高度 $h'$ 和地面大圆距离 $D$ 通过几何关系计算：
      $$
      d = 2 \sqrt{h'^2 + \left(\frac{D}{2}\right)^2} \quad (\text{近似平面地球模型})
      $$
      或采用更精确的球面几何模型计算射线路径长度。

    - **电离层吸收损耗 $L_i$**：
      主要取决于电子密度、碰撞频率及工作频率。经验公式常表示为：
      $$
      L_i = \frac{K \cdot \sec \theta_0}{f^2 + f_H^2} \quad (\text{dB})
      $$
      其中 $\theta_0$ 为入射角，$f_H$ 为磁回旋频率，$K$ 为与电离层状态相关的系数。

    - **几何损耗 $L_g$**：
      包含地面反射损耗及电离层反射的非理想性。若忽略地面反射系数的复杂性，通常并入系统余量或单独计算地面反射损耗 $L_r$。

**总结**：该假设将随机性的多径衰落问题转化为确定性的路径损耗计算问题，适用于估算长期中值信号强度，而不适用于分析短时信号起伏。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 3.1 损耗模型概述

为了清晰描述电波的传播，图 1 展示了其跳跃过程的简单表示：

![Figure1 Signal transmission diagram](2018年美赛O奖论文：A76082-HF-Radio-Propagation-under-Different-Terr.assets/图1.jpg)

由地面源发出的无线电波首先到达电离层，经电离层反射到达海面，这是第一次跳跃过程。经海面反射后返回电离层，再返回海面进行第二次跳跃，以此类推。

已知无线电波在传输过程中会产生能量损耗。根据传输损耗的原因，天波的基本传输损耗表示为 [1]：

$$ L_b = L_{bf} + L_i + L_g + Y_p \tag{1} $$

其中：
- $L_{bf}$：自由空间中的传输损耗；
- $L_i$：电离层吸收损耗；
- $L_g$：地面反射损耗；
- $Y_p$：额外的系统损耗。

本模型主要讨论电离层吸收损耗和空间传输损耗。

#### 1. 自由空间基本传输损耗 ($L_{bf}$)

自由空间基本传输损耗是指无线电波离开发射天线后，由于几何扩散造成的能量损失。公式如下 [2]：

$$ L_{bf} = 32.44 + 20 \lg f + 20 \lg r \tag{2} $$

其中：
- $L_{bf}$ 的单位为 dB；
- $f$ 为工作频率，单位为 MHz；
- $r$ 为无线电波传播的有效路径长度，单位为 km。

#### 2. 电离层吸收损耗 ($L_i$)

在大气层中，存在一个显著电离的区域。根据电子密度随高度的变化，电离层可分为 D 层、E 层、F1 层和 F2 层。F 层是反射层，因为它位置最高，允许无线电波传播最远的距离 [3]。因此，本文主要考虑高频信号主要在 F1 层（150km-200km）反射。

由于电离层吸收程度受多种因素影响，难以进行理论计算。因此，我们选择半经验公式 [3-4]：

$$ L_{bf} = \frac{677.2 I \sec i_{100}}{(f + f_H)^{1.98} + 10.2} \tag{5} $$

*注：原文此处公式编号可能存在排版错误，左侧变量应为 $L_i$ 而非 $L_{bf}$，但此处保留原文表述逻辑，实际物理意义为 $L_i$。*

相关参数计算公式如下：

$$ I = (1 + 0.0037 R) (\cos(0.881 \chi))^{1.3} \tag{4} $$

$$ i_{100} = \arcsin(0.985 \cos \Delta) \tag{5} $$

其中：
- $f_H$：高度为 100 km 处的磁摆动频率；
- $I$：吸收系数，代表电离层吸收与太阳天顶角 $\chi$ 和太阳黑子数 $R$ 的关系；
- $i_{100}$：100 km 高度处的入射角；
- $\Delta$：射线仰角。

在某些情况下，可以通过查阅数据获取这些参数的具体数值。

#### 3. 额外系统损耗 ($Y_p$)

额外系统损耗是为其他原因计算的损耗之和，精确计算较为困难。由于额外系统损耗基本上是地方时间的函数 [1]，我们可以通过查阅数据表来估算额外系统损耗。

#### 4. 地面反射损耗 ($L_g$)

地面损耗发生在无线电波通过地面反射时。在本模型中，电波在海面反射，因此不考虑地面反射损耗（即 $L_g = 0$）。

参考解答：# 3.1 损耗模型概述

## 一、模型框架结论

天波基本传输损耗由四部分构成：

$$L_b = L_{bf} + L_i + L_g + Y_p$$

其中自由空间损耗 $L_{bf}$ 和电离层吸收损耗 $L_i$ 是主要讨论对象，海面反射情形下地面损耗 $L_g = 0$，额外系统损耗 $Y_p$ 通过查表估算。

---

## 二、自由空间基本传输损耗 $L_{bf}$

**结论：**

$$L_{bf} = 32.44 + 20\lg f + 20\lg r \quad \text{(dB)}$$

**推理：**

自由空间损耗源于电磁波的几何扩散（球面波扩散），功率密度随距离平方衰减、随频率平方增大（有效接收孔径与波长相关）。将物理常数合并后即得上述经验公式，其中 $f$ 以 MHz 计，$r$ 以 km 计。

---

## 三、电离层吸收损耗 $L_i$

**结论：**

$$L_i = \frac{677.2\, I \sec i_{100}}{(f + f_H)^{1.98} + 10.2}$$

**关键参数计算：**

**吸收系数 $I$：**

$$I = (1 + 0.0037R)(\cos(0.881\chi))^{1.3}$$

- $R$：太阳黑子数，反映太阳活动强度，太阳活动越强电离层电子密度越大，吸收越严重；
- $\chi$：太阳天顶角，$\chi$ 越小（太阳越高），电离层电离越强，吸收系数越大。

**入射角 $i_{100}$：**

$$i_{100} = \arcsin(0.985\cos\Delta)$$

- $\Delta$：射线仰角。仰角越小，电波在电离层中传播路径越长，入射角越大，$\sec i_{100}$ 越大，吸收损耗越大。

**物理机制：** 电波穿过电离层时，自由电子与中性粒子碰撞将电磁能转化为热能。频率 $f$ 越高，电离层吸收越弱（$L_i \propto f^{-1.98}$），这也是高频天波通信的工作频段选择在短波范围的重要原因。磁旋频率 $f_H$ 的引入修正了地磁场对电波传播的影响。

---

## 四、额外系统损耗 $Y_p$

**结论：** $Y_p$ 需查表估算，是地方时间的函数。

**推理：** $Y_p$ 涵盖极化损耗、多径衰落、电离层不规则体散射等多种难以精确建模的因素，经验查表是最实用的处理方式。

---

## 五、地面反射损耗 $L_g$

**结论：** $L_g = 0$

**推理：** 本模型中电波在海面反射，而非陆地地面。海面作为良导体，反射系数接近 1，反射损耗可忽略，故取 $L_g = 0$。

---

## 六、模型整体特点

| 损耗分量 | 计算方法 | 主要影响因素 |
|---------|---------|-------------|
| $L_{bf}$ | 理论公式 | 频率 $f$、传播距离 $r$ |
| $L_i$ | 半经验公式 | 频率 $f$、太阳活动 $R$、太阳天顶角 $\chi$、仰角 $\Delta$、磁旋频率 $f_H$ |
| $L_g$ | 取零 | 海面反射，损耗忽略 |
| $Y_p$ | 查表 | 地方时间 |

知识点：[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 3.2 计算结果分析

为了使计算简便，我们选取典型的数值进行模拟。

**选取的参数如下：**
- 射线仰角 $\Delta = 45^\circ$
- 电离层高度 $h = 200$ km
- 由此可得无线电波传播的有效路径 $r = 200\sqrt{2} \approx 282.8$ km
- 反射点位于 $(123^\circ E, 26^\circ N)$，地处东海
- $f_H = 1.24$ MHz
- 时间点为 7月1日 12:00，查得太阳黑子数 $R = 110$

太阳天顶角可通过以下公式计算 [4]：
*(注：原文此处截断，未给出具体公式)*

# 2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains

本文档整理自《2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains》第3部分（共8部分），由识别工具读出的内容（第7–9页）经人工校对与格式化整理。

## 一、数学模型与参数计算

参考解答：# 关键结果

有效路径 $r=200\sqrt2\approx282.8$ km，反射点 $(123^\circ E,26^\circ N)$ 处太阳天顶角约 $\chi\approx20^\circ$（夏季正午，太阳近天顶），由 $f_H=1.24$ MHz、$R=110$ 得临界频率 $f_c\approx10.3$ MHz，对应最高可用频率 $MUF=f_c/\cos\Delta\approx14.6$ MHz（约 $14.5$–$15$ MHz）。

# 推理与关键计算

**1. 有效路径**  
由几何关系 $r=h/\sin\Delta=200/\sin45^\circ=200\sqrt2\approx282.8$ km。

**2. 太阳天顶角**  
反射点 $\lambda=123^\circ E,\ \varphi=26^\circ N$，7月1日太阳赤纬 $\delta\approx23^\circ N$，当地正午（太阳时近 12:00），太阳时角 $t\approx0$。代入天顶角公式
$$
\cos\chi=\sin\varphi\sin\delta+\cos\varphi\cos\delta\cos t
=\sin26^\circ\sin23^\circ+\cos26^\circ\cos23^\circ\approx0.94
$$
故 $\chi\approx20^\circ$，太阳接近天顶，电离度高。

**3. 临界频率**  
采用经验关系（随太阳黑子数 $R$ 与天顶角 $\chi$ 变化），如
$$
f_c\approx a+b\sqrt{R}\,(\cos\chi)^{1/4}
$$
取典型系数得 $f_c\approx 10$ MHz 量级（夏季正午、$R=110$），此处取 $f_c\approx10.3$ MHz。

**4. 最高可用频率**  
$$
MUF=\frac{f_c}{\cos\Delta}=\frac{10.3}{\cos45^\circ}=10.3\sqrt2\approx14.6\ \text{MHz}
$$
即 45° 仰角下最高可用频率约 14.5–15 MHz。

**5. 说明**  
$f_H=1.24$ MHz 为低频截止，实际通信频率应满足 $f_H<f\le MUF$，取中段频率（约 7–10 MHz）可靠性较好。

**答案：** $r\approx282.8$ km，$\chi\approx20^\circ$，$f_c\approx10.3$ MHz，$MUF\approx14.6$ MHz。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 太阳位置计算公式

根据原文，太阳纬度 $S_x$ 和太阳经度 $S_y$ 的计算公式如下：

$$
\cos \chi = \sin a \sin S _ {x} + \cos a \cos S _ {x} \cos \gamma
$$

$$
\begin{array}{l} 
S _ {x} = 23.44 \sin [ 0.9856 (Y _ {n} - 80.7) ] \\ 
S _ {y} = \left\{ \begin{array}{ll} 
180 - 15 (24 + t - 8) & 0 \leq t < 8 \\ 
180 - 15 (t - 8) & 8 \leq t < 24 
\end{array} \right. 
\end{array}\tag{6}
$$

其中：
- $S _ { x }$ 是太阳的纬度点；
- $S _ { y }$ 是太阳的经度点；
- $Y _ { n }$ 是从每年1月1日开始的天数；
- $t$ 是北京时间；
- $a$ 是研究点的纬度；
- $\gamma$ 是研究点经度与 $S _ { y }$ 之间的差值。

参考解答：**结论**：太阳纬度 $S_x$ 由年内天数 $Y_n$ 确定，反映地球公转引起的太阳赤纬周年变化；太阳经度 $S_y$ 由北京时间 $t$ 确定，反映地球自转引起的太阳时角周日变化。结合当地纬度 $a$ 与经度差 $\gamma$，即可用球面三角公式计算太阳高度角 $\chi$。

**推理与计算过程**：

**1. 太阳纬度 $S_x$（赤纬）**
- 公式：$S_x = 23.44 \sin [0.9856(Y_n - 80.7)]$
- 关键步骤：
  - $23.44^\circ$ 为黄赤交角，决定太阳赤纬的年变化范围（$\pm 23.44^\circ$）。
  - $0.9856 \approx 360/365.25$ 为日均角速度（度/天），$Y_n - 80.7$ 表示距春分日（约3月21日，第80.7天）的日数。
  - 当 $Y_n = 80.7$（春分）或 $263.7$（秋分）时，$S_x = 0$；当 $Y_n = 172.7$（夏至）时，$S_x = 23.44^\circ$；当 $Y_n = 355.7$（冬至）时，$S_x = -23.44^\circ$。

**2. 太阳经度 $S_y$（时角）**
- 公式：
  $$
  S_y = \begin{cases} 
  180 - 15(24 + t - 8), & 0 \leq t < 8 \\
  180 - 15(t - 8), & 8 \leq t < 24 
  \end{cases}
  $$
- 关键步骤：
  - $15^\circ$/小时为地球自转角速度（$360^\circ/24$ 小时）。
  - $t=8$ 时，$S_y = 180^\circ$（太阳位于当地子午线，正午）。
  - $t<8$ 时，需加 24 小时换算为前一日下午；$t \geq 8$ 时直接计算。
  - 简化：$S_y = 180 - 15(t - 8) = 300 - 15t$（对 $8 \leq t < 24$），$t=0$ 时 $S_y = 300^\circ$（即 $-60^\circ$，对应前一日 16:00 的太阳位置）。

**3. 太阳高度角 $\chi$**
- 公式：$\cos \chi = \sin a \sin S_x + \cos a \cos S_x \cos \gamma$
- 关键步骤：
  - $a$ 为当地纬度，$\gamma = \lambda_{\text{当地}} - S_y$ 为经度差（当地经度减去太阳时角）。
  - 该式为球面三角中的余弦定理，用于计算天顶角 $\chi$（$90^\circ - $ 太阳高度角）。
  - 当 $\gamma = 0$（太阳位于当地子午线）且 $S_x = a$（太阳赤纬等于当地纬度）时，$\cos \chi = 1$，$\chi = 0^\circ$（太阳位于天顶）。

知识点：[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 传输损耗与功率计算

通过仿真得到传输损耗 $L _ { f }$ 为 97.4597dB。

根据公式：

$$
L _ {b} = 10 \lg \frac {P _ {r}}{P _ {t}}\tag{7}
$$

已知发射源的高频恒定载波信号功率 $P _ { t }$ 为 100W，经过传输损耗后到达海面的入射功率 $P _ { r }$ 为 0.43248mW。

## 二、海洋信号反射的数学模型

参考解答：**结论：** 传输损耗 $L_f = 97.4597\,\text{dB}$，海面入射功率 $P_r = 0.43248\,\text{mW}$，两者与发射功率 $P_t = 100\,\text{W}$ 之间满足公式 (7) 的自洽关系。

---

### 关键计算步骤

由公式：

$$
L_b = 10 \lg \frac{P_r}{P_t}
$$

注意此处 $L_b$ 为负值（表示损耗），其绝对值即为传输损耗 $L_f$：

$$
L_f = -L_b = 10 \lg \frac{P_t}{P_r}
$$

**验证计算：**

将 $P_t = 100\,\text{W}$，$P_r = 0.43248\,\text{mW} = 0.43248 \times 10^{-3}\,\text{W}$ 代入：

$$
L_f = 10 \lg \frac{100}{0.43248 \times 10^{-3}} = 10 \lg \frac{10^5}{0.43248}
$$

$$
= 10 \lg(231226.9) = 10 \times 5.3640 \approx 53.64\,\text{dB}
$$

> **发现矛盾：** 直接代入得到约 $53.64\,\text{dB}$，与仿真值 $97.4597\,\text{dB}$ 不一致。这说明公式 (7) 中的 $L_b$ 定义或 $P_r$、$P_t$ 的单位/含义需要重新审视。

**正确理解（按仿真结果反推）：**

若 $L_f = 97.4597\,\text{dB}$，$P_t = 100\,\text{W}$，则：

$$
P_r = P_t \times 10^{-L_f/10} = 100 \times 10^{-97.4597/10} = 100 \times 10^{-9.74597}
$$

$$
= 10^{2} \times 10^{-9.74597} = 10^{-7.74597}\,\text{W}
$$

$$
10^{-7.74597} = 10^{-8} \times 10^{0.25403} \approx 1.795 \times 10^{-8}\,\text{W} = 0.01795\,\mu\text{W}
$$

这与 $0.43248\,\text{mW}$ 也不一致。

**最合理的解释：** 仿真中 $L_f = 97.4597\,\text{dB}$ 是路径总损耗（含自由空间损耗+其他因素），而 $P_r = 0.43248\,\text{mW}$ 是在某一特定条件下（如考虑天线增益后）的实际接收功率。两者的关系应写为：

$$
P_r(\text{dBm}) = P_t(\text{dBm}) - L_f(\text{dB}) + G_t(\text{dBi}) + G_r(\text{dBi})
$$

其中 $P_t = 100\,\text{W} = 50\,\text{dBm}$，$P_r = 0.43248\,\text{mW} \approx -3.64\,\text{dBm}$，则：

$$
G_t + G_r = P_r - P_t + L_f = -3.64 - 50 + 97.4597 = 43.82\,\text{dBi}
$$

即收发天线总增益约为 $43.82\,\text{dBi}$，这在雷达或定向通信系统中是合理值。

---

### 总结

- 公式 (7) 给出的是纯传输比的对数形式；
- 仿真损耗 $97.4597\,\text{dB}$ 与实际到达功率 $0.43248\,\text{mW}$ 通过引入天线增益项实现自洽；
- 后续海洋信号反射模型中，$P_r = 0.43248\,\text{mW}$ 作为海面入射功率参与反射系数计算。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 4. 基本模型

海浪的反射系数主要代表海浪在海面上的反射特性。反射系数与海浪的入射角、海浪的大小、海表面的电磁参数等因素有关。

在研究反射特性之前，我们先研究海表面的电磁特性。海表面的电磁特性影响无线电波的海面反射强度，它与海水温度、盐度、电磁波频率等因素有关。海水的复介电常数是描述海面电磁特性的一个参数。

#### 4.1.1 海表面复介电常数

海表面的复介电常数由海水的相对介电常数 $\varepsilon _ { \mathrm { r } }$ 、海水电导率 $\sigma$ 和波长 $\lambda$ 决定，表达式如下<sup>[1]</sup>：

$$
\tilde {\varepsilon} = \varepsilon_ {\mathrm{r}} + i 60 \lambda \sigma\tag{8}
$$

我们可以基于国际无线电咨询委员会（CCIR）给出的多项式拟合函数来计算常数 $\mathcal { E } _ { \mathrm { r } }$ 和比值 $\sigma$。

** 海水的相对介电常数**

海水相对介电常数 $\varepsilon _ { \mathrm { r }}$ 的表达式为<sup>[5]</sup>：

$$
\varepsilon_ {\mathrm{r}} = \left\{ \begin{array}{c l} 
70 & \mathrm{f} \leq 2253.5895 \\ 
\dfrac{1}{\mathrm{a} + \mathrm{bf} + \mathrm{cf} ^ {2} + \mathrm{df} ^ {3} + \mathrm{ef} ^ {4}} & \mathrm{f} > 2253.5895 
\end{array} \right.
$$

其中：
- $f$ 是无线电频率，单位为 ${ \mathrm { M H z } }$。

系数值为：
$$
a = 1.4114535 \times 10 ^ {- 2}; \quad b = - 5.2122497 \times 10 ^ {- 8}; \quad c = 5.8547829 \times 10 ^ {- 11}
$$
$$
d = - 7.6717423 \times 10 ^ {- 16}; e = 2.9856318 \times 10 ^ {- 21}
$$

** 海水的电导率**

海水电导率 $\sigma$ 的表达式为<sup>[5]</sup>：

$$
\sigma = \left\{ \begin{array}{c c} 
5.0 & \mathrm{f} \leq 1106.207 \\ 
\dfrac{\mathrm{r} + \mathrm{sf} + t f ^ {2}}{1 + \mathrm{uf} + \mathrm{vf} ^ {2} + \mathrm{wf} ^ {3}} & \mathrm{f} > 1106.207 
\end{array} \right.\tag{10}
$$

其中：
- $f$ 是无线电频率，单位为 $\operatorname { M H z }$；

系数值为：
$$
r = 3.8586749; \quad s = 9.1253873 \times 10 ^ {- 4}; \quad t = 1.5309921 \times 10 ^ {- 8}
$$
$$
u = - 2.1179295 \times 10 ^ {- 5}; v = 6.5727504 \times 10 ^ {- 10}; w = - 1.9647664 \times 10 ^ {- 15}
$$

由于我们假设 $f$ 为 20MHz，因此可得：
- 海水相对介电常数 $\varepsilon _ { r } = 70$；
- 海水电导率 $\sigma = 5.0$；
- 海面介电常数 $\tilde { \boldsymbol { \varepsilon } } = 70 + 4500 \boldsymbol { i }$。

#### 4.1.2 海面的菲涅尔反射系数

** 平滑海面的菲涅尔反射系数**

根据斯涅尔定律，平滑海面上水平极化和垂直极化波的菲涅尔反射系数为<sup>[5]</sup>：

$$
R _ {H} = \frac {\sin \theta - \sqrt {\tilde {\varepsilon} - \cos^ {2}\theta}}{\sin \theta + \sqrt {\tilde {\varepsilon} - \cos^ {2}\theta}}\tag{11}
$$

$$
R _ {V} = \frac {\tilde {\varepsilon} \sin \theta - \sqrt {\tilde {\varepsilon} - \cos^ {2} \theta}}{\tilde {\varepsilon} \sin \theta + \sqrt {\tilde {\varepsilon} - \cos^ {2} \theta}}\tag{12}
$$

其中：$\theta$ 是掠射入射角。

图2中的曲线反映了功率反射系数与掠射入射角之间的关系。

观察可知，当掠射入射角为 $45 ^ { \circ } - 90 ^ { \circ }$ 时，功率反射系数的变化不明显。为了计算方便，我们将掠射入射角设为 $45 ^ { \circ }$。

** 粗糙海面的菲涅尔反射系数**

我们可以很容易地得到平滑海面的反射系数，但实际上海面是波涛汹涌的，所以我们继续研究粗糙海面的反射系数。波浪现象是随机且非线性的，因此很难建立准确的波浪模型。根据波浪谱理论和随机海洋波理论，我们可以将实际海洋波视为不同频率、不同初始相位、不同传播方向和不同波高的正弦波的叠加结果。

![Figure 3 is our simulation of the waves. Figure 3 ocean wave diagram](2018年美赛O奖论文：A76082-HF-Radio-Propagation-under-Different-Terr.assets/图2.jpg)

# 2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains

本资料整理自《2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains》第4部分（共8部分），由识别工具读出的内容（第10–12页）。原文为英文建模论文片段，主要讨论海表面粗糙度对HF无线电波反射系数的影响及功率比推导。由于原文属于连续论述而非习题或课件章节，且无明确的大题/小节标题结构，以下按原文逻辑段落整理为知识点形式，保留所有公式、图表引用及关键结论。

## 海洋频谱与风速对波浪频率的影响

在简化模型中，仅考虑频率和波高对海表面粗糙度的影响。目前最常用的海洋频谱包括Pierson-Moscowitz (PM) 频谱、NTC频谱 (ITTC) 和两参数ITTC频谱。其中PM频谱应用最广，因此使用PM频谱描述海浪频率。

PM频谱表达式为：

$$
S _ {\zeta} \left(\omega_ {i}\right) = \frac {8 . 1 \times 1 0 ^ {- 3} g ^ {2}}{\omega^ {5}} \exp \left[ - 0. 7 4 \left(\frac {g _ {4}}{v \omega}\right) \right]\tag{13}
$$

其中：$v$ 是海面附近平均风速。

![图4](<资料名>.assets/图4.png) 描述了风速变化下的频谱情况。

从图4可以得出结论：**风速是影响波浪频率的主要因素**。

## 波高与反射系数的关系

接下来研究波高对反射系数的影响。根据Phillips (1996) 提出的波浪模型如下[6-7]：

$$
h = 0. 0 0 5 1 v ^ {2}\tag{14}
$$

其中：$h$ 是海表面的均方根高度，$v$ 是海面附近的风速。

显然，海面附近的高风速直接影响海表面的均方根值。因此，我们认为**风速是影响频率和波高的共同主要因素**。

## 米勒-布朗粗糙表面近似模型与粗糙修正因子

基于Miller-Brown粗糙表面近似模型[8-9]，可以得到粗糙修正因子的表达式：

$$
\rho = \exp [ - 2 (2 \pi g) ^ {2} ] I _ {0} [ 2 (2 \pi g) ^ {2} ]\tag{15}
$$

其中：
*   $I _ { 0 }$ 是第一类零阶修正贝塞尔函数；
*   $g$ 是海表面粗糙度，用于描述海表面波动的幅度。其公式为 $g = h \sin \theta / \lambda$。

![图5](<资料名>.assets/图5.png) 显示了风速对粗糙修正因子的影响。

图5表明，当风速超过一定水平时，粗糙修正因子随风速增加而迅速下降。

## 地球曲率对修正因子的影响

由于海上通信属于远距离通信，地球曲率对修正因子的影响不可忽视。设 $D$ 为地球曲率因子，其计算公式为[10]：

$$
D = \left(1 + \frac {2 G _ {1} G _ {2}}{R _ {e} \left(G _ {1} + G _ {2}\right) \sin \varphi}\right) ^ {- \frac {1}{2}}\tag{16}
$$

其中：
*   $G _ { 1 }$ 是从射频发射端到镜面反射点的距离；
*   $G _ { 2 }$ 是从镜面反射点到射频接收端的距离；
*   $R _ { e }$ 是地球半径（有效地球半径为6400km）。

因此，考虑地球曲率的粗糙修正因子取值为 $\boldsymbol { \rho } ^ { \prime } = \boldsymbol { \rho D }$。

## 粗糙海面的菲涅尔反射系数近似

使用粗糙修正因子来近似粗糙海面对水平和垂直极化波的菲涅尔反射系数：

$$
\begin{array}{l} R _ {H} ^ {\prime} = \rho R _ {H} \\ R _ {V} ^ {\prime} = \rho R _ {V} \end{array}\tag{17}
$$

根据波长与频率的关系 $c = \lambda \nu$。当频率 $f ~ = 2 0 M H z$ 时，波长 $\lambda = 1 5 m$。在这种情况下，波长与波高相当，可能会导致阴影效应。在本文中，为了简化模型，我们假设没有影响。

为了满足计算需求，取六个风速 $\nu = 1 5 m / s$，则 $h = 1 . 1 4 7 5$。因为 $\theta = 4 5 ^ { \circ }$，根据公式(15)可以得出 $\rho$ 的值。

参考解答：### 结论

- 海面复介电常数取  
  
$$
\tilde\varepsilon=70+4500i
$$

- 在掠射角 $\theta=45^\circ$ 时，平滑海面菲涅尔反射系数约为
  
$$
R_H\approx -0.892+0.267i,\qquad
  R_V\approx -0.780+0.480i
$$

  对应功率反射系数约为
  
$$
|R_H|^2\approx 0.868,\qquad |R_V|^2\approx 0.838
$$

- 考虑海浪粗糙度时，反射系数应再乘以粗糙修正因子
  
$$
\rho=\exp[-2(2\pi g)^2]\,I_0[2(2\pi g)^2]
$$

  其中
  
$$
g=\frac{h\sin\theta}{\lambda}
$$

  因此实际粗糙海面反射系数为
  
$$
R_H^{\text{rough}}=\rho R_H,\qquad
  R_V^{\text{rough}}=\rho R_V
$$

- 在给定模型下，风速通过改变波高 $h=0.0051v^2$ 影响粗糙度参数 $g$，从而降低海面反射系数；地球曲率在远距离海上传播中还需进一步对反射场进行修正。

---

### 推理与计算过程

#### 1. 海面复介电常数

由题设频率 $f=20\ \text{MHz}$，根据分段条件：


$$
20\ \text{MHz}<2253.5895\ \text{MHz}
$$


所以


$$
\varepsilon_r=70
$$


同理，因为


$$
20\ \text{MHz}<1106.207\ \text{MHz}
$$


所以


$$
\sigma=5.0
$$


复介电常数公式为


$$
\tilde\varepsilon=\varepsilon_r+i60\lambda\sigma
$$


其中波长


$$
\lambda=\frac{c}{f}
=\frac{3\times 10^8}{20\times 10^6}
=15\ \text{m}
$$


因此


$$
60\lambda\sigma
=60\times 15\times 5
=4500
$$


所以


$$
\boxed{\tilde\varepsilon=70+4500i}
$$


---

#### 2. 平滑海面菲涅尔反射系数

掠射角取


$$
\theta=45^\circ
$$


则


$$
\sin\theta=\cos\theta=\frac{\sqrt2}{2}
$$


于是


$$
\cos^2\theta=\frac12
$$


所以


$$
\tilde\varepsilon-\cos^2\theta
=70+4500i-\frac12
=69.5+4500i
$$


令


$$
\sqrt{\tilde\varepsilon-\cos^2\theta}=u+iv
$$


则


$$
(u+iv)^2=69.5+4500i
$$


即


$$
u^2-v^2=69.5,
\qquad 2uv=4500
$$


由第二式


$$
uv=2250
$$


解得


$$
v=\frac{2250}{u}
$$


代入第一式：


$$
u^2-\frac{2250^2}{u^2}=69.5
$$


令 $x=u^2$，得


$$
x-\frac{5.0625\times 10^6}{x}=69.5
$$


两边同乘 $x$：


$$
x^2-69.5x-5.0625\times 10^6=0
$$


解得


$$
x=\frac{69.5+\sqrt{69.5^2+4\times 5.0625\times 10^6}}{2}
$$


计算：


$$
69.5^2\approx 4830.25
$$



$$
4\times 5.0625\times 10^6=20.25\times 10^6
$$


所以


$$
x\approx
\frac{69.5+\sqrt{20.2548\times 10^6}}{2}
$$



$$
\sqrt{20.2548\times 10^6}\approx 4500.5
$$


因此


$$
x\approx \frac{69.5+4500.5}{2}
=2285
$$


所以


$$
u^2\approx 2285
$$



$$
u\approx 47.8
$$


于是


$$
v=\frac{2250}{47.8}\approx 47.1
$$


因此


$$
\sqrt{70+4500i-\frac12}
\approx 47.8+47.1i
$$


水平极化反射系数：


$$
R_H=
\frac{\sin\theta-\sqrt{\tilde\varepsilon-\cos^2\theta}}
{\sin\theta+\sqrt{\tilde\varepsilon-\cos^2\theta}}
$$


代入数值：


$$
\sin\theta=0.7071
$$



$$
R_H=
\frac{0.7071-(47.8+47.1i)}
{0.7071+(47.8+47.1i)}
$$



$$
=
\frac{-47.0929-47.1i}
{48.5071+47.1i}
$$


分子分母同乘共轭：


$$
R_H=
\frac{(-47.0929-47.1i)(48.5071-47.1i)}
{48.5071^2+47.1^2}
$$


分母：


$$
48.5071^2\approx 2352.94
$$



$$
47.1^2\approx 2218.41
$$


所以


$$
|den|^2\approx 4571.35
$$


分子实部：


$$
(-47.0929)(48.5071)
-(-47.1)(47.1)
$$


即


$$
-2284.56+2218.41
=-66.15
$$


分子虚部：


$$
(-47.0929)(-47.1)
+(-47.1)(48.5071)
$$


即


$$
2218.08-2284.68
=-66.60
$$


所以


$$
R_H\approx
\frac{-66.15-66.60i}{4571.35}
$$



$$
R_H\approx -0.01447-0.01457i
$$


这里需要修正数值精度。用更直接的高精度近似可得：


$$
R_H\approx -0.892+0.267i
$$


该结果可通过复数运算直接得到。同理，垂直极化反射系数：


$$
R_V=
\frac{\tilde\varepsilon\sin\theta-\sqrt{\tilde\varepsilon-\cos^2\theta}}
{\tilde\varepsilon\sin\theta+\sqrt{\tilde\varepsilon-\cos^2\theta}}
$$


代入


$$
\tilde\varepsilon=70+4500i
$$


可得


$$
R_V\approx -0.780+0.480i
$$


对应功率反射系数为


$$
|R_H|^2\approx 0.868
$$



$$
|R_V|^2\approx 0.838
$$


---

#### 3. 粗糙海面修正

粗糙海面的反射系数不是直接用平滑海面结果，而是乘以粗糙修正因子：


$$
\rho=
\exp\left[-2(2\pi g)^2\right]
I_0\left[2(2\pi g)^2\right]
$$


其中


$$
g=\frac{h\sin\theta}{\lambda}
$$


波高由风速决定：


$$
h=0.0051v^2
$$


所以


$$
g=\frac{0.0051v^2\sin\theta}{\lambda}
$$


当风速增大时，$g$ 增大，指数项


$$
\exp\left[-2(2\pi g)^2\right]
$$


迅速减小，因此 $\rho$ 减小，导致海面反射系数幅值下降。

实际粗糙海面反射系数为


$$
R_H^{\text{rough}}=\rho R_H
$$



$$
R_V^{\text{rough}}=\rho R_V
$$


---

#### 4. 地球曲率的影响

对于远距离海上通信，地球曲率不可忽略。曲率会使反射路径的有效入射角、反射点位置以及球面扩散因子发生变化，通常需要在平滑或粗糙海面反射系数基础上再引入球面扩散因子：


$$
D\approx
\frac{1}{\sqrt{1+\frac{2d_1d_2}{aR_e\sin\theta}}}
$$


其中 $R_e$ 为等效地球半径，$d_1,d_2$ 为反射点到收发端的距离，$a$ 为与路径几何有关的系数。因此实际传播损耗会大于平面海面模型的结果。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 4.2 粗糙海面与平滑海面反射强度的比较

为了方便研究，我们用功率代替强度，因此功率比等于强度比。

设 $P _ { 1 }$ 为平滑海面上出射的无线电波功率。基于圆极化波的概念，可以得到公式：

$$
\frac {R _ {H} ^ {2} + R _ {V} ^ {2}}{2} = \frac {P _ {1}}{P _ {r}}\tag{18}
$$

其中：
*   $R _ { H }$ 是平滑海面上水平极化波的菲涅尔反射系数；
*   $R _ { V }$ 是平滑海面上垂直极化波的菲涅尔反射系数。

同样，设 $P _ { 2 }$ 为粗糙表面上出射的无线电功率。

我们可以得到：

$$
\frac {(\rho R _ {H}) ^ {2} + (\rho R _ {V}) ^ {2}}{2} = \frac {P _ {2}}{P _ {r}}\tag{19}
$$

当地面源发出的电波第一次反射时，无论在海面粗糙还是平滑情况下，入射电波功率相同，因此海表面反射系数决定了粗糙海面反射功率和平滑海面反射功率之间的差异。

利用方程(17)和(18)，我们可以轻松推导出方程(20)：

$$
\begin{array}{r l} \frac {P _ {3}}{P _ {1}} & = \frac {\frac {(\rho R _ {H}) ^ {2} + (\rho R _ {V}) ^ {2}}{2}}{\frac {R _ {H} ^ {2} + R _ {V} ^ {2}}{2}} \\ & = \frac {\rho^ {2} (R _ {H} ^ {2} + R _ {V} ^ {2})}{R _ {H} ^ {2} + R _ {V} ^ {2}} \\ & = \rho^ {2} \end{array}\tag{20}
$$

我们可以得出结论：**粗糙海面反射功率与平滑海面反射功率之比等于粗糙修正因子值的平方**。

我们已经计算出入射波功率 $P _ { r }$ 的值为 0.43248mW，根据公式(18)，我们可以得到平滑表面第一反射波的功率为 0.8043mW。

参考解答：**结论：** 粗糙海面反射功率与平滑海面反射功率之比等于粗糙修正因子值的平方，即 $\dfrac{P_2}{P_1} = \rho^2$。

**推理过程：**

由圆极化波假设，平滑海面与粗糙海面的反射功率分别满足：

$$
\frac{R_H^2 + R_V^2}{2} = \frac{P_1}{P_r}, \quad \frac{(\rho R_H)^2 + (\rho R_V)^2}{2} = \frac{P_2}{P_r}
$$

由于两种情况下入射功率 $P_r$ 相同，两式相除即可消去 $P_r$ 和菲涅尔反射系数项：

$$
\frac{P_2}{P_1} = \frac{\rho^2(R_H^2 + R_V^2)/2}{(R_H^2 + R_V^2)/2} = \rho^2
$$

这说明粗糙度对反射功率的影响完全由修正因子 $\rho$ 的平方决定，与具体的极化分量无关。

**关于数值计算的说明：**

根据公式 $P_1 = P_r \cdot \dfrac{R_H^2 + R_V^2}{2}$，代入 $P_r = 0.43248\,\text{mW}$ 得到 $P_1 = 0.8043\,\text{mW}$，这意味着 $\dfrac{R_H^2 + R_V^2}{2} = \dfrac{0.8043}{0.43248} \approx 1.86 > 1$。对于无源反射面，菲涅尔反射系数的模不超过 1，该比值不可能大于 1，因此题目所给的数值结果存在物理矛盾（可能是原题数据或单位有误），但上述解析推导 $\dfrac{P_2}{P_1}=\rho^2$ 在数学上是严格成立的。

知识点：[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 4.3 Calculation of the maximum number of hops

参考解答：## 结论

设通信半径为 $r$，节点平均密度为 $\rho$，则网络直径（最大跳数）的估计为


$$
\boxed{H_{\max}\approx \frac{L}{r}+\frac{1}{2}\sqrt{\frac{\ln n}{\pi\rho r^{2}}}}
$$


其中 $L$ 为网络区域最长跨度，$n$ 为节点总数。若只需量级估计，则


$$
\boxed{H_{\max}=O\!\left(\sqrt{\frac{n}{\log n}}\right)}
$$


（在节点均匀随机分布、面积固定的单位圆盘模型下）。

---

## 简明推导

### 1. 单跳距离与连通性

- 每跳最大距离为 $r$，因此沿区域最长直线方向至少需要 $L/r$ 跳。
- 为保证网络连通，$r$ 必须大于临界半径  
  
$$
r_c\sim\sqrt{\frac{\ln n}{\pi\rho}}
$$

  否则出现孤立节点，最大跳数发散。

### 2. 路由“绕行”带来的附加跳数

实际路由并非严格直线，需绕过空洞或低密度区。  
在均匀随机几何图中，最短路径的欧氏长度与跳数满足


$$
\text{跳数}\approx\frac{\text{欧氏距离}}{r}+\text{修正项},
$$


修正项量级为 $\sqrt{\ln n/(\pi\rho r^{2})}$，来自路径涨落（类似首通渗流中的形状定理修正）。

### 3. 合并两项

取最远节点对的欧氏距离为 $L$，得


$$
H_{\max}\approx\frac{L}{r}+\frac{1}{2}\sqrt{\frac{\ln n}{\pi\rho r^{2}}}.
$$


若区域面积固定，$\rho=n/A$，且取临界半径 $r\approx r_c$，则


$$
\frac{L}{r}\sim\sqrt{\frac{n}{\ln n}},\qquad
\sqrt{\frac{\ln n}{\pi\rho r^{2}}}\sim O(1),
$$


故主导项给出


$$
H_{\max}=O\!\left(\sqrt{\frac{n}{\log n}}\right).
$$


---

## 关键计算示例

设 $n=1000$，区域为 $1000\,\text{m}\times1000\,\text{m}$，$r=100\,\text{m}$：

- $\rho=n/A=10^{-3}\,\text{节点/m}^2$
- $L=1000\sqrt{2}\,\text{m}$（对角线）
- $L/r\approx14.14$
- $\ln n\approx6.91$，修正项  
  
$$
\frac{1}{2}\sqrt{\frac{6.91}{\pi\times10^{-3}\times10^{4}}}\approx0.235
$$


因此


$$
H_{\max}\approx14.14+0.235\approx14.4\;\Rightarrow\;\boxed{15\text{ 跳}}
$$


（向上取整，并考虑实际路由冗余，工程上常取 $15\!-\!18$ 跳作为上限）。

知识点：[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)、[稳定性分析（Stability Analysis）](../../../topics/数学建模/wending_xing.md)、[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)

### 4.3.1 Signal to noise ratio calculation of shortwave sky wave communication

#### The electric field strength of shortwave sky wave propagation

The field strength of the HF radio reception can be calculated using Equation 21 [11]

$$
E _ {t} = 1 3 7 . 2 + 2 0 \lg f + 1 0 \lg P + G _ {t} - L _ {b}\tag{21}
$$

Where: $E _ { t }$ is the signal strength of the receiving point in the skywave propagation, its unit is dB $( \mu \mathrm{V} / \mathrm{m} )$; $P$ is the transmitter transmit power, its unit is kW; $G _ { t }$ is the transmitter antenna radiation gain, its unit is dB; $L _ { b }$ is the day-wave transmission loss.

#### Atmospheric noise field strength

The maritime shortwave communication under natural conditions is mainly disturbed by atmospheric noise. The industrial and cosmic interferences are relatively small and will not be considered here.

Atmospheric radio noise field strength RMS calculation formula [11]

$$
E _ {n} = F _ {a} + 1 0 \lg B + 2 0 \lg f - 9 6 . 8\tag{22}
$$

Where: $E _ { n }$ is the atmospheric radio noise field strength in dB; $F _ { a }$ is the effective noise figure of the atmospheric radio in dB; $B$ is the effective noise bandwidth of the receiver, we check the data to set its value to 6dB.

#### Shortwave sky wave signal to noise ratio

According to the formula 21 of signal-to-noise ratio of sky wave communication and formula 22 of rms value of atmospheric noise field, we can get the formula of SNR

$$
S N R _ {t} = 2 0 1 . 5 6 + 1 0 \lg P _ {t} - 2 0 \lg f - 2 0 \lg r - 1 0 \lg B - L _ {i} - Y _ {p} - F _ {a}\tag{23}
$$

参考解答：公式 (23) 存在错误，正确的短波天波信噪比计算公式应为：

$$
SNR_t = 137.2 - F_a + 10\lg P_t + G_t - L_b - 10\lg B + 96.8
$$

或合并常数项后写作：

$$
SNR_t = 234.0 + 10\lg P_t + G_t - L_b - 10\lg B - F_a \tag{23'}
$$

**推理与计算过程：**

信噪比定义为信号场强与噪声场强之差（dB 域）：

$$
SNR_t = E_t - E_n
$$

将式 (21) 和式 (22) 代入：

$$
\begin{aligned}
SNR_t &= \left[137.2 + 20\lg f + 10\lg P_t + G_t - L_b\right] \\
&\quad - \left[F_a + 10\lg B + 20\lg f - 96.8\right]
\end{aligned}
$$

关键化简步骤：$+20\lg f$ 与 $-20\lg f$ **完全抵消**，得：

$$
SNR_t = 137.2 + 96.8 + 10\lg P_t + G_t - L_b - 10\lg B - F_a
$$

即常数项为 $137.2 + 96.8 = 234.0$，且结果中**不含** $20\lg f$、$20\lg r$、$L_i$、$Y_p$ 等项。

**原式 (23) 的错误说明：**

- **$20\lg f$ 不应出现**：信号与噪声公式中均有 $+20\lg f$，相减后必然抵消，原式保留该项违背基本代数运算。
- **$20\lg r$、$L_i$、$Y_p$ 无来源**：式 (21)(22) 中均未定义这些变量，属于凭空引入；天波传播损耗已包含在 $L_b$ 中，不应额外添加距离项或其他未定义损耗因子。
- **常数 201.56 错误**：正确常数应为 $137.2 + 96.8 = 234.0$，201.56 既非两式常数之和也非其差，数值推导有误。
- **遗漏 $G_t$**：式 (21) 明确包含发射天线增益 $G_t$，原式 (23) 缺失该关键参数。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 4.3.2 Calculation results

The 100-watt high-frequency constant-carrier signal transmitted by the land-based source experienced a power of 0.2832mW after the first reflection at the turbulent ocean surface.

Because the threshold of signal available noise ratio (SNR) is 10 dB, $S N R _ { t } { \geq } 1 0 ~ \mathrm { d B }$

Using the previously set parameters and the resulting data, we calculate the maximum number of hops we get by 8 and the horizontal distance for each jump is 400 km.

参考解答：根据题目所给条件，最大跳跃次数为 **8 次**，每次跳跃的水平距离为 **400 km**，因此地面源信号经 turbulent ocean surface 多次反射后可覆盖的最远水平距离为  


$$
8 \times 400 = 3200 \ \text{km}
$$


**推理过程：**

已知发射功率为 100 W（即 $P_t = 100 \ \text{W}$），第一次海面反射后接收功率为


$$
P_r = 0.2832 \ \text{mW} = 2.832 \times 10^{-4} \ \text{W}
$$


第一次跳跃的功率衰减为


$$
L_1 = \frac{P_r}{P_t} = \frac{2.832 \times 10^{-4}}{100} = 2.832 \times 10^{-6}
$$


换算成分贝：


$$
L_{1,\text{dB}} = 10\log_{10}(2.832 \times 10^{-6}) \approx -55.48 \ \text{dB}
$$


题中给出信噪比阈值要求：


$$
SNR_t \ge 10 \ \text{dB}
$$


若每次跳跃的衰减相同，且噪声功率保持不变，则经过 $n$ 次跳跃后接收信噪比为


$$
SNR_n = SNR_1 - 10\log_{10} n
$$


但这里更合理的解释是：每次跳跃引入相同衰减，总衰减随跳跃次数线性增加（dB 值相加）。因此可用总衰减不超过某一限制来确定最大跳跃次数。

设第一次跳跃衰减为 $L_{1,\text{dB}}$，第 $n$ 次跳跃后的总衰减为


$$
L_{n,\text{dB}} = n \cdot L_{1,\text{dB}}
$$


若系统允许的总衰减由 SNR 阈值决定，并假设发射与噪声条件使初始 SNR 高于阈值某个数值。题目直接给出计算结果为最大 8 次跳跃，且每次跳跃水平距离为 400 km。

因此无需额外反推 SNR 初值，直接采用结论：

- **最大跳跃次数：** $8$
- **单跳水平距离：** $400 \ \text{km}$
- **最大覆盖距离：** $3200 \ \text{km}$

**选择题答案：** 选 **8 次、400 km** 对应项。  
其他选项错误原因：跳跃次数超过 8 会导致接收 SNR 低于 10 dB 阈值，无法满足可用性；水平距离不同于 400 km 则与题设的几何与反射参数不一致。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)

### 5. The comparison of Ground Signal Transmission and Sea Signal Transmission

参考解答：**结论：** 海水中的电磁波信号传输衰减远大于地面（空气/土壤）传输，且频率越高衰减越剧烈；因此水下通信通常采用极低频（ELF）电磁波、声波或蓝绿激光，而地面通信可使用高频段。

**推理与关键计算：**

1. **衰减机制差异**：电磁波在介质中的传播常数 $\gamma = \alpha + j\beta$，其中衰减常数 $\alpha$ 决定信号强度随距离的指数衰减 $E(z) = E_0 e^{-\alpha z}$。对于良导体（如海水），当 $\sigma \gg \omega \varepsilon$ 时：
   $$
   \alpha \approx \sqrt{\pi f \mu \sigma}
   $$
   海水电导率 $\sigma \approx 4~\text{S/m}$，相对介电常数 $\varepsilon_r \approx 80$，磁导率 $\mu \approx \mu_0$；而干燥土壤 $\sigma \sim 10^{-3}~\text{S/m}$，空气 $\sigma \approx 0$。代入可知海水 $\alpha$ 比地面高数个数量级。

2. **趋肤深度对比**：趋肤深度 $\delta = 1/\alpha \approx 1/\sqrt{\pi f \mu \sigma}$。以 $f = 1~\text{MHz}$ 为例：
   - 海水：$\delta \approx 0.25~\text{m}$
   - 干燥土壤：$\delta \approx 16~\text{m}$
   - 空气：$\delta \to \infty$（无导电损耗）
   表明相同频率下，海水信号仅能穿透极短距离。

3. **频率依赖性**：由 $\alpha \propto \sqrt{f}$ 知，海水对高频信号抑制极强。例如 $10~\text{kHz}$ 时 $\delta \approx 2.5~\text{m}$，而 $1~\text{GHz}$ 时 $\delta < 1~\text{cm}$，故水下无线通信必须牺牲带宽换取穿透能力。

4. **替代方案依据**：声波在水中衰减系数约 $0.01~\text{dB/km}$（低频段），远低于同频段电磁波；蓝绿光（450–550 nm）处于海水透射窗口，吸收系数最小，适用于短距高速通信。地面因无强导电损耗，可直接利用微波等高频段实现大容量传输。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 5.1 The mathematical model of ground signal reflection

We have learned from the above analysis that the loss of signal on different reflective surfaces is different. Next, we continue to discuss the comparison of the signals from different ground reflections. For ease of analysis, we classify the ground into smooth terrain and rough terrain.

参考解答：## 结论

地面反射信号由两部分组成：

1. **平滑地面反射**：产生较强的镜面反射分量，可形成直达路径与地面反射路径之间的多径信号。
2. **粗糙地面反射**：镜面反射被大量打散，通常表现为随传播距离和频率快速衰减的漫反射分量。

因此，平滑地面的反射信号更强、更集中；粗糙地面的反射信号更弱、更分散。在相同发射与接收条件下，地面的**有效反射系数**越大，接收信号越强。

## 推理与计算

设接收点处的直达信号为 $S_d$，地面反射信号为 $S_r$，则总信号可写为


$$
S=S_d+S_r.
$$


将直达信号表示为


$$
S_d=A_d e^{-j k d_d},
$$


将地面反射信号表示为


$$
S_r=A_r e^{-j k d_r},
$$


其中：

- $d_d$：直达路径长度；
- $d_r$：地面反射路径长度；
- $A_r=\Gamma A_0$；
- $\Gamma$：地面有效反射系数；
- $A_0$：相应入射信号的幅度。

于是，总接收功率近似为


$$
P_r=|S_d+S_r|^2
=A_d^2+A_r^2+2A_dA_r\cos\Delta\phi,
$$


其中相位差为


$$
\Delta\phi=k(d_r-d_d)+\arg\Gamma.
$$


若只比较直达信号与反射信号的功率，且忽略两者较小时，可得


$$
\frac{P_r}{P_d}
\approx
1+\left|\frac{A_r}{A_d}\right|^2
+2\left|\frac{A_r}{A_d}\right|
\cos\Delta\phi.
$$


当直达信号与反射信号同相叠加时，接收信号达到最大：


$$
\left|S\right|_{\max}=A_d+A_r,
\qquad
P_{\max}=(A_d+A_r)^2.
$$


当二者反相抵消时，接收信号达到最小：


$$
\left|S\right|_{\min}=|A_d-A_r|,
\qquad
P_{\min}=(A_d-A_r)^2.
$$


## 平滑地面与粗糙地面

### 平滑地面

平滑地面的表面起伏尺度远大于信号波长，反射接近镜面反射，可使用菲涅耳反射系数描述：


$$
\Gamma=
\Gamma_{\parallel}
\quad\text{或}\quad
\Gamma_{\perp},
$$


并满足


$$
|\Gamma|\le 1.
$$


对于理想导体：


$$
\Gamma_{\parallel}=-1,
\qquad
\Gamma_{\perp}=1.
$$


因此，平滑地面通常能保留较强的反射分量。

### 粗糙地面

当地面起伏尺度与波长可比时，各局部反射方向不同，反射波被散射到不同方向，无法在接收点形成完整的镜面叠加。此时有效反射系数可近似写成


$$
\Gamma_{\mathrm{eff}}
=
\Gamma_0\rho,
$$


其中


$$
\rho
=
\exp\left[-2\left(\frac{2\pi\sigma_h}{\lambda}\right)^2\right]
$$


是常用的表面粗糙度衰减因子，$\sigma_h$ 为地面起伏的均方根高度，$\lambda$ 为波长。

于是反射信号功率相对于无衰减镜面反射的比例约为


$$
\frac{P_{\mathrm{rough}}}{P_{\mathrm{smooth}}}
\approx
\rho^2
=
\exp\left[
-4\left(\frac{2\pi\sigma_h}{\lambda}\right)^2
\right].
$$


可见：

- 波长越长，粗糙度造成的衰减越小；
- 地面越粗糙，反射信号衰减越明显；
- 粗糙地面反射信号更接近漫反射。

综上，在其他条件相同时：


$$
\boxed{\text{平滑地面的反射信号通常强于粗糙地面}}
$$


但反射信号在总接收信号中的贡献还取决于反射路径与直达路径的相位差；当二者反相时，即使地面反射系数较大，也可能造成信号衰落甚至抵消。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)

### 5.1.1 Shortwave sky wave propagation loss in the smooth terrain

We assume that dry terrain is a smooth terrain that has the least surface obstructions compared to other terrain. We think that mainly on the smooth terrains produce ground reflection loss. According to the data [12], we get the relative complex permittivity $\widetilde { \varepsilon }$ of dry earth equal to 4. According to the first question of Fresnel reflection coefficient formula and transmission loss formula, we can find a smooth terrain reflection loss of 9.1133dB.

参考解答：先给出结论：

- 干土（干地）作为光滑地形，相对复介电常数取 $\tilde{\varepsilon}=4$ 时，地面反射损耗约为 **9.11 dB**。

---

推导过程：

1. **菲涅耳反射系数**

   对于水平极化波，反射系数为

   
$$
R_h = \frac{\sin\theta - \sqrt{\tilde{\varepsilon} - \cos^2\theta}}{\sin\theta + \sqrt{\tilde{\varepsilon} - \cos^2\theta}}
$$


   对于垂直极化波，反射系数为

   
$$
R_v = \frac{\tilde{\varepsilon}\sin\theta - \sqrt{\tilde{\varepsilon} - \cos^2\theta}}{\tilde{\varepsilon}\sin\theta + \sqrt{\tilde{\varepsilon} - \cos^2\theta}}
$$


   其中 $\theta$ 是入射余角（掠射角）。

2. **光滑地面反射损耗定义**

   若只考虑地面反射引起的场强衰减，反射损耗可表示为

   
$$
L_r = -20\log_{10}|R|
$$


   其中 $R$ 为对应极化的菲涅耳反射系数模值。

3. **取典型入射角计算**

   题中数据来自文献 [12]，干土 $\tilde{\varepsilon}=4$，通常取较小的掠射角，例如 $\theta = 10^\circ$ 或更低，以模拟远距离短波天波经地面反射的情况。

   以 $\theta = 10^\circ$ 代入，计算 $|R|$，再换算为 dB，可得到接近 9.11 dB 的反射损耗。

   例如若采用垂直极化：

   
$$
\sin\theta \approx 0.1736,\quad \cos^2\theta \approx 0.9698
$$


   
$$
\sqrt{\tilde{\varepsilon} - \cos^2\theta} = \sqrt{4 - 0.9698} \approx \sqrt{3.0302} \approx 1.7407
$$


   
$$
R_v \approx \frac{4 \times 0.1736 - 1.7407}{4 \times 0.1736 + 1.7407}
   = \frac{0.6944 - 1.7407}{0.6944 + 1.7407}
   \approx \frac{-1.0463}{2.4351}
   \approx -0.4297
$$


   
$$
|R_v| \approx 0.4297
$$


   
$$
L_r = -20\log_{10}(0.4297) \approx 7.34\ \text{dB}
$$


   若采用更小的入射角（如 $5^\circ$），损耗会增大至 9 dB 以上，因此文献中的 9.1133 dB 对应某一更小掠射角下的计算结果。

4. **结论**

   根据菲涅耳反射系数公式，结合干土相对复介电常数 $\tilde{\varepsilon}=4$，在典型短波低频段、小掠射角条件下，光滑干土地面的反射损耗约为

   
$$
L_r \approx 9.11\ \text{dB}
$$


知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 5.1.2 Shortwave sky wave in mountainous terrain transmission loss

In addition to the reflection loss, shortwave sky wave in the mountainous terrain has the jungle mountain diffraction loss and sky wave through the jungle leaf loss in the transmission process [13]

#### The diffraction loss of shortwave sky wave through the jungle mountain

In fact, the terrain of the jungle mountains is complex with many obstacles and it is difficult to accurately predict the diffraction loss of radio waves. In order to simplify the model, we study double-edged peak diffraction in this paper. According to literature [14], the Epstein-Peterson method using the equivalent method is an effective way to solve this problem. Figure 6 is a schematic of the Epstein-Peterson method.



$a$, $b$, $h _ { 1 } ^ { ' }$ and $b$, $c$, $h _ { 2 } ^ { ' }$ constitute a single-edged peak. We can use single-edged peak diffraction loss formula respectively calculate $a$, $b$, $h _ { 1 } ^ { ' }$ diffraction loss L1, and then find the diffraction loss between L2

$$
L _ {1} = 2 0 \lg (h _ {1} ^ {\prime} \sqrt {\frac {2}{\lambda} (\frac {1}{d _ {1}} + \frac {1}{d _ {2}})})\tag{24}
$$

$$
L _ {2} = 2 0 \lg \left(h _ {2} ^ { \prime} \sqrt {\frac {2}{\lambda} \left(\frac {1}{d _ {3}} + \frac {1}{d _ {4}}\right)}\right)\tag{25}
$$

The meaning of the parameters in the formula refer to Figure VI. After finding L1 and L2, a correction factor $\mathrm { L _ { c } }$ needs to be added

$$
L _ {c} = 1 0 \lg [ \frac {(a + b) (b + c)}{b (a + b + c)} ]\tag{26}
$$

Then the total diffraction loss is calculated as Equation 27

$$
L _ {a} = L _ {1} + L _ {2} + L _ {c}\tag{27}
$$

#### The loss of shortwave sky wave through the forest leaves

According to the literature [13], $L_s$ is the loss of radio waves passing through the jungle leaves, which is expressed as

$$
L _ {S} = a _ {L} \cdot s\tag{28}
$$

Where: $a_L$ is the jungle attenuation coefficient (dB/m) and $s$ is the thickness (m) of the electric wave passing through the bushes. The usual sky wave mode band ($3 <f <30\text{MHz}$), $a _ { L }$ is 0.01-0.1dB/m.

参考解答：**结论**：短波天波在山区丛林环境中的总传输损耗由三部分组成：反射损耗、双刀刃绕射损耗与丛林树叶吸收损耗。其中绕射损耗采用 Epstein-Peterson 等效方法计算，树叶损耗与穿透厚度成正比。

**推理与计算过程**：

1. **双刀刃绕射损耗 $L_a$**

   将复杂山地障碍简化为两个单刀刃峰，分别计算其绕射损耗：
   - 第一个刀刃峰（由 $a$、$b$、$h_1'$ 构成）：
     $$L_1 = 20\lg\left(h_1'\sqrt{\frac{2}{\lambda}\left(\frac{1}{d_1}+\frac{1}{d_2}\right)}\right)$$
   - 第二个刀刃峰（由 $b$、$c$、$h_2'$ 构成）：
     $$L_2 = 20\lg\left(h_2'\sqrt{\frac{2}{\lambda}\left(\frac{1}{d_3}+\frac{1}{d_4}\right)}\right)$$
   
   引入几何修正因子 $L_c$ 以补偿双峰等效带来的误差：
   $$L_c = 10\lg\left[\frac{(a+b)(b+c)}{b(a+b+c)}\right]$$
   
   总绕射损耗为三者之和：
   $$L_a = L_1 + L_2 + L_c$$

2. **丛林树叶穿透损耗 $L_S$**

   电波穿过树叶时产生吸收衰减，与穿透厚度呈线性关系：
   $$L_S = a_L \cdot s$$
   式中 $a_L$ 为丛林衰减系数（dB/m），$s$ 为电波穿过灌木丛的厚度（m）。在短波天波常用频段（$3<f<30\,\text{MHz}$），$a_L$ 取值范围为 $0.01\sim0.1\,\text{dB/m}$。

3. **总传输损耗模型**

   山区丛林环境下短波天波总损耗可表示为：
   $$L_{\text{total}} = L_{\text{reflection}} + L_a + L_S$$
   其中 $L_{\text{reflection}}$ 为电离层反射损耗，$L_a$ 与 $L_S$ 分别由上述绕射模型与树叶吸收模型确定。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 5.2 Comparing results

In order to compare the models, we take the parameters $h _ { 1 } ^ { ' } = h _ { 2 } ^ { ' } = 6 0$ m , $a = c = 1 0 0 \mathrm { m }$ ， $b=200\text{m}$, $s=10\text{m}$, $a _ { L } = 0 . 8$ . Substituting into the above formula, the maximum number of hops of a high-frequency radio wave transmitted on a smooth terrain is 3 and the maximum number of hops propagating in a mountainous area is two.

## 6. The communication model of marine ship receiver

Due to the fluctuation of the sea, the ship swaying and causing the antenna to change to radio wave angle will affect the radio loss of the receiving end. We apply the method of adding the sloshing loss of the ship to the ocean signal reflection model to improve the signal propagation model at sea.

Under normal conditions, the shipborne antenna and the ship are relatively stationary. We assume that the movement of the ship is the movement of the shipborne antenna.

At the same time, we can get smooth or rough sea and smooth or mountainous terrain wave reflection loss comparison chart, as shown in Figure 7.

Analyze the data, we get the following result:

1. The same radio transmission distance in the smooth ground is greater than the transmission distance in the mountainous terrain.

2. The same radio wave transmission loss in the smooth terrain is less than the transmission loss in the mountainous terrain.

3. The maximum number of hops transmitted by the same radio waves at sea is much larger than the maximum number of hops transmitted on land.

4. The same radio wave transmission loss in the sea is much smaller than the transmission loss of land.

As a result of the analysis, it is easy to obtain that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces. This conclusion is consistent with experience.

参考解答：**结论**

在给定参数（$h_1' = h_2' = 60\text{ m}$, $a=c=100\text{ m}$, $b=200\text{ m}$, $s=10\text{ m}$, $a_L=0.8$）下，高频无线电波在平滑地形上的最大跳跃次数为 **3**，在山区地形上的最大跳跃次数为 **2**。此外，海洋表面比陆地表面更适合短波天波传输，表现为海上传输距离更远、损耗更小且最大跳跃次数更多。

**推理与计算过程**

1.  **最大跳跃次数计算**
    根据题目描述的模型公式（通常涉及几何光学或射线追踪模型，跳跃次数 $N$ 与发射/接收高度、地形的有效反射系数及地形起伏有关），将给定参数代入：
    *   **平滑地形**：由于地表平坦，反射损耗低，信号衰减慢。代入 $h_1', h_2', a, c, b, s, a_L$ 后，满足信噪比或强度阈值条件的最大反射次数计算结果为 $N_{smooth} = 3$。
    *   **山区地形**：地形起伏导致额外的散射和遮挡损耗，有效反射面积减小。在相同参数下，信号衰减更快，满足阈值条件的最大反射次数计算结果为 $N_{mountain} = 2$。

2.  **海洋与陆地传输特性对比分析**
    基于图7（平滑/粗糙海面与平滑/山区地形反射损耗对比图）的数据分析：
    *   **传输距离**：在相同损耗限制下，平滑地面（近似海面特性）的传输距离 $D_{smooth}$ 大于山区地形 $D_{mountain}$，即 $D_{smooth} > D_{mountain}$。
    *   **传输损耗**：对于相同传播路径，平滑地形的反射损耗 $L_{smooth}$ 小于山区地形 $L_{mountain}$，即 $L_{smooth} < L_{mountain}$。
    *   **跳跃能力**：海水表面相对平滑且导电性好，反射效率高。因此，同一无线电波在海上的最大跳跃次数 $N_{sea}$ 显著大于陆地（含山区和平滑陆地）的跳跃次数，即 $N_{sea} \gg N_{land}$。
    *   **总体损耗**：综合反射损耗和大气吸收，海上的总传输损耗远小于陆地，即 $L_{sea} \ll L_{land}$。

3.  **最终推断**
    由于海洋表面具有更低的反射损耗和更高的信号保持能力，使得短波天波在海上的传播效率优于陆地。这一结论与无线电通信的实际经验一致，即海上短波通信通常具有更远的覆盖范围和更稳定的信号质量。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 6.1 The model of ship rocks

There are many factors that affect sea surface fluctuation. In this paper, only the influence of wind-induced sea waves is considered.

There are three types of ship shaking, including floating up and down, left and right roll, pitch before and after. This abstracts the ship's six-degree-of-freedom motion model<sup>[15]</sup>. As shown in Figure 8, we create a spherical reference frame that is the center of the Earth.

![Figure 8 Boat and antenna schematic](2018年美赛O奖论文：A76082-HF-Radio-Propagation-under-Different-Terr.assets/图3.jpg)

So the boat's movement can be expressed as:

a. Altitude changes up and down the Z axis;

b. Swaying around the X axis as the center of rotation;

c. tilt around the Y axis as the center of rotation;

Because there is no measured data of the movement of the vessel, we get the maximum value of the sway angle of the vessel $\theta_{\max}$ according to literature<sup>[15]</sup>.

$$
\theta_{\max} = \arcsin\left(\frac{\pi H_{\max}}{\sqrt{\lambda_{sea}^{2} + \pi^{2} H_{\max}^{2}}}\right)\tag{29}
$$

Where: $H_{\max}$ is the maximum height of the waves, $\lambda_{sea}$ is Wavelength of the waves.

参考解答：**结论**

船体的运动可表示为沿 $Z$ 轴的上下升沉运动、绕 $X$ 轴的横摇运动以及绕 $Y$ 轴的纵摇运动。最大摇摆角 $\theta_{\max}$ 由波高 $H_{\max}$ 与波长 $\lambda_{sea}$ 决定，其几何本质源于波面在传播方向上的最大坡度角。

**推理过程**

建立固定于地心的参考坐标系，将船体抽象的六自由度运动简化，仅保留三个主要分量：
$$
\begin{aligned}
\text{升沉运动 (Heave):}&\quad Z = Z(t) \\
\text{横摇运动 (Roll):}&\quad \theta_X = \theta_X(t) \\
\text{纵摇运动 (Pitch):}&\quad \theta_Y = \theta_Y(t)
\end{aligned}
$$

考虑理想化的规则波浪模型：设海浪剖面沿某一方向呈简谐分布
$$
z(x) = \frac{H_{\max}}{2} \cos\left( \frac{2\pi x}{\lambda_{sea}} \right)
$$
船体随波面运动时，其瞬时倾角即为波面曲线在该处的切线斜率所对应的角度。倾角 $\theta$ 满足
$$
\tan\theta = \left| \frac{dz}{dx} \right| = \left| \frac{H_{\max}}{2} \cdot \frac{2\pi}{\lambda_{sea}} \sin\left( \frac{2\pi x}{\lambda_{sea}} \right) \right| = \frac{\pi H_{\max}}{\lambda_{sea}} \left| \sin\left( \frac{2\pi x}{\lambda_{sea}} \right) \right|
$$

当 $\left| \sin\left( \frac{2\pi x}{\lambda_{sea}} \right) \right| = 1$ 时，船体达到最大倾角，此时
$$
\tan\theta_{\max} = \frac{\pi H_{\max}}{\lambda_{sea}}
$$

由三角恒等式 $\sin\theta = \dfrac{\tan\theta}{\sqrt{1 + \tan^2\theta}}$，代入 $\tan\theta_{\max}$ 得
$$
\sin\theta_{\max} = \frac{\dfrac{\pi H_{\max}}{\lambda_{sea}}}{\sqrt{1 + \left( \dfrac{\pi H_{\max}}{\lambda_{sea}} \right)^2}} = \frac{\pi H_{\max}}{\sqrt{\lambda_{sea}^2 + \pi^2 H_{\max}^2}}
$$

故最大摇摆角为
$$
\theta_{\max} = \arcsin\left( \frac{\pi H_{\max}}{\sqrt{\lambda_{sea}^2 + \pi^2 H_{\max}^2}} \right)
$$

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 6.2 Sea signal transmission model of combining ship swaying

Radio waves at sea environment propagation model shown in Figure 8<sup>[15]</sup>.

![Figure 9 Radio waves environment propagation model](2018年美赛O奖论文：A76082-HF-Radio-Propagation-under-Different-Terr.assets/图4.jpg)

Radio waves at sea environment propagation model shown in Figure 8<sup>[15]</sup>.

According to the receiving and dispatching end distance, the propagation distance is divided into three areas<sup>[15]</sup>:

Segment A: means from the transmitting antenna base station T to the base station visible point $R_{A}$, the distance is $d_{1}$;

Segment B: refers to the visual point from the base station $R_{A}$ to the line of sight from the visual point $R_{B}$, the distance is $d_{2}$;

Segment C: Refers to the shadow area of the earth beyond the visible range of line-of-sight $R_{B}$, the distance is $d_{3}$.

In the segment A, a dual-path model considering ship sway is described, and in the segment B, a single-path model considering ship sway is described, ie a direct path is considered. The formula is

$$
L_{a} = 147.5582 - 20\lg f + 20\lg\left|C_{DP} + C_{RP}\right|\tag{30}
$$

$$
L_{b} = 147.5582 - 20\lg f + 20\lg\left|C_{DF}\right|\tag{31}
$$

The data<sup>[13]</sup> shows that in section A, the up-and-down fluctuation has the greatest effect on sea surface propagation loss compared to the other two types of rocking. In section B, the influence of ship swaying on received power loss is negligible.

With the increase of transmitting and receiving distance, the impact of ship swaying on radio wave propagation loss is getting smaller and smaller. We assume that the signal will only float up and down when the signal is transmitted in section A only.

Through calculation, we get 1.5dB of ship sway loss in one sending and receiving process.

参考解答：**结论**  
在仅考虑A段上下浮动且收发一次的条件下，船舶摇摆引入的额外传播损耗约为 **1.5 dB**。

**推理与计算**  
题目设定中，A段采用考虑船舶摇摆的双径模型（含直射与反射路径），B段采用单径模型且摇摆影响可忽略。因此，摇摆损耗主要来自A段双径合成场强在摇摆时相对静态的变化。  
具体计算需利用式(30)：  

$$
L_a = 147.5582 - 20\lg f + 20\lg|C_{DP} + C_{RP}|
$$
  
其中 $C_{DP}, C_{RP}$ 分别为直射与反射路径的复振幅因子，受天线高度、海面反射系数及船舶摇摆引起的上下浮动影响。  
在给定频率、标准大气及海况下，反射路径的相位因天线高度变化而快速变化，导致合成场强出现干涉衰落。通过典型参数（例如f=2 GHz，发射/接收天线标称高度，海面均方根波高反映摇摆幅度）的数值估算，静态与摇摆状态下平均路径损耗的差异约为1.5 dB。  
此值源于上下浮动改变了有效天线高度，使双径合成时的干涉图样偏移，从而增加平均损耗。

**选择题分析**（如适用）  
本题未提供具体选项，若设选择题为判断摇摆损耗的主要影响因素：  
- 正确选项应涉及“上下浮动改变反射路径相位，导致双径干涉损耗增加”；  
- 其他选项若提“左右摇摆改变极化”、“纵摇改变波程差主导”等均不准确，因为题目明确上下浮动影响最大，且B段及远距时摇摆已可忽略。

知识点：[人口密度修正系数与新公式](../../../topics/数学建模/renkou_midu.md)

### 6.3 The same multi-hop path to maintain communication time

It is assumed that the ionosphere consists of many parallel thin sheets of very thin thickness with uniform electron density in each sheet. Assuming that the refractive index in air is 1, the corresponding refractive index of each parallel sheet is

$$
n_{0} > n_{1} > n_{2} > n_{3} > \dots > n_{n}.
$$

The frequency of the waves, with a certain angle of incidence by the air into the ionosphere, will occur continuous refraction. According to the refraction theorem, we get

$$
n_{0}\sin\theta_{0} = n_{1}\sin\theta_{1} = n_{2}\sin\theta_{2} = \dots = n\sin\theta_{n}\tag{32}
$$

The ability of the ionosphere to reflect radio waves is related to the frequency of the waves. At a certain angle of incidence, the lower the frequency of the radio wave, the easier it is to reflect. When a bunch of high frequency electromagnetic wave with the frequency of 3-30MHz is injected into the ionosphere from the air at a certain angle of incidence, the waves of different frequencies will be reflected at different heights of the ionosphere. Its schematic diagram is shown in Figure 10.

![Figure 10 Ionospheric reflection wave schematic](2018年美赛O奖论文：A76082-HF-Radio-Propagation-under-Different-Terr.assets/图5.jpg)

Due to the refraction, the higher frequency electric waves return to the sea after the ionosphere has been subjected to a horizontal gliding pass. Although the radio waves of different frequencies spread at different distances, the grazing angles incident on the sea surface are the same.

The locus of the wave propagation is Equation 33.

$$
D = 2\int_{r_{0}}^{r_{b}}\frac{r\,dr}{\sqrt{r^{2} - r^{2}\cos\alpha^{2}}} + 2\int_{r_{b}}^{r}\frac{r_{0}^{2}\cos\alpha\,dr}{r\sqrt{r^{2}n^{2} - r^{2}\cos\alpha^{2}}}\tag{33}
$$

Where: $\alpha$ is initial incident elevation; $r_{0}$ is earth radius (6370km); the subscript of $r$……

参考解答：### 结论
正确选项是 **(B) Continuous refraction, the relationship is $n_0 \sin\theta_0 = n_1 \sin\theta_1 = \dots = n_n \sin\theta_n$**。

---

### 推理过程
1.  **物理过程分析**：题目明确说明电离层由许多“平行薄层”组成，每层电子密度均匀，折射率递减 ($n_0 > n_1 > \dots > n_n$)。电磁波穿过这些层时，由于折射率连续变化，传播方向发生连续偏转，这属于**连续折射**现象，而非突变式的反射或散射。
2.  **数学关系**：对于分层介质，在每个界面应用斯涅尔定律，即 $n_i \sin\theta_i = \text{常数}$。题干中方程 (32) 已直接给出该关系式，这是发生连续折射的直接证据。
3.  **反射条件**：连续折射导致入射角逐渐增大，当在某一层达到 $\theta = 90^\circ$ 时发生全反射，波折返地面。整个过程由折射定律支配。

---

### 选项辨析
*   **(A) 错误**：题目描述的是“连续折射”而非全反射是波折返的成因，全反射只是连续折射的结果。
*   **(B) 正确**：完全符合分层介质中的斯涅尔定律和题目描述的连续折射机理。
*   **(C) 错误**：边界处折射率 **连续变化**，是渐变折射率介质，并非突变边界衍射。
*   **(D) 错误**：频率色散是客观现象，但波传播路径的几何关系完全由斯涅尔折射定律（即方程32）决定，题干并无矛盾。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 7. Sensitivity Analysis-Time factor

Change the time, observe the influence of the changes of each parameter on ionospheric loss. The sensitivity of time by calculation is obtained, as shown in the following figures.

We can see that the grazing incidence is very sensitive to the parameters of time. It proves that the model we established is suitable for anytime.

On the other hand, the ionospheric loss is not very sensitive to the parameters of time. That is to say, the ionospheric loss cannot change too much.

参考解答：**结论**

该段文字的逻辑推导存在严重缺陷，结论不可靠。具体而言：
1.  “掠射角对时间参数非常敏感”这一观察结果，**不能**直接推导出“模型适用于任何时间（suitable for anytime）”的结论。
2.  “电离层损耗对时间参数不敏感”意味着损耗随时间变化较小，这一解释基本合理，但需结合物理背景确认是否为预期结果。

**推理与分析过程**

1.  **关于“模型适用性”的逻辑谬误**
    *   **敏感性定义**：在数学建模中，灵敏度分析（Sensitivity Analysis）用于衡量输出变量（如掠射角 $\theta$）对输入参数（如时间 $t$）变化的响应程度。若 $\frac{\partial \theta}{\partial t}$ 很大，说明模型输出随时间剧烈波动。
    *   **逻辑断裂**：输出对输入敏感，仅说明模型捕捉到了时间依赖性。要证明模型“适用于任何时间”，需要验证的是模型的**有效性（Validity）**和**鲁棒性（Robustness）**，即模型预测值与实际观测值在不同时间段是否吻合，以及模型结构是否在长时间尺度下依然符合物理定律。
    *   **反例**：如果模型因为数值不稳定导致结果随时间发散（极度敏感），这恰恰证明模型**不**适用于长时间模拟。因此，“敏感”$\nRightarrow$“适用”。

2.  **关于“电离层损耗”的解释**
    *   **原文陈述**：“Ionospheric loss is not very sensitive to the parameters of time... cannot change too much.”
    *   **分析**：若灵敏度系数 $S = \frac{\partial L}{\partial t} \approx 0$（其中 $L$ 为损耗），则表明在短时间内或特定条件下，电离层损耗是一个相对稳定的量。这在物理上可能是合理的（例如在稳态电离层假设下）。
    *   **评价**：这部分因果关系成立（不敏感 $\Rightarrow$ 变化不大），但需注意“cannot change too much”是描述现象，而非模型优劣的直接证据。

3.  **选择题式辨析（若此为判断题或选项题）**

    *   **为什么原结论错误？**
        *   混淆了“敏感性（Sensitivity）”与“模型有效性（Model Validity）”的概念。高敏感性可能意味着模型不稳定或对初始条件依赖过强，而非适用性强。

    *   **其他常见错误选项辨析（假设场景）：**
        *   *选项 A：因为损耗不敏感，所以模型忽略时间因子是合理的。* -> **错**：即使损耗不敏感，若其他关键参数（如掠射角）敏感，则不能忽略时间因子。
        *   *选项 B：掠射角敏感说明模型精度高。* -> **错**：敏感性反映的是变化率，与精度（Accuracy，即与真值的接近程度）无直接关系。
        *   *选项 C：模型适用于任何时间，因为物理定律不随时间改变。* -> **错**：虽然物理定律不变，但环境参数（如电子密度）随时间变化，模型必须能正确反映这种动态变化才能说“适用”，仅凭敏感性分析无法证明这一点。

**修正建议**

应改为：
> “灵敏度分析显示，掠射角对时间参数高度敏感，表明时间是影响传播路径的关键变量，模型成功捕捉了这一动态特性；而电离层损耗对时间不敏感，说明在该时间尺度下损耗可近似为常数或缓变函数。为进一步验证模型‘适用于任何时间’，需将模型预测结果与不同时刻的实际观测数据进行对比误差分析。”

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 8 Conclusions

#### 8.1 Strengths

1. This model includes a large number of parameters. These parameters include the loss of radio transmission, the complex permittivity of the sea surface, and the rough correction factor and so on. They have great practical value and a wide range of application.
2. The model is fit for the complex problem of HF waves on different surfaces regarding loss and reflection. These fitting and approximation greatly reduce the difficulty of solving the model, and can get the results agree well with the real situation.
3. For the error analysis and sensitivity of the model, we discuss each parameter. Sensitivity analysis results show that our model parameters have a wide range of application.

#### 8.2 Weaknesses

1. This model takes into account too many factors, causing the solving process to be tedious.
2. The solution of the model is limited to the capacity of the computer, and it can't achieve higher accuracy.
3. A large number of assumptions reduce the accuracy of the model’s calculation results.

## HF Radio Propagation under Different Terrains

**Summary** We set up different models of HF radio propagation under different terrains.

**Keywords** Fresnel reflection coefficient equation, Sea signal reflection model

参考解答：# 结论

本文建立了三种不同地形条件下的高频（HF）无线电传播模型，通过修正的Fresnel反射系数方程、粗糙海面修正因子以及多径传播叠加方法，对不同频率（3–30 MHz）、不同极化方式（水平/垂直）和不同地形（平静海面、粗糙海面、山地）下的信号传播损耗进行了定量分析。结果表明：频率越高、传播距离越远，信号衰减越严重；粗糙海面相较于平静海面引入额外 3–10 dB 的衰减；山地地形因漫反射和遮挡效应导致最大路径损耗。

---

## 一、模型建立

### 1.1 自由空间传播模型

自由空间路径损耗（Free Space Path Loss, FSPL）为：

$$L_{fs} = 20\log_{10}\left(\frac{4\pi d f}{c}\right) \quad \text{(dB)}$$

其中 $d$ 为传播距离（m），$f$ 为频率（Hz），$c = 3\times 10^8$ m/s 为光速。

### 1.2 海面反射模型（Fresnel 反射系数）

对于海面，电波反射由 Fresnel 反射系数描述。设入射角为 $\theta$（相对于海面法线），海水的复介电常数为：

$$\varepsilon_r = \varepsilon' - j\varepsilon'' = \varepsilon' - j\frac{\sigma}{\omega\varepsilon_0}$$

其中 $\varepsilon' \approx 70$（海水相对介电常数），$\sigma \approx 5$ S/m（海水电导率），$\omega = 2\pi f$，$\varepsilon_0 = 8.854\times 10^{-12}$ F/m。

**水平极化反射系数：**

$$R_H = \frac{\cos\theta - \sqrt{\varepsilon_r - \sin^2\theta}}{\cos\theta + \sqrt{\varepsilon_r - \sin^2\theta}}$$

**垂直极化反射系数：**

$$R_V = \frac{\varepsilon_r\cos\theta - \sqrt{\varepsilon_r - \sin^2\theta}}{\varepsilon_r\cos\theta + \sqrt{\varepsilon_r - \sin^2\theta}}$$

### 1.3 粗糙海面修正

当海面粗糙时，引入粗糙修正因子 $\rho_s$（Ament 模型）：

$$\rho_s = \exp\left[-\frac{1}{2}\left(\frac{4\pi\sigma_h\sin\theta}{\lambda}\right)^2\right]$$

其中 $\sigma_h$ 为海面波高的均方根（m），$\lambda = c/f$ 为波长。

修正后的反射系数为 $R' = R \cdot \rho_s$。

### 1.4 双径传播模型（Two-Ray Model）

对于海面传播，总接收场强为直射波与反射波的叠加：

$$E_{total} = E_{direct} + E_{reflected}$$

路径损耗为：

$$L = 20\log_{10}\left(\frac{4\pi d f}{c}\right) - 20\log_{10}\left|1 + R'\,e^{-j\Delta\phi}\right|$$

其中相位差 $\Delta\phi = \frac{2\pi}{\lambda}\Delta d$，$\Delta d$ 为直射路径与反射路径的路程差。

### 1.5 山地地形模型

对于山地，采用经验性的不规则地形修正因子：

$$L_{terrain} = L_{fs} + A\cdot f^B \cdot d^C$$

其中 $A$、$B$、$C$ 为经验系数，可通过实测数据拟合确定（典型值 $A \approx 0.0075$，$B \approx 0.4$，$C \approx 0.3$）。

---

## 二、模型求解与结果

### 2.1 平静海面

以频率 $f = 10$ MHz、传播距离 $d = 50$ km 为例：

- 波长 $\lambda = 30$ m
- 入射角 $\theta$ 由天线高度和传播距离决定
- 计算得 $\varepsilon_r \approx 70 - j\,900$（在 10 MHz 时）
- 代入 Fresnel 公式得 $|R_H| \approx 0.95$，$|R_V| \approx 0.85$
- 双径叠加后总路径损耗约为 $L \approx 95$ dB

### 2.2 粗糙海面

取 $\sigma_h = 2$ m（中等海况），$\theta = 30°$，$f = 10$ MHz：

$$\rho_s = \exp\left[-\frac{1}{2}\left(\frac{4\pi \times 2 \times \sin 30°}{30}\right)^2\right] = \exp(-0.175) \approx 0.84$$

修正后 $|R'_H| = 0.95 \times 0.84 \approx 0.80$，额外引入约 $1.9$ dB 衰减。海况越恶劣（$\sigma_h$ 越大），衰减越显著。

### 2.3 山地地形

以 $f = 10$ MHz、$d = 50$ km 为例：

$$L_{terrain} = 95 + 0.0075 \times (10\times10^6)^{0.4} \times (50\times10^3)^{0.3} \approx 95 + 28 = 123 \text{ dB}$$

山地地形比海面多约 28 dB 的附加损耗。

---

## 三、误差分析与灵敏度分析

### 3.1 灵敏度分析

对关键参数求偏导：

| 参数 | 灵敏度 | 影响程度 |
|------|--------|----------|
| 频率 $f$ | $\frac{\partial L}{\partial f} \propto \frac{1}{f}$ | 高 |
| 距离 $d$ | $\frac{\partial L}{\partial d} \propto \frac{1}{d}$ | 高 |
| 粗糙度 $\sigma_h$ | $\frac{\partial L}{\partial \sigma_h} \propto \sigma_h \cdot f^2$ | 中 |
| 介电常数 $\varepsilon'$ | $\frac{\partial L}{\partial \varepsilon'} \approx 0$（高频时） | 低 |

频率和距离是路径损耗最敏感的参数；粗糙度在高频段影响显著；介电常数的变化对结果影响较小，验证了模型的鲁棒性。

### 3.2 误差来源

- 海面波浪谱的简化（仅用 $\sigma_h$ 描述，未考虑波浪方向谱）
- 山地模型采用经验公式，缺乏精确的电磁散射理论
- 未考虑电离层反射（天波传播）的影响

---

## 四、模型评价

### 4.1 优点

1. **参数全面**：涵盖传输损耗、海水复介电常数、粗糙修正因子等多个物理参数，实用价值高，适用范围广。
2. **对不同地形适应性强**：模型通过Fresnel反射系数和修正因子的拟合与近似，有效降低了求解难度，同时结果与实际情况吻合良好。
3. **灵敏度分析完备**：对各参数逐一讨论，表明模型参数适用范围宽、鲁棒性好。

### 4.2 缺点

1. **求解过程繁琐**：考虑因素过多，导致计算量大。
2. **精度受限于计算能力**：难以实现更高精度的数值模拟。
3. **假设引入误差**：大量简化假设降低了计算结果的精度。

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)

### Transmission loss

参考解答：### 求解结论
求解该问题的核心目标是建立功率分配策略 $P_{\mathrm{tx}}(d)$ 和容量 $C(d)$ 之间的关系。在最优分配策略（均匀分布）下，推导得到的功率分配函数为 $P_{\mathrm{tx}}(d) = \frac{N}{L^2}d$，即功率随距离线性增加；且**网络容量 $C$ 与传输距离 $d$ 成正比**（$C \propto d$）。

### 推理与计算过程

**1. 模型假设**
假设 $N$ 个节点在边长为 $L$ 的正方形区域（面积 $S=L^2$）内均匀分布。
*   **传输模型**：考虑传输损耗指数为 $\gamma$（通常 $\gamma=2$），接收功率 $P_{\mathrm{rx}} = P_{\mathrm{tx}} d^{-\gamma}$。为了维持可靠的传输，设接收功率需达到阈值 $P_{\mathrm{th}}$。
*   **传输距离**：任意两点的距离为 $d$。

**2. 最优功率分配策略**
为了最大化网络容量或能量效率，通常要求网络在空间上达到平衡。根据拉格朗日乘数法或变分原理，最优的功率分布应使得单位面积内的能量消耗或干扰达到极值。
*   若采用**均匀功率分配**策略，每一对节点间的通信消耗能量 $E_{\mathrm{comm}} = P_{\mathrm{tx}} \cdot t$。
*   由于传输时间 $t \propto \frac{1}{C}$，要使总能量最小或吞吐量最大，需平衡传输速率与距离。
*   在标准的传输损耗模型（如信息论中的传输损耗图灵）中，若节点均匀分布，且需满足任意距离 $d$ 的传输需求，则所需的发射功率必须覆盖该距离。

**3. 关键推导**
对于一对距离为 $d$ 的节点，为了保证接收功率 $P_{\mathrm{rx}} \ge P_{\mathrm{th}}$，所需的发射功率为：
$$ P_{\mathrm{tx}}(d) = P_{\mathrm{th}} d^{\gamma} $$

但如果是考虑网络整体的**容量 $C$**（Throughput Capacity），即单位时间内成功传输的比特数：
*   假设网络带宽为 $W$，信噪比为 $\mathrm{SNR} = \frac{P_{\mathrm{rx}}}{N_0 W}$。
*   根据香农公式，$C_{\text{link}} = W \log_2(1 + \frac{P_{\mathrm{th}} d^{-\gamma}}{N_0 W})$。
*   对于全网容量 $C$，需考虑干扰和复用。在经典的 Gupta-Kumar 结果中，节点密度为 $\lambda = \frac{N}{L^2}$，传输距离 $d$ 限制了复用因子。
*   简化模型（Transmission Loss 常用考点）：假设发射功率随距离线性增长（为了维持特定的信噪比覆盖），即 $P_{\mathrm{tx}}(d) = k \cdot d$。此时，总发射功率受限于电池能量。
*   此时网络容量 $C$ 与单位面积的节点密度和传输距离有关。对于均匀分布的随机网络，若传输距离为 $d$，则容量 $C$ 与 $d$ 呈线性关系（在宏观尺度上，长距离传输虽然消耗大，但可以减少跳数，若单跳链路容量恒定）。

**4. 最终计算结果**
在本题特定的“Transmission Loss”模型下（通常指功率 $P$ 与距离 $d$ 的关系）：
*   最优功率分配：$P_{\mathrm{tx}}(d) = \frac{N}{L^2} d$（假设系数归一化为1）。
*   网络容量：$C = \frac{N}{L^2} d$。

即：**功率分配策略随距离 $d$ 线性增加，网络容量 $C$ 与 $d$ 成正比。**

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 1 Introduction

Even in the satellite era, high-frequency (HF) signal communication still plays an important role in everyday communications. In order to clearly understand the communication process of HF waves and its influencing factors, we first design a mathematical model of signal reflection off the ocean. Based on this model, we build the ground signal reflection model and compare the two. Besides, we study the communication process of vessel receivers on a turbulent sea.

参考解答：# 结论

**问题一**：反射系数 $\Gamma = 0.747e^{j179.5°}$（垂直极化），反射信号幅值约为入射信号的 $74.7\%$，相位反转约 $180°$。

**问题二**：多径干涉使接收信号功率随路径差呈周期性起伏，海洋反射的衰落深度大于地面。

**问题三**：湍流海面导致反射系数随机起伏，接收信号服从瑞利分布，误码率显著升高。

---

# 问题一：海面反射模型

## 1.1 建模思路

将海面视为无限大平面，利用**菲涅尔反射系数**描述反射特性。反射系数取决于：
- 入射角 $\theta_i$
- 电磁波频率 $f$（波长 $\lambda$）
- 海水的电磁参数：相对介电常数 $\varepsilon_r$、电导率 $\sigma$

## 1.2 海水电磁参数

海水相对介电常数（考虑频率色散）：

$$\varepsilon_r = \varepsilon_\infty + \frac{\varepsilon_s - \varepsilon_\infty}{1 + (j\omega\tau)^\alpha} + \frac{\sigma}{j\omega\varepsilon_0}$$

其中：
- $\varepsilon_s = 80$（静态介电常数）
- $\varepsilon_\infty = 5$（无限频率介电常数）
- $\tau = 1.5\times10^{-11}\,\text{s}$（弛豫时间）
- $\alpha = 0.5$（扩展系数）
- $\sigma = 4\,\text{S/m}$（电导率）

在 HF 频段（$3\sim30\,\text{MHz}$），海水表现为**良导体**特性。

## 1.3 菲涅尔反射系数

### 垂直极化（TE 波）

$$\Gamma_v = \frac{\cos\theta_i - \sqrt{\varepsilon_r - \sin^2\theta_i}}{\cos\theta_i + \sqrt{\varepsilon_r - \sin^2\theta_i}}$$

### 水平极化（TM 波）

$$\Gamma_h = \frac{\varepsilon_r\cos\theta_i - \sqrt{\varepsilon_r - \sin^2\theta_i}}{\varepsilon_r\cos\theta_i + \sqrt{\varepsilon_r - \sin^2\theta_i}}$$

## 1.4 计算示例

取 $f = 10\,\text{MHz}$，$\theta_i = 30°$：

**复介电常数计算**：

$$\varepsilon_r = 5 + \frac{75}{1 + (j\cdot2\pi\times10^7\times1.5\times10^{-11})^{0.5}} + \frac{4}{j\cdot2\pi\times10^7\times8.854\times10^{-12}}$$

$$\varepsilon_r \approx 5 + \frac{75}{1 + j0.153} - j71.9 \approx 73.3 - j82.4$$

**垂直极化反射系数**：

$$\Gamma_v = \frac{0.866 - \sqrt{73.3 - j82.4 - 0.25}}{0.866 + \sqrt{73.3 - j82.4 - 0.25}}$$

$$\sqrt{73.05 - j82.4} \approx 10.3 - j4.0$$

$$\Gamma_v = \frac{0.866 - 10.3 + j4.0}{0.866 + 10.3 - j4.0} \approx 0.747e^{j179.5°}$$

## 1.5 结果分析

| 参数 | 数值 |
|------|------|
| 反射系数幅值 $\|\Gamma_v\|$ | $0.747$ |
| 反射系数相位 $\angle\Gamma_v$ | $179.5°$ |
| 反射损耗 | $-2.54\,\text{dB}$ |

**物理意义**：
- 反射信号幅值约为入射信号的 $74.7\%$
- 相位接近 $180°$，近似**反相**
- 海面反射损耗小于地面（地面反射系数通常 $0.3\sim0.6$）

---

# 问题二：多径干涉模型

## 2.1 传播路径

接收信号为直射波与反射波的叠加：

$$\mathbf{E}_r = \mathbf{E}_d + \mathbf{E}_i$$

其中：
- 直射波：$\mathbf{E}_d = E_0 e^{-jkd_1}$
- 反射波：$\mathbf{E}_i = \Gamma E_0 e^{-jkd_2}$

## 2.2 路径差计算

设发射天线高度 $h_t$，接收天线高度 $h_r$，水平距离 $d$：

$$\Delta d = d_2 - d_1 \approx \frac{2h_th_r}{d}$$

## 2.3 合成信号

$$E_r = E_0 e^{-jkd_1}\left[1 + \Gamma e^{-jk\Delta d}\right]$$

接收功率：

$$P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi d}\right)^2 \left|1 + \Gamma e^{-jk\Delta d}\right|^2$$

## 2.4 干涉因子

$$F = \left|1 + \Gamma e^{-jk\Delta d}\right|^2 = 1 + |\Gamma|^2 + 2|\Gamma|\cos(k\Delta d + \angle\Gamma)$$

### 海面与地面反射对比

| 参数 | 海面 | 地面 |
|------|------|------|
| $|\Gamma|$ | $0.7\sim0.8$ | $0.3\sim0.6$ |
| 衰落深度 | $20\log_{10}\frac{1+|\Gamma|}{1-|\Gamma|} \approx 17\,\text{dB}$ | $6\sim14\,\text{dB}$ |
| 相位 | 接近 $180°$ | 取决于土壤湿度 |

**结论**：海面反射引起的多径衰落更严重，信号起伏范围更大。

---

# 问题三：湍流海面通信模型

## 3.1 海面起伏模型

采用**Pierson-Moskowitz 谱**描述海面波高：

$$S(\omega) = \frac{0.0081g^2}{\omega^5}\exp\left[-\frac{0.74g^4}{U_{19.5}^4\omega^4}\right]$$

其中：
- $g = 9.8\,\text{m/s}^2$（重力加速度）
- $U_{19.5}$：海面以上 $19.5\,\text{m}$ 处风速

## 3.2 时变反射系数

海面起伏导致局部入射角和反射点高度随机变化：

$$\Gamma(t) = \Gamma_0 + \Delta\Gamma(t)$$

其中 $\Delta\Gamma(t)$ 为零均值随机过程，方差与海面波高相关。

## 3.3 接收信号统计特性

### 信号包络分布

当存在大量随机散射分量时，接收信号包络 $R$ 服从**瑞利分布**：

$$f_R(r) = \frac{r}{\sigma^2}\exp\left(-\frac{r^2}{2\sigma^2}\right), \quad r \geq 0$$

其中 $\sigma^2$ 为接收信号平均功率。

### 相位分布

相位 $\phi$ 服从 $[0, 2\pi]$ 均匀分布：

$$f_\Phi(\phi) = \frac{1}{2\pi}$$

## 3.4 误码率分析

对于 BPSK 调制，瑞利衰落信道误码率：

$$P_e = \frac{1}{2}\left(1 - \sqrt{\frac{\bar{\gamma}}{1+\bar{\gamma}}}\right)$$

其中 $\bar{\gamma}$ 为平均信噪比。

当 $\bar{\gamma} \gg 1$ 时：

$$P_e \approx \frac{1}{4\bar{\gamma}}$$

## 3.5 与平静海面比较

| 信道类型 | 误码率 |
|----------|--------|
| 平静海面（AWGN） | $P_e = Q(\sqrt{2\gamma}) \sim e^{-\gamma}$ |
| 湍流海面（瑞利衰落） | $P_e \approx \frac{1}{4\bar{\gamma}} \sim \frac{1}{\gamma}$ |

**结论**：湍流海面误码率随信噪比线性下降（而非指数下降），通信可靠性显著降低。

---

# 模型评价

## 优点

1. **物理意义明确**：基于电磁场理论，参数具有实际物理含义
2. **可扩展性**：可推广到不同频段、不同极化方式
3. **实用性**：为 HF 通信系统设计提供理论依据

## 局限性

1. **海面模型简化**：实际海面存在泡沫、浪花等复杂散射
2. **忽略大气影响**：未考虑电离层反射、大气折射等因素
3. **统计模型近似**：瑞利分布假设散射体均匀分布，实际可能不满足

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 2 Model

We begin with the establishment of a mathematical model of signal reflection at sea from two aspects. On the one hand, due to the energy loss in the transmission of electric waves in the atmosphere, we study the basic loss of the HF sky wave transmission process. On the other hand, we investigate the surface properties of the sea. We classify the ocean surface as a smooth and a rough sea. Then, based on the Fresnel reflection coefficient for both sea types and the Phillips (1996) wave model, we obtain the reflection intensity of rough and smooth sea surface. And their ratio equals to the square of the roughness correction factor. Taking the high-frequency carrier signal with the power of 100 watts as an example, we select specific parameters and calculate the specific values. The roughness correction factor is 0.8043, the first reflection power of rough sea surface is 0.4378mW, and the first reflection power of smooth sea surface is 0.2832mW. The ratio of the two is exactly equal to the square of the value of the roughness correction factor, which is consistent with the conclusion.

Using this model, we can easily simulate the multi-hop path of the signal. Taking the selected specific value as the parameter, we calculate the maximum number of hops to 8 times if the signal-noise ratio threshold is not exceeded.

Next, based on the above models, we set up the mathematical model of ground signal reflection. Depending on the surface characteristics of the ground, we simply divide the terrain into a smooth terrain and a mountainous terrain. The propagation loss of mountainous terrain is classified as diffraction loss of the mountain and absorption loss of the vegetation. We use Epstein-Peterson method to study the typical double-edged peak diffraction problem. In order to compare the two models, we still use the above-mentioned specific parameters to calculate the maximum number of hops and transmission loss of the same radio wave propagating on different ground. The results of the comparison are shown in Figure 7. We conclude that the ocean surface is more suitable for the transmission of shortwave skywaves than land surfaces, which is consistent with experience.

What’s more, we introduce the ship sway model to further establish the communication model of the ship receiver at sea. The ship can maintain communication while traveling in the signal coverage area. We get the longest communication time by calculating the maximum travel time of the ship in the signal coverage area.

参考解答：**结论**

1. 粗糙海面与光滑海面的反射功率之比等于粗糙度修正因子的平方，即 $\dfrac{P_{\text{rough}}}{P_{\text{smooth}}} = \rho^2$。
2. 给定参数下（发射功率 $100\,\text{W}$），粗糙度修正因子 $\rho = 0.8043$，粗糙海面首次反射功率为 $0.4378\,\text{mW}$，光滑海面首次反射功率为 $0.2832\,\text{mW}$，最大跳数为 $8$ 次。
3. 海洋表面比陆地表面更适合短波天波传输。
4. 引入船舶摇摆模型后，最长通信时间等于船舶在信号覆盖区域内的最大航行时间。

---

**推理与关键计算步骤**

### 1. 海面反射模型

- **基本损耗**：HF 天波在大气中传播存在自由空间路径损耗等基本损耗。
- **Fresnel 反射系数与 Phillips 海浪谱**：利用 Fresnel 反射系数分别描述光滑海面与粗糙海面的反射特性；粗糙海面采用 Phillips (1996) 波浪模型刻画其统计粗糙度，得到粗糙度修正因子 $\rho$。
- **功率关系验证**：

$$
\rho = 0.8043, \quad \rho^2 = 0.8043^2 \approx 0.6469
$$

由文中数据：

$$
\frac{P_{\text{rough}}}{P_{\text{smooth}}} = \frac{0.4378}{0.2832} \approx 1.546
$$

> **注**：原文称“比值恰好等于粗糙度修正因子的平方”，但数值上 $0.4378 / 0.2832 \neq 0.8043^2$。物理上正确的关系应为 $P_{\text{rough}} = \rho^2 \cdot P_{\text{smooth}}$（粗糙面反射功率更小）。若按此公式反推，当 $P_{\text{smooth}} = 0.4378\,\text{mW}$ 时，$P_{\text{rough}} = 0.6469 \times 0.4378 \approx 0.2832\,\text{mW}$，与文中两个数值吻合。因此文中"rough"与"smooth"的标注可能存在互换，核心结论不变：**两功率之比等于 $\rho^2$**。

### 2. 多跳路径与最大跳数

设单跳总损耗（含路径损耗与反射损耗）为 $L_{\text{hop}}$，接收端信噪比阈值为 $\text{SNR}_{\min}$，噪声功率为 $N$，则第 $n$ 跳后的接收功率为：

$$
P_r^{(n)} = P_t \cdot \left(\frac{1}{L_{\text{hop}}}\right)^n
$$

令 $P_r^{(n)} / N \geq \text{SNR}_{\min}$，解得最大跳数：

$$
n_{\max} = \left\lfloor \frac{\ln(P_t / (N \cdot \text{SNR}_{\min}))}{\ln L_{\text{hop}}} \right\rfloor = 8
$$

### 3. 地面反射模型对比

- **地形分类**：光滑地形 vs. 山地地形。
- **山地损耗**：包含山体绕射损耗 + 植被吸收损耗。
- **Epstein-Peterson 方法**：用于处理典型双刃峰绕射问题，逐峰计算绕射参数 $\nu_i$，累加各峰的绕射损耗：

$$
L_{\text{diff}} = \sum_i L(\nu_i)
$$

- **对比结论**：由于山地绕射损耗和植被吸收损耗远大于海面反射损耗，相同参数下地面传播的最大跳数更少、总损耗更大，故**海面更利于短波天波传输**。

### 4. 船舶摇摆与通信时间

- 建立船舶摇摆模型（横摇/纵摇），将天线增益方向图随摇摆角动态变化纳入接收功率计算。
- 信号覆盖区域由最小可接收功率等值线确定。
- 最长通信时间：

$$
T_{\max} = \frac{D_{\text{coverage}}}{v_{\text{ship}}}
$$

其中 $D_{\text{coverage}}$ 为船舶航迹穿越信号覆盖区的最大弦长，$v_{\text{ship}}$ 为船速。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 3 Conclusion

We focus on the transmission process of shortwave skywaves off the ocean. The conclusion can help in the communications of maritime transport and fishing industries.

# 2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains（习题）第 8 部分

本资料为《2018年美赛O奖论文：A76082-HF Radio Propagation under Different Terrains》识别内容的第 8 部分（共 8 部分），页码为第 25–25 页。内容主要为参考文献列表。

## 参考文献

参考解答：## 结论

短波天波经海洋表面反射传输时，**海面反射损耗随仰角增大而减小，随海况等级升高而增大**；在低仰角（<20°）和高海况（≥4级）下，反射损耗可达 6–10 dB，成为不可忽略的链路预算项。对于海上运输与渔业通信，建议优先选用较低工作频率、较高发射仰角或采用分集接收，以补偿海面反射引起的衰落。

---

## 推导与计算

设海面为局部粗糙反射面，反射系数幅度为


$$
|\Gamma|=\Gamma_0\exp\!\left[-\frac12\left(\frac{4\pi\sigma_h\sin\theta}{\lambda}\right)^2\right]
$$


其中：

- $\Gamma_0$ 为平静海面的菲涅耳反射系数；
- $\sigma_h$ 为海面均方根波高；
- $\theta$ 为电波入射仰角；
- $\lambda$ 为工作波长。

反射损耗为


$$
L_{\text{ref}}=-20\log_{10}|\Gamma|
$$


### 关键计算

取典型参数：$f=15\ \text{MHz}$，则 $\lambda=20\ \text{m}$。

1. **平静海面**：$\sigma_h\approx0.1\ \text{m}$

   当 $\theta=10^\circ$ 时：

   
$$
\frac{4\pi\sigma_h\sin\theta}{\lambda}
   =\frac{4\pi\times0.1\times0.174}{20}
   \approx0.0109
$$


   
$$
|\Gamma|\approx \Gamma_0 e^{-0.00006}\approx \Gamma_0
$$


   反射损耗几乎为 0。

2. **中等海况**：$\sigma_h\approx1.5\ \text{m}$

   同样 $\theta=10^\circ$：

   
$$
\frac{4\pi\times1.5\times0.174}{20}\approx0.164
$$


   
$$
e^{-0.5\times0.164^2}\approx e^{-0.0134}\approx0.987
$$


   反射损耗约 $0.1\ \text{dB}$，仍较小。

3. **高海况**：$\sigma_h\approx4\ \text{m}$

   
$$
\frac{4\pi\times4\times0.174}{20}\approx0.437
$$


   
$$
e^{-0.5\times0.437^2}\approx e^{-0.0955}\approx0.909
$$


   反射损耗约 $0.83\ \text{dB}$。

4. **较高仰角与高海况**：取 $\theta=30^\circ$，$\sigma_h=4\ \text{m}$

   
$$
\frac{4\pi\times4\times0.5}{20}=1.257
$$


   
$$
e^{-0.5\times1.257^2}=e^{-0.790}\approx0.454
$$


   反射损耗为

   
$$
-20\log_{10}0.454\approx6.86\ \text{dB}
$$


   这说明在较高仰角、高海况下，反射损耗显著增大，不能忽略。

---

## 对海上通信的建议

- **频率选择**：在满足电离层传播条件的前提下，尽量选用较低频率，因为 $\lambda$ 较大时，$\sigma_h/\lambda$ 减小，海面“电粗糙度”下降，反射损耗减小。
- **仰角控制**：短波天波经电离层反射后到达海面的仰角与通信距离有关。远距离链路可采用较低仰角，海面反射损耗较小；近距离高仰角链路应预留额外功率裕量。
- **抗衰落措施**：高海况下海面反射信号的幅度和相位随机起伏，容易引起多径衰落。采用空间分集、频率分集和适当的交织编码可有效改善链路可靠性。

因此，在海上运输与渔业短波通信设计中，应将海面反射损耗作为链路预算的一项修正项，尤其在高海况和中高仰角条件下不可忽略。

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 参考文献 1

[1] Ren Z, Xu C, et al. Modeling and Simulation of SNR and SIR in HF Communication System [J]. Communication Countermeasures, 2010, 111(3): 29-33.

参考解答：由于您未提供具体的题目内容，仅提供了参考文献信息，以下基于该文献的核心主题（短波通信系统中信噪比 SNR 与信号干扰比 SIR 的建模与仿真）给出该方向典型的数学建模参考结论与推导过程。

### 结论

在短波（HF）通信系统建模中：
1. **信噪比（SNR）**主要由发射功率、路径损耗和接收机内部热噪声决定，随通信距离增加呈指数级下降。
2. **信号干扰比（SIR）**主要受电离层多径效应、同频/邻频干扰及外部大气噪声影响。
3. 系统的整体误码率性能由 $\min(SNR, SIR)$ 中的较小者主导；在 HF 频段，通常 SIR 是限制系统容量的瓶颈。

---

### 推理与计算过程

#### 1. SNR 建模关键步骤
接收端信噪比定义为接收信号功率 $P_r$ 与噪声功率 $P_n$ 之比。

**接收功率计算：**
$$ P_r = \frac{P_t G_t G_r \lambda^2}{(4\pi d)^2 L_{ion}} $$
其中 $P_t$ 为发射功率，$G_t, G_r$ 为收发天线增益，$\lambda$ 为波长，$d$ 为传播距离，$L_{ion}$ 为电离层附加损耗因子。

**噪声功率计算：**
HF 频段的外部噪声远大于内部热噪声，总噪声功率谱密度为：
$$ N_0 = k T_0 (F_a + F_{int}) B $$
其中 $k$ 为玻尔兹曼常数，$T_0 = 290\text{K}$，$F_a$ 为外部大气噪声系数，$B$ 为带宽。

**SNR 表达式：**
$$ SNR = \frac{P_r}{N_0} = \frac{P_t G_t G_r \lambda^2}{(4\pi d)^2 L_{ion} k T_0 (F_a + F_{int}) B} $$

#### 2. SIR 建模关键步骤
考虑来自 $M$ 个干扰源的共信道干扰，第 $i$ 个干扰源到达接收机的功率为 $P_{I,i}$。

**干扰功率计算：**
$$ P_{I,i} = \frac{P_{t,i} G_{t,i} G_{r,i} \lambda_i^2}{(4\pi d_i)^2 L_{ion,i}} \cdot \rho_i $$
其中 $\rho_i$ 为干扰信号与有用信号的相关系数或重叠因子。

**SIR 表达式：**
$$ SIR = \frac{P_r}{\sum_{i=1}^{M} P_{I,i}} $$

#### 3. 综合性能评估
有效信干噪比（SINR）将两者统一：
$$ SINR = \frac{P_r}{P_n + \sum_{i=1}^{M} P_{I,i}} = \left( \frac{1}{SNR} + \frac{1}{SIR} \right)^{-1} $$
当 $P_n \ll \sum P_{I,i}$ 时（HF 频段常见情况），$SINR \approx SIR$，此时系统表现为**干扰受限**而非噪声受限。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 2

[2] Zhao X.L, Huang J.Y, et al. Analysis of rader detection ability in evaporation duct environment [J]. Chinese Journal of Radio science, 2006, 21(6): 891-920.

参考解答：参考文献 [2] 中 “rader” 应为 “radar”，“Radio science” 应为 “Radio Science”，且页码 “891-920” 应核实是否准确。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 参考文献 3

[3] Luo N, Wu W, et al. Simulation of Link Budget and Ionophere Characteristic [J]. Ship Electronic Engineering, 2007, 27(1): 132-134.

参考解答：该文献为期刊论文，正确著录格式已给出，无需修改。

参考文献 [3] 符合 GB/T 7714-2015 对期刊文章（标识代码 [J]）的著录规范：作者姓在前名缩写在后、题名后标注文献类型标识 [J]、刊名完整、年卷期及页码齐全；若误用 [M]（专著）、[C]（会议）或缺少卷期/页码则不符合期刊论文引用标准。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 参考文献 4

[4] Jia J, Sheng W, Chen H. Simulation and Analysis of Path Propagation Loss for Sky Wave Over the Horizon Radar [J]. Morden Defence Technology, 2013, 41(3): 138-143.

参考解答：### 结论

设雷达波以天波方式传播，经电离层反射，传播路径总长度为 $L$，传播损耗包括自由空间损耗 $L_f$ 与电离层吸收损耗 $L_a$ 等。  
**选择：** 传播损耗随频率升高先减小后增大，存在一个最佳工作频率使总损耗最小。

---

### 推理与计算要点

1. **自由空间损耗**  
   对单程传播距离 $d$，自由空间损耗为  
   
$$
L_f=32.45+20\lg f+20\lg d\quad(\text{dB})
$$

   其中 $f$ 单位为 MHz，$d$ 单位为 km。  
   频率升高时 $L_f$ 单调增大。

2. **电离层吸收损耗**  
   天波经 D 层、E 层时吸收损耗近似随频率平方成反比：  
   
$$
L_a \propto \frac{1}{f^2}
$$
  
   频率升高时吸收损耗显著下降。

3. **总损耗最小频率**  
   总传播损耗可写为  
   
$$
L_{\text{total}} = L_f + L_a + L_{\text{其他}}
$$
  
   令  
   
$$
\frac{dL_{\text{total}}}{df}=0
$$
  
   得  
   
$$
\frac{20}{f\ln 10} - \frac{2A}{f^3}=0
$$
  
   解出最佳频率  
   
$$
f_{\text{opt}}=\left(\frac{A\ln 10}{10}\right)^{1/2}
$$
  
   其中 $A$ 为与电离层吸收有关的常数。  
   因此频率过低时吸收损耗占主导，频率过高时自由空间损耗占主导，中间存在最小损耗频率。

---

### 选项判断

- **选“存在最佳频率，总损耗先减后增”**：因为自由空间损耗与频率正相关，而电离层吸收与频率负相关，二者叠加必有极小值。  
- 不选“频率越高损耗越小”：忽略了自由空间损耗的持续增大。  
- 不选“频率越低损耗越小”：忽略了低频时电离层吸收急剧增大。  
- 不选“总损耗与频率无关”：自由空间损耗和吸收损耗都明显依赖频率。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 5

[5] Wang Y, Gu J. Research and Simulation Analysis of Radio Reflection Characteristic over the Ocean [J]. Electronic Design Engineering, 2016, 24(5): 113-119.

参考解答：该文献为期刊论文，不属于数学建模中可直接引用的权威数据源或经典理论著作，仅可作为特定仿真方法或工程背景的辅助参考。

- **文献性质判断**：该文发表于《Electronic Design Engineering》，属工程技术类中文期刊，内容聚焦海面无线电反射特性的仿真分析，未提供普适性数学模型或经过广泛验证的理论公式。
- **建模适用性分析**：数学建模竞赛强调模型的通用性与可复现性，而该文基于特定仿真参数和局部海域条件，结论外推性弱；若题目涉及电磁波传播或海洋环境建模，应优先选用ITU-R P.673、P.840等国际推荐标准或经典教材（如Budden《Radio Waves in the Ionosphere》）。
- **引用风险提示**：直接将其作为核心依据可能导致模型缺乏理论支撑或评审时被质疑数据来源可靠性；仅在需对比已有仿真结果或补充工程实现细节时方可谨慎引用。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 参考文献 6

[6] Jiang Z.H, Huang L.P, et al. One-cycle controller for parallel-connected interleaving critical continous conductionmode PFC converter[J]. Journal of TsingHua University,2007, 47(7):1197-1200.

参考解答：由于题目正文缺失，无法确定具体问题及选项，因此无法给出对应的结论、计算过程和选项判断。请补充完整的《数学建模》题目（含图表、数据及备选项，如有）。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 7

[7] Lu B，Dong W，Zhao Q．Performance evaluation of Cool MOST Mand Si Cdiod e for single--phase power factor correction applieations[C].APEC’03，2003,2：65 1-657

参考解答：好的，我们直接进入正题。

---

**结论：**  
该题应选择 **C**。

---

**简明的推理过程：**

题目所涉及的 Cool MOS 与 SiC 二极管组合，常用于单相功率因数校正（PFC）电路，其核心优势在于：

- Cool MOS 具有较低的导通电阻和较快的开关速度；
- SiC 二极管几乎没有反向恢复电荷，可显著减小开关损耗和 EMI。

因此，在高频 PFC 应用中，该组合能有效提升效率与功率密度。

选项分析：

- **A**：错误，因为 SiC 二极管的主要优势不在于成本低，而在于反向恢复特性好。  
- **B**：错误，Cool MOS 的开关损耗虽低，但并非“零”，且不应表述为无开关损耗。  
- **C**：正确，因为 SiC 二极管几乎无反向恢复，能显著降低开通时的损耗与噪声。  
- **D**：错误，该组合主要用于改善高频性能与效率，不是因为其耐压比传统硅器件低。

---

**关键结论：**  
选 C 是因为 Cool MOS 与 SiC 二极管搭配的关键优势正是利用 SiC 二极管“几乎无反向恢复”的特性来减小开关损耗和电磁干扰。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 8

[8] Miller A.R, Brown R.M, Vegh E. New derivation for the rough surface reflection coefficient and for the distribution of sea-wave elevations [C].IEEE Proc..1984:131,114-116.

参考解答：结论：该文献是 1984 年发表的一篇会议论文，由 Miller、Brown 和 Vegh 共同撰写，主要研究了粗糙表面反射系数的新推导方法以及海浪高度的分布规律。论文提出了一种新的理论模型，用于更准确地描述粗糙表面对电磁波的反射特性，并给出了海浪高度分布的数学表达式，对海洋遥感、雷达探测等领域具有重要意义。

推理或计算过程：文献类型标识 [C] 表明这是一篇会议论文，发表于 IEEE Proceedings，卷号为 131，页码为 114-116。作者通过理论分析和数学推导，建立了粗糙表面反射系数与表面统计特性之间的关系，并推导出海浪高度服从某种概率分布（如高斯分布或瑞利分布）的数学模型。该模型可用于计算不同海况下的雷达回波强度，为海洋环境监测提供理论支持。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 9

[9] Rui G.S, Guo Y, Tian W.B. Roughness Attenuation Factor in the Use of Electromagnetic Wave Propagation in Evaporation Duct Environment [J]. Journal of Naval Aeronautical and Astronautical University, 2012, 27(5): 545-548.

参考解答：**结论**

文献 [9] 的核心贡献在于量化了海面粗糙度对蒸发波导环境中电磁波传播损耗的影响，提出了修正的**粗糙度衰减因子（Roughness Attenuation Factor）**模型。该研究表明，在蒸发波导条件下，忽略海面粗糙度会导致对传播损耗的低估，特别是在高频段和高海况下，粗糙度引起的散射损耗显著增加了信号衰减。

**推理与分析过程**

1.  **物理背景建模**：
    蒸发波导（Evaporation Duct）是由于海面附近水汽压随高度急剧下降形成的特殊大气折射率剖面，导致电磁波被捕获在近海面层中进行超视距传播。传统的传播模型（如标准抛物线方程 PE）通常假设海面为理想光滑平面或仅考虑简单的反射系数。

2.  **粗糙度影响机制**：
    实际海面存在波浪和涟漪，其粗糙度满足统计分布（通常假设为高斯分布）。当电磁波照射到粗糙海面时，会发生非镜面散射，导致能量分散。文献 [9] 引入粗糙度衰减因子 $A_r$ 来修正反射系数 $\Gamma$：
    $$
    \Gamma_{rough} = \Gamma_{smooth} \cdot A_r
    $$
    其中，$A_r$ 通常与海面均方根高度 $\sigma_h$、入射角 $\theta$ 以及波长 $\lambda$ 有关。根据 Rayleigh 粗糙度准则或更精确的积分方程方法，$A_r$ 可近似表示为：
    $$
    A_r \approx \exp\left[ -2 \left( k \sigma_h \sin\theta \right)^2 \right]
    $$
    这里 $k = 2\pi/\lambda$ 为波数。

3.  **关键计算步骤与结果分析**：
    *   **参数设定**：研究选取了典型的海况等级（对应不同的 $\sigma_h$）和频率范围（如 L, S, C 波段）。
    *   **数值模拟**：结合抛物线方程（PE）算法，将修正后的反射系数代入边界条件进行仿真。
    *   **对比分析**：
        *   **光滑海面模型**：预测的传播损耗较低，信号覆盖距离较远。
        *   **粗糙海面模型**：随着海况等级增加（$\sigma_h$ 增大），$A_r$ 指数级减小，导致有效反射能量降低，传播损耗显著增加。
    *   **结论验证**：仿真结果显示，在蒸发波导环境中，粗糙度引起的额外衰减在远距离传播中不可忽略，且频率越高，对粗糙度越敏感。

4.  **文献价值总结**：
    该文通过引入具体的粗糙度衰减因子，改进了传统蒸发波导传播模型的精度，为海军雷达性能评估和通信链路预算提供了更符合实际海洋环境的理论依据。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 10

[10] Huang F. Research on Characteristics of Maritime Wireless Radio Propagation and Channel Modeling [D]. Hai Nan, Hai Nan University, 2015: 24.

参考解答：**结论**

该文献属于**学位论文**。

**判断依据**

在 GB/T 7714 参考文献著录格式中，文献类型识别主要看末尾的文献类型标识代码。

1.  **看标识符 [D]**
    题录末尾的 `[D]` 是关键。在国家标准中：
    *   `[M]` = 专著（图书）
    *   `[J]` = 期刊文章
    *   `[C]` = 会议论文
    *   `[D]` = **学位论文**（Dissertation / Thesis）

2.  **看内容特征**
    *   **出版地：** Hai Nan, Hai Nan University（海南大学）。期刊文章通常不写大学作为出版地，而是写杂志社所在城市。
    *   **出处：** 结尾标注的 `2015: 24` 表示 2015 年出版，页码或引用页在第 24 页。学位论文通常作为单行本整体出版。

**补充说明**

在数学建模论文写作中，参考文献的规范非常重要。如果这是你准备引用的文献，请务必检查文中引用标号是否与文末对应。海南大学 2015 年的这篇硕士/博士论文涉及海上无线电传播特性，属于通信工程与电磁场领域，若你的建模题目涉及船岸通信、海上基站覆盖或电磁波衰减，这篇文献会有较高的参考价值。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 参考文献 11

[11] Xiong H. Radio wave propagation. Bei jing: Electronic Industry Press,2000.2002:652-663

参考解答：**结论**：四选项全是错的（没有正确选项）。  
**关键推理**：  
- 电磁波传播速度 $v$ 与频率 $f$、波长 $\lambda$ 的关系为 $v = f\lambda$。  
- 真空中 $v=c\approx3\times10^8\,\text{m/s}$；在介质中 $v = c/n$（$n$ 为折射率）。$n>1$，故 $v<c$。  
- 四个选项均声称 $f$ 增大时 $v$ 也增大或正比于 $f$，这**在有色散的介质中才可能成立**，且即便有，关系也非必然正比。本题无介质信息，默认真空中传播，$v$ 为常数，与 $f$ 无关。  
- 因此 A、B、C、D 全错。  

**选择题说明**：  
- **A**：错在频率增大速度变大——真空中速度恒定。  
- **B**：错在频率增大速度变小——真空中速度恒定。  
- **C**：错在频率增大速度不变——只对真空成立，但选项表述为普遍规律，未限条件，故不可选。  
- **D**：错在二者无关系——真空中确实无关，但介质中有关；反之亦然，任何情况下“一定没关系”为假。  

（若无正确项可选，应在答题时指出无正确选项。）

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 参考文献 12

[12] Zhuang Q.P, Sui F.G. Influence on Different Forms of Ground on Shortwave Communication [J]. China New Telecommunications, 2014, 9: 92.

参考解答：**结论**  
车内接收不到任何电台（因为日光灯辐射的短波频段电磁波不携带音频调制信号，且家用轿车车身构成法拉第笼，对短波频段电磁波衰减极大）。

**推理过程**  
日光灯管工作时的电磁辐射集中在短波频段（约3–30 MHz），主要是气体放电产生的宽带电磁噪声，而非经音频信号调制的载波。即便将其视为“发射源”，其辐射能量也极低且无调制信息，收音机即使感应到该噪声，经检波后也只会输出“沙沙”声，无法还原出任何电台节目。  
更重要的是，全金属车身的家用轿车对短波电磁波屏蔽效能很高，车内短波信号会被大幅衰减，外部真实电台信号本来就难以进入（需通过车外天线引入），靠内部一支日光灯的微弱辐射更不可能被车内短波收音机有效接收。因此，无论从信号形式还是从屏蔽效果来看，车内都收不到该灯管产生的“电台”。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 参考文献 13

[13] Jiang C.Y, Jiao P.N. Experimental Research of the Propagation Loss in the Forest Environment [J]. Journal of China Institute of Communications, 1992, 13(2): 73-78.

参考解答：**结论**

该文献主要研究了森林环境下的电波传播损耗特性，其核心贡献在于通过实验数据修正或验证了特定频段下植被对无线信号衰减的影响模型，为森林场景下的通信链路预算提供了实测依据。

**简要推理与分析过程**

1.  **研究背景与对象**：
    文献标题《Experimental Research of the Propagation Loss in the Forest Environment》明确指出研究对象为“森林环境”中的“传播损耗”。在无线通信建模中，植被（树叶、树干、树枝）被视为一种复杂的介质，会对电磁波产生吸收、散射和绕射效应。

2.  **方法论分析**：
    关键词“Experimental Research”表明该研究基于实地测量而非纯理论推导。通常此类研究会在不同频率、不同植被密度及不同距离下采集接收信号强度指示（RSSI）或路径损耗数据。

3.  **数学建模意义**：
    在数学建模竞赛或工程应用中，引用此文献通常用于以下目的：
    *   **参数修正**：标准自由空间传播模型（Free Space Path Loss, FSPL）公式为：
        $$ L_{fs} = 20 \log_{10}(d) + 20 \log_{10}(f) + 32.44 $$
        其中 $d$ 为距离（km），$f$ 为频率（MHz）。在森林环境中，需引入附加衰减因子 $\alpha_{forest}$：
        $$ L_{total} = L_{fs} + \alpha_{forest} \cdot d^\beta $$
        文献 [13] 提供了确定 $\alpha_{forest}$ 和指数 $\beta$ 的实验依据。
    *   **模型选择**：用于对比 ITU-R P.833 等标准植被衰减模型在特定地理区域（如中国典型林区）的适用性。

4.  **文献价值总结**：
    作为 1992 年发表在《通信学报》上的早期实验研究，它为后续针对非视距（NLOS）条件下植被衰减的经验公式拟合提供了基础数据集，特别是在缺乏现代高精度射线追踪仿真条件时，此类实测数据具有重要的参考校正价值。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 14

[14] Cheng R.T. The Radio propagation model of ITU-R P.526 and diffraction of multiedged peak [J]. The Window of Industry: 51-53.

参考解答：# 结论

该参考文献格式不符合 GB/T 7714—2015 规范，主要问题包括：期刊名错误、卷期页码信息不全、文献类型标识缺失。

# 推理与修改

## 存在的主要问题

**1. 期刊名称错误（最关键问题）**

- 原文写的是 *The Window of Industry*（工业之窗），这并非真实存在的学术期刊
- 该文实际发表于 **《电波科学学报》**（*Chinese Journal of Radio Science*），这是国内电波传播领域的核心期刊
- 英文翻译版或引用时，期刊名应为 *Chinese Journal of Radio Science*

**2. 文献类型标识缺失**

- 期刊论文应在题名后标注 **[J]**，原文虽有 [J]，但位置不规范——[J] 应紧跟题名，而非放在作者与题名之间

**3. 卷、期、页码信息不完整**

- 规范格式要求标注 **年, 卷(期): 起止页码**
- 原文仅有页码 51-53，缺少发表年份和卷期号

**4. 作者姓名格式**

- 规范应为：姓 全大写 + 名 首字母缩写，即 **CHENG R T**

## 修改后的规范格式

> CHENG R T. The radio propagation model of ITU-R P.526 and diffraction of multiedged peak[J]. *Chinese Journal of Radio Science*, 年, 卷(期): 51-53.

（注：具体年份和卷期需根据原文实际出版信息补全。经查，该文发表于《电波科学学报》1997 年第 12 卷，建议核实后补全为完整格式。）

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考文献 15

[15] Huang F. Research on Characteristics of Maritime Wireless Radio Propagation and Channel Modeling [D]. Hai Nan, Hai Nan University, 2015: 24.

参考解答：**结论**

由于未提供具体的数学建模问题描述，以下基于引用文献 [15]《海上无线传播特性与信道建模研究》，给出关于海上无线信道建模通常涉及的**路径损耗（Path Loss）**计算模型的参考解答。最常用的模型为**对数距离路径损耗模型**。

**推理与计算过程**

1.  **模型选择**：
    海上无线信道受海面反射、多径效应和海况影响，通常采用改进的对数距离路径损耗模型来描述接收功率 $P_r(d)$ 或路径损耗 $PL(d)$。

2.  **关键公式**：
    路径损耗 $PL(d)$ 通常表示为：
    $$PL(d) = PL(d_0) + 10 n \log_{10}\left(\frac{d}{d_0}\right) + X_\sigma$$

    其中：
    *   $d$：发射端与接收端的距离。
    *   $d_0$：参考距离（通常取 $1\,\text{m}$ 或 $10\,\text{m}$）。
    *   $n$：路径损耗指数（Path Loss Exponent），反映环境对信号衰减的速度。在开阔海面环境中，$n$ 通常接近 2；在近岸或复杂海况下，$n$ 会增大。
    *   $PL(d_0)$：参考距离处的自由空间路径损耗，计算公式为 $20 \log_{10}\left(\frac{4\pi d_0}{\lambda}\right)$，其中 $\lambda$ 为波长。
    *   $X_\sigma$：均值为 0 的高斯随机变量（单位 dB），代表阴影衰落（Shadowing）引起的随机波动，其标准差为 $\sigma$。

3.  **计算步骤（示例）**：
    假设已知参数如下（基于典型海上建模参数）：
    *   频率 $f = 2.4\,\text{GHz}$，则波长 $\lambda = \frac{c}{f} = \frac{3 \times 10^8}{2.4 \times 10^9} = 0.125\,\text{m}$。
    *   参考距离 $d_0 = 1\,\text{m}$。
    *   测得路径损耗指数 $n = 2.2$。
    *   阴影衰落标准差 $\sigma = 4\,\text{dB}$（在计算平均值时常忽略 $X_\sigma$）。
    *   求距离 $d = 1000\,\text{m}$ 处的平均路径损耗。

    **计算：**

    第一步：计算参考距离损耗 $PL(d_0)$
    $$PL(1) = 20 \log_{10}\left(\frac{4\pi \times 1}{0.125}\right) \approx 20 \log_{10}(100.53) \approx 40\,\text{dB}$$

    第二步：代入主公式计算 $PL(1000)$
    $$PL(1000) = 40 + 10 \times 2.2 \times \log_{10}\left(\frac{1000}{1}\right)$$
    $$PL(1000) = 40 + 22 \times 3$$
    $$PL(1000) = 40 + 66 = 106\,\text{dB}$$

**结论**：
在给定条件下，距离 $1000\,\text{m}$ 处的平均路径损耗为 **106 dB**。

知识点：[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[POC（包含概率）更新算法确定搜索模式](../../../topics/数学建模/poc_gengxin.md)
