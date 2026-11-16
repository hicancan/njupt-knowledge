---
title: 《Java语言程序设计》期末考试模拟试题
kind: 期末试卷
course: Java软件开发
term: 2015-2016-2
source: batch-2:JAVA/15级java试卷(1) (1).doc
---

# 《Java语言程序设计》期末考试模拟试题

原件经识别和整理；“参考解答”是我们补的。

## 一、单选择题（每小题 2 分，共 10 分）

### 选择 1

编译 Java Application 源程序文件将产生相应的字节码文件，这些字节码文件的扩展名为（ ）。

- A. .java
- B. .class
- C. .html
- D. .exe

答案：B。

知识点：[Java平台、JVM定义及编译解释执行原理](../../../topics/Java开发/Java平台与JVM.md)、[第一个Java程序（源文件创建、javac编译、类定义、main方法）](../../../topics/Java开发/HelloWorld程序结构.md)

### 选择 2

设 x = 1，y = 2，z = 3，则表达式 `y += z-- / ++x` 的值是（ ）。

- A. 3
- B. 3.5
- C. 4
- D. 5

答案：A。

知识点：[算术、关系、逻辑、位运算、移位、条件及复合赋值运算符与优先级](../../../topics/Java开发/运算符与表达式.md)、[基本数据类型的隐式转换与强制转换规则](../../../topics/Java开发/数据类型转换.md)

### 选择 3

在 Java Applet 程序用户自定义的 Applet 子类中，一般需要重载父类的（ ）方法来完成一些画图操作。

- A. start()
- B. stop()
- C. init()
- D. paint()

答案：D。

知识点：[Java SE、Java EE、Java ME的区别与应用领域](../../../topics/Java开发/Java版本体系.md)、[对象(Object)和类(Class)的概念、实例变量与方法](../../../topics/Java开发/对象与类的概念.md)

### 选择 4

不允许作为类及类成员的访问控制符的是（ ）。

- A. public
- B. private
- C. static
- D. protected

答案：C。

知识点：[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)、[对象(Object)和类(Class)的概念、实例变量与方法](../../../topics/Java开发/对象与类的概念.md)

### 选择 5

为 AB 类的一个无形式参数无返回值的方法 method 书写方法头，使得使用类名 AB 作为前缀就可以调用它，该方法头的形式为（ ）。

- A. static void method()
- B. public void method()
- C. final void method()
- D. abstract void method()

答案：A。

## 二、填空题（每空格 1 分，共 20 分）

知识点：[方法的声明、调用、按值/按引用参数传递及方法的重载(Overloading)](../../../topics/Java开发/方法的定义与重载.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 填空 1

开发与运行 Java 程序需要经过的三个主要步骤为 ==编辑源程序==、==编译生成字节码== 和 ==解释运行字节码==。

知识点：[Java平台、JVM定义及编译解释执行原理](../../../topics/Java开发/Java平台与JVM.md)

### 填空 2

如果一个 Java Applet 源程序文件只定义有一个类，该类的类名为 MyApplet，则类 MyApplet 必须是 ==Applet== 类的子类并且存储该源程序文件的文件名为 ==MyApplet==。

知识点：[Java SE、Java EE、Java ME的区别与应用领域](../../../topics/Java开发/Java版本体系.md)、[第一个Java程序（源文件创建、javac编译、类定义、main方法）](../../../topics/Java开发/HelloWorld程序结构.md)

### 填空 3

如果一个 Java Applet 程序文件中定义有 3 个类，则使用 Sun 公司的 JDK 编译器 javac.exe 编译该源程序文件将产生 ==3== 个文件名与类名相同而扩展名为 ==.class== 的字节码文件。

知识点：[第一个Java程序（源文件创建、javac编译、类定义、main方法）](../../../topics/Java开发/HelloWorld程序结构.md)、[Java平台、JVM定义及编译解释执行原理](../../../topics/Java开发/Java平台与JVM.md)

### 填空 4

在 Java 的基本数据类型中，char 型采用 Unicode 编码方案，每个 Unicode 码占用 ==2== 字节内存空间，这样，无论是中文字符还是英文字符，都是占用 ==2== 字节内存空间。

知识点：[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 填空 5

设 x = 2，则表达式 `(x++) / 3` 的值是 ==1==。

知识点：[算术、关系、逻辑、位运算、移位、条件及复合赋值运算符与优先级](../../../topics/Java开发/运算符与表达式.md)、[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[成员变量与局部变量的作用范围、默认值及final终止变量](../../../topics/Java开发/变量的作用域与初始化.md)

### 填空 6

若 x = 5，y = 10，则 `x < y` 和 `x >= y` 的逻辑值分别为 ==true== 和 ==false==。

知识点：[算术、关系、逻辑、位运算、移位、条件及复合赋值运算符与优先级](../../../topics/Java开发/运算符与表达式.md)、[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)

### 填空 7

==抽象(abstract)方法== 是一种仅有方法头，没有具体方法体和操作实现的方法，该方法必须在抽象类之中定义。==最终(final)方法== 方法是不能被当前类的子类重新定义的方法。

知识点：[类之间的继承、聚合、合成、依赖关系及开闭原则(OCP)](../../../topics/Java开发/类之间的关系.md)、[成员变量与局部变量的作用范围、默认值及final终止变量](../../../topics/Java开发/变量的作用域与初始化.md)

### 填空 8

创建一个名为 MyPackage 的包的语句是 ==package MyPackage;==，该语句应该放在程序的位置为：==应该在程序第一句==。

知识点：[第一个Java程序（源文件创建、javac编译、类定义、main方法）](../../../topics/Java开发/HelloWorld程序结构.md)

### 填空 9

设有数组定义：`int MyIntArray[] = { 10, 20, 30, 40, 50, 60, 70 };` 则执行以下几个语句后的输出结果是 ==120==。

知识点：[数组的声明、初始化、访问、数组复制及数组的数组](../../../topics/Java开发/一维数组与多维数组.md)、[算术、关系、逻辑、位运算、移位、条件及复合赋值运算符与优先级](../../../topics/Java开发/运算符与表达式.md)

### 填空 10

在 Java 程序中，通过类的定义只能实现 ==单== 重继承，但通过接口的定义可以实现 ==多== 重继承关系。

## 三、写出下列程序完成的功能（每小题 5 分，共 20 分）

知识点：[接口(Interface)用于定义协议或行为的作用](../../../topics/Java开发/接口的基础概念.md)、[类之间的继承、聚合、合成、依赖关系及开闭原则(OCP)](../../../topics/Java开发/类之间的关系.md)、[对象(Object)和类(Class)的概念、实例变量与方法](../../../topics/Java开发/对象与类的概念.md)
