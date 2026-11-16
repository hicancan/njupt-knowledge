---
title: 《Java程序设计》小测试题
kind: 习题
course: Java软件开发
term: 2017-2018-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0302281C%E3%80%91JAVA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/JAVA%E5%B0%8F%E6%B5%8B_%E8%AF%95%E9%A2%98_20172018S2.doc
---

# 《Java程序设计》小测试题

原件经识别和整理；“参考解答”是我们补的。

## 一、选择题（每题均有 1 个或 1 个以上正确答案）

### 选择 1

类 A 定义如下，可正确替换 `//here` 的选项是 ( )

```java
public class A {
    public void amethod(int i) { }
    //here
}
```

- A. `public int amethod(int z) { }`
- B. `public int amethod(int i, int j) { return 99; }`
- C. `protected void amethod(long l) { }`
- D. `private void anothermethod() { }`

答案：B、C、D
知识点：[方法的声明、调用、按值/按引用参数传递及方法的重载(Overloading)](../../../topics/Java开发/方法的定义与重载.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 2

下面正确的语句是 ( )

- A. `boolean b = -1;`
- B. `boolean b2 = false;`
- C. `int i = 019;`
- D. `char c = 99;`

答案：B、D
知识点：[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[成员变量与局部变量的作用范围、默认值及final终止变量](../../../topics/Java开发/变量的作用域与初始化.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 3

下面正确的语句是 ( )

- A. `System.out.println(1 + 1);`
- B. `int i = 2 + '2';`
- C. `String s = “on” + ‘one’;`
- D. `int z = 025;`

答案：A、B、D
知识点：[基本数据类型的隐式转换与强制转换规则](../../../topics/Java开发/数据类型转换.md)、[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 4

“result” 是一个布尔变量，下面表达式正确的是 ( )

- A. `result=true;`
- B. `if(result){ …}`
- C. `if(result!=0){ …}`
- D. `result=1;`

答案：A、B
知识点：[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[if-else、switch、while、do-while、for语句及break/continue/return分支控制](../../../topics/Java开发/流程控制语句.md)

### 选择 5

程序片段代码如下，当 m 取何值时仅输出 Default ( switch(m){ case 0:System.out.println(“Case 0”); default:System.out.println(“Default”); }

- A. 0
- B. 1
- C. 2
- D. 3

答案：B、C、D
知识点：[if-else、switch、while、do-while、for语句及break/continue/return分支控制](../../../topics/Java开发/流程控制语句.md)

### 选择 6

下面的哪些声明是不合法的（ ）

- A. `public protected amethod(int i)`
- B. `public void amethod(int i)`
- C. `public void amthod(void)`
- D. `void public amethod(int i)`

答案：A、C、D
知识点：[方法的声明、调用、按值/按引用参数传递及方法的重载(Overloading)](../../../topics/Java开发/方法的定义与重载.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 7

某程序如下, 对其运行结果描述正确的是（ ）

```java
public class PainOrGain {
    private static Random rnd = new Random();
    public static void main(String[] args) {
        StringBuffer word = null;
        switch(rnd.nextInt(2)) {
            case 0: word = new StringBuffer('P');
            case 1: word = new StringBuffer('G');
        }
        word.append('a');
        word.append('i');
        word.append('n');
        System.out.println(word);
    }
}
```

- A. 随机输出 Pain 或 Gain
- B. 总是输出 Gain
- C. 总是输出 Pain
- D. 以上都不正确

答案：D
知识点：[if-else、switch、while、do-while、for语句及break/continue/return分支控制](../../../topics/Java开发/流程控制语句.md)、[基本数据类型的隐式转换与强制转换规则](../../../topics/Java开发/数据类型转换.md)、[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)

### 选择 8

某程序如下, 对其描述正确的是（ ）

```java
class B {
    public static void main(String args[]) {
        int p;
        int j = 10;
        j = p;
    }
}
```

- A. 程序编译时出现 1 处错误
- B. 程序编译时出现 2 处错误
- C. 程序运行时出现错误
- D. 程序编译和运行都没有错误

答案：A
知识点：[成员变量与局部变量的作用范围、默认值及final终止变量](../../../topics/Java开发/变量的作用域与初始化.md)、[Java平台、JVM定义及编译解释执行原理](../../../topics/Java开发/Java平台与JVM.md)
