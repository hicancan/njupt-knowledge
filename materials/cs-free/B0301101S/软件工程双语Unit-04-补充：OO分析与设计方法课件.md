---
title: 《软件工程（双语）》Unit 04 补充：OO分析与设计方法（课件）
kind: 课件
course: 软件工程（双语）
term: 2020-2021-2
source: cs-free:【B0301101S】软件工程（双语）/课件（PPT）/软件工程（双语）-课件-20-21-2.7z/Unit_04_补充_OO分析与设计方法.ppt
---

# 《软件工程（双语）》Unit 04 补充：OO分析与设计方法（课件）

原件的每一页，下面附识别出的文字。

### OOA & OOD & UML分析与设计的基础

![第 1 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第1页.webp)

原文：

OOA & OOD & UML分析与设计的基础

王传栋

南京邮电大学计算机学院

### 引子

![第 2 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第2页.webp)

原文：

引子

计算两个数的平均数过程思维

public static void main(String arg

int[] i = {1,2,3,4,5,6,7};

System.out.printIn(getAve(

### 引子

![第 3 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第3页.webp)

原文：

引子

计算两个数的平均数❑ OO思维：类与对象

### 引子

![第 4 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第4页.webp)

原文：

引子

:Main

计算两个数的平均数❑ OO思维：类与对象

Average

ExamMarks

\+ main ()

\- marks: ataSet;

\+ enterMark(float m); + average();

DataSet

\- data[]:float;

\- items:int;

\+ DataSet();

\+ addDataPoint(float d);

\+ mean();

\+ getSize();

new ExamMarks(

exam :ExamMarks

enterMark(56)

new DataSet()

marks : DataSet

addDataPoint(56)

enterMark(72)

average()

AddDataPoint(72)

mean()

getSize()

return 64

return 64 return 2 -7 1 E-

### OO思想

![第 5 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第5页.webp)

原文：

OO思想

◼ 简介

❑ 从现实世界中客观存在的事物（即对象）出发来构造软件系统

❑ 在系统构造中尽可能运用人类的自然思维方式，强调直接以问题域（现实世界）中的事物为中心来思考问题，认识问题，并根据这些事物的本质特点，把它们抽象地表示为系统中的对象，作为系统的基本构成单位

❑ 使系统直接地映射问题域，使得求解域与问题域一致，保持问题域中事物及其相互关系的本来面貌

◼ OO：采用封装、继承、多态和抽象等方法实现

❑ 面向对象的分析（OOA，Object Oriented Analysis）

❑ 面向对象的设计（OOD，Object Oriented Design）

❑ 面向对象的编程（OOP，Object Oriented Programming）

5

### OO基本概念

![第 6 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第6页.webp)

原文：

OO基本概念

◼ 类、对象、实例

职员

class staff{

客观世界nameagesalarypublic staff {}

类

职员

抽象

\- 姓名

-年龄

-工资

实例化

+显示姓名（）

+显示年龄（）

+修改姓名（）

+领取工资（）

计算机世界

staff zhangsan = new staff( )

对象

张三：职员

-姓名=‘张三’

-年龄=29

-工资= 5000

实例化

李四：职员

-姓名=‘李四’

-年龄=31

-工资= 3000

6

### OO基本概念

![第 7 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第7页.webp)

原文：

OO基本概念

### 第 8 页

![第 8 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第8页.webp)

### OO基本概念

![第 9 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第9页.webp)

原文：

OO基本概念

◼ 类、对象、实例

是对具有相同数据和相同操作的一组相似对象的抽象定义实例，以某个特定的类为“样板”建立的一个具体的对象

### OO基本概念

![第 10 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第10页.webp)

原文：

OO基本概念

◼ 类：

❑ 是对具有相同数据和相同操作的一组相似对象的抽象定义

❑ 理解

◼ 是对具有相同属性（不同值）和行为的一组对象的描述◼ 是支持继承的抽象数据类型，是对象实例化的模版

对象与实例

❑ 一个对象就是类的一个实例

❑ 实例化：以某个特定的类为“样板”建立的一个具体的对象

类定义了对象的特征，分为属性和操作属性，定义类实例存储的数据，是对客观实体所具有共同性质的抽象，类实例化的每个对象都有自己特有的属性值操作：也称方法，定义类实例的动态行为（算法）

10

### OO基本概念

![第 11 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第11页.webp)

原文：

OO基本概念

封装与信息隐藏

public class Driver { private String name;

public Driver(String name) { super(); this.nàme = name;}

public String getName() { return name; }

public void setName(String name) { this.name = name;}

public void, drive(Car c) { c.go(new Address(“东北”));}

public void drive(Car c, Address dest) c.go(dest);}

公共（public）

私有（private）

保护（protected）

实现（implementation）

### OO基本概念

![第 12 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第12页.webp)

原文：

OO基本概念

封装与信息隐藏

❑ 封装有清晰的边界，私有数据和操作代码封装在模块内；

❑ 有确定的接口（即协议），用于接受消息；

❑ 受保护的内部实现，只能模块内，访问功能细节和数据

面向对象的封装

❑ 信息隐藏，实现细节（数据和实现操作的代码）组织在对象内

❑ 对象就像个黑盒子，外界看不到，更不能直接访问或修改隐藏的数据和代码

❑ 对象类的实质就是抽象数据类型，类把数据、操作的说明（接口）与数据的表达、操作的实现分离开来，其他对象仅通过接口（值域及对数据可施加的操作）向该对象传递消息

12

### OO基本概念

![第 13 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第13页.webp)

原文：

OO基本概念

继承和类等级

派生类自动地共享基类中定义的属性和服务只有public和protected的属性和服务才被继承❑ 继承分单继承和多继承，多继承易产生二义性

❑ 继承有传递性

QClass Specification for Teacher
<table><tr><td colspan="2">Relations</td><td colspan="2">Components</td><td colspan="2">Nested</td><td>Files</td></tr><tr><td colspan="2">General</td><td>Detail</td><td colspan="2">Operations</td><td colspan="2">Attributes</td></tr><tr><td colspan="7">Show inherit</td></tr><tr><td></td><td>St...</td><td>Name</td><td>Pa...</td><td>Type</td><td colspan="2">Ini...</td></tr><tr><td></td><td></td><td>身高</td><td colspan="4">Person</td></tr><tr><td></td><td></td><td>健康状况</td><td colspan="4">Person</td></tr><tr><td></td><td></td><td>姓名</td><td colspan="4">Teacher</td></tr><tr><td></td><td></td><td>性别</td><td colspan="4">Teacher</td></tr></table>

吃饭 睡觉 行走 交友(0)

13

### OO基本概念

![第 14 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第14页.webp)

原文：

OO基本概念

继承和类等级❑ 大学教师

QClass Specification for 大学老师

<table><tr><td colspan="2">Relations</td><td colspan="2">Components</td><td colspan="2">Nested</td><td>Files</td></tr><tr><td colspan="2">General</td><td colspan="2">Detail</td><td colspan="2">Operations</td><td>Attributes</td></tr><tr><td colspan="7">Show inherit</td></tr><tr><td></td><td>St...</td><td>Name</td><td>Pa...</td><td>Type</td><td colspan="2">Ini...</td></tr><tr><td></td><td colspan="2">身高</td><td colspan="4">Person</td></tr><tr><td></td><td colspan="2">健康状况</td><td colspan="4">Person</td></tr><tr><td></td><td colspan="2">姓名</td><td colspan="4">Teachers</td></tr></table>

14

### OO基本概念

![第 15 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第15页.webp)

原文：

OO基本概念

继承和类等级❑ 小学教师

QClass Specification for 小学老师

Class Specification for 小学老师

15

### OO基本概念

![第 16 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第16页.webp)

原文：

OO基本概念

消息、协议和服务

public void drive(Car c, Address dest)

协议的一部分

服务

消息

16

### OO基本概念

![第 17 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第17页.webp)

原文：

OO基本概念

消息

❑ 是用于请求某个对象提供某个服务的一种处理机制，是对象之间相互联系和通信的唯一途径

❑ 形式上，就是请求某个对象执行“定义它的类中所定义的某个操作”的规格说明，由三部分组成 ：

接受消息的对象

消息选择符 （消息名）

零个或多个变元（参数）

d.drive(c, ad);

myCircle.Show(Green);

❑ 实质

Circle myCircle = new Circle();

❑ 一次函数调用，要求调用某个对象封装的函数提供服务

有返回值 / 无返回值

17

### OO基本概念

![第 18 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第18页.webp)

原文：

OO基本概念

◼ 服务

❑ 服务是对象的某种处理，是一系列控制和操作过程

❑ 服务是通过其他对象的申请、调用（消息传递）来实现的

❑ 接受消息的对象，按照消息的要求提供相应的服务

◼ 目标对象

◼ 服务名称

◼ 服务变量

◼ 服务内容：实现服务的一组控制和操作指令

public class Driver { public class Test { public static void main(String[] args) {

d.drive(c, ad);

### OO基本概念

![第 19 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第19页.webp)

原文：

OO基本概念

19

### OO基本概念

![第 20 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第20页.webp)

原文：

OO基本概念

重载

函数重载：同一个作用域中，若干个参数特征不同的函数，使用相同的函数名

运算符重载：同一个运算符可以施加于不同类型的操作数

重载机制

静态联编（static binding）

在程序编译时，根据函数变元的个数和类型，决定使用同名函数的哪个实现代码

提高OO程序灵活性和可读性

20

### OO基本概念

![第 21 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第21页.webp)

原文：

OO基本概念

多态

通过重写(override)父类的同名操作，使不同的子类对象和父类对象接受同一消息，却提供不同服务

不同层次的类共享一个行为(函数名、参数和返回值类型都相同)，但行为实现却不同多 态的发生有 3 个条件<sub>：</sub>

(1) 继承或实现

(2) 子类中重写父类（接口）的方法

(3) 父类引用指向子类对象

多态机制

❑ 动态联编(dynamic binding)，也称滞后联编(late binging)运行时，消息发送对象不知道谁将接收消息，依赖接收对象以一种恰当的方式解释消息，根据消息接收对象所属的类，决定实现什么样的行为，享受什么样的服务

❑ 增强OO系统的灵活性，减少信息冗余，提高软件的可重用性和可扩充性

21

### 第 22 页

![第 22 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第22页.webp)

### OO基本概念

![第 23 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第23页.webp)

原文：

OO基本概念

◼ 多态：以类继承的方式实现

23

### OO基本概念

![第 24 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第24页.webp)

原文：

OO基本概念

### OO类图

![第 25 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第25页.webp)

原文：

OO类图

◼ 示例

### 类关系

![第 26 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第26页.webp)

原文：

类关系

继承（泛化）关系(Generalization)

❑ 也称为“is-a-kind-of”关系，用于描述父类与子类之间的关系，父类又称作基类或超类，子类又称作派生类

❑ UML中用带空心三角形的直线来表示

❑ 在Java语言中使用extends关键字、在C++/C#中使用冒号“：”来实现

Student

\- studentNo : String

\+ study () : void

public class Person

protected String name; protected int age; public void move()

public void say()

public class Student extends Person

private String studentNo; public void study()

26

### 类关系

![第 27 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第27页.webp)

原文：

类关系

Form

\- buttons : Button[]

1..1

0..

Button

关联关系(Association)

❑ 类与类之间的一种结构化关系，用于表示类对象与另一类对象之间有联系

UML类图中，用实线连接有关联的对象所对应的类，编程实现关联关系时，通常将一个类的对象作为另一个类的属性

类图表示常在关联线上标注角色名和重数

Node

contains

\- subNode : Node

LoginForm

\- loginButton : JButton

contains

JButton

Customer - products : Product[]

purchases

is sold to

Product - customer : Customer public class LoginForm { private JButton loginButton;

public class JButton

public class Customer { private Product[] products; }

public class Product { private Customer customer; }

public class Node { private Node subNode;

### 类关系

![第 28 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第28页.webp)

原文：

类关系

聚合与组合：整体与部分关系❑ 聚合关系中成员类是整体类的一部分，即成员对象是整体对象的一部分，但成员对象可以脱离整体对象独立存在UML中用带空心菱形的直线表示

Car

\- engine : Engine

Head

❑ 组合关系也表示类之间整体和部分的关系但部分和整体具有统一的生存期，一旦整体对象不存在，部分对象也将不存在UML中用带实心菱形的直线表示

\+ Car (Engine engine)

\- mouth : Mouth

\+ setEngine (Engine engine) : void

has

Mouth

\+ Head ()

public class Car

public void setEngine(Engine engine)

private Engine engine; public Car(Engine engine)

this.engine = engine;

public class Engine

Engine

contains

public class Head

mouth = new MouthQ;

public class Mouth

### 类关系

![第 29 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第29页.webp)

原文：

类关系

依赖关系(Dependency)

是一种使用关系，特定事物的改变有可能会影响到使用该事物的其他事物在需要表示一个事物使用另一个事物时使用依赖关系。大多数情况下，依赖关系体现在某个类的方法使用另一个类的对象作为参数（或返回值，或局部变量）

UML图中用带箭头的虚线表示，由依赖的一方指向被依赖的一方

Driver

Car

\+ drive (Car car)

\+ move () : void

car.move():

29

### 类关系

![第 30 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第30页.webp)

原文：

类关系

接口与实现关系(Realization)

❑ 接口是一种特殊的抽象类，之间也可以有继承关系和依赖关系

接口和类之间还存在一种实现关系，在这种关系中，类实现了接口，类中的操作实现了接口中所声明的操作

❑ UML中用带空心三角形的虚线来表示

30

### OO类图

![第 31 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第31页.webp)

原文：

OO类图

◼ 示例

### OO类图

![第 32 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第32页.webp)

原文：

OO类图

◼ 示例

### 建模工具

![第 33 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第33页.webp)

原文：

建模工具

◼ UML

Object-Oriented Software Engineering(OOSE)

UML

### UML— 5视图

![第 34 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第34页.webp)

原文：

UML— 5视图

结构视图

实现视图

用户视图：以用户的观点行为视 行为视图表示系统的目标，它是所有视图的核心，该视图描述系统的需求。

用户视图

环境视图

结构视图：表示系统的静态行为，描述系统的静态元素，如包、类与对象，以及它们之间的关系。

行为视图：表示系统的动态行为，描述系统的组成元素如对象在系统运行时的交互关系。

实现视图：表示系统中逻辑元素的分布，描述系统中物理文件以及它们之间的关系。

环境视图：表示系统中物理元素的分布，描述系统中硬件设备以及它们之间的关系。

34

### Architectural Descriptions

![第 35 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第35页.webp)

原文：

Architectural Descriptions

35

### UML— 9图

![第 36 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第36页.webp)

原文：

UML— 9图

用例图(Use Case Diagram)

❑ 又称为用况图，对应于用户视图

在用例图中，使用用例来表示系统的功能需求

用例图用于表示多个外部执行者与系统用例之间以及用例与用例之间的关系

用例图与用例说明文档(UseCase Specification)是常用的需求建模工具，也称为用例建模

### UML— 9图

![第 37 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第37页.webp)

原文：

UML— 9图

类图(Class Diagram)类图对应于结构视图

使用类来描述系统的静态结构，类图包含类和它们之间的关系，它描述系统内所声明的类

没有描述系统运行时类的行为

用例图与类图是使用频率最高的两种图

### 38

![第 38 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第38页.webp)

原文：

38

### 第 39 页

![第 39 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第39页.webp)

### UML— 9图

![第 40 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第40页.webp)

原文：

UML— 9图

类图示例

### UML——9图

![第 41 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第41页.webp)

原文：

UML——9图

对象图(Object Diagram)

对应于结构视图

对象图是类图在某一时刻的一个实例，用于表示类的对象实例之间的关系。

### UML— 9图

![第 42 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第42页.webp)

原文：

UML— 9图

状态图(State Diagram)

❑ 对应于行为视图

状态图用来描述一个特定对象的所有可能状态及其引起状态转移的事件

一个状态图包括一系列对象的状态及状态之间的转换

Public class window { int x,y ; int length, width;

Public class test { window w = new window(); w.open; ... ... ; w. minimize; w.restore; ... ...; w. maximize;

### UML——9图

![第 43 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第43页.webp)

原文：

UML——9图

状态图示例

### UML— 9图

![第 44 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第44页.webp)

原文：

UML— 9图

活动图(Activity Diagram)对应于行为视图

活动图用来表示系统中各种活动的次序，既可用来描述用例的工作流程，也可以用来描述类中某个方法的操作行为。

44

### UML——9图

![第 45 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第45页.webp)

原文：

UML——9图

顺序图(Sequence Diagram)

❑ 又称为时序图或序列图

❑ 对应于行为视图

顺序图用于表示对象之间的交互，重点表示对象之间发送消息的时间顺序。

ATM登录

45

### UML——9图

![第 46 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第46页.webp)

原文：

UML——9图

顺序图示例

### UML— 9图

![第 47 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第47页.webp)

原文：

UML— 9图

通信图(CommunicationDiagram)

❑ 在UML1.x中称为协作图，对应于行为视图

通信图展示了一组对象、这些对象间的连接以及它们之间收发的消息

它与顺序图是同构图，也就是它们包含了相同的信息，只是表达方式不同而已，通信图与顺序图可以相互转换。

### UML——9图

![第 48 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第48页.webp)

原文：

UML——9图

组件图(Component Diagram)

❑ 又称为构件图，对应于实现视图

❑ 组件图用于描述每个功能所在的组件位置以及它们之间的关系。

### UML——9图

![第 49 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第49页.webp)

原文：

UML——9图

部署图(Deployment Diagram)❑ 又称为实施图，对应于环境视图

❑ 部署图用于描述软件中各个组件驻留的硬件位置以及这些硬件之间的交互关系。

### UML— 新增4图

![第 50 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第50页.webp)

原文：

UML— 新增4图

包图(Package Diagram)

❑ UML2.0新增，对应于结构视图

❑ 包图描述包与包之间的关系

包是一种把元素组织到一起的通用机制，如可以将多个类组织成一个包。

◼ 组合结构图(Composite Structure Diagram)

UML2.0新增，对应于结构视图

❑ 组合结构图将每一个类放在一个整体中，从类的内部结构来审视一个类。组合结构图可用于表示一个类的内部结构，用于描述一些包含复杂成员或内部类的类结构。

50

### UML— 新增4图

![第 51 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第51页.webp)

原文：

UML— 新增4图

定时图(Timing Diagram)

❑ UML2.0新增，对应于行为视图

定时图采用一种带数字刻度的时间轴来精确地描述消息的顺序，而不是像顺序图那样只是指定消息的相对顺序，而且它还允许可视化地表示每条生命线的状态变化，当需要对实时事件进行定义时，定时图可以很好地满足要求。

◼ 交互概览图(Interaction Overview Diagram)

❑ UML2.0新增图，对应于行为视图

交互概览图是交互图与活动图的混合物，可以把交互概览图理解为细化的活动图，在其中的活动都通过一些小型的顺序图来表示；也可以将其理解为利用标明控制流的活动图分解过的顺序图。

注：在 UML 中，顺序图、通信图、定时图和交互概览图又统称交互图(Interactive Diagram)，交互图是表示各对象如何依据某种行为进行协作的模型，通常可以使用一个交互图来表示和说明一个用例的行为。

51

### OO的软件过程

![第 52 页](软件工程双语Unit-04-补充：OO分析与设计方法课件.assets/第52页.webp)

原文：

OO的软件过程

需求获取

inception elicitation negotiation

Requirements Analysis

分析建模

basic requirements (elaborate)

❑ 场景建模

❑ 类建模（数据建模）

数据流建模

行为建模 （顺序图和状态图）

设计建模 （复用设计模式）

❑ 体系结构设计数据流图 → 结构图

❑ 构件设计

❑ 界面设计

◼ OO编程

Scenario-based models e.g., use cases user stories

Class models e.g., class diagrams collaboration diagrams

data functional behavior design

Behavioral models e.g., state diagrams sequence diagrams

Flow models e.g., DFDs data models

architecture, interface, and component

Scenerio-based elements Use cases - text Use-case diagrams Activity diagrams Swimlane diagrams

Class-based elements

Class diagrams Analysis packages CRC models Collaboration diagrams

Component-Level Design

Interface Design

Architectural Design

Data/Class Design

Design Model
