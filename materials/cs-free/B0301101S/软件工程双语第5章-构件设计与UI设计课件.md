---
title: 《软件工程（双语）》第5章 构件设计与UI设计（课件）
kind: 课件
course: 软件工程（双语）
term: 2024-2025-2
source: cs-free:【B0301101S】软件工程（双语）/课件（PPT）/软件工程（双语）-课件-24-25-2.7z/UNIT-05 构件设计与UI设计.pptx
---

# 《软件工程（双语）》第5章 构件设计与UI设计（课件）

原件的每一页，下面附识别出的文字。

### UNIT 5

![第 1 页](软件工程双语第5章-构件设计与UI设计课件.assets/第1页.webp)

原文：

UNIT 5

构件设计 & UI设计Component-LevelDesign & UI Design

郑尚东

Software Engineering A PRACTITIONER'S APPROACH

### Component-Level Design

![第 2 页](软件工程双语第5章-构件设计与UI设计课件.assets/第2页.webp)

原文：

Component-Level Design

### Component-Level Design

![第 3 页](软件工程双语第5章-构件设计与UI设计课件.assets/第3页.webp)

原文：

Component-Level Design

Goal: bridging design and construction, transforming design models into a working software

• occurs after the first iteration of architectural design has been completed

defines the data structures, algorithms, interface characteristics, and communication mechanisms allocated to each component at a level of abstraction that is close to code.

• work product: represented in graphical, tabular, or text-based notation.

follow a set of design principles to ensure that the software is functional before coding.

• review the design details for correctness and consistency with other design representations.

### What is a component?

![第 4 页](软件工程双语第5章-构件设计与UI设计课件.assets/第4页.webp)

原文：

What is a component?

OMG UML Specification defines a component as

• “… a modular, deployable, and replaceable part of a system that encapsulates implementation and exposes a set of interfaces.”

components reside within the architecture,

they must communicate and collaborate with other components and with entities (e.g., other systems, devices, people) that exist outside the boundaries of the software.

### view: OO & traditional

![第 5 页](软件工程双语第5章-构件设计与UI设计课件.assets/第5页.webp)

原文：

view: OO & traditional

How does the OO-View of component-level design differ from the traditional-view?

OO-View: a component contains a set of collaborating classes. A class is related to the problem domain and infrastructure domain. Classes are elaborated by defining all attribute data structures, describing process flow for operations, specifying messaging details for interfaces.

• Traditional-View: a module is a functional element of a program. three type of modules: control, business, infrastructure.

All modules requires representations to be created for processing logic, the internal data structures, and an interface that enables the modules to be invoked and data to be passed to it.

• A Process-Related View: CBSE, assembling architecture by reusing components or design patterns.

### 构件的OO观点

![第 6 页](软件工程双语第5章-构件设计与UI设计课件.assets/第6页.webp)

原文：

构件的OO观点

印刷管理软件

• 接收印务，定价并将印务交给自动生产设备

• 设计构件 PrintJob

接口 computeJob：

• 实现 computePageCost() 等操作

• 与定价构件 PricingTable 协作

接口 initiateJob：

• 实现 checkPriority() 操作

• 与 JobQueue 构件协作，判断任务类型和优先级

思：接口设计是否已经最优 ？

### 构件的传统观点

![第 7 页](软件工程双语第5章-构件设计与UI设计课件.assets/第7页.webp)

原文：

构件的传统观点

### 传统观点：ComputePageCost 模块设计

![第 8 页](软件工程双语第5章-构件设计与UI设计课件.assets/第8页.webp)

原文：

传统观点：ComputePageCost 模块设计

accessCostDB (JS, color, size)

job complexity factor (JCF) =

设计思路：

• 调用 getJobData 模块得到印务数据

• 调用 accessCostDB 模块，访问数据库得到成本数据

• 根据用户提供的规格说明，衡量任务量和负载度，计算印刷价格

注意：

• 随着逐步细化，设计焦点转向特定数据结构设计与操作数据的过程设计

• 但是不要忘记容纳构件的体系结构与服务于多数构件的全局数据结构

### 构件级设计指导方针

![第 9 页](软件工程双语第5章-构件设计与UI设计课件.assets/第9页.webp)

原文：

构件级设计指导方针

• 构件：对那些已经被确定为体系结构模型一部分的构件应该建立命名约定，并对其做进一步的精细化处理，使其成为构件级模型的一部分

• 接口：接口提供关于通信和协作的重要信息（也可以帮助我们实现OOP原则）

• 依赖与继承：为了提高可读性，依赖关系自左向右，继承关系自底（导出类）向上（基类）

### Cohesion

![第 10 页](软件工程双语第5章-构件设计与UI设计课件.assets/第10页.webp)

原文：

Cohesion

Traditional View - the “single-mindedness” of a module.

OO View - cohesion implies that a component encapsulates only attributes and operations that are closely related to one another and the component itself.

Levels of cohesion:

• Functional - module performs one and only one computation.

Layer - occurs when a higher layer accesses the services of a lower layer, but lower layers do not access higher layers.

• Communicational - All operations that access the same data are defined within one class.

### coupling

![第 11 页](软件工程双语第5章-构件设计与UI设计课件.assets/第11页.webp)

原文：

coupling

Traditional View - degree to which a component is connected to other components and to the external world.

OO View - qualitative measure of the degree to which classes are connected to one another.

Levels of coupling:

Content - occurs when one component “surreptitiously modifies data that is internal to another component.

• Control – occurs when control flags a passed to components to requests alternate behaviors when invoked.

• External - occurs when a component communicates or collaborates with infrastructure components.

### OO中的类耦合

![第 12 页](软件工程双语第5章-构件设计与UI设计课件.assets/第12页.webp)

原文：

OO中的类耦合

OO 类之间的耦合关系（依赖关系）有 3 种：

1. 零耦合关系：两个类之间没有任何耦合关系

2. 具体耦合关系：发生在两个具体类（可实例化的类）之间，由一个类直接引用另一个具体类的实例而产生

3. 抽象耦合关系：发生在具体类和抽象类之间，或发生在两个抽象类之间；由不同的具体实现类扩展抽象类，具有很大灵活性

耦合（依赖）注入：如何在对象之间传递依赖关系？

对象中调用另一个对象的方法要在抽象层编程，编程时应尽量注入父类对象，运行时子类对象覆盖父类对象，有 3 种注入方式：

1. 构造注入：通过构造函数注入实例变量

2. 设值注入：通过 Setter 方法注入实例变量

3. 接口注入：通过接口方法注入实例变量

### 耦合的构造注入

![第 13 页](软件工程双语第5章-构件设计与UI设计课件.assets/第13页.webp)

原文：

耦合的构造注入

通过构造函数注入实例变量

### 耦合的设值注入

![第 14 页](软件工程双语第5章-构件设计与UI设计课件.assets/第14页.webp)

原文：

耦合的设值注入

通过 Setter 方法注入实例变量

### 耦合的接口注入

![第 15 页](软件工程双语第5章-构件设计与UI设计课件.assets/第15页.webp)

原文：

耦合的接口注入

通过接口方法注入实例变量

### Component Design Principles

![第 16 页](软件工程双语第5章-构件设计与UI设计课件.assets/第16页.webp)

原文：

Component Design Principles

• Single Responsibility Principle (SRP). “Every class should have a single responsibility, and that responsibility should be entirely encapsulated by the class.

• Open-Closed Principle (OCP). “A module [component] should be open for extension but closed for modification.

• Liskov Substitution Principle (LSP). “Subclasses should be substitutable for their base classes.

• Dependency Inversion Principle (DIP). “Depend on abstractions. Do not depend on concretions.”

• Interface Segregation Principle (ISP). “Many client-specific interfaces are better than one general purpose interface.

• Release Reuse Equivalency Principle (REP). “The granule of reuse is the granule of release.”

• Common Closure Principle (CCP). “Classes that change together belong together.”

• Common Reuse Principle (CRP). “Classes that aren’t reused together should not be grouped together.”

Law of Demeter (LoD). “Each unit should have only limited knowledge about other units: onlyunits 'closely' related to the current unit.

### Single Responsibility Principle

![第 17 页](软件工程双语第5章-构件设计与UI设计课件.assets/第17页.webp)

原文：

Single Responsibility Principle

Every class should have a single responsibility, and that responsibility should be entirely encapsulated by the class.

Or: should never be more than one reason for a class to change.

Login方案设计有什么问题 ?

### Single Responsibility Principle

![第 18 页](软件工程双语第5章-构件设计与UI设计课件.assets/第18页.webp)

原文：

Single Responsibility Principle

设计重构，符合单一职责原则

一个类的修改不会影响其他类，增强系统的可维护性

负责启动系统，类中定义了main()函数

负责界面显示，因此它只包含与界面有关的方法和事件处理方法

负责用户表的增删改查操作，封装了对用户表的全部操作代码，登录本质上是一个查询用户表的操作

可供多个界面类使用

负责数据库的连接，该类可以供多个DAO类重用

所有操作数据库的类都可以调用该类中的getConnection()方法来获取数据库连接对象

### Open-Closed Principle

![第 19 页](软件工程双语第5章-构件设计与UI设计课件.assets/第19页.webp)

原文：

Open-Closed Principle

A module [component] should be open for extension but closed for modification

### 开闭原则OCP：示例

![第 20 页](软件工程双语第5章-构件设计与UI设计课件.assets/第20页.webp)

原文：

开闭原则OCP：示例

对于各种类型传感器，Sensor 接口都向 Detector 构件呈现一致的视图

• 当增添新类型的传感器时，对类Detector 构件无需任何修改

### 开闭原则OCP：示例

![第 21 页](软件工程双语第5章-构件设计与UI设计课件.assets/第21页.webp)

原文：

开闭原则OCP：示例

设计方案违反：开闭原则

需求改变，需要修改LoginForm类的源码，修改按钮类的类名，因两个按钮类的显示方法不相同，需要修改 LoginForm 类的 display()方法

### 开闭原则OCP：示例

![第 22 页](软件工程双语第5章-构件设计与UI设计课件.assets/第22页.webp)

原文：

开闭原则OCP：示例

方案重构

### Java的反射机制

![第 23 页](软件工程双语第5章-构件设计与UI设计课件.assets/第23页.webp)

原文：

Java的反射机制

### Liskov Substitution Principle

![第 24 页](软件工程双语第5章-构件设计与UI设计课件.assets/第24页.webp)

原文：

Liskov Substitution Principle

Subclasses should be substitutable for their base classes.

### Liskov替换原则LSP：示例

![第 25 页](软件工程双语第5章-构件设计与UI设计课件.assets/第25页.webp)

原文：

Liskov替换原则LSP：示例

方案重构

### Liskov替换原则LSP：示例

![第 26 页](软件工程双语第5章-构件设计与UI设计课件.assets/第26页.webp)

原文：

Liskov替换原则LSP：示例

方案重构

### Liskov替换原则LSP：示例

![第 27 页](软件工程双语第5章-构件设计与UI设计课件.assets/第27页.webp)

原文：

Liskov替换原则LSP：示例

系统提供两种加密算法，设计方案的问题：

更换加密算法，需要修改客户类 Client 与数据操作类 DataOperator

### Liskov替换原则LSP：示例

![第 28 页](软件工程双语第5章-构件设计与UI设计课件.assets/第28页.webp)

原文：

Liskov替换原则LSP：示例

方案重构：

### Dependency Inversion Principle

![第 29 页](软件工程双语第5章-构件设计与UI设计课件.assets/第29页.webp)

原文：

Dependency Inversion Principle

\+ abstract speaking(): void ;

\+ descriptiion(): void ;

Depend on abstractions. Do not depend on concretions.

• 抽象容易扩展设计方案，不会导致大的混乱

• 构件依赖的具体构件越多（而非依赖7 抽象类或接口），扩展就越困难

### 依赖倒置原则DIP：示例

![第 30 页](软件工程双语第5章-构件设计与UI设计课件.assets/第30页.webp)

原文：

依赖倒置原则DIP：示例

以抽象方式耦合，是依赖倒置原则的关键

• LSP是DIP的基础：抽象耦合关系一定涉及具体类继承抽象类，需保证在任何引用基类的地方，都可以替换成其子类

设计方案：违反开闭原则

数据来自数据库

转换后的格式：XML文件

数据转换功能

将来自不同数据源的数据，转换为多种格式

\+ main (String args[]) : void

当新增数据源或文件格式时，需修改Client

数据来自文本文件

转换后的格式：XLS文件

### 依赖倒置原则DIP：示例

![第 31 页](软件工程双语第5章-构件设计与UI设计课件.assets/第31页.webp)

原文：

依赖倒置原则DIP：示例

• 设计方案重构

### Interface Segregation Principle

![第 32 页](软件工程双语第5章-构件设计与UI设计课件.assets/第32页.webp)

原文：

Interface Segregation Principle

Many client-specific interfaces are better than one general purpose interface.

• The client does not rely on unnecessary interfaces.

• Just need to know the relevant methods (a controlled connection).

ISPI suggest：

The operations of the design class are categorized into one or more abstract classes (or interface).

operations within the abstract class (the interface) should be cohesive; that is, it should exhibit a limited function.

### Interface Segregation Principle

![第 33 页](软件工程双语第5章-构件设计与UI设计课件.assets/第33页.webp)

原文：

Interface Segregation Principle

SafeHome 住宅安全与监视功能

FloorPlan在平面图中配置设备

DeviceSet

\+ placeDevice() :void + showDevice() :void + groupDevice() :void + removeDevice() :void

VideoManagement

Surveillance

\+ showDeviceID() :void+ showFOV() :void实现放置、显示、分组、删除设备管理的功能

ConcreteService

\+ placeDevice() :void

\+ showDevice() :void

\+ groupDevice() :void

\+ removeDevice() :void

\+ showFOV() :void

\+ showDeviceID() :void

实现显示摄像头的ID与视

角(field of view)等功能

### 接口分离原则ISP

![第 34 页](软件工程双语第5章-构件设计与UI设计课件.assets/第34页.webp)

原文：

接口分离原则ISP

接口设计是否已经最优 ？

构件PrintJob与接口initiateJob应被重构：

initiateJob 接口分解为 3 个接口： buildJob、submitJob、initiateJob

• 每个接口仅关注一个功能，且构件PrintJob 新增 3 个类：定义类WorkOrder：其操作buildWorkOrder()负责组装一个工作单，定义类JobQueue：其操作checkPriority()检查任务优先级，定义类ProductionJob：负责将任务传递到生产设施，进行生产作业

• 接口initiateJob专注于一个功能，与ProductionJob、WorkOrder和JobQueue关联的接口同样是专一的

### 接口分离原则ISP

![第 35 页](软件工程双语第5章-构件设计与UI设计课件.assets/第35页.webp)

原文：

接口分离原则ISP

接口设计是否已经最优 ？

### Common Reuse Principle

![第 36 页](软件工程双语第5章-构件设计与UI设计课件.assets/第36页.webp)

原文：

Common Reuse Principle

also called: Composite Reuse Principle

• Classes that aren’t reused together should not be grouped together.

• Favor composition of objects over inheritance as a reuse

mechanism.

### reuse: inheritance & association

![第 37 页](软件工程双语第5章-构件设计与UI设计课件.assets/第37页.webp)

原文：

reuse: inheritance & association

<table><tr><td>继承复用(“白箱”复用)</td><td>关联复用(“黑箱”复用)</td></tr><tr><td>子类继承父类的方法,易于扩展</td><td>通过组合/聚合类实例作为另一个类实例的一部分</td></tr><tr><td>✧ 继承将基类的实现细节,暴露给子类,破坏系统的封装性</td><td>✧ 新对象调用已有对象的功能,已有对象的内部实现细节,对于新对象是不可见的</td></tr><tr><td>✧ 基类发生改变,子类实现也不得不改变</td><td rowspan="2">✧ 根据需要,新对象在运行时、动态、有选择性地调用成员对象的操作,或与成员对象类型相同的其他对象</td></tr><tr><td>✧ 继承得来的实现是静态的,不能在运行时改变,不灵活性</td></tr><tr><td>✧ 继承只能在有限环境中使用,如类不能被声明为 final 类</td><td>✧ 使系统更灵活,降低类与类之间的耦合度,一个类的变化对其他类造成的影响相对较少</td></tr></table>

### 共同复用原则CRP：示例

![第 38 页](软件工程双语第5章-构件设计与UI设计课件.assets/第38页.webp)

原文：

共同复用原则CRP：示例

数据库访问方案的设计问题 ？

类DBUtil用于访问DB，方法getConnection()返回一个DB连接Connection的对象

方法getConnection()在子类中被继承复用

设计方案的问题：

DB支持多种连接方式：1）JDBC连接；2）池连接类

若两个子类采用不同连接，需新增一个DBUtil类，且修改StudentDAO类或TeacherDAO类，继承新的DBUtil类

违反开闭原则，系统扩展差

### 共同复用原则CRP：示例

![第 39 页](软件工程双语第5章-构件设计与UI设计课件.assets/第39页.webp)

原文：

共同复用原则CRP：示例

设计重构

设计方案改进：

StudentDAO类、TeacherDAO类与DBUtil类不再是继承关系，改为聚合关联关系

通过setDBOperator()函数，为类的成员变量dBOperator赋值

更换连接方式时，1）新增一个DBUtil类的子类，2）子类重写getConnection()函数，3)客户端调用setDBOperator()函数时，注入子类对象即可

客户端只针对DBUtil类编程，符合开闭原则

### Law of Demeter, LoD

![第 40 页](软件工程双语第5章-构件设计与UI设计课件.assets/第40页.webp)

原文：

Law of Demeter, LoD

also called: Least Knowledge Principle (LKP)

• Each unit should have only limited knowledge about other units: onlyunits 'closely' related to the current unit

• Don't talk to strangers.

• Talk only to your immediate friends.

1. 当前对象本身(this)

2. 以参数形式传入到当前对象方法中的对象

3. 当前对象的成员对象

4. 如果当前对象的成员对象是一个集合，那么集合中的元素也都是朋友

5. 当前对象所创建的对象

### 迪米特法则LoD

![第 41 页](软件工程双语第5章-构件设计与UI设计课件.assets/第41页.webp)

原文：

迪米特法则LoD

<table><tr><td colspan="2">迪米特法则,也称为:最少知识原则</td></tr><tr><td>典型定义</td><td>◇ 不要和“陌生人”说话◇ 只与直接朋友通信◇ 每一个软件单位对其他单位都只有最少知识,而且局限于那些与本单位密切相关的软件单位</td></tr><tr><td>目的</td><td>◇ 降低系统的耦合度,保持类与类之间的松散耦合关系◇ 一个软件实体应当尽可能少地与其他实体发生相互作用◇ 当一个模块修改时,尽量少地影响其他模块,扩展相对容易◇ 狭义法则:两个类之间不必彼此直接通信◇ 广义法则:控制信息过载,控制对象之间的信息流量、流向以及信息的影响,即对信息隐藏的控制</td></tr><tr><td>使用法则的注意事项</td><td>1 在类的划分上,应当尽量创建松耦合的类,类之间的耦合度越低,就越有利于复用,一个处在松耦合中的类一旦被修改,不会对关联的类造成太大波及2 在类结构设计上,每一个类都应当尽量降低其成员变量和成员函数的访问权限3 在类的设计上,只要有可能,一个类型应当设计成不变类4 在对其他类的引用上,一个对象对其他对象的引用应当降到最低</td></tr></table>

### 迪米特法则LoD：示例

![第 42 页](软件工程双语第5章-构件设计与UI设计课件.assets/第42页.webp)

原文：

迪米特法则LoD：示例

界面类与数据访问类之间的调用关系复杂，耦合度大

• 新增界面或新增数据访问麻烦，系统可维护性、扩展性差

### Conducting Component-Level Design

![第 43 页](软件工程双语第5章-构件设计与UI设计课件.assets/第43页.webp)

原文：

Conducting Component-Level Design

What are the steps used to complete the component-level design for a software development project?

1.Identify all design classes that correspond to the problem domain.

2.Identify all design classes that correspond to the infrastructure domain.

3.Elaborate all design classes that are not acquired as reusable components.

4.Identify persistent data sources (databases and files) and identify the classes required to manage them.

5.Develop and elaborate behavioral representations for each class or component.

6.Elaborate deployment diagrams to provide additional implementation detail.

7.Factor every component-level diagram representation and consider alternatives.

### 实施构件级设计

![第 44 页](软件工程双语第5章-构件设计与UI设计课件.assets/第44页.webp)

原文：

实施构件级设计

1. 标识出所有与问题域相对应的设计类

2. 确定所有与基础设施域相对应的设计类

分析建模:what

设计建模：how

问题需求

基础设施infrastructure

安全需求性能需求可靠性需求分析模型类实体类

边界类

控制类

用户接口类

业务域类

过程类

持久类

系统类

### 实施构件级设计

![第 45 页](软件工程双语第5章-构件设计与UI设计课件.assets/第45页.webp)

原文：

实施构件级设计

3. 细化所有非作为可复用构件的设计类

3a：说明类或构件协作时的消息细节

细化交互的消息细节：

[guard condition] sequence expression (return value) := message name (argument list)

[guard condition]：用OCL语言说明在消息发出之前应该满足的条件

sequence expression：一个表明消息发送的序号

(return value)：消息唤醒的操作返回值

message name：被唤醒的操作

(argument list)：传递给操作的参数列表

### 实施构件级设计

![第 46 页](软件工程双语第5章-构件设计与UI设计课件.assets/第46页.webp)

原文：

实施构件级设计

3. 细化所有非作为可复用构件的设计类

3b：确定每个构件的适当接口

### 实施构件级设计

![第 47 页](软件工程双语第5章-构件设计与UI设计课件.assets/第47页.webp)

原文：

实施构件级设计

3. 细化所有非作为可复用构件的设计类

3c：细化属性，定义实现属性所需的数据类型和数据结构

注：若一个属性在多个设计类中重复出现，且结构复杂，应分离为一个单独的类

### 实施构件级设计

![第 48 页](软件工程双语第5章-构件设计与UI设计课件.assets/第48页.webp)

原文：

实施构件级设计

3. 细化所有非作为可复用构件的设计类

3d：详述每个操作中的处理流

操作应实现高内聚性，一个操作仅完成单一目标功能或子功能

若算法简单易理解，就无需细化，复杂难理解，则必须设计细化

细化常使用：伪码或UML活动图

### 实施构件级设计

![第 49 页](软件工程双语第5章-构件设计与UI设计课件.assets/第49页.webp)

原文：

实施构件级设计

4. 描述持久数据源（数据库和文件），确定管理数据源的类

5. 开发并且细化类或构件的行为表示

<table><tr><td colspan="2">事件表达</td></tr><tr><td colspan="2">Event-name (parameter-list) [guard-condition] / action-expression</td></tr><tr><td>event-name</td><td>✧ 事件名称</td></tr><tr><td>parameter-list</td><td>✧ 与事件相关的数据</td></tr><tr><td>guard-condition</td><td>✧ OCL语言书写,描述事件发生前必须满足的条件</td></tr><tr><td>action-expression</td><td>✧ 定义状态转换时发生的动作</td></tr><tr><td colspan="2">状态表达</td></tr><tr><td>entry/</td><td>✧ 指示进入状态时的动作</td></tr><tr><td>exit/</td><td>✧ 指示离开状态时的动作</td></tr><tr><td>do/</td><td>✧ 提供一种机制,示意伴随状态发生的相关活动</td></tr><tr><td>include/</td><td>✧ 提供了一种“在状态定义中嵌入更多状态图细节”进行细化的手段</td></tr></table>

### 实施构件级设计

![第 50 页](软件工程双语第5章-构件设计与UI设计课件.assets/第50页.webp)

原文：

实施构件级设计

4. 描述持久数据源（数据库

5. 开发并且细化类或构件

<table><tr><td colspan="2"></td></tr><tr><td colspan="2">Event-name (parameter-list)</td></tr><tr><td>event-name</td><td>✧ 事件名称</td></tr><tr><td>parameter-list</td><td>✧ 与事件相关的数</td></tr><tr><td>guard-condition</td><td>✧ OCL语言书写,</td></tr><tr><td>action-expression</td><td>✧ 定义状态转换时</td></tr><tr><td colspan="2"></td></tr><tr><td>entry/</td><td>✧ 指示进入状态时</td></tr><tr><td>exit/</td><td>✧ 指示离开状态时</td></tr><tr><td>do/</td><td>✧ 提供一种机制,</td></tr><tr><td>include/</td><td>✧ 提供了一种“在</td></tr></table>

由状态图得到的额外信息：当得到印务的成本和进度数据时，PrintJob 类的动态行为取决于用户是否同意，若不同意（警戒条件确保用户有权审核），达不到 submittingJob 状态，印务不能提交

### 实施构件级设计

![第 51 页](软件工程双语第5章-构件设计与UI设计课件.assets/第51页.webp)

原文：

实施构件级设计

6. 细化部署图以提供额外的实现细节

• 部署图是体系结构设计的一部分，示意系统功能（常表现为子系统）容纳在计算环境中

• 在构件级设计过程中，部署图应细化为实例形式，说明硬件和使用的OS环境，指定构件包在环境中的位置

7. 重构每个构件级设计表示，并且考虑其他可选方案

### Traditional Component-Level Design

![第 52 页](软件工程双语第5章-构件设计与UI设计课件.assets/第52页.webp)

原文：

Traditional Component-Level Design

Design of processing logic is governed by

• the basic principles of algorithm design and structured programming.

Design of data structures is defined by

• the data model developed for the system.

Design of interfaces is governed by

• the collaborations that a component must effect.

### Component-Based SE

![第 53 页](软件工程双语第5章-构件设计与UI设计课件.assets/第53页.webp)

原文：

Component-Based SE

The software team asks:

• Are commercial off-the-shelf (COTS) components available to implement the requirement?

Are the interfaces for available components compatible within the architecture of the system to be built?

• Are internally-developed reusable components available to implement the requirement?

### CBSE: advantages & risks

![第 54 页](软件工程双语第5章-构件设计与UI设计课件.assets/第54页.webp)

原文：

CBSE: advantages & risks

What are the advantages and risks of CBSE ?

<table><tr><td>advantages</td><td rowspan="2"></td><td>risks</td></tr><tr><td>Reduced lead time.Greater return on investment (ROI).Leveraged costs of developing components.Enhanced quality.Maintenance of component-based applications.</td><td>Component selection risks.Component integration risks.Quality risks.Security risks.System evolution risks.</td></tr></table>

### Component Refactoring

![第 55 页](软件工程双语第5章-构件设计与UI设计课件.assets/第55页.webp)

原文：

Component Refactoring

• Most developers would agree that refactoring components to improve quality is a good practice.

• It is hard to convince management to expend resources fixing components that are working correctly rather than adding new functionality to them,

• Changing software and failing to document the changes can lead to increasing technical debt.

• Reducing this technical debt often involves architectural refactoring, which is generally perceived by developers as both costly and risky.

• Developers can make of tools to examine change histories to identify the most cost effective refactoring opportunities.

### User eXperience Design

![第 56 页](软件工程双语第5章-构件设计与UI设计课件.assets/第56页.webp)

原文：

User eXperience Design

### User eXperience Design

![第 57 页](软件工程双语第5章-构件设计与UI设计课件.assets/第57页.webp)

原文：

User eXperience Design

The software development from "people are required to conform to technology" to "make technology that conforms to people".

UX Design needs to exhibit usability and accessibility.

• usability: Is it easy and effective ?

• accessibility: Is the assistive technologies provided ?

two dominant issues studied in UX Design.

1. a set of golden rules were identified.

2. a set of interaction mechanisms (user interface, UI) were defined.

### UX Design Elements

![第 58 页](软件工程双语第5章-构件设计与UI设计课件.assets/第58页.webp)

原文：

UX Design Elements

UX design tries to ensure that no aspect of the software appears the final product without the explicit decision of stakeholders to include it.

• Strategy. Identifies user needs and customer business goals.

• Scope. Includes both the functional and content requirements.

Structure. Consists of the interaction design and information architecture.

• Skeleton. Comprised of three design components: information, interface, navigation.

• Surface. Presents visual design or the appearance of the software.

### Information Architecture

![第 59 页](软件工程双语第5章-构件设计与UI设计课件.assets/第59页.webp)

原文：

Information Architecture

3 types of architecture

Information architecture structures lead organization, labeling, navigation, and searching of content objects.

Content architecture focuses on the manner that the content objects are structured for presentation and navigation.

Software architecture addresses the manner that the application is structured to manage user interaction, effect navigation, and present content.

Architecture design is conducted in parallel with design of interface, aesthetic, and content.

Decisions made during architecture design action will influence work conducted during navigation design.

### User Interaction Design

![第 60 页](软件工程双语第5章-构件设计与UI设计课件.assets/第60页.webp)

原文：

User Interaction Design

Interaction design focuses on interface between product and user.

Modes of user input and output include voice input, computer speech generation, touch input, 3D printed output, immersive augmented reality experiences, and sensor tracking of users.

User interaction should be defined by the stakeholders in the user stories created to describe how users can accomplish their goals using the software product.

User interaction design should also include a plan for how information should be presented within such a system and how to enable the user to understand that information.

It is important to recall that the purpose of the user interface is to present just enough information to help the users decide what their next action should be to accomplish their goal and how to perform it.

### questions of UI design

![第 61 页](软件工程双语第5章-构件设计与UI设计课件.assets/第61页.webp)

原文：

questions of UI design

• What can users do with a mouse, finger, or stylus to interact with the interface directly?

• What about the appearance (e.g., color, shape, size) gives users clues about how the user interaction functions?

• What information do you provide to let users know what will happen before they perform an action?

• Are there any constraints put in place to help prevent errors?

• Do error messages provide a way for users to correct a problem or explain why an error occurs?

• What feedback do users get once an action is performed?

• Are the interface elements a reasonable size to facilitate interaction?

• What familiar or standard formats should be used to display information and accept input?

### Usability Engineering

![第 62 页](软件工程双语第5章-构件设计与UI设计课件.assets/第62页.webp)

原文：

Usability Engineering

Usability engineering is part of UX design that defines the specification, design, and testing of the human-computer interaction portion of a software product.

• focuses on devising human-computer interfaces that have high usability.

focus on easy to learn, easy to use, and easy to remember over time, usability can be measured quantitatively and tested for improvements in usability.

Accessibility is the degree to which people with special needs are provided with a means to perceive, understand, navigate, and interact with computer products.

• Accessibility is another aspect of usability engineering that needs to be considered during design.

### Visual Design

![第 63 页](软件工程双语第5章-构件设计与UI设计课件.assets/第63页.webp)

原文：

Visual Design

Visual design (aesthetic design or graphic design) is an artistic endeavor that complements the technical aspects of the UX design.

• Without it, a product may be functional, but unappealing.

With it, a product draws its users into a world that embraces them on an emotional as well as an intellectual level.

Graphic design considers every aspect of the look and feel of a web or mobile app.

• Not every software engineer has artistic talent.

• If you fall into this category, hire an experienced graphic designer to help.

### The Golden Rules

![第 64 页](软件工程双语第5章-构件设计与UI设计课件.assets/第64页.webp)

原文：

The Golden Rules

What principles should be followed when building any user interface?

• Place the user in control.

• Reduce the user’s memory load.

• Make the interface consistent.

### Rule 1: Place User in Control

![第 65 页](软件工程双语第5章-构件设计与UI设计课件.assets/第65页.webp)

原文：

Rule 1: Place User in Control

• Define interaction modes in a way that does not force a user into unnecessary or undesired actions.

• Provide for flexible interaction.

• Allow user interaction to be interruptible and undoable.

• Streamline interaction as skill levels advance and allow the interaction to be customized.

• Hide technical internals from the casual user.

• Design for direct interaction with screen objects.

### Rule 2: Reduce User’s Memory Load

![第 66 页](软件工程双语第5章-构件设计与UI设计课件.assets/第66页.webp)

原文：

Rule 2: Reduce User’s Memory Load

• Reduce demand on short-term memory.

• Establish meaningful defaults.

• Define shortcuts that are intuitive.

• The visual layout of the interface should be based on a real-world metaphor.

• Disclose information in a progressive fashion.

### Rule 3: Make Interface Consistent

![第 67 页](软件工程双语第5章-构件设计与UI设计课件.assets/第67页.webp)

原文：

Rule 3: Make Interface Consistent

• Allow the user to put the current task into a meaningful context.

• Maintain consistency across a family of applications.

• If past interactive models have created user expectations, do not make changes unless there is a compelling reason to do so.

### UX Analysis

![第 68 页](软件工程双语第5章-构件设计与UI设计课件.assets/第68页.webp)

原文：

UX Analysis

A key tenet of all SE process models is this :

• Understand the problem before you attempt to design a solution.

What things you need to do in user experience analysis if you seek to “understand the problem before you attempt to design a solution.”?

In the case of UX design, understanding the problem means understanding :

1. the people (end users) who will interact with the system through the interface,

2. the tasks that end users must perform to do their work,

3. the content that is presented as part of the interface, and

4. the environment in which these tasks will be conducted.

### Using Customer Journey Map

![第 69 页](软件工程双语第5章-构件设计与UI设计课件.assets/第69页.webp)

原文：

Using Customer Journey Map

1. Gather stakeholders.

2. Conduct research. Collect all information you can about all the things users may experience as they use the product and define your customer phases (touch points).

3. Build the model. Create a visualization of the touch points.

4. Refine the design. Make the deliverable visually appealing and ensure touchpoints are identified clearly.

5. Identify gaps. Note any gaps in the customer experience or points of friction or pain.

6. Implement your findings. Assign responsible parties to bridge the gaps and resolve pain points found.

### Using Customer Journey Map

![第 70 页](软件工程双语第5章-构件设计与UI设计课件.assets/第70页.webp)

原文：

Using Customer Journey Map

计划提升房屋的安全性，寻找传感器放置的最佳房间布局

目标：找到适合个人喜好的最小化传感器放置的最佳布局

示例

审查模型传感器能感知房间的每个部分吗？

第3步：审查模型，确保传感器能监控房间的每个位置

第1步：提出目标

开始创建房间的地板和墙壁

为房间建模布置家具和门窗

布置传感器保证安全保存设计模型

第2步：建模房间，依照地板、墙壁、家具、门窗的顺序，寻找传感器的最佳位置，保存模型

### 第 71 页

![第 71 页](软件工程双语第5章-构件设计与UI设计课件.assets/第71页.webp)

原文：

User Modeling: <sub>Creating</sub> <sub>and</sub> <sub>Using</sub> <sub>Personas</sub>

Four tasks that occur during the general process of creating and using personas to guide the UX design process:

1. Data collection and analysis. Stakeholders collect information about proposed product users and determine the user group needs.

2. Describe personas. The developers need to decide how many personas to create and decide which persona will be their focus.

3. Develop scenarios. Scenarios are user stories about how personas will use the product being developed. often focus on the touchpoints and obstacles described in the customer journey.

4. Acceptance by stakeholders. Often this is done by validating the scenarios using a review technique or demonstration called cognitive walkthrough (stakeholders assume the role defined by a persona and work through a scenario using a prototype).

### Task Analysis

![第 72 页](软件工程双语第5章-构件设计与UI设计课件.assets/第72页.webp)

原文：

Task Analysis

Goal of task analysis (scenario analysis) is to answer the following questions:

• What work will the user perform in specific circumstances?

• What tasks and subtasks will be performed as the user does the work?

• What specific problem domain objects will the user manipulate as work is performed?

• What is the sequence of work tasks — the workflow?

• What is the hierarchy of tasks?

### 角色创建与任务分析：示例

![第 73 页](软件工程双语第5章-构件设计与UI设计课件.assets/第73页.webp)

原文：

角色创建与任务分析：示例

某软件公司为装饰公司开发一个计算机辅助设计系统

2. 置门窗于合适位置

3. 分别用家具模型和饰件模板，在平面图上描绘相应比例的家具与饰件轮廓

4. 移动家具和饰件轮廓线，到达理想位置

5. 标记所有家具和饰件的轮廓

6. 标出尺才以显示其位置

7. 为用户勾画透视图

### 角色创建与任务分析：示例

![第 74 页](软件工程双语第5章-构件设计与UI设计课件.assets/第74页.webp)

原文：

角色创建与任务分析：示例

工作流分析

• 当多个角色用户操作界面时，可通过“多个成员(角色)” 是如何完成工作

层次表示

• 一旦建立工作流，应细化每类用户的

如：重填处方请求

1. 提供辨识信息

1.1 指定姓名

1.2 指定用户 ID

1.3指定个人身份识别码（PIN）和密码

2. 指定处方序号

3. 指定重填处方所需的日期

处方重填功能的泳道图

### Work Environment Analysis

![第 75 页](软件工程双语第5章-构件设计与UI设计课件.assets/第75页.webp)

原文：

Work Environment Analysis

Hackos & Redish

"People do not perform their work in isolation. They are influenced by the activity around them, the physical characteristics of the workplace, the type of equipment they are using, and the work relationships they have with other people."

UI design needs to consider 2 factors.

physical environmental factor:

• "user-friendly" may not be applicable to all software, and some may be constrained by reduced usability.

workplace culture factor:

• Will system interaction be measured in some manner (e.g., time per transaction or accuracy of a transaction)?

• Will two or more people have to share information before an input can be provided?

• How will support be provided to users of the system?

### Iterative UX Design Process

![第 76 页](软件工程双语第5章-构件设计与UI设计课件.assets/第76页.webp)

原文：

Iterative UX Design Process

User Research

• Iterate to validate user needs

Design

• Iterate to design around constraints

Build

• Iterate to validate design ideas

Iteration to a complete UX model

• As with all iterative processes, there is not a clean division between analysis and design.

• The emphasis is on creating incremental prototypes and by testing it with actual users.

### Google 5-Day UX Design Sprint

![第 77 页](软件工程双语第5章-构件设计与UI设计课件.assets/第77页.webp)

原文：

Google 5-Day UX Design Sprint

1. Understand. User research activities (user needs and business goals) for the product. This information is posted on whiteboards for easy reference throughout the sprint.

2. Sketch. Individual stakeholders are given the time and space needed to brainstorm solutions to the problems discovered in the understand phase.

3. Decide. Each stakeholder presents his solution sketch and the team votes to determine the solutions that should be tackled in the prototyping activities that will follow.

4. Prototype. May be a minimally viable product based on the solution selected from the sketch phase, or it may be based on the portions of the customer journey map or storyboard you want to evaluate with potential users in the validate phase.

5. Validate. Every developer watching users try out the prototype this is the best way to discover major issues with its UX design.

### UI Analysis & Design

![第 78 页](软件工程双语第5章-构件设计与UI设计课件.assets/第78页.webp)

原文：

UI Analysis & Design

Design of the UI is a good place to start understanding the UX process.

The overall process for analyzing and designing a UI begins with the creation of different models of system function (as perceived from the outside).

begin by delineating the human- and computer-oriented tasks that are required to achieve system function and then

considering the design issues that apply to all interface designs. Tools are used to prototype and ultimately implement the design model, and

• the result is evaluated by end users for quality.

### UI Design Models

![第 79 页](软件工程双语第5章-构件设计与UI设计课件.assets/第79页.webp)

原文：

UI Design Models

• User model — a profile of all end users of the system.

• Design model — a design realization of the user model.

• Mental model (system perception) — the user’s mental image of what the interface is.

• Implementation model — the interface “look and feel” coupled with supporting information that describe interface syntax and semantics.

An interface designer needs to reconcile these models and derive a consistent representation of the interface.

### UI process: analysis & design

![第 80 页](软件工程双语第5章-构件设计与UI设计课件.assets/第80页.webp)

原文：

UI process: analysis & design

What framework activities need to be completed in the development process of user interface evolution (or spiral)?

• Interface analysis and modeling focuses on the profile of the users who will interact with the system.

• Interface design defines a set of interface objects and actions that enable a user to perform all defined tasks in a manner that meets every usability goal defined for the system.

Interface construction normally begins with the creation of a prototype that enables usage scenarios to be evaluated.

• Interface validation focuses on:

1. The ability of interface to implement every user task correctly.

2. The degree to which interface is easy to use and easy to learn.

3. The user’s acceptance of the interface as a tool in her work.

### UI process: analysis & design

![第 81 页](软件工程双语第5章-构件设计与UI设计课件.assets/第81页.webp)

原文：

UI process: analysis & design

### UI过程：分析与建模

![第 82 页](软件工程双语第5章-构件设计与UI设计课件.assets/第82页.webp)

原文：

UI过程：分析与建模

分析与系统交互的用户特征

• 记录技能级别、业务理解以及对系统的感悟

• 定义用户类别、理解每类用户对系统的感觉，引导定义需求

• 定义需求后，详细分析任务：标识、描述和细化（螺旋迭代）用户为达到系统目标而执行的任务

• 分析用户的物理工作环境特征，如地理位置、采光、位置约束等

• 收集分析信息，创建界面的分析模型

### UI过程：界面设计

![第 83 页](软件工程双语第5章-构件设计与UI设计课件.assets/第83页.webp)

原文：

UI过程：界面设计

定义一组界面对象和动作

• 建模对象和动作的屏幕表示

• 使用户以满足系统所定义的每个使用目标的方式，能够完成所有定义的任务

### UI过程：界面构建

![第 84 页](软件工程双语第5章-构件设计与UI设计课件.assets/第84页.webp)

原文：

UI过程：界面构建

开始于创建可评估使用场景的原型

• 随着迭代设计过程的继续，可用界面开发工具，来完成界面的构造

### UI过程：界面确认

![第 85 页](软件工程双语第5章-构件设计与UI设计课件.assets/第85页.webp)

原文：

UI过程：界面确认

实现任务的能力、易学习和使用的程度

• 界面正确实现每个用户任务的能力，适应所有任务变化的能力、以及达到所有一般用户需求的能力

• 界面容易使用和学习的程度

• 作为工作中的得力工具，用户对界面的接受程度。

### UI Design Evaluation Cycle

![第 86 页](软件工程双语第5章-构件设计与UI设计课件.assets/第86页.webp)

原文：

UI Design Evaluation Cycle

1. After the design model has been completed, a first-level prototype is created.

evaluated by the user, who provides you with direct comments about the efficacy of the interface.

2. Design modifications are made based on user input, and a next level prototype is created.

3. The evaluation cycle continues until no further modifications to the design are necessary.

### Prototype Review

![第 87 页](软件工程双语第5章-构件设计与UI设计课件.assets/第87页.webp)

原文：

Prototype Review

How to evaluate user interface design before building a working computer prototype?

If a design model of the interface has been created, a number of evaluation criteria can be applied during early design reviews:

1. The length and complexity of the interface specification (provides insight into learning effort required by user).

2. The number of user tasks specified and the number of user actions required to complete each (provide estimates of system efficiency).

3. Number of tasks, actions, and states in the design model (imply the memory load imposed on the user).

4. Interface style, help facilities, and error handling protocol provide a general indication of complexity of the interface and its acceptance by the users.

### UI 设计示例

![第 88 页](软件工程双语第5章-构件设计与UI设计课件.assets/第88页.webp)

原文：

UI 设计示例

<table><tr><td>用例</td><td>通过互联网访问摄像机-显示播放视图(ACS-DCV)</td><td rowspan="3">语法解析动词(动作,操作)名词(对象/数据项)源对象、目标对象、应用对象</td><td rowspan="2">房主的任务列表</td></tr><tr><td>参与者</td><td>房主</td></tr><tr><td>用户故事</td><td>我希望通过互联网,在任意远程位置,都能访问SafeHome系统。使用浏览器软件(当正处于工作或旅行状态时),可设置警报系统的状态,启动或关闭系统,重新配置安全区域,以及通过预先设置的摄像机观察住宅内的不同房间。为远程访问SafeHome,需提供ID和密码。ID和密码定义了访问级别、提供安全保证,如并非所有用户都可以重新配置系统。一旦确认身份(通过验证),可检查系统状态,可启用或关闭SafeHome系统而更改状态。在住宅平面图内,查看每个安全传感器,显示每个当前配置的区域,可根据需要修改区域来重新配置系统。通过有策略地布置摄像机,查看住宅内部。通过摇动和变焦每个摄像机,提供住宅内的不同内部视角。</td><td>访问SafeHome系统输入ID和密码,实现远程访问检查系统状态启动或关闭SafeHome系统显示平面图和传感器位置显示平面图上的区域更改平面图上的区域显示平面图上的摄像机位置选择要查看的摄像机查看视频图像(每秒4帧)摇动或变焦摄像机</td></tr></table>

屏幕布局是一个交互式过程，包括：图标的图形设计和放置、描述性文本定义、窗口的规格说明和标题、菜单项定义等

### UI 设计示例

![第 89 页](软件工程双语第5章-构件设计与UI设计课件.assets/第89页.webp)

原文：

UI 设计示例

交互流程

即：用例事件流

活动图表示

### UI 设计示例

![第 90 页](软件工程双语第5章-构件设计与UI设计课件.assets/第90页.webp)

原文：

UI 设计示例

交互流程

即：用例事件流

泳道图表示

### UI 设计示例

![第 91 页](软件工程双语第5章-构件设计与UI设计课件.assets/第91页.webp)

原文：

UI 设计示例

PC 端设计草图

移动端设计草图

### UI 设计模式

![第 92 页](软件工程双语第5章-构件设计与UI设计课件.assets/第92页.webp)

原文：

UI 设计模式

设计模式是一种抽象，描述一个特定、有界的问题解决方案

• CalendarStrip 模式

• 移动端模式：如何缩放、侧边栏访问（华为）、通知显示信息等，其它如：

<table><tr><td>模式名称</td><td>解决问题</td></tr><tr><td>Check-in screens</td><td>登录屏幕✧ 如何从一个特定位置登录,发表评论,并在社交网络中与朋友和粉丝分享评论?</td></tr><tr><td>Maps</td><td>地图✧ 如何在当前环境中,显示一个能解决一些其他问题的地图?✧ 例如,查看一家餐厅并表示其在城市中的位置。</td></tr><tr><td>Popovers</td><td>漂浮选单✧ 如何表示实时产生或作为用户操作结果的消息或信息(来自应用程序或其他用户)?</td></tr><tr><td>Sign-up flows</td><td>注册流程✧ 如何提供一种登录或注册等功能的简单方法?</td></tr><tr><td>Custom tab navigation</td><td>自定义选项卡导航✧ 如何表示各种不同内容对象,使用户能够选择其想要的对象?</td></tr><tr><td>Invitations</td><td>邀请✧ 如何通知用户必须参与的一些活动或对话?✧ 典型示例包括使用对话框、工具提示或自播放视频演示等。</td></tr></table>

<table><tr><td colspan="7">1:29</td></tr><tr><td colspan="7">&lt; NBA ▼</td></tr><tr><td>赛程</td><td>排行</td><td>球员榜</td><td>球队榜</td><td colspan="3">新秀榜</td></tr><tr><td colspan="3">筛选球队</td><td colspan="4">筛选比赛日期</td></tr><tr><td colspan="7">《 2024年03月 &gt;</td></tr><tr><td>日</td><td>一</td><td>二</td><td>三</td><td>四</td><td>五</td><td>六</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>18场</td><td>29场</td></tr><tr><td>35场</td><td>410场</td><td>57场</td><td>610场</td><td>79场</td><td>88场</td><td>99场</td></tr><tr><td>108场</td><td>1111场</td><td>127场</td><td>138场</td><td>1410场</td><td>157场</td><td>167场</td></tr><tr><td>1710场</td><td>189场</td><td>198场</td><td>205场</td><td>218场</td><td>227场</td><td>238场</td></tr><tr><td>248场</td><td>257场</td><td>2611场</td><td>274场</td><td>2812场</td><td>292场</td><td>3012场</td></tr><tr><td>31</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="4">重置</td><td colspan="3">确定</td></tr></table>

### 其它常用 UI 设计模式

![第 93 页](软件工程双语第5章-构件设计与UI设计课件.assets/第93页.webp)

原文：

其它常用 UI 设计模式

SearchBox: 用户需要找到一项信息或特定信息

<table><tr><td>模式名称</td><td>SearchBox</td></tr><tr><td>问题</td><td>用户需要找到一项信息或特定信息。</td></tr><tr><td>动机</td><td>在任何情况下,关键词搜索都作用于组织成网页的内容对象集合。</td></tr><tr><td>环境</td><td>✧ 用户不会用导航去获取信息或内容,而是在包含很多网页的内容里直接搜索。✧ 所有网站都有主导航系统。用户可能想在一个类里搜索一项,也可能想进一步指定一个查询。</td></tr><tr><td>影响因素</td><td>✧ 网站有主导航系统。✧ 用户可能想在一个类里搜索一项,也可能通过简单的布尔运算符进一步指定一个查询。</td></tr><tr><td>解决方案</td><td>✧ 搜索功能是由搜索标签、关键词字段、筛选程序(如果适用)以及“搜索”按钮构成的。✧ 按回车键和点击搜索按钮的功能是一样的。同时在一个单独的网页上提供了搜索提示和示例。✧ 进入这个网页的链接就放在搜索功能的旁边。编辑搜索词的编辑框足够容纳3个典型的用户查询(通常约20个字符)。✧ 如果筛选条件多于两个,可以用组合框,否则用单选按钮。✧ 搜索结果显示在新的网页上,这个网页上有清除标签,而且至少含有“搜索结果”或类似的信息。位于网页顶部的带有输入关键词的搜索功能可以重复执行,使用户知道关键词是什么。</td></tr></table>

### 其它常用 UI 设计模式

![第 94 页](软件工程双语第5章-构件设计与UI设计课件.assets/第94页.webp)

原文：

其它常用 UI 设计模式

Whole UI：指导整个界面的顶层结构和导航设计

<table><tr><td>模式名称</td><td>Top-level navigation</td></tr><tr><td>概述</td><td>✧ 用于网站或应用程序完成一些主要功能。✧ 提供一个高级菜单,徽标或图形标识常常与菜单一起出现,通过菜单可以直接导航到系统的主要功能。</td></tr><tr><td>详细资料</td><td>✧ 主要功能(一般仅限于4~7个功能名)用一条水平的文字横列在显示器的上部(也可能是重直纵列格式)。✧ 每个功能名提供到达相应的功能或信息源的链接。✧ 通常使用后面讨论的Bread Crumbs模式。</td></tr><tr><td>导航元素</td><td>✧ 每个功能或内容的名称代表连接相应功能或内容的链接。</td></tr><tr><td colspan="2">... ...</td></tr></table>

### 其它常用 UI 设计模式

![第 95 页](软件工程双语第5章-构件设计与UI设计课件.assets/第95页.webp)

原文：

其它常用 UI 设计模式

Page layout：解决网页或交互式组织问题

<table><tr><td>模式名称</td><td>Card stack</td></tr><tr><td>概述</td><td>当必须按任意顺序选择与特征或功能相关的一些特定子功能或内容分类时,使用该模式。该模式提供了大量的选项卡,用鼠标点击可以选择,每个选项卡代表特定的子功能或内容分类。</td></tr><tr><td>详细资料</td><td>选项卡是容易理解的隐喻,且易于用户操作。每个选项卡的格式可能有些不同。一些选项卡可能需要输入信息,会有按钮或其他导航机制;另一些选项卡可能是提供信息的。该模式可结合 Drop-Down List、Fill-in-the-Blanks 等其他模式一起使用。</td></tr><tr><td>导航元素</td><td>用鼠标点击标签,就会显示相应的选项卡。选项卡的导航功能也可能同时出现,但是通常情况下,这些只是初始化与选项卡数据相关的功能,并不连接到其他显示。</td></tr><tr><td colspan="2">... ...</td></tr></table>

### 其它常用 UI 设计模式

![第 96 页](软件工程双语第5章-构件设计与UI设计课件.assets/第96页.webp)

原文：

其它常用 UI 设计模式

Forms and input：解决表单输入的设计技术

<table><tr><td>模式名称</td><td>Fill-in-the-Blanks</td></tr><tr><td>概述</td><td>将字母数字数据输人到“文本框”中。</td></tr><tr><td>详细资料</td><td>✧ 可以将数据输入到文本框中。✧ 一般地,通过选取某些文本或图形指示器(例如“搜索”“提”“下一个”等按钮)可以验证并处理数据。✧ 很多情况下,该模式与 Drop Down List 或其他模式(例如,SEARCH &lt;drop down list&gt; FOR&lt;fill-in-blanks textbox&gt;)结合起来使用。</td></tr><tr><td>导航元素</td><td>✧ 文本或图形指示器启动验证并处理数据。</td></tr><tr><td colspan="2">... ...</td></tr></table>

### 其它常用 UI 设计模式

![第 97 页](软件工程双语第5章-构件设计与UI设计课件.assets/第97页.webp)

原文：

其它常用 UI 设计模式

Navigation：解决分层菜单、网页和交互式屏显的导航问题

<table><tr><td>模式名称</td><td>Edit-In-Place</td></tr><tr><td>概述</td><td>对于显示出的某些类型的内容,该模式提供了简单的文本编辑功能,而不需要用户明确指定文本编辑功能或状态。</td></tr><tr><td>详细资料</td><td>✧ 用户在显示屏上看到需要修改的内容。✧ 用鼠标在显示的内容上双击,就是向系统表示希望编辑该内容。✧ 该内容会突出显示,表示处于可编辑状态,用户就可以进行适当的修改了。</td></tr><tr><td>导航元素</td><td>无</td></tr><tr><td colspan="2">... ...</td></tr></table>

### 其它常用 UI 设计模式

![第 98 页](软件工程双语第5章-构件设计与UI设计课件.assets/第98页.webp)

原文：

其它常用 UI 设计模式

E-commerce：电子商务网站可复用元素

<table><tr><td>模式名称</td><td>Shopping Cart</td></tr><tr><td>概述</td><td>列出了要购买的选项清单。</td></tr><tr><td>详细资料</td><td>✧ 列出项目、数量、产品代码、可供性(有现货、无现货)、价格、交付信息、运费及其他相关的购买信息。✧ 同时也提供了编辑功能(例如,删除、修改数量)。</td></tr><tr><td>导航元素</td><td>✧ 包括继续购买或前往结账。</td></tr><tr><td colspan="2">... ...</td></tr></table>

### 反模式

![第 99 页](软件工程双语第5章-构件设计与UI设计课件.assets/第99页.webp)

原文：

反模式

描述一些对软件质量有负面影响的设计方案，描述在错误环境中，使用设计模式的后果

<table><tr><td>反模式名称</td><td></td><td>模式名称</td><td>Blob</td></tr><tr><td>Big ball of mud</td><td>一个大泥球✧ 一个没有可识别结</td><td>问题</td><td>单个类具有大量的属性、操作,或者两者都有。</td></tr><tr><td>Stovepipe system</td><td>炉管系统✧ 一个几乎不可维护</td><td rowspan="3">症状和后果</td><td rowspan="3">✧ 封装在单个类中的不相关属性和操作的完全不同的集合。✧ 属性和操作的整体缺乏凝聚力是the Blob的典型特征。✧ 具有关联的简单数据对象类的单个控制器类。✧ 一个控制器类封装了整个功能,就像一个过程主程序。✧ Blob限制了在不影响其他对象功能的情况下修改系统的能力。✧ 对系统中其他对象的修改也可能影响Blob的类。✧ Blob类通常过于复杂,无法重用和测试。✧ Blob类加载到内存中的成本可能很高,并且使用了过多的资源。</td></tr><tr><td>Boat anchor</td><td>船锚✧ 保留不再有任何用</td></tr><tr><td>Lava flow</td><td>熔岩流✧ 保留不需要的(冗贵或会产生不可预</td></tr><tr><td>Spaghetti code</td><td>意大利面条代码✧ 结构难以理解的程</td><td rowspan="2">典型原因</td><td rowspan="2">✧ 缺乏面向对象的体系结构。✧ 团队可能缺乏适当的抽象技能。✧ 缺乏定义的软件体系结构。✧ 缺乏对架构设计的编程语言支持。✧ 在迭代项目中,开发人员倾向于向现有类添加一些功能。✧ 在需求分析过程中定义系统体系结构通常会导致Blob。</td></tr><tr><td>Copy and paste programming</td><td>复制粘贴编程✧ 多次复制现有代码</td></tr><tr><td>Silver bullet</td><td>银弹✧ 假设最喜欢的技术</td><td rowspan="2">解决方案</td><td rowspan="2">✧ 该解决方案涉及一种形式的再保理。✧ 关键是将行为从Blob中移除。✧ 以使Blob不那么复杂的方式将行为重新分配给其他数据对象。</td></tr><tr><td>Programming by permutation</td><td>通过排列编程✧ 尝试通过连续修改</td></tr><tr><td colspan="2"></td><td colspan="2">... ...</td></tr></table>

### 可用性准则

![第 100 页](软件工程双语第5章-构件设计与UI设计课件.assets/第100页.webp)

原文：

可用性准则

预测：应用应能预测用户的下一个动作

传达：界面应能传达由用户启动的任何活动的状态

一致：导航控制、菜单、图标和美学风格（如颜色、形状和布局）的使用，应在整个应用中保持一致

自律：界面应辅助用户在整个应用中移动，但也应该坚持使用已经为应用建立起来的导航习惯

效率：应用的设计和界面，应该优化用户的工作效率

灵活性：界面应足够灵活，既能使一些用户直接完成任务，也能使另一些用户以一种比较随意的方式浏览应用

关注点：界面（及界面表示的内容）应该关注用户正在完成的任务

人机界面对象：对于WebApp和移动App，使用已开发的可复用人机界面对象库

缩短等待时间：应用不应该让用户等待内部操作的完成（例如，下载一个复杂的图形图像），而应该利用多任务处理方式，从而使用户继续他的处理工作，看起来就像前面的操作已经完成一样

学习能力：应用应将用户的学习时间减到最少，并且一旦用户已经学习过了，当再次访问此应用时，将所需要的再学习时间减到最少

隐喻：只要隐喻适合应用和用户，使用交互隐喻的界面就更容易学习和使用。

易读性：界面展示的所有信息对于老人和年轻人都应该是易读的。

跟踪状态：应跟踪和保存用户状态，使用户能够退出系统，稍后返回系统时又能回到退出的地方

可视化导航：设计合理的界面，提供“用户待在同一个地方，工作被带到他们面前”的设想

### 可访问性准则

![第 101 页](软件工程双语第5章-构件设计与UI设计课件.assets/第101页.webp)

原文：

可访问性准则

应用的可访问性：随着计算应用变得无处不在，软件工程师必须确保界面设计中包含使有特殊要求的用户易于访问的机制。

响应时间：系统响应时间包括两个重要的属性：时间长度和可变性。

帮助设施：几乎所有计算机交互式系统的用户都时常需要帮助。现代软件均提供联机帮助，用户可以不离开用户界面就解决问题。

错误处理通常：交互式系统给出的出错消息和警告应具备以下特征：

1. 以用户可以理解的语言描述问题

2. 应提供如何从错误中恢复的建设性意见；

3. 应指出错误可能导致哪些不良后果（比如破坏数据文件），以便用户检查是否出现了这些情况（或者在已经出现的情况下进行改正）；

4. 应伴随着视觉或听觉上的提示；

5. 永远不应该把错误归咎于用户。

菜单和命令：使用面向窗口的点选界面减少了对键入命令的依赖。重要的是：确保每个菜单选项都有一个命令版本，使命令易于用户键入，使命令易于记忆，允许命令缩写，确保菜单标签不言自明，确保子菜单与主菜单项，并确保命令约定适用于整个应用程序系列。

国际化：软件工程师和他们的经理往往会低估建立一个适应不同国家和不同语言需要的用户界面所应付出的努力和技能。

### Homework after class

![第 102 页](软件工程双语第5章-构件设计与UI设计课件.assets/第102页.webp)

原文：

Homework after class

1. How does the object-oriented view of component-level design differ from the traditional view?

2. What are the advantages of component-based software engineering?

3. What are the steps used to complete the component-level design for a software development project?

4. What principles should be followed when building any user interface?

5. What framework activities need to be completed in the development process of user interface evolution (or spiral)?

6. What things you need to do in user experience analysis if you seek to “understand the problem before you attempt to design a solution.”?

7. How to evaluate user interface design before building a working computer prototype?
