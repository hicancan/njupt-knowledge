---
title: 《大学物理》同步练习册 第29章 电磁感应（III）（答案）
kind: 答案
course: 大学物理
source: batch-2:大学物理/同步练习册上答案(1).zip/同步练习册答案/29 电磁感应（III）.pdf
---

# 《大学物理》同步练习册 第29章 电磁感应（III）（答案）

原件经识别和整理；“参考解答”是我们补的。

## 电磁感应（III）

### 简答 1

由位移电流密度 $\vec{j}_{D}=\frac{\partial\vec{D}}{\partial t}$，大小 $j_{D}=\frac{\partial D}{\partial t}=\frac{\partial\sigma_{0}}{\partial t}$，且 $j_{D}\cdot S=\frac{\partial\sigma_{0}}{\partial t}S=\frac{\partial(\sigma_{0}S)}{\partial t}=I$。

方向：平板电容器充电时，板上电荷面密度 $\sigma_{0}$ 增加，故两板之间电位移矢量 $D=\sigma_{0}$ 也增加，因此位移电流密度 $\vec{j}_D$ 的方向与电位移矢量 $\vec{D}$ 相同。

对回路 $L_{1}$，有

$$\oint_{L_1}\vec{H}\cdot d\vec{l} = \int_{S_1}\vec{j}_D\cdot d\vec{S} < \int_S\vec{j}_D\cdot d\vec{S} = I;$$

对回路 $L_{2}$，有

$$\oint_{L_2}\vec{H}\cdot d\vec{l} = I$$

所以 $\oint_{L_{1}}\vec{H}\cdot d\vec{l}<\oint_{L_{2}}\vec{H}\cdot d\vec{l}$。

答案：选（C）。

知识点：[安培环路定理及其应用](../../../topics/大学物理/安培环路定理.md)

### 填空 2

位移电流密度的大小 $J_{D}=\frac{\partial D}{\partial t}=\varepsilon_{0}\frac{\partial E}{\partial t}=\varepsilon_{0}\frac{dE}{dt}=8.85\times10^{-11}\ \mathrm{A/m^{2}}$，单位为 $\mathrm{A/m^{2}}$。

知识点：[电通量的概念与静电场的高斯定理](../../../topics/大学物理/电通量与高斯定理.md)、[法拉第电磁感应定律与楞次定律](../../../topics/大学物理/法拉第电磁感应定律.md)

### 填空 3

位移电流密度 $\vec{J}_D = \frac{\partial\vec{D}}{\partial t} = \varepsilon_0\frac{\partial\vec{E}}{\partial t}$，位移电流密度的大小 $J_{D} = \varepsilon_{0}\frac{dE}{dt} = -\frac{\varepsilon_{0}}{RC} E_{0}e^{-\frac{t}{RC}}$，负号表示位移电流密度的方向与场强方向相反。

知识点：[电场强度的定义与叠加原理](../../../topics/大学物理/电场强度.md)、[电介质的极化、电极化强度与有介质时的高斯定理（D矢量）](../../../topics/大学物理/静电场中的电介质.md)

### 简答 4

没有自由电荷，即 $\rho=0$；没有传导电流，即 $J_{C}=0$。由麦克斯韦方程组：

$$
\oint_{L} \vec{H} \cdot d\vec{l} = \int_{S} \left(\vec{J}_{c} + \frac{\partial \vec{D}}{\partial t}\right) \cdot d\vec{S} \quad \Rightarrow \quad \oint_{L} \vec{H} \cdot d\vec{l} = \int_{S} \frac{\partial \vec{D}}{\partial t} \cdot d\vec{S};
$$

$$
\oint_{L} \vec{E} \cdot d\vec{l} = - \int_{S} \frac{\partial \vec{B}}{\partial t} \cdot d\vec{S}.
$$

知识点：[安培环路定理及其应用](../../../topics/大学物理/安培环路定理.md)、[法拉第电磁感应定律与楞次定律](../../../topics/大学物理/法拉第电磁感应定律.md)

### 简答 5

① $\oint_{S} \vec{D} \cdot d\vec{S} = \int_{V} \rho\, dV$ 表示电荷总伴随有电场；

② $\oint_{L}\vec{E}\cdot d\vec{l}=-\int_{S}\frac{\partial\vec{B}}{\partial t}\cdot d\vec{S}$ 表示变化的磁场一定伴随有电场；

③ $\oint_{S}\vec{B}\cdot d\vec{S}=0$ 表示磁感线是闭合曲线，无头无尾；

④ $\oint_{L}\vec{H}\cdot d\vec{l}=\int_{S}\left(\vec{J}_{c}+\frac{\partial\vec{D}}{\partial t}\right)\cdot d\vec{S}$ 表示传导电流和位移电流一定伴随有磁场。

知识点：[电介质的极化、电极化强度与有介质时的高斯定理（D矢量）](../../../topics/大学物理/静电场中的电介质.md)、[法拉第电磁感应定律与楞次定律](../../../topics/大学物理/法拉第电磁感应定律.md)、[磁通量与磁场中的高斯定理](../../../topics/大学物理/磁场中的高斯定理.md)
