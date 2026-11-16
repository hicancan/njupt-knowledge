---
title: 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）
kind: 竞赛论文
course: 数学建模
source: batch-2:数学建模/2017年美国大学生数学建模竞赛O奖论文（全部）.zip/2017年美国大学生数学建模竞赛O奖论文（全部）/2017年美国大学生数学建模竞赛O奖论文（全部）/F/72283.pdf
---

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）

原件为竞赛论文。补充：文中的阅读练习及“参考解答”为整理时增加，原件图文保留出处。

## 2017 MCM/ICM Summary Sheet

（摘要页说明：提交时摘要应作为电子版第一页；本页不写学校、指导教师、队员姓名。）

针对“Population Zero”火星殖民地各项属性与结果，我们建立了一组有定量支撑的模型。首先，我们为收入、教育、平等三个优先因素分别定义重要指标与评价标准。收入分解为经济效率与经济平等，选定 GDP、基尼系数与社会最低工资作为主要指标；教育以师生比和教育对 GDP 的贡献衡量；平等从性别与文化角度考虑，采用相异度（dissimilarity）指标。

在分析 Population Zero 的人口结构与殖民地目标相关因素时，我们通过量纲分析，把火星上农民生产力与人类基本消费需求联系起来，确定约 25% 的人口应为农民；随后用多种方法求出其他职业的构成。此外，准马尔可夫链模型帮助我们确定最优初始年龄分布，并通过逻辑推理将人口平均分为男、女。

接着，我们针对收入、教育、平等三个优先领域分别建模，应用前述关键指标。我们找到教育与 GDP 的关系，并求出高度技能化、自给自足社会的最优教育投入。我们确定：在经济主要由政府运行、政府工作人员实行工资分级的情况下，可以实现收入不平等极小的经济（基尼系数 = 0.0336），且 GDP 位居地球各国 GDP 前 25%（人均 GDP 约 28800 美元，与教育模型预测一致）。基于相异度的模拟揭示了收入平等与社会平等之间的权衡，并给出了殖民地合理的育儿假长度。

随后，我们将三个模型整合为一个模型，以三个优先领域为函数评估社会不同子群体的满意度。我们为 GDP、相异度等关键参数赋予基于数据的权重并加以应用，发现关键参数的取值较强。通过分析社会平等与收入平等的权衡，模型发现：少量收入不平等优于影响更大的社会不平等。

最后，我们把模型应用于地球向殖民地追加移民的情形。认识到移民可有多种方式，我们分析了三种差异很大的移民方式/政策对年龄分布与经济影响的作用，以判断哪些相对可持续。沿用“渐进移民是最优引入方式”的结论，我们估计了火星殖民地的最大移民速率。LIFE 应认真考虑我们的……

## A Brave New World: A Quantitative Model of A Self-Sufficient Martian Society

Team 72283

January 24, 2017

### 1 Defining the Colony

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 1.1 Restatement of the Problem

For Task 1, we were asked to do the following:

1. Develop evaluation criteria for each of three priority factors for a Martian colony:

   (a) Income, or the existence of an appropriate distribution of wealth that allows all people to afford their fundamental necessities

   (b) Education, the quality of training and preparation of citizens for the relevant necessities and difficulties of living on a Martian colony in the 22<sup>nd</sup> century

   (c) Equality, or the establishment of equitable and fair living and labor conditions for citizens of all genders, races, needs, and other backgrounds and characteristics

2. Infer what aspects of Population Zero would most directly impact the results across these three factors. Define quantitative metrics that can be used to evaluate whether the colony is meeting the challenges posed by the three priority factors.

知识点：[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 1.2 Developing the Criteria and Metrics

To evaluate results across the three priority factors, relevant parameters and inputs to the factors must be defined. We can view income as a two-sided factor: it can be condensed into the two critical factors of most economic debates and discussions—efficiency and equality. Efficiency, or the gross output of the economy, can be assessed in terms of the community's gross domestic product (GDP) and other aspects such as amount of research and agricultural output. The overall success of the colony's economy can be evidenced by such outcomes as population growth due to crop surpluses, major technological spinoffs off research efforts, growth in GDP-related factors such as private investment and consumption, and successful privatization of originally public industries.

Equality refers to the level of egalitarianism reflected by the distribution of wealth across society. The ability of as many people in society to provide for their own basic needs is important in assessing the income equality within the colony. Relevant metrics for equality include the Gini coefficient and the minimum wage. A diminishing wage gap would be a strong indication of income equality.

Education can be broken down into three areas. Most importantly, the effectiveness of formal education programs on the colony is critical. In addition to metrics of the strength of a school, such as teacher-to-student ratio, the actual contributions of students to the economy down the road are key indicators of the quality of education. In that way, the income and education factors are extremely intertwined. In addition, an appropriate volume of research is necessary, especially considering that the long-term development of the colony as well as of human understanding of physics, chemistry, astrobiology, and other fields and the prospects for future space colonization efforts are dependent upon scientific research. Finally, the presence of a multicultural, open-minded environment within the community is of understated significance. As most behavioral and classical economic models will suggest, as discrimination by race, gender, religion, and other personal factors disappear from society, efficiency will rise.

知识点：[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 2 Selecting Population Zero

知识点：[TOPSIS 模型构建步骤（逼近理想解排序法）](../../../topics/数学建模/topsis_moxing.md)、[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[层次分析法 AHP（Analytic Hierarchy Process）用于综合评价](../../../topics/数学建模/ahp_fangfa.md)

### 2.1 Restatement of the Problem

For Task 2, we were asked to do the following:

1. Identify a census dataset from which actionable insights about individuals of a population can be derived
2. Plan a sample Population Zero, considering such factors as the following in order to form a successful and happy community:
    (a) Personal characteristics–age, gender, ethnicity, race
    (b) Education, skills, occupation
    (c) Relationship/marital and family status

知识点：[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)

### 2.2 Assumptions and Justifications

1. Our colony is located millions of miles from the next human settlement. As a result of this enormous distance, Population Zero will be assumed to not engage in much trade with other societies. It needs to be self-sufficient and sustainable–the colony should have the potential to survive without any direct interaction with Earth.

2. Land is not a particularly limiting factor considering the relatively small size of our population and the vastness of the planet, land will not be a concern for Population Zero.

3. Inhabitants of Planet Zero have been vetted to ensure proper health and physical condition for successful transition to and life on Mars. These individuals are capable of thriving on a 2000 kcal/day diet, on average.

4. The average farm size is 4.9 acres, based on the average farm size in north Africa and west Asia (Pungali 3330). This region was chosen as the basis of average farm size because of its many similarities to the surface and environment of Mars: limited natural resources, arid environment, and sparse population. In addition, the fact that this colony, the first of its kind, has to deal with unprecedented agricultural and resource challenges helps to explain why farmers are not expanding too far on the planet.

5. In the absence of fertility and mortality rate data on the surface of another planet, we will use relevant American nationwide data, applying it for current and future generations of colonists. We assume that at best case, people will have similar life expectancies on Mars as on Earth, though it is reasonable that conditions on Mars would shorten the average lifespan of a person.

6. Colonists continue to live in family units and have monogamous reproductive relationships.

7. Given the fact that our society is built largely with the help of augmentation units, we will assume that there is not a major human construction industry. This is supported by the plethora of research avenues looking into the use of artificial intelligence and augmentation intelligence in construction and development of infrastructure (Grayson, Messier, Brachmann).

8. We use Earth years and 2016 dollars.

9. The colony is small enough that transportation costs are negligible - people can generally get around by foot.

10. In reality, the International Coalition on Mars would likely desire a global array of colonists for the new colony, especially if this venture was backed by many different countries and agencies. Given, however, that our census data pertains to the U.S. alone and that authentic census data across several countries is difficult to obtain, we will assume that all 10,000 of our colonists are American.

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 2.3 Planning the community

Our model first requires an understanding of the age distribution. We aim to create a society that experiences population growth and expansion to ensure the survival and success of humanity on Mars. Simultaneously, learning from examples such as China and the U.S.A., where curtailed birth rates over the past several decades are placing the weight of the increasing elderly population on a decreasing population of working-age adults (S.C.), and Bangladesh and Nigeria (Bish), where recent explosions of population are causing overcrowding and sanitation issues, we wish to build a population with stable proportions of the various age groups over time.

Using American fertility and mortality data from the last decade, we established fertility and mortality rates for individuals of all ages (National Center for Health Statistics, U.S. Death Rates). For simplicity, we assume that no person will exceed the age of 100, which is a reasonable assumption due to the fact that individuals over 100 are a negligible proportion of the population.

We used the mortality data to develop a survival-rate for each age, where the survival-rate, $s$, of age $a$ at $x$ is the value such that $sx$ people are age $x + 1$ the next year.

We then created a quasi-Markov chain model to study the effects of various age distributions for Population Zero on the survival and scalability of humans on Mars. We used different numbers of people of each of 100 ages (age of 1 through age of 100) as the original distribution of Population Zero. One transition of the chain, which corresponded to one year of change, was represented by multiplying the current distribution by the transition matrix. We used transition probabilities of $q_{i, i+1}$ to indicate the probability that a person survived and grew one year older. We also applied our fertility and mortality data, using the transition term $q_{i, 1}$ to indicate the probability that a person gave birth to a baby in the transition from one step to the next. $q_{i, j}$ was equal to 0 in cases where $j \neq 1$ and $j \neq i + 1$.

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）

## 一、生育率政策与人口结构优化

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[考虑尸体、医院和接触者追踪的原因阐述](../../../topics/数学建模/shi_ti_yiyuan.md)

### 选择 1：初始生育率调整策略

**背景分析**
模型发现初始出生率不足以抵消死亡率，导致殖民地人口下降。为了维持不同年龄段女性的出生比例不变，团队决定将出生率乘以一个常数因子进行缩放。

- **测试过程**：经过多次测试，团队选择了参数值为 1.08 的出生率参数。
- **结果**：该参数使人口在达到约 18,100 人的稳定点之前实现了稳步增长。
- **实施手段**：为实现略高于美国实际水平的出生率，并考虑到引入新成员对火星新文明发展的重要性，团队建议实施政府政策鼓励生育。
- **具体政策**：在第3部分中，团队采用了公平且合理的育儿假政策来激励个人生育，预计这些慷慨的政策能够实现约 1.08 的出生率。

**知识点**：人口动力学 政策模拟

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 选择 2：理想人口分布（Population Zero）的筛选

**筛选逻辑**
设定出生率参数为 1.08 后，团队测试了大量样本人口分布以寻找理想的“零号人口”（Population Zero）。
- **排除老年群体**：团队决定不携带老年人前往火星，因为目标是带来能为新文明提供最大效用的个体。因此，测试模型中各年龄段人数相对均匀，且年龄不超过 50 岁。
- **关于儿童迁移的论证**：有观点认为不应将儿童作为初始移民的一部分（Redd）。团队通过马尔可夫链模拟验证了这一论点，发现这不是可行的方案。

**模拟案例对比**
团队模拟了一种特定的人口年龄分布情况：
- 11至20岁：2000人（均匀分布）
- 21至30岁：3000人（均匀分布）
- 31至40岁：3000人（均匀分布）
- 41至50岁：2000人（均匀分布）

**模拟结果分析**
在该模型下，文明建立约40年后，退休人员比例远高于工作成年人的比例。
- **问题**：退休人员需要食物和更多医疗关注，却不贡献社区生产或工业。
- **结论**：排除大量年轻人口会对长期发展产生不利影响，因此必须确保带入足够数量的儿童。

**最终确定的最佳分布**
经过比较其他各种人口分布，团队确定了 Population Zero 的最佳构成：
- **1至20岁**：4000人（均匀分布）
- **21至40岁**：6000人（均匀分布）

该分布既支持了殖民地人口的增长，又保持了各年龄段人群比例的稳定性。

**知识点**：马尔可夫链 人口结构优化

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 选择 3：性别分配与遗传多样性策略

**性别分配**
团队发现最优的性别划分是各年龄段男女比例为 50-50。
- **理由**：这允许以最高的生育率进行建模（在一夫一妻制条件下，每个男性恰好需要一个专属女性进行繁殖）。

**遗传多样性与种族分布**
基因变异和多样性对 Population Zero 至关重要。为了防止近亲繁殖的可能性，团队制定了以下策略：
1. **等位基因与表型多样性**：目标是在殖民地实现等位基因分布和表型的多样性。
2. **种族分布**：应追求不同主要种族和民族群体的均匀分布。
3. **文化多元主义**：倡导多元文化，创建一个开放、包容并庆祝跨种族互动和婚姻的社区。
4. **来源多样性**：应从不同地区和家族群体中抽取 Population Zero，以避免后代出现无意识的近亲繁殖。

**遗传变异度量指标**
团队提出了一种基于种族和民族背景的评分系统，用于衡量遗传变异程度：

$$
w = \frac{1}{\prod_{j=1}^{n} p_j}
$$

其中：
- $n$ 是社会中的不同种族数量。
- $p_j$ 是 Population Zero 中属于第 $j$ 种族的成员比例。

**指标解读**：
- **低变异**：如果所有居民都属于同一种族，则 $w = 1$，表明种族线上的遗传变异极低。
- **高变异**：如果极端情况下所有居民都属于不同的种族（假设最小比例为 $10^{-4}$），则 $w = \frac{1}{10^{-4}} = 10000$，表明种族线上存在大量的遗传变异。

尽管该指标较为粗略，但它能提供关于社区主要种族和民族线上变异量的宝贵见解。

**知识点**：种群遗传学 多目标优化

## 二、角色分配与社会功能

**基本需求**
团队开始为成年人分配角色，核心洞察是：必须选出 10,000 名个体组成一个社区，至少能够生存于火星的环境和条件中。
- **劳动力构成**：其中有 6,000 名处于工作年龄（大于20岁）的成年人，他们将分布在社会所需的各个角色中。
- **首要任务**：人类需要食物才能生存，因此社会中最重要的角色回归到了早期社区的基石——农业生产。

*(注：原文在此处结束，后续内容未提供)*

## 农业与医疗人员估算

发展稳定且可持续的农业系统对于殖民地的自给自足和增长至关重要。为了估算殖民地所需的农民数量，考虑到美国人平均每天摄入 2.7 kcal 的饮食（此处原文数据可能有误，通常指每日总热量消耗或特定作物产出，但依据上下文逻辑，后续计算使用了 2000 kcal/day 作为基准）由每年约 1.111974 英亩的农产品满足（Bradford）。因此，平均一英亩农田提供 886.869 kcal/yr。

我们可以通过以下量纲分析来计算我们殖民地所需的农民数量：

$$
\frac {2 0 0 0 \mathrm{kcal}}{1 \mathrm{day} _ {E a r t h} \times 1 \mathrm{person}} \times 1 0 0 0 0 \mathrm{ppl} \times y \times \frac {\mathrm{crops} _ {E a r t h}}{1 \mathrm{kcal}} \times \frac {1}{0 . 6} \times \frac {\mathrm{crops} _ {M a r s}}{\mathrm{crops} _ {E a r t h}} \times z \times \frac {1 \mathrm{farmer} \times 1}{\mathrm{crops} _ {E a r t h}}
$$

其中 $y$ 是地球每英亩作物千卡产量的倒数，$z$ 是一名农民每天可照料的作物英亩数的倒数。$\frac { 1 } { 0 . 6}$ 因子源于在火星上，由于距离太阳较远且光照相对有限，作物生长速度只有地球的 0.6 倍（Starr）。因此，在地球上耕种 1 英亩作物所需的工作量相当于在火星上照料 0.6 英亩作物所需的工作量。

为了获得 $y$ 的合理值，我们可以考虑一英亩甘薯的千卡产量，甘薯通常被认为是火星主要作物中高效且可持续的选择。一英亩正常种植的甘薯估计产量为 2832.8038688 kcal/acre（Renoe, Agriculture and Consumer Protection）。因此，$y$ 是该值的倒数。对于每位农民每天的平均作物量，我们基于北非和西亚洲的平均农场规模选择了 4.9 的值（Pungali 3330）。我们选择该地区作为基础，是因为其与火星表面和环境有许多相似之处：自然资源有限、干旱环境以及人口稀疏。因此，$z$ 是 $\textstyle { \frac { 1 } { 4 . 9 } }$。

使用这些参数值，并假设农民平均每天工作 8 小时，我们得出的农民数量为 2401.41。然而，这里有一个问题！考虑到第三部分平等模型中提出的育儿假和产假选项——婴儿出生后父母共有 6 个月的假期——以及社区每年约有 231 次出生，这意味着全年所有农民时间中约有 1.925% 用于休假，社会中的农民总数必须增加，以便任何时刻工作的平均农民数量等于 2401.41。结果，社会中实际的农民数量为 2448.54。

接下来，我们转向在一个前所未有且潜在危险的生存环境中对新殖民地至关重要的下一组个体：医疗和公共卫生工作者。根据提供的 PUMS 数据集的数据（U.S. Census Bureau.），美国约 10.5% 的工作与公共卫生、医学或医学研究有关。仅仅镜像这个数值是不够的。我们必须考虑到，人在陌生环境中更容易生病，尤其是在之前未接触过的环境中。在火星上，即使新传染病的可能性有限，Population Zero 的孤立性和独特挑战确实创造了对医疗专业人员以及公共卫生和医学研究领域人员的需求。在缺乏火星疾病发病率数据的情况下，我们将不得不使用地球上旅行者的此类数据。地球上的旅行者比在其原生环境中的人生病的可能性高出约 2.18 倍（Daily Mail Online, "Travel Abroad In-Depth Report."）。将火星上从事健康行业的人员百分比按该值加权：

$$
0. 1 0 4 9 2 7 6 0 4 2 4 4 \times 2. 1 8 0 1 6 3 1 5 1 6 1 \times 1 0 0 0 0 = 2 2 8 7. 5 9
$$

因此，大约 2287.59 人应受雇于健康行业。此时，我们还剩下 1263.86 个需要确定角色的个体。转向另一个重要的需求领域——科学研究，我们需要估算在类似火星的条件下发生的科学兴趣量——物理、化学、天体生物、宇宙学以及与殖民化相关的研究。为此，我们可以使用位于犹他州的火星沙漠研究站（Mars Desert Research Station, MDRS）的兴趣量和使用情况，该站模拟了火星的环境和条件。在其存在期间，已有超过 1000 人访问并居住在该站（"About MDRS"）。应努力说服尽可能多的这些科学家定居火星，以扩展对火星大气层和环境的当前知识和认知，进一步努力殖民和适应火星，并在未来继续追求有效的太空殖民方法。理想情况下，ICM 能够说服这 1000 名科学家、工程师和研究人员中的最优数量加入殖民地。让我们假设 ICM 计划带来其中的 60%（600 人），并将其余人员留在地球，与该团队保持联系并进行远程研究和分析。

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）

## 一、社会角色分配与模型验证

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)

### 简答 1

根据我们拥有的人口数量（最初，1到20岁之间的所有4000人被视为学生，尽管在教育模型的长期视角中，这一数字会变小），以及理想师生比为19:1的估计值（“Faculty Teaching Load.”），我们可以计算出最优教师人数为210.53人。利用美国警察部门关于服务于不同人口规模的部门的平均平民与警官比例的数据，我们创建了一个拟合模型，使我们能够估计人口为10,000时的最优平民与警官比例为每1000名平民2.09名警官（Reaves）。将此比例扩展到10,000人口，我们需要20.91名执法官员。

- 参考答案：原文未提供标准答案，以下为基于文本内容的梳理。
- 参考解答：
    1. **教师人数计算**：基于初始人口4000人（1-20岁），理想师生比19:1，计算得教师人数 $4000 / 19 \approx 210.53$ 人。
    2. **执法官员人数计算**：基于美国警察部门数据，建立拟合模型得出每1000平民对应2.09名警官。对于10,000人口规模，所需执法官员数为 $10,000 \times (2.09 / 1000) = 20.9$ 人（文中记为20.91）。
- 知识点：数据拟合, 比例估算

知识点：[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[层次分析法 AHP（Analytic Hierarchy Process）用于综合评价](../../../topics/数学建模/ahp_fangfa.md)

### 简答 2

剩余的432.425个个体将分配到社会中的另外两个重要角色：卫生和商务。基于纽约市每人0.00108076名环卫工人的数据（“NYC Department of Sanitation.”），我们得出社会中需要10.8076名环卫工人。劳动力中剩余的421.617个个体将从事商业、零售以及其他基于非农产品交易的职业。

研究、教育和执法几乎肯定由政府调解，因为这样一个孤立且自给自足的社区的规划必须具有一定的集中性。公共卫生、医疗和卫生工作也可能受到政府监管。在更私有化的行业将是商业/零售和至关重要的农业。由于这两个行业代表商品而非服务，它们作为私人产业发展得更容易，比上述服务业更容易。虽然农业行业可能存在一定程度的政府监管，以确保有足够的食物，但私有化允许由于消费者需求和生产者利润动机而更自然地出现食品盈余。此外，这些行业的相对较大规模，特别是农业，确保市场保持接近完全竞争，稳定的供需市场力量，而不是垄断动机，将决定这些行业的发展方向。

- 参考答案：原文未提供标准答案，以下为基于文本内容的梳理。
- 参考解答：
    1. **剩余劳动力分配**：总劳动力减去教师和执法人员后，剩余432.425人。
    2. **环卫工人**：依据纽约市人均比率（0.00108076/人），计算出需10.8076名环卫工人。
    3. **其他职业**：剩余421.617人从事商业、零售及非农产品交易相关职业。
    4. **行业性质分析**：
        - **政府主导/监管**：研究、教育、执法、公共卫生、医疗、卫生。原因：社区孤立且自给自足，需集中规划；涉及基本生存保障。
        - **私有化倾向**：商业/零售、农业。原因：代表商品而非服务，易市场化；私有化能通过供需机制自然产生盈余；农业规模大，接近完全竞争，避免垄断。
- 知识点：模型假设合理性, 社会经济系统建模

知识点：[层次分析法 AHP（Analytic Hierarchy Process）用于综合评价](../../../topics/数学建模/ahp_fangfa.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 简答 3

为了在我们社区中获得最佳性别比例，我们必须承认拥有过多某一性别的人的后果。人口的扩展能力与其生殖潜力内在相连，当生物学上健康且具有生殖潜力的男性数量等于健康且具有生殖潜力的女性数量时，生殖潜力最高；本质上，男女50-50的分割是最优的。如果假设是一夫一妻制——每个个体在这种情况下有一个配偶，那么只有在由相等数量的男性和女性组成的社区中，生殖关系和可能性的数量才是最优化的。理想情况下，分解还应包括每个代际或年龄组中男性和女性的数量相等；如果在30岁以下有5,000名男性和30岁以上有50,000名女性，这在促进一夫一妻制繁殖方面的相互兴趣方面可能不是最优的。

此外，从文化角度来看，男性和女性在所有年龄组中的均匀分布可能是可取的；例如，男性的过剩让人联想到狂野西部的棚屋区和许多欧洲在新世界定居点的严厉父权和社会等级制度。

一夫一妻制关系和家庭环境很重要，因为它们在家中提供道德和情感支持。这种类型的关系也是优化繁殖的最佳选择，减少了近亲繁殖或遗传变异过少的机会。家庭特别为自己提供道德和情感支持，更有可能彼此互动，并且天生更善于参与社区。更重要的是，如果我们的定居点有儿童，家庭绝对有必要作为社会的基本支持网络。

- 参考答案：原文未提供标准答案，以下为基于文本内容的梳理。
- 参考解答：
    1. **性别比例最优性**：男女50-50比例最大化生殖潜力。
    2. **一夫一妻制假设下的优化**：在单配偶制下，等量男女能最大化配对数量和生殖可能性。
    3. **年龄结构均衡**：各年龄段男女比例应均衡，避免结构性失衡影响婚配和繁衍。
    4. **文化与社会稳定**：性别均匀分布有助于避免极端父权或社会等级冲突，维持社会稳定。
    5. **家庭功能**：家庭提供情感支持，减少近亲繁殖风险，促进社区互动，是儿童成长的基本支持网络。
- 知识点：种群动力学, 社会结构建模

知识点：[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)

### 简答 4

这个社会中农民的数量似乎很高，因为该职业约占劳动力的40.81%。然而，优先考虑社会的各种需求，人们可以很容易地理解为什么食品和营养安全是最重要的。为了在一个如此偏远和荒凉的星球上生存，距离可持续农业增长的最接近能力在地球上至少3300万英里之外（Redd），人类需要一个可持续的食物来源。考虑到水稀缺，火星的土壤和大气本身不适合长期的农业增长，大规模农业社区对于人口的生存乃至其长期的可扩展性是必要的。

同样，公共健康和医疗部门员工的数量可能看起来很高，因为我们社区中约38.13%的工作属于该部门。然而，在农业之后，对社区生存和可持续性最重要的是健康和社会福祉。在一个对外星生物和心理挑战毫无经验的外星环境中，必须优先发展公共卫生和医学，以确保社区随着时间的推移能够持续和增长。除了农业、医学和公共卫生外，这个社区中的所有工作都是可有可无的。即使研究是火星社区的关键次要目标，它也在可持续生存和增长的主要目标之后。同时，像卫生和建筑等行业的人力投入可能看起来很低，但考虑到增强单元和人工智能在这些行业中迅速融合，到2100年，大多数这些工作应该实现自动化。

- 参考答案：原文未提供标准答案，以下为基于文本内容的梳理。
- 参考解答：
    1. **农业高占比原因**：占劳动力40.81%，因火星环境恶劣（缺水、土壤大气不适耕种），距地球遥远（3300万英里），必须建立大规模可持续农业以保障生存。
    2. **医疗高占比原因**：占就业38.13%，因火星环境未知，存在生物和心理挑战，公共卫生和医学是继农业后的第二大生存关键。
    3. **其他行业地位**：除农业、医疗、公共卫生外，其他工作相对次要。研究虽重要但次于生存。
    4. **低人力行业预期**：卫生和建筑行业人力少，因预计2100年自动化技术（增强单元、AI）将普及，大部分工作将由机器完成。
- 知识点：资源约束建模, 技术替代效应

## 二、成功社会的因素

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 3.1 问题重述

（此处为章节标题，无具体题目内容）

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)

### 3.2 假设

1. 家庭规模在各职业中标准化。例如，农民家庭中子女的数量占working farmer population的比例，与全社会子女数量占总人口的比例相同。

2. 性别在各职业中标准化。例如，使用社会中最佳的男女50-50分割，对于每一个男性研究人员，都有一个女性研究人员。除了作为性别平等和工作场所平衡的最佳结果外，这种分割在2100年之前对于大多数职业来说也可能是可实现的。

3. 在收入模型的背景下，对于已婚夫妇所生的每个孩子，每个配偶在经济上照顾 $\frac { 1 } { 2 }$ 个孩子。这相当具有代表性，反映了现实世界的家庭护理，因为每个父母都被期望平等地贡献于照顾孩子。

- 参考答案：原文未提供标准答案，以下为基于文本内容的梳理。
- 参考解答：
    1. **家庭规模标准化假设**：各职业家庭的子女比例与社会整体子女比例一致。简化了不同职业间家庭结构的差异。
    2. **性别分布标准化假设**：各职业内部男女比例均为1:1。基于社会整体性别平衡假设，并认为2100年可实现此平衡。
    3. **育儿经济责任均分假设**：在收入模型中，已婚夫妇的育儿经济负担由双方各承担50%。反映现实世界中父母平等分担育儿成本的趋势。
- 知识点：模型假设, 人口统计建模

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）

## 3.3 Developing the Models

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 3.3.1 Education

In this section, we create a model for the colony’s productivity as a function of number of years of schooling as well as a model for an individual’s utility to society as a function of their educational history. In addition, we will look at the equilibrium population of the colony in order to determine the average years of schooling children in the colony should receive in order for the colony to be self-sufficient. Two of the key elements of a successful society on Mars are self-sufficiency and happiness. By reducing unemployment among individuals between 18 and 24, overall happiness, one of the key metrics we’ve identified in this society, increases. Using EU-28 census data from 2013, we’ve established a negative correlation between unemployment among young people and happiness (“Quality of Life”).

Since we want to minimize unemployment, young individuals should either be in the workforce or in school. Since there is an established optimal ratio in the society for skilled to unskilled labor, this negative correlation means that education should be a primary emphasis for young people if they do not want to join the workforce or there are no available jobs.

Now we will model the value of an education based off of the relationship between Average Number of Years in School and GDP per capita. Using data from Barro-Lee’s study on average years in education by country and from the World Bank to get GDP per capita we’ve established two possible fits for the relationship between education and GDP per capita (Barro, ”GDP Per Capita”).

Using a linear model fit we get an R-Squared of 0.27. We also get an R-squared of 0.27 using a quadratic fit. In addition, when using the Akaike information criterion (AIC) we get 2710 for both fits. Therefore, we will use both fits to establish a range of possible GDP’s per capita for a given education level within the colony.

Now that we have models to predict GDP per capita for a given education level, we should enact an education policy which maximizes happiness and overall utility to society. In most countries, child labor laws require that agricultural workers must be at least 14 years old. Therefore, all students should be educated at least 9 years in general education. In an equilibrium population for the colony of 18161 individuals, 60% will be in the workforce. Using our previous population analysis, we see that approximately 11264 individuals will be between the ages of 16 and 65 and eligible to work. Since only 10800 of these individuals need jobs, approximately 464 students will be funneled in higher education after general education is over. In addition, each year, there is a demand of 120 skilled jobs due to existing workers retiring or dying. Therefore, on average, students in university spend 3.87 years in university before entering the workforce. Taking the average of students who only do general education and those who enter higher learning, the average student spends 11.02 years in the society’s education system.

Therefore, the educational system of 9 years of general education and approximately 3.87 years in university for skilled laborers allows for a society with minimal unemployment and enough skilled laborers graduating from university each year to maintain self-sufficiency in labor and education.

As Education relates to the other parameter of Income, this model’s conservative linear projection predicts that in a workforce with 6000 workers, we expect a GDP of 289.613 million dollars for the society.

知识点：[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)

### 3.3.2 Income

As a result of its largely federally run economy, much tax revenue would have to be generated to pay for public sector workers wages and government programs. This could come from an income tax on all members of society.

In order to maximize the income effect, a balance between efficiency and equality must be established in the economy. Incentives should not be blurred to the point of significantly harming the GDP, but at the same time, a fair distribution of wealth must be in place so that all people can afford the basic necessities of life. These necessities primarily include food and clothing, since housing will be provided by augmentation units such as large-scale 3D printers (Messier,Brachmann). Whereas GDP will be the metric used to evaluate the economy’s efficiency, we will use the Gini coefficient as a proxy for income equality–and, therefore, for the ability of all to afford fundamental necessities. We calculate GDP as follows:

$$
GDP = C + I + G + NX
$$

where $C$ = Gross private consumption expenditures, $I$ = Gross private investment, $G$ = Government spending, and $NX$ = Net exports. Because Population Zero is self-sufficient and unable to sustainably trade on a large scale with populations on Earth, $NX = 0$.

Government salaries will be standardized in the form of the following tiers for different jobs:

- A. Research
- B. Public Health, Education
- C. Sanitation, Law Enforcement

Suppose we awarded people in tier A with a salary of $a$, people in tier B with a salary of $b$, and people in tier C with a salary of $c$, where $a \geq b \geq c$. In addition, let us suppose that individuals in private industries (i.e. commerce/retail and farming) have an average salary of $c$, since their wage ranges on Earth are most similar to the salaries of the types of public sector jobs in tier C.

There are 2400 farmers in our community, and together, they have to provide at least 2,000,000 kcal per day to the community. The government will regulate the average farm size to be at least 4.9 acres (to ensure that there is enough food for the population at the minimum of 2000 kcal/day/person). Most private consumption of goods will come in the arena of agriculture.

## 3.3.2 Economic Model

Under the assumption that family size is standardized across all professions (6000 adults, 4000 kids), the average farmer will have approximately $\frac{4}{3}$ children along with his/her spouse (spouses will have their own occupations and sources of income). Since the spouse is also working, the farmer will essentially have to provide for himself/herself and $\frac{2}{3}$ children (spouse essentially provides for himself/herself and $\frac{2}{3}$ children).

Suppose that people in tier A are willing to purchase $(2000 + \frac{a}{a} * 700)$ kcal/day/person on average at the equilibrium price $p$ USD/kcal. Let us assume that people in tier B are willing to purchase $(2000 + \frac{b}{a} * 700)$ kcal/day/person on average and that people in tier C are willing to purchase $(2000 + \frac{\overline{c}}{a} * 700)$ kcal/day/person on average. Assuming that price discrimination is not an option, one fee in this competitive market will be established by market forces. Again, under the assumption that family size is standardized, a person in each tier will provide for himself/herself and $\frac{2}{3}$ kids.

Total demand $\left( \mathrm { k c a l / d a y } \right) = (\# \text{ in A}) \left(1 + \frac{2}{3} \text{ kids}\right) \left(\left(2000 + \frac{a}{a} * 700\right) \text{ kcal/day/person}\right) + (\# \text{ in B}) \left(1 + \frac{2}{3} \text{ kids}\right) \left(\left(2000 + \frac{b}{a} * 700\right) \text{ kcal/day/person}\right) + (\# \text{ farmers}) \left(1 + \frac{2}{3} \text{ kids}\right) \left(\left(2000 + \frac{c}{a} * 700\right) \text{ kcal/day/person}\right)$

Thus:
$$ \text{Total demand} = (\#\text{research}) \left(\frac{5}{3}\right)(2700) + (\#\text{health \& teachers}) \left(\frac{5}{3}\right)\left(2000 + \frac{b}{a} * 700\right) + (\#\text{sanitlawenfor \& commerce/retail \& farmers}) \left(\frac{5}{3}\right) \left(2000 + \frac{c}{a} * 700\right) $$

Varying the values for $a$, $b$, and $c$, we can come up with interesting simulations that give us a glimpse into both the GDP and the Gini coefficient.

Trying a variety of possibilities, we found that the optimal combination of salaries was modeled off of U.S. data on current average private sector salaries for the types of workers in each tier. We set government worker salaries in tiers A, B, and C to be 65% of their average private sector salaries in their U.S., which were \$76,961, \$62,610, \$38,862 (Lunney). Ultimately, the public sector salaries for tiers A, B, and C were \$50,024.7, \$40,696.5, \$25,260.3, respectively. Farmers and commerce/retail workers earned \$38,862, meanwhile.

Looking at GDP, in terms of private investment, no forms of fixed investment on capital would exist since the government is regulating all services. In addition, since the core mission of inhabitants of this colony is to survive rather than generate personal wealth, investment in goods such as agricultural surpluses and clothing would not be a significant venture in the first years of the colony. Thus, private investment is negligible at the start of the colony. Government spending comes in the form of wages and a variety of intuitive forms of publicly funded programs: RD, education, and public sector wages. The U.S. spends \$1442.51 per capita on RD; translating that over to our population of 10,000 ppl, the costs there amount to \$14.4251 million ("List of Countries"). The U.S. also spends \$11,700 per student on education ("Education Expenditures"), so for our education model’s prediction of 2800 students, the costs there amount to \$37.44 million. Based on our values for salaries, public sector wages come out to \$179.666 million.

Private consumption includes the amount spent on food and the amount spent on healthcare (government funding of healthcare is a transfer payment to private citizens, so healthcare costs come under private consumption). The global average for healthcare per capita spending is \$3800 ("Health Resources"). These two avenues of spending come out to \$109.066 million. Since GDP is the sum of government spending and private spending, this yields us a GDP of \$288.732 million. Clear support for the accuracy of this value is the fact that the education model predicts an extremely close value of \$289.613 million for our society of 10,000.

We can next turn to the Gini coefficient value; based on our wages for our various public and private sector jobs, we computed a Gini coefficient value of 0.0335591. This value is very small compared to those of countries on Earth; the lowest Gini value among contemporary countries with sufficient data is 0.237 ("Country Comparison"). However, our society’s low Gini coefficient makes sense in the context of the small size of our population and workforce, the fact that wages are standardized within tiers, and the knowledge that most industries are government controlled–the tax rate, equal to government spending over total income, comes out to 73.64%, indicating a highly publicly controlled economy. This combination of high GDP (our per capita GDP of \$28,873.2 ranks in the 76th percentile of contemporary nations’ GDP) and extremely low inequality is indicative of a very successful settlement venture based on income and economic standards.

知识点：[TOPSIS 模型构建步骤（逼近理想解排序法）](../../../topics/数学建模/topsis_moxing.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[符号说明与术语定义（Nomenclature / Symbols and Definitions）](../../../topics/数学建模/fuhao_shuoming.md)

### 3.3.3 Equality

We simplify the issue of equality into the following three categories: income equality, gender equality, and racial equality. There are definitely [other issues such as] religious equality. We note that religious equality and homosexual equality can be modeled in a similar way to racial equality, as we can simplify these issues down to an affinity towards similar people. Thus, we will focus our efforts on modeling racial equality, and this model is flexible enough to understand religious and sexuality as well. As we already discussed income inequality in the section above, we will focus on racial and gender equality in this section.

知识点：[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 3.3.4 Racial Equality

Racial inequalities are systemic issues that are difficult to tackle. Such inequalities may arise due to homophily in human social networks, the studied phenomenon that individuals are more likely to forge social connections with those that are most similar to themselves (Smith et. al.).

We simplify the population down to five major races: Black, Caucasian, Asian, Hispanic, and Middle Eastern. Then we simulated a population of individuals as they entered careers, possibly switch careers, and retire over time. To model the changes in the job distributions over time, we approximated that about 5% of the workforce would take on a first job, switch careers, or retire during one year. This accounts for the new graduates joining the workforce and the 67-year-olds retiring each year, as well as a small amount of people allowed to change jobs, which would be discouraged due to training costs.

To simulate these changes, we used a Markov-chain model where each individual is assigned a race and an initial job. At each time step, this individual has a 5% chance of leaving the workforce.

Now, for each of these individuals that will change jobs every year, they will be influenced by a homophily factor that makes jobs with a higher percentage of people in their respective racial category. We chose a homophily factor of $1.2$, which is lower than extreme factors seen in the data (Smith et. al.). For example there is a $0.387$ chance that blacks and whites will become friends by chance, but only a $.098$ reported value in today’s society (Smith et. al.). We estimate that homophily will significantly decrease on Mars, as individuals new Martian identity will serve to unify the population, thereby reducing racial bias. Furthermore, a small population will likely force individuals to marry individuals of other races, which will eventually serve to blur racial lines.

Using this value for homophily, we weight the individuals decision to choose one of the other two jobs using the ratio of his or her race to the other races in those jobs, scaling the higher job ratio by our homophily factor.

We choose a traditional metric to measure segregation levels between races in different jobs. Dissimilarity is a measure that simulates how many individuals would have to change jobs in order to have a perfectly equal and unsegregated society. Dissimilarity is measured between $0$ and $1$, where a dissimilarity value of $0$ indicates perfect equality and a dissimilarity value of $1$ indicates total segregation. We calculate the dissimilarity, $D$, of races A and B as

$$
\frac {1}{2} \sum_ {j \in J} \left| \frac {a _ {j}}{a} - \frac {b _ {j}}{b} \right|
$$

where $J$ is the set of distinct jobs, $a$ and $b$ are the sizes of the populations of races A and B, respectively, and $a _ { j }$ and $b _ { j }$ are the number of individuals in job $j$ that belong to races A and B, respectively.

Now we wish to identify causes of increased dissimilarity. When all three tiers of income are equal, we see this income model is less than ideal. Looking at Figure 3, we see that dissimilarity increases over time, as individuals choosing jobs are influenced not by salaries, but by interests and personal network connections only.

Our sources show that a way to prevent these negative changes to the colony's equality is to have significant variations in salaries. These price differences incentivize individuals to seek the highest level job they are qualified for, hopefully overriding the individuals tendencies to seek others most similar to themselves.

Thus, we use the salary model from Part 3 that was also successful. These salaries were: `[50024.7, 40696.5, 38000]`

We then adjust the simulation so that each individual is influenced to enter a career by two factors: the homophily factor from before and also the salary of each job. We see that when people are incentivized to earn a higher salary, they are more likely to choose a higher-paying career, even if they have fewer contacts in that particular field.

However, looking at the results of the simulation, we see that this solution does not result in complete equality, as those who have more contacts in the highest paying fields have an easier time entering that field, creating a barrier for individuals or. However, the dissimilarity rates are considerably improved in this scenario, so we adopt this model of income stratification.

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[随机模型与确定性模型的对比（Stochastic vs Deterministic Model）](../../../topics/数学建模/suiji_queding.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)

### 3.3.5 Gender Equality

To combat gender inequalities, our primary goal is to allow for women of working age to give birth to children without leaving the workforce entirely. Proposals often advocate for a longer paid maternity leave, and optional paid paternity leaves in order to reduce the economic disadvantages of having a child. These policies are especially important, as we scaled the U.S. birth rate by a small parameter of $1.08$ in order to maintain a period of steady growth during the initial stages of our colony. In order to promote these birth rates, we propose a considerable paid leave of 6 months. Because we wish to emphasize both males and females as important caretakers of children, we allow both the father and the mother to take leave, provided that their combined leave duration does not exceed 6 months. As mentioned in Part 2, having almost 50 extra farmers accounts for the time taken off by farmers due to parental leave and allows our society to still have enough food to be sustained.

This is a component of the model that will require repeated evaluation. Ideally, the ability to distribute child care leave evenly between both parents would be sufficient to combat gender inequalities in the workforce. However, persistent bias and stereotypes that men should work more than women may arise on Mars as well. In order to combat such potential obstacles to gender equality, frequent evaluation will be necessary by looking at the changes in dissimilarity between men and women. We notice in the simulations of Section 3.3.4 that significant changes to the dissimilarities arose simply due to each persons’ natural tendencies to interact better with those whom they have much in common. Due to these factors, and the common association of women with childcare, we see that we will need to monitor dissimilarity and may need to enact government policies that require fathers to be more involved in child care, for example.

## 4 Forming a Global Model

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 4.1 Restatement of the Problem

Task 4 asks us to do the following:

1. Create a single model from our individual models from task 3.

2. Consider the main priorities in the lives of major portions and demographics of Population Zero.

3. Explore the impact of our model on these different subgroups based on their major priorities.

4. Adjust the model if necessary to optimize the priorities of different subgroups without significantly downgrading global outcomes.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[多目标优化模型（药物相对充足阶段的配送策略）](../../../topics/数学建模/duo_mubiao_youhua.md)

### 4.2 Assumptions and Justifications

知识点：[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 4.3 Developing the Model

Our three models–for income, education, and equality–are highly interdependent and interrelated. Strong education levels are correlated with greater economic efficiency, and there are various relationships between equality and both education and income. In order to merge our three models into one, we need to first consider what these three together can tell us. The task asks us to assess optimal outcomes for society and various subgroups. One way to do so is to create a happiness index based on the major priority areas in society.

We established four basic areas of priority critical to determining the happiness of an individual in the context of society. They are education, economic efficiency, economic equality, and social equality. In order to quantitatively measure the extent of achievement in or fulfilment of each of these priority areas, we based our proxies on appropriate metrics. For education, we used years of education. For economic equality, we used the Gini coefficient. For economic efficiency, we used the GDP, and for social equality, we used the dissimilarity metric. In order to standardize each of these metrics to the same 0-to-1 scale, we set the education fulfillment variable equal to $N_{years}/44$. We chose 44 based off Mincer's famous model (Stearns) that predicted a positive marginal benefit of education for up to 44 years. We then computed the efficiency fulfillment proxy by finding where on the distribution of national GDP per capitas on Earth our colony's GDP per capita would lie. In formal terms:

$$
GDPproxy = CDF[dist, GDP_{PopZero}]
$$

Next, we evaluated the economic equality proxy by the following, since we wished 1 to be an indication of optimal equality and 0 to be an indication of perfect inequality:

$$
eeproxy = 1 - gini
$$

Finally, we calculated the social equality proxy by using the harmonic mean $H$ of the various dissimilarity values $D_1$ through $D_5$, since any sort of inequality in the system should skew the distribution more in its direction to reflect a negative social outcome (one right doesn't correct a wrong!):

$$
seproxy = H(1 - D_1, 1 - D_2, 1 - D_3, 1 - D_4, 1 - D_5)
$$

Now that we have established these four priority areas as the backbone of the universal model, we need to form a way to compute happiness index from these four. Realizing that the importance of each of these priorities varies across the different subgroups, we assign weights to each of these to evaluate how much importance each one holds in the eye of the average individual of each subgroup. Using these weights and the standardized priority metrics, we can define the happiness index as follows:

$$
H = (w_{edu} \times N_{years}) + (w_{gdp} \times GDPproxy) + (w_{ee} \times eeproxy) + (w_{se} \times seproxy)
$$

with the sum of the weights being equal to 1. For the priority metric values, we used our education's model optimal education length of 11.02 years, our calculated GDP percentile of 0.76754, our Gini coefficient of 0.0335591, and an $H$ value of 0.9287899. This provides us with a lens with which to view the total utility or satisfaction one develops from the various aspects of life in the community. In addition, by comparing the sets of weights of one subgroup to those of the next, one can understand how different groups prioritize the different aspects–education, economic efficiency, economic equality, social equality–of society. In order to come up with reasonable and empirically supported values for these weights, however, we have to make inferences from data.

The Pew Values Survey allows us to collect estimates and proxies for people's concern about the four major priority areas we defined (Gewurz). Based on the tier system of our economy, we look at the responses to these question from the top 10% of income earners to reflect the sentiments of our society's top 10% of income earners, scientific researchers. The next 40% of income earners' responses reflects the sentiments of our society's next 40% of earners, public health professionals and teachers, and the bottom half of income earners' responses reflects the sentiments of our society's bottom half of earners, farmers, commerce, law enforcement, and sanitation.

To estimate the relative value of the four priority categories on the three income levels, we looked at individuals response to the following questions:

1. Education: In making your decision about who to vote for this fall, will the issue of Education be very important, somewhat important, not too important, or not at all important?

2. Economic Efficiency: Do you agree completely, agree mostly, disagree mostly, or disagree completely with the statement, The strength of this country today is mostly based on the success of American business?

3. Economic Equality: Do you agree completely, agree mostly, disagree mostly, or disagree completely with the statement, The government should guarantee every citizen enough to eat and a place to sleep?

4. Social Equality: Do you agree completely, agree mostly, disagree mostly, or disagree completely with the statement, Our society should do what is necessary to make sure that everyone has an equal opportunity to succeed?

For these first question, we weight the responses as follows in Table 1.

Then we use the responses to compute an importance metric for each priority for all three income categories. Then, we normalized the importance values so that the sum of the importance values of all priorities is 1, so that we could compare the priorities of individuals across different economic levels. We obtained the following results, which are summarized in Table 2. Once we computed the weights of the different major income groups in our society, we were able to infer their various preferences. Public health employees and teachers, for example, in tier B were more concerned with education and economic efficiency, while farmers, law enforcement, sanitation, and commercial vendors in less lucrative positions were more concerned with economic and social equality.

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）习题

本部分整理了论文中关于权重分配、人口细分优先级分析以及模型验证和迁移测试的相关数据表格与分析内容。

## 一、权重与优先级分析

知识点：[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)、[人类发展指数 HDI 的局限性与社会经济调整指数的构建](../../../topics/数学建模/hdi_zhibiao.md)

### 简答 1

**题目：** 根据表1，总结受访者对各项指标重要性的权重评分标准。

- **参考解答：**
  表1展示了受访者对各项指标重要性的主观权重评分标准：
  
| Response | Weight |
| :--- | :--- |
| Very important, Agree completely | 3 |
| Somewhat important, Agree mostly | 2 |
| Not too important, Disagree mostly | 1 |
| Not at all important, Disagree completely | 0 |

- **补充：** 该权重体系用于量化不同社会群体对教育、经济效率、经济平等、社会平等和幸福指数的重视程度。

知识点：[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)、[层次分析法 AHP（Analytic Hierarchy Process）用于综合评价](../../../topics/数学建模/ahp_fangfa.md)

### 简答 2

**题目：** 根据表2，分析不同收入阶层在美国个体中的优先级分布情况。

- **参考解答：**
  表2展示了不同收入阶层的优先级权重分布：

| Income Category | Education | Economic Efficiency | Economic Equality | Social Equality | Happiness Index |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Top 10% of Incomes | 0.32088 | 0.21762 | 0.18632 | 0.27517 | 0.68305 |
| Middle Tier of Incomes | 0.32116 | 0.22734 | 0.17901 | 0.27248 | 0.68102 |
| Bottom 48% of Incomes | 0.31239 | 0.20817 | 0.19937 | 0.28008 | 0.69083 |

- **分析说明：**
  这些结果符合直觉。高收入工人通常技能更高、受教育程度更深且更专业化，因此他们更关心教育和市场中的金钱总量（经济效率），因为他们更有可能从这种效率提升中受益。与此同时，非熟练工人和贫困工人往往更关注社会问题和平等以及收入平等，因为他们在这些领域的进步中最有可能受益。

知识点：[层次分析法 AHP（Analytic Hierarchy Process）用于综合评价](../../../topics/数学建模/ahp_fangfa.md)、[可持续发展指数 SDI 的构建与指标体系结构](../../../topics/数学建模/kechixu_zhibiao.md)

### 简答 3

**题目：** 根据表3，分析基于性别和年龄的美国个体优先级差异。

- **参考解答：**
  表3展示了基于性别和年龄的社会类别的优先级权重：

| Social Category | Education | Economic Efficiency | Economic Equality | Social Equality | Happiness Index |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Men | 0.16150 | 0.27839 | 0.21994 | 0.34017 | 0.78263 |
| Women | 0.17490 | 0.24966 | 0.24356 | 0.33189 | 0.77907 |
| Working Adults | 0.16013 | 0.26150 | 0.24140 | 0.33697 | 0.78709 |
| Retired Adults | 0.19257 | 0.26768 | 0.20735 | 0.33240 | 0.76281 |

- **分析说明：**
  这些数据也揭示了一些有趣的趋势。例如，受访女性比男性更倾向于优先考虑收入平等。这并不令人惊讶，因为历史上女性在相同职位上的薪酬低于男性，因此女性可能认为收入平等是一个更重要的问题。出于同样的原因，女性可能比男性稍高地重视教育。受访的在职成年人对教育的兴趣低于退休成年人，这可能归因于一种普遍观点，即高等教育通常不直接应用于工作。然而，退休人员似乎更重视他们的教育，这可能是由于对他们影响的更高欣赏。值得注意的是，在职成年人比退休人士更看重收入平等，这符合直觉，因为他们目前领取工资，因此更意识到人口中的收入不平等。

知识点：[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)

### 简答 4

**题目：** 根据表4，分析在改变参数值（特别是社会经济权衡）后幸福指数的变化。

- **参考解答：**
  表4展示了在社会经济权衡前后各社会类别的幸福指数值：

| Social Category | Original | After EE/SE Tradeoff |
| :--- | :--- | :--- |
| Top 10% of Incomes | 0.683048 | 0.678462 |
| Middle Tier of Incomes | 0.681015 | 0.676289 |
| Bottom 48% of Incomes | 0.690827 | 0.686485 |
| Men | 0.782632 | 0.776614 |
| Women | 0.779065 | 0.774166 |
| Working Adults | 0.78709 | 0.781918 |
| Retired Adults | 0.762808 | 0.756674 |

- **分析说明：**
  我们尝试通过微调参数值来检查其对幸福指数的影响。例如，我们试图估算社会平等与收入平等之间的权衡：通过将工资标准化为同一值，从而使基尼系数降为0，我们观察到劳动力中的隔离现象加剧，因为工人选择与自己种族相同工作的倾向没有被任何薪资差异所抵消。此处的调和平均值降至0.8894。与原始幸福指数值相比，幸福指数随后下降。表4显示了这些权衡分析的结果。显然，原始值更可取，因为它们的幸福指数值更高。因此，我们决定保留原始值。

知识点：[敏感性分析方法（Sensitivity Analysis，单参数与多参数变动）](../../../topics/数学建模/minganxing_fenxi.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 简答 5

**题目：** 简述模型验证的方法及其合理性。

- **参考解答：**
  构建一个以未指定权重为中心的模型迫使我们使用真实世界的数据来提供合理的值。因此，与其为权重或个体对社会不同方面结果的优先级创建人为或编造的值，我们基于收入或人口统计学的各种子组的实证分析来提出智能且彻底的假设。此外，虽然我们为每个子组使用相同的优先领域，而不是为不同组创建不同的关切，但我们的模型的这一方面更像是一种优势而不是弱点，因为它允许我们以定量方式基于权重分析不同子组的优先级模式。此外，直觉结论遵循我们模型的结果：为什么女性如此重视收入平等和教育，以及为什么低收入工人比他们的高技能同行更关心经济和社会平等，这都是合理的。此外，结合直觉，基于加权模型的结果，我们可以推断出某些子组特别关注的更具体类别。例如，我们可以推断女性将特别优先考虑缩小性别工资差距，而农民接受的教育较少，专业化程度不如高技能工人，因此不像植物学家或医生那样深切关注教育。

知识点：[模型验证方法概述（随机模型与确定性模型验证）](../../../topics/数学建模/moxing_yanzheng.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)

### 简答 6

**题目：** 针对额外迁移情况，模型进行了哪些测试？

- **参考解答：**
  为了测试我们的模型对额外迁移的韧性，我们计划了几种不同的场景，并对火星社会的人口和经济进行了分析。

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）

## 五、情景分析

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)

### 5.1 Scenario 1: A One-time Migration

The first scenario is a one-time migration of 10,000 individuals much like the initial settlers on the colony. In this scenario, we make several assumptions such as the existence of infrastructure and jobs for migrants once they join the colony. In addition, it is assumed that government can initially support all new migrants economically because they will be working immediately. Using population analysis, it is shown that an equilibrium population to which 10,000 migrants of the same demographics as the initial settlers will reach a new equilibrium and not collapse.

知识点：[传统 SEIR 流行病模型（Susceptible-Exposed-Infectious-Recovered）](../../../topics/数学建模/seir_moxing.md)、[确定模型的定点与稳定性分析](../../../topics/数学建模/dingdian_wending.md)、[人口密度修正系数与新公式](../../../topics/数学建模/renkou_midu.md)

### 5.2 Scenario 2: A Separate City

Now, if we add 10,000 people to a separate city, we can make some assumptions in order to e↵ectively model the two separate populations. Since our model works for a 10,000 individual population we can assume a similar model for the second city (which we will call Society 2) has some benefits during its development compared to Society 1. For instance, we can assume that the average educational level will be higher than Society 1 at a similar population and consequently according to the positive relationship between education and GDP per capita Society 2 will be more prosperous than the original Martian society at corresponding stages of development. Let us presume that 10 years have passed for Society 1. The average annual GDP growth rate over the last ten years is about 3.5% (Data World Bank). Based on that, over the next ten years, the economy should grow 41.06%. Given this substantial growth on Earth, the new colonists will be more advanced as a result of progress in education, technology, and other areas that influence GDP. As a result, their society will have a higher GDP than the first society.

As a result of higher education, GDP, and specialization, Society 2 will likely exhibit a comparative advantage in some industries, goods, or services. As a result, trade patterns will likely develop between the two communities, allowing both to benefit through simple free market economics. Thus, having a separate city that develops trading patterns but that falls under its own jurisdiction and independent government theoretically can only have positive results. Unlike Scenario 1, there are no negative pressures on Society 1 because Society 2 follows the same model of self-su ciency. Therefore, the model for both societies are incredibly robust to additional cities.

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)、[有效性参数（Effectiveness Parameter）与搜索模式对比](../../../topics/数学建模/youxiaoxing_canshu.md)

### 5.3 Scenario 3: Gradual Migration

Our third scenario involves the gradual migration of individuals from Earth over 100 years. In this scenario, our simulations showed that the population quickly adjusts to gradual influx of people as shown in the following figure. It takes approximately 30 years for the population to reach a maximum due to the migration of adults and after that the population lowers until it reaches an equilibrium.

As a result, the optimal gradual migration pattern would allow the population to reach equilibrium, about 50 years after the addition of the migrant population, before the next wave of migrants. Alternatively, the next wave of migrants could likely enter society after 30 years, when the population was starting to lower to its equilibrium value.

## 六、Evacuating Planet Earth

In this scenario we attempt to maximize the number of people from Earth who can be saved while keeping the parameters defined previously in the problem in mind. There are several limiting factors which limit the number of migrants from Earth. Looking first at government spending, we calculate that the current goverment spending can support up to 8304 migrants from Earth given no warning and no time to change the current rates of government spending. This number comes from the calculation of the minimum amount government must spend per capita on a migrant ($7745.5$) from our earlier economic model. This means a population of $10,000$ could support another $80\%$ of its weight given a sudden migration from Earth from an economic government perspective. Another factor to consider would be the increased tax in order to support migrants. The taxation rate of $73\%$ indicates that in order to support an additional $80\%$ of the population government would need to subsidize many other aspects of citizen’s lives such as the goods they consume in order for individuals to be able to a↵ord goods with such a high taxation rate. In addition, another limiting factor is food consumption. Currently, farmers work $8$ hour workdays. If the population grows by $83\%$, then they must work $14.6$ hour days if it is assumed that they have enough land to grow an increased number of crops.

Overall, unexpected migration places a huge burden on the existing society and many parameters such as the lack of unemployment would no longer work. As with any large scale migration, unemployment would go up as the number of jobs could not grow like population does.

# 2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）

## 习题

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)

### 简答 12

Dear Director,

Upon the request of the International Coalition of Mars, our team has devised an empirically and quantitatively supported model that makes allows us to make various policy recommendations centered on the expected income, education, and equality aspects of Population Zero’s settlement.

First, we recommend a balance between student-age and working-age colonists in the initial group of colonists. Specifically, we believe a 40-60 breakdown of children/students and workingage adults, respectively, in family units will maximize the potential for growth and economic development in the community because it includes enough working-age adults to support the large student population financially, in terms of food, and in terms of family-based moral and emotional support. Also, though some may envision that a society highly focused on breeding and population expansion represents humanity’s best chance for survival and growth on another planet, our group disagrees with that notion. Family support is critical for wellbeing and survival on the remote Red Planet, and an explosion of young people in our population is not at all sustainable in the long run. Steady and stable population expansion has been shown by our growth models to create a successful and sustainable society, in terms of age and occupation distribution, in the long run.

In addition, we suggest that Population Zero set a cuto↵ age of 40 for eligibility; one must be at most 40 years old in order to be eligible to come to Mars. We make this recommendation based on the idea that we wish for every colonist to be able to contribute for as long as possible. In the first generation of settlers in particular, we wish to establish the roots for long-term sustainability and growth, and we can only ensure that if every person is able to contribute for a long enough period of time to support the generation going through education. Moreover, we believe that an even gender split (50-50 between males and females) and as diverse a population racially and genetically would be optimal for healthy levels of genetic variation and reproduction as well as issues such as social and income equality. Having a society dominated by any one racial or gender group would not be a good idea in terms of either the long-term sustainability of the population or the degree of egalitarianism in society.

We also recommend that LIFE plan for Population Zero to be composed of 25% farmers and 23% public health and medical sector professionals. Though these values may seem appalling at first glance, we wish to advise the agency to consider that food and health are the cornerstones of any hope for long-term sustainability and success of the colony. Considering that agriculture and health on Mars are not tested in long-term scenarios, the colony will certainly need an emphasis on these two areas.

Next, looking at issues of governance and economy, we recommend that the colony on Mars establish a system in which the government regulates most industries. In particular, we recommend that the government handle the operations of all service-based industries, with goods-based industries in private hands. We are convinced that such a breakdown is optimal, as the relatively small size of the society allows the government to control important industries like research and health without encountering the problems of most large-scale communist societies. Additionally, we urge the government on Mars to set salaries for public-sector workers to be increasing as the level of skill necessary for a job goes up. While minor income discrepancies will ensue–public-sector salaries modeled o↵ average Americans wages for related job areas yields a tiny Gini value of 0.0336–we predict that creating complete income equality is a poor idea, for our model reveals that doing so not only decreases motivation to become educated and highly skilled but also increases the amount of self-selecting segregation in workforce industries on various demographic levels such as race. The state of the tradeo↵ between income equality and social equality is clearly in favor of allowing a little economic inequality in order to ensure

## 结论与建议

为了扩大社会平等，我们主张为每位新父母提供共计 6 个月的带薪育儿假，这是实现更大性别平等的直接途径。我们希望这一政策不仅能促进社会中男女之间的更多平等，还能鼓励夫妇提高出生率。我们的模型预测，在殖民地初期保持稳定增长的关键在于出生率增长 8%。通过为夫妇生育子女提供保障，我们旨在确保殖民地的稳定增长。

我们的教育模型预测，平均最优的教育年限为 11 年。这一数值处于地球上各国义务教育年限的最高水平之列；然而，鉴于我们社会中约有一半人口是高技能和高学历人群（教师、医疗和公共卫生专业人员、研究人员），这一数值是合理的。我们倡导所有学生接受 9 年的通识教育，因为生活在这样一个技术和科学高度发达且导向明确的社会中，要求具备掌握火星任务关键概念所需的足够熟练度。在 9 年通识教育之上，准备进入高技能岗位的学生应接受约 4 年的专门教育，以使其为社会角色做好准备。

关于未来移民对该殖民地的影响，由于具有可扩展性，我们的模型对任何类型的计划移民都是稳健的。我们接受高达 10,000 人的一次性移民，以及姐妹城市的建设或从地球逐步接收成年人。总体而言，我们的模型显示，拥有这些移民的人口随时间推移达到了平衡状态，从未崩溃。

最后，我们的政策建议试图在地球面临即将到来的彗星撞击的情况下，最大化可挽救的人数。虽然我们估计可以挽救 8300 人，但这只是一个上限，在这种情况下，政府可能不得不削减之前概述的该社会的一些参数。不过，总体而言，我们的模型允许我们从地球按比例增加大量移民至当前社会人口。

我们相信，我们的政策建议是有效的且符合实证标准的，尤其是在前所未有的任务背景下尤为有力。希望您也认为如此。很高兴能协助 LIFE 规划这次人类历史上不可思议的远征。如有任何问题或疑虑，请随时联系我们。

此致，

Team 72283

## 参考文献

[1] "About MDRS." Mars Desert Research Station. Mars Society, n.d. Web. 23 Jan. 2017.

[2] Agriculture and Consumer Protection. "Roots, Tubers, Plantains and Bananas in Human Nutrition." Roots, Tubers, Plantains and Bananas in Human Nutrition - Nutritive Value. Food and Agriculture Organization of the United Nations, n.d. Web. 23 Jan. 2017.

[3] Barro, Robert and Jong-Wha Lee, 2013, "A New Data Set of Educational Attainment in the World, 1950-2010." Journal of Development Economics, vol 104, pp.184-198.

[4] Bish, Joseph J. "Population Growth in Africa: Grasping the Scale of the Challenge." The Guardian. Guardian News and Media, 11 Jan. 2016. Web. 23 Jan. 2017.

[5] Brachmann, Steve. "NASA Is Seeking Answers for Growing Plants, Constructing Buildings on Mars." IPWatchdog. IPWatchdog, Inc., 04 Nov. 2015. Web. 23 Jan. 2017.

[6] Bradford, Jason. "One Acre Feeds a Person." Farmland LP. Vital Farmland Holdings, 13 Jan. 2012. Web. 23 Jan. 2017.

[7] "Country Comparison - Distribution of Family Income." Central Intelligence Agency. Central Intelligence Agency, n.d. Web. 23 Jan. 2017.

[8] Daily Mail Reporter. "Pull the Other One: Women Call in Sick More Often, but Men Are More Likely to Skip Work as Soon as They Start Feeling Ill." Daily Mail Online. Associated Newspapers, 25 May 2011. Web. 23 Jan. 2017.

[9] "Education Expenditures by Country." The Condition of Education. National Center for Education Statistics, May 2016. Web. 23 Jan. 2017.

[10] "Faculty Teaching Load." Grambling State University - Academics. Grambling State University, n.d. Web. 23 Jan. 2017.

[11] "GDP per Capita (current US$)." Data World Bank. Data World Bank, n.d. Web. 23 Jan. 2017.

[12] Gewurz, Danielle. "April 2012 Values Survey." Pew Research Center for the People and the Press. N.p., 15 Apr. 2012. Web. 23 Jan. 2017.

[13] Grayson, Wayne. "AI, Robotics Expected to Claim Nearly 500,000 Construction Jobs by 2020." Equipment World. Randall Reilly, 25 Jan. 2016. Web. 23 Jan. 2017.

[14] "Health Resources - Health Spending - OECD Data." OECD Data. OECD, 2015. Web. 23 Jan. 2017.

[15] Leij, Marco Juri Van Der, and Sebastian I. Buhai. "A Social Network Analysis of Occupational Segregation." SSRN Electronic Journal (n.d.): n. pag. Sebastian Buhai. Oct. 2014. Web. 23 Jan. 2017.

[16] "List of Countries by Research and Development Spending." Wikipedia. Wikimedia Foundation, n.d. Web. 23 Jan. 2017.

[17] Lunney, Kellie. "Public-Private Sector Pay Gap Remains at 35 Percent." Government Executive. National Journal Group, n.d. Web. 23 Jan. 2017.

这是一份参考文献列表，属于论文末尾的参考资料部分。根据格式规范，由于没有具体的“题目”或“章节”结构，而是连续的引用条目，我们将其整理为“参考资料”章节下的列表项。

注意：
1. 原文中的 `Je↵` 是识别错误，应为 `Jeff`。
2. 原文中的 `O ce` 是识别错误，应为 `Office`。
3. 页眉页脚（Team #, Page info）已去除。
4. 由于这是参考文献列表，不符合“习题/试卷”的结构化格式（无题干、选项、答案），但为了保持资料完整性，按规范整理为纯文本列表，并修正明显的OCR错误。

# 《2017年美国大学生数学建模竞赛F题O奖论文（Population Zero）》参考文献

本部分整理了原论文第 25–25 页（共 24 页，此处可能为附录或参考文献页码标注差异，内容确认为参考文献）的参考文献列表。由识别工具读出后，修正了明显的字符识别错误（如 `Je↵` 改为 `Jeff`，`O ce` 改为 `Office`）。

## 参考文献

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[非技术性文稿撰写（如致世界医学会的信函、新闻发布会声明）](../../../topics/数学建模/fei_jishu_wengao.md)、[一般假设及其合理性说明（Assumptions and Justifications）](../../../topics/数学建模/jiaben_shezhi.md)

### 参考 18

Messier, Doug. ”PISCES Embarks on Lunar Concrete Development Project.” Parabolic Arc. Parabolic Arc, 31 May 2014. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 参考 19

National Center for Disease Statistics. Birth Rates 2015. 29 Sep. 2015. Raw data. National Vitals Statistics System, Atlanta, GA.

知识点：[长期预测模型（如20年可持续发展计划预测）](../../../topics/数学建模/nian_yuce.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[模型优缺点分析（Strengths and Weaknesses）](../../../topics/数学建模/youque_dian.md)

### 参考 20

National Center for Disease Statistics. Death Rates by 10-Year Age Groups: United States and Each State, 1999-2007. 10 Feb. 2012. Raw data. National Vitals Statistics System, Atlanta, GA.

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 参考 21

”New York City Department of Sanitation.” Wikipedia. Wikimedia Foundation, n.d. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 参考 22

Pingali, Prabhu L., and Robert E. Evenson. ”Farm Rights.” Handbook of Agricultural Economics. Amsterdam: Elsevier, 2010. N. pag. Print.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 23

”Quality of Life Indicators - Education.” Eurostat: Statistics Explained. N.p., n.d. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 24

Reaves, Brian A. ”Local Police Departments, 2013: Personnel, Policies, And Practices.” Bureau of Justice Statistics. Bureau of Justice Statistics (BJS), 14 May 2015. Web. 23 Jan. 2017.

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 25

Redd, Nola Taylor. ”How Long Does It Take to Get to Mars?” Space.com. Purch, 13 Feb. 2014. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[任务分解与目标明确](../../../topics/数学建模/renwu_fenjie.md)

### 参考 26

Renoe, Jeff. ”Get Up and Grow: Part One in a Series on Farming in Extreme Environments.” Dickson. Dickson, 27 Oct. 2016. Web.

知识点：[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)、[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)

### 参考 27

S. C. ”One Billion Workers.” The Economist. The Economist Newspaper, 23 Jan. 2012. Web.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[问题重述与分析（Problem Restatement and Analysis）](../../../topics/数学建模/wenti_chongshu.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)

### 参考 28

Smith, Jeffrey A., Miller McPherson, and Lynn Smith-Lovin. ”Social Distance in the United States: Sex, Race, Religion, Age, and Education Homophily among Confidants, 1985 to 2004.” DigitalCommons@University of Nebraska - Lincoln. University of Nebraska, 24 Apr. 2014. Web.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 29

Starr, Michelle. ”Leaf on Mars: Can NASA Grow a Garden on the Red Planet?” CNET. CNET, 26 Oct. 2015. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 30

Stearns, Jenna. ”Estimating Marginal Returns to Education.” Encyclopedia of Quality of Life and Well-Being Research (2014): 1631. University of California - Santa Barbara. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 31

”Travel Abroad In-Depth Report.” New York Times. New York Times, n.d. Web. 23 Jan. 2017.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)

### 参考 32

U.S. Census Bureau. American Community Survey 2015. 20 Oct. 2016. Raw data. American Community Survey Office, n.p.

知识点：[文献综述与研究背景撰写方法](../../../topics/数学建模/wenxian_zongshu.md)、[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[影响因素评估指标体系构建（温度、湿度、经济、教育等）](../../../topics/数学建模/yingxiang_zhibiao.md)

### 参考 33

U.S. Death Rates by Age Group. 2004. Raw data. Data360, n.p.

知识点：[模型参数的确定（基于数据拟合或实验选择）](../../../topics/数学建模/canshu_queding.md)、[参数合理性验证](../../../topics/数学建模/canshu_heli_xing.md)、[数学建模的基本步骤（问题分析、模型假设、建立、求解、检验、推广）](../../../topics/数学建模/jianmo_buzhou.md)
