---
title: 2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文精选：城市智慧增长模型
kind: 竞赛论文
course: 数学建模
source: batch-2:数学建模/2017年美国大学生数学建模竞赛O奖论文（全部）.zip/2017年美国大学生数学建模竞赛O奖论文（全部）/2017年美国大学生数学建模竞赛O奖论文（全部）/E/67171.pdf
---

# 2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文精选：城市智慧增长模型

原件为竞赛论文。补充：文中的阅读练习及“参考解答”为整理时增加，原件图文保留出处。

本资料整理自《2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文精选》，提取了参赛队伍编号为 67171 的 O 奖论文的摘要、目录及开头部分，用于展示城市智慧增长模型的构建思路与论文结构。

## 一、摘要部分

### 摘要 1

题干：The problems caused by rapid urban sprawl are becoming increasingly important in the past few decades. Our team was tasked with modeling smart growth of a city in the light of urban planning theory.We assumed that budget is the major factor which determines growth of a city and the budget in a certain year is limited.

We developed a three dimensional baseline cube model to measure the success of smart growth of a city. The three dimensions are Economic Development Index(EDI), Social Justice Index(SJI) and Environment Performance Index(EPI), with which we measure economic state, social state and environment state of a city growth respectively. A state of growth is mapped into a vector in this cube. And the vector of ideal smart growth is represented by diagonal of the cube. By comparing the vector of growth about a city and the ideal vector, we can directly know how the current growth plan of this city meets the smart growth principles. The angle between city vector and ideal vector means the degree of sustainability of a city. The smaller the angle is, the more sustainable the city is. Besides, the length of city vector represents the speed of growth. The larger the length is, the faster the city grows. Using our cube model, we measured the growth plan of Wellington and Edinburgh.

In order to develop a smart growth plan, we need to optimize the angle and length of a city vector. Therefore, we integrate angle and length into an Smart Growth Index(SGI) with an added parameter $\mu$ illustrating how policymakers weigh importance between these two elements. Based on our assumptions, our task is to find an optimal allocation of total budget. Our total budget comprises seven components: transport service, social service, environmental service, education service, health service, development service and other service. So we updated the baseline cube model to modified cube model to evaluate the effects of these components on EPI, SJI and EDI with parameters. We estimated these parameters using data of this city collected in past few years, with which we are able to find an optimal allocation of budget given a total budget. What's more, we can rank the individual initiatives as the most potential to the least potential by sorting the components of the optimal budget. By incorporating known numerical values about budget and EPI, SJI, EDI in Wellington and Edinburgh into our model, we shed light on the most influential factors in budget and developed a smart growth plan to significantly improve states of these two cities. Based on our plan, we made a 30-year forecast for them. Also, with an additional 50% population increase, we adjusted our growth plan. Utilizing sensitivity analysis and F test, our model is testified to be reliable.

答案：无（此为论文摘要原文，非试题问答）。

## 二、目录部分

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 目录 1

题干：Contents

- I. Introduction......3
- II. Restatement of the Problem......4
- III. General Assumptions......4
- IV. Models......4
    - 4.1 A Measurement of Smart Growth: Baseline Cube Model......4
        - 4.1.1 Main Parameters in Baseline Cube Model......4
        - 4.1.2 Smart Growth Index(SGI......5
        - 4.1.3 Economic Development Index(EDI......6
        - 4.1.4 Social Justics Index(SJI......6
        - 4.1.5 Environment Performance Index(EPI......7
        - 4.1.6 A Three Dimensional Baseline Cube Model to Determine Smart Growth......7
    - 4.2 A Development of Growth Plan: Modified Cube Model......8
        - 4.2.1 Additional Assumptions......8
        - 4.2.2 A Modified Cube Model for Growth Plan......9
        - 4.2.3 Solution to the Modified Cube Model......9
        - 4.2.4 The Optimal States(S) of the Next Few Decades......10
        - 4.2.5 Development of Growth Plan and Rank of the Components......10
- V. Case study......11
    - 5.1 The Current Growth Plan for Edinburgh and Wellington......11
        - 5.1.1 Evaluation of Current Growth Plan for Edinburgh......11
        - 5.1.2 Evaluation of Current Growth Plan for Wellington......11
    - 5.2 Growth Plan for Edinburgh and Wellington......13
        - 4.2.1 Growth Plan for Edinburgh......13 （注：此处原文编号有误，应为 5.2.1）
        - 4.2.1 Growth Plan for Wellington......14 （注：此处原文编号有误，应为 5.2.2）
    - 5.3 Ranking and Comparison of Components......16
    - 5.4 Explanation of Growth Plan in Additional 50% Populatio Growth......16
- VI. Model Testing......17
- VII. Sensitivity Analysis......17
- VIII. Strength and Weakness......18
    - 8.1 Strength of Models......18
        - 8.1.1 Inclusive......18
        - 8.1.2 Quantification......18
        - 8.1.3 Simple but Universal......18
        - 8.1.4 Visible and Understandable......18
    - 8.2 Weakness of models......19
        - 8.2.1 Accuracy Relies on Statistics......19
        - 8.2.2 Disasters Are Not Included.... 19
        - 8.2.3 Difference Replaced Derivatives.... 19
- IX. References.... 21

答案：无。

## I. Introduction

> “Poor accessibility is the common denominator of urban sprawl - nothing is within easy walking distance of anything else.”
>
> Dr Reid Ewing, the National Center for Smart Growth, quoted from a BBC article “The community are still not very happy about the plans……The concerns relate to the huge volume of traffic and school capacity……You are looking at a lovely rural community becoming more urban sprawl.”
>
> - Kevin Turley, deputy manager of Lakeside Plant Centre, quoted from a BBC article

The problems caused rapid urban sprawl is becoming increasingly important in the past few decades. In 1950, 30 percent of the world’s population was urban, but by 2050, 66 percent of the world’s population is projected to be urban. Also, the urban population of the world has grown rapidly since 1950, from 746 million to 3.9 billion in 2014[1]. The rapid urbanizing is causing serious problems for the economy, society and environment of cities, such as traffic jam, less farmland, higher resource pressure, etc. With an attempt to solve these problems, the Local Government Commission which presents the annual New Partners for Smart Growth conference adopted the original Ahwahnee Principles in 1991[2]. Many of the major principles are now generally accepted as part of smart growth movement such as Transit oriented development, a focus on walking distance, greenbelts and wildlife corridors, and infill and redevelopment[3].

There are at least two definitions about smart growth. According to Boeing et al.[4], “smart growth is an urban planning and transportation theory that concentrates growth in compact walkable urban centers to avoid sprawl. It also advocates compact, transit-oriented, walkable, bicycle-friendly land use, including neighborhood schools, complete streets, and mixed-use development with a range of housing choices”. IEPA[5] also describes that smart growth is about helping every town and city become a more economically prosperous, socially equitable, and environmentally sustainable place to live. The three E’s sustainability raised by the latter is clearer and more practical. As the problem caused by urban sprawl is becoming increasingly serious, the International City Management Group (ICM) is eager to implement smart growth theories into city design around the world.

![图 1 三个 E 的可持续性及其相关组成部分](2017年美国大学生数学建模竞赛MCM-ICMO奖论文精选：城市智慧增长模型.assets/图1.jpg)

## II. Restatement of the Problem

The International City Management Group (ICM) raised a series of tasks for our group to deal with. These problems and our work can be restated as the following lists:

1) Considering the 3 E’s of sustainability and/or the 10 principles of smart growth, design a metric to measure the smart growth of a city. According to the three E’s requirement, we designed a three dimensional baseline cube model to determine whether the smart growth of the city is successful or not. This model is based on Smart Growth Index(SGI), Economic Development Index (EDI), Social justice index (SJI) and Environment Performance Index(EPI). By utilizing EDI, SJI and EPI, we can determine a city is smart growth or not. The SGI is used to measure the level of the growth.

2) Select two mid-sized cities (with a population of between 100,000 and 500,000) on different continents and measure how the current growth plan of each city meets the smart growth principles. We selected Edinburgh and Wellington as our targets and searched the growth plan of the two cities. Using the baseline cube model, we measured and discussed how successfully their growth plan meets the smart growth.

3) Develop a growth plan for both cities over the next few decades and support your choice of the components, after which use your metric to evaluate the success of your smart growth plans. Based on the budget plan of the selected cities and our baseline cube model, we developed modified cube model with a component matrix B. The matrix B is consisted of seven components: transport service(B1), social service(B2), environmental service(B3), education service(B4), health service(B5), development service(B6) and other(B7). By maximizing the SGI, an optimal growth plan can be achieved by changing B1, B2, B3, B4, B5, B6 and B7 to the optimal value. Since the metric is based on the cube model and during the calculation process the SGI achieves the maximum value, the optimal growth plan we developed can automatically meet the smart growth requirement in our baseline cube model.

4) Rank the individual components in your smart growth plan according to their potential. Compare the components and their ranking between the two cities. We used our modified cube model to evaluate the potential of the individual components and compared both the components and their rankings in the two cities.

5) Under the consumption that the population of the two cities will increase by additional 50% by 2050, explain how your plan supports the growth. We evaluated the extent to which our plans support the growth.

## III. General Assumption

We assume that the statistics we collected from the website are reliable and accurate. The data utilized in our models is mainly collected from valid statistics websites of Edinburgh and Wellington, such as Scotland’s census[6], Statistics New Zealand[7]. Thus, this assumption is reasonable.

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 4.1 A Measurement of Smart Growth: Baseline Cube Model

In this model, Economic Development Index(EDI), Social Justice Index(SJI) and Environment Performance Index(EPI) are used to determine whether the growth of a city is smart growth or not. Smart Growth Index(SGI) is calculated from the three indexes(EDI,SJI,EPI) to evaluate the level of smart growth. To begin with, we summarized the main parameters used in our model. Then, we defined the expression of Smart Growth Index(SGI), after which Economic Development Index(EDI), Social Justice Index(SJI) and Environment Performance Index(EPI) are introduced. These indexes(EDI, SJI and EPI) represent Economically prosperous, Socially Equitable, and Environmentally Sustainable (the 3E’s of sustainability) respectively. At last, based on the SGI, EDI, SJI and EPI, we developed a three dimensional baseline cube model to determine the smart growth of a city.

#### 4.1.1 Main Parameters in Baseline Cube Model

After referring to the work of Professor Montenegro et al.[8], the definition of Social justice index[10] and Environmental Performance Index[11], we selected the following parameters to determine the smart growth. We will explain the reasons for the choice in the next few sections.

Table 1: Main parameters utilized in baseline cube model

| First stage | Second stage | Third stage |
| :--- | :--- | :--- |
| **Smart Growth Index (SGI)** | **Economic Development Index (EDI)** | Life Expectancy |
| | | GDP Per Capita |
| | | Expense (% of GDP) |
| | **Social Justice Index (SJI)** | Employment Rate |
| | | Number of Study Participants |
| | | Gini Coefficient |
| | **Environment Performance Index (EPI)** | Total Greenhouse Gas Emissions |
| | | Forest Area |
| | | Renewable Energy Consumption |

#### 4.1.2 Smart Growth Index (SGI)

Considering the three E’s sustainability, we defined Smart Growth Index(SGI) to measure the level of smart growth. SGI is calculated from Current Growth(CG) and Smart Growth(SG) with

$$
S G I = \frac {\cos \left\langle \overrightarrow {C G} , \overrightarrow {S G} \right\rangle + \mu \left| \overrightarrow {C G} \right|}{1 + \mu \sqrt {3}} \tag{1}
$$

where the first term of the numerator is the cosine function of the angle between the current growth vector and the ideal smart growth vector. This term represents whether the direction of current growth is close to smart growth or not. If this term is closed to one, it means the city is developing at a right direction. The second term of the numerator is the length of the current growth vector, representing the rate of the city growth. In this equation, $\mu$ is utilized to illustrate the weight of growth rate to growth direction. The value of $\mu$ is dependent on the policymaker and requirement. If growth rate is more important than growth direction(such as a developing country), $\mu$ can be set as larger than $1 / \sqrt { 3 }$ to balance the two terms, but it is recommended that the value set between 0 and $1 / \sqrt { 3 }$ especially in developed countries, since the direction of growth is more important than growth rate in most cases. The denominator of the equation on the right hand is utilized to normalize the SGI to a range of 0~1 for the convenience of defining the extent of smart growth. A summary of the SGI equation is given as the following table:

Table 2: A summary of SGI Expression

| Expression | Term | Description | Meaning |
| :--- | :--- | :--- | :--- |
| $SGI = \frac{\cos\langle\overrightarrow{CG},\overrightarrow{SG}\rangle + \mu|\overrightarrow{CG}|}{1+\mu\sqrt{3}}$ | $\cos\langle\overrightarrow{CG},\overrightarrow{SG}\rangle$ | The angle between CG vector and SG vector | The direction of city growth |
| | $|\overrightarrow{CG}|$ | The length of CG vector | The rate of city growth |
| | $\mu$ | Weight of CG length | Importance of growth rate to growth direction |
| | $\frac{1}{1+\mu\sqrt{3}}$ | normalization | Normalize the SGI to a range of 0~1 |

# 城市智慧增长模型：指标体系与三维基准立方体

本节内容源自《2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文精选》第4部分，主要阐述了城市智慧增长指数（SGI）的计算方法，包括经济、社会和环境三个维度的具体指标定义，以及基于三维坐标系的基准立方体模型判定逻辑。识别并修正了原文中的拼写错误（如 "axial" 改为 "axial" 或 "axis"，"Gin i" 等），并将公式转换为 LaTeX 格式。

## 一、智慧增长指数计算框架

知识点：[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 选择 1：状态向量与增长矢量定义

**题干**：
如何定义城市的智慧增长状态（State, S）及其变化量（CG）？

- **A**. 仅由经济数据决定。
- **B**. 由当前状态与上一时刻状态的差值构成，包含经济、社会、环境三个维度。
- **C**. 仅由环境指标决定。
- **D**. 通过单一的社会正义指数计算。

**答案**：B。

**参考解答**：
文中指出，城市在特定时间的智慧增长状态 $S$ 由三个指数组成：经济发展指数 (EDI)、社会正义指数 (SJI) 和环境绩效指数 (EPI)。智慧增长矢量 $\overrightarrow{CG}$ 通过当前状态与上一状态的差值计算得出：

$$
\overrightarrow {C G} = \left(\overrightarrow {S _ {c u r r e n t}} - \overrightarrow {S _ {p r e v i o u s}}\right)
$$

其中：
$$
\begin{array}{l} \overrightarrow {S _ {\text { current }}} = \left(S J I _ {\text { current }}, E D I _ {\text { current }}, E P I _ {\text { current }}\right) \\ \overrightarrow {S _ {\text { previous }}} = \left(S J I _ {\text { previous }}, E D I _ {\text { previous }}, E P I _ {\text { previous }}\right) \end{array}
$$

> [!NOTE]
> 核心高亮
> 智慧增长不仅看绝对数值，更看重**变化量**。只有当三个维度的指标同时提升时，才代表真正的智慧增长。

![Fig 2. The value of $\mu$ for different types of city](2017年美国大学生数学建模竞赛MCM-ICMO奖论文精选：城市智慧增长模型.assets/图2.jpg)
*图 2：不同城市类型的 $\mu$ 值示意图*

---

## 二、三大维度指标详解

知识点：[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 选择 2：经济发展指数 (EDI) 的构建

**题干**：
关于经济发展指数 (EDI) 的构建，以下描述正确的是？

- **A**. 仅使用人均收入水平。
- **B**. 结合了人均 GDP、GDP 支出占比和预期寿命。
- **C**. 仅依赖 Montenegro 教授提出的原始方法。
- **D**. 忽略了收入分配的影响。

**答案**：B。

**参考解答**：
在 Professor Montenegro 等人提出的基础上，作者结合可用数据进行了更新。新的 EDI 模型利用三大经济指标之一（此处指代 GDP 相关指标）及 GDP 支出，具体采用以下三个变量来衡量城市经济发展：
1. 人均 GDP (GDP per Capita)
2. GDP 支出占比 (Expense of GDP)
3. 预期寿命 (Life Expectancy) —— *注：引入此指标以提高预测准确性*

计算公式为：
$$
E D I = \frac {1}{3} \left(L i f e E x p e c t e n c y + G D P p e r C a p i t a + E x p e n s e o f G D P\right)
$$

---

知识点：[人类发展指数 HDI 的局限性与社会经济调整指数的构建](../../../topics/数学建模/hdi_zhibiao.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 选择 3：社会正义指数 (SJI) 的构成

**题干**：
社会正义指数 (SJI) 选取了哪三个主要因素来代表六个维度中的关键方面？

- **A**. 贫困预防、教育公平、劳动力市场准入。
- **B**. 基尼系数、就业率、受教育人数。
- **C**. 健康水平、非歧视程度、代际正义。
- **D**. 所有 27 个定量指标的平均值。

**答案**：B。

**参考解答**：
社会正义指数原本包含 27 个定量和 8 个定性指标，涵盖六个维度（贫困预防、教育公平、劳动力市场准入、社会凝聚力与非歧视、健康、代际正义）。模型从中选取了三个主要因素：
1. **基尼系数 (Gini coefficient)**：代表收入分配的公平性。权重为 $3/7$。
2. **就业率 (Employment rate)**：代表劳动力市场准入。权重为 $2/7$。
3. **受教育人数 (Number of study participants)**：代表教育公平。权重为 $2/7$。

计算公式为：
$$
S J I = \frac {3}{7} G i n i C o e f f i c i e n t + \frac {2}{7} N u m b e r o f S t u d y P a r t i c i p a n t s + \frac {2}{7} E m p l o y m e n t R a t e
$$

> [!WARNING]
> 订正说明
> 原文中公式排版存在乱码（如 "Numbe r of Study Participants"），已根据上下文逻辑修正为连贯的变量名。

---

知识点：[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 选择 4：环境绩效指数 (EPI) 的定义

**题干**：
环境绩效指数 (EPI) 在本模型中是从哪三个方面计算的？

- **A**. 空气质量、水质、噪音污染。
- **B**. 温室气体排放总量、森林面积、可再生能源消耗。
- **C**. 联合国千年发展目标的所有指标。
- **D**. 仅计算碳排放。

**答案**：B。

**参考解答**：
环境绩效指数 (EPI) 用于量化国家政策的环保表现。在本模型中，EPI 从以下三个方面计算：
1. 温室气体排放总量 (Total Greenhouse Gas Emissions)
2. 森林面积 (Forest Area)
3. 可再生能源消耗 (Renewable Energy Consumption)

计算公式为：
$$
E P I = \frac {1}{3} \left(\text { TotalGreenhousGasEmissions } + \text { ForestArea } + \text { RenewableEnergyConsumption }\right)
$$

> [!TIP]
> 补充说明
> 原文中 "TotalGreenhousGasEmissions" 疑似拼写错误（少了一个 'e'），但在公式中作为整体变量处理。实际应用中应确保数据清洗正确。

---

## 三、三维基准立方体模型判定逻辑

知识点：[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 简答 1：三维立方体模型的判定规则

**题干**：
请简述如何利用三维基准立方体模型判断一个城市是否实现了“智慧增长”？

**参考解答**：
在定义了因变量 SGI 和自变量 EDI、SJI、EPI 后，模型构建了一个三维立方体来衡量城市的智慧增长：
1. **坐标轴定义**：
   - X 轴：经济发展指数 (EDI)
   - Y 轴：社会正义指数 (SJI)
   - Z 轴：环境绩效指数 (EPI)
2. **判定原则**：
   - **理想状态**：智慧增长向量 SG 的坐标为 $(1, 1, 1)$。
   - **核心逻辑**：智慧增长由三个因素中的**最低值**决定（木桶效应）。只有当三个参数的值都较高时，城市才能实现理想的智慧增长。
   - **分类标准**：
     - 若三个参数均为正值且达到一定高度，归类为**智慧增长 (Smart Growth)**。
     - 否则，归类为**非智慧增长 (Non-smart Growth)**。
3. **分级机制**：
   - 每个变量在立方体模型中被分为 6 个等级。

> [!IMPORTANT]
> 核心概念
> **“木桶效应”是判定关键**。即使两个维度很高，如果第三个维度很低（例如经济发展很好但环境污染严重），则不能被视为实现了全面的智慧增长。

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 简答 2：模型改进点

**题干**：
本模型在 Li et al. 的研究基础上做了哪些改进？

**答案**：
将原有的二维坐标改进为三维坐标，分别对应 EDI、SJI 和 EPI，使评估更加全面和立体。

---

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 知识点：城市智慧增长模型
### 知识点：多指标综合评价
### 知识点：加权平均法

# 2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文精选：城市智慧增长模型

## 一、评价指标与结果分析

### 选择 1

**题干：**
根据模型，EDI、SJI 和 EPI 的最低值用于判断城市增长是否为智慧增长，SGI 用于衡量智慧增长的等级。评价结果如下表所示。请根据下表回答相关问题。（注：此处为原文表格内容的文字化整理，原题为陈述性段落配合表格）

**Table 4. Evaluation of growth results**

| Min(EDI,SJI,EPI) | Growth type | SGI | Level of growth |
| :--- | :--- | :--- | :--- |
| > 0 | Smart growth | 0.8~1 | High |
| | | 0.5~0.8 | Medium |
| | | 0~0.5 | Low |
| < 0 | Non-smart growth | — | — |

**答案：**
（原文无具体选择题选项，此为陈述性结论）
In summary, in this model the lowest value of EDI, SJI and EPI is utilized to determine whether the growth of a city is smart growth or not, SGI is utilized to measure the level of smart growth.

**知识点：**
智慧增长评价指标

## 二、改进立方体模型：发展计划制定

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 简答 1

**题干：**
简述 4.2 节中提出的“Modified Cube Model”（改进立方体模型）的背景、假设及主要目标。

**参考解答：**
该模型旨在基于基线立方体模型，为城市制定未来几十年的发展计划。其核心思想是基于预算（Budget）这一社会经济开发的主要工具进行优化。

**Additional Assumptions（额外假设）：**
1. **预算有限性：** 爱丁堡（Edinburgh）和惠灵顿（Wellington）在特定年份的总预算是有限的，且未来三十年的预算可根据 2009-2015 年的数据进行预测。
2. **预算可预测性：** 由于这两个城市在未来几十年内经济和政治环境相对稳定，预算趋势不会出现大幅波动，因此可以通过历史数据预测。
3. **预算主导性：** 预算是影响城市发展的主要因素。引用 N.V. Prosyanik et al.[16] 的观点，在市场经济社会中，城市预算是调节社会和经济过程的主要工具。

**预算分类：**
预算分为七类：
1. Transport service（交通服务）
2. Social service（社会服务）
3. Environmental service（环境服务）
4. Education service（教育服务）
5. Health service（健康服务）
6. Development service（发展服务）
7. Other（其他）

**知识点：**
数学建模假设

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 计算 1

**题干：**
写出改进立方体模型的优化问题公式，包括目标函数、约束条件以及各变量的定义。

**参考解答：**

**1. 优化模型公式：**

$$
\begin{aligned}
& \max \quad \mathrm{SGI} \\
& s.t. \left\{ \begin{array}{c} \vec {B} \geq 0 \\ \Delta \vec {S} \geq 0 \\ \sum_ {i = 1} ^ {7} B _ {i} = total Budget \end{array} \right.
\end{aligned}
\tag{6}
$$

**2. 变量定义与解释：**

*   **目标函数 SGI：**
    $$
    \mathrm{SGI} = f (\vec {B}) = \frac {\cos \langle \overrightarrow {S G} , \Delta \vec {S} \rangle + \mu | \Delta \vec {S} |}{1 + \sqrt {3} \mu}
    $$

*   **状态变化向量 $\Delta \vec {S}$：**
    $$
    \Delta \vec {S} = \left[ \begin{array}{l} \frac {\mathrm{dEPI}}{\mathrm{dt}} \\ \frac {d S J I}{d t} \\ \frac {d E D I}{d t} \end{array} \right] = \left[ \begin{array}{l l l l l l l} b _ {1 1} & b _ {1 2} & b _ {1 3} & b _ {1 4} & b _ {1 5} & b _ {1 6} & b _ {1 7} \\ b _ {2 1} & b _ {2 2} & b _ {2 3} & b _ {2 4} & b _ {2 5} & b _ {2 6} & b _ {2 7} \\ b _ {3 1} & b _ {3 2} & b _ {3 3} & b _ {3 4} & b _ {3 5} & b _ {3 6} & b _ {3 7} \end{array} \right] \left[ \begin{array}{l} B _ {1} \\ B _ {2} \\ B _ {3} \\ B _ {4} \\ B _ {5} \\ B _ {6} \\ B _ {7} \end{array} \right]
    \tag{7}
    $$

*   **参数说明：**
    *   $\vec {B}$：预算分配矩阵，包含七个因子：$B_1$ (Transport), $B_2$ (Social), $B_3$ (Environmental), $B_4$ (Education), $B_5$ (Health), $B_6$ (Development), $B_7$ (Other)。这些因子源自爱丁堡[14]和惠灵顿[15]的发展计划总结。
    *   $\hat {b}$：通过过去 $k$ 年的数据估计的参数矩阵元素。
    *   $\vec {B} \geq 0$：确保每个预算元素为正数，因为城市预算计划中不能出现负值。
    *   $\Delta \vec {S} \ge 0$：确保 SGI 落在第一象限。
    *   $\sum _ { i = 1 } ^ { 7 } B _ {i} = total Budget$：限制总预算在一定数值范围内。

**知识点：**
非线性规划
最小二乘法

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[多目标优化模型（药物相对充足阶段的配送策略）](../../../topics/数学建模/duo_mubiao_youhua.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 简答 2

**题干：**
如何求解上述非线性规划问题中的参数 $\hat {b}$？请写出残差误差的定义及最小化目标。

**参考解答：**

为了求解模型，使用过去 $k$ 年的数据通过**最小二乘法（Least Square Method）**来估计参数 $\widehat {b}$。

**1. 残差误差定义：**
用 $e$ 表示残差误差：
$$
e = \Delta S _ {k} - \hat {b} B _ {k}
$$

**2. 数据矩阵定义：**
$$
\begin{array}{r} \Delta S _ {k} = \left[ \Delta \vec {S} _ {t - 1} \Delta \vec {S} _ {t - 2} \dots \Delta \vec {S} _ {t - k} \right] \\ B _ {k} = \left[ \vec {B} _ {t - 1} \vec {B} _ {t - 2} \dots \vec {B} _ {t - k} \right] \end{array}
\tag{8}
$$

**3. 求解策略：**
使用最小二乘法最小化残差误差（原文截断于 "Using the least square method to minimize"，通常后续为最小化误差平方和 $\min \| e \|^2$）。

**知识点：**
最小二乘法

# 2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文精选：城市智慧增长模型（习题）

## 一、模型推导与算法设计

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)、[非技术性文稿撰写（如致世界医学会的信函、新闻发布会声明）](../../../topics/数学建模/fei_jishu_wengao.md)

### 计算 1 最优预算分配系数的求解

为了确定各预算组件的最优分配比例，模型通过最小化误差范数来求解系数 $\hat{b}$。

根据公式：

$$
\left\| e \right\| ^ {2} = e ^ {T} e = \left\| \Delta S _ {k} - \hat {b} B _ {k} \right\| ^ {2}
$$

我们可以得到：

$$
\hat {b} = (B _ {k} ^ {T} B _ {k}) ^ {- 1} B _ {k} \Delta S _ {k}
$$

其中，$B _ { k }$ 可以直接从惠灵顿[17]和爱丁堡[18]的预算计划中获得。为了获得 $\Delta S _ { t }$，我们计算相邻两年状态（S）之间的差异，使用以下方程：

$$
\Delta S _ {t} = \left[ \begin{array}{c} \frac {d E P I}{d t} \\ \frac {d S J I}{d t} \\ \frac {d E D I}{d t} \end{array} \right] _ {t} = \left[ \begin{array}{c} E P I _ {t + 1} \\ S J I _ {t + 1} \\ E D I _ {t + 1} \end{array} \right] - \left[ \begin{array}{c} E P I _ {t} \\ S J I _ {t} \\ E D I _ {t} \end{array} \right]\tag{9}
$$

在求得 $\hat { b }$ 后，我们可以将其代入模型以计算相应的最佳预算分配 $\vec { \mathrm { B } } _ { \mathrm { o p t i m a l } }$，并根据其潜力对各组件进行排名。一个组件的潜力是通过比较当前预算与最优预算来计算的。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 计算 2 未来几十年最优状态的预测

下一年的状态可以通过当前年份的状态和最优预算分配来计算，公式如下：

$$
\left[ \begin{array}{c} E P I \\ S J I \\ E D I \end{array} \right] _ {t + 1} = \left[ \begin{array}{c} \frac {d E P I}{d t} \\ \frac {d S J I}{d t} \\ \frac {d E D I}{d t} \end{array} \right] _ {t} + \left[ \begin{array}{c} E P I \\ S J I \\ E D I \end{array} \right] _ {t} = \left[ \begin{array}{c c c c c c c} b _ {1 1} & b _ {1 2} & b _ {1 3} & b _ {1 4} & b _ {1 5} & b _ {1 6} & b _ {1 7} \\ b _ {2 1} & b _ {2 2} & b _ {2 3} & b _ {2 4} & b _ {2 5} & b _ {2 6} & b _ {2 7} \\ b _ {3 1} & b _ {3 2} & b _ {3 3} & b _ {3 4} & b _ {3 5} & b _ {3 6} & b _ {3 7} \end{array} \right] \left[ \begin{array}{c} B _ {1} \\ B _ {2} \\ B _ {3} \\ B _ {4} \\ B _ {5} \\ B _ {6} \\ B _ {7} \end{array} \right] _ {\textit {o p t i m a l}} + \left[ \begin{array}{c} E P I \\ S J I \\ E D I \end{array} \right] _ {t}\tag{10}
$$

在上述方程的右侧，第一项是最优的 SGI（Smart Growth Index，智慧增长指数），第二项是 $t$ 年的状态。基于此方程，我们可以绘制城市在未来几十年的状态变化图。

知识点：[长期预测模型（如20年可持续发展计划预测）](../../../topics/数学建模/nian_yuce.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 计算 3 增长计划的制定与组件排序

基于上述的 $\Vec { B } _ { o p t i m a l }$，我们能够对智慧增长计划中的各个独立举措按潜力从高到低进行排序。

最优预算向量为：

$$
\vec {B} _ {o p t i m a l} = \left[ B _ {1} B _ {2} B _ {3} B _ {4} B _ {5} B _ {6} B _ {7} \right]
$$

我们得到预算分配中组件和举措的排序结果：

$$
\vec {B} _ {o p t i m a l} = [ B _ {1} ^ {\prime} B _ {2} ^ {\prime} B _ {3} ^ {\prime} B _ {4} ^ {\prime} B _ {5} ^ {\prime} B _ {6} ^ {\prime} B _ {7} ^ {\prime} ]
$$

其中满足：

$$
B _ {1} ^ {\prime} > B _ {2} ^ {\prime} > B _ {3} ^ {\prime} > B _ {4} ^ {\prime} > B _ {5} ^ {\prime} > B _ {6} ^ {\prime} > B _ {7} ^ {\prime}
$$

通过比较当前预算计划与最优预算分配计划，我们可以制定未来几十年的增长计划。

## 二、案例研究

知识点：[人口密度修正系数与新公式](../../../topics/数学建模/renkou_midu.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 综合 1 爱丁堡与惠灵顿的当前增长计划评估

在第 3 节所做的假设下，我们使用第 4.1 节开发的三维基准立方体模型来评估 2005 年至 2015 年间爱丁堡和惠灵顿的增长状况。由于这两个城市未来四十年的发展计划[14,15]与过去十年相当相似，且我们假设爱丁堡和惠灵顿的政治和经济环境相对稳定，因此使用我们从 2005 年到 2015 年收集的数据来衡量当前的增长计划是合理的。

#### 综合 1.1 爱丁堡当前增长计划的评估

基于我们从苏格兰人口普查[6]收集的数据，我们计算了爱丁堡的增长状况。前期状态是 2004、2005 和 2006 年状态的均值。当前状态是 2013、2014 和 2015 年状态的均值。结果如下表所示：

**表 5. 爱丁堡评估结果**

| State | EPI | SJI | EDI |
| :--- | :--- | :--- | :--- |
| Previous | 0.4029 | 0.4234 | 0.2751 |
| Current | 0.6201 | 0.6686 | 0.6173 |
| CG | 0.2172 | 0.2452 | 0.3422 |
| SGI | colspan="3">0.2814 |

*注：原表中 SGI 行跨列合并，此处 Markdown 表格无法完美呈现跨列效果，通常写作单格或省略其他列。为保持数据清晰，建议格式如下：*

| State | EPI | SJI | EDI |
| :--- | :--- | :--- | :--- |
| Previous | 0.4029 | 0.4234 | 0.2751 |
| Current | 0.6201 | 0.6686 | 0.6173 |
| CG | 0.2172 | 0.2452 | 0.3422 |
| SGI | 0.2814 | | |

根据结果，CG 的三个因子均为正值。因此，爱丁堡的增长符合三个 E 的要求，该城市处于智慧增长状态。然而，爱丁堡的发展也存在一些不足。爱丁堡的 SGI 为 0.2814，这意味着智慧增长处于较低水平。虽然三个因子均为正值，但每个分量的值相对较小，尤其是 EPI 和 SJI。爱丁堡仍有很大发展空间。

#### 综合 1.2 惠灵顿当前增长计划的评估

与爱丁堡的情况类似，我们使用从新西兰统计局[7]收集的数据来获得惠灵顿的增长状况。前期状态是 2004、2005、2006 年状态的均值，当前状态是 2013、2014、2015 年状态的均值。结果如下表所示：

**表 6. 惠灵顿评估结果**

| State | EPI | SJI | EDI |
| :--- | :--- | :--- | :--- |
| Previous | 0.5612 | 0.3026 | 0.9284 |
| Current | 0.3806 | 0.6390 | 0.3000 |
| CG | -0.1806 | -0.3374 | 0.6284 |
| SGI | — | | |

*注：原表中有 Team #67171 Page 13 of 20 的水印信息混入表格单元格，已去除。SGI 值为破折号，表示未计算或无有效值。*

It’s clear from the table that there are two factors (EPI and SJI) that are negative, which means that both social equality and environment of Wellington got worse between 2005 and 2015. Thus, the growth of Wellington is not smart growth. However, there is also a merit in the development of Wellington. Compared with that of Edinburgh, the EDI of Wellington is much higher (0.6284). Thus, the rate of economic growth is higher in Wellington, but the growth of the city not in a smart way.

![Fig 4. SJI and EDI in current growth plan of Edinburgh and Wellington](2017年美国大学生数学建模竞赛MCM-ICMO奖论文精选：城市智慧增长模型.assets/图3.jpg)

![Fig 5. SJI and EPI in current growth plan of Edinburgh and Wellington](2017年美国大学生数学建模竞赛MCM-ICMO奖论文精选：城市智慧增长模型.assets/图4.jpg)

![Fig 6. EDI and EPI in current growth plan of Edinburgh and Wellington](2017年美国大学生数学建模竞赛MCM-ICMO奖论文精选：城市智慧增长模型.assets/图5.jpg)

![Fig 7. The current growth plan of Wellington and Edinburgh in the cube model](2017年美国大学生数学建模竞赛MCM-ICMO奖论文精选：城市智慧增长模型.assets/图6.jpg)

知识点：[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[长期预测模型（如20年可持续发展计划预测）](../../../topics/数学建模/nian_yuce.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)

### 5.2 Growth Plan for Edinburgh and Wellington

Based on the model developed in section 4.2 and the budget plan of Edinburgh and Wellington from 2009 to 2015[17,18], we achieved the optimal budget plan for the two cities. Then, according to the difference between the current budget plan and the optimal plan, we raised a new development plan.

知识点：[多目标优化模型（药物相对充足阶段的配送策略）](../../../topics/数学建模/duo_mubiao_youhua.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 5.2.1 Growth Plan for Edinburgh

The current budget plan of Edinburgh is an average of the budget from 2009 to 2015. The optimal budget plan for next three decades is calculated with the current budget plan with the model raised in section 4.2. The results of current plan and optimal plan are shown in following table as percentage of total budget:

Table 7. the current budget plan and optimal budget plan(% of total budget) of Edinburgh

| Term | Factor | Current plan(%) | Optimal plan(%) | Change Δ (%) |
| --- | --- | --- | --- | --- |
| B1 | transport service | 0.9887 | 8.0097 | 7.0210 |
| B2 | social service | 36.6694 | 30.0526 | -6.618 |
| B3 | environmental service | 7.8152 | 14.7184 | 6.9032 |
| B4 | education service | 41.1969 | 31.1592 | -10.0377 |
| B5 | health service | 3.8814 | 7.6051 | 3.7237 |
| B6 | development service | 1.8227 | 7.9766 | 6.1539 |
| B7 | other | 7.6256 | 0.4785 | -7.1471 |
| Total | All | 100 | 100 | 0 |

According to the table, we give the following suggestions for the growth plan in the next three decades. Since it is not practical for a city to transform the current plan to the optimal plan in a short time, we made a growth plan with a period of three decades for the city to develop from current situation to optimum smart growth.

1) Increase transport service from current 0.9887% to optimal 8.0097%. The transport service budget in current plan is rather small, which has became a limitation for the further development of the city. To increase the transport service, the government can take a variety of measures, such as adding additional bus lines, building more public transport facilities and updating the road systems of the city.

2) Decrease social service from 36.6694% to 30.0526%. By cutting off unnecessary fire and social work, the social service budget can be slightly reduced.

3) Increase environmental service from 7.8152% to 14.7184%. The government should put more funding into the environmental protection service. This is also a good way to boost the tourism industry.

4) Decrease education service from 41.1969% to 31.1592%. In current budget system, a large proportion of funding is used for education. This high budget can be decreased by reducing excess welfare and adopt new education policy.

5) Increase health service from 3.8814% to 7.6051%.

6) Increase development service from 1.8227% to 7.9766%.

7) Decrease other from 7.6256% to 0.4785%.

After raising the optimal growth plan, we developed the growth plan figure which represents the change of EDI, SJI and EPI in the next three decades. The figure is shown below:

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 5.2.2 Growth Plan for Wellington

Similar to the case of Edinburgh, the optimal budget plan of Wellington for the next three decades is calculated with the current budget plan and the model of 4.2. The results of current plan and optimal plan are shown in following table as percentage of total budget:

Table 8. the current budget plan and optimal budget plan(% of total budget) of Wellington

| Term | Factor | Current plan(%) | Optimal plan(%) | Change Δ (%) |
| --- | --- | --- | --- | --- |
| B1 | transport service | 12.4286 | 7.5749 | -4.8537 |
| B2 | social service | 49.8571 | 41.6691 | -8.1880 |
| B3 | environmental service | 7.1429 | 18.7261 | 11.5832 |
| B4 | education service | 4.8571 | 11.3591 | 6.5020 |
| B5 | health service | 3.1429 | 3.8608 | 0.7179 |
| B6 | development service | 16.8571 | 10.5691 | -6.2880 |
| B7 | other | 5.7143 | 6.2409 | 0.5266 |
| Total | All | 100 | 100 | 0 |

we give the following suggestions for the growth plan in the next three decades for Wellington.

1) Decrease transport service from current 12.4286% to optimal 7.5749%. In current budget plan, the transport service makes up a relatively large proportion of the budget. The government should take new transport policy to reduce the cost in

知识点：[长期预测模型（如20年可持续发展计划预测）](../../../topics/数学建模/nian_yuce.md)、[多目标优化模型（药物相对充足阶段的配送策略）](../../../topics/数学建模/duo_mubiao_youhua.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 5.3 Ranking and Comparison of Components

After achieving the current plan and optimal plan of Edinburgh and Wellington, we ranked the components according to their potential and made a comparison between the two cities. The results are shown in the following table:

Table 10. ranking and comparison of components for Edinburgh and Wellington

| Ranking | Edinburgh Components | Change $|\Delta|$ (%) | Wellington Components | Change $|\Delta|$ (%) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | education service(B4) | 10.0377 | environmental service(B3) | 11.5832 |
| 2 | Other(B7) | 7.1471 | social service(B2) | 8.1880 |
| 3 | transport service(B1) | 7.0210 | education service(B4) | 6.5020 |
| 4 | environmental service(B3) | 6.9032 | development service(B6) | 6.2880 |
| 5 | social service(B2) | 6.6180 | transport service(B1) | 4.8537 |
| 6 | development service(B6) | 6.1539 | health service(B5) | 0.7179 |
| 7 | health service(B5) | 3.7237 | Other(B7) | 0.5266 |
| Average | — | 6.8007 | — | 5.5228 |

It is clear from table that there is a significant difference in the most potential components between Edinburgh and Wellington. For Edinburgh, the top three components are education service, other and transport service, representing 10.0377%, 7.1471% and 7.0210% respectively, while in Wellington environmental service(11.5832%), social service(8.1880%) and education service(6.5020%) are the dominating components. Similarly, the least three components are generally not the same expect the health service.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 5.4 Explanation of Growth Plan in Additional 50% Population Growth

According to the modified cube model, we can support the population growth by adjusting the distribution of the budget.

We proposed SJI, EDI, EPI to measure the process of ‘Smart Growth’. Considering another 50% growth of population, we reanalyze the three indicators qualitatively. We assumed that SJI is made up of the employment rate and literacy rate between males and females, and Gini coefficient. We raised that the proportion of growth people follows that of the current people, which means that there will be the same scale of people who are not in study, who are out of job, and who are members of low-income group. As is demonstrated above, the first indicator, SJI, will remain unchanged with the burgeoning population.

The second index (EDI) consists of life expectancy, GDP per capita and expanse of GDP. As we mentioned above, the rising population follows the original population ratio. It is reasonable to believe that the health level will be the same as before, which means that life expectancy will not change. The statistics shown in the chart demonstrates the stagnation in GDP per capita since the financial crisis in the UK[19], we can conclude that GDP per capita will fluctuate on an even keel. The amount of expanse and GDP will increase with the the rise of the population at similar rate. Thus, we can assume that expense of GDP will not change. In conclusion, it is reasonable to assume that EDI will not be severely affected by the population growth.

As for the last index EPI, it is acceptable to assume that the total greenhouse gas emission will increase with the rise of population when the economic and political status is stable. After analyzing the data, we achieved the result that the EPI will decrease. Also, the city will need to provide more space for living, which will reduce the forest area invisibly. In addition, According to the EU Public Affairs, Regulatory, Policy & Government Relations Professional, Bogdan Patru, In 2014, the share of energy from renewable sources in gross final consumption of energy reached 16% in the EU, almost double that of 2004 (8.5%), the first year for which data is available[20]. However, the renewable energy is still a small part of the final energy. With the population growing, there is no enough renewable energy to consume, while the total energy is required to increased to meet their increasing demands, which will bring about the renewable energy consumption ratio dropping sharply.

Finally, we concluded that EPI will decrease until the environment can not afford it. Among the three indicators, we reached the conclusion that only EPI increases with the rise of population, and the city budget should be adjusted to adapt to the change. As for the budget plan we came up with in section5.2, only the environment service budget is related to EPI, so we need to add the environment budget to improve environment conditions to reduce the impact caused by population growth.

Considering the specific index of EPI, the city should put more budget into reducing the emission of greenhouse gas. There are many measures that can be adopted to achieve this goal. For example, the government could support the study of improving energy efficiency by providing financial support. Besides, we should put more funds into planting trees and building flats to reserve the forest area. Last but not least, the government is supposed to discover and develop new energy. Advanced technology shall be utilized to improve the versatility and reduce the storage of renewable energy.

## VI. Model Testing

We tested our model by the method of F test. We denoted regression sum of squares by RSS and residual sum of squares by SSE.

$$
\begin{array}{c} M S R = \frac {S S R}{k - 1} \\ M S E = \frac {S S E}{T - k} \\ F = \frac {M S R}{M S E} = \frac {S S R / (k - 1)}{S S E / (T - k)} \end{array}\tag{11}
$$

The null hypothesis is rejected if the F calculated from the data is greater than the critical value of the F-distribution for some desired false-rejection probability (e.g. 0.05).

## VII. Sensitivity Analysis

In this section, we tested the sensitivity of the baseline cube model changing one of the

# 城市智慧增长模型（O奖论文精选）

本节内容源自2017年美国大学生数学建模竞赛（MCM/ICM）O奖论文，主要包含参数敏感性分析结果、模型的优缺点总结以及参考文献。原文为论文的第9部分（第20–22页），已整理为结构化文档。

## 一、敏感性分析：基尼系数变化对爱丁堡的影响

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 选择 1

**背景说明**：为了验证模型的稳健性，研究团队将爱丁堡的基尼系数（Gini coefficient）从原始值 $0.3087$ 调整为 $0.3859$（增幅 $25\%$），并对比了改变前后的各项指标结果。

| 指标 | 原始结果 (original) | 改变后结果 (changed) | 变化幅度 $\Delta(\%)$ |
| :--- | :---: | :---: | :---: |
| **EPI** | 0.2172 | 0.2172 | 0 |
| **SJI** | 0.2452 | 0.2247 | 8.3605 |
| **EDI** | 0.3422 | 0.3422 | 0 |
| **SGI** | 0.2814 | 0.2767 | 1.6702 |

> **注**：表格数据根据原文 Table 11 整理。其中 SGI 在原文中为跨列合并单元格，此处统一列出数值。

- **分析结论**：当基尼系数变化 $25\%$ 时，社会正义指数（SJI）变化了 $8.3605\%$，社会总体增长指数（SGI）变化了 $1.6702\%$。由于基尼系数仅用于计算 SJI，因此其他参数（EPI 和 EDI）保持不变。
- **模型特性**：总体而言，当第三阶段参数发生变化时，第二阶段（SJI）的灵敏度相对较高，而第一阶段（SGI）则相当不敏感。

## 二、模型的优缺点分析

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 选择 2

#### 9.1 模型优势

##### 9.1.1 包容性 (Inclusive)

我们的基线立方体模型和修正后的立方体模型分别包含了 9 个独立参数和 7 个独立组件。这些参数和组件代表了决定城市增长的大部分主要因素，使得模型相对可靠且具有包容性。

##### 9.1.2 量化 (Quantification)

在我们的模型中，“三个 E"（环境、经济、社会）的要求被转化为三个无量纲指数。在对参数进行归一化处理后，更容易判断增长是否为“智慧增长”，并对智慧增长的等级进行分类。同时，通过量化这些因素，评估过程变得更加清晰和直观。

##### 9.1.3 简单但通用 (Simple but Universal)

我们模型的构建过程简单，因素与结果之间的关系清晰明了。然而，通过引入一些包容性的参数和组件，该模型很容易应用于其他城市的案例。因此，我们的模型也具有较强的通用性。

##### 9.1.4 可见且易懂 (Visible and Understandable)

通过引入三维立方体，我们能够直接、可视地展示结果。这一优点也使得人们更容易理解我们的模型。此外，我们将模型中的组件与社会发展中的因素联系起来，使模型更加易于理解。

#### 9.2 模型劣势

##### 9.2.1 准确性依赖于统计数据 (Accuracy Relies on Statistics)

在我们的模型中，需要大量的统计数据来确保预测的准确性和可靠性。因此，修正后的立方体模型依赖于数据库来保证准确性。

##### 9.2.2 未包含灾害 (Disasters Are Not Included)

在我们的模型中，未考虑包括自然灾害和人为破坏事件在内的紧急事件。在面对毁灭性灾害时，我们的模型不可靠。

##### 9.2.3 差分替代导数 (Difference Replaced Derivatives)

我们使用相邻两年的差值来计算导数，这不能保证绝对的准确性。因此，微小的误差可能会被引入我们的模型中。不过，这不会影响模型的可靠性。

## 三、参考文献

[1] World Urbanization Prospects. Retrieved from: https://esa.un.org/unpd/wup/Publications/Files/WUP2014-Highlights.pdf

[2] Local Government Commission. Retrieved from: http://www.lgc.org/about/ahwahnee/principles

[3] New Partners. Retrieved from: https://www.newpartners.org/about-the-event/

[4] Boeing, Geoff; Church, Daniel; Hubbard, Haley; Mickens, Julie; & Rudis, Lili. (2014). LEED-ND and Livability Revisited. Berkeley Planning Journal, 27(1). ucb\_crp\_bpj\_24500. Retrieved from: https://escholarship.org/uc/item/49f234rd

[5] EPA. Retrieved from: https://www.epa.gov/smartgrowth/smart-growth-publication

[6] Scotland's census. Retrieved from: http://www.scotlandscensus.gov.uk/ods-web/area.html

[7] Statistics New Zealand. Retrieved from: http://nzdotstat.stats.govt.nz/wbos/index.aspx#

[8] Montenegro A. An Economic Development Index[J]. Development & Comp Systems, 2004.

[9] The big three economic indicators. Retrieved from: https://www.discoveroptions.com/mixed/content/education/articles/bigthreeeconomicindicators.html

[10] Social Justice Index. Retrieved from: http://www.social-inclusion-monitor.eu/social-justice-index/

[11] Environmental Performance Index. Retrieved from: https://en.wikipedia.org/wiki/Environmental\_Performance\_Index

[12] Yale Center for Environmental Law & Policy, and Center for International Earth Science Information Network at Columbia University. "Environmental Performance Index"

[13] Li, Y., Zhang, K. S., Song, N., Chen, L. Comparison of Two Analytical Approaches in the Assessment of Urban Sustainable Development. Huanjing Kexue yu Jishu, 2012, 35(8), 199-205.

[14] The city of Edinburgh Council. Retrieved from: http://www.edinburgh.gov.uk/localdevelopmentplan

[15] Wellington city council. Retrieved from: http://wellington.govt.nz/have-your-say/public-inputs/feedback/closed/wellington-urban-growth-plan

[16] N.V. Prosyanik. Retrieved from: http://www.nbuv.gov.ua/old\_jrn/Soc\_Gum/Vdnuet/econ/2012\_4/Prosanik.pdf

[17] Wellington County. Retrieved from: http://www.wellington.ca/en/government/budget.asp

[18] The city of Edinburgh Council. Retrieved from: http://www.edinburgh.gov.uk/downloads/file/8300/key\_facts\_and\_figures\_booklet\_2016-2017

[19] SPERI British Political Economy Brief No. 7. Retrieved from: http://speri.dept.shef.ac.uk/wp-content/uploads/2014/09/Brief7-the-relationships-between-economic-growth-and-population-growth.pdf

[20] Renewable energy share rose to 16% in 2014. Retrieved from: https://www.linkedin.com/pulse/renewable-energy-share-rose-16-2014-bogdan-patru

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)
