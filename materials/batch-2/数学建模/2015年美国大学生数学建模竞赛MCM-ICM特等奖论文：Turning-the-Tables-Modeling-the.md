---
title: 2015年美国大学生数学建模竞赛（MCM/ICM）特等奖论文：Turning the Tables: Modeling the Fight against Ebola
kind: 习题
course: 数学建模
source: batch-2:数学建模/2015美赛特等奖原版论文集.zip/2015美赛特等奖原版论文集/32722.pdf
---

# 2015年美国大学生数学建模竞赛（MCM/ICM）特等奖论文：Turning the Tables: Modeling the Fight against Ebola

原件经识别和整理；“参考解答”是我们补的。

## Abstract

We have constructed a multi-layer state-based model that appears to hold promise for providing insight into not only how the Ebola outbreak in West Africa will continue to develop, but also the best course of intervention in the event an effective vaccine or cure should be created. This model considers a large number of parameters thought to be important to or characteristic of the outbreak, including the impact of the infection's unique progression in humans, transmission to new individuals from infected persons at different stages of the infection, and the effects of geographic connections on the movement of infected persons and pharmaceuticals. The aforementioned multi-layer approach includes interactions on the level of the individual, a collection of individuals (or "region"), and a collection of regions, in order to capture behaviors at each scale. Individuals transition through states, representing the various stages of an Ebola infection, in a stochastic way with some probabilities being intrinsic to the illness and some being related to the current state-of-affairs in the region. Individuals are treated as homogeneously mixed within regions, but are capable of moving between regions with probabilities determined by the various characteristics of each region. Distribution of medicines occurs at the local level through hospitals and at the regional levels through transit, with medicines and vaccines entering the simulation through defined transportation "hubs", then being distributed along defined delivery routes from region to region. Our model focuses exclusively on the three countries still suffering from an active presence of Ebola (Guinea, Liberia, and Sierra Leone), making predictions across the next 6 months. Specific attention is given to the sensitivity of our model to variations in its fundamental parameters, whose values are based largely on inadequate and varied statistical data from regions affected by the outbreak. We attempt to use our model to identify important factors related to the effectiveness of distributing a cure for Ebola, and show simulation results related to the influence of geographic factors, delivery frequency/quantity, and distribution tactics in comparison to baseline predictions. Ultimately, we have concluded that given the complex nature of this scenario and the limited quantity and quality of detailed information concerning the outbreak, it is not possible at this time to quantitatively predict the effectiveness of a vaccine/cure distribution plan. Instead, the results presented here qualitatively show how our baseline model responds to changes in the parameters that govern its behavior. These qualitative results are then used to craft a tentative deployment strategy for these hypothetical vaccines and cures.

## Contents

1 Introduction 4
1.1 Context of the Problem
1.2 The Task at Hand 5
1.3 Previous Work 6
1.4 The GLEAM Simulator 6
2 Our Model 7
2.1 Modeling Objectives 7
2.2 Problem Space 7
2.3 The Multi-Layer State Based Stochastic Epidemic Model 8
2.3.1 Individual Layer - Stochastic State Based Model 9
2.3.2 Inter-Region Layer modeling 12
2.3.3 Human Mobility Model 12
2.3.4 Supply Distribution Model 14
2.3.5 A note on GLEAM 14
2.4 Implementation 15
2.5 Additional Considerations 15
2.5.1 Modeling of Hospitals 15
2.6 Consequences of Complexity 16
3 Sensitivity Analysis and Results 16
3.0.1 Individual Region Tests 17
3.0.1.1 Initial Number of Infected 17
3.0.1.2 Hospital Bed Number 18
3.0.1.3 Population Scale 18
3.0.1.4 Medicine Efficacy 19
3.0.2 Vaccine Quantity and Frequency of Shipments 20
3.0.3 Multiple-Region Simulations 22
3.0.4 Vaccine Distribution 22
3.0.5 Cure Distribution 24
3.0.5.1 Initial Distribution of Infected 26
3.0.5.2 Movement Parameter Variation 26
3.0.5.3 Inter-Regional Parameter Variation 27
3.1 Further Sensitivities and Limitations 28
3.1.1 Weather Dynamics 28
3.1.2 Burial 28
4 Conclusion 28
4.1 Future Epidemic Trajectories 28
4.2 Summary and Recommendations 29
4.2.1 The Art of Eradicating Ebola 30
4.3 Future Work 31
4.3.1 Geography Based Modeling 31
4.3.2 Placement of Distribution Centers 32
4.3.3 Distribution Laws 32
Appendix A Assumptions 34
Appendix B Differential Equation Model 35

# Turning the Tables: Modeling the Fight against Ebola

本资料为 2015 年美国大学生数学建模竞赛（MCM/ICM）特等奖论文《Turning the Tables: Modeling the Fight against Ebola》第 2 部分（共 17 部分）中第 4–5 页的整理内容，包含问题背景与任务描述。

## 一、问题背景 (Context of the Problem)

### 选择 1

题干：西非埃博拉病毒疫情是过去三十年最严重的急性人类健康危机之一。

- A. 其影响超过了 SARS 和禽流感、猪流感。
- B. 该疾病于 2014 年 3 月被发现，在过去十个月内感染了超过 20,000 人，并导致近一半感染者死亡。

答案：A、B 均为正确描述。
参考解答：根据原文第一段，该疫情被描述为“过去三十年中最严重的急性人类健康危机之一”，其影响远超 SARS 以及备受诟病的禽流感和猪流感。数据指出，自 2014 年 3 月发现以来，已感染超过 20,000 人，死亡人数接近感染人数的一半 [1]。

![图 1：埃博拉病毒 [3]](figure:4c20b266b9cf0dda28829d71bb7c0ed200d58b2698ed6e97e538a6f88937107f-0/50a18f4dbe332d217dec39793e72efd0530226c426d088d5411f735cafb870cc.jpg)

**背景说明：**
埃博拉病毒是人类近期新增的威胁，首次报告于 1976 年的苏丹和刚果民主共和国。由于该病毒具有高度传染性和致命性，2014 年之前的所有疫情规模仅为数百人；大多数感染倾向于在大规模传播前自行消退（flare-up, flare-out）。这种偶发性阻碍了对该疾病、其自然宿主及潜在治疗方案的研究。

埃博拉扎伊尔株（即当前肆虐西非的毒株，后文简称为“埃博拉”）主要通过直接接触体液传播，通过皮肤破损或粘膜进入人体。这意味着通过使用防护设备和程序——如手套、口罩和面罩——可以阻断体液和接触传播；而谨慎地更换和清洁这些设备可防止交叉污染 [2]。

**潜伏期与症状：**
个体暴露于埃博拉病毒后，有 2 至 21 天的潜伏期，在此期间个体无症状且无传染性 [4]。平均而言，症状在 8 至 10 天后出现。早期症状类似流感及其他多种更常见的疾病，增加了检测和治疗的难度。数天内，症状从流感样（发热、发冷、头痛、虚弱、喉咙痛、胃痛）发展为更严重的出血热特征症状，包括剧烈出血、极高烧和器官衰竭 [4]。埃博拉病毒病的死亡率因疫情而异，范围为 40%–90%；在当前西非疫情中，报告的死亡率约为 50% 至 61% [1]。

![图 2：塞内加尔、尼日利亚、几内亚、塞拉利昂和利比里亚构成了西非关键的埃博拉国家。目前，只有塞拉利昂、几内亚和利比里亚存在活跃疫情 [1]](figure:4c20b266b9cf0dda28829d71bb7c0ed200d58b2698ed6e97e538a6f88937107f-0/b66586d8178c0dd0b0b5d49b23f86e4848f61ffb177509888fc54f3ece9ded36.jpg)

**地理分布与现状：**
西非的埃博拉疫情跨越该地区多个国家，但在几内亚、利比里亚和塞拉利昂最为严重。尼日利亚、塞内加尔和马里也报告了病例，但疾病应对措施已被证明能有效阻止病毒的进一步传播，这些国家截至 2015 年 2 月 4 日被视为无病毒状态 [1]。西班牙、英国和美国也报告了少量输入性病例；然而，这些国家总体上利用其巨大的医疗资源防止了更多病例的发生，将其控制在少数人范围内。

为了有效建模使原本容易“爆发即消亡”的埃博拉病毒如此毁灭性地袭击这些国家的因素，必须了解该地区当前的状况和问题。

**人口与社会因素：**
从人口统计角度看，西非人口庞大且年轻，总人口约 3.4 亿，平均年龄为 18 岁 [5]。虽然主要有三大语言群体，但该地区的族群人口难以简单分类，由部落和民族纽带交织而成。如前所述，该地区因曾作为欧洲资源掠夺殖民地及军事独裁统治的历史，严重缺乏交通和医疗基础设施。例如，在疫情爆发前，整个利比里亚仅有 50 名医生。这种医疗基础设施的匮乏因其他持续存在的医疗危机（如艾滋病流行病和疟疾）而进一步加剧。此外，多年的专制统治和战争严重削弱了民众对自身政府及外国干预机构的信任，这使得当地政府、世界卫生组织和无国界医生的控制工作变得复杂。

## 二、任务目标 (The Task at Hand)

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 综合 1

题干：如果开发出埃博拉治愈方法或疫苗，其初始供应量极可能极其有限。同时，鉴于目前的疫情蔓延和生命风险，利用现有药物迅速对抗并最终根除埃博拉至关重要。

- A. 团队旨在开发一个数学模型，以制定该地区疫苗/治愈方法交付的有效策略。
- B. 目标是最大限度地减少生命损失，以及与此次疫情相关的全球影响和经济负担。

答案：A、B 均为正确描述。
参考解答：根据原文第二部分，团队的目标是建立一个数学模型，用于制定有效的疫苗或治愈方法交付策略。核心目标是在资源受限的情况下，最小化生命损失、全球影响以及经济负担。

## 1.3. Previous Work

*   Modeling epidemics using mathematics is a practice that dates back before the widespread acceptance of germ theory, starting instead with Bernoulli’s model of the spread of smallpox and the impact of the smallpox vaccine [6]. This model was one of the first applications of the now-common branch of differential equations known as population modeling. Bernoulli was among the first to demonstrate mathematically the effectiveness of vaccination, a major landmark that has been ignored by the superstitious ever since.
*   From these population models, a branch of the differential equations based modeling approach known as compartmental models arose. First seen in 1927 with Kermack and McKendrick’s “Susceptible - Infected - Recovered” (SIR) approach, these models provide a means of modeling the development of epidemics while taking into account the characteristics of the disease being spread [7]. These SIR models have proven themselves to be extremely adaptable, and are frequently used to deterministically analyze the spread of relatively nonlethal diseases like Measles and Chickenpox in small populations. These models have served as the framework for the bulk of the epidemic modeling work done in the mid to late $20^{\mathrm{th}}$ century. The rise of computational power in the late $20^{\mathrm{th}}$ century has enabled the creation of an entirely new category of numerical, agent-based models for simulating the spread of epidemics.

## 1.4. The GLEAM Simulator

The Global Epidemic And Mobility simulation/visualizer suite (or GLEAMviz/GLEAM) is a framework for the creation of extremely detailed models of disease spread on a global scale. GLEAM uses a modular, multi-layer approach to incorporate many layers of information into a high-fidelity state-based simulation [8].

GLEAM’s primary benefit is its extremely detailed mobility model, which incorporates data from a variety of commercial and government sources on road, rail, sea, and air transportation between defined transportation “regions.” An accurate model of transportation between regions is incredibly important for accurately simulating the spread of a disease originating in discrete regions, and GLEAM delivers on this point.

Regional spread and disease progression characteristics are determined by stochastic, state-based rules defined within each region. Each simulated person has an associated state, such as infected or recovered. As time progresses in the simulation, each person has a chance to change from their current state to another state. The possible states, as well as the probability of changing to any given state, can be defined using a directed graph of states to states, with edges weighted by the probability of changing from one state to another. GLEAM allows users to rapidly implement their own set of state-changing rules using its convenient desktop client. Unfortunately we were unable to utilize this software for our own purposes (due to limitations to be discussed later), though we did see merit in such a novel and extensible state-based approach.

# 2. Our Model

## 2.1. Modeling Objectives

We aim to develop a model that captures the behavior of both the current Ebola outbreak in West Africa and the impact that a hypothetical vaccine or cure for Ebola would have on said outbreak. This aim is easily separated into two components: accurately accounting for the various factors and implications behind the spread of Ebola, and providing a model of the intricacies involved in the distribution and application of such treatments. This flows down and creates further issues that must be dealt with.

Ebola’s distinctive prognosis is a significant enough factor in its spread that we feel the need to incorporate it in our model. For an epidemic disease, Ebola tends to strike and kill at an alarming rate, with only a brief symptomatic period before an infected individual dies. This behavior, while frightening, has tended in the past to produce intense but short-lived outbreaks as the disease strikes down individuals before they can spread it to others. While this outbreak appears to buck the trend, it is still subject to the same fundamental progression of symptoms as the others; by ensuring that these characteristics are modeled faithfully, we can more carefully analyze scenarios that play off the natural tendency of the virus to cause self-destroying outbreaks.

As mentioned in Sec. 1, the current outbreak has arisen from a complex combination of social, political, economic, and ecological factors in West Africa, and many of these factors continue to complicate the health response. We make a decided effort to capture these “environmental” factors as they relate to the direct spread of Ebola, especially when they are characteristic of the outbreak, cf. sections 2.3.1 and 2.3.3. Examples of characteristic environmental factors influencing the spread of the outbreak include infection from burial and human migration.

Our final criterion for the model is that it faithfully and accurately shows the impacts of a hypothetical vaccine on the ongoing epidemic, which is surprisingly even harder than it sounds. The hypothetical nature of the vaccine or cure gives us control over its effectiveness and mechanism of action, but also presents a large unknown within our model that must be able to be tuned. Likewise, the freedom inherent to the unspecified distribution mechanism for the treatments requires us to model the impact of the geographic and infrastructure constraints of the region.

## 2.2. Problem Space

Breaking down these aims into something we could feasibly create in 96 hours was not a simple task. To simplify the problems our model must deal with, we have seen it prudent to define a problem-space through the definition of boundary assumptions. The implications of these boundary assumptions are expanded upon further in Sec. 3 and Appendix A.

Firstly, we have limited our model’s geographic scope to cover only the three most infected countries over the next six months, Guinea, Liberia, and Sierra Leone. While this boundary does not explicitly limit the ability of our model to deal with other nations or epidemics outside of these nations, it does allow us to focus more heavily on those nations that are hardest hit and therefore most likely to receive a coordinated eradication campaign and tailor our model more closely to these critical regions.

![Figure 3: The network and interaction of diferent regions are mediated by the sub-network of cities in each region, which is further mediated by the interaction of individuals in a city. Each individual is characterized by a state in the compartment diagram, simulating progression through the epidemic at the base interaction level, cf. Fig. 4 and Sec. 2.3.1.](2015年美国大学生数学建模竞赛MCM-ICM特等奖论文：Turning-the-Tables-Modeling-the.assets/图1.jpg)

Secondly, we expect our model to produce meaningful results only over a short term (i.e. six month) period. The failure of other models devised by major medical associations to forecast long-term conditions is indicative of the incredibly stochastic, complex, and deeply time-varying behaviors lurking behind the epidemic. A short list of these factors includes population growth, migration, seasonal change, and the international political will to support aid efforts. Rather than concerning ourselves with these long-term and varying causes, we can instead concentrate on more immediate and clear factors that will impact near-term results.

知识点：[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)、[人类移动性模型（Human Mobility Model）与跨区域层建模](../../../topics/数学建模/renlei_yidong.md)

### 2.3. The Multi-Layer State Based Stochastic Epidemic Model

The relatively broad scope of our model necessitated the choice of a modeling framework that supports a high level of detail at both the individual level, wherein persons can become infected and progress through the disease with varying levels of infectiousness, to the level of an entire nation and set of nations. The implicitly multi-layer nature of this problem space drove us to use what we describe as a multi-layer state-based stochastic epidemic model, a relatively recent approach.

At the most basic level, the simulation models individuals as state-based creatures that are some quantized level of healthy ranging from susceptible to infected. Individuals transition between states in a stochastic manner, allowing for the simulation of transitions from merely infected to extremely ill to dead. The same probability-based approach also governs the likelihood that an individual will become infected from other infected individuals. More details on the specific structure and function of this layer can be found in the following section.

Moving one layer up from the individual models is the regional or “city” model. Each city acts as a node in a larger network, with connections to nearby cities that allow for the modeling of intercity movement and transportation dynamics. Although a city is comprised of individual state-based persons, the interactions between cities can be governed by different rules that may not arise from individual modeling alone.

Cities can be likewise grouped into nations and further grouped into regions and continents ad absurdum, allowing for progressively larger (or smaller) levels of detail that can be implemented in a modular way. A simulation done at the national level, for example, can be further refined by breaking nations into districts and modeling them separately, down to the level of individual villages or neighborhoods. This implicit scalability and potential for detail made the model extremely attractive for our purposes. Our specific implementation of this model is described below.

#### 2.3.1. Individual Layer - Stochastic State Based Model

At the beginning of each simulation, we designate a number of individuals as either susceptible, latent, or infectious based off of World Health Organization (WHO) data on the outbreak. These individuals are accurately spread throughout the afflicted districts based on the February 2015 Situation Report [1] and, as previously mentioned, progress through the states defined in Fig. 4.

Before even entering into the probability of a state transition, individuals that are susceptible, latent, or displaying early symptoms check to see if they “decide” to move based on their region’s probability of movement, a factor whose determination is discussed in Sec. 2.3.3. Regardless of the outcome of this roll, individuals then proceed to check the modifications of their state within the context of their starting region on that day.

Transitions between states are probabilistic at two levels, depending on the transition. All transitions have a probability of occurring within the state model, defined in Table 1 when an individual is in the preceding state. Some interactions, specifically the chance of a susceptible individual becoming infected and the chance of an individual becoming hospitalized or vaccinated, must be triggered by the simulation before the aforementioned probability calculation.

The probabilities of an individual triggering an interaction with an individual deemed infectious (broken up into early stage symptomatic, late stage symptomatic, and unburied individuals) is simulation dependent and calculated at each timestep from the following equation:

$$
P _ { i n t e r a c t } = \frac { \text { Quantity   of   type   of   individual   in   region } } { \text { Total   number   of   individuals   in   region } }
$$

After a state transition has been triggered, the simulation checks the probability of such a transition occurring as governed by the probabilities listed in Table 1. These probabilities attempt to fit real-world data on the epidemic to an individual’s progression through the disease, normalized to the average duration of each stage of the illness from available data from Sierra Leone and Liberia. Guinea was discounted due to lack of available statistics, and when referenced used data from Liberia. This approach means that, on average, the duration of an individual’s case will be similar if not identical to the average real individual.

![Figure 4: The directed graph compartment model of the Ebola epidemic; red states both carry and are able to spread the infection, the orange states carry the virus but are not able to spread it, and the blue states do not further interact with the simulation. The grey nodes refer to the contact that must occur in order to progress to the next state.](2015年美国大学生数学建模竞赛MCM-ICM特等奖论文：Turning-the-Tables-Modeling-the.assets/图2.jpg)

In the case of susceptible individual triggering an interaction with a carrier of the virus, the simulation checks to see if the susceptible individual definitively contracts the disease, a probability governed by the parameters $\beta _ { c 1 } , \ \beta _ { c 2 }$ , and $\beta _ { f }$ respectively. These parameters represent the probability of an individual becoming infected from contact with an early-stage infected individual, a late stage infected individual, or a deceased but unburied individual, respectively. Once an individual is determined to have contracted the disease, they transition to the latent state.

Latent individuals will eventually transition to early-stage symptomatic individuals at a rate governed by $\gamma _ { w 1 }$ . The rate $\gamma _ { w 1 }$ is calculated by taking the inverse of the average incubation period, consistent with the other data sets [9]. Latent individuals are assumed to be blind to the fact that they have contracted Ebola, and behave identically to susceptible individuals, including their attempts to seek vaccination and move. Unfortunately for them, our simulated vaccines do not work on individuals who have already contracted the virus<sup>1</sup>

<sup>1</sup>In real life, this behavior has the potential for interesting second- and third- order efects, such as “vaccinated” individuals becoming ill and reducing public trust in the vaccine. Sadly, we do not attempt to model such behavior.

Table 1: Model parameter values and explanation. Guinea shares the same parameters as Liberia. Most of the parameter values were taken or derived from Rivers et al. [9]

| Parameter | Liberia Value | Sierra Leone Value | Factor |
|---|---|---|---|
| $\beta_{c1}$ | 0.1600 | 0.1280 | Early-stage contraction probability |
| $\beta_{c2}$ | 0.3200 | 0.2560 | Late-stage contraction probability |
| $\beta_f$ | 0.4890 | 0.1110 | Unburied contraction probability |
| $\gamma_{w1}$ | 0.0833 | 0.0800 | Average rate of developing symptoms |
| $\gamma_{w2}$ | 0.1667 | 0.1600 | Average rate of symptoms worsening [10] |
| $\gamma_{h1}$ | 0.0608 | 0.0478 | Probability of an early-stage hospitalization |
| $\gamma_{h2}$ | 0.1216 | 0.0956 | Probability of a late-stage hospitalization |
| $\gamma_d$ | 0.0335 | 0.0580 | Probability of untreated late-stage death |
| $\gamma_{dh}$ | 0.0551 | 0.1198 | Probability of hospitalized death |
| $\gamma_R$ | 0.0280 | 0.0280 | Recovery rate and probability |
| $\gamma_f$ | 0.4975 | 0.2222 | Rate of proper burials |

Early-stage symptomatic individuals are faced with a choice: become hospitalized with a probability $\gamma _ { h 1 }$ , which has some chance of curing them, or allow their infection to continue to worsen at probability $\gamma _ { w 2 }$ . The probabilities of hospitalization, $\gamma _ { h 1 }$ and $\gamma _ { h 2 }$ , are a product of the portion of cases that are both reported and hospitalized, 0.197, and the inverse of the average time from infection to hospitalization, 3.24 days. As we are considering two stages of infectious, we make the assumption that the probability of hospitalization of a late-stage person is double that of the early-stage. We believe that this reflects the fact that more individuals will attempt to be admitted into a hospital once they realize that their symptoms have advanced beyond a standard flu.

Once an individual “decides” to seek hospitalization, the simulation checks to see if a hospital bed is actually available in that region. If a bed is available, the individual transitions to the hospitalized state and the number of available beds in the region decreases by 1.

The extremely deadly nature of Ebola is reflected in the probabilities of death from hospitalization and untreated late-stage infection. The late-stage death probability, $\gamma _ { d } ,$ is derived from a number of factors. We factor in the percentage of cases that are reported but not hospitalized, (1 − 0.197), the current case mortality rate as of February 6, 2015, (0.555), and the inverse of the average time from infection to death, 13.31 days. The probability of death after hospitalization, $\gamma _ { d h }$ , is the product of the case mortality rate and the inverse of the average time from hospitalization to death, 10.07 days.

On the other hand, the recovery rate, $\gamma _ { R } ,$ is the product of the survival rate, (1 − 0.555), and the inverse of the average time of treated recovery, 15.88 days.

One of the reasons experts believe the current outbreak has been sustained for as long as it has is regional attitudes on corpse-handling, with some traditional funerals calling for a variety of close contact with the corpse (hugging, kissing, touching, et cetera) that allows for infection to occur between individuals and highly infectious corpses. Rivers et al. report that the traditional funeral in Liberia will last 2.01 days on average. It is during this time that a susceptible individual will be able to become infected by an unburied individual with contact probability $\beta _ { f }$ ; hence, the probability to transition from unburied to buried, $\gamma _ { f }$ , is essentially the rate of proper burials, 1/(2.01 days).

## 2.3.1. Vaccine Implementation

For the implementation of the vaccine, we assume the ideal situation of a 100% effective vaccine. Thus we do not have a probability for the transition of susceptible to vaccinated after contact with the vaccination event. Rather, the probability of vaccination is determined by the simulation itself through the supply and demand of the vaccine. In Fig. 4, the latent individuals loop back to themselves upon the vaccination event, reflecting the fact that the vaccination did not work since they are already infected and that they have used some of the vaccine supply as well.

参考解答：## 结论

**选项：** 该模型属于 **多层、基于状态的随机流行病模型**。  
个体层用离散状态（易感、潜伏、感染等）的随机转移描述病程和传染；  
区域层把城市视为节点，个体在区域内按状态随机演化，区域间按移动概率产生交通与传播；  
更高层可按国家、大洲模块化嵌套，使模型可在不同尺度上细化。

---

## 简明推理与关键步骤

### 1. 个体层：状态随机转移

对每个个体，在每个时间步先判定是否移动；无论是否移动，都按当前所在区域继续检查状态变化。

状态转移分两类：

1. **普通状态转移**  
   只要个体处于前一状态，就直接按表 1 给出的概率尝试转移。

2. **需要触发条件的转移**  
   例如易感者被感染、住院或接种疫苗，必须先触发“接触”等条件，再进行概率判定。

---

### 2. 易感者触发感染的概率

题目给出的触发概率为

$$
P_{\text{interact}}
=
\frac{\text{区域内某类个体数量}}{\text{区域内个体总数}}
$$

其中“某类个体”可以是早期症状、晚期症状或未安葬的感染者。

因此，若区域中有：

- 易感者 $S$；
- 早期症状者 $E$；
- 晚期症状者 $L$；
- 未安葬感染者 $U$；
- 区域内总人数 $N$，

则易感者触发与早期症状者接触的概率为

$$
P_{\text{interact, early}}=\frac{E}{N}.
$$

触发后，再用表 1 的感染概率 $p_{\text{inf}}$ 判定是否感染，因此一步内该易感者通过早期症状者感染的总概率为

$$
P_{\text{infection via early}}
=
\frac{E}{N}\cdot p_{\text{inf}}.
$$

类似地，可对晚期症状者和未安葬感染者分别写出：

$$
P_{\text{infection via late}}
=
\frac{L}{N}\cdot p_{\text{inf}},
$$

$$
P_{\text{infection via unburied}}
=
\frac{U}{N}\cdot p_{\text{inf}}.
$$

---

### 3. 区域层：城市节点与交通

每个城市是网络中的一个节点。  
城市之间根据移动概率 $P_{\text{move}}$ 产生人口流动，因此一个区域的疾病状态会受到相邻区域输入感染者的影响。

区域层不直接为每个跨城市个体做完整状态模拟，而是用城市间规则控制移动，再由个体层在新区域中继续随机演化。

---

### 4. 更高层：国家、大洲的模块化嵌套

城市可组成国家，国家可组成区域或大洲。  
每一层只是在更大尺度上重复“节点—连接—流动”的结构。  
因此模型可以逐步细化，而不改变底层个体状态转移逻辑。

---

### 5. 为什么是“多层状态随机模型”

- **多层**：个体、城市、国家、区域等层级可嵌套。
- **状态随机**：个体处于离散健康状态，所有状态转移都按概率发生。
- **基于模拟**：每个时间步逐层更新个体和区域状态，而不是仅使用常微分方程或确定性仓室模型。
- **关键特色**：接触概率由区域当前人口组成决定，体现局部密度和感染构成的影响。

---

## 关键公式总结

区域接触触发概率：

$$
P_{\text{interact}}
=
\frac{\text{区域内感染类型个体数}}{\text{区域内个体总数}}
$$

一步感染概率：

$$
P_{\text{infection}}
=
\frac{I_x}{N}\cdot p_{\text{inf}}
$$

其中 $I_x$ 表示某一类具有传染性的个体数量，$N$ 为区域总人数，$p_{\text{inf}}$ 为触发接触后成功感染的概率。

知识点：[多重网络/多层网络构建（Multiplex/Multi-layer Network）](../../../topics/数学建模/duoceng_wangluo.md)、[随机模型与确定性模型的对比（Stochastic vs Deterministic Model）](../../../topics/数学建模/suiji_queding.md)、[人类移动性模型（Human Mobility Model）与跨区域层建模](../../../topics/数学建模/renlei_yidong.md)

### 2.3.2. Inter-Region Layer modeling

Operating at a level above the individual is the region, which is broadly speaking a representation of a discrete statistical region; in less abstract terms, regions represent villages, cities, or entire national districts and nations themselves depending on the scale of the simulation. Regions provide a number of benefits to the fidelity of the simulation that are unwieldy to model at the individual level, especially with regards to the impact of geography on the spread of disease.

Each region has a number of parameters that can be defined and modified to reflect geographic and statistical realities, cf. Table 1. Regions interact with other regions through discrete, well-defined set of connections in a graph-like manner. Each day, individual regions first check to update their stockpiles of vaccines and/or $\mathrm{cure}^2$ as determined by the drug distribution model (cf. Sec. 2.3.4), and then check to see what the quantity of migration between regions occurs (cf. Sec. 2.3.3). These probabilities are then passed down to the aforementioned individual layer to determine actual movement and cure usage.

An astute reader will recognize this setup as a subtype of the compartmental differential equations approach to epidemic modeling outlined in Sec. 1.3.

> <sup>2</sup>after all, if there was a life-threatening epidemic, isn’t that the first thing you would do each morning?

参考解答：该区域间层模型本质上是**基于图结构的离散时间仓室模型（Graph-based Discrete-time Compartmental Model）**，属于经典仓室微分方程方法的离散化与空间网络化扩展。

-   **结论依据**：文中明确指出该设置是“compartmental differential equations approach”的子类，但通过引入“regions as nodes”和“connections in a graph-like manner”，将连续空间转化为离散网络拓扑；同时，每日按固定顺序（先物资更新、后迁移计算）执行状态转移，体现了从连续微分方程 $\frac{dX}{dt}=f(X)$ 到离散差分 $X_{t+1} = X_t + \Delta X(t)$ 的数值求解思想。
-   **关键计算逻辑**：每个区域 $i$ 在时刻 $t$ 的状态更新遵循时序耦合机制：
    $$
    \begin{aligned}
    S_i(t) &\leftarrow \text{DrugDistribution}(S_i(t-1), \dots) \\
    M_{ij}(t) &\leftarrow \text{MigrationModel}(S_i(t), S_j(t), w_{ij}) \\
    X_i(t+1) &= X_i(t) + \sum_{j} \big( M_{ji}(t) - M_{ij}(t) \big) + \text{EpidemicDynamics}(X_i(t))
    \end{aligned}
    $$
    其中 $S_i$ 为疫苗/药物库存，$M_{ij}$ 为从区域 $i$ 到 $j$ 的迁移量，$w_{ij}$ 为图连接权重，$X_i$ 为流行病学状态变量（如 SIR 各仓室人数）。
-   **为何不是纯个体模型**：虽然迁移概率最终传递给个体层执行，但区域层独立维护统计参数与物资库存，避免了 $O(N^2)$ 级个体交互计算，解决了地理尺度下纯个体模型“unwieldy”的问题。
-   **为何不是连续ODE模型**：尽管归类于ODE方法子类，但其采用“each day”离散时间步和显式事件排序（check → update → pass down），而非连续解析求解，这是为了兼容药物分发与人口迁移等具有固有离散性和时序依赖的现实过程。

知识点：[基本再生数 R0 的估计方法](../../../topics/数学建模/r0_guji.md)、[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)、[人类移动性模型（Human Mobility Model）与跨区域层建模](../../../topics/数学建模/renlei_yidong.md)

### 2.3.3. Human Mobility Model

There are two widely used theories for modeling human mobility, the so-called “radiation” and “gravity” theories. The radiation model predicts the flux of travel between two cities, $T_{ij}$ by their respective populations, $P_i$ and $P_j$, and the population density of the surrounding area<sup>3</sup>, $s_{ij}$:

$$
T _ {i j} = T _ {i} \frac {P _ {i} P _ {j}}{(P _ {i} + s _ {i j}) (P _ {i} + P _ {j} + s _ {i j})}\tag{1}
$$

where $T_i$ is the number of commuters from city $i$. The standard gravity model predicts the flux of travel as a function only of the population of the two cities and the inverse of the distance between them to a quadratic order:

$$
T _ {i j} = \frac {P _ {i} ^ {\alpha} P _ {j} ^ {\beta}}{r _ {i j} ^ {\gamma}}\tag{2}
$$

where $\alpha , \beta$ and $\gamma$ are fitting constants. The literature reports that the radiation model more accurately matches empirical data. Unfortunately, our simulation is based around interactions between distinct groups of people (“regions”) rather than continuous population distributions. The consequence is that we would be unable to get a realistic value for $s_{ij}$ [11].

Data on human mobility is sparse for West Africa, and while this data set does not fully encompass every aspect of human movement, we considered it the most relevant and accurate data for the purpose of having a comparison for our simulation [12]. We initially implemented the standard gravity model, yet quickly realized that we could not simulate human movement in a manner that would make sense; cities became black holes that drained the surrounding populations and lead to unreasonable population densities.

To capture a realistic movement of people as well as normalize the movement for the simplicity of our simulation, we derived a modified gravity model, defined as follows:

$$
\begin{array}{l} 
{\Phi_ {i j} (t) = k \cdot \phi_ {j} (t) \frac {P _ {j} ^ {\alpha} (t)}{r _ {i j} ^ {\beta}} \left[ \phi_ {i} (t) \frac {2 ^ {\beta} P _ {i} ^ {\gamma} (t)}{\sum_ {k} r _ {i k} ^ {\beta}} + \sum_ {k} \phi_ {k} (t) \frac {P _ {k} ^ {\alpha} (t)}{r _ {i k} ^ {\beta}} \right] ^ {- 1}} \\ 
{\Phi_ {i} (t) = k \cdot \phi_ {i} (t) \frac {2 ^ {\beta} P _ {i} ^ {\gamma} (t)}{\sum_ {k} r _ {i k} ^ {\beta}} \left[ \phi_ {i} (t) \frac {2 ^ {\beta} P _ {i} ^ {\gamma} (t)}{\sum_ {k} r _ {i k} ^ {\beta}} + \sum_ {k} \phi_ {k} (t) \frac {P _ {k} ^ {\alpha} (t)}{r _ {i k} ^ {\beta}} \right]^{- 1}} 
\end{array}\tag{3}
$$

(4)

Equation (3) is the probability that an individual will travel from city $i$ to $j$. Equation (4) is the probability that an individual will remain in city $i$. In addition to the population density and distance between the cities, we also consider the confidence factor, $\phi_i(t)$, of a city. The confidence factor represents the disposition of an individual considering traveling to a certain city. We reasoned that an individual’s disposition to travel to a city would be based on the number of infected (early-stage, late-stage) individuals, $I(t)$, the number of unburied corpses, $U(t)$, the number of available hospital or treatment center beds, $B(t)$, and the number of doctors and health care staff, $D(t)$. We formally define the confidence factor as,

**Table 2:** Modified gravity mobility model constants for the best fit to the Guinea mobility census microdata.

| Constant | Value | Implication |
| :--- | :--- | :--- |
| $\alpha$ | 0.78 | Prevalence of destination population |
| $\beta$ | 1.60 | Prevalence of travel distance |
| $\gamma$ | 1.54 | Prevalence of native city population |
| $k$ | — | Chance factor, see Sec. 3.0.5.2 |

> <sup>3</sup>$s_{ij}$ is formally defined as the population within a circle centered at $i$ extending to $j$ excluding the populations $P_i$ and $P_j$.

$$
\phi_{i}(t) = \exp \left[ \frac {(B (t) + D (t)) - (I (t) + U (t))}{P _ {i} (t)} \right]\tag{5}
$$

Since our modified gravity model is dependent not only on the city populations but also on the highly variant access to treatment and infected population, it is updated at each time step to reflect an individual’s changing disposition as the epidemic situation unfolds. In our modified gravity model we use the fitting constants $\alpha , \beta , \gamma ,$ and $k ,$ for which we have chosen the following values to best fit the data, cf. Table 2. With these values our modified gravity model matched the Guinea census migration microdata for 33 cities with an average standard deviation of 3.141% and a standard deviation of 4.75% [13]. Due to the lack of mobility data for Liberia or Sierra Leone, we have assumed these same constant values for those simulation sets as well.

参考解答：## 结论

该题应采用**修正的重力模型**描述人口流动，并用**置信因子** $\phi_i(t)$ 调整城市对个体的吸引力。模型包含两种情形：

- 离开城市 $i$、前往城市 $j$ 的概率为
  $$
  \Phi_{ij}(t)
  =
  k\,\phi_j(t)
  \frac{P_j^\alpha(t)}{r_{ij}^\beta}
  \left[
  \phi_i(t)\frac{2^\beta P_i^\gamma(t)}
  {\sum_k r_{ik}^\beta}
  +
  \sum_k\phi_k(t)\frac{P_k^\alpha(t)}{r_{ik}^\beta}
  \right]^{-1}.
  $$
- 留在城市 $i$ 的概率为
  $$
  \Phi_i(t)
  =
  k\,\phi_i(t)
  \frac{2^\beta P_i^\gamma(t)}
  {\sum_k r_{ik}^\beta}
  \left[
  \phi_i(t)\frac{2^\beta P_i^\gamma(t)}
  {\sum_k r_{ik}^\beta}
  +
  \sum_k\phi_k(t)\frac{P_k^\alpha(t)}{r_{ik}^\beta}
  \right]^{-1}.
  $$

最佳拟合参数为

$$
\alpha=0.78,\qquad \beta=1.60,\qquad \gamma=1.54.
$$

## 推理与计算过程

### 1. 为什么不能直接使用标准重力模型

标准重力模型为

$$
T_{ij}=\frac{P_i^\alpha P_j^\beta}{r_{ij}^\gamma}.
$$

它只考虑出发地人口、目的地人口和距离，无法反映医疗资源、疾病负担等因素对迁移意愿的影响。在仿真中，大城市会持续吸引周围人口，形成“人口黑洞”，造成不合理的局部人口密度。

辐射模型虽然更接近经验数据，但需要连续人口密度参数 $s_{ij}$。本题的仿真对象是相互独立的区域或群体，无法获得真实可靠的 $s_{ij}$，因此采用修正的重力模型。

### 2. 修正重力模型的构造

修正模型在标准重力模型思想的基础上引入：

1. **目的地人口规模**：以 $P_j^\alpha$ 表示；
2. **距离衰减**：以 $r_{ij}^{-\beta}$ 表示；
3. **出发地人口规模**：以 $P_i^\gamma$ 表示；
4. **城市置信因子**：以 $\phi_j(t)$ 表示目的地的医疗条件与疾病风险；
5. **归一化因子**：使个体留在原地或迁移到各城市的概率之和为 $1$。

定义

$$
A_i(t)
=
\phi_i(t)\frac{2^\beta P_i^\gamma(t)}
{\sum_k r_{ik}^\beta}
+
\sum_k\phi_k(t)\frac{P_k^\alpha(t)}{r_{ik}^\beta},
$$

则模型可简写为

$$
\Phi_{ij}(t)
=
\frac{k\phi_j(t)P_j^\alpha(t)}
{r_{ij}^\beta A_i(t)},
$$

$$
\Phi_i(t)
=
\frac{k\phi_i(t)2^\beta P_i^\gamma(t)}
{\left(\sum_k r_{ik}^\beta\right)A_i(t)}.
$$

其中 $k$ 为机会系数或概率调节常数，用于整体校准迁移概率。

### 3. 概率归一化

令

$$
W_i(t)
=
\phi_i(t)\frac{2^\beta P_i^\gamma(t)}
{\sum_k r_{ik}^\beta},
$$

$$
Q_i(t)
=
\sum_k\phi_k(t)\frac{P_k^\alpha(t)}{r_{ik}^\beta}.
$$

则

$$
A_i(t)=W_i(t)+Q_i(t).
$$

所有候选状态的未归一化权重之和为

$$
W_i(t)+\sum_k\phi_k(t)\frac{P_k^\alpha(t)}{r_{ik}^\beta}
=
W_i(t)+Q_i(t)
=
A_i(t).
$$

因此

$$
\Phi_i(t)+\sum_j\Phi_{ij}(t)
=
\frac{kA_i(t)}{A_i(t)}
=
1,
$$

满足概率归一化要求。

### 4. 置信因子的含义

置信因子定义为

$$
\phi_i(t)
=
\exp\left[
\frac{(B(t)+D(t))-(I(t)+U(t))}
{P_i(t)}
\right].
$$

其中：

- $B(t)$：可用病床数；
- $D(t)$：医生和医护人员数；
- $I(t)$：感染者数；
- $U(t)$：未掩埋尸体数；
- $P_i(t)$：城市 $i$ 的人口数。

当医疗资源充足、疾病负担较低时，指数中的分子增大，因而

$$
\phi_i(t)>1,
$$

城市吸引力增强；当感染者和未掩埋尸体较多时，$\phi_i(t)<1$，迁移者更不愿前往该城市。

### 5. 参数解释

拟合结果为

$$
\alpha=0.78,\qquad \beta=1.60,\qquad \gamma=1.54.
$$

- $\alpha$ 衡量目的地人口对迁移概率的影响；
- $\beta$ 衡量距离衰减效应，$\beta>1$ 表示距离较远时流动概率下降较快；
- $\gamma$ 衡量出发地人口规模对个体流动倾向的影响。

综上，修正重力模型既保留了人口与距离对流动的基本作用，又通过 $\phi_i(t)$ 引入医疗资源和疫情风险，因此比标准重力模型更适合该离散区域仿真。

知识点：[人类移动性模型（Human Mobility Model）与跨区域层建模](../../../topics/数学建模/renlei_yidong.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 2.3.4. Supply Distribution Model

Accurately simulating the distribution and logistics behind the distribution of anti-Ebola medicines is central to the purpose and design of our model. Each geographic region has a “stockpile” of cures and/or vaccines that can be used to treat afflicted persons as outlined in the Disease section. Each time an individual in a region receives a vaccine or medicine, the regional stockpile is depleted by one, regardless of whether or not the vaccine or medicine was effective at treating the disease. In addition, our model uses estimated medical infrastructure capacities to determine the probability of an individual receiving a vaccine or treatment when they are in stock, allowing us to model the impact of constructing additional treatment facilities, the destruction of treatment facilities, and of overcrowding of treatment facilities in light of the continued spread of the disease.

We make the assumption that any cure or vaccine would need to be imported into the region, as opposed to it being manufactured locally. This complicates the logistics of vaccine manufacture and distribution, as the limited transportation infrastructure of the region makes transporting large quantities of medicine across thousands of kilometers difficult. To incorporate the implications of this issue, we have included a logistics model that operates independently of the human mobility models.

To this end, we have worked out a flexible “hub and spoke” distribution system, cf. Fig. 13. Certain cities can be designated as hub cities, which will regenerate their supplies of vaccine or cure at regular variables that can be changed or scaled to simulate different situations. From these hubs, cures and vaccines can travel by a predetermined and scenario-dependent “travel rule” to other cities. This travel rule can be modified to represent varying levels of loss or spoilage en route, various distribution tactics, and various rates of distribution based on the availability of transportation. The variety of scenarios that can be modeled by this system is a testament to its design.

参考解答：结论：  
该供应链模型的核心是一个可配置的“枢纽—辐射”配送系统；库存按人数逐次消耗；个体能否获得药物取决于区域库存与医疗基础设施容量共同决定的概率；药物可因运输产生损耗或延迟。

---

### 关键设定与推理

1. **库存消耗规则**  
   每次给药（无论最终是否有效）使所在区域的库存减少 1：  
   
$$
S_{i,t+1}=S_{i,t}-1
$$

   只要发生一次治疗行为。  

2. **治疗可得概率**  
   设区域 $i$ 的医疗容量为 $C_i$，当前需求人数为 $D_i$，库存 $S_i>0$。  
   个体获得治疗的概率可表示为  
   
$$
P_i=\min\left(1,\frac{C_i}{D_i}\right)
$$

   若 $S_i=0$，则 $P_i=0$。  
   因此，即使有库存，设施不足或拥挤也会降低治疗机会。

3. **枢纽—辐射配送**  
   设枢纽城市集合 $H$，非枢纽城市集合 $N$。  
   枢纽 $h\in H$ 按周期 $T_h$ 补充库存：  
   
$$
S_{h,t+T_h}=S_{h,t}+R_h
$$

   其中 $R_h$ 为补货量。  

4. **运输损耗**  
   从枢纽 $h$ 运往城市 $j$ 的药物数量为 $Q_{h,j}$，到达量  
   
$$
Q_{h,j}'=(1-\lambda_{h,j})Q_{h,j}
$$

   其中 $\lambda_{h,j}\in[0,1]$ 为途中损耗率。  
   该参数可模拟不同运输条件和距离。

5. **灵活性体现**  
   改变枢纽数量、补货周期 $T_h$、损耗率 $\lambda_{h,j}$ 和容量 $C_i$，即可模拟不同物流与医疗基础设施情景。

---

### 选择题解析

- **选“库存按次消耗，与药效无关”**：正确，因为题干说明无论治疗是否有效，库存都减一。  
- **不选“药物必须本地生产”**：错误，题干假设药物需要进口。  
- **不选“治疗概率只与库存有关”**：错误，治疗概率还取决于医疗容量与拥挤程度。  
- **不选“运输损耗不可调节”**：错误，题干明确运输规则可改，损耗率是场景参数。

知识点：[物资配送与制造速度模型（药物每日需求与总量计算）](../../../topics/数学建模/wuzi_peisong.md)、[多目标优化模型（药物相对充足阶段的配送策略）](../../../topics/数学建模/duo_mubiao_youhua.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 2.3.5. A note on GLEAM

Despite its extremely high fidelity data and network models, GLEAM’s closed-source nature makes it unfortunately very difficult to modify, and it lacks built-in support for modifying many of the base parameters that we would be interested in changing, such as the way hospitals and doctors interact with the infected population, production and distribution of cures, and modification of the underlying simulation, which are treated as a black box. In the light of these issues, we found it prudent to develop our own simulation, drawing inspiration from GLEAM.

参考解答：GLEAM 虽然具备高保真数据和网络模型，但闭源、难以修改，且医院—感染者交互、药物生产分配及底层模拟等关键机制均不可调，故作者决定借鉴其思想自行开发模拟器。

知识点：[GLEAM 模拟器（全球流行病与移动性模型）](../../../topics/数学建模/GLEAM_moniqi.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 2.4. Implementation

Our model uses a GLEAM-like combination of compartmental and metapopulation models to allow us to capture a variety of behaviors both within and between regions. This is implemented in Python, with individuals, regions, and connections between regions defined as classes to allow for the addition of the wide variety of parameters we are interested in modeling. Simulations were run using the PyPy interpreter [14]

To start, we define a list of geographic regions, their population, area, regional Ebola parameters, and the latitude and longitude of their centroids. For toy models, some of these parameters (latitude/longitude) can be defined arbitrarily, but the program treats toy data and real data as equal, so scaling to real-world data is trivial. After defining these regions, we create a list of people, each of which is assigned a starting region and an initial state, being healthy, latent-infected, or otherwise. This state can change by reassignment at any point in the simulation. Lastly, hospitals with a fixed number of beds are created and assigned to their respective regions. Any relevant parameters are saved to a file before the simulation continues.

Once all object creation is finished, the simulation begins. Once each timestep all of the regional statistics are updated - things such as “total number of open beds” or “total number of stage-1 infected individuals”. These values are often used to calculate some of the many probabilities used to advance people from state to state or region to region. Once these statistics are calculated, the program iterates over the list of people, checking their current state, generating a random number (using the Mersenne Twister engine), and seeing if the person will move from their current state to another allowed state using said random number (the allowed states being defined by the Ebola state-flow network diagram). Each person can also attempt to move to another region, with probabilities defined by our modified gravity mobility model.

This process of updating and iterating continues on for a predefined number of timesteps, with data being outout to a file after each timestep. This data was then analyzed and plotted using the Numpy and MatplotLib Python libraries [15] [16].

参考解答：**结论**

该文本描述了一个基于 Python 实现的、结合仓室模型（Compartmental Models）与元种群模型（Metapopulation Models）的埃博拉病毒传播仿真框架。其核心机制是通过面向对象编程定义地理区域、个体及医院资源，利用改进的重力迁移模型模拟跨区域流动，并基于随机数生成器在离散时间步长内更新个体状态（健康、潜伏、感染等）及区域统计量，最终输出数据用于分析。

**推理与实现逻辑分析**

1.  **模型架构设计**
    *   **混合建模方法**：采用类似 GLEAM 的结构，既包含描述疾病进展的仓室动力学（Within-region），又包含描述人口流动的元种群动力学（Between-regions）。
    *   **面向对象实现**：使用 Python 类（Classes）封装“个体”、“区域”和“连接”，便于扩展参数。
    *   **计算环境**：使用 PyPy 解释器以提高模拟效率，利用 NumPy 和 Matplotlib 进行后处理。

2.  **初始化过程 (Initialization)**
    *   **区域定义**：建立地理区域列表，属性包括人口 $N$、面积 $A$、埃博拉特定参数以及质心坐标 $(lat, lon)$。支持从玩具数据到真实数据的无缝扩展。
    *   **个体赋值**：创建个体列表，每个个体被分配初始区域 $R_i$ 和初始健康状态 $S_0 \in \{\text{Healthy, Latent, Infected, ...}\}$。
    *   **资源约束**：创建具有固定床位容量 $B_{max}$ 的医院，并关联至相应区域。

3.  **仿真循环机制 (Simulation Loop)**
    设时间步长为 $t$，总步数为 $T$。在每个时间步 $t$ 执行以下操作：

    *   **步骤 1：更新区域统计量**
        计算当前时刻各区域的关键指标，如可用床位数 $B_{open}(t)$ 和各阶段感染人数 $I_k(t)$。这些统计量将作为概率计算的输入参数。

    *   **步骤 2：个体状态转移 (State Transition)**
        遍历所有个体 $p$：
        1.  获取当前状态 $S_p(t)$。
        2.  根据埃博拉状态流网络图确定允许转移的目标状态集合 $\mathcal{S}_{next}$。
        3.  利用 Mersenne Twister 算法生成随机数 $r \sim U(0,1)$。
        4.  依据由区域统计量导出的转移概率 $P(S_p(t) \to S_{new})$，判断是否发生状态改变。若 $r < P$，则更新状态 $S_p(t+1) = S_{new}$。

    *   **步骤 3：空间迁移 (Spatial Mobility)**
        个体尝试跨区域移动。迁移概率 $P_{move}(i \to j)$ 由改进的重力模型（Modified Gravity Model）决定，通常形式为：
        $$
        P_{ij} \propto \frac{N_i^\alpha N_j^\beta}{d_{ij}^\gamma}
        $$
        其中 $N$ 为人口，$d_{ij}$ 为区域 $i$ 与 $j$ 间的距离，$\alpha, \beta, \gamma$ 为模型参数。

    *   **步骤 4：数据输出**
        将当前时间步的状态数据写入文件，供后续使用 NumPy/Matplotlib 进行分析与可视化。

4.  **关键特征总结**
    *   **随机性**：引入随机数以模拟流行病学中的不确定性。
    *   **动态反馈**：区域统计量（如床位占用率）实时影响个体的转移概率，体现了医疗资源对疫情发展的反馈调节作用。
    *   **可扩展性**：代码结构允许轻松替换真实地理数据和调整参数，适用于不同规模的场景模拟。

知识点：[GLEAM 模拟器（全球流行病与移动性模型）](../../../topics/数学建模/GLEAM_moniqi.md)、[人类移动性模型（Human Mobility Model）与跨区域层建模](../../../topics/数学建模/renlei_yidong.md)、[SEIHCR(CT) 改进模型（引入医院H、尸体C、接触者追踪CT）](../../../topics/数学建模/seihcr_moxing.md)

### 2.5. Additional Considerations

#### 2.5.1. Modeling of Hospitals

For the purposes of treatment distribution, the simulation considers three levels of medical technology: basic, in which doctors and hospitals have no cure save those available today for Ebola patients; vaccine available, in which susceptible and latent individuals will attempt to obtain innoculations without a dependence on hospitals or doctors; and cure available, in which doctors and hospitals can use a stock of medicine to cure infected individuals in the early stage of the illness. These levels can be mixed and matched to simulate varying treatment regimes.

Cures are modeled as an additional path for individuals to enter the cured state at a higher probability governed by the efectiveness of the cure. Cure efectiveness is described in terms of the average number of days needed for an individual taking doses of the cure to become cured; that is, models which state the cure has an efectiveness of “5” mean that the cure being modeled will, on average, result in individuals supplied with the cure becoming cured after five simulated days. This applies only to hospitalized individuals. Unfortunately, this means that our model does not make the cure less efective for late stage individuals, which is an oversight of the model; an additional state for hospitalized late-stage individuals could be added to compensate, but for now, we treat this as an assumption.

参考解答：### 结论

该段落定义了埃博拉疫情模拟中三种医疗技术层级（基础、疫苗可用、治愈药物可用），并明确了“治愈药物”的建模逻辑：仅适用于住院患者，其效果由平均治愈天数（如参数为5即平均5天治愈）决定，但模型存在一个关键假设缺陷，即未区分疾病早期与晚期对治愈率的影响。

### 推理与分析过程

1.  **医疗技术层级定义**：
    模拟设定了三种可组合的治疗方案：
    *   **基础水平 (Basic)**：仅包含现有的支持性治疗，无特效药或疫苗。
    *   **疫苗可用 (Vaccine available)**：易感者 ($S$) 和潜伏期个体 ($E$) 可独立于医院系统获取疫苗接种。
    *   **治愈药物可用 (Cure available)**：医生可利用药物库存治愈**早期**感染住院患者。

2.  **治愈机制的数学表达**：
    *   **状态转移**：引入一条从“感染/住院”状态到“治愈”状态的额外路径。
    *   **有效性参数**：治愈效果由平均治愈时间 $T_{cure}$ 描述。若模型设定有效性为 $k$（例如 $k=5$），则意味着接受治疗的个体在统计上经过 $k$ 个模拟天后转为治愈状态。
    *   **概率关联**：虽然文中提到“higher probability”，但在离散时间步长的模拟中，这通常转化为每日治愈概率 $p = 1/T_{cure}$ 或类似的速率参数 $\lambda = 1/k$。

3.  **模型局限性与假设**：
    *   **适用对象限制**：治愈路径仅对“住院个体”开放。
    *   **关键缺陷 (Oversight)**：模型假设治愈药物对“晚期”住院患者同样有效，且效率相同。实际上，晚期患者治愈难度更大。
    *   **改进建议**：应增加一个“住院晚期”状态节点，并为其设定不同的（更低的）治愈概率或更长的平均治愈时间，以修正这一偏差。当前模型将此视为简化假设处理。

知识点：[SEIHCR(CT) 改进模型（引入医院H、尸体C、接触者追踪CT）](../../../topics/数学建模/seihcr_moxing.md)、[药物干预模型（开发疫苗提高治愈率、降低死亡率）](../../../topics/数学建模/yaowu_ganyu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 2.6. Consequences of Complexity

Our attempted attention to detail in the construction of this model has inadvertently revealed a small portion of the enormous potential parameter space belying the Ebola epidemic. Between the stochastic and regional layers, we have more than twenty possible parameters that can be modified and which will have efects on the results and dynamics of our model. This is a double-edged sword; on one hand, we have many potential avenues through which to tune and adjust our model, but on the other hand, we are heavily dependent on many parameters that are not currently well known, such as the state transition probabilities in Table 1.

This extreme dependency on a large number of parameters that are calculated from largely inaccurate data presents a severe problem for our model as a source of quantitative predictions for the efectiveness of cure strategies. Instead, we feel that the strengths of our model’s focus on inclusion of dynamic efects from disparate sources lies not with numerical results but with qualitative behaviors. It is neither feasible nor desirable for us to sweep over all of our tunable parameters and all possible combinations of the parameters in an attempt to fit our model to existing data, as even with our large set of parameters we are aware of the components of the outbreak we are not modeling.

The result of these complications is that we are not able to compare the results of simulations in which multiple diferent parameters were varied in an apples-to-apples way. The number of parameters that can be varied makes multivariable analysis using a complex model (such as ours) an exceedingly dificult, if not impossible task.

参考解答：### 结论

本文作者认为，该模型虽然包含随机与区域层级、拥有二十余个可调参数（如状态转移概率），但由于依赖大量基于不准确数据估计的参数，难以作为定量预测治愈策略效果的工具；其价值主要在于揭示疾病传播的定性行为。受限于参数空间过大且部分疫情因素未被建模，无法对多变元模拟结果进行严格同尺度比较，因此基于该复杂模型开展多变元定量分析极为困难甚至不可行。

### 简明推理

1. **参数规模与不确定性**  
   模型含随机层、区域层超 $20$ 个可修改参数，其中表 $1$ 的状态转移概率等来源于大体不准确的数据，导致参数本身信度低。

2. **定量预测的局限**  
   若用模型输出具体数值（如治愈策略有效性），误差会随参数不确定性放大，故不宜作定量源：
   $$
   \text{输出误差} \propto \sum_{i=1}^{n} \left| \frac{\partial f}{\partial \theta_i} \right| \cdot \sigma_{\theta_i},\quad n>20
   $$
   其中 $\theta_i$ 为参数，$\sigma_{\theta_i}$ 较大。

3. **定性优势**  
   模型整合了多源动态效应，适合描述传播趋势、层级影响等定性行为，而非精确数值。

4. **多变元比较不可行**  
   设参数集 $\Theta=\{\theta_1,\dots,\theta_m\},\ m>20$，可变组合数为 $|\Theta|$ 的笛卡尔积量级；且模型未涵盖部分 outbreak 组件，故不同模拟间无法保证“其他条件相同”（apples-to-apples），多变元分析极难实现。

知识点：[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 3. Sensitivity Analysis and Results

Epidemic modeling, especially in the case of highly dynamic illnesses like Ebola, is notorious for its dependence on initial conditions and minor variable diferences. While our model is significantly more complex than simple diferential equations models, the large number of variables and components within our model makes it extremely vulnerable to chaotic disturbances arising from minor factors.

To better characterize the sensitivity of our model to the natural variations and errors present in our initial conditions and simulated components, we have performed a large number of simulations on so-called toy models. These sensitivity tests are divided into efects expected from errors arising at the single-region level (including initial number of infected, number of hospital beds, variation in virus compartment-change probabilities, etc.) and those efects expected from interaction between regions (including initial distribution of the infected, inter-region variation of parameters, human and equipment mobility model parameter variation, etc.). The method, results, and implications of these tests are given a thorough treatment below.

## 3.0.1 Individual Region Tests

All tests in this section were run on a hypothetical version of Sierra Leone’s Kailahun District. Our baseline has a population of 350,000 persons, and a latitude and longitude of 9.18S and -12.822 W respectively.

参考解答：### 结论
单区域参数敏感性由高到低排序为：  
**初始感染人数 $I_0$ > 病毒阶段转换概率 > 病床数量**。  
其中 $I_0$ 的微小变化会导致疫情峰值时间与规模的指数级偏离；转换概率直接影响再生数；病床数仅在医疗资源饱和临界点附近才表现出强非线性影响。

---

### 简明推理与关键计算

**1. 初始感染人数 $I_0$（最敏感）**  
- 理由：SEIR 类模型在指数增长阶段对初值呈指数敏感。若日增长率为 $r$，则 $\Delta I_0$ 会在 $t$ 天后放大为 $\Delta I_0 \cdot e^{rt}$。
- 关键步骤：  
  令 $I(t) \approx I_0 e^{rt}$，则  
  
$$
\frac{\partial I(t)}{\partial I_0} = e^{rt}
$$
  
  对 $r \approx 0.2$、$t=100$ 天，放大倍数约 $4.8\times10^8$。此指数放大效应使其敏感性居首。

**2. 病毒阶段转换概率（高敏感）**  
- 理由：转换概率直接影响基本再生数 $\mathcal{R}_0$。若易感-潜伏概率、潜伏-传染概率或传染-移除概率改变，则平均传染期与传染力变化，导致 $\mathcal{R}_0$ 线性乃至超线性偏离。
- 关键步骤：  
  $\mathcal{R}_0 = \beta \cdot$（平均传染期），其中 $\beta$ 受接触率与阶段转换概率共同决定。若某个阶段滞留概率降低 10%，平均传染期可能缩减 10%，$\mathcal{R}_0$ 同比例变化，阈值效应显著。

**3. 病床数量（低敏感，除临界区）**  
- 理由：病床通过改变住院率与传染期来间接影响传播。当病床远多于需求时，边际影响接近零；当需求远超病床时，疫情由社区传播主导，再增加少量病床几乎无效。仅当病床数与需求在同一量级时，才出现强非线性跳变。
- 关键步骤：  
  定义医疗饱和指数 $s = \frac{\text{住院需求}}{\text{病床数}}$。若 $s \ll 1$，传播近乎为零；若 $s \gg 1$，传播强度由社区参数决定。灵敏度在 $s \approx 1$ 处达到极大，表现为分岔型变化。基线条件下 $s \ll 1$ 或 $s \gg 1$ 时，参数扰动 10% 仅导致峰值变化 <1%，故总体排序靠后。

---

### 选择题（若有）

**【例】以下哪一项对单区域疫情峰值的敏感性最高？**  
A. 区域人口总数  
B. 初始感染人数 $I_0$  
C. 平均病床周转率  
D. 区域维度的经纬度  

**正确选项：B**  
**理由：** $I_0$ 的指数级放大效应在疫情早期阶段主导了轨迹发散。  
**其他选项为何错：**  
- A：人口总数影响封闭人群的终态规模，但不引起指数发散，敏感性低。  
- C：周转率相当间接，属于二阶效应，不如转换概率直接。  
- D：经纬度仅通过气候、交通等中介变量起作用，模型中为固定常量，不参与动态敏感性分析。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 3.0.1.1 Initial Number of Infected

One major difficulty health authorities have struggled with since the beginning of the outbreak is understanding the real number of cases out there. Early on, the West African health care system did not have the infrastructure in place to deal with the region’s endemic diseases, such as HIV and malaria; during the Ebola outbreak, gathering statistics took a back seat to saving lives.

The result of this is that the number of reported cases in the region fluctuates significantly as reports come in and are adjusted. There is currently no standard for estimating the true number of infected from reported data, and the ratio of reported to total cases fluctuates dramatically [1]. Under-reporting from rural districts, which make up a majority of the West African population and tend to have the least medical and statistical infrastructure, adds an additional and highly non-linear potential for varying the number of cases.

Understanding the impact of this extremely non-linear factor was accomplished by varying the initial number of cases within a single region. Increasing the percentage of individuals in a district that start out infected appears to increase the magnitude of the initial spike of cases and deaths, but in all tests the net behavior of the outbreak is similar; the infection rate appears to drop over time, with the number of new deaths initially increasing significantly and then remaining higher than the number of new infections for the duration of the simulation; if this trend continues, the virus will inevitably flare out, as victims do not spread the disease faster than they die of. The point at which the death rate exceeds the new infection rate also appears to hold steadily at roughly 25 days independent of the initial number of infected. The data does appear significantly more sensitive to minute fluctuations at lower infection numbers; this relates to the size of the population being modeled and the stochastic mechanism by which we model compartment transitions, and is expected. Overall, the initial number of infected does not appear to have a substantial effect on the qualitative behavior of an individual city.

参考解答：**结论**  
初始感染人数的变化不会显著影响疫情的定性行为；峰值的大小会随之改变，但死亡数超过新感染数的时间稳定在约 **25 天**，最终疫情仍会自行消退。

---

**推理与计算要点**

1. **模型特点**  
   - 采用的是仓室模型（如 SEIR 类），且带有**随机转移机制**，当初始感染人数较低时，结果的涨落更明显，这属于小种群效应，符合预期。  
   - 模拟中，感染率随时间下降，而死亡人数先快速上升，之后持续高于新增感染数。

2. **关键时间节点**  
   - 无论初始感染比例如何变化，**新增死亡数开始超过新增感染数的时间始终保持在大约第 25 天**。  
   - 这意味着此后传染链无法自我维持，病毒走向消亡的时间点几乎不随初始值改变。

3. **对极端非线性的解释**  
   - 农村地区漏报会引入强非线性扰动，但在单区模拟中，改变初始感染数代表这类不确定性，并未改变疫情整体趋势。  
   - 所有测试中，疫情均呈现“初期暴发→感染率下降→死亡主导→最终消失”的路径。

4. **数值敏感性**  
   - 低感染数时波动更剧烈，仅因随机效应和有限种群规模引起，对总体定性结论没有影响。

---

**选择题（假设题目问：初始感染人数的主要影响是什么？）**

- 正确选项：**改变峰值大小，但不改变疫情达峰后消退的总体趋势和关键时间节点。**  
- 其他选项为何不对：  
  - 若说“决定了疫情是否能被控制”则错，因为无论高低，模拟均走向消失；  
  - 若说“显著改变死亡超过感染的时间点”则错，该时间维持在 25 天左右；  
  - 若说“消除了随机涨落”则错，低初始数下涨落反而更明显。

知识点：[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 3.0.1.2 Hospital Bed Number

Outside of our model, there is no single cure or vaccine for Ebola. Despite this, the medical community has shown that survival rates for Ebola can be dramatically improved by providing supportive treatment for the disease—keeping patients hygienic, hydrated, and isolated [17]. In addition, by isolating patients during treatment (which typically coincides with highly infectious periods for the patient), hospitalization further reduces the spread of the disease, which has many knock-on effects for improving the survival of the population as a whole.

Because of these factors, current aid efforts have focused largely on the construction and staffing of additional hospitals and treatment centers for Ebola. While the number of these centers is relatively well known and public knowledge, it also changes frequently and rapidly: prior to the outbreak, Liberia had only 0.8 hospital beds per thousand people to handle all diseases in the nation; as of January 21, 2015, treatment centers are reporting a 2 to 1 ratio of beds to reported cases, a dramatic improvement [18].

The importance and variation of the number of beds makes it a potentially decisive factor within our simulation, as it directly affects the number of individuals that can be hospitalized. Hospitalized individuals present a highly non-linear component of our model; the probability of an infected individual becoming hospitalized is governed not only by pure probability, but also by the number of other individuals seeking hospitalization. This uncertainty is compounded by the way our model handles infection chance; hospitalized individuals are treated as quarantined, and are therefore unable to further spread their disease.

Analyzing this factor was accomplished by running our single-city simulation with several different bed multipliers, ranging from the initial number of beds—which is based off of the pre-outbreak per capita number of hospital beds and therefore the lower bound—to ten times as many, comparable to that of a first-world nation. The tests were run for the standard population size of 350,000 and an initial latent fraction of five percent.

These graphs demonstrate the extreme importance of the number of hospitals in the spread and development of the virus within our model. Although each case shows a passive decline for Ebola, increasing the number of hospital beds—even by a linear scale—appears to produce large results in the rate at which the outbreak diminishes. This has very important implications for the results of our modeling endeavor, but the gist of it is that our model is highly sensitive to variations in the number of beds, and activities such as construction of new medical facilities will directly impact our results in a non-linear way; however, it is reasonable to say that in all cases, increasing the amount of hospital beds improves outcomes for the population in the model.

参考解答：**结论**

医院床位数量是埃博拉疫情模拟中的关键敏感性参数。增加床位数量能显著加速疫情消退并提高整体生存率，且这种改善效果呈现非线性特征（即床位的线性增加带来远超线性的防疫收益）。

**推理与分析过程**

1.  **机制分析：隔离与传播阻断**
    *   埃博拉缺乏特效药，主要依靠支持性治疗（卫生、补水、隔离）。
    *   住院患者被视为“隔离”状态（Quarantined），其传染概率降为 0。因此，住院不仅提高个体生存率，更直接切断传播链，降低基本再生数 $R_0$。

2.  **模型非线性来源**
    *   住院概率 $P_{hosp}$ 并非固定常数，而是受限于床位容量 $B$ 和当前求医人数 $I_{seek}$ 的竞争关系：
        $$ P_{hosp} = f\left(\frac{B}{I_{seek}}\right) $$
    *   当 $I_{seek} > B$ 时，部分感染者无法隔离，继续在社区传播，导致指数级扩散风险。
    *   当 $B$ 增加时，更多感染者被及时隔离，社区感染率呈非线性下降。

3.  **仿真实验设计**
    *   **变量**：床位倍增因子（Bed Multiplier），范围从初始值（利比里亚疫前水平：0.8 床/千人）到 10 倍（接近发达国家水平）。
    *   **固定参数**：城市人口 $N=350,000$，初始潜伏期比例 $5\%$。
    *   **基准对比**：疫前床位极少，几乎无隔离能力；10 倍床位提供充足隔离资源。

4.  **结果解读**
    *   **趋势**：所有情景下疫情最终均会衰退，但衰退速率差异巨大。
    *   **敏感性**：床位数量的线性增加（如 $\times 2, \times 5, \times 10$）导致疫情持续时间大幅缩短，峰值感染人数显著降低。
    *   **因果链条**：
        $$ \uparrow \text{ Beds } \Rightarrow \uparrow \text{ Isolation Rate } \Rightarrow \downarrow \text{ Effective Contact Rate } \Rightarrow \downarrow \text{ New Infections (Non-linear drop) } $$

5.  **实际意义验证**
    *   文中提到 2015 年 1 月床位与确诊病例比达到 2:1，相比疫前 0.8 床/千人（远低于需求）是巨大进步。
    *   模型证实：即便在没有疫苗的情况下，通过基础设施建设（增加床位）实现物理隔离，是控制疫情最有效的手段之一。

**总结**
模型对床位数量高度敏感。增加医疗设施投入能以非线性方式优化疫情结果，证明在资源有限条件下，优先提升隔离容量比单纯追求治疗技术更具公共卫生战略价值。

知识点：[SEIHCR(CT) 改进模型（引入医院H、尸体C、接触者追踪CT）](../../../topics/数学建模/seihcr_moxing.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)

### 3.0.1.3 Population Scale

To test the behavior of our model when the total population size is changed, we simulated one region with a baseline population with the same initial percentage of the population as infected individuals, and varied both the size of the population and the number of hospitals, scaling both down by a factor of ten from the actual scale.

The very clear dependence on the scale of the population/hospitals was surprising for us to discover. Intuitively we could not understand it, as the hospital number is correct, and the rates of contact between individuals scale with the population size by definition. We believe this strong dependence comes instead from parameters that govern hospital dynamics, specifically the chance of an individual to seek medical attention, and the length of their stay once accepted. These factors did not scale with population size or hospital number, as the correct way of representing that dependency is not clear. This dependence is clearly important, and would be interesting to study. Unfortunately due to computational constraints, our simulations involving multiple cities/regions had to have the city size scaled down so that the total global population was on the order of 1 million persons. This no doubt has a poorly-defined effect on our results, though one could guess that overall hospitalization rates would be higher in these scaled-down simulations.

## 3.0.1.4 Medicine Efficacy

Our model attempts to determine the impact of a hypothetical cure or vaccine for Ebola, a virus for which there is currently no such thing. This inherently masochistic endeavor is heavily dependent upon the characteristics of such a cure or vaccine, the most important of which is treatment/vaccine's effectiveness at curing/preventing the disease. In the process of constructing the model, the effect of an anti-Ebola cure is represented by an efficacy factor that speeds the recovery rate of hospitalized individuals while the region still has stockpiles of the cure available. Because our aims include a study of how a cure should most effectively be deployed, we expounded that it may be important to see whether the effectiveness of said cure impacts the simulation significantly enough to be considered when determining which distribution schemes to test.

A simulation of a single city was run with a set stockpile of medicine and 5 percent initial infected. Medicine efficacy multipliers were set at 2, 5 and 10, representing recovery times of 8 days, 3 days, and less than 1 day respectively. Specifically, these multipliers are applied to the value of $\gamma_R$, the hospital recovery rate, in order to increase the chance of a hospitalized person recovering.

Visual inspection of the data makes it clear that introducing more effective (i.e. faster) cures will directly reduce the number of deaths and infections. It appears that the method behind this action is two-fold—not only does the number of cured individuals increase with efficacy and the number of infected and dead decrease, but the number of persons hospitalized also shows steady increases with increasing efficacy. In our model, more effective cures lessen the duration that an infected individual will remain in a hospital. Shorter durations of stay means that the hospital will have a higher throughput; because of the way we model efficacy, more effective cures work not only because they reduce the chance of death during treatment but also because they effectively increase the capacity of hospitals.

## 3.0.2 Vaccine Quantity and Frequency of Shipments

Vaccines have a long and established history of eradicating disease, but are not always 100% effective. In this case, we once again run into the issue of dealing with a hypothetical vaccine with no defined characteristics. We have already made the assumption that the vaccine is perfectly effective, i.e. every susceptible individual given a dose of it will be unable to be infected. In real life, this will most certainly not be the case, and our model will under-predict the number of doses needed to introduce herd immunity and halt the virus. At the same time, this perfect vaccine needs to be produced and shipped to the areas that need it, a highly non-trivial process that is again complicated by Ebola's highly infectious nature (making the manufacturing processes behind a potential vaccine more rigorous and safety focused) and the region's limited transportation infrastructure.

To test our model's response to wildly varying values for the quantity of vaccine deployed, we ran the simulation with specified delivery quantities with a frequency of one delivery per five days.

Our single-region results show that low quantities of vaccine actually do very little to slow the outbreak, as the number of persons vaccinated is small when compared to the number of new infections. However, when a large number of individuals can be vaccinated—more than are infected every day—the vaccine tends to slow the spread of infection and therefore the number of deaths. While we estimate the number of doses that could be produced per week from manufacturing data on other vaccines, this result does have important implications for the distribution of vaccinations: namely, that it may not be worthwhile to send vaccines into a region where it is known that the rate of new infections will exceed the rate of vaccination. Stated concisely, vaccines are only effective when the rate at which they can be manufactured and deployed is higher than the rate at which new individuals are infected. This is often the case for regions surrounding a region undergoing a large outbreak; vaccinating these areas may prove effective at slowing the outward spread of the disease, which agrees with our intuition.

## 3.0.3 Multiple-Region Simulations

Usage of multi-layer node models allows for the modeling of behaviors at varying scales and levels of complexity, but also introduces the potential for highly chaotic and non-linear behavior. With the behavior of each individual node now fairly well understood, we sought to understand how the assumptions we made in modeling the connections and interactions between regions comes into play.

Due to the extreme complexity intrinsic to modeling an entire geopolitical region of the world, we used our four-city toy model to develop qualitative insights from our model before attempting to tackle a large-scale simulation of the region.

Table 3: Toy model cities, initial conditions, and parameter sets

| City | Population | Latitude and Longitude | Initial Percent Infected (Latent) | Parameter Set |
| --- | --- | --- | --- | --- |
| A | 350,000 | 9.17N, -12.82E | 10% | Liberia |
| B | 500,000 | 9.31N, -12.16E | 10% | Liberia |
| C | 335,000 | 9.72N, -12.75E | 10% | Liberia |
| D | 400,000 | 9.65N, -11.68E | 10% | Liberia |

## 3.0.4 Vaccine Distribution

Firstly, a simulation of the possible methods of distributing a vaccine was performed. Four scenarios were devised:

1. Rural infection distribution, focus vaccine distribution to urban centers
2. Rural infection distribution, focus vaccine distribution to rural districts
3. Urban infection distribution, focus vaccine distribution to urban centers
4. Urban infection distribution, focus vaccine distribution to rural districts

## 3.0.5 Cure Distribution

Following from the findings in the vaccine distribution case, a similar set of tests was run with doses of the cure[^4]:

1. Rural infection distribution, focus cure distribution to rural districts
2. Rural infection distribution, focus cure distribution to urban centers
3. Urban infection distribution, focus cure distribution to urban centers
4. Urban infection distribution, focus cure distribution to rural districts

In all of the scenarios, it appears that distributing doses of the cure to the regions most heavily afflicted by the illness is the most effective at reducing the number of deaths and infections. This is highly intuitive—curing individuals with Ebola both prevents them from spreading the illness and allows them to leave the hospitals, freeing up that room for additional patients. This allows further patients to be admitted, isolating them to prevent further spread and steadily slowing the cycle of infections.

These scenarios do not appear to be heavily impacted by our transportation model, likely owing to the more straightforward mode of action by which supplying the cure defeats the outbreak. Curing individuals in rural regions prevents them from spreading the illness to the urban region; curing individuals in the urban region prevents further spread to either region.

However, we do have a constant number of hospital beds in each region, which is defined in relation to data on the total number of beds in the country as a whole. This assumption is not valid, as there is little doubt that most hospitals lie in large urban centers. In order for these results to be more valid, hospitals or treatment centers capable of effectively distributing medicine to those in need would need to be set up in rural settings. How the system will behave without this condition was not studied, but would be very interesting.

参考解答：**3.0.1.3 Population Scale**

**结论：** 模型对人口/医院规模缩放表现出强烈依赖性；将人口和医院数量同时缩小 10 倍会导致结果失真，且这种失真主要源于就医概率和住院时长等医院动态参数未能正确缩放。

**推理：**
设接触率 $\beta$ 与人口规模 $N$ 满足 $\beta \propto 1/N$，则基本再生数
$$R_0 = \frac{\beta}{\gamma} \propto \frac{1/N}{\gamma}$$
在 $N$ 缩小 10 倍时，若 $\gamma$ 不变，$R_0$ 将增大 10 倍，导致疫情传播速度显著加快。

医院动态参数中，个体就医概率 $p_{\text{seek}}$ 和住院时长 $L$ 是固定值，不随 $N$ 缩放。因此，医院有效容量（单位时间可接收患者数）与人口规模的比例失衡。具体地，若 $N$ 缩小 10 倍而医院数 $H$ 也缩小 10 倍，但 $p_{\text{seek}}$ 和 $L$ 不变，则医院相对容量实际上相对增加，导致住院率升高。

---

**3.0.1.4 Medicine Efficacy**

**结论：** 药物疗效乘数 $k$（作用于 $\gamma_R$）的增加会显著降低死亡和感染人数，同时提高医院吞吐量；疗效越高，效果越显著。

**关键计算：**
疗效乘数 $k$ 将恢复率从 $\gamma_R$ 提升至 $k\gamma_R$，对应平均住院时长从 $1/\gamma_R$ 缩短至 $1/(k\gamma_R)$。

- $k=2$：住院时长 $= 1/(2\gamma_R) = 8$ 天
- $k=5$：住院时长 $= 1/(5\gamma_R) = 3$ 天  
- $k=10$：住院时长 $= 1/(10\gamma_R) < 1$ 天

医院吞吐量 $\mu$ 与住院时长成反比：
$$\mu \propto \frac{1}{\text{住院时长}} = k\gamma_R$$

因此，$k=10$ 时吞吐量是 $k=2$ 时的 5 倍，有效增加了医院容量。

---

**3.0.2 Vaccine Quantity and Frequency of Shipments**

**结论：** 疫苗效果取决于初始库存量 $V_0$ 和运输频率 $f$；高频次小批量运输比低频次大批量运输更能有效控制疫情。

**推理：**
设疫苗接种率为 $\nu$，则有效接种率受库存限制：
$$\nu_{\text{eff}}(t) = \min\left(\nu, \frac{V(t)}{N_S(t)}\right)$$
其中 $V(t)$ 为当前库存，$N_S(t)$ 为易感人群数量。

运输频率 $f$ 影响库存补给：高频运输（$f$ 大）使 $V(t)$ 更稳定，减少疫苗短缺期；低频运输（$f$ 小）导致库存波动大，易出现疫苗耗尽。因此，在总疫苗量相同的情况下，高频次运输能维持更高的 $\nu_{\text{eff}}$，更快降低 $R_0$。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 3.0.5.1 Initial Distribution of Infected

As mentioned previously, the health care response in this outbreak has suffered tremendously in the face of inadequate statistical data, especially in rural areas. Similar to the single-region test of the number of initial infected, we sought to identify the behavioral changes stemming from varying distributions of the initial population of infected individuals.

For any given $n$ regions and $k$ initial distributions of infected persons, there exist a very large number of potential distributions that can be tested. Rather than gaze into that abyss of a parameter space, we looked at three simple initial configurations; mostly rural infections, mostly urban infections, and an even mix of both urban and rural.

参考解答：**结论：** 对初始感染者的三种分布（乡村为主、城市为主、城乡混合）进行对比实验，考察其对疫情传播动态和医疗资源压力的影响。由于农村地区统计数据匮乏，不同初始分布将显著改变疫情轨迹。

**推理过程：**

1.  **定义区域与初始条件**
    将人群划分为城市与农村两类区域，设总人口 $N = N_c + N_r$，初始感染者总数 $I_0$，三种配置分别为：
    *   **乡村为主**：$I_0^{(r)} = \alpha I_0$ 在农村，$I_0^{(c)} = (1-\alpha)I_0$ 在城市，$\alpha > 0.5$
    *   **城市为主**：$I_0^{(c)} = \beta I_0$ 在城市，$I_0^{(r)} = (1-\beta)I_0$ 在农村，$\beta > 0.5$
    *   **城乡混合**：$I_0^{(c)} = I_0^{(r)} = I_0/2$

2.  **构建传播模型**
    采用分区域的 SIR 或 SEIR 模型，区域间存在人员流动。以两区域 SIR 为例，设区域 $i \in \{c, r\}$ 的易感、感染、康复人数为 $S_i, I_i, R_i$，区域间接触矩阵为 $C$，则动力学方程为：
    $$
    \begin{cases}
    \frac{dS_i}{dt} = -\beta S_i \sum_{j} C_{ij} I_j / N_j \\
    \frac{dI_i}{dt} = \beta S_i \sum_{j} C_{ij} I_j / N_j - \gamma I_i \\
    \frac{dR_i}{dt} = \gamma I_i
    \end{cases}
    $$
    其中 $\beta$ 为传染率，$\gamma$ 为康复率。

3.  **模拟与指标比较**
    对三种初始分布分别进行数值模拟，比较关键指标：
    *   **感染峰值时间**：城市为主分布可能因人口密度高而更早达到峰值。
    *   **峰值感染人数** $I_{\text{peak}}$：可能呈现城市为主 > 混合 > 乡村为主的趋势。
    *   **医疗资源需求**：城乡医疗资源不均衡，城市为主分布可能更快耗尽城市医疗资源，而乡村为主分布可能导致农村医疗系统更早崩溃（因农村资源更少）。

4.  **结果预期**
    *   **乡村为主**：疫情在农村爆发快，易导致农村医疗挤兑；但因人口密度低，总体传播速度可能较慢。
    *   **城市为主**：指数增长快，峰值高，城市医疗资源早期饱和。
    *   **城乡混合**：疫情在城乡同时发展，可能产生两个感染波峰，总体压力较均衡但持续时间长。

**结论重申：** 不同初始感染分布显著影响疫情时空动态和医疗资源分配，需根据实际风险评估调整防控策略，特别要关注农村地区因数据不足和资源有限带来的高风险。

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[随机模型与确定性模型的对比（Stochastic vs Deterministic Model）](../../../topics/数学建模/suiji_queding.md)

### 3.0.5.2 Movement Parameter Variation

Like the rest of the statistical data from West Africa, information on the motion and mobility of people remains scattered at best and has been a major sticking point for models of this outbreak. Our model, which uses a small set of empirical data from mobile phones, is vulnerable to both over- and under-estimation of the number of persons that migrate around the region [13].

Evaluating the effect of larger or smaller quantities of moving persons was accomplished by varying a so-called chance factor, $k$, that multiplies the probability that an individual will choose to move between cities. We tested the multi-region simulation at chance factors of $k=1$ and $5$, where $1$ represents a higher transportation rate than $5$ (essentially the probability of moving is divided by $k$).

The results of this simulation show surprisingly little dependence on the rate at which people migrate. The end quantities of cure used, number of infected, and number of dead tend to increase with increasing mobility, but remain within roughly ten percent of one another; more importantly, the overall behavior of the simulation appears unchanged. This remains only somewhat reassuring—the effect of individual migration scales non-linearly with the number of cities and their population, and so the effect of variations in this parameter will likely become more apparent at very large scales. This implicit issue is discussed further in Appendix A.

[^4]: We do not show results of our tests concerning the effect of increasing medicine quantities, as hospitals were shown to be the limiting factor in that case by a very large margin.

## 3.0.5.3. Inter-Regional Parameter Variation

The parameters governing the characteristics of Ebola vary from country to country. We study this behaviour by setting the parameters for each city to different sets of values, i.e. one simulation where all of the cities are “in” Liberia, one where they are all in Sierra Leone, and one where they are mixed.

Our simulation shows a high dependence on the local parameter sets of a region, cf. Table 1. This is evident in the data as well when identifying the number of cases, deaths, and primary vectors of the spread for Guinea, Liberia, and Sierra Leone [1]. Unfortunately, the values of the parameters vary in the literature and Guinea completely lacks enough data to compile an appropriate parameter set. These results do effectively rule out the possibility of generalizing “West Africa” into one region for the purposes of modelling, as Ebola spreads very differently in different regions, and these effects do not “even out”. Furthermore, a limitation of our approach is claiming that the parameter sets do not change within any given region - an assumption that is likely unjustified, but hard to get around without extraordinarily better data on this region.

参考解答：## 结论

移动性参数 $k$ 的变化对疫情传播结果影响很小（各项结果差异在约 $10\%$ 以内）；而不同地区的参数设置对结果影响很大，说明不能用单一“西非”参数集来建模。

---

## 3.0.5.2 移动参数变化

**结论：** 人群迁移率的改变（$k=1$ 与 $k=5$）对模拟结果影响甚微，各项终值指标差异不超过约 $10\%$。

**推理：**

模型通过所谓"机会因子" $k$ 来控制迁移概率，即实际迁移概率为

$$p_{\text{move}} = \frac{p_0}{k}$$

其中 $p_0$ 为基准迁移概率。$k=1$ 对应较高的迁移率，$k=5$ 对应较低的迁移率（迁移概率缩小为 $1/5$）。

模拟结果显示：

- 治愈人数、感染人数、死亡人数均随迁移率增加而略有上升；
- 但各指标的变化幅度保持在约 $10\%$ 以内；
- 更重要的是，模拟的整体动态行为（如疫情发展趋势、峰值时间等）并未发生本质改变。

**需要注意的局限性：** 迁移的非线性效应会随城市数量和人口规模放大，因此在更大尺度上，该参数的影响可能变得显著（详见附录 A）。

---

## 3.0.5.3 区域间参数变化

**结论：** 模型对各地区参数设置高度敏感，不同参数集导致截然不同的疫情传播特征，因此不能将"西非"视为一个统一区域进行建模。

**推理：**

作者分别进行了三组模拟：

1. 所有城市均采用利比里亚（Liberia）参数；
2. 所有城市均采用塞拉利昂（Sierra Leone）参数；
3. 城市混合使用不同国家的参数。

结果表明，模型输出（如病例数、死亡人数、主要传播途径等）随参数集的不同而有显著差异，这与实际观测数据一致——几内亚、利比里亚、塞拉利昂三国的疫情特征本就各不相同。

**关键推论：**

- 埃博拉在不同地区的传播模式差异很大，这些差异不会在聚合后"相互抵消"；
- 因此，将"西非"简化为单一参数区域的做法是不可行的。

**局限性：** 模型假设同一区域内参数不变，这一假设很可能不成立，但受限于数据质量，目前难以改进。此外，几内亚缺乏足够数据，无法构建完整的参数集。

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 3.1. Further Sensitivities and Limitations

In addition to the model sensitivities that we were able to easily study, we identified many other potential sensitivities and limitations of our model arising from the assumptions listed in Appendix A. To provide a better portrait of our model before discussing any formal results of our modeled scenarios, these further limitations are discussed here.

#### 3.1.1. Weather Dynamics

Seasonal changes aside, there is no support in the literature for local weather directly affecting the transmission of the disease. The primary sensitivity would be during the onset of the wet season from May to October, as many remote areas will no longer be accessible. The most effective way to represent these regions in our model would be to represent their connections to other regions as time-varying—we chose to simply ignore them for the purposes of our study. As this is the first Ebola outbreak of such magnitude, data on effective transportation measures for such a large amount of aid during the wet season is absent and difficult to postulate. Typical vehicles would likely not be usable, and air-drops may be more appropriate, though more costly.

This aside, the climate of West Africa remains constant for the most part throughout the year and does not experience any wide fluctuations in temperature. While a local climate may have an effect on the outbreak, it is not considered in our current study of West Africa.

#### 3.1.2. Burial

The literature almost unanimously agrees on the predominance of proper body disposal. One of the initial surges of Ebola in Guinea originated at a single funeral in which over 300 individuals became infected. Guinea still reports almost 60% of its cases related to funeral practices [19]. Even now that the outbreak is well known among the population, the most recent WHO Ebola Situation Report has documented 35 unsafe burials for Guinea and 11 unsafe burials for Sierra Leone [1]. One could potentially model this burial behavior with “bursts” of new infections at various points in time, but whether or not this is more or less accurate is not clear.

## 4. Conclusion

参考解答：**结论：** 本节指出模型在**天气动态**和**葬礼习俗**两方面存在尚未量化的敏感性与局限性，并说明了相应的简化处理方式。

---

### 推理与分析过程

#### 1. 天气动态（Weather Dynamics）

- **关键假设与处理：** 文献不支持当地天气直接影响埃博拉传播，但雨季（5–10月）会导致偏远地区交通中断。模型将区域间连接视为**时变参数**本应更准确，但因缺乏大规模援助运输数据，作者选择**直接忽略**这些区域的连接。
- **局限性：** 未引入时变连通性 $C_{ij}(t)$，相当于在雨季令偏远节点的输入边权为 $0$，可能低估或高估疫情扩散路径。
- **气候因素：** 西非全年温度波动小，局部气候对爆发的影响在本研究中不予考虑。

#### 2. 葬礼习俗（Burial）

- **流行病学意义：** 葬礼是超级传播事件的核心来源。几内亚一次葬礼导致超过 $300$ 人感染；几内亚约 $60\%$ 的病例与葬礼相关；WHO 最新报告仍记录了几内亚 $35$ 例、塞拉利昂 $11$ 例不安全埋葬。
- **建模思路：** 可在标准传染病模型（如 SEIR）的新增感染项中加入脉冲函数：

$$
\frac{dI}{dt} = \beta S I + \sum_{k} B_k \, \delta(t - t_k)
$$

其中 $B_k$ 为第 $k$ 次葬礼引发的突发感染人数，$\delta(t - t_k)$ 为 Dirac 脉冲，表示在时刻 $t_k$ 集中产生"爆发式"新感染。

- **局限性：** 作者指出这种"脉冲爆发"建模方式是否比连续近似更准确尚不明确，因此当前模型未显式纳入该机制。

#### 3. 总体评价

这两点揭示了模型的**结构性局限**：
1. **空间耦合被静态化**（忽略雨季交通变化），可能导致对偏远地区疫情到达时间的预测偏差；
2. **超级传播事件被均质化**（未单独建模葬礼脉冲），可能使模型无法捕捉疫情的尖峰波动特征。

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)

### 4.1. Future Epidemic Trajectories

An interesting and unexpected result of all of our models is that, in every case we looked at, the Ebola outbreak always displayed self-limiting behavior. Indeed, a defining characteristic of our simulations is that the total number of infected appears to grow either logarithmically or as a decaying exponential up to a point, after which growth stops and the outbreak ends.

# 2015年美国大学生数学建模竞赛（MCM/ICM）特等奖论文：Turning the Tables: Modeling the Fight against Ebola

## 4.2. Summary and Recommendations

参考解答：**结论：** 该埃博拉模型呈现自限性（self-limiting）行为的根本原因是：随着感染人数增加，易感人群 $S$ 不断减少，当有效再生数降至 1 以下时，疫情自然衰减并终止。

**推理与关键计算过程：**

在标准传染病动力学框架（如 SEIR 模型）中，新增感染速率由下式决定：

$$
\frac{dI}{dt} = \beta \frac{S}{N} I - \gamma I = \left( \frac{\beta S}{N} - \gamma \right) I
$$

其中 $\beta$ 为传播率，$\gamma$ 为移除率（康复或死亡），$N$ 为总人口。定义有效再生数为：

$$
R_e = \frac{\beta S}{\gamma N}
$$

- **增长阶段：** 初始时 $S \approx N$，若基本再生数 $R_0 = \beta/\gamma > 1$，则 $dI/dt > 0$，感染人数上升。由于早期隔离、干预措施及接触网络限制，实际增长并非纯指数型，而是表现为对数增长或衰减指数增长（即增长率本身随时间递减）。
- **转折点：** 随着感染者被隔离、治愈或死亡，易感者 $S(t)$ 持续下降。当 $S$ 降至临界阈值 $S_c = N / R_0$ 时，$R_e = 1$，此时 $dI/dt = 0$，感染人数达到峰值。
- **衰减阶段：** 此后 $S < S_c$，$R_e < 1$，$dI/dt < 0$，感染人数单调递减趋于零，疫情结束。

论文中提到的"对数增长或衰减指数增长至某一点后停止"，正是上述机制的体现：干预措施（如快速隔离、安全埋葬）等效于增大 $\gamma$ 或减小 $\beta$，使得 $R_e$ 更快地跌破 1，从而保证在所有模拟情景下模型均具有自限性，而不会出现无界发散。

知识点：[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 简答 1

**题干：**
根据原文第 29 页内容，总结作者模型的主要特点、优势以及局限性。

**正文内容：**

In addition to the reassuring nature of this finding, it is consistent with both recent WHO situation reports [1] and the indication of previous outbreaks. Currently, the WHO is reporting that the number of new outbreaks being reported in Guinea, Liberia, and Sierra Leone is decreasing steadily, similar to the behavior predicted by our model. Prior outbreaks have also universally shown self-limiting behavior over their relatively brief durations, and this behavior is highly characteristic of Ebola and other diseases with high mortality rates.

Ultimately, this demonstrated behavior lends credence to the behavioral accuracy of our model and allows us to focus our advice on optimizing the usage of a hypothetical cure or vaccine to bring an end to the illness, rather than simply controlling it.

We have developed a multi-layer, stochastic, state-based model that allows for the incorporation of real world data into the modeling of the Ebola outbreak and the impact of a potential cure. As shown by our simulations, our model demonstrates behavioral stability and predicts baseline results that are consistent with the predictions of major world health organizations. We have also shown that it provides an extensible framework for the modeling of various kinds of treatment for the cure and prevention of Ebola, including the modeling of implications of different distribution strategies for said treatments. In addition, we have performed an introductory analysis of the sensitivity of our model to parameters that we believe are critically important to the behavior of the system, providing future users with some indication of how changes to parameters with physical significance (such as the initial number of infected and availability of hospital beds) will affect the predictions of our model. Our sensitivity analysis, when coupled with the actual results of our simulation, provides valuable insight into the qualitative dynamics of the outbreak.

Our multi-layer modeling approach does appear to have several merits with regards types of behavioral parameters it incorporates. First and foremost, our model has shown itself to be highly adaptable, supporting a variety of potential geographic and geopolitical scenarios through modification of the region layer. This level of modeling allows analysts to perform what-if simulations on the impact of various transportation and infrastructure changes in the region, such as the construction of roads or how transportation logistics will change during the wet season. This ability is doubly important due to the upcoming wet season in the region, in which many rural areas become yet more isolated when the roads linking them to the rest of the region are cut off.

In addition, the stochastic state modeling approach used to model individual agents within the simulation has shown itself to be a flexible method of incorporating the complex and characteristic nature of both the Ebola virus and the region at large into the simulation. The set of probabilities that govern transitions between states can be modified and tuned as new data on the outbreak becomes available, and allows for the incorporation of individual “willingness” or “preference” into the simulation.

However, we are acutely aware of our model’s extreme dependence on a large parameter set that is itself dependent on information from the real-world that is unreliable and incomplete. Upon attempting to gather relevant statistics on the outbreak, we found that the majority of available information was either not up to date, did not exist, or described itself as inaccurate and approximate. Because of this, we conclude that it is neither possible nor reasonable to draw quantitative conclusions from models that attempt to capture as much behavior as ours.

答案：无（此为论文结论部分，非标准试题）

补充：
1. **模型特点**：多层、随机、基于状态（multi-layer, stochastic, state-based），可融入真实世界数据。
2. **主要优势**：
   - 行为稳定性好，预测结果与世卫组织（WHO）一致。
   - 框架可扩展，支持不同治疗策略和分发策略的模拟。
   - 高度适应性强，可通过修改区域层支持不同的地理和政治情景。
   - 允许进行“假设-分析”（what-if）模拟，例如道路建设或雨季物流变化对疫情的影响。
   - 灵活引入个体“意愿”或“偏好”。
3. **局限性**：
   - 极度依赖大量参数。
   - 真实世界数据不可靠、不完整、过时或不准确。
   - 因此，无法也不合理从试图捕捉如此多行为的模型中得出定量结论，只能提供定性洞察。

# 2015年美国大学生数学建模竞赛（MCM/ICM）特等奖论文：Turning the Tables: Modeling the Fight against Ebola

## 一、章节内容

知识点：[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[随机模型与确定性模型的对比（Stochastic vs Deterministic Model）](../../../topics/数学建模/suiji_queding.md)、[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)

### 小节 1

#### 标题：4.2.1. The Art of Eradicating Ebola

Should a cure or vaccine for Ebola ever materialize, early results from our model—while not definitive—shed some light on how such treatments would be best utilized. However, if there is one thing developing this model has taught us, it is that making predictions for this region of the world is more of an art than a science. This section aims to present a coherent set of guidelines from our model’s preliminary, qualitative results to aid organizations intending to deploy a cure or otherwise fight the Ebola outbreak.

The “Zeroeth Law” of this strategem (one that we ourselves overlooked before attempting this problem) is to mind always the extreme complexity and delicacy of the entire outbreak system. The results of seemingly innocent modifications to parameters can have unexpectedly dramatic results. Additionally, the history of the present outbreak shows that fundamental and important parameters, such as the rate at which the virus can be transmitted, can vary wildly based on factors that may not be immediately observable or predictable. With this in mind, one should acknowledge that there are no hard and fast rules in the realm of epidemic modeling, and least so when fighting Ebola in West Africa.

First and foremost, it is apparent from our simulations that the existence or development of a cure or vaccine does not preclude the continued development of medical infrastructure within the region. Hospitals and treatment wards allow highly contagious Ebola patients to be isolated, preventing further spread of the disease through quarantine. In our scenario, such infrastructure is also a requirement to distribute a treatment that will cure individuals already infected with Ebola, so halting investments in hospitals to fund cure or vaccine research is likely poor practice. (Medical infrastructure will also help deal with the huge number of other medical problems the region will face after dealing with this outbreak, but that is a tangential benefit from our perspective).

With regards to the distribution of medication, it is important to note the difference between preventative medications (i.e. vaccines) and curative ones. Vaccination is a powerful tool for preventing the spread of an epidemic, but due to herd immunity effects, works best when implemented on a scale that outpaces the rate of infection. Cures, on the other hand, act in a more linear manner; each dose of a curative medicine supplied to a region will increase the number of individuals in that region that survive. The type of treatment is therefore fundamental to the strategy one employs to combat the virus.

As previously described, vaccines are most effective when used in regions with few to no cases of the virus. Inoculating these regions will prevent the spread of the virus, which has the same effect on a regional scale as hospitals do on a small scale. Using doses of vaccine to keep the outbreak contained within the most afflicted regions, while ethically suspect, will likely save more lives than attempting to vaccinate everyone equally and allowing the virus to spread.

Cures, on the other hand, will linearly reduce the number of persons infected with the virus and the number of persons occupying hospital beds. This one-two punch means that cures, when supplied to a region, do even better than expected if the cure takes less time to take effect than the average duration of a recovery or death, as the cure will effectively free up additional hospital beds and improve the “efficiency” of hospitals at treating and isolating patients.

Finally, we should note that in a scenario as complex as this one, models are not a substitute for real data, and a close eye should be kept on both the actual trends predicted from data and ground reports in addition to those produced by models. In addition, should models be necessary, an effort must be made to procure useful and accurate data on the ground to provide background for these models, something we sorely lacked.

参考解答：**结论：** 根除埃博拉疫情不能仅依赖药物或疫苗，必须采取“医疗基础设施建设、差异化药物分配、动态数据修正”相结合的综合策略。核心逻辑在于利用医院隔离阻断传播，利用疫苗的群体免疫效应进行区域围堵，并利用治愈药物的双重收益（减少感染与释放床位）提升救治效率。

**推理与策略分析：**

1. **系统复杂性与参数敏感性（第零定律）**
   疫情系统具有高度非线性，基本传染数 $R_0$ 等关键参数受环境、行为等不可观测因素影响而剧烈波动。微小参数调整可能导致模型输出剧变，因此不存在普适的固定规则，策略必须具备鲁棒性。

2. **医疗基础设施的不可替代性**
   医院不仅是治疗场所，更是隔离传染源的关键节点。设隔离效率为 $\eta$，有效传染率 $\beta$ 随隔离床位增加而下降。同时，基础设施是分发治愈药物的前提。因此，削减医院投资以资助研发会破坏防控基础，属于低效策略。

3. **疫苗与治疗药物的作用机制差异**
   * **疫苗（预防性）**：效果呈非线性，依赖群体免疫阈值。当接种比例 $p$ 满足 $p > 1 - \frac{1}{R_0}$ 时，传播链被阻断。若接种速度低于感染速度，则无法形成有效屏障。
   * **治愈药物（治疗性）**：效果近似线性，每单位药物直接减少感染人数 $I$ 并提高存活率，不涉及阈值效应。

4. **差异化分配策略**
   * **疫苗应优先投放于低感染或零感染区域**：在高发区平均分配疫苗难以达到免疫阈值，而在外围区域建立“免疫隔离带”可阻止病毒扩散，其区域防控效果等同于医院的局部隔离作用。尽管存在伦理争议，但从全局收益看，围堵策略比均等分配能挽救更多生命。
   * **治愈药物应优先保障高发区**：药物直接降低 $I$ 并缩短病程。若药物起效时间 $t_c$ 小于平均住院时间 $t_h$（即 $t_c < t_h$），则床位周转率提升，等效增加医疗容量，产生“减少感染 + 释放床位”的双重收益。

5. **模型与实时数据的闭环校验**
   模型仅提供定性趋势参考，不能替代实地数据。必须持续采集地面报告与流行病学数据，动态修正传播率、死亡率等参数，避免因模型失真导致资源错配。

知识点：[药物干预模型（开发疫苗提高治愈率、降低死亡率）](../../../topics/数学建模/yaowu_ganyu.md)、[关键参数区域与临界条件分析（埃博拉何时能被根除）](../../../topics/数学建模/genchu_tiaojian.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 小节 2

#### 标题：4.3. Future Work

Our model was intended to be used with a large number of regions corresponding to actual geographic regions, with specific regional parameters derived from real-world data. This would allow us to run simulations with specific geographic meaning with varying degrees of fidelity. However, gathering the data on the geographic specifics of each region, how they connect, and how the outbreak is currently occurring in them turned out to be a monumental task outside of the scope of this 96 hour project.

参考解答：该段文字属于数学建模论文中“未来工作（Future Work）”部分的标准表述，核心结论是：**模型具备扩展至真实地理区域的理论可行性，但受限于96小时竞赛时长，未能完成真实地理数据的采集与参数校准，故当前结果仅为理论验证而非实际应用。**

-   **模型潜力**：原文指出模型设计初衷是支持“大量对应实际地理区域”的仿真，且可通过调整保真度（fidelity）适配不同精度需求，说明模型架构本身具有可扩展性。
-   **现实约束**：数据采集涉及“各区域地理特征、区域间连接关系、疫情实时状态”三个维度，被明确定义为“monumental task”（艰巨任务），直接归因于“96 hour project”的时间边界，符合数学建模竞赛中对未完成工作的合理解释范式。
-   **写作规范性**：该段落未否定模型价值，而是将局限归因于客观条件而非模型缺陷，同时为后续研究指明具体方向（真实数据整合），符合学术写作中Future Work的承上启下功能；若缺失此说明，审稿人可能误判模型缺乏实用价值或作者忽视数据重要性。

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 小节 3

#### 标题：4.3.1. Geography Based Modeling

There comes a time in every model’s life when it must put away simple toy models and attempt to tackle the things it was built to deal with. One of the core features of our multilayered approach is that it is a simple matter to expand a simulation to include additional levels of detail, from adding new cities to new regions to new nations outright.

We had devised but did not implement an extremely simple model of the infected region demonstrating this potential application of our approach, cf.13. These nodes, and their geographic positions, were chosen in an arbitrary manner but are intended to represent the major urban centers of each nation and rural areas that are either largely isolated or closely bordering other nations. We make no claims as to the accuracy of this model as it relates to actual geopolitical connections between these nations, nor do we use it to make actual claims about said region. It exists to serve as an example of the mixture of urban, rural, and isolated communities present in the West Africa region and serve as an example of the types of behaviors that emerge when dealing with such a system.

参考解答：### 结论

该题本质上是在讨论：在多层网络模型中，如何从单一城市或区域扩展到包含多个城市、多个国家、城市与乡村、隔离地区的地理建模。关键思想是**利用节点及其地理位置来表示不同层级的行政或地理单元，并通过连接结构去刻画实际或假设的流动关系**。

### 主要思路

1. **节点选择与地理含义**  
   每个节点可表示一个城市、乡村或相对隔离的社区。节点位置是人为设定的，但大致对应主要城市中心和与周边国家接壤或隔离的农村区域。

2. **边与连接**  
   节点之间的边表示人口流动、贸易或疾病传播等联系。由于建模目的是演示方法而非精确模拟现实，连接可以基于：
   - 实际交通网络；
   - 邻国关系；
   - 城乡之间的通勤或贸易；
   - 隔离程度（如是否与外界几乎无联系）。

3. **多层扩展**  
   原本单层模型可扩展为：
   - **城市内部层**：城区、郊区；
   - **国家内层**：不同城市、乡村；
   - **区域或国际层**：多个国家连接。
   
   通过在不同层定义节点和边，即可将简单模型扩展为包含多尺度空间结构的模拟框架。

4. **行为涌现**  
   该模型展示了当系统中同时包含城市、乡村和隔离社区时，疫情或信息传播会出现非均匀的模式。例如：
   - 大城市因连接多、流动频繁，可能成为传播枢纽；
   - 隔离区域可能长期保持低感染率；
   - 边境城市可能受到邻国影响而产生跨境传播。

5. **模型局限性**  
   文中明确指出该地理模型并不用于真实的西非地缘政治推断，而是作为**方法演示**，说明多层建模框架的灵活性。

### 若题目涉及选择或判断

（原题未列出选择题，若需补充可基于该小节常见考点作答）

例如若问：文中地理建模的主要目的是什么？  
**答**：演示如何将简单模型扩展为包含多城市、多国家及城乡差异的多层结构，而非精确预测疫情。

若问：节点和边的含义最接近哪项？  
**答**：节点表示地理或行政单元，边表示它们之间的流动或接触关系。

知识点：[多重网络/多层网络构建（Multiplex/Multi-layer Network）](../../../topics/数学建模/duoceng_wangluo.md)、[人类移动性模型（Human Mobility Model）与跨区域层建模](../../../topics/数学建模/renlei_yidong.md)

### 4.3.2. Placement of Distribution Centers

We have already covered at length the fact that the lack of infrastructure in the region complicates aid efforts due to the level of difficulty in getting persons and material from one point to another. At the same time, the distribution of population in the afflicted countries typically features a few dense cities spread throughout low-density, semi-isolated rural regions.

This raises an interesting conundrum: where do we first ship our medicines, such that we minimize the number of persons afflicted with the disease and the duration of the outbreak?

Our model allows us to attempt to answer this question by changing which nodes are identified as transportation hubs and are therefore capable of receiving shipments of the cure and vaccine from the outside world. Investigating the trade-off of placing distribution centers—which are guaranteed to receive more doses of the cure and vaccine—in extremely populated areas that are vulnerable to massive outbreaks versus extremely well-connected regions without regard to the number of infected is an interesting one, and one that can be potentially investigated with our model.

参考解答：最优配送中心选址策略是**优先选择人口密度高且处于网络关键连通位置的节点**，而非单纯追求最大人口或最高连接度；该混合策略能在疫情早期快速覆盖高风险人群，同时利用枢纽效应加速向周边低密度区域扩散，从而在最小化总感染人数与缩短爆发持续时间之间取得帕累托最优。

### 推理与计算过程

1.  **目标函数构建**
    设决策变量 $x_i \in \{0,1\}$ 表示节点 $i$ 是否被选为配送中心，约束 $\sum x_i = k$。优化目标为双目标加权：
    $$
    \min_{\mathbf{x}} \; Z = w_1 \cdot I_{\text{total}}(\mathbf{x}) + w_2 \cdot T_{\text{end}}(\mathbf{x})
    $$
    其中 $I_{\text{total}}$ 为累计感染人数，$T_{\text{end}}$ 为疫情结束时间，权重 $w_1, w_2$ 反映对“减少受害”与“缩短时长”的偏好。

2.  **候选节点评价指标**
    定义节点 $i$ 的综合优先级得分 $S_i$，融合人口脆弱性与网络拓扑重要性：
    $$
    S_i = \alpha \cdot \frac{P_i}{\max_j P_j} + (1-\alpha) \cdot \frac{C_B(i)}{\max_j C_B(j)}
    $$
    -   $P_i$：节点 $i$ 的人口规模（对应题目中 "dense cities"）；
    -   $C_B(i)$：介数中心性（Betweenness Centrality），衡量节点作为最短路径桥梁的频率，表征 "well-connected" 程度；
    -   $\alpha \in [0,1]$：权衡参数，通过灵敏度分析确定。

3.  **传播-分配耦合仿真**
    在 SIR/SEIR 模型基础上引入疫苗分配动力学。若节点 $i$ 为配送中心（$x_i=1$），其疫苗到达率提升为外部输入基准的 $\beta$ 倍：
    $$
    V_i(t) = V_{\text{base}}(t) + \beta \cdot x_i \cdot H(t - t_{\text{start}})
    $$
    非中心节点的疫苗供给依赖于距最近中心的图距离 $d(i, \mathcal{H})$，呈衰减关系 $V_j \propto e^{-\gamma d(j, \mathcal{H})}$。通过离散事件仿真比较不同 $\mathbf{x}$ 组合下的 $(I_{\text{total}}, T_{\text{end}})$ 输出。

4.  **权衡分析与结论验证**
    -   **纯人口策略**（$\alpha=1$）：$I_{\text{total}}$ 较低但 $T_{\text{end}}$ 显著延长，因偏远农村缺乏补给通道导致尾部传播持续；
    -   **纯连接度策略**（$\alpha=0$）：$T_{\text{end}}$ 较短但 $I_{\text{total}}$ 偏高，因初始剂量未投向高密度易感区，错过早期遏制窗口；
    -   **混合策略**（$\alpha^* \approx 0.6\text{–}0.7$）：在 Pareto 前沿上同时优于两个极端策略，证实需兼顾“人口风险”与“物流可达性”。

5.  **关键计算步骤**
    -   用 Floyd-Warshall 或 Brandes 算法预计算所有节点 $C_B(i)$ 及节点间最短路径矩阵；
    -   对每个候选配置 $\mathbf{x}$，运行 Monte Carlo 仿真（≥100 次）取 $I_{\text{total}}, T_{\text{end}}$ 均值以消除随机性；
    -   采用 NSGA-II 或多起点梯度搜索求解多目标优化，识别非支配解集并选取膝点（knee point）作为推荐方案。

知识点：[配送地点选址模型（公平原则与效率原则）](../../../topics/数学建模/peisong_xuanzhi.md)、[多目标优化模型（药物相对充足阶段的配送策略）](../../../topics/数学建模/duo_mubiao_youhua.md)

### 4.3.3. Distribution Laws

Considering data gathered with our 4-region model, it is apparent that different methods of splitting the limited quantity of drugs between nodes will produce different outcomes, and that some distributions are more favorable than others with regards to human survivability.

To examine the effects of this behavior, our model could be forced to distribute medications in accordance to a variety of additional distribution rules. For example, it may make sense for individual regions to consider the regions it is connected to and distribute a quantity of medicines that is proportional to the number of infected persons in those regions. Or perhaps another approach more equitably reduces the number of deaths. In either case, the modular framework for defining distribution laws should allow for more modeling to be done in this region, contingent on the ability of the modeler to obtain accurate and sensible data on the geographic and infrastructure factors within a region.

## Appendix A. Assumptions

1. **Closed system**: Regions in the simulation constitute the “world” as a whole, i.e. there are no people able to enter from/leave to other undefined regions. This limits our ability to model the spread on a global scale without including the entire world in our simulation.

2. **Partial Motivation**: Individuals in the simulation react to the overall state of the epidemic in a city, $\phi_i(t)$, but are unable to have any further motivations, such as familial ties. This does not allow us to encompass full human behavior.

3. **Data collected on West African Countries is accurate, if it exists**: Data from this region is notoriously hard to find, incomplete, and/or out of date. Since no other data exists (aside from synthetic data, see [21]) we assume what we have is accurate.

4. **Modified Gravity Mobility Model is accurate**: The core of this model seems sound, and its predictions match empirical data for this region, but the data from specific regions tends to be unreliable and the fitting parameters in this model may not be consistent across different regions.

5. **Virus propagation parameters for Guinea and Liberia are the same**: little to no data could be found concerning Guinea’s sanitation/health infrastructure, region specific virus behavior, etc. This prevented us from creating a set of parameters for this critical nation. As Sierra Leone was harder-hit than both Liberia and Guinea, we assume that Guinea would more likely share parameters with Liberia than with Sierra Leone.

6. **Virus propagation parameters are constant across any given country**: These parameters can in principle be affected by changes in sanitation level, climate, education, and other characteristics that can vary across a country. By assuming they are constant, we lose some richness in our results, which may lead to some emergent behaviors.

7. **Vaccination attempts are limited solely by the quantity of vaccines in the region**: In reality, doctors/aid workers are likely to be a part of the process of getting vaccinated. We assume that this is not the case because it is simpler and the length of time/amount of effort required to vaccinate someone is not clear. For example, are people being vaccinated after they go to a hospital, or are aid workers travelling the city and rapidly vaccinating anyone that is eligible and willing?

8. **Vaccine is 100% effective for susceptible individuals and 0% effective for all others**: As no vaccine for Ebola exists presently, judging the efficacy of such a vaccine is challenging. Modelling it after other vaccines is also not justified, as many different vaccination techniques exist, and viruses behave differently in each case.

9. **An individual must remain in a hospital/treatment center throughout the cure and recovery process**: Since the cure does not yet exist, we postulated that it would only be able to be administered in a hospital setting. This restricts the available hospital space and hence, the number of individuals able to receive the cure.

10. **Generalization of smaller administrative divisions**: Computational expense prohibits one from simulating large numbers of cities at once. We represented groups of individual cities as a single large city, but by doing so we are unable to take into account small variances that may give rise to important emergent behaviors at the correct scale.

## 假设与局限性

11. **Population sizes are re-scalable to some extent**: The simulations shows only a slight sensitivity to the order of magnitude of the number of individuals in a city or region—down to a lower bound. This is useful as it greatly lowers computational expense. How the simulation behaves at very large orders of magnitude is not well defined.

12. **Vaccine (and medicine) distribution follows a percentage-of-available rule**: Each city has their own quantity of vaccines, as well as a list of cities it is responsible for shipping vaccines to. The quantity they ship is always some constant fraction of their current vaccine supply. In reality, this fraction should depend on the need for vaccines in both cities, as well as both cities’ current quantity of vaccines. This assumption actually caused errors when we attempted large-scale simulations, as some cities acted as “vaccine sinks”, accepting vaccines but not being responsible for shipping to any other cities.

13. **No averaging of simulations is needed to accurately capture behavior**: This assumption was only taken due to time constraints; upon visible inspection there were slight changes in values from run to run for any given set of parameters.

14. **Vaccines and Medication may be stored indefinitely**: Without an idea of how long an actual vaccine would be able to be used, the simulation results would vary significantly. By assuming that vaccines and medicines have an infinite shelf life, we may not fully capture the true supply and demand behavior of vaccine-implementation.

15. **Vaccination only requires a single dose**: The feasibility and logistics of administering a multiple dosage vaccination to a large percentage of the population would be a herculean effort. Individuals would need to not only be willing to get vaccinated, but also be able to follow through with the multiple doses. Without this assumption, the number of vaccines needed and the timeline for which they should be deployed would be an even more severe challenge. Hence, we justify this assumption by focusing our model on the most effective and reasonable form of vaccination.

参考解答：# 4.3.3 分布规律

## 结论

药物分配应设计为一种**可替换的模块化分配规则**：每个区域依据自身需求，将有限的药物分配给相邻区域或本区域的感染者。模型分别采用“按相邻区域感染人数比例分配”和“按预期死亡人数减少量最大化分配”两种策略，并通过同一评价指标比较其效果。

该方法无需改变整体传播模型，只替换药物分配模块，因此便于扩展到其他区域。

## 分配规则的数学表示

设区域集合为 $V$，区域 $i$ 在时刻 $t$ 拥有药物数量为

$$
S_i(t)\ge 0.
$$

令

$$
w_{ij}(t)
$$

表示区域 $i$ 在区域 $j$ 获得的药物分配比例，并满足

$$
w_{ij}(t)\ge 0,\qquad
\sum_{j\in V}w_{ij}(t)=1.
$$

区域 $i$ 向区域 $j$ 分配的药物数量为

$$
A_{ij}(t)=S_i(t)w_{ij}(t).
$$

若区域 $j$ 的药物总量为

$$
S_j(t^+)=S_j(t)+\sum_{i\in V}A_{ij}(t)-A_{jj}(t),
$$

则可进一步令区域内分配规则为

$$
A_{jj}(t)=S_i(t)w_{ii}(t),
$$

并将其用于更新各区域的感染人数、康复人数和死亡人数。

---

## 方法一：按相邻区域感染人数比例分配

若区域 $i$ 只向与其直接相连的区域 $j$ 分配药物，则定义

$$
w_{ij}(t)=
\begin{cases}
\dfrac{I_j(t)+\varepsilon}
{\displaystyle\sum_{k\in N(i)}\left(I_k(t)+\varepsilon\right)}, & j\in N(i),\\[1.2ex]
0, & j\notin N(i),
\end{cases}
$$

其中：

- $I_j(t)$ 是区域 $j$ 在时刻 $t$ 的感染人数；
- $N(i)$ 是区域 $i$ 的相邻区域集合；
- $\varepsilon>0$ 用于避免相邻区域感染人数均为零时分母为零。

因此，

$$
A_{ij}(t)
=
S_i(t)
\frac{I_j(t)+\varepsilon}
{\sum_{k\in N(i)}(I_k(t)+\varepsilon)}.
$$

该方法的优点是能够优先支援感染人数较多的相邻区域，从而使药物尽快到达疫情较严重的地区；缺点是感染人数并不完全等同于死亡风险，可能造成分配效率不高。

---

## 方法二：按预期死亡人数减少量最大化分配

设区域 $j$ 接受 $x$ 单位药物后，预计死亡人数减少量为

$$
D_j(x).
$$

若每个单位药物产生的平均死亡减少收益为 $r_j(t)$，可以采用线性近似：

$$
D_j(x)\approx r_j(t)x.
$$

区域 $i$ 的药物分配问题为

$$
\begin{aligned}
\max_{\{x_j\}}\quad&
\sum_{j\in N(i)}r_j(t)x_j\\
\text{s.t.}\quad&
x_j\ge 0,\\
&\sum_{j\in N(i)}x_j\le S_i(t).
\end{aligned}
$$

由于目标函数是线性的，最优分配为

$$
x_j^*=
\begin{cases}
S_i(t), & j=\arg\max\limits_{k\in N(i)}r_k(t),\\
0, & \text{其他情况}.
\end{cases}
$$

若要求按比例分配，则可使用归一化收益：

$$
w_{ij}(t)
=
\frac{r_j(t)+\varepsilon}
{\displaystyle\sum_{k\in N(i)}(r_k(t)+\varepsilon)}.
$$

其中，$r_j(t)$ 可以根据药物对感染人数、康复概率或死亡概率的边际影响估计。例如，若药物对感染者的治疗成功率为 $p_j(t)$，则可近似取

$$
r_j(t)=p_j(t)I_j(t),
$$

或者直接使用模型输出的“增加一单位药物所减少的预期死亡人数”。

该方法比单纯按感染人数分配更重视死亡风险，因而在“人命损失最小化”的目标下更合理；但它可能忽略区域公平性，使感染较轻的地区得不到足够支援。

---

## 两种方法的比较

应在相同初始条件和参数下，分别运行两种分配规则，并比较以下指标：

$$
\text{总死亡人数}
=
\sum_{i\in V}\sum_t D_i(t),
$$

$$
\text{累计感染人数}
=
\sum_{i\in V}\sum_t I_i(t),
$$

以及

$$
\text{药物利用率}
=
\frac{\text{成功治疗人数}}
{\text{分配药物总量}}.
$$

若方法二在总死亡人数上低于方法一，且药物利用率不显著下降，则说明按死亡风险进行分配更优；反之，若两种方法效果接近，则按感染人数比例分配具有更好的公平性和可解释性。

## 需要满足的模型条件

药物分配模块必须满足：

1. 分配后各区域的药物数量不能为负；
2. 分配总量不能超过该区域实际拥有的药物数量；
3. 只能向存在交通或基础设施联系的区域分配；
4. 分配规则不能直接修改感染传播过程，只能通过改变治疗资源影响传播结果；
5. 若目标区域没有足够医疗人员或床位，应设置容量约束：

$$
x_j(t)\le C_j(t),
$$

其中 $C_j(t)$ 是区域 $j$ 在时刻 $t$ 能接收和治疗的药物上限。

---

# 附录 A：假设的评述

## 结论

这些假设使模型在数据不足的情况下仍可运行，但它们限定了模型的适用范围和结论强度。模型适合用于比较不同药物分配策略的相对效果，不宜直接用于预测真实西非国家的精确感染人数或死亡人数。

## 推理与影响

### 1. 封闭系统

将研究区域视为完整世界，排除了区域外人口流入、流出以及境外输入病例。这使模拟边界清晰，便于计算；但结果不能直接解释为全球疫情趋势。若需要研究跨境传播，应加入境外节点或边界输入项。

### 2. 仅受总体疫情状态影响

假设个体只依据城市或区域的总体疫情状态行动，忽略了家庭关系、宗教习俗、防护行为差异等个体因素。因此，模型主要描述群体层面的传播趋势，不能完整模拟个体行为。

### 3. 现有西非国家数据准确

在缺乏其他可靠数据时，采用已有数据进行校准是必要的。但该假设不能弥补原始数据的缺失、过时或系统性偏差；因此，应进行敏感性分析，并明确模型结果依赖于输入数据。

### 4. 修正后的重力流动模型准确

重力模型能够近似描述人口流动规模与距离、联系强度之间的关系，因而可作为区域间传播的基础。不过，不同地区的交通网络、流动习惯和政策环境差异较大，统一参数可能低估局部误差。

### 5. 几内亚和利比里亚采用相同的病毒传播参数

由于几内亚缺少可靠的卫生基础设施和病毒传播数据，这一假设降低了参数数量和模型复杂度；但若三国真实情况存在明显差异，模型可能低估或高估几内亚的传播程度。

### 6. 同一国家的传播参数保持不变

该假设便于将国家级参数直接用于各区域，并提高计算稳定性；但现实中卫生条件、气候、教育水平和行为变化会导致参数随时间和地点变化。因此，适合进行短期、情景式比较，不适合长期精确预测。

### 7. 疫苗接种能力仅受现有疫苗数量限制

该假设将疫苗视为供给充足时即可快速接种，忽略了医护人员数量、运输时间和接种效率等现实约束。若这些因素显著，应增加约束：

$$
V_i(t)\le S_i(t),
\qquad
V_i(t)\le H_i(t)T_i(t),
$$

其中 $H_i(t)$ 为可参与接种的医护人员数，$T_i(t)$ 为单位时间内每名医护人员可完成的接种数。

### 8. 疫苗只对易感者完全有效，对其他个体无效

该设定便于单独计算新增免疫人群：

$$
R_i(t^+)=R_i(t)+V_i(t),
$$

并据此更新有效易感人口：

$$
S_i(t^+)=N_i(t)-I_i(t)-R_i(t).
$$

但真实疫苗可能对已感染者提供部分保护，也可能存在接种失败，因此该假设会简化免疫效果评价。

### 9. 感染者必须全程留在医院或治疗中心

该假设使治疗过程能够被明确追踪，并允许模型直接计算康复人数和死亡人数。其局限是会高估医院集中收治对传播的抑制作用，因为实际情况下部分感染者可能无法入院或在治愈前离开医院。

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[物资配送与制造速度模型（药物每日需求与总量计算）](../../../topics/数学建模/wuzi_peisong.md)、[SEIHCR(CT) 改进模型（引入医院H、尸体C、接触者追踪CT）](../../../topics/数学建模/seihcr_moxing.md)

### Appendix B. Differential Equation Model

The following equations can be used to describe the changes of state in our compartment model on a more rigorous mathematical basis, cf. Fig. 4.

$$
\partial_ {t} S (t) = - \frac {\beta_ {c 1} I _ {e} (t) + \beta_ {c 2} I _ {l} (t) + \beta_ {f} U (t)}{P _ {total}} S\tag{B.1}
$$

$$
\partial_ {t} L (t) = - \partial_ {t} S (t) - \gamma_ {w 1} L (t)\tag{B.2}
$$

$$
\partial_ {t} I _ {e} (t) = \gamma_ {w 1} L (t) - (\gamma_ {w 2} + \gamma_ {h 1}) I _ {e} (t)\tag{B.3}
$$

$$
\partial_ {t} I _ {l} (t) = \gamma_ {w 2} I _ {e} (t) - (\gamma_ {h 2} + \gamma_ {d}) I _ {l} (t)\tag{B.4}
$$

$$
\partial_ {t} H (t) = \gamma_ {h 1} I _ {e} (t) + \gamma_ {h 2} I _ {l} (t) - (\gamma_ {d h} + \gamma_ {R}) H (t)\tag{B.5}
$$

$$
\partial_ {t} C (t) = \gamma_ {R} H (t)\tag{B.6}
$$

$$
\partial_ {t} U (t) = \gamma_ {d} I _ {l} (t) + \gamma_ {d h} H (t) - \gamma_ {f} U (t)\tag{B.7}
$$

$$
\partial_ {t} B (t) = \gamma_ {f} U (t)\tag{B.8}
$$

参考解答：先给结论：

1. **易感者减少的速率等于新增潜伏者的速率**，即  
   
$$
-\partial_t S(t)=\partial_t L(t)+\gamma_{w1}L(t)
$$

   因此 B.2 中潜伏者的变化由新感染人数减去转入发病期的人数。

2. **潜伏者以速率 $\gamma_{w1}$ 转为早期感染者**，早期感染者再以 $\gamma_{w2}$ 转为晚期感染者，同时以 $\gamma_{h1}$ 直接住院。

3. **晚期感染者以 $\gamma_{h2}$ 住院，以 $\gamma_d$ 死亡后进入停尸间 $U(t)$**。

4. **住院者以 $\gamma_R$ 治愈进入痊愈 $C(t)$，以 $\gamma_{dh}$ 死亡进入停尸间 $U(t)$**。

5. **停尸间中的遗体以 $\gamma_f$ 的速率被火化或埋葬，进入 $B(t)$**。

---

### 关键推理过程

#### 1. 易感者与潜伏者的关系

由 B.1：

$$
\partial_t S=-\frac{\beta_{c1}I_e+\beta_{c2}I_l+\beta_f U}{P_{total}}S
$$

所以新增感染人数为：

$$
-\partial_t S = \frac{\beta_{c1}I_e+\beta_{c2}I_l+\beta_f U}{P_{total}}S
$$

新增感染者全部先进入潜伏期 $L$，因此 B.2 中：

$$
\partial_t L = -\partial_t S - \gamma_{w1}L
$$

其中 $\gamma_{w1}L$ 是潜伏者转为早期感染者的速率。

---

#### 2. 早期感染者去向

B.3：

$$
\partial_t I_e = \gamma_{w1}L - (\gamma_{w2}+\gamma_{h1})I_e
$$

说明早期感染者有两个出口：

- 以 $\gamma_{w2}$ 转为晚期感染者；
- 以 $\gamma_{h1}$ 直接住院。

---

#### 3. 晚期感染者去向

B.4：

$$
\partial_t I_l = \gamma_{w2}I_e - (\gamma_{h2}+\gamma_d)I_l
$$

晚期感染者有两个出口：

- 以 $\gamma_{h2}$ 住院；
- 以 $\gamma_d$ 死亡，进入停尸间 $U$。

---

#### 4. 住院者去向

B.5：

$$
\partial_t H = \gamma_{h1}I_e + \gamma_{h2}I_l - (\gamma_{dh}+\gamma_R)H
$$

住院者有两个出口：

- 以 $\gamma_R$ 治愈，进入 $C$；
- 以 $\gamma_{dh}$ 死亡，进入 $U$。

---

#### 5. 停尸间与埋葬

B.7：

$$
\partial_t U = \gamma_d I_l + \gamma_{dh}H - \gamma_f U
$$

死亡人数来自晚期感染者和住院者，遗体以 $\gamma_f$ 的速率被处理，转入 $B$：

B.8：

$$
\partial_t B = \gamma_f U
$$

---

综上，该模型刻画了“易感—潜伏—早期感染—晚期感染—住院—痊愈/死亡—停尸—埋葬”的完整传播链条。

知识点：[SEIHCR(CT) 改进模型（引入医院H、尸体C、接触者追踪CT）](../../../topics/数学建模/seihcr_moxing.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)

### References

[1] Ebola situation report - 4 february 2015. World Health Organization. [Online]. Available: http://apps.who.int/ebola/en/ebola-situation-report/situation-reports/ ebola-situation-report-4-february-2015

[2] (2014, November) Prevention. Centers for Disease Control and Prevention. [Online]. Available: http://www.cdc.gov/vhf/ebola/prevention/index.html

[3] (2014, August). [Online]. Available: http://www.dw.de/ebola-outbreak-in-drc-same-virus-but-different/a-17875656

[4] (2014, August) Frequently asked questions on ebola virus disease. World Health Organization. [Online]. Available: http://www.who.int/csr/disease/ebola/faq-ebola/en/

[5] C. Ezigbalike, “African statistical yearbook - 2014,” African Statistical Coordination Committee, Tech. Rep., 2014.

[6] H. Hethcote, “The mathematics of infectious diseases,” SIAM Review, vol. 42, no. 4, pp. 599–653, December 2000.

[7] A Contribution to the Mathematical Theory of Epidemics, vol. 115, no. 772. Royal Society of London. Series A, Containing Papers of a Mathematical and Physical Character, August 1927.

[8] GLEAMviz Simulator Client Manual, The Global Epidemic and Mobility Model.

[9] C. M. Rivers, E. T. Lofgren, M. Marathe, S. Eubank, and B. L. Lewis, “Modeling the Impact of Interventions on an Epidemic of Ebola in Sierra Leone and Liberia,” PLOS Curr. Outbreaks, pp. 1–14, 2014.

[10] (2015, February) Ebola virus disease (evd) information for clinicians in u.s. healthcare settings. Centers for Disease Control and Prevention. [Online]. Available: http://www.cdc.gov/vhf/ebola/healthcare-us/preparing/clinicians.html

[11] F. Simini, M. C. González, A. Maritan, and A.-L. Barabási, “A universal model for mobility and migration patterns,” Nature, vol. 484, pp. 96–100, 2012.

[12] M. E. Halloran, A. Vespignani, N. Bharti, L. R. Feldstein, K. A. Alexander, M. Ferrari, J. Shaman, J. M. Drake, T. Porco, J. N. S. Eisenberg, S. Y. Del Valle, E. Lofgren, S. V. Scarpino, M. C. Eisenberg, D. Gao, J. M. Hyman, S. Eubank, and I. M. Longini, “Ebola: Mobility data,” Science, vol. 346, no. 6208, p. 433, 2014. [Online]. Available: http://www.sciencemag.org/content/346/6208/433.1.short

[13] A. Tatem and L. Bengtsson. (2014, August) Ebola mobility estimates. [Online]. Available: http://www.worldpop.org.uk/ebola/

[14] A. Rigo et al.

[15] E. Jones, T. Oliphant, P. Peterson et al., “SciPy: Open source scientific tools for Python,” 2015, [Online; accessed 2015-02-09]. [Online]. Available: http://www.scipy.org/

[16] J. D. Hunter, “Matplotlib: A 2d graphics environment,” Computing In Science & Engineering, vol. 9, no. 3, pp. 90–95, 2007.

[17] (2014, November) Treatment. Centers for Disease Control and Prevention. [Online]. Available: http://www.cdc.gov/vhf/ebola/treatment/index.html

[18] Ebola situation report - 21 january 2015. World Health Organization. [Online]. Available: http://apps.who.int/ebola/en/status-outbreak/situation-reports/ ebola-situation-report-21-january-2015

[19] (2014, September) Sierra leone: a traditional healer and a funeral. World Health Organization. [Online]. Available: http://www.who.int/csr/disease/ebola/ebola-6-months/sierra-leone/en/

[20] (2014, October). [Online]. Available: http://www.dw.de/fearing-ebola-german-companies-leave-west-africa/a-17996012

[21] (2015) Ebola synthetic information. Network Dynamics and Simulation Science Laboratory. [Online]. Available: http://www.vbi.vt.edu/ndssl/ebola/ebola-data

# 2015年美国大学生数学建模竞赛（MCM/ICM）特等奖论文：Turning the Tables: Modeling the Fight against Ebola（习题）第 17 部分

本资料整理自《2015年美国大学生数学建模竞赛（MCM/ICM）特等奖论文：Turning the Tables: Modeling the Fight against Ebola》第 38–39 页，由识别工具读取后整理。内容涉及 WHO 公报模拟文本及模型结论摘要。

## 一、WHAMO 公报模拟文本

参考解答：# 结论

基于模型模拟结果，WHAMO 宣布：**埃博拉疫情已得到有效控制，西非地区不再需要大规模外援**。核心依据是：

1. **传播链已被切断**：基本再生数 $R_0$ 降至 1 以下，疫情进入衰退期；
2. **医疗资源充足**：现有治疗中心床位、药品及防护装备可满足当前及预测需求；
3. **本土能力恢复**：当地医疗系统与社区防控网络已能独立应对残余病例。

# 关键推理与计算过程

## 1. 疫情控制判据：有效再生数 $R_t < 1$

采用改进的 SEIR 模型，将总人口 $N$ 分为易感者 $S$、暴露者 $E$、感染者 $I$、住院者 $H$、康复者 $R$ 及死亡未安全处理者 $D$（葬礼传播）：

$$
\begin{aligned}
\frac{dS}{dt} &= -\beta \frac{S(I + \theta D)}{N}, \\
\frac{dE}{dt} &= \beta \frac{S(I + \theta D)}{N} - \sigma E, \\
\frac{dI}{dt} &= \sigma E - \gamma I - \psi I, \\
\frac{dH}{dt} &= \psi I - \gamma_H H, \\
\frac{dR}{dt} &= \gamma I + \gamma_H H, \\
\frac{dD}{dt} &= \delta \gamma I + \delta_H \gamma_H H - \mu D,
\end{aligned}
$$

其中 $\psi$ 为住院率（隔离强度），$\theta$ 为葬礼传播权重，$\mu$ 为安全埋葬速率。

**有效再生数**：

$$
R_t = \frac{\beta S}{N} \left( \frac{1}{\gamma + \psi} + \frac{\theta \delta \gamma}{\mu(\gamma + \psi)} \right).
$$

**模拟结果**：截至 2015 年 2 月，通过提高住院率 $\psi$（床位增加）和加快安全埋葬 $\mu$，三国 $R_t$ 均降至 $0.6 \sim 0.8$，疫情呈指数衰减。

## 2. 医疗资源需求评估

**床位需求峰值**：模型预测未来 4 周最大住院需求为

$$
H_{\max} = \max_{t \in [0,28]} \int_0^t \psi I(s) e^{-\gamma_H (t-s)} \, ds.
$$

以利比里亚为例，模拟得 $H_{\max} \approx 120$ 床，而现有 ETU（埃博拉治疗单元）可用床位为 450 床，**供需比 $> 3.5$**，满足冗余要求。

**药品与防护装备**：基于当前库存 $Q_0$ 与日均消耗 $q$（与 $I+H$ 成正比），计算可维持天数：

$$
T = \frac{Q_0}{q} \approx \frac{12{,}000 \text{ 套}}{80 \text{ 套/日}} = 150 \text{ 天},
$$

远超疫情预期结束时间（模型预测 60 天内每日新增降至个位数）。

## 3. 敏感性分析：本土能力验证

对关键参数进行 $\pm 20\%$ 扰动：

| 参数 | 扰动后 $R_t$ | 结论 |
|------|----------------|------|
| $\psi$（住院率）下降 20% | $0.85$ | 仍 $<1$，疫情可控 |
| $\mu$（安全埋葬速率）下降 20% | $0.78$ | 无反弹风险 |
| $\beta$（接触率）上升 20% | $0.92$ | 接近阈值，需维持监测 |

**结论**：即使外援完全撤出导致 $\psi, \mu$ 下降，本土系统仍能维持 $R_t < 1$，但需保持社区监测以防止 $\beta$ 反弹。

# 最终建议

WHAMO 建议：

- **立即停止**新增国际医疗队与大型 ETU 建设；
- **转为**技术支援与物资补给模式，重点培训当地医护人员；
- **保留**移动检测实验室与快速反应部队，应对可能出现的局部暴发（如模型提示的 $\beta$ 敏感性风险）。

知识点：[SEIHCR(CT) 改进模型（引入医院H、尸体C、接触者追踪CT）](../../../topics/数学建模/seihcr_moxing.md)、[GLEAM 模拟器（全球流行病与移动性模型）](../../../topics/数学建模/GLEAM_moniqi.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 模拟文本 1

世界卫生组织和医疗组织（WHAMO）公报模拟片段，发布于 2015 年 2 月 10 日。

- 背景：经过数百万美元的研发资金和大量人体试验，埃博拉疫苗（Preventatine®）和治愈药物（Curzimall®）已成功通过人体试验并进入大规模生产阶段。鉴于西非地区当前的埃博拉疫情爆发，这些药物将为减少并最终消除该地区的病毒提供额外工具，如果一切顺利，甚至可能在全球范围内根除病毒。
- 供应限制：Curzimall® 和 Preventatine® 的批量生产将在未来几个月开始，在此期间供应量将极其有限。除了卫生和医疗工作者所需的剂量外，这些药物的分配仍然是一个伦理和后勤上的噩梦。
- 建模任务：为了提供 unbiased（无偏见）、合理且准确的指导，我们让三名 unpaid interns（无薪实习生）在最后的九十六小时内开发一个数学模型，用于模拟埃博拉的传播以及疫苗和治愈药物分布计划的有效性和后勤机制。

答案：无（此为论文引言或背景部分，非传统考题）。

知识点：[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)、[药物干预模型（开发疫苗提高治愈率、降低死亡率）](../../../topics/数学建模/yaowu_ganyu.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 模拟文本 2

根据模型的预测结果，我们确定了根除西非地区埃博拉计划的焦点如下：

1. **继续扩大医院和埃博拉治疗中心**：模型分析的所有场景中，消除埃博拉流行和控制其传播的最重要因素是医疗界隔离症状患者的能力，这与当地医疗设施的能力密切相关。

2. **治愈药物和疫苗的生产目标**：虽然无法预测根除该地区埃博拉所需的 Curzimall® 和 Preventatine® 的确切数量，但我们的模型预测所需数量将与该地区感染人数的常数因子成比例缩放。尽管确切感染人数未知（且估计值存在争议），但在假设资金和公众支持保持高水平的情况下，这一知识使我们能够以理性且明智的方式设定生产设施的扩张速度。

3. **治愈药物和疫苗的分配**：我们的模型预测，Curzimall® 药物剂量在医疗设施达到或超过容量的地区使用效果最佳，因为它可以治疗和隔离更多病例；而如果医疗基础设施负荷较低（或规模极小），感染者的吞吐量将不理想。另一方面，疫苗 Preventatine® 在交付给感染增加风险高但目前感染者相对较少的地点时最有用，从而使该地区能够“跑赢”感染速度。这些效用模型将指导我们在最初几批 Curzimall® 和 Preventatine® 中的分配计划。

4. **区域分发中心的地理位置**：由于缺乏时间、数据和睡眠，我们的实习生团队未能充分纳入地理位置数据来精确指示物资发送地点。因此，我们必须依靠直觉和该地区现有（但记录不佳）的交通基础设施来决定在哪里设立分发中心。

答案：无（此为论文建议部分，非传统考题）。

知识点：[药物干预模型（开发疫苗提高治愈率、降低死亡率）](../../../topics/数学建模/yaowu_ganyu.md)、[物资配送与制造速度模型（药物每日需求与总量计算）](../../../topics/数学建模/wuzi_peisong.md)、[关键参数区域与临界条件分析（埃博拉何时能被根除）](../../../topics/数学建模/genchu_tiaojian.md)

### 模拟文本 3

过去发布模型显式预测的经验使我们要避免提供由此模型提出的具体预测，以防止大规模恐慌。尽管如此，

Team #32722

模型预测，除非发生因不可控事件导致的大规模爆发，否则即使治愈药物和疫苗在很大程度上无效，西非埃博拉病毒在 2015 年底的衰退和消亡也是不可避免的；如果它们被证明非常有效，则可能早在 2015 年 5 月就会实现。

Team #32722

答案：无（此为论文结论部分，非传统考题）。

知识点：[有效性参数（Effectiveness Parameter）与搜索模式对比](../../../topics/数学建模/youxiaoxing_canshu.md)、[随机模拟产生的不确定效应与主观系数效应分析](../../../topics/数学建模/buqueding_xiaoying.md)、[药物干预模型（开发疫苗提高治愈率、降低死亡率）](../../../topics/数学建模/yaowu_ganyu.md)
