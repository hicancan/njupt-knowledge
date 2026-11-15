---
title: 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）
kind: 教材
course: 数学建模
source: batch-2:数学建模/2017年美国大学生数学建模竞赛O奖论文（全部）.zip/2017年美国大学生数学建模竞赛O奖论文（全部）/2017年美国大学生数学建模竞赛O奖论文（全部）/E/71672.pdf
---

# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

原件经识别和整理；“参考解答”是我们补的。

# Sustainable Cities Needed!（ICM E题）

2017年美国大学生数学建模竞赛O奖论文第1部分（摘要、目录及引言开头），基于识别内容整理。

## Summary (Team 71672)

The world is becoming increasingly urbanized - small cities are developing rapidly, and large cities are growing larger and more populated. By 2050, the percentage of people living in cities is expected to reach 66.4%, a 22% increase from today’s percentage [20]. Cities in the United States and Australia will particularly notice the growth, with current urbanization rates of 82% and 90%, respectively. Principles of smart growth can be used to address the issues of increased population. To address city plans for growth over the next 30 years, we first defined a metric to measure the success of smart growth. We used van Rijsbergen’s information retrieval effectiveness measure to combine pairs of quantitative measures of the growth principles that were significantly related. We then summed all of the resulting measures, under the assumption that each principle of smart growth was equally important. We applied this metric to the current growth plans of two cities: Boulder, CO, USA and Canberra, ACT, AUS. After evaluation of their current growth plans, we developed growth initiatives for both cities, and evaluated the expected outcomes of the new plans with our metric. For Boulder, these initiatives included rezoning land for mixed use, redeveloping residential areas, instituting vacancy taxes, increasing public transportation, and increasing community programming. For Canberra, the initiatives included rezoning new mixed use areas, partnering with private developers, increasing community engagement, and expanding bus routes. In both cities, we rated our proposed initiatives with our smart growth metric. Each city saw an increased score compared to the score the current city plan received. Our metric proves very easy to use: all that is needed is census data that is easily found. On the other hand, we note that our model may be oversimplified due to equal weighting of each growth measure, and the subjective nature of some of measures. Our growth plan for each city also proved inefficient in accommodating a 50% increase in population in each city. Additional data could be used to improve our proposed initiatives so that they could be effective for larger population increases and to improve our quantifying metric to better reflect how well the city is planning using smart growth principles.

## Contents

1. Introduction
2. A Metric for Smart Growth
3. Current Growth Plans
    3.1 Boulder, CO, USA
    3.2 Canberra, ACT, AUS
4. Proposed Growth Plans
    4.1 Boulder, CO, USA
    4.2 Canberra, ACT, AUS
    4.3 Comparing Initiatives
5. Population Increase
    5.1 Boulder, CO, USA
    5.2 Canberra, ACT, AUS
6. Model Strengths and Weaknesses
7. Conclusion

## List of Tables

| Table No. | Description | Page |
| :--- | :--- | :--- |
| 1 | Table of individual metrics and final success level for the current growth plan of Boulder, CO, USA | 8 |
| 2 | Table of individual metrics and final success level for the current growth plan of Canberra, ACT, AUS | 10 |
| 3 | Table of individual metrics and final success level for our proposed growth plan for Boulder, CO, USA | 13 |
| 4 | Table of individual metrics and final success level for our proposed growth plan for Canberra, ACT, AUS | 16 |
| 5 | Table of the effects of individual initiatives on success level for Boulder, CO, USA and Canberra, ACT, AUS | 17 |

## 1 Introduction

Smart growth is a strategy used to direct sustainable development of cities, particularly those that face rapid urbanization. Smart growth can be evaluated using the three E’s of sustainability - Economically prosperous, socially Equitable, and Environmentally Sustainable [2]. More specifically, smart growth can be defined in terms of ten principles [2]:

1. Mixed land uses
2. Taking advantage of compact building design
3. Creating a range of housing opportunities and choices
4. Creating walkable neighborhoods
5. Fostering distinctive, attractive communities with a strong sense of place
6. Preserving open space, farmland, natural beauty, and critical environmental area
7. Strengthening and directing development towards existing communities
8. Providing a variety of transportation choices
9. Making development decisions predictable, fair, and cost effective

# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

本资料整理自《2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）》教材第4–6页内容，由识别工具读取后修正错别字、断行及格式，保留原文核心逻辑与公式。

## 二、智慧城市增长指标体系构建

### 引言与总体方法

本研究选取了两个在智慧增长（Smart Growth）方面已做出显著努力且具有未来提升潜力的城市：**美国科罗拉多州博尔德市（Boulder, CO）**和**澳大利亚首都领地堪培拉市（Canberra, ACT）**。本文首先分析两市的当前增长状况，随后提出改进计划。

在第2节中，我们概述了一个用于量化每个城市智慧增长成功水平的指标（Metric）。该指标基于两市可用的数据构建，部分指标具有精确的数学定义。鉴于博尔德和堪培拉最新的增长计划分别制定或更新于2010年和2012年，我们决定使用当前的城市统计数据来评估这些计划的成功率。

为了合并相关性强的原则指标，我们采用了van Rijsbergen的信息检索效能度量公式 [9] 的修改版，将这些组合后的结果求和，并与最优值进行比较。这构成了我们衡量智慧增长计划成功水平的最终指标。

### 十项原则的具体指标定义

我们针对智慧增长的十项原则分别建立了一个指标，具体定义如下：

#### 选择 1：混合用地（Principle 1）
*   **原则描述**：关注混合用地（mixed use land）。
*   **指标定义**：计算城市分区为混合用地的土地面积与城市总土地面积的比率。
*   **最优值设定**：根据当前数据，确定该指标的最优可实现值为 $0.15$。

#### 选择 2：紧凑建设（Principle 2）
*   **原则描述**：关注建筑是否紧凑（building compactly）。
*   **指标定义**：引用文献 [17] 中计算欧洲城市紧凑度的方法，采用人口密度（人/平方英里）作为指标。考虑到即使到2050年人口增加50%，两座城市的人口密度也不会超过2000人/平方英里，因此将实际人口密度除以2000进行归一化处理。居住人数可直接反映建筑的紧凑程度。
*   **最优值设定**：该指标的最优值为 $1$。

#### 选择 3：多样化住房供应（Principle 3）
*   **原则描述**：关注多样化住房的可获得性（availability of diverse housing）。
*   **指标定义**：聚焦于经济适用房，考察各城市增长计划中计划新增住房中旨在永久保持可负担性的比例。
*   **最优值设定**：该指标的最优值为 $25\%$，即 $0.25$。

#### 选择 4：步行友好社区（Principle 4）
*   **原则描述**：强调社区应适合步行（walkable），即工作场所和商店应靠近住宅区。
*   **指标定义**：采用城市中步行上班的人口百分比作为指标。
*   **最优值设定**：最优值为 $25\%$（即 $0.25$），这一数值考虑了居住在混合用途区域及其周边的人群。此指标在逻辑上与“原则1"相关。

#### 选择 5：维护社区特色（Principle 5）
*   **原则描述**：发展和维护各个社区的独特特色（character of individual neighborhoods）。
*   **指标定义**：量化难度较大。我们通过检查城市增长计划中对这一目标的描述，并主观评价其对这一目标的投入程度，评分范围为 $0$ 到 $1$。
*   **最优值设定**：最优值为 $1$。

#### 选择 6：保护开放空间（Principle 6）
*   **原则描述**：保护开放空间、农田等（preserve open space, farmland, etc.）。
*   **指标定义**：计算城市中开放土地与总土地的比率。
*   **最优值设定**：基于所研究城市的当前开放空间水平，确定最优值为 $0.75$。

#### 选择 7：再开发现有社区（Principle 7）
*   **原则描述**：建议再开发现有社区，而不是在新土地上建设（绿色田野开发）（redeveloping existing communities instead of building on new land）。
*   **指标定义**：未找到关于各城市当前再开发程度的具体数据，因此根据增长计划中的既定目标，主观分配 $0$ 到 $1$ 的评分。
*   **最优值设定**：最优值为 $1$。由于原则7和原则5都涉及现有社区，我们将两者进行了关联。

#### 选择 8：提供替代交通方式（Principle 8）
*   **原则描述**：提供替代交通方式（providing alternative methods of transportation）。
*   **指标定义**：采用城市中使用替代交通方式（即不单独驾车）通勤上班的人口百分比。
*   **最优值设定**：最优值为 $100\%$，即 $1$。这与紧凑的建筑布局相关，因为紧凑布局可以为自行车道、行人步道、公交场站和火车站留出更多空间。

#### 选择 9：明智的发展决策（Principle 9）
*   **原则描述**：关于做出明智的发展决策（making smart development decisions）。
*   **指标定义**：因素之一是城市愿意与私营开发商合作进行新开发。根据城市的增长计划，主观地在 $0$ 到 $1$ 的尺度上进行评分。
*   **最优值设定**：最优值为 $1$。

#### 选择 10：社区成员参与规划（Principle 10）
*   **原则描述**：让社区成员参与发展规划（engaging community members in development planning）。
*   **指标定义**：在城市增长计划网页上搜索社区成员反馈计划的独特途径。统计这些独特途径的数量，并将其除以12。结论是，如果找到12种不同的、易于发现的方式（对于不熟悉市政府网站的人来说），就足以让社区成员提供反馈。
*   **最优值设定**：最优值为 $1$。这与原则9相关，因为原则9的另一个因素是做出社区预期且满意的决策。

### 指标关联与合成公式

上述指标中，我们将以下原则进行关联（Correlation）：
*   原则 1 与 原则 4
*   原则 2 与 原则 8
*   原则 5 与 原则 7
*   原则 9 与 原则 10

为了合并这些指标，我们使用了以下原始用于精度（Precision, $P$）和召回率（Recall, $R$）的效能度量公式的修改版 [9]：

$$
E = 1 - \frac {1}{\alpha \frac {1}{P} + (1 - \alpha) \frac {1}{R}}
$$

由于我们的原则指标中，数值越高代表成功水平越高，且仅使用了公式的第二项并使其为正，我们将每个关联指标的权重设为相等，即设 $\alpha = 0.5$。

对于指标 $a$ 和 $b$，合成公式变为：

$$
S _ {a, b} = \frac {1}{0 . 5 \frac {1}{a} + 0 . 5 \frac {1}{b}} = \frac {2}{\frac {1}{a} + \frac {1}{b}}
$$

我们将这四对指标的计算结果相加，再加上原则3和原则6的独立指标值，得到总成功评级 $S_{tot}$：

$$
S _ {t o t} = S _ {1,4} + S _ {2,8} + S _ {5,7} + S _ {9,10} + S _ {3} + S _ {6}
$$

最后，我们利用每个指标的最优值计算出最优成功评级 $S_{opt}$：

$$
S _ {o p t} \approx 4 . 1 8 7 5
$$

通过将计算出的成功评级与最优成功评级进行比较，我们得到最终的分数化成功水平 $L$：

$$
L = \frac {S _ {t o t}}{S _ {o p t}}
$$

我们使用 $L$ 来评估每个城市当前增长计划及拟议增长计划的成功率。

# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

本部分整理自《2017年美国大学生数学建模竞赛O奖论文》教材第3部分（共9部分），内容涉及美国博尔德市和澳大利亚堪培拉市的当前增长计划评估。

## 一、博尔德市，科罗拉多州，美国

### 博尔德增长计划概述

博尔德的增长计划为《博尔德谷综合规划》，最新更新于2010年 [10]。我们将评估该市如何满足每个智慧增长原则。

#### 选择 1：土地分区与混合用地

目前，博尔德有5%的土地被划定为商业或混合用途 [13]。因此，其混合用地的土地比例小于5%。

- **现状**：仅5%的土地用于商业或混合用途。
- **结论**：混合用地比例低。

#### 选择 2：人口密度与建筑高度限制

博尔德的人口密度为每平方英里1107人（基于城市人口和面积计算，包括城市区域内的开放空间）[13]。值得注意的是，博尔德通常将建筑物（特别是住宅建筑）限制在三层楼高（35英尺）[18]。这限制了当前的住房容量和再开发潜力。

- **人口密度**：1107人/平方英里。
- **建筑限制**：通常不超过3层（35英尺）。
- **影响**：限制了住房容量和再开发。

#### 选择 3：住房价格与可负担性

博尔德的独立屋中位售价为约75万美元 [13]。市政府计划保留现有的移动房屋公园，并增加永久性可负担住房，直到住房存量中有10%为永久性可负担住房 [10]。

- **房价**：约$750,000。
- **目标**：10%的住房为永久性可负担住房。
- **措施**：保留现有移动房屋公园。

#### 选择 4：步行与自行车友好度

博尔德较老、西部的社区主要是步行和骑行友好的，而城市的其他部分则不是。城市的增长计划指定了使社区更加步行友好并开发更多行人步道的计划 [10]。在2011年（最后一次 readily available 调查的日期），博尔德有8.3%的劳动人口步行上班 [11]。

- **现状**：老旧西部社区步行/骑行友好，其他区域较差。
- **计划**：增加步行友好度和行人步道。
- **数据**：2011年步行通勤比例为8.3%。

#### 选择 5：景观保护与社区特色

博尔德的建筑高度限制有助于保留附近山脉的视野 [16]，从而维持社区特色。城市的增长计划引用了几个具有独特风格的具体社区（例如历史悠久的市中心区域），并规定再开发和任何绿地开发都必须融入这些社区。

- **目的**：保护山景和社区特色。
- **策略**：确保新开发符合社区既有风格。

#### 选择 6：开放空间保护

博尔德拥有71平方英里的开放空间，相比之下城市空间仅为25.8平方英里 [13]。其致力于保护“自然区域、环境和文化资源、关键生态系统、水资源、农业用地、风景 vista 以及用于被动休闲的土地”，以及在农村和城市区域之间划定明确的边界 [10]。

- **开放空间**：71平方英里。
- **城市空间**：25.8平方英里。
- **保护对象**：自然、生态、水、农业及休闲用地。

#### 选择 7：再开发与公共服务

博尔德计划在已有公共服务的区域（即现有社区）完成新的开发和再开发。博尔德几乎没有未被指定为保护开放空间的剩余开放土地 [10]。因此，再开发是博尔德最可行的选项。

- **策略**：优先在现有社区进行开发。
- **原因**：缺乏未开发的开放土地。
- **结论**：再开发是唯一可行路径。

#### 选择 8：交通系统

博尔德拥有超过300英里的自行车道、路径和路肩 [15]。该市由科罗拉多州交通部地区运输区（RTD）的公共交通系统服务，包括本地和区域巴士以及轻轨列车。博尔德打算继续与RTD合作，鼓励替代交通方式并减少交通拥堵 [10]。从丹佛（最近的主要城市）到博尔德的通勤轻轨路线也在建设中 [19]。在2011年（最后一次 readily available 调查的日期），博尔德有36.8%的劳动人口使用除单独驾驶以外的其他方式通勤 [11]。

- **基础设施**：>300英里自行车道。
- **公共交通**：RTD巴士和轻轨。
- **未来项目**：丹佛至博尔德轻轨正在建设。
- **数据**：2011年多模式通勤比例为36.8%。

#### 选择 9：私人开发与基础设施

博尔德鼓励符合城市其他目标的私人开发 [10]。它还要求私人开发商建设直接有利于其项目的城市基础设施 [14]。

- **政策**：鼓励符合目标的开发。
- **要求**：开发商需建设相关基础设施。

#### 选择 10：社区参与

博尔德鼓励社区参与其发展决策。我们轻松找到了10种独特的方法供社区成员参与并提供关于发展规划的反馈 [12]。

- **参与度**：提供10种反馈渠道。

### 博尔德市指标汇总表

下表总结了上述指标以及最终成功水平0.7753。

| Metric | Value |
| :--- | :--- |
| P1 | 0.05 |
| P2 | 0.5535 |
| P3 | 0.1 |
| P4 | 0.083 |
| P5 | 1 |
| P6 | 0.733 |
| P7 | 1 |
| P8 | 0.368 |
| P9 | 1 |
| P10 | 0.8333 |
| L | 0.7753 |

## 二、堪培拉，澳大利亚首都领地

### 堪培拉增长计划概述

堪培拉的最新增长计划由澳大利亚首都领地政府于2012年提出，概述了2030年的成果。

#### 选择 1：混合用地规划

ACT当前的增加混合用地计划包括开发现有城市中心，以创造更集中的商业和生活中心。该计划并未列出混合用地的确切目标，但从城市土地地图可以清楚地看出，目前划定为混合用地的土地面积非常少 [5]。我们将其估算为5%。

- **策略**：集中发展现有城市中心。
- **现状**：混合用地极少，估算约为5%。

#### 选择 2：人口密度与紧凑发展

堪培拉的人口密度为每平方英里1161人（基于城市人口和面积计算）[4]。政府计划利用现有交通路线周围的区域来集中住房和商业开发 [4]。这些举措将允许更高的人口密度和紧凑性。

- **人口密度**：1161人/平方英里。
- **规划**：沿交通线路集中开发。
- **目标**：提高密度和紧凑度。

#### 选择 3：可负担住房

ACT在2016年更新了《可负担住房行动计划第三阶段》，概述了可负担住房的成本阈值 [6]。该计划保持了20%的新住房必须满足这些阈值的要求 [6]。

- **政策**：2016年更新行动。
- **要求**：20%的新住房需符合成本阈值。

#### 选择 4：步行通勤

2011年（根据最新 readily accessible 调查），堪培拉约有4.5%的人步行上班 [3]。然而，堪培拉人严重依赖车辆交通。ACT的计划概述了通过创建更多混合用地空间以及在现有铁路线周围开发步行网络来增加步行通勤的目标。

- **现状**：2011年步行通勤率为4.5%。
- **问题**：过度依赖汽车。
- **计划**：增加混合用地和铁路沿线步行网络。

#### 选择 5：健康社区

ACT政府似乎关注创建新的有吸引力的社区，并希望建立更大的商业和生活中心。特别是，政府建议使社区更加注重健康生活 [4]。

- **重点**：打造有吸引力的社区。
- **导向**：注重健康生活。

#### 选择 6：公共空间

ACT政府计划创建新的开放空间并保持现有的开放空间。他们提到需要“增强堪培拉的公共空间系统，提供充满活力的、宜人的城市公园和场所，让每个人都能享受，同时确保它们安全且易于进入……”[4]。在2008年（最新 readily available 数据），堪培拉的开放空间占总面积的百分比为63.4% [1]。

- **目标**：创建和维护开放空间。
- **愿景**：安全、宜人、易达的公共空间。
- **数据**：2008年开放空间占比63.4%。

# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

本文档整理自《2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!》第4部分（共9部分），由识别工具读取第10–12页内容后整理而成。原文为英文，此处保留原文语言以维持学术严谨性，并对HTML表格、断行及格式进行规范化处理。

## 4. Proposed Growth Plans

Boulder and Canberra can adjust their growth plans to accommodate a population that continues to increase over the next 30 years. Using our metric, we determined optimal values for each of the smart growth principles for both Boulder and Canberra. To reach these optimal values, we propose the following growth plans for Boulder and Canberra.

### 4.1 Boulder, CO, USA

Our proposed growth plan for Boulder involves encouraging the city to continue some initiatives that it already has in place, and adds the following five additional initiatives that are key in adhering to the smart growth principles:

Table 2 summarizes the metrics described above, as well as the final success level of 0.5882.

**Table 2:** Table of individual metrics and final success level for the current growth plan of Canberra, ACT, AUS

| Metric | Value |
| :--- | :--- |
| P1 | 0.05 |
| P2 | 0.5805 |
| P3 | 0.2 |
| P4 | 0.045 |
| P5 | 1 |
| P6 | 0.634 |
| P7 | 0.5 |
| P8 | 0.158 |
| P9 | 1 |
| P10 | 0.5 |
| L | 0.5882 |

The five additional initiatives are listed below:

A. Rezone and redevelop land for mixed use that is currently zoned for residential or commercial use only.
B. Redevelop current residential neighborhoods to include higher density and more affordable housing, such as townhouses and apartments.
C. Increase public transportation by finishing the light rail between Boulder and Denver and providing additional bus routes and buses per route around the city.
D. Discourage home owners from leaving their houses vacant by implementing a vacancy tax.
E. Create more community programming, particularly for youth and young adult age groups, to foster a strong sense of community within their neighborhoods.

These apply to the ten smart growth principles as follows:

1. Ideally, Boulder would have 15% of its land area zoned as mixed use by 2050. Since Boulder does not have additional land that it can expand to with new buildings, it will have to redevelop existing areas to make them mixed use areas. One way to do this is to rezone areas that are currently residential neighborhoods, particularly those near downtown, as mixed use land areas. Additionally, areas with less stringent height restrictions could be rezoned for mixed use land. Taller buildings can accommodate multiple uses, such as retail and residential, by having different uses of the building on each floor.

2. In order to accommodate population increase, Boulder must increase building density to provide enough housing and commercial buildings. Boulder is projected to increase its population density to 1230 people per square mile in the next 30 years as the total population climbs [13]. One way to accomplish this goal is to increase housing density in residential neighborhoods. Density could be increased by decreasing lot sizes and replacing old houses with town houses or small apartment buildings that can accommodate many more tenants in the same amount of space. In 2015, the residential rental vacancy rate was 4.4% [13]. Decreasing this vacancy rate would also help increase population density. The city could encourage people rent out their vacant houses by creating a tax on vacant properties, incentivizing owners to seek out renters. Additionally, the city could incentivize building additional housing on existing property, such as microhouses, to increase housing density.

3. As the population increases, Boulder should ideally have 20% of its housing qualify as low-income housing. In order to accomplish this goal, Boulder should focus on building townhouses and apartment buildings. This initiative would help increase population density and improve city walkability, because it would allow lower-income people to walk to work instead of having to commute from outside city limits. Apartments could be built in areas where the height restrictions are less stringent, and townhouses could replace detached houses in residential neighborhoods near downtown.

4. Ideally, 15% of Boulder’s residents would be able to walk to work. This increase would be a result of the city creating more walkable neighborhoods by rezoning residential areas for mixed use. Also, increasing housing density near downtown would allow more people to walk to work and retail locations, because they would live closer to commercial areas.

5. As the population density grows and more people move into existing neighborhoods, it will become more difficult for communities to maintain their current identities. Since some neighborhoods will be rezoned for mixed land use and different demographics will occupy new housing, some current residential areas will not be as quiet and quaint as they are now. This smart growth principle may suffer slightly as the communities grow, but over time, a new sense of community will be developed around the new and old residents in each community. Boulder should also maintain its community centers, such as public parks and recreation centers. As the population increases, the city should consider building additional community centers and recreation centers to maintain its current ratio of community members per community center. As such, we assign this metric a value of 0.8.

# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

本部分整理自《2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!》教材第5部分，对应原稿第13–15页内容，主要涉及博尔德市增长计划的结果总结及堪培拉市的增长计划提案。

## 一、博尔德市增长计划结果

### 段落 6

Boulder currently has 73.3% of its total land area as open space land [13]. As the population grows and there is an increased need for housing and commercial buildings, there may be proposals to rezone some open space land for these buildings. However, in following with the smart growth principle of preserving open space, Boulder should not develop any of its current open space land.


### 段落 7

Boulder has little to no surrounding land to expand to, so it is already focused on redeveloping existing areas. This redevelopment should include introducing mixed land areas to areas that are currently residential only. Also, redeveloping existing neighborhoods allows communities to maintain their current sense of community and can increase the population density in the area to accommodate the additional people who want to live in the city. This metric has a value of 1.


### 段落 8

Boulder should increase availability of public transportation as the population increases. By 2050, Boulder would ideally have 45% of its commuters use a mode of transportation other than driving to arrive at work. As the amount of low income housing in Boulder increases as part of our proposed smart growth plan, there will be higher demand for public transportation by those who cannot afford personal cars. Boulder can reach this goal by continuing its collaboration with RTD to provide buses around the city. Also, Boulder should continue its efforts to build a light rail train route between Boulder and Denver to aid commuters traveling much farther for work.


### 段落 9

Boulder should continue its public-private partnerships for new developments [10]. As the city redevelops residential areas with higher building density, construction should be done by private companies that align with the smart growth principles the city is adhering to with its development. This metric has a value of 1.


### 段落 10

Boulder is already doing well in asking for community feedback on development decisions. As the city works toward the development plan presented above, city officials should ensure the plans are transparent to citizens, and that that all citizens understand the smart growth principles to which the plans adhere. This metric has a value of 1.


### 综合结果

The results of our proposed growth plan for Boulder are summarized in Table 3, including a computed success level of $L = 0.8338$, an increase of 0.0785 from Boulder’s current growth plan.

Table 3: Table of individual metrics and final success level for our proposed growth plan for Boulder, CO, USA

| Metric | Value |
| :--- | :--- |
| P1 | 0.15 |
| P2 | 0.615 |
| P3 | 0.2 |
| P4 | 0.15 |
| P5 | 0.8 |
| P6 | 0.733 |
| P7 | 1 |
| P8 | 0.45 |
| P9 | 1 |
| P10 | 1 |
| L | 0.8338 |


## 二、堪培拉市增长计划

### 4.2 Canberra, ACT, AUS

Our proposed growth plan for Canberra includes five initiatives:

- A Rezone and redevelop land for mixed use; loosen building height restrictions
- B Develop new, mixed use areas on at most 10% of current open space
- C Partner with private developers to build affordable housing in a costeffective manner
- D Expand express bus routes and offer businesses discounted bus passes
- E Offer more opportunities for community engagement in development planning and advertise these opportunities effectively

These initiatives relate to the 10 smart growth principles (and our metrics) as follows.

### 段落 1

Ideally, 15% of Canberra’s city area would be zoned for mixed use. Canberra’s current plan includes converting some urban areas to mixed use. We recommend also redeveloping some of its current residential areas to mixed use areas. This will help to prevent excessive greenfield development and promote preservation of open space. The little greenfield development that Canberra then does should also be in areas newly zoned for mixed use.


### 段落 2

In the next 30 years, Canberra’s population density is expected to grow to 1455 people per square mile [4]. This growth will result in more housing demand. Redeveloping some urban and residential areas for mixed use should alleviate this to some extent. Enforcing a less stringent height restriction on buildings than is currently present will also allow more space for building upwards, resulting in a more compact city.


### 段落 3

Canberra’s current plan for affordable housing aims for 20% of new development to be affordable. We believe that Canberra could aim higher and reach our optimal value of 25% permanently affordable housing. We believe that Canberra should focus on redeveloping current areas to be higher-density (e.g. building townhouses instead of detached houses). Having mixed-use areas will help with this, as in Boulder, since low-income people could walk to work more easily, reducing their overall expenses. To encourage this, Canberra’s government should offer tax benefits to private developers who are willing to complete construction of affordable housing at a discounted rate.


### 段落 4

Canberra should aim to have 15% of its working population walk to work. This should account for most people living in existing and new mixed use areas, near existing and new mixed use areas, and near commercial/industrial areas.


# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

本部分为论文第6部分（共9部分）的整理内容，包含堪培拉发展计划的具体措施、指标变化及与博尔德计划的对比分析。

## 堪培拉发展计划实施细节

### 措施 5

**内容**：建议堪培拉保留保持独特社区特色的意图，但不要将其价值置于混合用途再开发和建设更多住房之上。因此，我们预期该指标的数值将下降至 0.8。

**原文依据**：We suggest that Canberra keep the intent to preserve distinctive neighborhood character, but not value this above redeveloping property for mixed use and building more housing. Thus, we anticipate a decrease of the value of our metric to 0.8.

### 措施 6

**内容**：目前 63% 的堪培拉土地面积为开放空间。虽然理想情况下堪培拉应保留所有开放空间，但我们认为考虑到人口的大幅增长，利用部分开放空间进行绿地开发更为现实。我们将这一开发的硬性上限设定为当前开放空间面积的 10%。这将使堪培拉的开放空间面积减少至城市总土地面积的 57.06%。

**原文依据**：63% of Canberra's land area is currently open space. While, ideally, Canberra would maintain all of its open space, we decided that it is more realistic that it will need to use some of it for greenfield development due to the large population increase. We are setting a hard cap on this development at 10% of the current open space area. This would reduce the amount of open space in Canberra to 57.06% of the city's total land.

### 措施 7

**内容**：我们对堪培拉的规划侧重于现有社区的再开发，但并非完全投入其中。要在维持社区特色的同时容纳大量新居民涌入，仅靠再开发现有的堪培拉是极其困难的，必须同时在开放土地上进行开发。我们计划将堪培拉开发的（最大）10% 的开放空间转化为混合用途区域。据此估算，该指标的数值应变为 0.75。

**原文依据**：Our plan for Canberra involves a focus on, but not a total devotion to, redevelopment of existing communities. It would be very difficult to redevelop Canberra enough to allow for the large influx of new residents while also maintaining community character without also developing on open land. We plan for Canberra to convert the (maximum) 10% of open space that it develops to mixed use areas. We estimate that the new value of our metric should, then, be 0.75.

### 措施 8

**内容**：虽然使用替代交通方式通勤的最佳工作人口比例为 100%，但堪培拉目前的比例仅为 15.8%。我们建议堪培拉的公共交通系统在郊区与市中心之间增加更多的快速公交线路。为此，应向企业员工提供打折的公交月票。廉价的交通将提高员工使用公共交通通勤的可能性。我们预计堪培拉将有 25% 的通勤者使用替代交通方式。

**原文依据**：While the optimal proportion of the working population that commutes to work using alternative transportation methods is 100%, Canberra's current proportion is only 15.8%. We recommend that Canberra's public transit system add more express bus routes between outer areas of the city and the city's center. To accompany this, they should offer businesses bus passes for their employees at a discounted rate. Affordable transit will make employees more likely to commute on public transit. We estimate that Canberra will reach a metric value of 25% of commuters using alternative transportation methods.

### 措施 9

**内容**：堪培拉应继续与私人开发商合作，特别是在建设经济适用房方面。该指标数值应保持在 1。

**原文依据**：Canberra should continue to partner with private developers, particularly in building affordable housing. This metric value should remain at 1.

### 措施 10

**内容**：堪培拉应更好地宣传现有机会，让社区成员对发展计划提供反馈。我们发现这些机会较难查找。此外，堪培拉应提供更多此类机会，包括但不限于邮寄调查、快闪活动和各子社区/社区的讨论。据此，堪培拉可以达到理想的指标数值 1。

**原文依据**：Canberra should better publicize existing opportunities for community members to give feedback on development plans. We found these somewhat difficult to track down. In addition, Canberra should offer more of these opportunities, including but not limited to mail surveys, pop-up events, and discussions in individual subcommunities/neighborhoods. Canberra could, then, reach the ideal metric value of 1.

## 堪培拉发展计划结果汇总

我们提出的堪培拉发展计划的结果总结如表 4 所示，其中包括成功水平 $L = 0.7443$，比堪培拉当前的计划增加了 0.1561。

| Metric | Value |
| :--- | :--- |
| P1 | 0.15 |
| P2 | 0.7275 |
| P3 | 0.25 |
| P4 | 0.15 |
| P5 | 0.8 |
| P6 | 0.5706 |
| P7 | 0.75 |
| P8 | 0.25 |
| P9 | 1 |
| P10 | 1 |
| L | 0.7443 |

## 措施对比分析

从上一节的两个子节结果可以看出，我们的博尔德计划产生的成功水平高于我们的堪培拉计划，但我们的堪培拉计划相对于堪培拉当前计划的改进幅度，几乎是我们的博尔德计划相对于博尔德当前计划改进幅度的两倍。

我们根据考察每项具体措施的影响计算了新指标。结果总结在表 5 中，其中 $\Delta L$ 表示在添加一项单独的措施后，城市的成功水平 $L$ 减去其当前增长计划的成功水平 $L$。

我们将博尔德的措施按优劣顺序排列为 E、C、D、A、B。根据我们的指标和这些结果，对智慧增长成功影响最大的因素是增加社区项目，特别是通过针对青年和年轻人的外展活动（E）。增加公共交通（C）和减少空置房产数量（D）都改善了博尔德的智慧增长。根据指标，将土地重新分区用于混合用地（A）和再开发住宅社区（B）的措施对博尔德的智慧增长产生了负面影响，因为它们允许更多人搬入社区，从而对社区认同感产生负面影响。

# 2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）

本文档整理自《2017年美国大学生数学建模竞赛O奖论文：Sustainable Cities Needed!（ICM E题）》教材第7部分（共9部分），对应原件第18–19页内容。主要包含针对Boulder和Canberra人口增长情景的分析，以及模型优缺点的总结。

## 5 Population Increase

### 5.1 Boulder, CO, USA

Boulder’s population is projected to increase by 22,166 people by 2050 if growth continues at the current rate, which is a 20.7% increase from the current population [13]. If the population were to instead increase by 50% over the next 30 years, the city would not be able to provide housing and space for all the additional people, even using our smart growth plan. Since the 50% increase in population is much larger than the projected 20.7%, the city will be able to keep up with its predicted growth but not with the hypothetical situation of 50% growth. With 50% growth there will not be enough housing or land on which additional housing could be built. In order to build enough housing, the city would have to change the height requirement on buildings to allow for upward expansion or decrease the land designated for open space to provide enough space to build new housing. If open space land was redesignated to provide for the additional population, new developments should be zoned for mixed land use, so that new neighborhoods are walkable and adhere to smart growth principles. This would match our proposal for 15% of city land to be mixed land use, though our proposal bases this change on rezoning commercial and residential land rather than open space. Public transportation to these locations would also have to increased. This could be accomplished by creating new bus routes throughout the city and by increasing the number of buses that currently run on each route. Additional buses would also need to be added to Boulder to Denver routes to account for the additional number of commuters who may work in Denver and live in Boulder. These initiatives would help Boulder reach the goal of 45% of people commuting to work by some form other than driving set forth by our proposal.

### 5.2 Canberra, ACT, AUS

Canberra’s projected growth in the next 30 years is approximately 25%. If it continued at the same rate, it would increase by 41.7 by 2050. A population increase of 50% by 2050 is certainly larger than the projected growth of Canberra, but not by a huge margin. Our plan would likely result in housing shortages. We attempted to minimize use of open space in new development, but if Canberra grew 50% by 2050, we believe that the amount of redevelopment required to avoid eliminating more than 10% of the current open space is unrealistic. Canberra would likely need to expand further into open space, which is not accounted for in our plan. The city would also need to further expand mixed use areas and the public transit system to encourage alternative transportation methods and avoid significant increases in traffic. The 15% mixed use zoning that we identified as Canberra’s goal might need to be increased to 20%. The public transit system would need to be expanded and advertised proportionally to the city’s growth, similarly to our plan. Our initiative for community engagement would, most likely, be fine as is. In summary, the growth plan for Canberra that we proposed would need to be altered slightly in order to accommodate this level of growth.

## 6 Model Strengths and Weaknesses

The main strength of our model is that it is relatively easy to use. To calculate the objective portion of our metrics, one simply needs data that is easily found in census reports and news articles (i.e. commute statistics, land zones, etc.) or goal data determined through analysis of the city’s potential and needs. The subjective portion concerns the city’s initiatives, which can be found in the city’s plans or proposed in one’s own plan.

## 模型的局限性

由于缺乏与某些智慧增长原则相关的可量化实证数据，我们将相应的个体指标定义为零到一的主观排名。因此，这些指标高度依赖于城市增长计划文件中措辞的具体内容，且存在一定的不精确性。

另一个局限性在于我们对各个组成部分赋予了相等的权重。在将每一对相关性与我们的 S 度量进行相关性分析后，我们对配对结果以及剩余的两个未相关指标进行了简单求和，而未进行加权处理。这导致像社区参与这样的原则的指标对最终成功等级的影响，大于混合用地和替代交通等指标的权重。仔细考虑各原则的相对重要性并应用适当的权重可以使我们的模型更加完善。

### 7 结论

美国科罗拉多州博尔德市（Boulder, CO）和澳大利亚首都领地堪培拉市（Canberra, ACT）预计在未来 30 年内人口都将增长。为了容纳新增人口，每个城市都提出了基于预测人口增长的长期增长计划，以帮助城市实现可持续性的三个 E（经济、环境、社会）。每个城市增长计划的许多要素已经遵循了智慧增长的十项原则。博尔德市已经采取措施增加城市范围内保障性住房的比例至 10%，增加步行路径并保持自行车道系统，保持 71 平方英里的开放空间，并通过公交车和轻轨进一步发展公共交通 [10]。堪培拉市计划增加混合用地的分区面积，建设新住房，保留指定为开放空间的土地，并通过轻轨系统继续发展公共交通。

我们根据智慧增长度量标准对每个城市的当前状态进行了评级，以确定每个城市在实现智慧增长方面的成功程度。博尔德市的得分为 0.7753，堪培拉市的得分为 0.5882。从这些结果中我们注意到，尽管两个城市都必须继续考虑这十项原则以实现人口增长背景下的可持续性，但堪培拉在实现智慧增长原则方面比博尔德市有更大的改进空间。为了更好地实现智慧增长的十项原则，我们为这两个城市未来 30 年的城市增长提出了新的计划。我们还考虑了如果每个城市的人口分别增加 50%（而不是博尔德市的 21% 和堪培拉市的 25%），我们的提议能否成功。

团队 # 71672

第 19 页，共 22 页

我们提出的博尔德市增长计划包括五项关键举措，共同可将该城市的智慧增长度量指标提高至 0.8338。这五个计划要素是：重新分区和开发混合用地、改造现有住宅区、增加公共交通、消除空置房屋以及增加社区项目和青年外展活动。我们提出了到 2050 年为实现可持续支持增长人口而应达到的这五项倡议的理想值。

同样，我们为堪培拉市提出了一个包含五项关键举措的增长计划，如果所有举措共同实施，可将智慧增长得分提高至 0.7443。这五个要素是：重新分区土地用于混合土地利用、放宽建筑高度限制、开发目前作为开放空间的土地、建设更多保障性住房、通过公交车扩大公共交通规模以及提供更多社区参与途径。

如果到 2050 年堪培拉和博尔德的人口都增长 50%，我们的增长计划必须进行修正。这种人口增长对堪培拉来说不会造成太大问题，初始的住房短缺可以通过混合用地的微小增加来解决，以及对高质量公共交通的需求加剧。然而，博尔德市的人口增长则更具挑战性。我们预测，即使重新划分开放空间、增加高度要求并增加交通设施，博尔德市仍可能面临严重的住房短缺。博尔德市为智慧增长提供了一个警示案例；在快速城市化的当今世界，应尽快实施智慧增长原则。

团队 # 71672

第 20 页，共 22 页

### 参考文献

[1] 规划数据统计：ACT。网站，2008。URL https://web.archive.org/web/20080802163103/http://www.actpla .act.gov.au/tools resources/planning data.

[2] 智慧增长：制定和实施温室气体减排计划的指南。网站，2011。URL http://www.sustainablecitiesinstitute.org/Documents/SCI/Report Guide/Guide PA SmartGrowthGHGReduction 2011.pdf.

[3] 通勤方式：堪培拉地区。网站，2017。URL http://profile.id.com.au/cbrjo/travel-to-work?WebID=10SeifaKey =40004.

[4] ACT。ACT 规划战略。可在 act.gov.au 获取，2012。URL http://www.planning.act.gov.au/ data/assets/pdf file/ 0008/895076/2012 Planning Strategy.pdf.

[5] ACT。ACTmapi 领土计划和国家首都管理局地图查看器。网站，2015。URL http://app.actmapi.act.gov.au/actmapi/index.html?viewer=tp.

[6] ACT。保障性住房行动计划。网站，2016。URL http://www.economicdevelopment.act.gov.au/buy-land-and-build/ affordable housing/affordable housing action<sub>p</sub>lan.

[7] ACT。社区参与。网站，2017。URL http://www.cityplan.act.gov.au/community-engagement.

[8] ACT。Your Say ACT。网站，2017。URL https://yoursay.act.gov.au/.

[9] C. J. van Rijsbergen。信息检索。英国格拉斯哥大学，格拉斯哥，第二版，1979。

[10] 博尔德市。2010 博尔德谷综合规划。可在 bouldercolorado.gov 在线获取，2010。URL https://www-static.bouldercolorado.gov/docs/boulder-valleycomprehensive -plan-2010-1-201410091122.pdf.

[11] 博尔德市。经济概况：科罗拉多州博尔德市。可在 bouldercolorado.gov 在线获取，2011。URL

团队 # 71672

第 21 页，共 22 页

## 参考文献

[12] City of Boulder. BVCP Community Engagement. Available on bouldercolorado.gov, 2015. URL bouldercolorado.gov/docs/Community Engagement-1-201510061348. png? ga=1.16336694.1243963416.1482432947.

[13] City of Boulder. 2016 Boulder Community Profile. Available online at bouldercolorado.gov, 2016. URL https://www-static.bouldercolorado.gov/docs/2016-communityprofile -1-201610101422.pdf? ga=1.74122770.1243963416.1482432947.

[14] City of Boulder. Development-Related Impact Fees and Excise Taxes. Website, 2016. URL https://bouldercolorado.gov/plan-develop/development-impactfees-excise-taxes.

[15] City of Boulder. Maps of Boulder’s Transportation System. Website, 2017. URL https://bouldercolorado.gov/maps/maps-of-boulders-transportation -system.

[16] City of Boulder and Boulder County. Boulder Valley Comprehensive Plan: 2016 Community Survey. Available online at bouldercolorado.gov, 2017. URL https://www-static.bouldercolorado.gov/docs/Boulder Comp Plan 2016 Survey Report FINAL-1-201701131444.pdf? ga=1.86221336. 1243963416.1482432947.

[17] D. Stathakis, G. Tsilimigkas. Applying urban compactness measures on pan-european datasets. International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences, XL-4/W1:130, 2013.

[18] Erica Meltzer. Boulder gives final approval to height limit ordinance. Daily Camera, 2015.

[19] RTD. Northwest Rail - B Line. Website, 2016. URL http://www.rtd-fastracks.com/nw 1.

[20] United Nations, Department of Economic and social affairs. Annual Percentage of Population at Mid-Year Residing in Urban Areas by Major Area, Region and Country, 1950-2050. Website, 2014. URL https://esa.un.org/unpd/wup/CD-ROM/.
