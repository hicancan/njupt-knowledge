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

参考解答：
$$
\boxed{J_D=8.85\times10^{-11}\ \mathrm{A/m^2}}
$$

位移电流密度的大小为

$$
J_D=\frac{\partial D}{\partial t}
=\varepsilon_0\frac{\partial E}{\partial t}.
$$

在该题中电场随时间均匀变化，故

$$
\frac{\partial E}{\partial t}=\frac{\Delta E}{\Delta t}=\frac{dE}{dt}.
$$

代入

$$
\varepsilon_0=8.85\times10^{-12}\ \mathrm{F/m},
\qquad
\frac{dE}{dt}=10\ \mathrm{V/(m\cdot s)},
$$

得到

$$
J_D
=8.85\times10^{-12}\times10
=8.85\times10^{-11}\ \mathrm{A/m^2}.
$$

因此应填：

$$
\boxed{8.85\times10^{-11}\ \mathrm{A/m^2}}.
$$

知识点：[电通量的概念与静电场的高斯定理](../../../topics/大学物理/电通量与高斯定理.md)、[法拉第电磁感应定律与楞次定律](../../../topics/大学物理/法拉第电磁感应定律.md)

### 填空 3

位移电流密度 $\vec{J}_D = \frac{\partial\vec{D}}{\partial t} = \varepsilon_0\frac{\partial\vec{E}}{\partial t}$，位移电流密度的大小 $J_{D} = \varepsilon_{0}\frac{dE}{dt} = -\frac{\varepsilon_{0}}{RC} E_{0}e^{-\frac{t}{RC}}$，负号表示位移电流密度的方向与场强方向相反。

参考解答：**结论：**  
位移电流密度大小为  

$$
J_D=\frac{\varepsilon_0 E_0}{RC}e^{-\frac{t}{RC}}
$$

方向与电场方向相反。

**推理过程：**  
已知电场按  

$$
E=E_0 e^{-\frac{t}{RC}}
$$

变化，则位移电流密度  

$$
\vec J_D=\varepsilon_0 \frac{\partial \vec E}{\partial t}
$$

其大小为  

$$
J_D=\varepsilon_0\left|\frac{dE}{dt}\right|
=\varepsilon_0\left|-\frac{E_0}{RC}e^{-\frac{t}{RC}}\right|
=\frac{\varepsilon_0 E_0}{RC}e^{-\frac{t}{RC}}
$$

负号表示方向与电场方向相反。

知识点：[电场强度的定义与叠加原理](../../../topics/大学物理/电场强度.md)、[电介质的极化、电极化强度与有介质时的高斯定理（D矢量）](../../../topics/大学物理/静电场中的电介质.md)

### 简答 4

没有自由电荷，即 $\rho=0$；没有传导电流，即 $J_{C}=0$。由麦克斯韦方程组：

$$
\oint_{L} \vec{H} \cdot d\vec{l} = \int_{S} \left(\vec{J}_{c} + \frac{\partial \vec{D}}{\partial t}\right) \cdot d\vec{S} \quad \Rightarrow \quad \oint_{L} \vec{H} \cdot d\vec{l} = \int_{S} \frac{\partial \vec{D}}{\partial t} \cdot d\vec{S};
$$

$$
\oint_{L} \vec{E} \cdot d\vec{l} = - \int_{S} \frac{\partial \vec{B}}{\partial t} \cdot d\vec{S}.
$$

参考解答：**结论**

在无自由电荷（$\rho=0$）且无传导电流（$\vec{J}_C=0$）的介质中，变化的电场产生磁场，变化的磁场产生电场。电场 $\vec{E}$ 与磁场 $\vec{H}$（或 $\vec{B}$）相互激发，形成统一的电磁场，并以波的形式在空间中传播（即电磁波）。

**推理过程**

1.  **安培-麦克斯韦定律分析**：
    由方程 $\oint_{L} \vec{H} \cdot d\vec{l} = \int_{S} \frac{\partial \vec{D}}{\partial t} \cdot d\vec{S}$ 可知，即使没有传导电流 $\vec{J}_C$，只要电位移矢量 $\vec{D}$ 随时间变化（即存在位移电流 $\frac{\partial \vec{D}}{\partial t}$），就会在周围空间激发涡旋磁场 $\vec{H}$。

2.  **法拉第电磁感应定律分析**：
    由方程 $\oint_{L} \vec{E} \cdot d\vec{l} = - \int_{S} \frac{\partial \vec{B}}{\partial t} \cdot d\vec{S}$ 可知，只要磁感应强度 $\vec{B}$ 随时间变化，就会在周围空间激发涡旋电场 $\vec{E}$。

3.  **场的耦合与传播**：
    *   变化的 $\vec{E}$ 产生变化的 $\vec{B}$；
    *   变化的 $\vec{B}$ 又产生变化的 $\vec{E}$；
    *   这种电场和磁场的交替激发使得电磁扰动不再局限于源附近，而是脱离源向远处传播，形成电磁波。

4.  **补充说明（高斯定律）**：
    虽然题目未列出，但在 $\rho=0$ 时，$\oint \vec{D} \cdot d\vec{S} = 0$ 和 $\oint \vec{B} \cdot d\vec{S} = 0$ 表明电磁波是横波（在均匀各向同性介质中），且电场线和磁感线是闭合的或延伸至无穷远，无源头。

知识点：[安培环路定理及其应用](../../../topics/大学物理/安培环路定理.md)、[法拉第电磁感应定律与楞次定律](../../../topics/大学物理/法拉第电磁感应定律.md)

### 简答 5

① $\oint_{S} \vec{D} \cdot d\vec{S} = \int_{V} \rho\, dV$ 表示电荷总伴随有电场；

② $\oint_{L}\vec{E}\cdot d\vec{l}=-\int_{S}\frac{\partial\vec{B}}{\partial t}\cdot d\vec{S}$ 表示变化的磁场一定伴随有电场；

③ $\oint_{S}\vec{B}\cdot d\vec{S}=0$ 表示磁感线是闭合曲线，无头无尾；

④ $\oint_{L}\vec{H}\cdot d\vec{l}=\int_{S}\left(\vec{J}_{c}+\frac{\partial\vec{D}}{\partial t}\right)\cdot d\vec{S}$ 表示传导电流和位移电流一定伴随有磁场。

参考解答：- **结论**：四个说法均正确。

- **①**：高斯定理 $\oint_{S} \vec{D} \cdot d\vec{S} = \int_{V} \rho\, dV$ 表明通过任意闭合曲面的电位移通量等于该面内包围的自由电荷代数和，即电荷是电场的通量源，故“电荷总伴随有电场”成立。

- **②**：法拉第电磁感应定律的积分形式 $\oint_{L}\vec{E}\cdot d\vec{l}=-\int_{S}\frac{\partial\vec{B}}{\partial t}\cdot d\vec{S}$ 表明随时间变化的磁场会在空间中激发涡旋电场，故“变化的磁场一定伴随有电场”成立。

- **③**：磁场的高斯定理 $\oint_{S}\vec{B}\cdot d\vec{S}=0$ 表明磁感线无源头也无尾闾，只能是无头无尾的闭合曲线（或来自无穷远并去向无穷远），故说法成立。

- **④**：安培–麦克斯韦定律 $\oint_{L}\vec{H}\cdot d\vec{l}=\int_{S}\left(\vec{J}_{c}+\frac{\partial\vec{D}}{\partial t}\right)\cdot d\vec{S}$ 表明传导电流 $\vec{J}_c$ 与位移电流 $\partial \vec{D}/\partial t$ 都是磁场的涡旋源，故“传导电流和位移电流一定伴随有磁场”成立。

知识点：[电介质的极化、电极化强度与有介质时的高斯定理（D矢量）](../../../topics/大学物理/静电场中的电介质.md)、[法拉第电磁感应定律与楞次定律](../../../topics/大学物理/法拉第电磁感应定律.md)、[磁通量与磁场中的高斯定理](../../../topics/大学物理/磁场中的高斯定理.md)
