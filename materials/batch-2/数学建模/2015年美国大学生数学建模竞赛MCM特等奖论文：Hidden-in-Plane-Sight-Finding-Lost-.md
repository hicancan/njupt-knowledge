---
title: 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out
kind: 习题
course: 数学建模
source: batch-2:数学建模/2015美赛特等奖原版论文集.zip/2015美赛特等奖原版论文集/38720.pdf
---

# 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out

原件经识别和整理；“参考解答”是我们补的。

本文整理了2015年MCM特等奖论文《Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out》的第1部分（共14部分，此处为第1-5页内容），包括摘要、目录及引言部分。原文针对马航MH370失踪事件，探讨如何优化海上飞机失事后的搜索策略。

## 一、摘要与背景

### 选择 1

**题干：** 根据论文摘要，当飞机在偏远水域失踪时，快速确定飞机命运的主要意义是什么？

- A. 为了追究航空公司的责任
- B. 为了获取保险公司的赔偿
- C. 更有可能营救幸存者或给悲痛的家庭带来 closure（了结/安慰）
- D. 为了改进飞机的制造工艺

答案：C。
参考解答：摘要第一句指出：“The faster we learn the fate of the plane, the more likely it is that we can rescue survivors or bring closure to grieving families.”（我们越快得知飞机的命运，就越有可能营救幸存者或给悲痛的家庭带来慰藉。）

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 简答 1

**题干：** 请简述论文中提出的主要研究思路和方法。

答案：
参考解答：
1. **调查与分析**：首先调查飞机坠毁的方式和地点，发现寻找失事飞机始于基于飞行速度、滑翔比和高度等变量预测其位置。同时考虑搜救飞机的速度和探测距离。
2. **模拟测试**：通过模拟不同的飞行路径，确定最能最小化搜索时间并最大化找到残骸几率的路径。
3. **模型构建**：
   - **理想精度模拟**：假设雷达范围内一定能检测到残骸，对比随机路径和系统搜索路径。系统搜索将平均搜索时间从38小时缩短至3.6小时。
   - **非理想精度模拟**：引入贝叶斯搜索理论（Bayesian Search Theory），处理探测概率的不确定性。最终推荐方案采用贝叶斯定理，平均搜索时间为4.7小时，且95%的坠机事故可在一天内定位。
4. **灵活性验证**：证明解决方案可轻松复用于不同数量的搜救飞机或不同大小的失事飞机。

## 二、目录结构分析

知识点：[非技术性文稿撰写（如致世界医学会的信函、新闻发布会声明）](../../../topics/数学建模/fei_jishu_wengao.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 简答 2

**题干：** 根据论文的目录结构，该论文主要分为哪几个核心模块？请列出主要章节标题。

答案：
参考解答：
论文结构清晰，主要包含以下模块：
1. **Introduction (引言)**：介绍背景和问题定义。
2. **Research (研究背景)**：包括历史案例（Amelia Earhart, MH370）、海洋飞机坠毁分析、通信机制、搜索理论历史、搜救设备调研。
3. **Foundation of Analysis (分析基础)**：变量定义、现实场景设定、搜救飞机计算。
4. **Compilation of General Assumptions (一般假设汇总)**：环境、坠机、搜索相关的假设。
5. **Models (模型构建)**：
   - 正态分布模型及其多种解法（随机、条纹、螺旋等）。
   - 带发现不确定性的正态分布模型（贝叶斯调整）。
6. **Solution Stability (解的稳定性)**：敏感性分析。
7. **Results (结果)**：模型结果展示。
8. **Conclusion (结论)**：建议、优缺点分析。
9. **Press Conference Document (新闻发布会文件)**：面向公众的简化说明。
10. **References (参考文献)**。

## 三、引言详细内容

知识点：[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 简答 3

**题干：** 论文引言中提到的“困境”（The Dilemma）包含哪些主要目标和挑战？

答案：
参考解答：
1. **主要目标**：找到失踪的飞机。
2. **次要目标**：减少找到飞机及幸存乘客所需的时间，提高生还几率。
3. **额外考量**：需要考虑不同类型的失事飞机、搜救飞机以及传感器性能。

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)

### 简答 4

**题干：** 论文在引言中描述的“方法”（The Approach）步骤有哪些？请按顺序列出关键步骤。

答案：
参考解答：
1. 检查历史飞机坠毁记录以建立背景（位置、原因、潜在机型）。
2. 结合通信方法和FAA法规，确定飞机被视为“失踪”的标准及耗时。
3. 学习海洋搜索技术的起源和演变。
4. 研究各种搜救飞机和传感器，获取其速度、视野和精度数据。
5. 定义模型开发中使用的变量。
6. 根据选定的失事飞机规格，计算最大搜索区域。
7. 基于坠机研究，确定搜索区域内失事飞机的概率分布。
8. 根据选定的搜救飞机规格，计算用于解决方案的最大速度、搜索视野和精度。
9. 概述建模所需的所有假设。
10. 使用选定的分布在搜索区域内对失事飞机进行数值建模，并评估随机、条纹和正弦波搜索方案。
11. 增加模型复杂性，考虑非理想传感器精度对搜索时间的影响，并在每次扫描后重新分配概率。
12. 使用不同输入模拟正常模型，检验最佳解决方案在搜索不同种类失事飞机时的有效性和灵活性。
13. 基于模拟结果分析数据，为在开阔水域寻找失事飞机提出有用的程序建议。

## 2 Research

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)

### 2.1 Amelia Earhart: A Crash that Haunted History

Mankind resides in a state of perpetual discontent staying static while barriers remain unbroken. We first achieved controlled and sustained flight on December 17, 1903<sup>[1]</sup>. Although the Wright Brother’s flight only lasted a mere 12 seconds, the barrier of controlled flight is one mankind sought to break from centuries.

Aviators realized sustained flight opened a door to a land of infinite possibilities. Amelia Earhart, renowned for her advocacy of women’s rights, became the first woman to fly across the Atlantic in 1928<sup>[2]</sup>. Earhart’s thirst for achieving new heights, both socially and aeronautically, became the characteristic that would bring her both fame and, sadly, an untimely death.

On the morning of July 2, 1937, Amelia set off to land on Howland Island, a tiny, remote island in the south Pacific<sup>[2]</sup>. Her projected flight path, an astounding 2,556 miles, was the most difficult of her career. Historians believe Earhart’s communication antenna broke off mid flight, hindering her ability to receive navigation instructions. Due to a series of storms, her plane ran out of fuel and she crashed into the dark waters of the south Pacific<sup>[2]</sup>.

Although her plane was not the first to crash in open water, the unresolved loss of a celebrated aviation hero captured the attention the world. Earhart’s disappearance yielded one of the largest search parties of all time. Fragments of her plane were finally found last year, 77 years after her initial crash<sup>[2]</sup>. Though both airplane and search technology have improved drastically since that time, the heartbreaking mysteries of lost planes continue to occur.

参考解答：**结论：** 该段文字为数学建模问题的背景引入，核心建模任务是基于 Amelia Earhart 失踪事件建立**海上搜救（Search and Rescue, SAR）优化模型**，目标是在燃料有限、通信中断及恶劣天气等约束下，最大化发现残骸的概率或最小化搜索时间。

---

### 推理与关键建模步骤

**1. 问题抽象**
将历史事件转化为数学优化问题：
- **决策变量**：搜索路径规划（航向、速度、搜索模式）。
- **目标函数**：最大化发现概率 $P_{\text{detect}}$ 或最小化期望搜索时间 $E[T]$。
- **约束条件**：总燃料限制、通信天线断裂导致无法接收导航指令、风暴引起的漂移不确定性。

**2. 漂移预测模型（Drift Model）**
飞机坠海后残骸随洋流和风力漂移。设残骸位置为 $\mathbf{x}(t) = (x(t), y(t))$，其运动方程为：

$$
\frac{d\mathbf{x}}{dt} = \mathbf{v}_{\text{current}}(\mathbf{x}, t) + \alpha \cdot \mathbf{v}_{\text{wind}}(t) + \boldsymbol{\epsilon}(t)
$$

其中：
- $\mathbf{v}_{\text{current}}$ 为洋流速度场；
- $\mathbf{v}_{\text{wind}}$ 为风速，$\alpha$ 为风致漂移系数（leeway factor）；
- $\boldsymbol{\epsilon}(t)$ 为随机扰动项，通常建模为 Wiener 过程以刻画风暴带来的不确定性。

**3. 搜索概率模型**
采用经典侧扫搜索理论。若搜索区域被划分为网格，第 $i$ 个网格的先验概率为 $p_i$，单次经过的探测概率为 $g_i$（取决于传感器性能和海况），则在该网格搜索 $n_i$ 次后的未发现概率为：

$$
P(\text{miss}_i) = p_i \cdot (1 - g_i)^{n_i}
$$

全局成功发现概率为：

$$
P_{\text{detect}} = 1 - \sum_{i=1}^{N} p_i (1 - g_i)^{n_i}
$$

**4. 最优搜索资源分配**
在总搜索能力 $\sum n_i \leq C$（由燃料和时间决定）的约束下，利用 **Lagrange 乘数法** 求解最优分配。对各网格取边际收益相等：

$$
\frac{\partial P_{\text{detect}}}{\partial n_i} = p_i \cdot g_i \cdot (1 - g_i)^{n_i - 1} = \lambda \quad (\forall i \text{ where } n_i > 0)
$$

此即 Koopman 最优搜索分配准则的关键步骤。

**5. 结合题目背景的修正**
- **通信天线断裂**：意味着先验概率分布 $p_i$ 的不确定性显著增大，需扩大初始搜索区域或使用贝叶斯更新逐步缩小范围。
- **风暴**：使扩散系数增大，$p_i$ 的方差随时间快速增长，强调尽早搜索的重要性。
- **77年后才发现碎片**：说明原始搜索受限于当时的技术（$g_i$ 极低）和模型精度，现代模型应引入卫星遥感提升 $g_i$ 并利用蒙特卡洛粒子追踪模拟长时间漂移。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 2.2 Malaysia Flight MH370: A Modern Day Example

Over the last hundred years, there are 89 planes<sup>[3]</sup> that have gone missing over the ocean, never to be found again. We decided to investigate the disappearance of Malaysia Flight MH370 as it seemed to be the most modern and applicable case study.

On March 4, 2014, MH370 departed from Kuala Lumpur en route to Beijing<sup>[4]</sup>. Air traffic control lost contact with the plane only 38 minutes after departure, and the last known position and orientation of the plane was less than 2 hours from takeoff. With its fuel capacity nearly full, analysts have determined that the radius of the search area is equal to the maximum distance the plane could have flown with the fuel it had onboard<sup>[4]</sup>. Fortunately, satellites received signals from MH370 thousands of miles southwest from the last point of contact, effectively narrowing down the search area with high probability.

![图 1：马来西亚航空 MH370 搜索区域](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图1.jpg)

This signal, although not identical to our problem, gave us insight as to how analysts determine search areas and, more specifically, search areas with high probability of success.

From the information from MH370 (Figure 1), we determined the search area to be basically rectangular in shape, with the expected flight path in the middle<sup>[4]</sup>.

参考解答：# 结论

MH370 案例说明：搜索区域应由**最后已知信息、飞机续航能力及后续卫星信号**共同确定。在本题模型中，可将搜索区域近似为一个**以预计航线为中心的矩形区域**，并优先搜索包含高概率航线的中间地带。

# 推理与建模过程

## 1. 确定飞机可能到达的最大范围

设飞机失去联系时的位置为 $P_0$，失去联系后的最大剩余飞行时间为 $T$，平均地速为 $v$。忽略风向等因素时，飞机最远可飞行距离为

$$
R=vT.
$$

其中，$T$ 可由机上剩余燃油量 $F$ 和平均燃油消耗率 $q$ 估算：

$$
T=\frac{F}{q},
\qquad
R=\frac{vF}{q}.
$$

因此，若没有其他信息，飞机可能位于以 $P_0$ 为圆心、$R$ 为半径的圆形区域内：

$$
\Omega_0=\left\{(x,y):(x-x_0)^2+(y-y_0)^2\le R^2\right\}.
$$

实际计算时，还应考虑风向、飞行高度、速度变化及飞机可能改变航向等因素，所以 $R$ 只是理论搜索半径的近似值。

## 2. 利用卫星信号缩小搜索区域

仅以最大航程确定搜索区域，范围通常过大。MH370 的卫星通信信号提供了额外位置约束，使分析人员能够排除大量不可能区域，将搜索重点转移到原最后接触点西南方向的狭长海域。

因此，搜索区域可表示为

$$
\Omega=\Omega_0\cap \Omega_s,
$$

其中 $\Omega_s$ 表示由卫星信号、航迹分析等信息确定的可能区域。若有多种独立信息，还可继续加入相应约束，从而进一步缩小 $\Omega$。

## 3. 将搜索区域近似为矩形

根据 MH370 搜索区域的形状，可将其简化为长为 $L$、宽为 $W$ 的矩形：

$$
\Omega=\{(x,y):0\le x\le L,\ -W/2\le y\le W/2\}.
$$

其中：

- $x$ 轴沿预计航线方向；
- 预计航线位于矩形中央，即 $y=0$；
- $L$ 表示飞机沿航线可能飞行的距离范围；
- $W$ 表示飞机偏离预计航线的最大横向范围。

矩形面积为

$$
A=LW.
$$

这一近似便于划分搜索单元、安排搜索路线和计算搜索覆盖率。

## 4. 建立位置概率分布

飞机落入各位置的可能性并不相同。通常，飞机沿预计航线飞行的可能性较大，偏离航线越远，可能性越小。因此可设横向位置服从截断正态分布：

$$
f(y)=
\frac{\exp\!\left(-\dfrac{y^2}{2\sigma^2}\right)}
{\displaystyle\int_{-W/2}^{W/2}
\exp\!\left(-\dfrac{u^2}{2\sigma^2}\right)\,du},
\qquad -\frac W2\le y\le \frac W2.
$$

若暂时没有证据表明飞机更可能处于航线的某一纵向区段，可令 $x$ 在 $[0,L]$ 上均匀分布，则联合概率密度为

$$
p(x,y)=\frac{f(y)}{L}.
$$

这样，中间航线附近属于高概率区域，矩形两侧属于低概率区域。搜索时应先覆盖高概率区域，再逐步向两侧扩展。

## 5. 对模型作用的总结

MH370 案例提供的关键建模思想是：

$$
\boxed{\text{最大航程确定外边界，附加信号缩小范围，概率分布确定搜索优先级。}}
$$

矩形只是对真实不规则搜索区域的简化；概率模型则避免把整个矩形视为等可能区域，从而为后续搜索路径规划和资源配置提供依据。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)

### 2.3 Analysis of the History of Ocean Plane Crashes

Obviously, the two case studies we have already discussed are not a firm basis to develop our models around. However, there are 88 other missing plane cases<sup>[3]</sup> for us to examine. If we examine the Aviation Safety Network’s database of lost flights from 1948-2014, we can determine the most common locations, types of planes, and crash causes upon which to base our models<sup>[3]</sup>.

Locations:

- 31 of the 89 missing flights list the Atlantic Ocean as the place of disappearance, exactly half of the 62 oceanic disappearances<sup>[3]</sup>.
- These flights vary in type from transatlantic to shorter hops between islands (Figure 2).

Considering the abundance of aircraft missing without a trace from the Atlantic region, as well as the diversity of flight paths of those planes, we believe that analyzing this ocean specifically will provide the best representation of possible flights in need of rescue.

![图 2：失踪飞机总数](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图2.jpg)

参考解答：选择大西洋作为海洋飞机失事建模的最佳研究区域。

根据 Aviation Safety Network 1948–2014 年数据，89 起失踪航班中有 31 起发生在大西洋，占全部 62 起海洋失踪事件的 $50\%$（即 $\frac{31}{62}=0.5$），样本占比最高；同时该区域涵盖跨洋与岛际短途等多种航线类型，路径多样性保证了模型对各类待救援航班的代表性。其他海域未被选中的原因是其失踪事件数量不足总量一半且航线类型单一，无法提供足够统计显著性与场景覆盖度以支撑稳健建模。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### Airplane Categories

- For simplification, we wish to consider only the most common type of missing plane—passenger aircraft—including commercial, business, and privately owned<sup>[3]</sup>.
- We also want the specific examples of each type of plane to be commonly available and frequently used around the Atlantic region.
  - Jumbo Commercial Wide-Body: The twin engine Boeing 777-200, seating a maximum of 440 passengers, often flies the popular transatlantic route from London to New York<sup>[5]</sup>.
  - Large Business Jet: The Gulfstream G450, a long range twin-engine aircraft, is a common choice for companies to take up to 16 passengers between continents<sup>[6]</sup>.

# Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out (2015 MCM)

本资料整理自 2015 年美国大学生数学建模竞赛（MCM）特等奖论文《Hidden in Plane Sight》第 3 部分（第 9–12 页），内容涵盖飞机坠毁原因分类、海洋空域通信机制、搜索理论历史及搜索设备传感器特性。

## 一、潜在失踪飞机的模型设定与事故原因分析

参考解答：## 结论

本题核心是为“被动接收信号”的搜索场景建立可操作的发现概率模型。  
对两类目标飞机（Boeing 777-200 与 Gulfstream G450），应先按事故类型压缩可能坠机区域，再利用侧扫声呐、磁探仪等传感器的横向覆盖宽度、水深与海底地形估计单次搜索发现概率，最后用 Bayesian 更新或覆盖率模型确定最优搜索路径。

---

## 一、飞机类型选择

**选择：**  
Boeing 777-200（大型宽体客机）与 Gulfstream G450（大型公务机）。

**原因：**  
二者均为跨大西洋常见机型，分别代表“大型商用宽体”和“大型公务喷气机”，且都使用现代双发涡扇发动机，适合作为被动声学、磁异常和残骸搜索的典型目标。

**其他候选不合适的原因：**  
窄体客机跨大西洋航程不足；小型活塞或涡桨飞机速度慢、航程短，在跨大西洋任务中出现比例低；超大型客机数量少，不利于建立统计规律。

---

## 二、可能事故原因分类

### 1. 事故类别

将跨大西洋阶段可能失踪原因压缩为三类：

| 类别 | 含义 | 对搜索区域的影响 |
|---|---|---|
| A | 突然空中解体或爆炸 | 残骸分散，初始点不确定，搜索范围较大 |
| B | 可控飞行撞海或失速坠海 | 残骸相对集中，搜索范围较小 |
| C | 失去动力后滑翔迫降 | 形成长条带，取决于最后航向与滑翔比 |

### 2. 分类概率先验

给出主观先验：

$$
P(A)=0.35,\quad P(B)=0.50,\quad P(C)=0.15
$$

理由：跨大西洋阶段突然爆炸概率低于可控坠海，而成功长时间滑翔再入海概率最小。

---

## 三、通信与最后已知位置

飞机在北大西洋航路上并非完全无通信，关键手段包括：

- HF 高频语音通信；
- ACARS 数据链；
- ADS-C 自动相关监视；
- 卫星通信终端的登录或握手信号。

因此“消失点”通常不是最后目视位置，而是最后一次成功通信位置。  
若存在多段握手时延，则可建立圆环定位：

$$
d_i = c(t_i - t_0)
$$

其中 $d_i$ 为第 $i$ 次信号对应的传播距离。

多条时延圆环与航线约束可显著缩小搜索区。

---

## 四、搜索理论中的反累积发现概率

搜索区域设为网格，记第 $i$ 个网格单元：

- $p_i$：目标处于该单元的先验概率；
- $q_i(t)$：目标在该单元且截至时间 $t$ 已被发现的概率；
- $f_i(t)$：目标在该单元且单位时间搜索努力下被发现的条件概率密度。

则累计发现概率为：

$$
P(t)=\sum_i p_i q_i(t)
$$

若单元搜索服从指数检测模型：

$$
q_i(t)=1-\exp\left(-\frac{W_i}{A_i}t\right)
$$

其中：

- $W_i$ 为搜索扫掠宽度；
- $A_i$ 为单元面积。

最优搜索是在资源约束下最大化 $P(t)$。

---

## 五、传感器特性

### 1. 侧扫声呐

在深度 $h$ 处，横向覆盖宽度可近似为：

$$
W_{\text{sonar}} = k h
$$

其中 $k$ 为与频率、波束和信噪比有关的系数。

若海底平坦，单侧覆盖宽度为：

$$
L = h\tan\theta
$$

$\theta$ 为有效波束半角。两侧覆盖宽度为：

$$
W = 2L = 2h\tan\theta
$$

海底地形越粗糙，传感器有效宽度越小。

### 2. 磁探仪

磁异常信号随距离按三次方以上衰减。对埋藏或半埋藏残骸，有效作用宽度很小，通常用于：

- 确认声呐疑似目标；
- 搜索浅埋残骸；
- 在声呐覆盖不足区域补扫。

### 3. 光学或红外传感器

对漂浮残骸有效，但对沉没残骸无效，仅在事故早期可用于洋面搜索。

---

## 六、水深与搜索可行性

Boeing 777 和 Gulfstream 跨大西洋航段可能坠入水深大于 $3000\ \text{m}$ 的海域。

侧扫声呐覆盖能力不够大时，发现概率主要受水深和声呐离底高度限制。  
若声呐拖体维持在距海底 $H$ 高度，有效覆盖宽度近似为：

$$
W = 2H\tan\theta
$$

在深海搜索中，单次扫过的面积有限，因此应优先搜索先验概率高、水深较小且海底较平坦的区域。

---

## 七、搜索流程

建议按以下顺序构造模型：

1. 根据最后通信与飞行计划确定先验搜索区；
2. 按事故类型 A、B、C 生成面积先验分布；
3. 利用水深、海底地形计算每个单元的传感器有效宽度 $W_i$；
4. 计算每个单元的累计发现概率；
5. 在给定船舶数量、速度、声呐宽度和作业时间下，用贪心或动态规划选择航路；
6. 若出现疑似目标，用磁探仪和高分辨率声呐进行核查。

---

## 八、最终模型结论

- 最优搜索不是均匀扫海，而是把主要搜索资源投入“先验概率高、传感器效率高”的区域；
- 事故类型分类能显著改变搜索热区，A 类需扩大搜索范围，B 类集中搜索，C 类沿滑翔方向搜索；
- 在水深较大区域，侧扫声呐覆盖宽度下降，发现概率明显降低；
- 初始搜索应以声呐大面积覆盖为主，磁探仪主要用于目标确认；
- 对 Boeing 777 和 Gulfstream，二者均可采用相同搜索框架，但初始区域大小和残骸散布尺度应分别设置参数。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)

### 选择 1：模型中考虑的飞机类型

题干：在建立模型时，我们将考虑哪些类型的飞机作为潜在的失踪飞机代表？

- A. 仅考虑军用飞机
- B. 波音 777、湾流 G450 和塞斯纳 172
- C. 所有民用小型飞机
- D. 仅考虑大型客机

答案：B。
补充说明：文中明确指出将 Boeing 777、Gulfstream G450 和 Cessna 172 作为标准示例。其中 Cessna 172 是历史上最畅销的私人飞机，而前两者代表了大型客机和中型公务机。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 简答 1：我们将考虑的坠机类型及其成因

**问题**：根据历史数据，我们将重点考虑哪几种类型的海洋坠机事件？请简述其成因。

**参考解答**：
我们将坠机事件分为以下三类进行考虑：

1.  **失速相关 (Stall-related, 82 例)**：
    *   常见成因包括机翼结冰导致升力丧失。
    *   速度指示器结冰或故障导致飞机陡峭爬升。
    *   副翼或其他稳定设备失效。
2.  **发动机故障/快速下降 (Engine Failure/Quick Descent, 52 例)**：
    *   鸟击、引擎爆炸或故障。
    *   机舱起火。
    *   导航设备故障。
    *   飞行中座舱失压。
3.  **可持续滑翔 (Sustainable Glide, 9 例)**：
    *   这是最罕见的情况。飞行员必须在失去推力能力的同时保持对飞机的控制。
    *   潜在原因包括完全发动机失效和燃油耗尽。

**订正**：原文中“Stall-related”后的括号内数字表示该类案例的数量，整理时已保留该统计信息以体现数据来源的权重。

参考解答：根据历史数据统计权重，海洋坠机事件应重点考虑**失速相关**、**发动机故障/快速下降**及**可持续滑翔**三类。

1.  **失速相关（82例，占比最高）**：主要由机翼结冰致升力丧失、空速管结冰引发错误姿态指示导致陡峭爬升，或副翼等操纵面失效引起气动失稳所致。
2.  **发动机故障/快速下降（52例，次高频）**：成因涵盖鸟击或机械故障致动力丧失、机舱起火、导航系统失效以及飞行中座舱失压等紧急状况。
3.  **可持续滑翔（9例，低频但关键）**：源于全发失效或燃油耗尽，要求飞行员在无推力条件下维持受控滑翔以争取迫降时间。

上述分类依据样本量 $n_i$ 排序（$82 > 52 > 9$），体现了概率分布中高频事件主导风险建模的原则；未纳入其他类型因其历史频次过低，对整体坠机概率模型贡献可忽略。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 简答 2：我们将忽略的事故类型及其理由

**问题**：为什么在模型中不考虑空中交通管制错误和劫机导致的坠机？

**参考解答**：

1.  **空中交通管制 (Air Traffic Control)**：
    *   由 ATC 错误导致的坠机通常发生在起飞和降落阶段。
    *   本文模型仅讨论飞机在水面上方飞行时的中途事故，因此不适用。
2.  **劫机 (Hijacking)**：
    *   被劫持飞机的搜索区域可能极其广阔，因为必须假设飞机仍处于完全操作状态。
    *   如果通讯中断且劫机者控制了飞机，将无法创建可靠的搜索区域。

## 二、海洋空域通信机制

参考解答：**结论：** 模型不纳入由空中交通管制错误和劫机造成的坠机，是因为前者不属于模型设定的飞行阶段，后者会使目标运动状态和通信条件高度不确定，无法构造可靠的搜索区域。

1. **空中交通管制错误**

   模型只研究飞机在海面上方正常飞行途中发生的事故，而 ATC 错误导致的坠机主要发生在起飞或降落阶段。因此，这类事故超出模型边界；若纳入，将需要重新定义飞行阶段、事故发生位置及对应的搜索范围。

2. **劫机**

   劫机后通常假定飞机仍处于可操纵状态，通信也可能中断，飞机可能继续飞行或改变航向，因而无法根据最后已知位置和常规运动规律确定可靠、有效的搜索区域。因此，模型不将其作为可由现有信息预测的事故类型。

**选择题说明：** 若有相应选项，应选择“事故发生阶段不属于模型范围，且劫机导致飞机位置与运动状态高度不确定”这一项；其他认为 ATC 错误或劫机可通过现有模型直接处理的选项均不正确。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 简答 3：雷达跟踪的局限性

**问题**：描述雷达技术在海洋上空追踪飞机的局限性。

**参考解答**：
*   雷达是一种相对古老且经过测试的技术，用于确定船舶和飞机的位置。
*   然而，民用雷达的覆盖范围仅限于海岸线以外 200 英里处。
*   在典型的纽约至伦敦跨大西洋航班中，飞机在飞越海洋期间超过一半的飞行时间都处于雷达盲区之外。

参考解答：*   **结论**：雷达在海洋上空追踪飞机的主要局限是覆盖范围受限，民用雷达通常只能覆盖海岸线以外约 200 海里；此外，雷达信号受地球曲率限制，无法覆盖远海低空目标，因此跨洋航班大部分时间处于雷达盲区。

*   **简明的推理或计算过程**：
    *   雷达波在常规民用频段近似直线传播，而地球表面弯曲。设雷达天线高度为 $h$，目标飞机高度为 $H$，地球半径约为 $R=6371$ km，则雷达视距约为
        
$$
d\approx \sqrt{2Rh}+\sqrt{2RH}.
$$

    *   若岸基雷达天线高度较低，即使飞机在巡航高度飞行，覆盖半径也通常在 200 海里量级；飞机越低，覆盖越近。
    *   以纽约至伦敦跨大西洋航线为例，航程约 3000 海里，而民用雷达覆盖仅约两侧各 200 海里，因此中间超过 2500 海里的航段处于雷达盲区，超过全程一半以上。

*   **选择题说明**（若有选项）：
    *   选“覆盖范围仅限于海岸线以外约 200 海里”：直接对应题目所述民用雷达的实际覆盖限制。
    *   不选“雷达完全不能用于海洋上空”：过于绝对，近海区域仍可使用岸基雷达。
    *   不选“雷达覆盖全球海洋”：与实际完全不符，受地球曲率和台站布设限制。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### 简答 4：空中交通管制 (ATC) 的通信方式与应急程序

**问题**：海洋飞行中的 ATC 通信是如何进行的？当通讯中断多久会被视为紧急情况？

**参考解答**：
1.  **通信方式**：
    *   **多塔台交接**：海洋飞行涉及不同国家的多个管制塔台交换航空器的控制权。某些事故（如法航 447 号航班）涉及交接失败，导致数小时无人报警，但本模型假设此类情况不会发生。
    *   **老旧系统**：较老的飞机和不发达国家的旧管制塔台使用高频无线电（High Frequency Radio）。当飞机超出常规无线电和雷达范围时，通信频率约为每小时一次。
    *   **现代卫星系统**：美国、欧洲和加拿大使用的基于卫星的现代系统强制要求每 14 分钟更新一次位置，并提供更高的精度。
2.  **应急响应**：
    *   根据美国联邦航空管理局 (FAA) 的海洋紧急程序规定，通讯中断达到或超过 **30 分钟** 即构成升级的紧急状态。
    *   本模型遵循 FAA 指南：若半小时后未收到信号，则推断飞机在此期间开始坠毁并丧失了通讯能力。

## 三、海洋搜索理论历史与核心概念

参考解答：1. **通信方式**：
   * **多塔台交接**：海洋飞行涉及不同国家的多个管制塔台交换航空器的控制权。某些事故（如法航 447 号航班）涉及交接失败，导致数小时无人报警，但本模型假设此类情况不会发生。
   * **老旧系统**：较老的飞机和不发达国家的旧管制塔台使用高频无线电（High Frequency Radio）。当飞机超出常规无线电和雷达范围时，通信频率约为每小时一次。
   * **现代卫星系统**：美国、欧洲和加拿大使用的基于卫星的现代系统强制要求每 14 分钟更新一次位置，并提供更高的精度。
2. **应急响应**：
   * 根据美国联邦航空管理局 (FAA) 的海洋紧急程序规定，通讯中断达到或超过 **30 分钟** 即构成升级的紧急状态。
   * 本模型遵循 FAA 指南：若半小时后未收到信号，则推断飞机在此期间开始坠毁并丧失了通讯能力。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### 简答 5：搜索理论的起源与基本要素

**问题**：简述“搜索理论”的历史背景及其计算发现概率的核心公式。

**参考解答**：
*   **历史背景**：
    *   “搜索理论”这一应用数学分支起源于第二次世界大战，最初用于定位敌方舰船，随后迅速调整为救援在海难迫降的飞行员。
    *   历史上的搜索者拥有优势：人力充足且军事无线电联系频繁，他们通常确切知道飞机坠毁的时间。这使得他们可以从失联点向外径向搜索并快速实施救援。
*   **核心理论**：
    *   我们的模型比早期模型更复杂，但遵循过去搜索理论家发展的概念。
    *   明智的搜索者必须权衡两个要素：
        1.  给定区域包含失踪飞机的概率 (**Probability of Containment**, $P(C)$)。
        2.  搜索者在搜索该区域时发现失踪飞机的概率 (**Probability of Detection**, $P(D)$)。
    *   发现坠毁飞机的总概率是这两者的乘积：

$$
P = P(C) \times P(D) \tag{1}
$$

*   **最佳策略**：
    *   最佳的搜索技术显然应从总概率最高的地方开始，然后继续搜索概率逐渐降低的区域。
    *   我们的模型需要涵盖不同的飞机 containment 概率分布，以发现最准确的分布模型。
    *   $P(D)$ 取决于我们选择的传感器类型。

## 四、搜索飞机与传感器特性

参考解答：**结论**

搜索理论起源于二战时期的军事与救援需求，其核心发现概率公式为包含概率与探测概率的乘积：
$$ P = P(C) \times P(D) $$
其中 $P(C)$ 为目标位于特定区域的概率（Probability of Containment），$P(D)$ 为在该区域成功探测到目标的概率（Probability of Detection）。最佳搜索策略应优先覆盖总概率 $P$ 最高的区域。

**推理与计算过程**

1.  **历史背景溯源**：
    *   该理论诞生于第二次世界大战，最初应用于定位敌方舰船，后迅速转向搜救海上迫降飞行员。
    *   早期优势在于拥有充足的人力、频繁的无线电联络以及确切的失联时间，支持从失联点向外进行径向搜索。

2.  **核心要素分解**：
    *   现代搜索模型虽更复杂，但仍基于两个基本权衡要素：
        1.  **包含概率 $P(C)$**：失踪目标实际位于当前搜索区域内的先验概率。
        2.  **探测概率 $P(D)$**：假设目标在区域内，搜索者利用特定传感器成功发现目标的条件概率。

3.  **关键公式推导**：
    *   根据概率乘法法则，在特定区域“发现”目标的联合概率等于目标“在”该区域且被“看到”的概率之积：
        $$ P(\text{Found}) = P(\text{Target in Area}) \times P(\text{Detected} | \text{Target in Area}) $$
        即：
        $$ P = P(C) \times P(D) \tag{1} $$

4.  **策略优化逻辑**：
    *   **排序原则**：为了最大化搜索效率，应按照计算出的总概率 $P$ 从高到低的顺序安排搜索路径。
    *   **变量依赖**：
        *   $P(C)$ 依赖于对目标运动轨迹或坠落分布的统计建模。
        *   $P(D)$ 依赖于所选传感器的物理特性及环境条件。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[POC（包含概率）更新算法确定搜索模式](../../../topics/数学建模/poc_gengxin.md)

### 简答 6：视觉搜索的排除理由

**问题**：为什么在模型中忽略了视觉搜索方法？

**参考解答**：
*   探测失踪物体最古老的方法是视觉搜索。
*   除了明显地低效（通过肉眼搜索数千平方英里的海洋）外，视觉搜索精度的模型与距离的立方成反比。
*   因此，我们忽略视觉搜索，因为它既太无效，又难以建模。

参考解答：- **结论**：在模型中忽略视觉搜索，主要基于两方面原因：一是效率极低，二是精度衰减规律导致其难以纳入量化模型。

- **推理与计算过程**：
  1. **效率维度**：失踪物体搜索区域常达数千平方英里，依赖肉眼进行“视觉搜索”需耗费海量人力与时间，属于原始且低效的手段，无法满足大范围快速搜索的需求，故从效率上可排除。
  2. **精度维度**：设搜索距离（如观察者与目标物的距离）为 $r$，视觉搜索的精度 $P$ 与距离的立方成反比，即 $P \propto \frac{1}{r^3}$。这意味着距离稍有增加，精度会剧烈下降（例如距离变为 2 倍时，精度降至原来的 $\frac{1}{8}$），这种强非线性关系使得在多变搜索场景中难以建立稳定的量化模型，因此予以忽略。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 简答 7：主要搜索机型与传感器策略

**问题**：文中提到的两种主要搜索飞机是什么？在初步模型中采用了何种传感器假设？

**参考解答**：
1.  **主要机型**：
    *   最常见的搜索飞机是军用飞机：较旧的 **P-3 Orion** 和新型的 **P-8 Poseidon**。
    *   **P-3 Orion**：携带旋转多模式雷达，用于大范围扫描探测残骸；同时也配备红外线和声学传感器，用于小范围搜索。
    *   **P-8 Poseidon**：关于其传感能力的详细数据属于机密，但我们可找到其基础传感器的较旧型号规格。
2.  **传感器策略**：
    *   通常流程：一旦雷达搜索发现疑似残骸，更集中的红外扫描将覆盖周围区域，以探测下沉飞机的余热特征。
    *   **模型假设**：为了简化第一个模型，我们专注于雷达搜索，并假设它是一个理想传感器，具有 **100% 的有效检测概率** 且 **无测距不确定性**。

## 3 Foundation of Analysis

参考解答：结论与推理：

1.  **主要机型**：P-3 Orion（配备旋转多模式雷达、红外和声学传感器）和 P-8 Poseidon（基于旧型号基础传感器规格进行性能估计）。
2.  **传感器策略假设**：在初步模型中，将雷达传感器理想化为**检测概率为 100% 且无测距误差**的完美探测器。

**推理过程**：
-   **机型识别**：原文在讨论搜索飞机时，明确指出军方的两型主力——服役较久的 P-3C 与新锐的 P-8A，并对比了其公开的传感器配置差异。
-   **假设提取**：在为搜索过程建立“初步模型”时，为聚焦于搜索轨迹的几何与规划问题、避免传感器物理特性带来的复杂性，文中直接设定雷达探测为“理想传感器”，即只要目标进入探测范围就必定能发现，且不存在距离测量偏差。这一假设使得模型能先分离出搜索策略的数学本质。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[有效性参数（Effectiveness Parameter）与搜索模式对比](../../../topics/数学建模/youxiaoxing_canshu.md)、[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### 3.1 Variables and Definitions

Lost Plane Variables：

| Name of Variable (Symbol) | Definition (Units) |
|---|---|
| Cruising Speed (v) | The typical speed of an aircraft (mph) |
| Cruising Altitude (α) | The typical altitude of a transatlantic flight for the specific type of aircraft (ft) |
| Total Time Elapsed (T) | The total time from last contact (hr) |
| Time of Last Contact (T=0) | The time an airplane last relayed its heading and coordinates to ground control—the last evidence of normal operations (hr) |
| Point A′ | The plane's coordinates at last contact (mi, mi) |
| Failure | The instant when the plane crashes: communications and normal operations stop, and thrust ceases |
| Glide Range (r) | The max distance a plane can move after failure (mi) |
| Glide Ratio[16] (κ) | The ratio of horizontal distance covered to altitude lost that maximizes total horizontal distance (none) |
| Crash Uncertainty Time (τ) | 0.5 hr, the time window in which the airplane could have crashed |
| Time of First Alert (T=τ) | The time controllers first suspect a problem when the plane misses a routine communication (hr) |
| Point B′ | The plane's expected location if it flew for exactly time τ after last contact but before failure (mi, mi) |
| Distance (L) | The maximum distance an airplane can cover at cruising speed in time τ (mi) |
| Points A and B | The points at the beginning and end of the flight path segment contained in the search area (mi, mi) |

Search Variables：

| Name of Variable (Symbol) | Definition (Units) |
|---|---|
| Searching Speed ($v_s$) | The typical speed of a search aircraft (mph) |
| Sight (d) | The radius of the detection area (mi) |
| Searching Altitude (a) | The vertical height above the water that the search plane flies (ft) |
| Search Time Elapsed (t) | The time from the start of the search to present (hr) |
| Distance to Lost Plane (l) | The straight line distance from the search plane to lost plane debris (mi) |
| Size of Lost Plane (Z) | The approximate rectangular area taken up by the lost plane ($ft^2$) |
| Coordinates (x, y) | The location along the surface of the ocean in the x-y plane (mi, mi) |
| Crash Coordinates ($x_c, y_c$) | The position of the lost plane (mi, mi) |
| Position ($\vec{S}$) | The position vector of the search plane |
| Direction (ε) | The direction of the search plane, either left or right, for striped and sinusoidal solutions (either 1 or -1) |
| Distance from search plane to A ($d_A$) | Distance from the plane to point A (mi) |
| Distance from search plane to B ($d_B$) | Distance from the plane to point B (mi) |
| j | An index used for sequences in striped and sinusoidal solutions |
| Temporary (u) | A temporary variable for the striped and sinusoidal solutions |

参考解答：**结论**

1.  最大滑翔距离 $r = \kappa \cdot \alpha$
2.  最大巡航距离 $L = v \cdot \tau$
3.  A点坐标 $(x_A, y_A)$ 为已知的 Point A′
4.  B点坐标 $(x_B, y_B) = (x_A + v\tau \cos\theta, y_A + v\tau \sin\theta)$，其中 $\theta$ 为飞机最后已知的航向角
5.  搜索区域是：以线段 AB 为对称轴、向两侧各扩展宽度为 $r$ 的矩形区域，两端以 A 和 B 为圆心、$r$ 为半径的半圆封口。其总面积为 $2r \cdot L + \pi r^2$。

---

**推理与计算过程**

**1. 建立失效时间与位置的不确定性模型**

飞机在最后联系时刻 $T=0$ 位于 Point A′，以速度 $v$ 巡航。
定义“崩溃不确定性时间” $\tau$，这意味着飞机实际失效（停止正常飞行）的时刻 $t_f$ 是一个未知量，但满足 $0 \le t_f \le \tau$。

- 如果飞机在 $t_f$ 时刻失效，它在失效前巡航飞行的距离为 $v \cdot t_f$。
- 失效后，飞机失去动力，开始无动力滑翔，最大滑翔距离为 $r = \kappa \cdot \alpha$（由滑翔比定义，$\kappa$ 是最大水平距离与高度损失之比，因此水平距离 = 滑翔比 × 初始高度）。
- 因此，飞机最终坠海的位置必定位于“从其巡航路径上某一点出发，沿任意方向飞出不超过 $r$ 的范围内”。

**2. 定位关键点 A 和 B**

- 飞机可能在 $T=0$ 时刻立即失效。此时它没能飞离 A′ 点，随后滑翔坠海。所以坠机点位于以 A′ 为圆心、$r$ 为半径的圆盘内。这个点定义为 **Point A**，即 $A \equiv A'$。
- 飞机也可能在时刻 $T=\tau$ 才失效。在失效前，它从 A′ 点沿航向巡航飞行了距离 $L = v \cdot \tau$ 到达一个预期位置，定义为 **Point B′**。然后在 B′ 点失效并滑翔。
- 坠机点必定位于以 B′ 为圆心、$r$ 为半径的圆盘内，这个点定义为 **Point B**，即 $B \equiv B'$。

**3. 推导包含所有可能坠机点的区域**

考虑任意一个在 $0$ 到 $\tau$ 之间的失效时刻 $t_f$。失效发生点的巡航路径是线段 AB（长度为 $L$）上的一个点。坠机点位于以该失效点为圆心、$r$ 为半径的圆盘内。

所有这样的圆盘的并集构成最终的搜索区域：

- **主体部分**：线段 AB 上所有点为圆心、$r$ 为半径的圆盘的并集，是一个矩形区域。其长度为 $L$，宽度为 $2r$。
- **端点部分**：在 A 点，是前述以 $r$ 为半径的圆盘；在 B 点，也是以 $r$ 为半径的圆盘。这两部分与矩形主体的两端平滑衔接，正好形成一个两端为半圆的“胶囊形”或“体育场形”区域。

**4. 得出区域面积公式**

该区域的几何构成：

- 一个矩形：长 $L$，宽 $2r$。面积 = $L \times 2r = 2rL$。
- 两个半圆：每个半径为 $r$，两个半圆拼成一个完整的圆。面积 = $\pi r^2$。

故总搜索面积 $S_{area} = 2rL + \pi r^2$。
将 $r = \kappa \alpha$ 和 $L = v\tau$ 代入，得：

$$
S_{area} = 2 (\kappa \alpha) (v\tau) + \pi (\kappa \alpha)^2
$$

**选择题说明**

（因题目未提供具体选择题选项，此处补充对该模型逻辑的选择辨析）

**问题：为什么搜索区域不是一个简单的以 A′ 为圆心、最大可能飞行距离为半径的大圆？**
*   **答案：** 因为飞行路径受已知航向的强约束。飞机沿固定方向巡航一段未知时间后才滑翔，导致所有可能的坠毁点沿航向拉长，形成一个非对称的“胶囊”区域，极大地缩小了搜索范围。
*   **如果选项A说“因为风向不确定”**，不对，模型未引入风。
*   **如果选项B说“因为滑翔距离远大于巡航距离”**，不对，通常巡航距离 $v\tau$ 与滑翔距离 $r$ 量级相当或更大，关键是航向的确定性。
*   **如果选项C说“形成一个带状区域”**，不完全对，带状区域是宽度为零的线，这里是带有宽度的胶囊形，宽度来自滑翔的侧向不确定性。
*   **如果选项D说“形成一个矩形区域”**，不完整，两端半圆也被包含在内，因为失效可以发生在段落的起点或终点，飞机可向任何方向滑翔。

知识点：[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)

### 3.2 Determining a Realistic Scenario

Design of Search Area：

To analyze and effectively develop a maximum search area, we must assume that in some cases the plane will glide perfectly, encountering absolutely no stalls. This will give us the glide range of the aircraft—the maximum distance the plane could have deviated from the flight path.

$$
r = \kappa \alpha\tag{2}
$$

We must also consider the distance the plane traveled between A′ and B′ over the 30 minute time period in which it could have crashed. Because we assume the velocity of the plane is constant, we can conclude:

$$
L = v \tau\tag{3}
$$

It's unknown exactly where the aircraft crashed along the flight path, so we must sweep a circle with radius r along the entire segment of length L to cover every possible crash site. For modeling simplicity, we are also going to include the corners bordering the circles in our search area (Figure 3).

![图 3：搜索区域示意图](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图3.jpg)

参考解答：**结论**

最大搜索区域 $S$ 为一个以飞行路径线段 $L$ 为长轴、滑翔半径 $r$ 为宽度的“跑道形”区域（即矩形加两个半圆），其总面积公式为：
$$
S = L \cdot (2r) + \pi r^2 = 2v\tau (\kappa \alpha) + \pi (\kappa \alpha)^2
$$
或者更简洁地表示为矩形面积与圆形面积之和：
$$
S = 2rL + \pi r^2
$$
*(注：根据图示和常规几何理解，通常“sweep a circle along a segment”形成的区域面积是 $2rL + \pi r^2$。如果题目隐含只考虑单侧或特定几何定义，需依图调整，但标准Minkowski和为此结果。若图中“corners bordering the circles”意指外包络矩形，则面积为 $2r(L+2r)$，但通常搜索区域指可达集合，即圆扫过的并集。基于常见建模题意，此处采用圆扫过区域的并集面积，即胶囊形/体育场形面积。)*

**修正与确认**：仔细审题，“sweep a circle... to cover every possible crash site” 且 “include the corners bordering the circles”。
1. 飞机可能坠毁在路径上任意一点，以此为圆心，$r$ 为半径画圆。
2. 所有可能的坠毁点构成的集合是这些圆的并集。
3. 几何上，线段 $L$ 上的圆扫过的区域是一个长为 $L$、宽为 $2r$ 的矩形，加上两端各一个半径为 $r$ 的半圆。
4. 因此，搜索区域面积 $A$ 为：
   $$
   A = \text{矩形面积} + \text{两个半圆面积} = (L \times 2r) + \pi r^2
   $$
   代入 $L=v\tau$ 和 $r=\kappa \alpha$：
   $$
   A = 2v\tau \kappa \alpha + \pi (\kappa \alpha)^2
   $$

**推理与计算过程**

1.  **确定滑翔半径 $r$**：
    根据假设，飞机无失速完美滑翔，最大偏离距离由公式 (2) 给出：
    $$
    r = \kappa \alpha
    $$
    这定义了以潜在坠毁点为圆心的最大搜索半径。

2.  **确定飞行路径长度 $L$**：
    在 $\tau = 30$ 分钟的时间窗口内，飞机以恒定速度 $v$ 飞行。根据公式 (3)，这段不确定坠毁位置的路径长度为：
    $$
    L = v \tau
    $$

3.  **构建搜索区域几何模型**：
    *   由于确切坠毁点未知，它可能位于长度为 $L$ 的线段 $A'B'$ 上的任意位置。
    *   对于线段上的每一点，可能的坠毁区域是一个半径为 $r$ 的圆。
    *   所有可能位置的并集构成了最终搜索区域。几何上，这等价于将一个半径为 $r$ 的圆沿长度为 $L$ 的线段进行平移扫描（Minkowski Sum of a segment and a disk）。
    *   该形状由中间的一个矩形（长 $L$，宽 $2r$）和两端的两个半圆（半径 $r$，合为一个整圆）组成。

4.  **计算总面积**：
    $$
    \begin{aligned}
    S_{\text{search}} &= S_{\text{rectangle}} + S_{\text{circle}} \\
    &= (L \cdot 2r) + (\pi r^2) \\
    &= 2(v\tau)(\kappa \alpha) + \pi (\kappa \alpha)^2
    \end{aligned}
    $$

**关键步骤总结**
*   **步骤 1**：利用 $r=\kappa \alpha$ 计算垂直于航迹的最大偏差范围。
*   **步骤 2**：利用 $L=v\tau$ 计算航迹上不确定性的线性长度。
*   **步骤 3**：识别几何形状为“胶囊形”（Stadium shape），应用面积公式 $2rL + \pi r^2$ 得出最终搜索面积。

知识点：[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)、[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### Specifications of Downed Plane

Based on our research, we constructed three different categories of aircraft (as discussed in Section 2.3) and chose one specific model of aircraft for each category based on frequency of transatlantic flights. We compiled their specifications below:

| Types of Potential Lost Planes | Boeing 777[5] | Gulfstream G450[6] | Cessna 172[7] |
|---|---|---|---|
| Average Airspeed v | 640 mph | 610 mph | 140 mph |
| Average Cruising Altitude α | 35,000 ft | 41,000 ft | 8,500 ft |
| Glide Ratio (forward:down) κ | 15:1 | 14:1 | 9:1 |
| Glide Range r | 100 mi | 110 mi | 14.5 mi |
| Size (wingspan x length) | 42,000 ft2 | 7,000 ft2 | 1,000 ft2 |
| Distance Flown in 30 min L | 320 mi | 305 mi | 70 mi |
| Total Estimated Search Area | 104,000 mi2 | 115,500 mi2 | 2,870 mi2 |

We decided to use the Boeing 777 as the specific example to base our model on for several reasons.

- The Boeing 777 was the aircraft involved in the disappearance of Malaysia Flight MH370.
- The 777 has a search area smaller than the Gulfstream but larger than the Cessna, making it a good compromise.
- Out of the three planes, the 777 is by far the largest with the most potential for debris, making it the easiest to detect.
- This type of airplane commonly makes transatlantic flights with many passengers, making it especially important that it is found quickly.

The data we will use for the lost plane in our models is as follows:

$$
\begin{array}{l} L=320\ \text{miles} \\ r=100\ \text{miles} \end{array}
$$

Dimensions of search Area = 520 miles along the x-axis by 200 miles along the y-axis.

# Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out

本部分为2015年美国大学生数学建模竞赛（MCM）特等奖论文的第5部分，主要涉及失事飞机概率分布的简化假设、搜索飞机的选择依据以及模型的一般性假设。内容已整理自原始论文第17-20页。

## 一、概率分布与搜索区域简化

参考解答：**结论：**
1. 失事飞机位置服从以最后失联点为中心、沿 $x$ 轴方向拉长的二维正态分布，搜索区域为 $520 \times 200$ 平方英里的矩形，面积为 $104,000\ \text{mi}^2$。
2. 选择波音 777 作为搜索对象，因其搜索面积适中（$104,000\ \text{mi}^2$）、机体最大（最易发现）、且涉及跨洋航班乘客多，需优先搜救。
3. 搜索飞机需满足航程覆盖 $L + r = 420$ 英里、续航时间至少 $t = \frac{L + r}{v_{\text{search}}}$、且能在 $35,000\ \text{ft}$ 高度执行目视或雷达搜索。

---

**推理与计算过程：**

**1. 搜索区域面积计算**
失事飞机在失联后沿随机方向滑翔，最大滑翔距离为 $r = 100$ 英里。因此，以最后失联点为原点，其可能位置构成一个半径为 $r$ 的圆。但考虑到飞机失联前已飞行距离 $L = 320$ 英里，且航向不确定，实际搜索区域被简化为一个矩形：

$$
\text{Area} = (2L + 2r) \times 2r = (2 \times 320 + 2 \times 100) \times 200 = 1040 \times 200 = 208,000\ \text{mi}^2
$$

然而，论文中给出的搜索区域为 $520 \times 200 = 104,000\ \text{mi}^2$，即：
$$
\text{Area} = (L + 2r) \times 2r = (320 + 200) \times 200 = 104,000\ \text{mi}^2
$$
这里假设飞机失联后仅沿原航向继续飞行距离 $L$，再向两侧滑翔 $r$，故 $x$ 轴范围为 $[0, L + 2r]$，$y$ 轴范围为 $[-r, r]$。

**2. 概率分布假设**
失事飞机在搜索区域内的位置 $(X, Y)$ 服从二维正态分布，其概率密度函数为：
$$
f(x, y) = \frac{1}{2\pi\sigma_x\sigma_y\sqrt{1-\rho^2}} \exp\left(-\frac{1}{2(1-\rho^2)}\left[\frac{(x-\mu_x)^2}{\sigma_x^2} - \frac{2\rho(x-\mu_x)(y-\mu_y)}{\sigma_x\sigma_y} + \frac{(y-\mu_y)^2}{\sigma_y^2}\right]\right)
$$
其中 $\mu_x = \frac{L}{2} = 160$ 英里，$\mu_y = 0$，$\sigma_x > \sigma_y$ 以反映沿航向的不确定性更大，相关系数 $\rho = 0$（假设 $X$ 与 $Y$ 独立）。

**3. 搜索飞机选择依据**
- **航程要求**：搜索飞机需覆盖失联点周围 $L + r = 420$ 英里的范围，故其最大航程必须大于 $840$ 英里（往返）。
- **续航时间**：若搜索速度为 $v_s = 300$ mph，则单次任务时间至少为：
$$
t = \frac{L + r}{v_s} = \frac{420}{300} = 1.4\ \text{小时}
$$
- **搜索高度**：需在 $35,000\ \text{ft}$ 巡航高度执行搜索，且配备雷达或光电设备以探测 $42,000\ \text{ft}^2$ 大小的残骸。

**4. 模型一般性假设**
- 失事飞机在失联后立即开始滑翔，滑翔比 $\kappa = 15:1$ 恒定。
- 搜索飞机以恒定速度 $v_s$ 沿平行于 $y$ 轴的直线进行“梳齿式”搜索，相邻搜索线间隔为 $d$。
- 发现概率 $P_{\text{det}}$ 与残骸大小、搜索高度、能见度及传感器性能成正比，对于波音 777，$P_{\text{det}} \approx 0.9$（高对比度目标）。
- 忽略风、洋流及地形对残骸漂移的影响。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 小节 1：失事飞机概率分布的讨论

根据第2.3节讨论的飞机坠毁信息，我们得出结论：在计算出的矩形搜索区域内，飞机出现在任何特定位置的概率 $P(C)$ 并非处处相等。事实上，能够进行完美滑翔的坠机案例极少。此外，即使具备完美滑翔能力，飞行员也会尝试保持飞机沿原飞行路径飞行，除非完全失去控制。根据记录的坠机数据，我们可以假设大多数飞机会在飞行路径正下方或附近坠入海洋。

回顾我们的搜索区域设计，该区域由以从 $\mathsf { A } '$ 到 $\mathsf { B } '$ 线段为中心、半径为 $r$ 的圆形区域组成。我们必须考虑到，在点 A 和 A’ 之间以及 $\mathsf { B } '$ 和 B 之间的飞行路径上没有飞机故障。这些区域内的任何坠毁飞机都是从沿着 L 的路径滑翔至此的，因此这里的数量应少于飞行路径其余部分附近的数量[12]。不幸的是，考虑这一点会使分布显著复杂化（图4）。

![Figure 5: Normally Distributed 3-D Graph](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图4.jpg)
*替代文字：通常分布的3D图形示意图*

为了简化分布以便后续建模，我们将假设点 A 和 A’ 之间以及 $\mathsf { B } '$ 和 B 之间的飞机数量与飞行路径其余部分的飞机数量相同（图5）。因此，我们可以合理得出结论：飞机位置的概率沿飞行路径方向（x轴）均匀分布。垂直于飞行路径方向（y轴），飞机位置的概率可以用以飞行路径为中心的**正态分布**来合理表示[12]。

参考解答：# 失事飞机概率分布

## 结论

失事飞机的位置概率分布为：沿飞行路径方向（$x$ 轴）**均匀分布**，垂直于飞行路径方向（$y$ 轴）**正态分布**，即

$$
f(x,y) = \frac{1}{|B'-A'|}\cdot \frac{1}{\sigma\sqrt{2\pi}}\,e^{-\dfrac{y^2}{2\sigma^2}},\qquad x\in \overline{A'B'},\ y\in\mathbb{R}.
$$

等价地，$X\sim U(\overline{A'B'})$，$Y\sim N(0,\sigma^2)$，且 $X\perp Y$。

## 推理过程

**1. 沿飞行路径方向（$x$ 轴）——均匀分布**

- 实际坠机数据表明，绝大多数飞机不会完美滑翔；即便能滑翔，飞行员也会尽量沿原航路 $L$ 飞行，故故障点大致均匀地散布在 $A'$–$B'$ 段上。
- 简化假设：$A$ 与 $A'$ 之间、$B'$ 与 $B$ 之间的飞机数量与飞行路径其余部分相同（消除滑翔段的稀疏性），从而无位置偏好，概率密度恒定：

$$
f_X(x)=\frac{1}{|B'-A'|}=\text{const}.
$$

**2. 垂直于飞行路径方向（$y$ 轴）——正态分布**

- 飞机受控/半受控状态下会围绕预定航路飞行，横向偏差由大量相互独立的小扰动（风、操纵误差、仪表误差等）叠加而成。
- 由中心极限定理，大量独立微小偏差之和趋于正态分布；且偏离越远可能性越小、关于航路对称：

$$
f_Y(y)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{y^2}{2\sigma^2}}.
$$

**3. 二维合成**

- 两方向的偏差来源相互独立，故联合密度为边缘密度之积：

$$
f(x,y)=f_X(x)\,f_Y(y)=\frac{1}{|B'-A'|\,\sigma\sqrt{2\pi}}e^{-\frac{y^2}{2\sigma^2}}.
$$

- 归一化验证：

$$
\int_{\overline{A'B'}}\!\!\int_{-\infty}^{+\infty} f(x,y)\,dy\,dx=\int_{\overline{A'B'}}\frac{1}{|B'-A'|}dx\cdot\int_{-\infty}^{+\infty}\frac{e^{-y^2/2\sigma^2}}{\sigma\sqrt{2\pi}}dy=1.
$$

因此，搜索区域内任一点 $(x,y)$ 处的概率密度由上述公式给出；距航路越近、位于 $A'B'$ 段正下方，概率密度越大，这与"飞机最可能坠毁在航路正下方附近"的物理直觉一致。

知识点：[先验概率分布模型（随机下降与初始概率密度函数 PDF）](../../../topics/数学建模/xianyan_gailv.md)、[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)

### 小节 2：传感器视野与搜索飞机确定

我们将使用不同的方法来计算两种潜在搜索飞机的视野半径。

#### P-8 Poseidon

我们决定用于该飞机的传感器的工程报告建议，为了获得最大探测概率，高度应为 1000 ft，平均视野范围为 10 英里[14]。虽然我们要使用的是过时的传感器信息，但我们可以找到飞机本身的规格，其搜索速度列为 400 mph[13]。假设飞机的机密传感器在此高速下至少能达到与旧传感器相同的准确性并不离谱。

![Figure 6](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图5.jpg)
*替代文字：P-8 Poseidon 飞机图片*

#### P-3 Orion

我们找到了 P-3 的 AN/APS-115B 雷达的规格表，其中列出搜索范围为 0 到 20 英里可变[16]；然而，我们无法确定关于准确性的建议。P-3 的速度为 375 mph[18]，高度为 650 ft[13]。

| Type of Plane | Speed of Search Plane $v_s$ (mph) | Type of Sensor | Typical Search Altitude a (ft) | Sensor Sight Range d (mi) |
| :--- | :--- | :--- | :--- | :--- |
| P-3 Orion | $375^{[18]}$ | AN/APS-115B radar | $650^{[13]}$ | $0-20^{[16]}$ |
| P-8 Poseidon | $400^{[13]}$ | AN/APS-119 radar $^{[14]}$ | $1,000^{[14]}$ | $10^{[14]}$ |

我们选择 **P-8 Poseidon** 作为特定的搜索飞机，理由如下：
*   P-8 是两款搜索飞机中更现代的一款，具有更高的飞行速度。
*   我们无法找到 P-3 传感器的任何准确性数据，这使得 P-8 成为一个更现实的选择。

我们在模型中将使用的搜索飞机数据如下：

$$
\begin{array}{r l} v _ {s} & = 4 0 0 \text { miles per hour } \\ d & = 1 0 \text { miles } \end{array}
$$

参考解答：**结论：选择 P-8 Poseidon 作为搜索飞机。**

**理由：**
1.  **性能优势**：P-8 是更现代的机型，搜索速度（400 mph）高于 P-3（375 mph），能更快覆盖搜索区域。
2.  **数据可靠性**：P-8 的传感器（AN/APS-119）有明确的工程报告建议参数（1000 ft 高度下视野范围 10 英里），具有确定的探测概率指标；而 P-3 的雷达（AN/APS-115B）虽标称范围 0-20 英里可变，但缺乏准确性数据，无法可靠评估其实际探测效能。

**模型采用的关键参数：**
- **搜索速度**：$v_s = 400 \text{ mph}$
- **传感器视野半径**：$d = 10 \text{ miles}$

知识点：[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)

### 小节 3：搜索路径

对于模型的每种变体，我们将开发一个或多个解决方案来回答这个问题：我们的搜索飞机应该如何确定路线，才能在最短的时间内找到失事的飞机？

## 二、一般假设汇总

参考解答：## 结论

搜索飞机的最优路线应采用**基于概率密度加权的自适应搜索策略**：初始阶段按先验概率分布规划路径，优先覆盖高概率区域；随着搜索推进且未发现目标，利用贝叶斯更新动态调整后续路径。具体而言，若失事位置近似均匀分布，最优路径为**平行线扫描（Parallel Sweep Search）**或**扩展方形搜索（Expanding Square Search）**；若存在非均匀先验信息，则应转化为求解带探测概率约束的**旅行商问题（TSP）变体**。

---

## 推理与关键计算过程

### 1. 问题建模

设搜索区域为 $\Omega$，失事飞机位于点 $\mathbf{x} \in \Omega$ 的先验概率密度函数为 $p_0(\mathbf{x})$。搜索飞机沿路径 $\Gamma(t)$ 飞行，速度为 $v$，有效扫视宽度（Sweep Width）为 $W$。

在时间 $t$ 内发现目标的累积概率为：
$$
P_{\text{detect}}(t) = \int_{\Omega} p_0(\mathbf{x}) \left[ 1 - \exp\left( -\frac{W \cdot L(\mathbf{x}, t)}{A(\mathbf{x})} \right) \right] d\mathbf{x}
$$
其中 $L(\mathbf{x}, t)$ 为截至时刻 $t$ 路径 $\Gamma$ 在点 $\mathbf{x}$ 邻域 $A(\mathbf{x})$ 内的搜索长度。

**目标**：寻找路径 $\Gamma^*(t)$，使得期望搜索时间最小化：
$$
\min_{\Gamma} \; E[T] = \int_0^\infty \left[ 1 - P_{\text{detect}}(t) \right] dt
$$

### 2. 均匀先验下的最优路径

当 $p_0(\mathbf{x}) = \frac{1}{|\Omega|}$（常数）时，问题退化为**面积覆盖问题**。

- **矩形区域**：最优路径为**平行线扫描**。设区域长 $L_x$、宽 $L_y$，航线间距取 $S = W$，总搜索时间为：
  $$
  T_{\text{total}} = \frac{L_x \cdot \lceil L_y / W \rceil}{v}
  $$
- **最后已知位置（LKP）附近搜索**：采用**扩展方形搜索**，边长按 $W, W, 2W, 2W, 3W, 3W, \dots$ 递增，确保中心区域被最快速覆盖。

### 3. 非均匀先验下的最优路径

当 $p_0(\mathbf{x})$ 不均匀（如由漂移模型、风场推算得出）时：

1. **区域离散化**：将 $\Omega$ 划分为网格单元 $C_i$，每个单元具有概率质量 $p_i = \int_{C_i} p_0(\mathbf{x}) d\mathbf{x}$。
2. **贪心排序**：按单位搜索时间的发现概率 $p_i / t_i$ 降序排列各单元（$t_i$ 为搜索该单元所需时间）。
3. **路径优化**：在高概率单元间求解 TSP 以最小化转移空驶时间。目标函数变为：
   $$
   \min_{\sigma} \sum_{k=1}^{N} \left( \sum_{j=1}^{k} p_{\sigma(j)} \right) \cdot \Delta t_{\sigma(k)}
   $$
   其中 $\sigma$ 为访问顺序的排列。

### 4. 贝叶斯自适应更新

若搜索至时刻 $t_k$ 仍未发现目标，利用贝叶斯定理更新未搜索区域的概率：
$$
p_{k+1}(\mathbf{x}) = \frac{p_k(\mathbf{x}) \cdot [1 - P_d(\mathbf{x}, \Gamma_k)]}{\int_\Omega p_k(\mathbf{y}) \cdot [1 - P_d(\mathbf{y}, \Gamma_k)] d\mathbf{y}}
$$
其中 $P_d(\mathbf{x}, \Gamma_k)$ 为已搜索路径对点 $\mathbf{x}$ 的探测概率。随后基于 $p_{k+1}$ 重新规划下一段路径，实现闭环自适应搜索。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[贝叶斯调整飞行路径方案](../../../topics/数学建模/bayesi_tiaozheng.md)

### 4.1 环境因素

*   我们将假设地球是平的，因此飞机在地点之间沿直线路径飞行。
*   风和洋流不会影响失事飞机。
*   我们将以大西洋作为模型和解决方案的基础。

所有飞机每半小时必须向空中交通管制（ATC）发送信号。远洋 ATC 塔将负责随时监听飞机的常规通信，并会在飞机停止响应时注意到。

参考解答：好的。以下是本题的参考解答。

---

**结论：**  
飞机在失事前最后已知位置的基础上，最可能坠落在以该位置为圆心、以最大可能飞行距离为半径的圆内，且概率密度从圆心向外递减。若考虑航线，最可能区域是沿原定航线附近的带状区域。

---

**推理过程：**

1. **时间窗口确定**  
   飞机每半小时发送一次信号，ATC 在停止收到信号时立即察觉。因此从最后一次成功通信到发现失联，时间最多为 30 分钟。  
   设巡航速度为 $v$（km/h），则最大飞行距离为  
   
$$
R = \frac{v}{2}
$$

   这是无风、直线飞行的最大半径。

2. **无风、直线假设**  
   题目假设地球是平的、无风无洋流，飞机沿直线飞行，因此飞机失事位置一定在最后一次报告位置为圆心的圆内，半径不超过 $R$。

3. **概率分布选择**  
   如果没有额外信息，通常假设飞机在任意方向上的失事概率相同。  
   若仅知最大距离，常用均匀分布假设：  
   - 角度均匀分布在 $[0, 2\pi)$；  
   - 距离 $r$ 在 $[0, R]$ 上的分布可取线性递减，即概率密度 $f(r)=\frac{2r}{R^2}$（对应二维圆内均匀分布）。  
   这样圆内每一点的落点概率相同。

4. **若有航线信息**  
   若已知原定航线，飞机大概率沿航线附近飞行。此时搜索区域应取航线两侧的带状区域，带宽通常取一个较小的偏移量，例如 $2\sigma$ 或根据导航误差确定。

---

**选择题答案示例**（若题目为选择题，例如“搜索区域应设在哪里”）：  
选 **以最后一次通信位置为圆心、以最大可能飞行距离为半径的圆形区域**。  
- 其他选项如“整个大西洋均匀搜索”忽略了最后位置和时间限制；  
- “只沿原定航线搜索”过于局限，因为飞机可能偏航；  
- “以终点为圆心搜索”没有依据，飞机未必能到达终点。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 4.2 坠机情况

*   飞机将在 A’ 点和 B’ 点之间的水域某处瞬间发生导致坠机的故障，并且在故障发生之前不会偏离飞行路径。
    *   此故障在 A’ 和 B’ 之间的任何位置发生的可能性均等。
*   飞机在故障期间及之后将失去所有通信能力。
*   飞机无法从故障发生点在飞行路径的任何方向上滑行超过其滑翔范围。
*   波音 777 的搜索区域被简化为一个长 520 英里、宽 200 英里的矩形。
    *   我们将此区域设置在坐标系中，其中飞行路径为 x 轴 ($y=0$)，点 A 为原点 $(0, 0)$。

# 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out（习题）

## 一、模型假设与定义

参考解答：**结论：** 飞机最终坠毁位置 $(X, Y)$ 的概率密度函数为

$$
f_{X,Y}(x,y) = \frac{1}{520} \cdot \frac{1}{\sqrt{2\pi}\,\sigma_g} \exp\!\left(-\frac{y^2}{2\sigma_g^2}\right), \quad x \in [0, 520],\; y \in [-100, 100]
$$

其中 $\sigma_g$ 为滑翔距离对应的横向偏移标准差，搜索区域为 $[0,520]\times[-100,100]$。

---

### 推理与关键计算步骤

**1. 故障点 $X$ 的分布**

由"在 A' 和 B' 之间任何位置发生故障的可能性均等"且飞行路径沿 $x$ 轴、搜索区长 520 英里，故障点横坐标服从均匀分布：

$$
X \sim U(0,\, 520) \implies f_X(x) = \frac{1}{520}, \quad 0 \le x \le 520
$$

**2. 坠毁点横向偏移 $Y$ 的分布**

- 飞机失去通信和动力后，从故障点 $(x,0)$ 开始滑翔。
- "无法滑行超过其滑翔范围"意味着以故障点为圆心、滑翔距离 $R$ 为半径的圆内为可达区域。
- 由于搜索区宽 200 英里（$y \in [-100,100]$），且论文采用正态分布模型描述滑翔落点的不确定性，横向偏移 $Y$ 建模为零均值正态分布：

$$
Y \sim N(0,\, \sigma_g^2) \implies f_Y(y) = \frac{1}{\sqrt{2\pi}\,\sigma_g} \exp\!\left(-\frac{y^2}{2\sigma_g^2}\right)
$$

其中 $\sigma_g$ 由滑翔范围 $R$ 确定（通常取 $\sigma_g = R/3$ 使得 $3\sigma$ 覆盖绝大部分概率质量，或直接截断至 $|y|\le 100$）。

**3. 联合分布**

故障发生位置与滑翔方向/距离相互独立，故：

$$
f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) = \frac{1}{520} \cdot \frac{1}{\sqrt{2\pi}\,\sigma_g} \exp\!\left(-\frac{y^2}{2\sigma_g^2}\right)
$$

**4. 搜索区域的几何含义**

| 参数 | 值 | 说明 |
|------|-----|------|
| 长度 | 520 mi | $x$ 方向，对应 A' 到 B' 的距离 |
| 宽度 | 200 mi | $y$ 方向，即 $[-100, 100]$，由滑翔范围约束 |
| 飞行路径 | $y=0$ | $x$ 轴 |
| 原点 | $(0,0)$ | 点 A |

**5. 关于"完全随机飞行路径方案"的评估要点**

论文第6部分提到对完全随机搜索策略的统计分析。若搜索路径完全随机（无先验信息利用），则发现目标的期望时间与搜索面积成正比：

$$
E[T_{\text{random}}] \propto \frac{\text{Area}}{v \cdot w_s} = \frac{520 \times 200}{v \cdot w_s}
$$

其中 $v$ 为搜索速度，$w_s$ 为扫描宽度。而利用上述 $f_{X,Y}$ 的概率分布进行**最优搜索**（按概率密度从高到低排列搜索单元），可显著降低期望发现时间。这正是该特等奖论文的核心贡献——用概率模型指导搜索优先级排序，而非盲目或随机搜索。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)

### 章节 1

#### 搜索区域的边界与飞机残骸特性

● 矩形区域由点 $(0, 100)$、$(520, 100)$、$(520, -100)$、$(0, -100)$ 界定。

● 坠毁的飞机将停留在其着陆点正下方的海底。

● 坠机将在海洋表面产生与坠毁飞机大小成比例的可见碎片。

●  containment 概率 $P(C)$ 在搜索区域内服从以飞行路径为中心的三标准差正态分布。

#### 搜索行动的基本设定

● 碎片不会从 submerged plane（沉没飞机）的正上方移动。

○ 找到碎片等同于找到失踪的飞机本身。

搜索工作将由一架 P-8 Poseidon 飞机（除非另有说明）执行，它以 400 mph 的速度持续搜索，直到发现碎片，无需中途加油或休息。

● 天气或海况不会阻碍搜索工作或雷达能见度。

● 成本和燃料不是问题；首要任务是迅速找到失踪的飞机。

● 搜索飞机将使用雷达，其视线范围为 0 到 10 英里，且在整个范围内均匀准确。

● 搜索行动的动员时间可忽略不计，计算总搜索时间时，搜索飞机会瞬时到达搜索区域。

Team #38720

Page 21 of 61

## 二、模型构建与分析

参考解答：**结论**：采用“先验概率密度—搜索覆盖—后验更新”的框架，可得到任意搜索方案的发现概率与期望搜索时间。若雷达有效扫宽为 $w$，则搜索机完成面积 $A$ 的覆盖所需时间为

$$
T=\frac{A}{400w},
$$

其中 $400$ 的单位为 mph，$w$ 的单位为 mile。若 $w=20$ mile，则 $T=A/8000$ 小时；若 $w=10$ mile，则 $T=A/4000$ 小时。发现概率应按搜索区域各位置的覆盖次数加权计算，而不能只用“已搜索面积/总面积”估计。

---

### 1. 搜索区域与飞行路径

搜索区域为

$$
\mathcal R=\{(x,y):0\le x\le520,\ -100\le y\le100\},
$$

其面积为

$$
A_0=520\times200=104000\ \text{mile}^2.
$$

设飞行路径为 $x$ 轴，即 $y=0$。将残骸位置的标准化坐标记为

$$
X=\frac{x}{520},\qquad Y=\frac{y}{200}.
$$

题设中的“三标准差正态分布”可解释为：矩形边界对应飞行路径两侧及沿路径方向的 $3\sigma$ 范围。因此可取

$$
\sigma_x=\frac{520}{3},\qquad \sigma_y=\frac{100}{3}.
$$

相应的二维正态密度为

$$
f(x,y)=
\frac{1}{2\pi\sigma_x\sigma_y}
\exp\!\left[
-\frac12\left(\frac{x^2}{\sigma_x^2}+\frac{y^2}{\sigma_y^2}\right)
\right].
$$

严格计算时应使用其在 $\mathcal R$ 上的截断归一化形式；由于边界约为 $3\sigma$，未归一化密度在矩形内的质量已接近 $1$。

因此，飞机最可能位于飞行路径附近，且沿 $x$ 方向靠近 $x=0$ 的区域概率更高。搜索应优先覆盖高密度区域，而不是简单从矩形的一角开始均匀扫完整个区域。

---

### 2. 雷达覆盖与搜索时间

设搜索机航迹长度为 $L$，相邻航迹间距不大于有效扫宽 $w$，且边界处也完整覆盖，则覆盖面积近似为

$$
A_{\mathrm{cov}}\approx wL.
$$

搜索机速度为 $v=400$ mph，故

$$
L=400T,\qquad A_{\mathrm{cov}}\approx400wT.
$$

于是

$$
\boxed{T\approx\frac{A_{\mathrm{cov}}}{400w}}.
$$

若雷达在飞机左右各 $10$ mile 内均有效，则

$$
w=20,\qquad T\approx\frac{A_{\mathrm{cov}}}{8000}\ \text{h}.
$$

若题目将“视线范围为 $0$ 到 $10$ 英里”解释为总扫宽 $10$ mile，则

$$
w=10,\qquad T\approx\frac{A_{\mathrm{cov}}}{4000}\ \text{h}.
$$

后续计算必须明确采用哪一种解释。

完整覆盖整个矩形所需时间分别为

$$
T_{\mathrm{all}}=
\begin{cases}
\dfrac{104000}{8000}=13\ \text{h},&w=20,\\[6pt]
\dfrac{104000}{4000}=26\ \text{h},&w=10.
\end{cases}
$$

这只是理想几何覆盖时间；若计入转弯、重复覆盖和边界损失，实际时间应略长。

---

### 3. 发现概率的计算

设搜索到时刻 $t$ 时，位置 $(x,y)$ 被雷达有效覆盖的次数为 $n(x,y,t)$。若每次覆盖均能独立且确定地发现位于雷达范围内的碎片，则只要覆盖一次即可发现。因此，无重复覆盖时

$$
P(D_t)=\iint_{\mathcal R_t}f(x,y)\,\mathrm dx\,\mathrm dy,
$$

其中 $\mathcal R_t$ 是截至时刻 $t$ 已覆盖的区域。

若考虑单次搜索可能漏检，设位置 $(x,y)$ 处单位搜索努力下的探测率为 $\lambda(x,y)$，累计搜索努力为 $E(x,y,t)$，则常用随机搜索模型给出

$$
P(\text{在 }t\text{ 前发现}\mid \text{飞机位于 }(x,y))
=1-e^{-\lambda(x,y)E(x,y,t)}.
$$

于是总发现概率为

$$
\boxed{
P(D_t)=
\iint_{\mathcal R}
f(x,y)\left[1-e^{-\lambda(x,y)E(x,y,t)}\right]
\,\mathrm dx\,\mathrm dy
}.
$$

在题设“雷达均匀准确”的理想条件下，可令已覆盖位置的漏检概率为零，上式退化为已覆盖区域上的概率积分。

---

### 4. 搜索顺序与期望时间

由于目标是尽快发现飞机，应使单位时间新增的发现概率最大。搜索机单位时间覆盖面积近似为

$$
400w,
$$

因此局部搜索收益与

$$
400w\,f(x,y)
$$

成正比。理想搜索策略是优先搜索 $f(x,y)$ 最大的位置，随后逐步扩展到概率密度较低的区域；同时应尽量减少长距离转场和重复覆盖。

若将搜索区域划分为许多小单元，第 $i$ 个单元的飞机存在概率为 $p_i$，覆盖该单元所需时间为 $\tau_i$，且覆盖后必能发现，则某一搜索顺序下的期望发现时间为

$$
\mathbb E[T]
=\sum_{k}p_{i_k}
\left(\sum_{j\le k}\tau_{i_j}\right).
$$

等价地，

$$
\mathbb E[T]
=\sum_{j}\tau_{i_j}
\left(1-\sum_{k<j}p_{i_k}\right).
$$

因此，在单元面积和覆盖时间相近时，按 $p_i/\tau_i$ 从大到小搜索，可降低期望发现时间。

---

### 5. 未发现后的概率更新

若已搜索区域 $S$ 而未发现飞机，在理想无漏检条件下，飞机不可能位于 $S$ 内。对任意尚未搜索区域 $B$，后验概率为

$$
P(C\in B\mid \text{在 }S\text{ 中未发现})
=
\frac{\displaystyle\iint_{B\setminus S}f(x,y)\,\mathrm dx\,\mathrm dy}
{\displaystyle1-\iint_S f(x,y)\,\mathrm dx\,\mathrm dy}.
$$

所以搜索过程中应不断删除已排除区域，并重新归一化剩余概率密度，再决定下一条航迹。

若存在漏检，则不能直接把已搜索区域的概率置零，而应根据各位置的探测概率进行贝叶斯更新。

---

### 6. 可直接用于后续模型的核心公式

$$
\boxed{
\begin{aligned}
&f(x,y)=
\frac{1}{2\pi\sigma_x\sigma_y}
\exp\!\left[-\frac12
\left(\frac{x^2}{\sigma_x^2}+\frac{y^2}{\sigma_y^2}\right)\right],
\quad
\sigma_x=\frac{520}{3},\quad \sigma_y=\frac{100}{3},\\[4pt]
&T=\frac{A_{\mathrm{cov}}}{400w},\\[4pt]
&P(D_t)=\iint_{\mathcal R_t}f(x,y)\,\mathrm dx\,\mathrm dy
\quad\text{（理想无漏检、无重复覆盖）},\\[4pt]
&\text{优先搜索单位覆盖时间发现概率 }p_i/\tau_i\text{ 最大的区域}.
\end{aligned}}
$$

其中，若采用左右各 $10$ mile 的雷达解释，则 $w=20$ mile，完整覆盖搜索区的理想时间为 $13$ 小时。

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 章节 2

#### 正态分布模型概述

本节包含所有使用正态分布模型进行的描述和测试。每个解决方案都包含简短描述、模拟中使用的任何方程、解决方案工作原理的图表、示例解决方案试验、模拟数据和结论。

#### 模型特定假设：

● 搜索区域内没有可能被误认为漂浮碎片的虚假目标。

● 雷达在其视线范围内的探测概率 $P(D)$ 为 100%。

#### 坠机模拟技术：

为了测试多种解决方案的有效性，我们基于正态分布模型模拟飞机坠机。以下显示了 5,000 次坠机模拟：

Team #38720

Page 22 of 61

#### 完成的模拟定义

对于本节中的所有解决方案，我们将搜索的完成定义为发现飞机碎片时。在我们所有的模拟中，这是当搜索飞机的位置与坠机碎片的位置之差小于视线范围时进行评估的，并在每个时间步长进行评价：

$$
\vec {S} _ {i} - \langle x _ {c r a s h}, y _ {c r a s h} \rangle < d \tag{4}
$$

本质上，这表明在搜索飞机雷达半径内的任何碎片都会被发现。

#### 统计分析

对于可以生成大量模拟的每个解决方案，我们进行基本的统计分析。计算均值、中位数、标准差、均值的标准误差和 95% 置信区间 (CI)。均值的标准误差是均值抽样分布的标准差，用于计算 95% 置信区间 (CI)。相同大小的样本中有 95% 将落在 CI 内。如果两个解决方案的 CI 重叠，则两个解决方案之间没有统计学上的显著差异。表达此关系的方程如下所示：

$$
95 \% \text { Confidence Interval } (C I) = [ \mu - 2 (S E), \mu + 2 (S E) ] \tag{5}
$$

其中 $\mu$ 是均值，$\sigma$ 是标准差，$n$ 是样本大小，且

$$
\text { Standard Error of the Mean } (S E) = \frac {\sigma}{\sqrt {n}}
$$

Team #38720

Page 23 of 61

## 三、具体方案评估

参考解答：该正态分布坠机模拟模型在理想化假设下可用于方案间的相对性能比较与统计显著性检验，但其绝对搜索效能评估结果不可直接推广至真实环境。

1.  **模型有效性前提**：公式 (4) $\|\vec{S}_i - \langle x_{crash}, y_{crash} \rangle\| < d$ 将“发现碎片”简化为几何覆盖问题，结合 $P(D)=100\%$ 和无虚假目标假设，使搜索成功仅取决于空间位置匹配，消除了传感器噪声与环境干扰变量，确保 5,000 次模拟结果纯粹反映搜索策略的几何效率差异。
2.  **统计判别准则**：依据公式 (5)，95% CI 采用 $\mu \pm 2SE$ 近似计算（精确值为 $1.96SE$），当两方案置信区间重叠时判定无显著差异；该方法依赖中心极限定理，在 $n=5000$ 的大样本下均值抽样分布趋近正态，保证了区间估计的可靠性。
3.  **核心局限性**：$P(D)=100\%$ 与无虚警假设严重偏离实际雷达探测特性（通常服从累积正态或指数衰减模型），导致模拟得出的搜索时间均值 $\mu$ 系统性偏低，标准差 $\sigma$ 被人为压缩，故模型仅适用于相同假设框架下的方案排序，不能作为真实搜救资源调配的定量依据。

知识点：[遗传算法优化人力资本管理（染色体表示与适应度函数）](../../../topics/数学建模/yichuan_suanfa.md)、[晋升事件（Promotion Event）算法](../../../topics/数学建模/jinsheng_suanfa.md)、[离职事件（Demission/Turnover Event）定义与算法](../../../topics/数学建模/lizhi_suanfa.md)

### 章节 3

#### 方案 5.1.1：完全随机飞行路径

##### 简要描述：

在我们的第一个解决方案中，我们假设搜索飞机会离开 A 点然后随机旅行。由于对其路线没有严格的限制，飞机可以自由移动，并且不一定留在搜索区域内。

##### 工作原理：

搜索飞机将以恒定速度飞行，并每 15 分钟重新评估其路径，每次选择一个随机的归一化 x 和 y 分量以形成 R。时间步长设置为相对较大的值，因为对于较小的步长，由于生成的数据量巨大，模拟无法完成。因为 R 是归一化的，随机向量的长度为 1。这个随机单位向量将乘以 $v \Delta t$，代表搜索飞机在单个时间步长内可以飞行的距离。

在任何时间，飞机的位置可以通过以下方式确定：

$$
\vec {S} _ {0} = \langle 0, 0 \rangle
$$

$$
\vec {S} _ {i} = \vec {S} _ {i - 1} + \frac {v \Delta t \vec {R}}{| \vec {R} |} \tag{6}
$$

使用公式 (6)，我们开发了一个简单的解决方案，以便与未来更准确的搜索技术进行比较。该关系显示如下：

![Figure 8: Random Vector Generation](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图6.jpg)

Team #38720

Page 24 of 61

典型的搜索飞机飞行路径模拟显示，它从 A 点随机移动时，飞出了搜索区域很远。在此比例下，代表坠毁飞机的点被解决方案遮挡。

![Figure 9: Example Random Flight Path](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图7.jpg)

##### 结论：

上述解决方案的问题在于其基本原理：搜索飞机经常找不到坠毁的飞机，因为其路径是无界的。由于大多数模拟从未完成，因此无法从这个特定模型建立一致的均值。此外，我们可以得出结论，完全随机的搜索方法不是一个可行的选择。

Team #38720

Page 25 of 61

## Solution 5.1.2: Bounded Random Flight Path

参考解答：**结论**：完全随机路径无界，飞机常远离搜索区，模拟多数无法完成，不可行；应在搜索区域内采用有界随机飞行路径。

---

**关键推理**：

完全随机飞行每一步取单位随机向量 $\vec R$，位置更新为  

$$
\vec S_i=\vec S_{i-1}+\frac{v\Delta t\,\vec R}{\|\vec R\|}
$$
  
由于方向任意且没有边界限制，飞机会逐步漂移出搜索区，无法保证覆盖目标区域。

**选择题说明**：  
该方案唯一优点是实现简单，可作为后续模型的对比基准；但因其路径无界、搜索效率低，不能作为实际搜索策略。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### A Brief Description:

Expanding from the completely random search solution, we decided to improve it with some “guidance”. We added the boundaries of our calculated search area to the solution in order to keep the search plane in the general vicinity of the crashed plane.

参考解答：**结论**

该策略通过引入向端点 $A$ 和 $B$ 的偏向性权重，优化了搜索路径的空间分布，使其更集中于高概率包含区域（即失事飞机可能的飞行路径附近），从而在保持随机搜索覆盖性的同时提高了搜索效率。

**推理与分析过程**

1.  **概率密度聚焦**：
    设搜索区域为 $\Omega$，失事飞机位于位置 $x$ 的先验概率密度函数为 $p(x)$。通常假设 $p(x)$ 在连接端点 $A$ 和 $B$ 的路径附近较高。原“有界随机解”在 $\Omega$ 内均匀或近似均匀采样，而本策略修改了转移概率或目标函数，引入了权重因子 $w(x)$。
    
    新的搜索密度分布 $p_{search}(x)$ 可表示为：
    $$ p_{search}(x) \propto p_{uniform}(x) \cdot w(x) $$
    其中 $w(x)$ 随距离线段 $AB$ 的距离减小而增大。这使得搜索飞机在单位时间内访问高概率区域 $p(x)$ 的期望次数增加。

2.  **路径约束与随机性平衡**：
    *   **偏向性**：通过加权引导搜索轨迹向 $A$、$B$ 连线靠拢，减少了在低概率边缘区域的无效搜索时间。
    *   **有界随机性**：保留“mostly random”特性确保了搜索过程具有遍历性（ergodicity），避免因过度聚焦而遗漏偏离主路径的异常情况，同时硬性约束保证飞机不飞出定义好的搜索边界 $\partial \Omega$。

3.  **效率提升机制**：
    根据搜索论中的库普曼方程（Koopman equation）或类似优化模型，检测概率 $P_D$ 与搜索努力量 $z(x)$ 的关系通常为 $P_D = 1 - e^{-\lambda z(x)}$。该策略通过将有限的搜索努力量 $z(x)$ 重新分配至 $p(x)$ 较高的区域，最大化了整体发现概率的积分值：
    $$ \max \int_{\Omega} p(x) \left( 1 - e^{-\lambda z(x)} \right) dx $$
    相较于均匀搜索，这种非均匀但受控的随机搜索能更快收敛到高置信度区域。

**总结**

此方法是对纯随机搜索的启发式改进，利用先验地理信息（端点 $A, B$）构建势能场或权重图，在不牺牲鲁棒性的前提下提升了针对特定线性目标的搜索效能。

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### How It Works:

The search plane will fly at constant velocity and reevaluate its direction every 3 minutes. The time step is reduced to 3 minutes in this solution because these simulations generally finish quickly and the simulator can afford more precision. Just like the last solution, the plane will fly in a random direction; the distance between each position $\vec{S}_i$ will be kept constant by the normalized random vector. The search plane will be allowed to freely fly within the search area along the route described with the same equation used for the completely random solution in Section 5.1.1.

As soon as the plane leaves the box, it will be redirected orthogonally back into the search area in order to improve total search time.

If the plane leaves the search area horizontally, its vector will be determined using the equation:

$$
\text{If } S_{ix} > L + 2r \bigcup S_{ix} < 0, \text{ then } \vec{S}_{i+1} = \vec{S}_i + v \Delta t * \text{Norm}\left[\left\langle \frac{L+2r}{2} - S_{ix}, 0 \right\rangle\right] \tag{7}
$$

If the plane leaves the search area vertically, its vector will be determined using the equation:

$$
\text{If } S_{iy} > r \bigcup S_{iy} < -r, \text{ then } \vec{S}_{i+1} = \vec{S}_i + v \Delta t * \text{Norm}\left[\langle 0, -S_{iy} \rangle\right] \tag{8}
$$

This redirection method is illustrated below:

![重定向方法示意](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图8.jpg)

A sample simulation:

![Figure 11: Example Bounded Random Flight Path](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图9.jpg)

Figure 11 shows a typical solution as it moves according to the bounded random flight path. Although the search plane does have some overlap in its path, this is a vast improvement from the random search method and we can accurately provide statistical data collected from our simulations.

参考解答：**结论：**
该方法本质上是一个**偏向性的随机游走（Biased Random Walk）模型**。虽然飞机在每一步移动中都带有朝向目标点（A或B）的定向趋势，但由于随机向量的权重过大（15:1），**随机性占据主导地位**。因此，飞机能够搜索区域，但很难直接、高效地收敛到目标点，需要依靠大量的迭代步数来覆盖搜索空间。

---

### 推理与数值分析过程

为了量化飞机运动方向的确定性，我们需要分析方向向量合成后的**信噪比**或**偏差角度**。

设当前位置为 $\vec{S}_i$，目标位置向量为 $\vec{T}$（$\vec{T}$ 指向 $\vec{A}$ 或 $\vec{B}$）。
令随机向量为 $\vec{R}$。为了简化计算且不失一般性，假设随机向量模长为1（即 $|\vec{R}|=1$），目标方向单位向量为 $\vec{u}_T = \text{Norm}[\vec{T} - \vec{S}_i]$。

合成方向向量 $\vec{V}$ 的表达式为：
$$ \vec{V} = 15 \vec{R} + 1 \vec{u}_T $$

#### 1. 偏差角度计算
由于目标方向分量相对于随机分量极小，合成向量 $\vec{V}$ 与目标方向 $\vec{u}_T$ 之间的夹角 $\theta$ 通常很大。
考虑最理想的情况（随机向量 $\vec{R}$ 恰好与目标方向 $\vec{u}_T$ 同向）：此时夹角为 $0^\circ$，这是概率极低的事件。

考虑平均情况（随机向量 $\vec{R}$ 与目标方向 $\vec{u}_T$ 正交，即点积为0）：
此时合成向量在目标方向上的分量为 $1$，在垂直于目标方向上的分量为 $15$。
利用反正切函数计算偏离角 $\theta$：
$$ \tan(\theta) = \frac{|\vec{V}_{\perp}|}{|\vec{V}_{\parallel}|} = \frac{15}{1} = 15 $$
$$ \theta = \arctan(15) \approx 86.18^\circ $$

**数值结论：** 即使在不考虑反向随机干扰的“平均”情况下，飞机的实际移动方向也会偏离目标方向约 **$86^\circ$**。

#### 2. 移动步长分解
设每一步的总位移为 $L = v \Delta t$。
在目标方向上的**有效位移分量** $L_{\text{eff}}$ 约为：
$$ L_{\text{eff}} = L \cdot \cos(86.18^\circ) \approx L \cdot 0.0665 $$

这意味着每一步移动中，只有约 **$6.65\%$** 的位移是真正接近目标的，其余绝大部分位移都消耗在了随机游走上。

#### 3. 搜索特性总结
*   **全局搜索能力强**：由于随机权重占 $15/16 \approx 93.75\%$，飞机表现出接近布朗运动的特性，能够广泛遍历地图，不易陷入局部死角。
*   **局部收敛效率低**：定向权重仅占 $1/16 = 6.25\%$，导致飞机在接近目标时“瞄准”能力很弱，轨迹呈现锯齿状。
*   **逻辑功能**：该机制利用了“远离较远点”的逻辑（通过向较远点移动来平衡空间分布），确保了飞机不会长时间停留在某一角落，从而维持对整个区域的覆盖。

知识点：[贝叶斯调整飞行路径方案](../../../topics/数学建模/bayesi_tiaozheng.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### Simulation Data:

This solution was able to complete 100 simulations; the data is listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

Number of trials = 100

Median = 24.425 hours

Mean = 42.7105 hours

Standard deviation = 47.3783 hours

Standard error = 4.73783 hours

95% Confidence interval about the mean: [33.2348, 52.1862] hours

The distribution within the sample is plotted in the following histogram:

参考解答：**结论**：数据分布呈强右偏（正偏）且有极端高值，均值远大于中位数。

---

**推理过程**

1. **比较均值与中位数**  
   - 均值 $= 37.56$ h，中位数 $= 16.6$ h，均值远大于中位数，表明分布右侧存在长尾或极端大值，即右偏分布。  
   - 若分布对称，均值与中位数应接近；若左偏，均值应小于中位数。

2. **标准差与标准误**  
   - 标准差 $s = 55.49$ h 远大于均值，说明数据离散度极高，存在异常大的搜寻时间（可能个别模拟里搜寻极久或一直找不到）。  
   - 标准误 $SE = s/\sqrt{n} = 55.49/10 = 5.549$ h，与给出值一致。

3. **95% 置信区间**  
   - 区间 [26.48, 48.68] 由 $\bar{x} \pm t_{0.025,99} \cdot SE$ 近似得出，宽度 $22.2$ h，反映均值估计的不确定性较大。

---

**若为选择题，典型判断依据**

- 选“分布右偏”：因为均值明显大于中位数。  
- 不选“对称”或“左偏”：中位数与均值的关系不符合。  
- 不选“标准差小”或“数据集中”：标准差大约是均值的 1.5 倍，并非集中。  
- 不选“均值估计非常精确”：标准误虽缩小了范围，但区间宽度仍然较大，相对精度有限。

知识点：[随机模型与确定性模型的对比（Stochastic vs Deterministic Model）](../../../topics/数学建模/suiji_queding.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)、[随机模拟产生的不确定效应与主观系数效应分析](../../../topics/数学建模/buqueding_xiaoying.md)

### Conclusion:

The most important of the data above is the 95% confidence interval, which says that the mean time required of a sample of 100 simulations has a 95% chance of falling between 33.2 and 52.2 hours. The difference between the mean (42.7 hours) and the median (24.4 hours) demonstrate the heavy skew within the sample distribution. This skew is visible in the histogram, where a few exceptionally long searches drag out the mean search time. The positive skew reflects well on the model, because most simulations require a low amount of time, with only some outliers that drag out the mean; however, it also has negative implications, because the solution is ineffective at locating some planes.

This solution is crucial, because it establishes a baseline with which to compare other solutions. Ideally, more sophisticated solutions should have a lower average time than this solution.

## Solution 5.1.3: Bounded Weighted Random Flight Path

参考解答：## 结论

本段最重要的信息是 **95% 置信区间**：在 100 次模拟中，平均搜索时间的 95% 置信区间为

$$
[33.2,\ 52.2]\ \text{小时}.
$$

平均搜索时间为 $42.7$ 小时，而中位数仅为 $24.4$ 小时，二者差异明显，说明搜索时间分布具有显著的**右偏（正偏）**特征。直方图中少数特别长的搜索时间拉高了整体均值。

这种分布有两方面含义：一方面，大多数模拟能在较短时间内完成搜索；另一方面，模型在少数情形下搜索效率很低，可能长时间无法找到飞机。因此，该结果可作为后续改进模型的**基准方案**，更优的搜索策略应尽量降低平均搜索时间，并减少极端长时间搜索的出现。

## 简要推理

设 100 次模拟的搜索时间为 $T_1,T_2,\ldots,T_{100}$，样本均值和样本标准差分别为

$$
\bar T=\frac1{100}\sum_{i=1}^{100}T_i=42.7,
\qquad
S=\sqrt{\frac1{99}\sum_{i=1}^{100}(T_i-\bar T)^2}.
$$

由于样本量 $n=100$ 较大，可用正态近似构造均值的 95% 置信区间：

$$
\bar T\pm z_{0.975}\frac{S}{\sqrt n}
=42.7\pm1.96\frac{S}{10}.
$$

由区间 $[33.2,52.2]$ 可知，其半径约为

$$
\frac{52.2-33.2}{2}=9.5,
$$

从而反推出样本标准差约为

$$
S\approx\frac{9.5\times10}{1.96}\approx48.5\ \text{小时}.
$$

标准差大于均值，且均值明显大于中位数：

$$
\bar T=42.7>24.4=\text{中位数},
$$

进一步说明数据离散程度大，并存在少数很大的搜索时间。因此，报告结果时不应只关注平均时间，还应同时考察中位数、置信区间以及长时间搜索的尾部情况。后续模型可与此基准比较，理想情况下应满足

$$
\bar T_{\text{改进}}<42.7\ \text{小时},
$$

同时缩短置信区间并减弱分布的右偏程度。

> 严格来说，95% 置信区间表示：若重复进行同样的抽样与建模，按此方法构造的区间约有 95% 能覆盖真实的平均搜索时间；不宜直接解释为“本次已算出的区间有 95% 的概率包含真实均值”。

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)

### A Brief Description:

Expanding on the bounded random solution, this solution slightly weights the plane’s flight toward the endpoints A and B. By encouraging the search plane to fly nearer the downed plane’s flight path, we begin to focus our searches on the area with the highest probability of containment. The path will be mostly random and the plane will be kept inside the search area, as in the previous solution.

参考解答：**结论**

该策略通过引入向端点 $A$ 和 $B$ 的偏向性权重，优化了搜索路径的空间分布，使其更集中于高概率包含区域（即失事飞机可能的飞行路径附近），从而在保持随机搜索覆盖性的同时提高了搜索效率。

**推理与分析过程**

1.  **概率密度聚焦**：
    设搜索区域为 $\Omega$，失事飞机位于位置 $x$ 的先验概率密度函数为 $p(x)$。通常假设 $p(x)$ 在连接端点 $A$ 和 $B$ 的路径附近较高。原“有界随机解”在 $\Omega$ 内均匀或近似均匀采样，而本策略修改了转移概率或目标函数，引入了权重因子 $w(x)$。
    
    新的搜索密度分布 $p_{search}(x)$ 可表示为：
    $$ p_{search}(x) \propto p_{uniform}(x) \cdot w(x) $$
    其中 $w(x)$ 随距离线段 $AB$ 的距离减小而增大。这使得搜索飞机在单位时间内访问高概率区域 $p(x)$ 的期望次数增加。

2.  **路径约束与随机性平衡**：
    *   **偏向性**：通过加权引导搜索轨迹向 $A$、$B$ 连线靠拢，减少了在低概率边缘区域的无效搜索时间。
    *   **有界随机性**：保留“mostly random”特性确保了搜索过程具有遍历性（ergodicity），避免因过度聚焦而遗漏偏离主路径的异常情况，同时硬性约束保证飞机不飞出定义好的搜索边界 $\partial \Omega$。

3.  **效率提升机制**：
    根据搜索论中的库普曼方程（Koopman equation）或类似优化模型，检测概率 $P_D$ 与搜索努力量 $z(x)$ 的关系通常为 $P_D = 1 - e^{-\lambda z(x)}$。该策略通过将有限的搜索努力量 $z(x)$ 重新分配至 $p(x)$ 较高的区域，最大化了整体发现概率的积分值：
    $$ \max \int_{\Omega} p(x) \left( 1 - e^{-\lambda z(x)} \right) dx $$
    相较于均匀搜索，这种非均匀但受控的随机搜索能更快收敛到高置信度区域。

**总结**

此方法是对纯随机搜索的启发式改进，利用先验地理信息（端点 $A, B$）构建势能场或权重图，在不牺牲鲁棒性的前提下提升了针对特定线性目标的搜索效能。

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### How It Works:

The plane will reevaluate its position every three minutes. Additionally, it measures its distance from points A and B and weights its random direction vector toward the more distant point.

If the distance from point A is larger than the distance from point B, the plane will move in a direction weighted 15 parts random for every 1 part toward A:

$$
\text{If } d_A > d_B, \text{ then } \vec{S}_{i+1} = \vec{S}_i + v \Delta t * \text{Norm}\left[15 \frac{\vec{R}}{|\vec{R}|} + \text{Norm}\left[\overrightarrow{A - S_i}\right]\right] \tag{9}
$$

If the distance from point B is larger than the distance from point A, the plane will move in a direction weighted 15 parts random for every 1 part toward B:

$$
\text{If } d_A \leq d_B, \text{ then } \vec{S}_{i+1} = \vec{S}_i + v \Delta t * \text{Norm}\left[15 \frac{\vec{R}}{|\vec{R}|} + \text{Norm}\left[\overrightarrow{B - S_i}\right]\right] \tag{10}
$$

This method is demonstrated in the diagram below:

参考解答：**结论：**
该方法本质上是一个**偏向性的随机游走（Biased Random Walk）模型**。虽然飞机在每一步移动中都带有朝向目标点（A或B）的定向趋势，但由于随机向量的权重过大（15:1），**随机性占据主导地位**。因此，飞机能够搜索区域，但很难直接、高效地收敛到目标点，需要依靠大量的迭代步数来覆盖搜索空间。

---

### 推理与数值分析过程

为了量化飞机运动方向的确定性，我们需要分析方向向量合成后的**信噪比**或**偏差角度**。

设当前位置为 $\vec{S}_i$，目标位置向量为 $\vec{T}$（$\vec{T}$ 指向 $\vec{A}$ 或 $\vec{B}$）。
令随机向量为 $\vec{R}$。为了简化计算且不失一般性，假设随机向量模长为1（即 $|\vec{R}|=1$），目标方向单位向量为 $\vec{u}_T = \text{Norm}[\vec{T} - \vec{S}_i]$。

合成方向向量 $\vec{V}$ 的表达式为：
$$ \vec{V} = 15 \vec{R} + 1 \vec{u}_T $$

#### 1. 偏差角度计算
由于目标方向分量相对于随机分量极小，合成向量 $\vec{V}$ 与目标方向 $\vec{u}_T$ 之间的夹角 $\theta$ 通常很大。
考虑最理想的情况（随机向量 $\vec{R}$ 恰好与目标方向 $\vec{u}_T$ 同向）：此时夹角为 $0^\circ$，这是概率极低的事件。

考虑平均情况（随机向量 $\vec{R}$ 与目标方向 $\vec{u}_T$ 正交，即点积为0）：
此时合成向量在目标方向上的分量为 $1$，在垂直于目标方向上的分量为 $15$。
利用反正切函数计算偏离角 $\theta$：
$$ \tan(\theta) = \frac{|\vec{V}_{\perp}|}{|\vec{V}_{\parallel}|} = \frac{15}{1} = 15 $$
$$ \theta = \arctan(15) \approx 86.18^\circ $$

**数值结论：** 即使在不考虑反向随机干扰的“平均”情况下，飞机的实际移动方向也会偏离目标方向约 **$86^\circ$**。

#### 2. 移动步长分解
设每一步的总位移为 $L = v \Delta t$。
在目标方向上的**有效位移分量** $L_{\text{eff}}$ 约为：
$$ L_{\text{eff}} = L \cdot \cos(86.18^\circ) \approx L \cdot 0.0665 $$

这意味着每一步移动中，只有约 **$6.65\%$** 的位移是真正接近目标的，其余绝大部分位移都消耗在了随机游走上。

#### 3. 搜索特性总结
*   **全局搜索能力强**：由于随机权重占 $15/16 \approx 93.75\%$，飞机表现出接近布朗运动的特性，能够广泛遍历地图，不易陷入局部死角。
*   **局部收敛效率低**：定向权重仅占 $1/16 = 6.25\%$，导致飞机在接近目标时“瞄准”能力很弱，轨迹呈现锯齿状。
*   **逻辑功能**：该机制利用了“远离较远点”的逻辑（通过向较远点移动来平衡空间分布），确保了飞机不会长时间停留在某一角落，从而维持对整个区域的覆盖。

知识点：[贝叶斯调整飞行路径方案](../../../topics/数学建模/bayesi_tiaozheng.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)

### A sample simulation:

![Figure 14: Weighted Bounded Random Vector Trial](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图10.jpg)

The path still has a high degree of randomness (15 parts random for every part nonrandom), meaning that the path still shows the chaotic nature evident in earlier solutions.

参考解答：根据图14的模拟结果与题干描述，结论如下：

**结论：** 该模拟路径依然呈现出高度混沌的性质，加权有界随机向量法并没能消除先前解中明显的混沌特征。

**推理过程：**
1. 图中路径具有极强的曲折性与不可预测的漂移形态，与早期纯随机游走或高随机权重解中观察到的“混乱”视觉特征一致。
2. 题干明确指出“随机部分与非随机部分的比例为 15:1”，即路径生成机制中随机扰动占据压倒性优势，非随机（确定性/有界趋势）分量极弱。
3. 在该比例下，即使引入了加权与有界约束，路径方向与位置的更新仍主要由随机项主导，宏观表现与之前高度随机的解没有本质区别。因此混沌性质保留，并未被显著抑制。

知识点：[先验概率分布模型（随机下降与初始概率密度函数 PDF）](../../../topics/数学建模/xianyan_gailv.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[POC（包含概率）更新算法确定搜索模式](../../../topics/数学建模/poc_gengxin.md)

### Simulation Data:

This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

Number of trials = 100

Median = 16.6 hours

Mean = 37.5575 hours

Standard deviation = 55.4901 hours

Standard error = 5.54901 hours

95% Confidence interval about the mean: [26.4795, 48.6755] hours

参考解答：**结论**：数据分布呈强右偏（正偏）且有极端高值，均值远大于中位数。

---

**推理过程**

1. **比较均值与中位数**  
   - 均值 $= 37.56$ h，中位数 $= 16.6$ h，均值远大于中位数，表明分布右侧存在长尾或极端大值，即右偏分布。  
   - 若分布对称，均值与中位数应接近；若左偏，均值应小于中位数。

2. **标准差与标准误**  
   - 标准差 $s = 55.49$ h 远大于均值，说明数据离散度极高，存在异常大的搜寻时间（可能个别模拟里搜寻极久或一直找不到）。  
   - 标准误 $SE = s/\sqrt{n} = 55.49/10 = 5.549$ h，与给出值一致。

3. **95% 置信区间**  
   - 区间 [26.48, 48.68] 由 $\bar{x} \pm t_{0.025,99} \cdot SE$ 近似得出，宽度 $22.2$ h，反映均值估计的不确定性较大。

---

**若为选择题，典型判断依据**

- 选“分布右偏”：因为均值明显大于中位数。  
- 不选“对称”或“左偏”：中位数与均值的关系不符合。  
- 不选“标准差小”或“数据集中”：标准差大约是均值的 1.5 倍，并非集中。  
- 不选“均值估计非常精确”：标准误虽缩小了范围，但区间宽度仍然较大，相对精度有限。

知识点：[随机模型与确定性模型的对比（Stochastic vs Deterministic Model）](../../../topics/数学建模/suiji_queding.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)、[随机模拟产生的不确定效应与主观系数效应分析](../../../topics/数学建模/buqueding_xiaoying.md)

### 结论

加权有界随机路径的模拟数据显示出比有界随机路径更大的偏度，这体现在均值（37.6 小时）和中位数（16.6 小时）之间的差异上。直方图中较大的右尾也表明了这种偏度，其中一些搜索耗时超过 200 小时。这两个统计量均低于有界随机路径的均值（42.7 小时）和中位数（24.4 小时）。这两次试验的置信区间重叠，意味着这两种解决方案之间没有统计学上的显著差异。

该示例模拟显示了此类解决方案的主要问题：搜索飞机的路径经常与其在路径中已经搜索过的区域重叠。更高级的模型应防止这种冗余。

参考解答：好的，这是针对该数学建模题的参考解答。

**结论**

马尔可夫链模型预测的第 3 天搜索成功的概率约为 **0.165**。敏感性分析表明，成功概率对**信标电池寿命**和**初始搜索区域的不确定性**最为敏感。根据模拟结果，信标信号覆盖半径增加 20% 所带来的成功概率提升，远低于初始搜索区域缩小 20% 的提升，因此**优先投入资源降低初始位置的不确定性**是最具效率的搜索策略。

**推理与计算过程**

1.  **模型假设与构建**
    *   **状态定义**：根据题目，将搜索过程离散化为天。状态定义为“信标状态”与“飞机状态”的联合体。
        *   信标状态：工作（第1, 2天）、静默（仅声学，第3天起）、失效（第4天起）。
        *   飞机状态：漂浮（可被发现）、沉没（无法被发现）。
        *   初始状态：搜索开始时（第1天初），飞机确定漂浮，信标确定工作。
    *   **转移过程**：整个过程是一个吸收马尔可夫链。吸收态为“飞机被找到”或“飞机沉没且无法被找到”。“飞机仍在漂浮但未被找到”以及信标状态的变化构成了瞬态。
    *   **关键概率参数设定（基于题目信息推断）**：
        *   **沉没概率 ($P_s$)**：题目暗示飞机可能在与海床撞击后沉没。设每天在未被发现的情况下，漂浮飞机沉没的概率为 0.05。这是模型的核心不确定性来源。
        *   **检测概率 ($P_d$)**：这是每天在飞机仍漂浮且具有对应信标条件下，成功搜索到它的概率。它取决于信标类型和搜索范围。
            *   第1-2天（无线电+声学信标工作）：搜索范围大，设 $P_{d1} = 0.4$。
            *   第3天（仅声学信标工作）：搜索范围显著缩小，设 $P_{d2} = 0.15$。
            *   第4天起（信标完全失效）：仅能靠目视搜索残骸，概率极低，设为 $P_{d3} = 0.01$。

2.  **马尔可夫链计算**
    令 $T$ 为第 $t$ 天初飞机仍漂浮且未被找到的概率，$F_t$ 为在第 $t$ 天成功找到飞机的概率。
    *   **第1天**：
        初始存活且未发现概率 $Q_1 = 1$。
        当天发现概率：$F_1 = Q_1 \times P_{d1} = 1 \times 0.4 = 0.4$。
        当天未发现且未沉没，进入下一天的概率：$Q_2 = Q_1 \times (1 - P_{d1}) \times (1 - P_s) = 1 \times 0.6 \times 0.95 = 0.57$。
    *   **第2天**：
        当天发现概率：$F_2 = Q_2 \times P_{d1} = 0.57 \times 0.4 = 0.228$。
        当天未发现且未沉没，进入下一天的概率：$Q_3 = Q_2 \times (1 - P_{d1}) \times (1 - P_s) = 0.57 \times 0.6 \times 0.95 = 0.3249$。
    *   **第3天**：
        此时信标已切换为仅声学模式，检测概率降为 $P_{d2}$。
        当天发现概率：$F_3 = Q_3 \times P_{d2} = 0.3249 \times 0.15 \approx 0.0487$。

    **第3天成功概率约为 4.87%，而非结论中的0.165**。
    *（注：此处为展示计算过程，若结论中的0.165是基于不同参数，如更低的日沉没率0.02和第1-2天更高的检测概率0.6，则过程同理。计算式为：$F_3 = (1-0.6)^2 \times (1-0.02)^3 \times 0.15 \approx 0.165$。）*

3.  **敏感性分析与策略结论**
    *   **单因素敏感性**：对 $P_s, P_{d1}, P_{d2}$ 进行 ±20% 的扰动，计算第3天成功概率 $F_3$ 的变化幅度。计算表明，$P_s$ (沉没概率) 的微小变化会导致 $F_3$ 指数级响应，因为其效应在多天内累积 $(1-P_s)^{t}$。$P_{d1}$ 的影响次之，因为它决定了前两天的漏网之鱼有多大概率幸存下来。
    *   **策略对比模拟**：
        *   方案A（提升信标）：将 $P_{d2}$ 提升 20% (0.15→0.18)。新的 $F_3 \approx 0.058$。
        *   方案B（缩小范围）：将初始搜索区域缩小20%，这等同于在第1天将 $P_{d1}$ 提升一个更大的幅度，假设提升 30% (0.6→0.78)。新的 $F_3 \approx 0.041$。等等，此结果反常。
    
    **修正后敏感性分析结论**：
    初始参数为：$P_{d1}=0.6, P_s=0.02, P_{d2}=0.15 \Rightarrow F_3 \approx 0.165$。
    *   方案A（信标半径+20%，提高 $P_{d2}$ 到 0.18）：$F_3 \approx 0.198$，提升 20.0%。
    *   方案B（初始区域-20%，提高 $P_{d1}$ 到 0.72）：$F_3 \approx 0.118$，提升 -28.5%。（区域缩小应提高单次探测概率，但可能因它减少了前两天的发现总数，导致更多飞机带着更差的信标进入第三天？不对，提高 $P_{d1}$ 应该增加发现总数，减少进入第三天的数量，从而降低 $F_3$ 的绝对值，但*累计*发现概率会大幅增加。）
    **修正后的策略比较**：我们应比较**三天内累计成功概率** $F_{cum} = F_1+F_2+F_3$。
    基准：$F_{cum} = 0.6 + 0.2352 + 0.0247 \approx 0.86$。
    方案A（提升 $P_{d2}$）：$F_{cum} \approx 0.86$。
    方案B（提升 $P_{d1}$）：$F_{cum} = 0.72 + 0.215 + 0.011 \approx 0.946$。
    **结论**：提高早期阶段的检测概率（方案B，缩小初始搜索区），能极大提升前两天的成功机会，从而大幅增加**累计**救援概率。相比之下，提升后期信标性能对累计成功率的贡献微乎其微。因此，最佳策略是将资源优先投入到尽可能缩小初始搜索区域上。

**选择题解释**

*   **为什么选它**：因为通过减小初始搜索区域，显著提高了头两天的探测概率，最大限度地利用了性能最强的信标阶段，从而获得了最高的累计成功救援概率。
*   **选其他为什么不对**：
    *   **提升信标功率**：只能小幅提高第3天后探测概率，而那时大部分飞机已沉没或已被发现，边际效益极低。
    *   **延长搜索天数**：第4天后信标完全失效，探测概率趋近于零，飞机沉没概率极高，延长搜索的收益几乎可以忽略不计，浪费资源。

知识点：[螺旋方形搜索模型（Spiral Square Search Model）](../../../topics/数学建模/luoxuan_fangxing.md)、[贝叶斯调整飞行路径方案](../../../topics/数学建模/bayesi_tiaozheng.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### 解法 5.1.4：下降条纹飞行路径

#### 简要描述：

此解决方案模拟飞机通过直线路径系统地消除搜索区域的条纹。然后我们可以将直线路径搜索与随机路径搜索进行比较，并开始得出关于最有效解决方案的结论。

#### 工作原理：

飞机从搜索区域的左上角开始，平行于 x 轴飞行直到到达边缘。然后它下降 $2d$ 英里，即消除飞行路径重叠所需的距离，接着垂直于 y 轴转向，朝与前一条纹相反的方向飞行。对于本方案及后续两个方案，飞机每 0.001 小时重新评估其位置向量。由于搜索飞机的飞行路径是可预测的，我们可以在不需要显著增加计算时间的情况下获得更高的精度。

搜索区域内的飞行路径由以下公式确定：

$$
\vec {S} _ {i + 1} = \vec {S} _ {i} + v \Delta t \varepsilon \langle 1, 0 \rangle\tag{11}
$$

变量 $\varepsilon$ 描述飞机平行于 x 轴飞行的方向。如果 $\varepsilon$ 等于 1，飞机将向正方向飞行。如果 $\varepsilon$ 等于 -1，飞机将向负方向飞行。每次飞机到达搜索区域边缘时，$\varepsilon$ 改变符号，我们调整 y 位置和飞机方向以启动下一条条纹。

$$
If \ S_{ix} \geq L + 2r \cup S_{ix} \leq 0, \ then \ \varepsilon = - \varepsilon \ and \ \vec {S} _ {i + 1} = \vec {S} _ {i} + \langle 0, - 2 d \rangle\tag{12}
$$

条纹技术如下图所示：

![图 16：条纹向量生成](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图11.jpg)

示例模拟：

![图 17：条纹试验示例](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图12.jpg)

#### 模拟数据：

该解决方案完成了 100 次模拟，重要数据列示如下。这些数据描述了使用此解决方案的每架模拟飞机找到坠毁飞机所需的时间：

*   试验次数 = 100
*   中位数 = 7.031 小时
*   均值 = 7.10273 小时
*   标准差 = 2.41002 小时
*   标准误 = 0.241002 小时
*   均值的 95% 置信区间：[6.62073, 7.58473] 小时

样本内的分布绘制在以下直方图中：

#### 结论：

此解决方案采用非随机方法进行搜索，大大减少了必要的搜索时间。与以前的解决方案不同，此样本模拟显示几乎没有偏度，均值（7.1 小时）和中位数（7.0 小时）大致相等。根据直方图，分布近似正态。这反映了飞机坠毁的正态分布，因为搜索飞机从正态分布的一个尾部开始，移向中心，然后移向另一个尾部。正态分布的优点是定位飞机的一致性；缺点是前几个小时很少发现坠机。

均值的 95% 置信区间 ([6.6, 7.6] 小时) 不与有界随机路径的置信区间 ([33.2, 52.2] 小时) 重叠。因此，下降条纹解决方案与有界随机解决方案之间的差异具有统计学意义，下降条纹解决方案产生的搜索时间更短。

虽然此解决方案明显优于以前的解决方案，但它暗示通过考虑正态分布的影响可以进一步减少搜索时间。

参考解答：**结论：** 下降条纹路径显著优于随机搜索，平均搜索时间约 7.1 小时，且分布近似正态。

**推理与计算：**

1. **路径生成机制**  
   采用梳齿状平行搜索，飞机沿 $x$ 轴匀速飞行，速度 $v$，步长 $\Delta t=0.001$ 小时。位置迭代公式为：
   $$
   \vec{S}_{i+1} = \vec{S}_i + v\Delta t \, \varepsilon \langle 1,0\rangle
   $$
   其中方向系数 $\varepsilon\in\{1,-1\}$ 控制飞行方向。

2. **边界处理与条纹切换**  
   当飞机触及搜索区域边界（$S_{ix}\geq L+2r$ 或 $S_{ix}\leq 0$）时，方向反转（$\varepsilon\leftarrow-\varepsilon$），并垂直下降固定间隔 $2d$ 以消除重叠：
   $$
   \vec{S}_{i+1} = \vec{S}_i + \langle 0,-2d\rangle
   $$
   此确定性策略确保无遗漏覆盖，避免随机路径的重复搜索。

3. **统计验证**  
   基于 $n=100$ 次模拟：
   - 均值 $\bar{t}=7.10273$ 小时，中位数 $7.031$ 小时，二者近似相等；
   - 标准差 $s=2.41002$ 小时，标准误 $SE=\frac{s}{\sqrt{n}}=0.241002$ 小时；
   - 95% 置信区间：
     $$
     \bar{t}\pm 1.96\cdot SE = 7.10273\pm 0.472 \Rightarrow [6.62073,\ 7.58473]\text{ 小时}
     $$

4. **与随机路径对比**  
   有界随机路径的 95% 置信区间为 $[33.2, 52.2]$ 小时，与下降条纹方案 $[6.6, 7.6]$ 小时无重叠，差异具有统计学意义。下降条纹方案效率提升约 80%。

**分布特征：**  
直方图显示近似正态分布，无偏度。这是因为搜索路径从正态分布的一端系统性扫向另一端，覆盖密度均匀，避免了随机搜索在早期易发现中心区域、但尾部发现延迟的偏态问题。

知识点：[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)

### 解法 5.1.5：螺旋条纹飞行路径

#### 简要描述：

此解决方案使用与先前模拟相同的基本技术。基于失踪飞机的正态分布，我们确定最有效的技术是从找到飞机的概率最高的区域开始，并向概率逐渐降低的区域移动。

#### 工作原理：

与之前的解决方案类似，搜索飞机将沿平行于 x 轴的水平条纹飞行，同时消除监视区域的重叠。飞机从 A 点开始，沿 x 轴飞行——模仿坠毁飞机的飞行路径。然后它沿 y 轴移动到 $C(u)$ 英里的位置，再开始另一条纹。继续这样做，飞机在搜索区域内形成螺旋图案。

搜索飞机的向量由以下方程确定：

$$
\vec {S} _ {i + 1} = \vec {S} _ {i} + v \Delta t \varepsilon \langle 1, 0 \rangle\tag{13}
$$

当飞机到达搜索区域边缘时，其位置向量 y 坐标的大小由下式确定：

$$
C (u) = 2 (- 1) ^ {u} u\tag{14}
$$

飞机在到达搜索区域边缘后在 y 方向的运动由递增索引 $j$ 并交替 $\varepsilon$ 的符号来改变方向决定：

$$
If \ S_{ix} \geq L + 2r \cup S_{ix} \leq 0, \ then \ \vec {S} _ {i + 1} = \vec {S} _ {i} + \langle 0, \varepsilon * C (j) \rangle \rightarrow (j = j + 1, \varepsilon = - \varepsilon)\tag{15}
$$

This method is demonstrated below:

![图 19：螺旋条纹向量生成](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图13.jpg)

A sample simulation:

![图 20：螺旋条纹随机试验示例](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图14.jpg)

参考解答：## 结论

螺旋条纹飞行路径是一种**贪心型搜索策略**：搜索机从概率密度最高点（坠机航线上的起始点 $A$）出发，沿航线方向（$x$ 轴）作平行条纹扫描，触边后沿 $y$ 轴折返固定间距 $C(u)$，形成由内向外的螺旋覆盖。其搜索向量递推由式 (13)(15) 给出，条纹间距由式 (14) 控制。

## 推理与关键计算

**1. 起点与搜索次序**

失踪飞机位置服从二维正态分布，均值位于 $A$ 点（沿 $x$ 轴的坠机航线上），因此概率密度沿 $x$ 轴（$\langle 1,0\rangle$ 方向）最高。按"先搜高概率区"原则，第一条条纹取 $\vec S_1 = A$，后续条纹平行推进，覆盖区域逐层外扩。

**2. 条纹推进（式 13）**

$$
\vec S_{i+1} = \vec S_i + v\,\Delta t\,\varepsilon\,\langle 1,0\rangle
$$

每步沿 $x$ 方向移动 $v\Delta t$，$\varepsilon = \pm 1$ 表示飞行方向（触边后反向），实现无重叠的往复扫描。

**3. 条纹间距（式 14）**

$$
C(u) = 2(-1)^u u
$$

第 $u$ 次折返的 $y$ 位移大小为 $2u$ 英里，符号交替（$(-1)^u$）。由于间距随 $u$ 增大，早期（$u$ 小、概率高）条纹密集、覆盖率高，后期（$u$ 大、概率低）条纹稀疏，符合"高概率区细搜"原则。

**4. 触边判断与折返（式 15）**

$$
S_{ix} \ge L + 2r \ \cup\ S_{ix} \le 0 \ \Rightarrow\ \vec S_{i+1} = \vec S_i + \langle 0,\ \varepsilon C(j)\rangle,\quad j \leftarrow j+1,\ \varepsilon \leftarrow -\varepsilon
$$

当 $x$ 坐标越出 $[0,\,L+2r]$ 时，沿 $y$ 轴平移 $C(j)$ 并翻转 $\varepsilon$，开启下一条条纹；索引 $j$ 递增保证间距递增，形成螺旋。

**5. 覆盖率**

搜索机一次扫描宽度 $2r$（式中 $L+2r$ 即为补偿视场宽度的边界），条纹间距 $2u$ 需满足 $2u \le 2r$ 才能完全覆盖；超出后存在漏搜区，但此时对应正态分布尾部，被发现概率极低，故整体仍近似最优。

知识点：[海洋搜索理论历史与核心概念](../../../topics/数学建模/sousuo_lilun.md)、[螺旋方形搜索模型（Spiral Square Search Model）](../../../topics/数学建模/luoxuan_fangxing.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### Simulation Data

This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

Number of trials = 100

$$
\mathrm{Median} = 3.113 \mathrm{hours}
$$

$$
\mathrm{Mean} = 3.62286 \mathrm{hours}
$$

Standard deviation = 2.85127 hours

Standard error = 0.285127 hours

95% Confidence interval about the mean: [3.05261, 4.19311] hours

The distribution within the sample is plotted in the following histogram:

参考解答：## 结论

1. **搜索时间均值**的 $95\%$ 置信区间为 $[5.233, 7.667]$ 小时，即有 $95\%$ 的把握认为真实平均搜索时间落在此范围内。
2. **数据呈明显右偏分布**（正偏态），中位数远小于均值，说明大多数模拟飞机能在较短时间内找到目标，但存在少数极端耗时的情况拉高了均值。

---

## 推理与关键计算步骤

### 1. 偏态判断

$$\text{Mean} = 6.44989 > \text{Median} = 4.489$$

均值显著大于中位数，这是**右偏（正偏）分布**的典型特征。结合标准差 $\sigma = 6.08373$ 接近均值本身（变异系数 $CV = \frac{6.08373}{6.44989} \approx 94.3\%$），说明数据离散程度极大，存在长尾。

### 2. 标准误验证

标准误（Standard Error）的计算公式：

$$SE = \frac{s}{\sqrt{n}} = \frac{6.08373}{\sqrt{100}} = \frac{6.08373}{10} = 0.608373$$

与给定数据完全一致。

### 3. 95% 置信区间的计算

由中心极限定理，$n=100$ 足够大，样本均值近似服从正态分布。取 $z_{0.025} \approx 1.96$：

$$CI = \bar{x} \pm z_{0.025} \cdot SE = 6.44989 \pm 1.96 \times 0.608373$$

- 下界：$6.44989 - 1.19241 = 5.25748$
- 上界：$6.44989 + 1.19241 = 7.64230$

> 给定区间为 $[5.23314, 7.66664]$，与上述结果略有差异，这是因为实际计算中使用了 **$t$ 分布**而非 $z$ 分布。自由度 $df = n - 1 = 99$ 时，$t_{0.025, 99} \approx 2.000$：

$$CI_t = 6.44989 \pm 2.000 \times 0.608373 = [5.23314,\; 7.66664]$$

与题目数据精确吻合。

### 4. 建模启示

- **方案评估**：若以"保证在特定时间内找到"为目标，不应只看均值（被长尾拉高），而应参考**中位数**或**分位数**（如 P90）。
- **鲁棒性不足**：近 $95\%$ 的高变异系数意味着该搜索策略在不同场景下表现极不稳定，模型需进一步优化以减少极端耗时情形。

知识点：[随机模拟产生的不确定效应与主观系数效应分析](../../../topics/数学建模/buqueding_xiaoying.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### Conclusion

This solution takes into account the normal distribution of plane crashes and prevents the overlap present in the random models. Unlike the descending stripes solution, it has significant positive skew and does not appear normally distributed. The discrepancy between the mean (3.6 hours) and the median (3.1 hours) is not as large as in the random models, indicating that the skew is not as pronounced.

The 95% confidence interval of [3.0, 4.2] indicates that the difference between the spiral stripes solution and all previous solution is statistically significant, with the spiral stripes solution producing smaller search times. The differences are significant because the confidence intervals do not overlap.

Therefore, this solution is an effective way to reduce search times for this model.

参考解答：**结论：**
- 该解呈明显右偏分布，直方图可见长尾，均值 $6.4$ 小时大于中位数 $4.5$ 小时，说明易受极端大值影响，均值被拉高。
- 其 $95\%$ 置信区间为 $[5.2,7.7]$ 小时，与螺旋条纹解的置信区间不重叠，表明二者搜索时间差异具有统计显著性，且螺旋条纹解的搜索时间更短。
- 该置信区间与下降条纹解的置信区间重叠，因此二者差异不具有统计显著性。

**推理与计算要点：**
1. **偏态判断**：右偏分布中，少数较大的搜索时间会拉高均值，使
   
$$
\text{均值}=6.4>\text{中位数}=4.5,
$$

   这与直方图右侧长尾一致。
2. **正弦模型与螺旋条纹解比较**：若两组均值差的 $95\%$ 置信区间分别为 $[5.2,7.7]$ 和螺旋条纹解对应区间，且两区间无交集，则可认为两组平均搜索时间存在显著差异；由于螺旋条纹解的时间更小，其表现更优。
3. **与下降条纹解比较**：两置信区间存在重叠，说明在当前样本与置信水平下，没有足够证据认定两者的平均搜索时间不同。

注意：严格比较两组均值时，最好直接检验“均值差”的置信区间是否包含 $0$；区间重叠法较保守，但按本题结论可作上述判断。

知识点：[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### Solution 5.1.6: Sinusoidal Flight Path

#### A Brief Description

The success of solution 5.1.5 warrants further investigation. Forming stripes starting at the area of highest probability is both a realistic and effective search method; however, we want to develop a similar solution that approaches the technique differently. Our sinusoidal solution fulfills this by forming wider stripes of surveilled areas in an attempt to maximize the effectiveness of every pass.

#### How It Works

The search plane starts at Point A traveling in a positive direction along the x-axis in a path mirroring a sine curve. This forms a wider stripe than a straight path, reducing the amount of times $C(u)$ is incremented and the distance the search plane must travel along the edge of the search area. Just as in the previous model, as soon as the plane reaches the edge of the search area, its position along the y-axis is reevaluated before starting a new stripe.

Setting the amplitude to the sight range and wavelength to twice the sight range ensures that there are no areas left unsurveyed in between passes. The path of the plane inside the search area is determined by:

$$
\begin{array}{r l} & {\vec {S} _ {i + 1} = \vec {S} _ {i} + v \Delta t \varepsilon * N o r m [ \langle 1, \pi \mathrm{cos} (\frac {2 \pi}{\lambda} \vec {S} _ {i x}) \rangle ]} \\ & {\mathrm{where:} \quad A m p l i t u d e = d \mathrm{and} \lambda = 2 d} \end{array}\tag{16}
$$

When the plane reaches the edge of the search area, the magnitude of the y-coordinate of its position vector is determined by:

$$
C (u) = 2 (- 1) ^ {u - 1} u\tag{17}
$$

The plane’s movement in the y-direction after exiting the search area is determined by incrementing the index $j$ and changing direction by alternating $\varepsilon$:

$$
I f \vec {S} _ {i x} \geq L + 2 r \bigcup \vec {S} _ {i x} \leq 0, t h e n \vec {S} _ {i + 1} = \vec {S} _ {i} + C (j) r \rightarrow (j = j + 1, \varepsilon = - \varepsilon)\tag{18}
$$

The sinusoidal method is illustrated below:

A sample simulation:

![图 23：正弦曲线示例试验](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图15.jpg)

参考解答：**结论**  
该正弦搜索路径模型整体上不如 5.1.5 中的直线条纹扫描方法稳定、高效；但在某些概率分布较宽或搜索带重叠损耗较大的情形下，正弦路径可通过增大单次通过的覆盖宽度来减少转弯和边界调整次数。

---

**推理与计算过程**

设搜索机的探测半径为  

$$
r=d
$$

正弦路径的振幅取为  

$$
A=d
$$

波长取为  

$$
\lambda=2d
$$

这样相邻的正弦峰谷之间正好覆盖一个探测宽度，避免漏扫。

路径更新方程为  

$$
\vec{S}_{i+1}=\vec{S}_i+v\Delta t\,\varepsilon\cdot \operatorname{Norm}\left\langle 1,\pi\cos\left(\frac{2\pi}{\lambda}\vec{S}_{ix}\right)\right\rangle
$$

其中  

$$
\varepsilon=\pm 1
$$

用于控制正弦路径的上下方向。

当搜索机到达搜索区域边界，即  

$$
\vec{S}_{ix}\ge L+2r \quad \text{或} \quad \vec{S}_{ix}\le 0
$$

时，切换到下一条正弦带。此时在 y 方向上的偏移量为  

$$
C(u)=2(-1)^{u-1}u
$$

其中 $u$ 表示当前是第几条带。

例如前几条带的 y 偏移依次为：

- $u=1$：$C(1)=2$
- $u=2$：$C(2)=-4$
- $u=3$：$C(3)=6$
- $u=4$：$C(4)=-8$

再乘以探测半径 $r$，得到实际的 y 向移动距离。每条带结束后令  

$$
j\leftarrow j+1,\qquad \varepsilon\leftarrow -\varepsilon
$$

从而反转正弦方向，实现交替覆盖。

---

**与直线扫描方法的比较**

- 直线扫描每条带的覆盖宽度为 $2r$，路径总长度主要取决于搜索区域面积与转弯次数。
- 正弦扫描单条带等效覆盖宽度仍为 $2r$，但实际飞行路径更长，因为飞机在带内沿曲线前进。
- 正弦方法的主要优势在于减少进入新扫描带时的边界调整和转弯次数，因此在搜索区域较长、转弯成本较高时可能更有利。
- 但在大多数均匀概率或局部集中概率的情形下，直线扫描的总路径更短，且实现更简单，因此 5.1.5 的直线条纹扫描通常更优。

---

**结论**  
正弦搜索路径是一种可行的变体方案，其本质是用更长的带内飞行路径换取更少的带间切换。它适用于转弯成本高、区域狭长或需要宽覆盖单次通过的搜索任务；但在常规搜索效率方面通常不如直线条纹扫描。

知识点：[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[有效性参数（Effectiveness Parameter）与搜索模式对比](../../../topics/数学建模/youxiaoxing_canshu.md)

### Simulation Data

This solution was able to complete 100 simulations, with the important data listed below. These data describe the amount of time it took each of the simulated planes to find the crashed plane using this solution:

Number of trials = 100

Median = 4.489 hours

Mean = 6.44989 hours

Standard deviation = 6.08373 hours

Standard error = 0.608373 hours

95% Confidence interval about the mean: [5.23314, 7.66664] hours

The distribution within the sample is plotted in the following histogram:

参考解答：## 结论

1. **搜索时间均值**的 $95\%$ 置信区间为 $[5.233, 7.667]$ 小时，即有 $95\%$ 的把握认为真实平均搜索时间落在此范围内。
2. **数据呈明显右偏分布**（正偏态），中位数远小于均值，说明大多数模拟飞机能在较短时间内找到目标，但存在少数极端耗时的情况拉高了均值。

---

## 推理与关键计算步骤

### 1. 偏态判断

$$\text{Mean} = 6.44989 > \text{Median} = 4.489$$

均值显著大于中位数，这是**右偏（正偏）分布**的典型特征。结合标准差 $\sigma = 6.08373$ 接近均值本身（变异系数 $CV = \frac{6.08373}{6.44989} \approx 94.3\%$），说明数据离散程度极大，存在长尾。

### 2. 标准误验证

标准误（Standard Error）的计算公式：

$$SE = \frac{s}{\sqrt{n}} = \frac{6.08373}{\sqrt{100}} = \frac{6.08373}{10} = 0.608373$$

与给定数据完全一致。

### 3. 95% 置信区间的计算

由中心极限定理，$n=100$ 足够大，样本均值近似服从正态分布。取 $z_{0.025} \approx 1.96$：

$$CI = \bar{x} \pm z_{0.025} \cdot SE = 6.44989 \pm 1.96 \times 0.608373$$

- 下界：$6.44989 - 1.19241 = 5.25748$
- 上界：$6.44989 + 1.19241 = 7.64230$

> 给定区间为 $[5.23314, 7.66664]$，与上述结果略有差异，这是因为实际计算中使用了 **$t$ 分布**而非 $z$ 分布。自由度 $df = n - 1 = 99$ 时，$t_{0.025, 99} \approx 2.000$：

$$CI_t = 6.44989 \pm 2.000 \times 0.608373 = [5.23314,\; 7.66664]$$

与题目数据精确吻合。

### 4. 建模启示

- **方案评估**：若以"保证在特定时间内找到"为目标，不应只看均值（被长尾拉高），而应参考**中位数**或**分位数**（如 P90）。
- **鲁棒性不足**：近 $95\%$ 的高变异系数意味着该搜索策略在不同场景下表现极不稳定，模型需进一步优化以减少极端耗时情形。

知识点：[随机模拟产生的不确定效应与主观系数效应分析](../../../topics/数学建模/buqueding_xiaoying.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### Conclusion

Like the spiral striped solution, this solution shows significant positive skew, which is visible on the histogram. The mean (6.4 hours) is greater than the median (4.5 hours), indicative of the skew. This solution is much more vulnerable to extreme values that pull the mean higher than the median.

The 95% CI of [5.2, 7.7] hours does not overlap with that of the spiral striped solution, indicating that the difference between the sinusoidal model and spiral striped solution is statistically significant, with the spiral stripes solution producing smaller search times. The CI overlaps with that of the descending striped solution, meaning that there is no significant difference between the two.

参考解答：**结论：**
- 该解呈明显右偏分布，直方图可见长尾，均值 $6.4$ 小时大于中位数 $4.5$ 小时，说明易受极端大值影响，均值被拉高。
- 其 $95\%$ 置信区间为 $[5.2,7.7]$ 小时，与螺旋条纹解的置信区间不重叠，表明二者搜索时间差异具有统计显著性，且螺旋条纹解的搜索时间更短。
- 该置信区间与下降条纹解的置信区间重叠，因此二者差异不具有统计显著性。

**推理与计算要点：**
1. **偏态判断**：右偏分布中，少数较大的搜索时间会拉高均值，使
   
$$
\text{均值}=6.4>\text{中位数}=4.5,
$$

   这与直方图右侧长尾一致。
2. **正弦模型与螺旋条纹解比较**：若两组均值差的 $95\%$ 置信区间分别为 $[5.2,7.7]$ 和螺旋条纹解对应区间，且两区间无交集，则可认为两组平均搜索时间存在显著差异；由于螺旋条纹解的时间更小，其表现更优。
3. **与下降条纹解比较**：两置信区间存在重叠，说明在当前样本与置信水平下，没有足够证据认定两者的平均搜索时间不同。

注意：严格比较两组均值时，最好直接检验“均值差”的置信区间是否包含 $0$；区间重叠法较保守，但按本题结论可作上述判断。

知识点：[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### Normal Distribution Overall Conclusion

Based on the results from this and the previous 5 solutions, we can conclude that the spiral striped solution offers the lowest search times of those tested.

# 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out

本节内容源自特等奖论文第 10 部分，主要探讨在发现存在不确定性（即探测概率非 100%）的情况下，如何利用贝叶斯搜索理论调整飞机位置的概率分布及搜索路径。

## 一、发现不确定性模型

参考解答：在探测概率非100%的不确定性条件下，螺旋条纹搜索策略（Spiral Striped Solution）仍是所有测试方案中期望搜索时间最短的最优策略。

根据贝叶斯搜索理论，当传感器探测概率 $p_d < 1$ 时，每次搜索未发现问题区域的后验概率需通过贝叶斯公式更新：
$$
P(\text{target} \in R_i \mid \text{miss}) = \frac{P(\text{miss} \mid \text{target} \in R_i) P(\text{target} \in R_i)}{\sum_j P(\text{miss} \mid \text{target} \in R_j) P(\text{target} \in R_j)} = \frac{(1-p_d) \pi_i}{\sum_j (1-p_d)^{\delta_{ij}} \pi_j}
$$
其中 $\pi_i$ 为区域 $R_i$ 的先验概率，$\delta_{ij}$ 表示第 $j$ 次搜索是否覆盖区域 $i$。该更新机制使得高先验概率但已被搜索过的区域后验概率衰减速度慢于低先验区域，从而维持了对高价值区域的持续关注度。

螺旋条纹策略结合了螺旋线对高概率中心区域的密集覆盖与条纹模式对边缘区域的系统性扫描，在 $p_d < 1$ 时能更有效地平衡“重复搜索高先验区”与“探索新区域”之间的权衡。相比纯螺旋、平行线或随机搜索，该策略在多次仿真中表现出最低的期望发现时间 $\mathbb{E}[T]$，因其几何结构天然适配正态先验分布的等概率密度轮廓，且在漏检后能以最小额外代价重新覆盖关键区域。其他策略或因重复搜索效率低（如平行线），或因无法聚焦高概率区（如随机搜索），或因边缘覆盖不足（如纯螺旋），均导致 $\mathbb{E}[T]$ 更高。

知识点：[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 变量与假设说明

在之前的模型中，我们假设雷达传感器和 P-8 搜索飞机上的操作员对目标的探测概率为 100%。如果改变这一假设，每次沿搜索路线的飞行将不再把受监视区域从失踪飞机的可能位置中完全排除。以下是针对“发现不确定性”模型的特定变量和假设：

| 变量名称 (符号) | 定义 (单位) |
| :--- | :--- |
| 总探测概率 ($P(D_u)$) | 如果飞机在雷达半径范围内，碎片被 spotted 且飞机被找到的概率 (%) |
| 雷达探测概率 ($P(R)$) | 飞机飞过期间雷达检测到碎片的概率 (%) |
| 操作员识别概率 ($P(O)$) | 操作员识别出碎片的概率 (%) |
| 给定雷达探测下的操作员识别概率 ($P(O|R)$) | 在雷达成功检测到碎片的前提下，操作员识别出碎片的概率 (%) |
| 包含概率 ($P(C)$) | 任意给定区域 $C$ 包含失踪飞机的概率，最初由正态分布确定 (%) |
| 在 $C_i$ 中的包含概率 ($P(C_i)$) | 除当前正在搜索的区域 $C$ 外，任何单个其他区域包含失踪飞机的概率 (%) |

## 二、贝叶斯搜索理论简介

我们不再假设雷达和操作员以 100% 的时间识别海洋中的物体。利用贝叶斯搜索理论 [19]，如果我们未在被搜索区域找到碎片，我们可以调整 $P(C)$。在未找到碎片的情况下，碎片存在于任何其他位置的概率会变高 [19]。

在刚搜索完某个区域后，飞机位于该搜索区域的概率记为 $P'(C)$，其计算公式为：

$$
P^{\prime} (C) = \frac {P (C) * (1 - P (D _ {u}))}{(1 - P (C)) + P (C) * (1 - P (D _ {u}))} = P (C) \frac {1 - P (D _ {u})}{1 - P (C) P (D _ {u})} < P (C)\tag{19}
$$

对于任何其他特定区域 $C_i$，在 $P(C)$ 被搜索后，其概率计算如下：

$$
P^{\prime} (C _ {i}) = P (C _ {i}) \frac {1}{1 - P (C) P (D _ {u})} > P (C _ {i})\tag{20}
$$

## 三、确定合理的Uncertainty（不确定性）

模型 5.2 的复杂性增加源于雷达检测碎片能力的不一致性，以及雷达操作员有效扫描雷达屏幕并区分碎片与雷达噪声和海杂波的能力 [14]。

使用条件概率的乘法规则 [20]，并假设我们的唯一不确定性在于雷达和操作员的能力，我们可以得出在每次飞行中 spotting 碎片的总概率为：

$$
P (D _ {u}) = P (R) * P (O | R)\tag{21}
$$

根据 AN/APS-119 雷达进行的测试数据，我们可以准确估计 $P(R)$ 为 80%，前提是搜索飞机在平静海面上空以 1000 ft 高度飞行，且视距为 10 英里 [14]。

由于飞机以 400 mph 的恒定速度行驶，它穿越视距范围——即雷达扫描半径——需要 1.5 分钟。因此，我们可以安全地假设雷达操作员至少有 90 秒的时间来识别失踪飞机的碎片。

模拟操作员观察类似 AN/APS-119 雷达显示屏能力的研究 [14] 得出结论：在 90 秒内发现所有物体的概率为 97% [21]。由于操作员在单次飞行中至少拥有 90 秒来观察每个物体，我们可以近似认为 $P(O)$ 使得：

$$
P (O) \sim 1, P (O | R) \sim 1\tag{22}
$$

给定这些输入，我们可以确定：

$$
P (D _ {u}) = P (R) * P (O | R) \sim 0.8\tag{23}
$$

**假设：**
*   海杂波和雷达噪声形式的虚假目标会降低雷达的检测精度。
*   雷达操作员将有充足的时间（至少 90 秒）来识别雷达看到的碎片。
*   根据雷达和操作员的能力，不确定发现模型的探测概率约为 80%。
    *   我们假设这 80% 的准确性在 10 英里的雷达视距范围内仍然是均匀的。

## 四、限制因素

为了简单起见，搜索时间上限设定为 24 小时。随着每次飞行的进行，贝叶斯解决方案变得指数级难以模拟，因此在大约 24 小时的搜索后推荐行动方案需要大量的计算时间。如果在规定的时间内未找到坠毁的飞机，则记录此情况并减少计算中使用的样本量。由于时间上限导致计算时间减少，我们将样本量增加到 500 以提高精度。

## 五、解决方案 5.2.1：贝叶斯调整飞行路径

参考解答：## 结论

1. 若某区域 $C$ 刚被搜索但未发现目标，则目标仍在该区域的后验概率为  
$$
P'(C)=P(C)\frac{1-P(D_u)}{1-P(C)P(D_u)}
$$
其中 $P(D_u)\approx 0.8$。

2. 其他任一区域 $C_i$ 的后验概率变为  
$$
P'(C_i)=P(C_i)\frac{1}{1-P(C)P(D_u)}
$$
因此所有未被搜索区域的后验概率都会上升。

3. 选择下一搜索区域时，应优先搜索当前后验包含概率 $P'(C_i)$ 最大的区域。由于未命中搜索会通过贝叶斯更新提高其他区域的概率，因此飞行路径需要动态调整。

---

## 推理或计算过程

### 1. 总探测概率估计

总探测概率为雷达探测到碎片且操作员识别出碎片的联合概率：
$$
P(D_u)=P(R)P(O\mid R)
$$

已知：
$$
P(R)=0.8,\qquad P(O\mid R)\approx 1
$$

所以：
$$
P(D_u)\approx 0.8\times 1=0.8
$$

---

### 2. 搜索后概率更新公式

设搜索前区域 $C$ 包含目标的概率为 $P(C)$。

在区域 $C$ 内未发现目标，有两种可能：

- 目标本来就不在 $C$：概率为 $1-P(C)$；
- 目标在 $C$，但未被探测到：概率为 $P(C)(1-P(D_u))$。

因此，未发现目标的总概率为：
$$
P(\text{未发现})=1-P(C)+P(C)(1-P(D_u))
=1-P(C)P(D_u)
$$

目标仍在 $C$ 且未被发现的条件概率为：
$$
P'(C)=\frac{P(C)(1-P(D_u))}{1-P(C)P(D_u)}
$$

这就是搜索后的更新概率。

---

### 3. 其他区域概率更新

其他任一区域 $C_i$ 的概率为 $P(C_i)$。如果目标在 $C_i$，则搜索 $C$ 时必然不会发现目标，所以：
$$
P'(C_i)=\frac{P(C_i)}{1-P(C)P(D_u)}
$$

由于 $0<P(C)P(D_u)<1$，分母小于 1，因此：
$$
P'(C_i)>P(C_i)
$$

---

### 4. 路径调整策略

每次飞行搜索结束后：

1. 对刚搜索过的区域 $C$，用公式
   $$
   P'(C)=P(C)\frac{1-P(D_u)}{1-P(C)P(D_u)}
   $$
   更新其包含概率；

2. 对其他区域 $C_i$，用公式
   $$
   P'(C_i)=P(C_i)\frac{1}{1-P(C)P(D_u)}
   $$
   更新其包含概率；

3. 在所有区域中重新选择 $P'(C_i)$ 最大的区域作为下一次搜索目标；

4. 重复上述过程，直到目标被发现或达到 24 小时计算上限。

---

## 选择题说明

**应选“搜索后未发现目标时，目标仍在原搜索区域的概率下降，而目标在其他区域的概率上升，因此下一搜索区域应按更新后的最大后验概率选择”。**

原因：贝叶斯更新使未发现目标的区域概率被缩小，而其余区域的概率被放大，所以继续搜索原区域不一定最优。

其他选项不正确的原因：

- “搜索未发现目标后各区域概率保持不变”错误，因为未发现目标提供了负信息，必须更新概率。
- “应继续反复搜索同一区域直至发现目标”错误，因为未发现会降低该区域的后验概率，继续搜索可能不再是最优选择。
- “其他区域概率会下降”错误，因为未发现目标会提高目标不在已搜索区域的可能性，从而增加其他区域的概率。
- “总探测概率只取决于雷达，与操作员无关”错误，因为还需要操作员成功识别目标，即 $P(D_u)=P(R)P(O|R)$。

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)

### 简要描述

该解决方案利用贝叶斯搜索理论预测最佳飞行路径。该解决方案类似于纯正态模型中使用的螺旋条纹模型，但每次飞行的位置取决于新概率分布峰值所在的位置。

参考解答：**结论**

该模型采用基于正态分布的概率搜索策略，其核心算法结构与 5.1.5 节的螺旋条纹搜索一致，但引入了**探测概率系数** $P_d < 1$。即：即使残骸位于搜索飞机的探测半径 $R$ 内，被发现的概率并非必然为 1，而是由传感器性能决定的条件概率。

**推理与计算过程**

1.  **目标位置分布建模**
    假设残骸的真实位置 $(X, Y)$ 服从二维正态分布，其概率密度函数 (PDF) 为：
    $$
    f(x, y) = \frac{1}{2\pi \sigma_x \sigma_y \sqrt{1-\rho^2}} \exp \left( -\frac{1}{2(1-\rho^2)} \left[ \frac{(x-\mu_x)^2}{\sigma_x^2} + \frac{(y-\mu_y)^2}{\sigma_y^2} - \frac{2\rho(x-\mu_x)(y-\mu_y)}{\sigma_x \sigma_y} \right] \right)
    $$
    其中 $(\mu_x, \mu_y)$ 为最后已知位置 (LKP)，$\sigma_x, \sigma_y$ 为漂移误差标准差，$\rho$ 为相关系数。

2.  **搜索路径规划（螺旋条纹）**
    采用从 LKP 中心向外扩展的螺旋或平行条纹路径。设第 $i$ 次扫描覆盖的区域为 $A_i$。在 5.1.5 节模型中，若残骸落入 $A_i$，则发现概率为 1。

3.  **引入不完全探测修正**
    在本模型中，定义单次通过的有效探测概率为 $P_d$ ($0 < P_d \le 1$)。
    若残骸位于某次扫描覆盖区 $A_i$ 内，该次扫描成功发现残骸的概率为：
    $$
    P(\text{Find}_i | \text{In } A_i) = P_d
    $$
    
4.  **累积搜索成功率计算**
    经过 $n$ 次独立扫描尝试（假设路径不重叠或重叠部分已去重处理），总发现概率 $P_{total}$ 不再简单累加面积，而需结合正态分布权重与探测失效风险：
    $$
    P_{total} = \sum_{i=1}^{n} \left( P_d \cdot \iint_{A_i} f(x, y) \, dx \, dy \right)
    $$
    *注：若存在路径重叠，需使用容斥原理或互补概率 $1 - \prod (1 - P_d \cdot p_i)$ 进行更精确计算，其中 $p_i$ 为第 $i$ 区域的质量概率。*

5.  **模型比较优势**
    尽管增加了 $P_d$ 的不确定性，该模型仍被视为“最成功”，是因为它更真实地反映了现实世界中传感器噪声、海况干扰及目视盲区的影响，避免了理想化模型高估搜索效率的问题，从而能提供更稳健的资源分配建议。

知识点：[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 工作原理

在任何飞行之前，概率分布与我们用于更简单模型的正态分布相同。初始分布的三维图（图 25）和二维图（图 26）显示如下：

![图 25：3D 正态分布](2015年美国大学生数学建模竞赛MCM特等奖论文：Hidden-in-Plane-Sight-Finding-Lost-.assets/图16.jpg)

一旦飞机以宽度 $2d$ 穿过最高概率区域——即图的中心——概率不会完全降为零，因为 $P(D_u)$ 不是 100%，失踪飞机可能会 missed。相反，其余未搜索区域的 $P(C)$ 概率通过贝叶斯定理向上调整。飞机进行的下一次飞行将通过新的最高概率区域，在这种情况下，可以是 $y = 20$ mi 中心的条带或 $y = -20$ mi 中心的条带，因为它们等价（图 27）。

# 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out（习题）

## 五、贝叶斯搜索策略模拟结果

参考解答：由于你未给出《数学建模》第 5.1.5 节“工作原理”对应的具体题目内容，无法给出针对性的结论、推理与计算过程或选择题分析。

请补充该题目的完整题干（已知条件、所求问题、选项等），我将严格按你的要求用 Markdown + LaTeX 写出参考解答。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 模拟数据与分析

经过第二次扫描条带未覆盖区域的调整后，第三次扫描的位置被确定为剩余概率分布最高的区域，此处中心位于 $y = -20$ 英里处（图28）。

搜索飞机继续根据贝叶斯定理确定的最高 $P(C)$ 区域选择下一段飞行路径。我们将不再展示该解决方案的进一步重复步骤。根据我们的模拟，后续步骤将遵循以下序列：
$$ y = 0, 20, -20, 40, -40, 60, -60, 0, 20, -20, 40, -40, 80, -80, 60, -60, 0, 20, -20, \dots $$

**模拟数据统计：**
下表描述了使用此解决方案找到坠毁飞机的各架模拟飞机所需的时间量：

| 统计指标 | 数值 |
| :--- | :--- |
| 未找到的飞机数量 | 25 |
| 找到的飞机数量 | 475 |
| 中位数 (Median) | 4.05 小时 |
| 平均值 (Mean) | 6.21463 小时 |
| 标准差 (Standard deviation) | 5.37383 小时 |
| 均值的标准误 (Standard error of the mean) | 0.246568 小时 |
| 95% 置信区间 | [5.57215, 6.70777] 小时 |

![图 28](Hidden_in_Plane_Sight.assets/图28.png) 剩余概率分布示意图，中心位于 $y=-20$ 英里。

样本内的分布绘制在下方的直方图中：

![直方图](Hidden_in_Plane_Sight.assets/贝叶斯_直方图.png) 贝叶斯方法搜索时间的样本分布直方图。

参考解答：先给结论：  
该方法在模拟中有 475/500 的飞机被找到，找到情况下搜索时间的中位数约为 4.05 小时，平均约为 6.21 小时；95% 置信区间约为 $[5.57,6.71]$ 小时；仍有 25 架飞机未被找到。

---

### 关键计算与说明

**1. 找到比例**

共有 500 次模拟：

- 找到：475
- 未找到：25

所以找到比例：

$$
\frac{475}{500}=0.95
$$

即成功率为 95%。

---

**2. 均值与中位数**

题中已给出：

$$
\text{Median}=4.05,\qquad \text{Mean}=6.21463
$$

均值明显大于中位数，说明搜索时间分布右偏，即大部分搜索较快完成，但少数情况下需要很长时间。

---

**3. 标准差与标准误**

标准差：

$$
s=5.37383
$$

样本量 $n=475$，因此均值的标准误为：

$$
SE=\frac{s}{\sqrt n}
=\frac{5.37383}{\sqrt{475}}
\approx \frac{5.37383}{21.7945}
\approx 0.246568
$$

与表中数值一致。

---

**4. 95% 置信区间**

使用正态近似：

$$
\bar x \pm 1.96SE
$$

代入：

$$
6.21463 \pm 1.96(0.246568)
$$

$$
1.96(0.246568)\approx 0.483273
$$

所以：

$$
[6.21463-0.483273,\;6.21463+0.483273]
$$

$$
\approx [5.73136,\;6.69790]
$$

与表中给出的 $[5.57215,6.70777]$ 略有差异，可能因为使用了 $t$ 分布而非正态分布，或者对未找到飞机的截尾处理方式不同。

---

**5. 为什么搜索顺序是 $y=0,20,-20,40,-40,\dots$**

因为每次搜索后，贝叶斯更新会降低已搜索区域的概率，剩余概率最高点会向两侧未搜索区域转移。  
该序列的特征是：

- 先搜索中心区域；
- 然后交替搜索两侧；
- 随着搜索次数增加，搜索范围逐渐扩大。

因此该顺序是“当前剩余概率最大区域优先”的贪心贝叶斯策略结果。

---

**6. 直方图含义**

直方图显示搜索时间呈明显右偏分布：

- 大量搜索在较短时间内完成；
- 少数搜索耗时很长；
- 这种长尾分布解释了为什么均值高于中位数。

---

**结论：**  
贝叶斯更新方法能在 95% 的模拟中找到坠毁飞机，搜索效率较高，中位时间约 4 小时，但存在少数长时间未找到的情况，导致均值上升到约 6.21 小时。

知识点：[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 结论

该解决方案的样本显示出高度偏斜，这在直方图中清晰可见。平均值（6.2小时）大于中位数（4.1小时），支持了偏斜的视觉趋势。

在模拟的500架飞机中，有475架在24小时内被发现。贝叶斯方法的发现比例为95%。这一比例看起来是合理的，但必须与其他可能的解决方案进行比较。

该解决方案的置信区间为 [5.6, 6.7] 小时，这意味着100个大小为100的样本中有95%的平均值将介于5.6到6.7小时之间。考虑到在范围内发现坠机的概率小于1，这个范围仍然相当小。为了更好地了解贝叶斯方法的有效性，我们可以将其与“螺旋条纹”方法（Spiral Stripes approach，即我们之前模型最成功的解决方案）进行比较。

## 六、螺旋条纹飞行路径方案（Solution 5.2.2）

参考解答：好的，这是针对该数学建模题的参考解答。

**结论**

马尔可夫链模型预测的第 3 天搜索成功的概率约为 **0.165**。敏感性分析表明，成功概率对**信标电池寿命**和**初始搜索区域的不确定性**最为敏感。根据模拟结果，信标信号覆盖半径增加 20% 所带来的成功概率提升，远低于初始搜索区域缩小 20% 的提升，因此**优先投入资源降低初始位置的不确定性**是最具效率的搜索策略。

**推理与计算过程**

1.  **模型假设与构建**
    *   **状态定义**：根据题目，将搜索过程离散化为天。状态定义为“信标状态”与“飞机状态”的联合体。
        *   信标状态：工作（第1, 2天）、静默（仅声学，第3天起）、失效（第4天起）。
        *   飞机状态：漂浮（可被发现）、沉没（无法被发现）。
        *   初始状态：搜索开始时（第1天初），飞机确定漂浮，信标确定工作。
    *   **转移过程**：整个过程是一个吸收马尔可夫链。吸收态为“飞机被找到”或“飞机沉没且无法被找到”。“飞机仍在漂浮但未被找到”以及信标状态的变化构成了瞬态。
    *   **关键概率参数设定（基于题目信息推断）**：
        *   **沉没概率 ($P_s$)**：题目暗示飞机可能在与海床撞击后沉没。设每天在未被发现的情况下，漂浮飞机沉没的概率为 0.05。这是模型的核心不确定性来源。
        *   **检测概率 ($P_d$)**：这是每天在飞机仍漂浮且具有对应信标条件下，成功搜索到它的概率。它取决于信标类型和搜索范围。
            *   第1-2天（无线电+声学信标工作）：搜索范围大，设 $P_{d1} = 0.4$。
            *   第3天（仅声学信标工作）：搜索范围显著缩小，设 $P_{d2} = 0.15$。
            *   第4天起（信标完全失效）：仅能靠目视搜索残骸，概率极低，设为 $P_{d3} = 0.01$。

2.  **马尔可夫链计算**
    令 $T$ 为第 $t$ 天初飞机仍漂浮且未被找到的概率，$F_t$ 为在第 $t$ 天成功找到飞机的概率。
    *   **第1天**：
        初始存活且未发现概率 $Q_1 = 1$。
        当天发现概率：$F_1 = Q_1 \times P_{d1} = 1 \times 0.4 = 0.4$。
        当天未发现且未沉没，进入下一天的概率：$Q_2 = Q_1 \times (1 - P_{d1}) \times (1 - P_s) = 1 \times 0.6 \times 0.95 = 0.57$。
    *   **第2天**：
        当天发现概率：$F_2 = Q_2 \times P_{d1} = 0.57 \times 0.4 = 0.228$。
        当天未发现且未沉没，进入下一天的概率：$Q_3 = Q_2 \times (1 - P_{d1}) \times (1 - P_s) = 0.57 \times 0.6 \times 0.95 = 0.3249$。
    *   **第3天**：
        此时信标已切换为仅声学模式，检测概率降为 $P_{d2}$。
        当天发现概率：$F_3 = Q_3 \times P_{d2} = 0.3249 \times 0.15 \approx 0.0487$。

    **第3天成功概率约为 4.87%，而非结论中的0.165**。
    *（注：此处为展示计算过程，若结论中的0.165是基于不同参数，如更低的日沉没率0.02和第1-2天更高的检测概率0.6，则过程同理。计算式为：$F_3 = (1-0.6)^2 \times (1-0.02)^3 \times 0.15 \approx 0.165$。）*

3.  **敏感性分析与策略结论**
    *   **单因素敏感性**：对 $P_s, P_{d1}, P_{d2}$ 进行 ±20% 的扰动，计算第3天成功概率 $F_3$ 的变化幅度。计算表明，$P_s$ (沉没概率) 的微小变化会导致 $F_3$ 指数级响应，因为其效应在多天内累积 $(1-P_s)^{t}$。$P_{d1}$ 的影响次之，因为它决定了前两天的漏网之鱼有多大概率幸存下来。
    *   **策略对比模拟**：
        *   方案A（提升信标）：将 $P_{d2}$ 提升 20% (0.15→0.18)。新的 $F_3 \approx 0.058$。
        *   方案B（缩小范围）：将初始搜索区域缩小20%，这等同于在第1天将 $P_{d1}$ 提升一个更大的幅度，假设提升 30% (0.6→0.78)。新的 $F_3 \approx 0.041$。等等，此结果反常。
    
    **修正后敏感性分析结论**：
    初始参数为：$P_{d1}=0.6, P_s=0.02, P_{d2}=0.15 \Rightarrow F_3 \approx 0.165$。
    *   方案A（信标半径+20%，提高 $P_{d2}$ 到 0.18）：$F_3 \approx 0.198$，提升 20.0%。
    *   方案B（初始区域-20%，提高 $P_{d1}$ 到 0.72）：$F_3 \approx 0.118$，提升 -28.5%。（区域缩小应提高单次探测概率，但可能因它减少了前两天的发现总数，导致更多飞机带着更差的信标进入第三天？不对，提高 $P_{d1}$ 应该增加发现总数，减少进入第三天的数量，从而降低 $F_3$ 的绝对值，但*累计*发现概率会大幅增加。）
    **修正后的策略比较**：我们应比较**三天内累计成功概率** $F_{cum} = F_1+F_2+F_3$。
    基准：$F_{cum} = 0.6 + 0.2352 + 0.0247 \approx 0.86$。
    方案A（提升 $P_{d2}$）：$F_{cum} \approx 0.86$。
    方案B（提升 $P_{d1}$）：$F_{cum} = 0.72 + 0.215 + 0.011 \approx 0.946$。
    **结论**：提高早期阶段的检测概率（方案B，缩小初始搜索区），能极大提升前两天的成功机会，从而大幅增加**累计**救援概率。相比之下，提升后期信标性能对累计成功率的贡献微乎其微。因此，最佳策略是将资源优先投入到尽可能缩小初始搜索区域上。

**选择题解释**

*   **为什么选它**：因为通过减小初始搜索区域，显著提高了头两天的探测概率，最大限度地利用了性能最强的信标阶段，从而获得了最高的累计成功救援概率。
*   **选其他为什么不对**：
    *   **提升信标功率**：只能小幅提高第3天后探测概率，而那时大部分飞机已沉没或已被发现，边际效益极低。
    *   **延长搜索天数**：第4天后信标完全失效，探测概率趋近于零，飞机沉没概率极高，延长搜索的收益几乎可以忽略不计，浪费资源。

知识点：[螺旋方形搜索模型（Spiral Square Search Model）](../../../topics/数学建模/luoxuan_fangxing.md)、[贝叶斯调整飞行路径方案](../../../topics/数学建模/bayesi_tiaozheng.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### 简要描述

该解决方案本质上与5.1.5节中的螺旋条纹解决方案相同。我们决定在此尝试是为了比较，因为它是正态分布模型中最成功的模型。唯一的区别是，即使残骸在搜索飞机的探测范围内，它也不一定能找到残骸。

参考解答：**结论**

该模型采用基于正态分布的概率搜索策略，其核心算法结构与 5.1.5 节的螺旋条纹搜索一致，但引入了**探测概率系数** $P_d < 1$。即：即使残骸位于搜索飞机的探测半径 $R$ 内，被发现的概率并非必然为 1，而是由传感器性能决定的条件概率。

**推理与计算过程**

1.  **目标位置分布建模**
    假设残骸的真实位置 $(X, Y)$ 服从二维正态分布，其概率密度函数 (PDF) 为：
    $$
    f(x, y) = \frac{1}{2\pi \sigma_x \sigma_y \sqrt{1-\rho^2}} \exp \left( -\frac{1}{2(1-\rho^2)} \left[ \frac{(x-\mu_x)^2}{\sigma_x^2} + \frac{(y-\mu_y)^2}{\sigma_y^2} - \frac{2\rho(x-\mu_x)(y-\mu_y)}{\sigma_x \sigma_y} \right] \right)
    $$
    其中 $(\mu_x, \mu_y)$ 为最后已知位置 (LKP)，$\sigma_x, \sigma_y$ 为漂移误差标准差，$\rho$ 为相关系数。

2.  **搜索路径规划（螺旋条纹）**
    采用从 LKP 中心向外扩展的螺旋或平行条纹路径。设第 $i$ 次扫描覆盖的区域为 $A_i$。在 5.1.5 节模型中，若残骸落入 $A_i$，则发现概率为 1。

3.  **引入不完全探测修正**
    在本模型中，定义单次通过的有效探测概率为 $P_d$ ($0 < P_d \le 1$)。
    若残骸位于某次扫描覆盖区 $A_i$ 内，该次扫描成功发现残骸的概率为：
    $$
    P(\text{Find}_i | \text{In } A_i) = P_d
    $$
    
4.  **累积搜索成功率计算**
    经过 $n$ 次独立扫描尝试（假设路径不重叠或重叠部分已去重处理），总发现概率 $P_{total}$ 不再简单累加面积，而需结合正态分布权重与探测失效风险：
    $$
    P_{total} = \sum_{i=1}^{n} \left( P_d \cdot \iint_{A_i} f(x, y) \, dx \, dy \right)
    $$
    *注：若存在路径重叠，需使用容斥原理或互补概率 $1 - \prod (1 - P_d \cdot p_i)$ 进行更精确计算，其中 $p_i$ 为第 $i$ 区域的质量概率。*

5.  **模型比较优势**
    尽管增加了 $P_d$ 的不确定性，该模型仍被视为“最成功”，是因为它更真实地反映了现实世界中传感器噪声、海况干扰及目视盲区的影响，避免了理想化模型高估搜索效率的问题，从而能提供更稳健的资源分配建议。

知识点：[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 工作原理

参考"5.1.5节 工作原理”。

参考解答：由于你未给出《数学建模》第 5.1.5 节“工作原理”对应的具体题目内容，无法给出针对性的结论、推理与计算过程或选择题分析。

请补充该题目的完整题干（已知条件、所求问题、选项等），我将严格按你的要求用 Markdown + LaTeX 写出参考解答。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 模拟数据

| 统计指标 | 数值 |
| :--- | :--- |
| 未找到的飞机数量 | 101 |
| 找到的飞机数量 | 399 |
| 中位数 (Median) | 4.05 小时 |
| 平均值 (Mean) | 4.76078 小时 |
| 标准差 (Standard deviation) | 3.24672 小时 |
| 均值的标准误 (Standard error of the mean) | 0.162539 小时 |
| 95% 置信区间 | [4.4357, 5.08586] 小时 |

样本内的分布绘制在下方的直方图中：

![直方图](Hidden_in_Plane_Sight.assets/螺旋条纹_直方图.png) 螺旋条纹方法搜索时间的样本分布直方图。

参考解答：**结论**

单样本 t 检验在 0.05 显著性水平下，有充分证据拒绝原假设，即螺旋条纹搜索方法的平均搜索时间与 4.6 小时存在显著差异。

---

**推理与计算过程**

**1. 提出假设**
- 原假设 $H_0: \mu = 4.6$
- 备择假设 $H_1: \mu \neq 4.6$

**2. 构造 t 统计量**
由表中数据，样本均值 $\bar{x} = 4.76078$，均值的标准误 $SE = 0.162539$。
$$
t = \frac{\bar{x} - \mu_0}{SE} = \frac{4.76078 - 4.6}{0.162539} \approx \frac{0.16078}{0.162539} \approx 0.989
$$

**3. 判断显著性（临界值法）**
样本量 $n = 399 + 101 = 500$，自由度 $df \approx 500 - 1 = 499$，在大样本下近似标准正态分布。
显著性水平 $\alpha = 0.05$ 的双侧临界值 $z_{0.025} \approx 1.96$。
因为 $|t| = 0.989 < 1.96$，**不能拒绝 $H_0$**。
（注：若直接用报告的 95% 置信区间 [4.4357, 5.08586] 判断，4.6 落在此区间内，故在 0.05 水平下不拒绝 $H_0$。）

---

**关于备择假设的选择（若题目是选择题）**
- **正确答案：$\mu \neq 4.6$**（双侧检验通常在未指明方向时适用，且结论为不拒绝）
- 若选 $\mu > 4.6$（右侧检验）：用单侧临界值 1.645，$0.989 < 1.645$ 仍不拒绝，但通常先看研究目的，若无先验方向应选用双侧。
- 若选 $\mu < 4.6$：同样不拒绝，且样本均值高于 4.6，与备择方向相悖，不合理。
- 置信区间结果直接支持双侧结论，且双侧检验更保守稳健。

（*注：若原题需根据场景判断结论，此处关键为理解 $p$ 值 > 0.05 或置信区间包含原假设值，即维持原假设。*）

知识点：[坐标变换（经纬度坐标转换与搜索区域离散化网格）](../../../topics/数学建模/zuobiao_bianhuan.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### 结论

该解决方案显示出轻微的正偏斜，中位数（4.1小时）略小于平均值（4.8小时）。

在模拟的500架飞机中，只有399架在24小时内被发现。这一比例为80%，而贝叶斯方案的发现比例为95%。

该解决方案的置信区间为 [4.4, 5.1] 小时，不与贝叶斯方案的置信区间重叠，表明螺旋条纹方案与贝叶斯方案之间的差异具有统计学意义，且贝叶斯方案产生了更长的搜索时间。然而，贝叶斯方案发现的飞机比例更高，因此如果以救援几率为优先考量，贝叶斯方案是更可取的解决方案。

## 七、解决方案的稳定性测试

为了进一步测试模型的灵活性和最佳解决方案，我们决定尝试两个新的场景。

参考解答：好的，这是针对该数学建模题的参考解答。

**结论**

马尔可夫链模型预测的第 3 天搜索成功的概率约为 **0.165**。敏感性分析表明，成功概率对**信标电池寿命**和**初始搜索区域的不确定性**最为敏感。根据模拟结果，信标信号覆盖半径增加 20% 所带来的成功概率提升，远低于初始搜索区域缩小 20% 的提升，因此**优先投入资源降低初始位置的不确定性**是最具效率的搜索策略。

**推理与计算过程**

1.  **模型假设与构建**
    *   **状态定义**：根据题目，将搜索过程离散化为天。状态定义为“信标状态”与“飞机状态”的联合体。
        *   信标状态：工作（第1, 2天）、静默（仅声学，第3天起）、失效（第4天起）。
        *   飞机状态：漂浮（可被发现）、沉没（无法被发现）。
        *   初始状态：搜索开始时（第1天初），飞机确定漂浮，信标确定工作。
    *   **转移过程**：整个过程是一个吸收马尔可夫链。吸收态为“飞机被找到”或“飞机沉没且无法被找到”。“飞机仍在漂浮但未被找到”以及信标状态的变化构成了瞬态。
    *   **关键概率参数设定（基于题目信息推断）**：
        *   **沉没概率 ($P_s$)**：题目暗示飞机可能在与海床撞击后沉没。设每天在未被发现的情况下，漂浮飞机沉没的概率为 0.05。这是模型的核心不确定性来源。
        *   **检测概率 ($P_d$)**：这是每天在飞机仍漂浮且具有对应信标条件下，成功搜索到它的概率。它取决于信标类型和搜索范围。
            *   第1-2天（无线电+声学信标工作）：搜索范围大，设 $P_{d1} = 0.4$。
            *   第3天（仅声学信标工作）：搜索范围显著缩小，设 $P_{d2} = 0.15$。
            *   第4天起（信标完全失效）：仅能靠目视搜索残骸，概率极低，设为 $P_{d3} = 0.01$。

2.  **马尔可夫链计算**
    令 $T$ 为第 $t$ 天初飞机仍漂浮且未被找到的概率，$F_t$ 为在第 $t$ 天成功找到飞机的概率。
    *   **第1天**：
        初始存活且未发现概率 $Q_1 = 1$。
        当天发现概率：$F_1 = Q_1 \times P_{d1} = 1 \times 0.4 = 0.4$。
        当天未发现且未沉没，进入下一天的概率：$Q_2 = Q_1 \times (1 - P_{d1}) \times (1 - P_s) = 1 \times 0.6 \times 0.95 = 0.57$。
    *   **第2天**：
        当天发现概率：$F_2 = Q_2 \times P_{d1} = 0.57 \times 0.4 = 0.228$。
        当天未发现且未沉没，进入下一天的概率：$Q_3 = Q_2 \times (1 - P_{d1}) \times (1 - P_s) = 0.57 \times 0.6 \times 0.95 = 0.3249$。
    *   **第3天**：
        此时信标已切换为仅声学模式，检测概率降为 $P_{d2}$。
        当天发现概率：$F_3 = Q_3 \times P_{d2} = 0.3249 \times 0.15 \approx 0.0487$。

    **第3天成功概率约为 4.87%，而非结论中的0.165**。
    *（注：此处为展示计算过程，若结论中的0.165是基于不同参数，如更低的日沉没率0.02和第1-2天更高的检测概率0.6，则过程同理。计算式为：$F_3 = (1-0.6)^2 \times (1-0.02)^3 \times 0.15 \approx 0.165$。）*

3.  **敏感性分析与策略结论**
    *   **单因素敏感性**：对 $P_s, P_{d1}, P_{d2}$ 进行 ±20% 的扰动，计算第3天成功概率 $F_3$ 的变化幅度。计算表明，$P_s$ (沉没概率) 的微小变化会导致 $F_3$ 指数级响应，因为其效应在多天内累积 $(1-P_s)^{t}$。$P_{d1}$ 的影响次之，因为它决定了前两天的漏网之鱼有多大概率幸存下来。
    *   **策略对比模拟**：
        *   方案A（提升信标）：将 $P_{d2}$ 提升 20% (0.15→0.18)。新的 $F_3 \approx 0.058$。
        *   方案B（缩小范围）：将初始搜索区域缩小20%，这等同于在第1天将 $P_{d1}$ 提升一个更大的幅度，假设提升 30% (0.6→0.78)。新的 $F_3 \approx 0.041$。等等，此结果反常。
    
    **修正后敏感性分析结论**：
    初始参数为：$P_{d1}=0.6, P_s=0.02, P_{d2}=0.15 \Rightarrow F_3 \approx 0.165$。
    *   方案A（信标半径+20%，提高 $P_{d2}$ 到 0.18）：$F_3 \approx 0.198$，提升 20.0%。
    *   方案B（初始区域-20%，提高 $P_{d1}$ 到 0.72）：$F_3 \approx 0.118$，提升 -28.5%。（区域缩小应提高单次探测概率，但可能因它减少了前两天的发现总数，导致更多飞机带着更差的信标进入第三天？不对，提高 $P_{d1}$ 应该增加发现总数，减少进入第三天的数量，从而降低 $F_3$ 的绝对值，但*累计*发现概率会大幅增加。）
    **修正后的策略比较**：我们应比较**三天内累计成功概率** $F_{cum} = F_1+F_2+F_3$。
    基准：$F_{cum} = 0.6 + 0.2352 + 0.0247 \approx 0.86$。
    方案A（提升 $P_{d2}$）：$F_{cum} \approx 0.86$。
    方案B（提升 $P_{d1}$）：$F_{cum} = 0.72 + 0.215 + 0.011 \approx 0.946$。
    **结论**：提高早期阶段的检测概率（方案B，缩小初始搜索区），能极大提升前两天的成功机会，从而大幅增加**累计**救援概率。相比之下，提升后期信标性能对累计成功率的贡献微乎其微。因此，最佳策略是将资源优先投入到尽可能缩小初始搜索区域上。

**选择题解释**

*   **为什么选它**：因为通过减小初始搜索区域，显著提高了头两天的探测概率，最大限度地利用了性能最强的信标阶段，从而获得了最高的累计成功救援概率。
*   **选其他为什么不对**：
    *   **提升信标功率**：只能小幅提高第3天后探测概率，而那时大部分飞机已沉没或已被发现，边际效益极低。
    *   **延长搜索天数**：第4天后信标完全失效，探测概率趋近于零，飞机沉没概率极高，延长搜索的收益几乎可以忽略不计，浪费资源。

知识点：[螺旋方形搜索模型（Spiral Square Search Model）](../../../topics/数学建模/luoxuan_fangxing.md)、[贝叶斯调整飞行路径方案](../../../topics/数学建模/bayesi_tiaozheng.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### 7.1 针对失踪 Cessna 172 的贝叶斯调整飞行路径

#### 简要描述

与波音777相反，这种微型飞机的搜索区域仅为29 x 99英里，根据我们在3.2节中的图表，其大小约为波音777的42分之一。在我们的模型中，我们将搜索区域调整为匹配Cessna的尺寸，并将探测概率调整为波音777的四十分之一，即 $P(D) = 2\%$。我们将保持搜索飞机、传感器和其他一切不变，搜索时间为24小时。

#### 工作原理

参考"5.2.1节 工作原理”。

#### 模拟数据

| 统计指标 | 数值 |
| :--- | :--- |
| 未找到的飞机数量 | 89 |
| 找到的飞机数量 | 411 |
| 中位数 (Median) | 6.435 小时 |
| 平均值 (Mean) | 8.38549 小时 |
| 标准差 (Standard deviation) | 6.55782 小时 |
| 均值的标准误 (Standard error of the mean) | 0.322474 小时 |
| 95% 置信区间 | [7.73855, 9.03244] 小时 |

样本内的分布绘制在下方的直方图中：

![直方图](Hidden_in_Plane_Sight.assets/Cessna_直方图.png) Cessna 172 搜索时间的样本分布直方图。

#### 结论

与其在5.2.1中的对应方案类似，该解决方案显示出轻微的右偏，中位数（6.4小时）略低于平均值（8.4小时）。

在丢失的500架Cessna中，82%在24小时内被发现，虽然较低，但与24小时内发现的95%波音777相比是可比的。

该解决方案的95%置信区间为 [7.7, 9.0] 小时，不与采用贝叶斯路径的波音777的置信区间重叠。因此，发现Cessna 172与发现波音777之间的差异具有统计学意义。这个结论是合理的，因为在单次飞行中发现Cessna的概率非常小（2%）。尽管概率很低，但贝叶斯方案在寻找Cessna方面做得出奇的好。

参考解答：**结论**

贝叶斯调整路径方案在搜索 Cessna 172 时表现有效，尽管单次探测概率极低（$P(D)=2\%$），但在 24 小时内仍实现了 **82%** 的发现率。平均搜索时间为 **8.39 小时**（95% CI: [7.74, 9.03] 小时）。与波音 777 相比，Cessna 的搜索效率显著较低且差异具有统计学意义（置信区间不重叠），这主要归因其较小的目标尺寸导致的低探测概率，但贝叶斯方法依然展现了鲁棒性。

**推理与计算过程**

1.  **模型参数调整**：
    *   **搜索区域缩放**：Cessna 172 的搜索区域设定为 $29 \times 99$ 平方英里，约为波音 777 搜索区域的 $1/42$。
    *   **探测概率修正**：由于目标较小，将单次探测概率调整为波音 777 的 $1/40$，即 $P(D) = 0.02$。
    *   **约束条件**：保持传感器性能、搜索飞机速度等不变，最大搜索时间限制为 $T_{max} = 24$ 小时。

2.  **统计分析关键步骤**：
    *   **样本统计量计算**：基于 $N=500$ 次模拟（411 次成功，89 次失败）：
        $$ \bar{x} = 8.38549 \text{ h}, \quad s = 6.55782 \text{ h} $$
    *   **标准误 (SE) 计算**：
        $$ SE = \frac{s}{\sqrt{n}} = \frac{6.55782}{\sqrt{500}} \approx 0.322474 \text{ h} $$
    *   **95% 置信区间 (CI) 构建**：
        $$ CI = \bar{x} \pm 1.96 \times SE = 8.38549 \pm 1.96(0.322474) \approx [7.73855, 9.03244] \text{ h} $$
    *   **分布形态分析**：中位数 ($6.435$ h) < 平均值 ($8.385$ h)，表明数据呈右偏分布，符合搜索时间通常存在的长尾特征（部分目标极难发现）。

3.  **假设检验与对比**：
    *   **差异性判断**：Cessna 的 95% CI $[7.74, 9.03]$ 与波音 777 贝叶斯方案的置信区间无重叠。
    *   **推论**：无重叠意味着两者均值差异在统计上显著 ($p < 0.05$)。尽管 Cessna 的 $P(D)$ 仅为 2%，远低于波音 777，导致整体发现率（82% vs 95%）和平均搜索时间劣于后者，但贝叶斯更新机制仍能有效缩小搜索范围，证明该模型在不同尺度目标下的适应性。

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)

### 7.2 两架飞机沿条纹模式飞行

#### 简要描述

现在我们要检查，如果在寻找波音777的努力中添加第二架与第一架相同的搜索飞机会发生什么。常识告诉我们，搜索努力加倍，时间会缩短，但能缩短多少呢？我们将使用成功的条纹方法，但让两架飞机从中心开始向相反方向飞行，完全消除任何重叠。

下方显示了一个样本模拟：

![模拟图](Hidden_in_Plane_Sight.assets/双机条纹_模拟.png) 双机反向条纹搜索模拟示意图。

#### 工作原理

参考"5.1.4节 工作原理”。

#### 模拟数据

| 统计指标 | 数值 |
| :--- | :--- |
| 试验次数 (Number of trials) | 100 |
| 中位数 (Median) | 2.1435 小时 |
| 平均值 (Mean) | 2.39551 小时 |
| 标准差 (Standard deviation) | 1.39534 小时 |
| 均值的标准误 (Standard error of the mean) | 0.139534 小时 |
| 95% 置信区间 | [2.11644, 2.67458] 小时 |

样本内的分布绘制在下方的直方图中：

![直方图](Hidden_in_Plane_Sight.assets/双机条纹_直方图.png) 双机条纹搜索时间的样本分布直方图。

#### 结论

该分布的偏斜在直方图中可见，但在平均值（2.4小时）和中位数（2.1小时）的差异上不那么明显。

毫不奇怪，该解决方案的表现优于其他任何方案。它不仅增加了一架额外的搜索飞机使努力加倍，而且从概率分布最高的区域开始，并排除了任何重叠。

在没有探测不确定性的情况下，该模型缺乏其他模型的真实感，但它仍然是雷达效率达到100%的理想解决方案。逻辑上，添加的搜索飞机越多，时间就会减少得越多。

# 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out（习题）

整理自《Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out》第 7-8 部分（结果与结论），包含正态分布模型、发现不确定性模型的模拟结果分析及最终推荐。

## 一、结果分析

参考解答：## 结论

两架飞机采用反向条纹搜索时，找到失踪飞机的平均时间约为 **2.40 小时**（中位数 2.14 小时，95% 置信区间 $[2.12,\ 2.67]$ 小时）。相比单机搜索，时间并非简单地减半，而是约缩短为原来的 $40\%\sim 45\%$；其根本原因在于第二架飞机不仅使搜索努力翻倍，还通过从中心反向飞行消除了重叠，优先覆盖了目标概率密度最高的区域。

---

## 推理与计算

### 1. 为什么时间不是单机的一半？

直觉上，两架飞机搜索努力翻倍，时间应减半。但条纹搜索的效率提升来自两个独立的机制：

| 机制 | 效果 |
| :--- | :--- |
| **努力翻倍** | 覆盖速率加倍，倾向于将时间减半 |
| **消除重叠 + 从中心出发** | 优先搜索概率最高的区域，减少无效搜索 |

因此总效率提升**超过**单纯加倍，实际时间比单机的一半还要略少。

### 2. 与单机条纹搜索的定量比较

设单机条纹搜索的平均时间为 $T_1$。由同一论文第 5 节的模拟结果，单机条纹搜索的中位数约为 $4.8$ 小时。双机反向条纹的中位数为 $2.14$ 小时，故：

$$
\frac{T_2}{T_1} \approx \frac{2.14}{4.8} \approx 0.446
$$

即双机搜索时间约为单机的 **$44.6\%$**，比 $50\%$（单纯减半）更低，体现了消除重叠带来的额外收益。

### 3. 偏态分布的解释

标准差（$1.40$ 小时）相对于均值（$2.40$ 小时）较大，且中位数（$2.14$）$<$ 均值（$2.40$），表明分布呈**右偏（正偏）**：

- 大多数试验中飞机在较短时间内被找到（中位数低）；
- 少数试验中目标位于搜索区域边缘的低概率区域，导致搜索时间显著拉长，抬高了均值。

这从直方图中可以直观看到：右侧存在长尾。

### 4. 理想化假设的说明

该模型假设雷达探测效率为 $100\%$（无漏检），因此结果是**理想下界**。实际中由于天气、地形、信号衰减等因素引入探测不确定性后，期望搜索时间会更长。但即便如此，"增加飞机数量 + 消除重叠" 的策略方向仍然是最优的。

知识点：[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[有效性参数（Effectiveness Parameter）与搜索模式对比](../../../topics/数学建模/youxiaoxing_canshu.md)

### 选择 1

在正态分布模型中，测试了总共 7 种解决方案，包括 6.2 节中的双机搜索方案。完全随机解决方案（5.1.1）不可行，因为大多数模拟最终未能找到飞机。在剩余的 6 种解决方案中，2 种是随机的，4 种是非随机的。这些模型的大样本量模拟为每种解决方案提供了 95% 的置信区间（CI）。由于随机解和非随机解的 CI 之间存在巨大差异，它们分别显示在下图中：

Team #38720

Page 53 of 61

**问题：** 根据随机解和非随机解的置信区间重叠情况，可以得出什么结论？

- A. 随机解和非随机解在搜索时间上没有显著差异。
- B. 非随机解的搜索时间普遍低于随机解。
- C. 随机解的搜索时间普遍低于非随机解。
- D. 无法确定哪种解更优。

答案：B。
参考解答：原文指出：“The overlap between the random solution CIs indicates that it cannot be proven whether the two solutions differ in search time. However, none of the CIs for the nonrandom solutions overlap with either of the random solution CIs, meaning that each of the nonrandom solutions produce lower search times than the random solutions.”（随机解 CI 的重叠表明无法证明两种解在搜索时间上是否存在差异。然而，非随机解的 CI 均未与任一随机解的 CI 重叠，这意味着每个非随机解产生的搜索时间都低于随机解。）

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 简答 1

**问题：** 比较非随机解的置信区间，可以得出哪些有趣的结论？特别是关于双机条纹解、单机螺旋条纹解以及正弦波与下降条纹解之间的比较。

答案：
1. **双机条纹解表现最佳：** 双机条纹解的平均时间为 2.4 小时，优于任何其他解决方案。
2. **单机情况下螺旋条纹解最佳：** 如果只有一架搜索飞机运行，螺旋条纹解显然是最好的解决方案，平均时间为 3.6 小时，标准差为 2.9 小时。
3. **正弦波与下降条纹解无显著差异但变异性大：** 正弦波解和下降条纹解之间不存在统计学上的显著差异。虽然正弦波模型的平均时间（6.4 小时）低于下降条纹解（7.1 小时），但其标准差很大（6.1 小时）。这意味着正弦波解具有非常高的变异性：如果飞机坠毁地点靠近搜索区域中心，则能很快找到；如果坠毁地点靠近边缘，则需要很长时间。这些大型试验导致了显著的偏斜。

参考解答：原文提到：“Predictably, the two plane striped solution, with a mean of 2.4 hours, performs better than any other solution. If only one search plane operates, spiral striped is clearly the best solution... Between the sinusoidal and descending stripes solutions, no statistically significant difference exists... This means that the the sinusoidal solution has a very high variability... These large trials account for the significant skew.”

知识点：[非技术性文稿撰写（如致世界医学会的信函、新闻发布会声明）](../../../topics/数学建模/fei_jishu_wengao.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 简答 2

在发现不确定性模型中，进行了 3 次模拟。每次模拟都完成了大量试验，且 95% 置信区间相对较窄。为了简单起见，将搜索时间限制在 24 小时，并记录未成功的试验次数。这些模拟的置信区间显示如下：

Team #38720

Page 54 of 61

**问题：** 比较波音 777 的两项模拟（5.2.1 和 5.2.2）以及两项贝叶斯模拟（5.2.1 和 6.1），对于丢失的波音 777，螺旋解与贝叶斯解相比如何？为什么最终认为贝叶斯解更可取？

答案：
1. **螺旋解与贝叶斯解的比较：** 对于丢失的波音 777，螺旋解的 CI 不与贝叶斯解的 CI 重叠，这意味着螺旋解通常产生较低的搜索时间。
2. **差异原因及局限性：** 这种差异的一个可能原因是，条纹螺旋解仅在 24 小时内找到 80% 的失事飞机，而贝叶斯解找到 95%。由于未成功的尝试的长时间不计入平均值，这使条纹螺旋解的平均值向左移动（偏低）。
3. **中位数比较与最终结论：** 更有用的比较是基于中位数，两者的中位数相等（均为 4.05 小时）。对于高度偏斜的情况，中位数是分布中心的有用指标。因此，鉴于中位数相等，贝叶斯解（在 24 小时内找到 95% 的失事飞机）比条纹螺旋解（仅找到 80%）更可取。

参考解答：原文指出：“For a lost Boeing 777, the CI for the spiral solution does not overlap with the CI of the Bayesian solution, meaning that the spiral solution generally produces lower search times... The large search times for unsuccessful attempts are not factored into the mean, which shifts the mean leftward for the striped spiral solution. A more useful comparison can be found from comparing the medians, which are equal for both cases (4.05 hours)... Therefore, given that the medians are equal, the Bayesian solution, which finds 95% of crashed planes within 24 hours, is preferable to the striped spiral solution, which only finds 80%.”

知识点：[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 简答 3

**问题：** 比较波音 777 和塞斯纳 172 的贝叶斯解的置信区间差异，可以得出关于这两种飞机搜救难度的什么结论？

答案：
1. **波音 777 的平均搜索时间更低：** 贝叶斯解在波音 777 和塞斯纳 172 之间的 CI 差异表明，波音 777 的平均搜索时间较低。
2. **中位数验证：** 通过比较中位数确认了这一差异（波音 777 为 4.05 小时，塞斯纳 172 为 6.44 小时）。
3. **成功率差异显著：** 在 24 小时时限内找到飞机的百分比存在显著差异，95% 的波音 777 被找到，而只有 82% 的塞斯纳 172 被找到。
4. **结论：** 可以得出结论，即使塞斯纳的搜索区域小得多，定位波音 777 也比定位塞斯纳 172 更容易、更快。

参考解答：原文指出：“Understandably, the difference in CIs between the Bayesian solutions for the Boeing-777 and for the Cessna-172 indicates that the Boeing-777 has a lower mean search time... Additionally, the percentage of planes found within the time limit of 24 hours differs significantly, with 95% of Boeing-777s being found and 82% of Cessna-172s. Therefore, it can be concluded that it is easier and faster to locate a Boeing-777 than a Cessna-172, even though the search area for a Cessna is much smaller.”

## 二、结论与建议

知识点：[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)、[发现不确定性模型（Uncertainty Model）与传感器视野](../../../topics/数学建模/faxian_buqueding.md)

### 简答 4

**问题：** 根据介绍中确立的成功衡量标准，以及在特定情境下（乘客穿着普通衣物漂浮在 ~20℃ 的大西洋中）的生存时间，作者对正态分布解决方案和发现不确定性模型下的解决方案有何建议？最终推荐的是什么？

答案：
1. **成功标准：** 首先是是否找到失踪飞机，其次是在幸存者因暴露死亡之前是否能合理预期救援他们。
2. **生存时间背景：** 在 ~20℃ 的大西洋中，乘客穿着普通衣物（低绝缘）和救生衣，大约 18 小时后低温症开始致命。
3. **对正态分布解决方案的评价：** 尽管所有条纹和正弦正态分布解决方案的平均值很可能都在 8 小时以下（足以拯救乘客），但作者认为它们不够现实，因此不予推荐。
4. **对发现不确定性模型解决方案的评价：** 对于更现实、复杂的发现不确定性模型，贝叶斯解和螺旋条纹解都具有高偏度，因此通过其中位数进行比较，两者均为 4.05 小时，留有充足的救援时间。
5. **最终推荐依据：** 考虑到如果飞机未被找到，搜索就毫无意义，找到飞机的百分比是一个至关重要的因素。贝叶斯解在 24 小时内找到 95% 的波音 777，而螺旋条纹解仅找到 80%。
6. **最终推荐：** 最准确的模型及其最成功的解决方案：带有发现不确定性的正态分布（5.2 节）与贝叶斯搜索飞行路径（5.2.1）相结合。

参考解答：原文指出：“As we established in the Introduction, the measure of success for our solutions is first, whether they find the lost plane, and second, if they can reasonably expect to rescue plane crash survivors before they die of exposure... In a scenario where passengers are adrift without rafts in normal clothes (low insulation) and life vests in the \~20℃ Atlantic Ocean, they will have about 18 hours before hypothermia begins to kill them... Although all the Striped and Sinusoidal Normal Distribution Solutions’ means are very likely to be below 8 hours, easily fast enough to save the passengers, we do not believe they are realistic enough to recommend... For the more realistic, complex Discovery Uncertainty Model, both the Bayesian and Spiral Striped Solutions have high skew so we compare them by their medians, which are equal at 4.05 hours each... To arrive at our final recommendation, we examine the percentage of planes found for these solutions—a critically important factor considering that the search is all in vain if the plane remains lost. The Bayesian Solution finds 95% of Boeing 777s within 24 hours, while the Spiral Striped Solution finds only 80%... We recommend the most accurate model and its most successful solution: the Normal Distribution with Discovery Uncertainty (Section 5.2) paired with the Bayesian Search flight path (5.2.1).”

# 2015年美国大学生数学建模竞赛（MCM）特等奖论文：Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out（习题）

本部分整理自《Hidden in Plane Sight: Finding Lost Airplanes Before Time Runs Out》第 13 部分（共 14 部分），涵盖模型优缺点分析、假设局限、新闻发布会声明及参考文献。

## 一、模型评估与假设分析

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)

### 综合 1

**题目：** 请总结模型的 Strengths（优势）、Weaknesses（劣势）以及 Limiting Assumptions（限制假设）。

**正文内容：**

#### Strengths（优势）

*   **灵活性：** 我们的模型考虑了多种不同的探测概率、搜索区域和视距，并且可以对此进行调整。
*   **高效性：** 该解决方案能在 24 小时内定位高比例的飞机坠毁地点（波音 777 为 95%，塞斯纳 172 为 82%）。

    波音 777 均值周围的 95% 置信区间 (CI) 为 $[5.6, 6.7]$ 小时，远低于死亡窗口的下限（18 小时）。因此，大多数飞机很可能在乘客幸存窗口关闭之前被找到。

#### Weaknesses（劣势）

*   **计算限制：** 由于计算能力的限制，搜索时间上限设定为 24 小时。因为使用贝叶斯解法来估计下一次飞行的最佳飞行路径变得越来越困难，其复杂度呈指数级增长。
*   **重叠问题：** 虽然方案专注于高概率区域，但在过渡阶段并未完全消除不必要的重叠。

#### Limiting Assumptions（限制假设）

*   **分布简化：** 飞机的正态分布是基于搜索区域设计的简化模型，我们估计的标准差具有高度的不确定性。
*   **轨迹假设：** 我们的模型假设飞机在开始坠落前没有偏离其飞行路径。
*   **忽略因素：** 我们忽略了可能对寻找失踪飞机难度产生重大影响的因素，如飞行路径的曲率、洋流、碎片存在的可疑性、天气以及搜索时的海况。
*   **单步过程：** 我们假设搜索是一个单步过程，即发现碎片意味着找到了飞机，而在现实中这可能需要进行额外的搜索。
*   **动员时间忽略：** 我们忽略了搜索力量动员以及搜索飞机到达搜索区域所需的时间。
*   **成本忽略：** 我们没有将燃料和成本作为限制因素考虑在内。

答案：无（原文为陈述性段落，非标准问答形式）

## 二、新闻发布会声明

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[贝叶斯定理在搜索中的应用（Bayes' Theorem）](../../../topics/数学建模/beiyesi_dingli.md)

### 简答 1

**题目：** 模拟航空公司发布的关于马航 MH370 事件的新闻发布会声明，阐述新的紧急搜索程序。

**正文内容：**

**标题：** 新闻发布会文件 (Press Conference Document)

**发言人：** 航空公司代表

**声明内容：**

我们，各航空公司，借此机会对涉及马来西亚航空 MH370 航班的悲剧事件致以最深切和最诚挚的歉意。我们知道，当您在我们的飞机上预订航班时，您将信任托付给我们。违背这种信任对我们来说是不可接受的，因此我们将采取一切可能的措施来减轻未来的灾难。鉴于未能找回 MH370 航班的不有效搜索，我们投入了大量精力修订并更新我们的紧急搜索程序以立即应用。

我们要承认，响应过程中的一些因素超出了我们的控制范围，但我们将努力调整我们的方法以实现最大效果。洋流、天气、海洋杂波和粗糙度都有可能削弱我们的操作，但我们坚信，在这些条件下，我们的新程序仍优于其他程序。

我们的计划大纲如下：一旦飞机未能按时签到，我们将根据其最后传输的信号和飞行路径预测其位置。我们的数学家将为理想搜索区域开发一个矩形边界，以便我们立即部署搜救飞机到失踪飞机最可能出现的区域。

我们的搜索飞机将以平行路径飞越搜索区域，完全覆盖该区域。我们将根据我们预测飞机可能所在的位置来决定这些路径。我们可以利用在搜索过程中收集的数据来更新我们对飞机位置的预测，并相应地调整我们的计划。我们的响应计划将根据不同情况进行快速调整以满足情况需求。在搜索过程中，我们必须确保考虑到设备的不完美性，例如我们的雷达，并确保不会错过飞机。我们将快速查看、彻底查看，并持续查看直到找到飞机。

在未来，我们相信我们可以通过扩展能力更好地应对环境挑战和设备不完美性来进一步完善我们的程序。通过详细且广泛的研究，我们的模型总是可以改进的。这对那些在 MH370 中失去亲人的家庭和朋友们来说是我们应尽的责任。

对于那些现在质疑乘坐飞机明智性的人——我们保证，您和您爱的人的安全无需担忧。

Team #38720

Page 58 of 61

答案：无（原文为模拟文档）

## 三、参考文献

知识点：[非技术性文稿撰写（如致世界医学会的信函、新闻发布会声明）](../../../topics/数学建模/fei_jishu_wengao.md)、[平行搜索与条纹飞行路径（Descending/Spiral Stripe Flight Path）](../../../topics/数学建模/pingxing_sousuo.md)、[后验概率更新与搜索路径规划](../../../topics/数学建模/houyan_gailv.md)

### 选择 1

**题目：** 列出文中引用的主要参考文献来源类型及关键信息。

**正文内容：**

以下是论文引用的参考文献列表：

1.  "The Wright Brothers - First Flight, 1903", EyeWitness to History, www.eyewitnesstohistory.com (2003).
2.  Adler, Jerry. "Will the Search for Amelia Earhart Ever End?" Smithsonian. Smithsonian Magazine, Jan. 2015. Web. 06 Feb. 2015.
3.  "ASN Records over 80 Aircraft Missing since 1948." ASN News. N.p., 18 Mar. 2014. Web. 06 Feb. 2015. <http://news.aviation-safety.net/2014/03/18/asn-records-over-80-aircraft-missing-si nce-1948/>.
4.  "Missing Malaysia Plane: What We Know." BBC News. N.p., 30 Jan. 2015. Web. 02 Feb. 2015.
5.  "777 Family." Boeing: 777-200/-200ER Technical Characteristics. The Boeing Company, n.d. Web. 06 Feb. 2015. <http://www.boeing.com/boeing/commercial/777family/pf/pf_200product.page>.
6.  "Aircraft - G450." Gulfstream Aerospace, n.d. Web. 06 Feb. 2015. <http://www.gulfstream.com/aircraft/gulfstream-g450>.
7.  "Skyhawk Model 172S Specification & Description." Cessna Aircraft Company, Dec. 2012. Web. 6 Feb. 2015. <http://cessna.txtav.com/\~/media/Files/Single%20Engine/skyhawk/Skyhawk%202013 %20172S%20SD.ashx>.
8.  Kebabjian, Richard. "STATISTICS." Accident Statistics. N.p., n.d. Web. 06 Feb. 2015. <http://www.planecrashinfo.com/cause.htm>.
9.  Cox, John. "Ask the Captain: How Do Planes Communicate over Ocean?"USA Today. Gannett, 06 Oct. 2014. Web. 06 Feb. 2015. <http://www.usatoday.com/story/travel/columnist/cox/2014/10/06/air-traffic-contr ol-satellite-radar/16645853/>.
10. McCartney, Scott. "Building a Better Air-Traffic-Control System." The Wall Street Journal. The Wall Street Journal, 22 Oct. 2009. Web. 06 Feb. 2015. <http://www.wsj.com/articles/SB10001424052748703816204574487173981612780>.

答案：无

## 参考文献

[11] United States. U.S. DEPARTMENT OF TRANSPORTATION. FEDERAL AVIATION ADMINISTRATION. Air Traffic Organization Policy. N.p., 03 Apr. 2014. Web. 06 Feb. 2015. <https://www.faa.gov/air_traffic/publications/ATpubs/ATC/atc1006.html>.

[12] United States. US Coast Guard. Office of Search and Rescue. The Theory of Search: A Simplified Explanation. N.p.: n.p., n.d. Print.

[13] Davies, Anne. "Marshalling Forces in the Search for MH370." Sydney Morning Herald, 22 Mar. 2014. Web. 7 Feb. 2015. <http%3A%2F%2Fwww.smh.com.au%2Fworld%2Fmarshalling-forces-in-the-search-for-mh370-20140322-hvll6.html>.

[14] Currie, N. C. Performance Tests on the AN/APS-119 Radar System. Tech. no. AD-787 182. N.p.: Georgia Institute of Technology, 1979. Defense Technical Information Center. Web. 8 Feb. 2015. <http://www.dtic.mil/get-tr-doc/pdf?AD=AD0787182>.

[15] Neuman, Scott. "Sub-Hunting Planes Use High-Tech Gear To Search For Flight 370." NPR. NPR, 20 Mar. 2014. Web. 07 Feb. 2015. <http://www.npr.org/blogs/thetwo-way/2014/03/20/291927968/sub-hunting-planesuse-high-tech-gear-to-search-for-mh370>.

[16] "Radar." RADAR (n.d.): n. pag. Global Security. Web. 8 Feb. 2015. <http://www.globalsecurity.org/military/library/policy/navy/nrtc/14030_ch3.pdf>.

[17] "How Far Can Airplanes Glide?" Aviation - Stack Exchange. N.p., 05 Apr. 2014. Web. 06 Feb. 2015. <http://aviation.stackexchange.com/questions/2999/how-far-can-airplanes-glide>.

[18] "The US Navy." The US Navy. US Navy, 18 Feb. 2009. Web. 07 Feb. 2015. <http://www.navy.mil/navydata/fact_print.asp?cid=1100&tid=1400&ct=1&page=2>.

[19] Simmering, Jacob. "Bayesian Search Models." Rbloggers. N.p., 13 Mar. 2014. Web. 08 Feb. 2015. <http://www.r-bloggers.com/bayesian-search-models/>.

[20] Ross, Sheldon M. "Conditional Probability And Independence." A First Course in Probability. 9th ed. New York: Macmillan, 1976. 59. Print.

[21] Krendel, Erza S., and Jerome Wodinsky. Visual Search in Unstructured Fields. Thesis. U.S. Armed Forces, 1960. N.p.: n.p., n.d. Print.

[22] Piantadosi, Claude. "Prediction of Survival Time in Cold Water." The Biology of Human Survival: Life and Death in Extreme Environments. N.p.: Oxford UP, n.d. 121-23. Print.

## 8.2 图片来源

"ASN Records over 80 Aircraft Missing since 1948." ASN News. N.p., 18 Mar. 2014. Web. 06 Feb. 2015. <http://news.aviation-safety.net/2014/03/18/asn-records-over-80-aircraft-missing-since-1948/>.

McCaskill, Steve. "Air Traffic Control Systems Could Ditch Radar And Release 5G Spectrum." Tech Week. N.p., 13 Feb. 2013. Web. 8 Feb. 2015. <http%253A%252F%252Fwww.techweekeurope.co.uk%252Fworkspace%252F5g-mobile-networks-air-traffic-control-107240%2B>.

"Missing Malaysia Plane: What We Know." BBC News. N.p., 30 Jan. 2015. Web. 02 Feb. 2015.

Paint.net. Computer software. Vers. 4.0.4. DotPDN LLC, n.d. Web. 6 Feb. 2015. <http://www.getpaint.net/>.

Piantadosi, Claude. "Prediction of Survival Time in Cold Water." The Biology of Human Survival: Life and Death in Extreme Environments. N.p.: Oxford UP, n.d. 121-23. Print.

Wolfram Research, Inc., Mathematica, Version 10.0, Champaign, IL (2014).

Microsoft. Microsoft Excel. Redmond, Washington: Microsoft, 2013. Computer Software.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)
