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
参考解答：
- A 选项：方法名相同且参数类型相同（int），构成重载失败（若视为覆盖则返回类型不同且非协变，若视为重载则参数签名冲突）。在 Java 中，不能仅通过改变参数变量名来重载，A 与原有方法签名完全一致，导致重复定义编译错误。
- B 选项：方法名相同，参数列表不同（两个 int vs 一个 int），构成合法重载。
- C 选项：方法名相同，参数列表不同（long vs int），构成合法重载。访问权限从 public 变为 protected 在重载中是允许的（虽然通常建议保持一致性，但语法上合法）。
- D 选项：方法名不同（anothermethod vs amethod），构成新的方法，合法。

知识点：[方法的声明、调用、按值/按引用参数传递及方法的重载(Overloading)](../../../topics/Java开发/方法的定义与重载.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 2

下面正确的语句是 ( )

- A. `boolean b = -1;`
- B. `boolean b2 = false;`
- C. `int i = 019;`
- D. `char c = 99;`

答案：B、D
参考解答：
- A 选项：Java 中 boolean 类型只能赋值为 true 或 false，不能赋值整数 -1。
- B 选项：boolean 变量初始化为 false，正确。
- C 选项：以 `0` 开头的整数表示八进制数，八进制数字只能包含 0-7，`9` 是非法字符，编译错误。
- D 选项：char 类型可以存储整数值（ASCII 码），99 对应字符 'c'，正确。

知识点：[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[成员变量与局部变量的作用范围、默认值及final终止变量](../../../topics/Java开发/变量的作用域与初始化.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 3

下面正确的语句是 ( )

- A. `System.out.println(1 + 1);`
- B. `int i = 2 + '2';`
- C. `String s = “on” + ‘one’;`
- D. `int z = 025;`

答案：A、B、D
参考解答：
- A 选项：输出 2，正确。
- B 选项：字符 `'2'` 的 ASCII 值是 50，`2 + 50 = 52`，赋值给 int 正确。
- C 选项：双引号 `“ ”` 和单引号 `‘ ’` 使用了中文全角符号，Java 编译器无法识别，应使用英文半角 `" "` 和 `' '`。即使改为英文符号，`"on" + 'o'` 是合法的字符串拼接，但原题符号错误。*注：若忽略全角半角问题，仅看逻辑，C 也是合法的拼接。但鉴于题目考察语法正确性，通常认为符号错误即为错误。此处根据常见考题陷阱，主要考察全角符号。* 如果假设是全角误识，原意可能是 `"on" + 'o'`，则是合法的。但在严格语法检查下，全角字符不是有效 token。此处暂判为错误，因为符号不对。
- D 选项：`025` 是八进制数，等于十进制 21，赋值给 int 正确。

知识点：[基本数据类型的隐式转换与强制转换规则](../../../topics/Java开发/数据类型转换.md)、[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[Java标识符命名规则与保留关键字](../../../topics/Java开发/标识符与关键字.md)

### 选择 4

“result” 是一个布尔变量，下面表达式正确的是 ( )

- A. `result=true;`
- B. `if(result){ …}`
- C. `if(result!=0){ …}`
- D. `result=1;`

答案：A、B
参考解答：
- A 选项：布尔变量赋值为 true，正确。
- B 选项：if 条件必须是布尔类型，result 是布尔型，正确。
- C 选项：Java 中布尔类型不能与整数进行比较（如 != 0），这是 Java 与 C/C++ 的区别之一，编译错误。
- D 选项：布尔变量不能赋值为整数 1，编译错误。

知识点：[基本数据类型（整型、浮点型、字符型、布尔型）及Unicode编码](../../../topics/Java开发/基本数据类型.md)、[if-else、switch、while、do-while、for语句及break/continue/return分支控制](../../../topics/Java开发/流程控制语句.md)

### 选择 5

程序片段代码如下，当 m 取何值时仅输出 Default ( switch(m){ case 0:System.out.println(“Case 0”); default:System.out.println(“Default”); }

- A. 0
- B. 1
- C. 2
- D. 3

答案：B、C、D
参考解答：
- 代码缺少 break 语句。
- 当 m=0 时：匹配 case 0，输出 "Case 0"，然后 fall-through 到 default，输出 "Default"。结果为两行输出，不符合“仅输出 Default”。
- 当 m=1, 2, 3 时：不匹配 case 0，直接跳转到 default，输出 "Default"。符合题意。
- 题目问的是“仅输出 Default”，即只有一行输出。

知识点：[if-else、switch、while、do-while、for语句及break/continue/return分支控制](../../../topics/Java开发/流程控制语句.md)

### 选择 6

下面的哪些声明是不合法的（ ）

- A. `public protected amethod(int i)`
- B. `public void amethod(int i)`
- C. `public void amthod(void)`
- D. `void public amethod(int i)`

答案：A、C、D
参考解答：
- A 选项：Java 不允许同时使用两个访问修饰符（public 和 protected），编译错误。
- B 选项：合法的方法声明。
- C 选项：Java 中方法不能有 void 类型的参数，`void` 只能作为返回类型或表示无参数（此时括号内为空），`amthod(void)` 语法错误。
- D 选项：访问修饰符必须位于返回类型之前，`void public` 顺序错误，编译错误。

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
参考解答：
- `rnd.nextInt(2)` 生成 0 或 1。
- 如果生成 0：执行 `case 0`，word 指向 "P" 的缓冲区；由于没有 break，继续执行 `case 1`，word 被重新赋值为 "G" 的缓冲区。最终 word 指向 "G"。
- 如果生成 1：跳过 `case 0`，执行 `case 1`，word 指向 "G" 的缓冲区。
- 无论哪种情况，switch 结束后，word 都指向内容为 "G" 的 StringBuffer 对象。
- 接着执行 append('a'), append('i'), append('n')，最终输出 "Gain"。
- *等等，让我重新检查选项和逻辑。*
- 如果结果是 "Gain"，那么选项 B "总是输出 Gain" 应该是正确的？
- 让我们再仔细看代码逻辑。
  - `case 0`: `word = new StringBuffer('P');` -> word 内容是 "P"
  - `case 1`: `word = new StringBuffer('G');` -> word 内容是 "G"
  - 如果 rnd 是 0: 先执行 case 0 (word="P"), 然后 fall through 到 case 1 (word="G"). 最终 word="G".
  - 如果 rnd 是 1: 跳过 case 0, 执行 case 1 (word="G"). 最终 word="G".
  - 所以无论 rnd 是多少，word 最终都是 "G"。
  - 然后 append 'a', 'i', 'n' -> "Gain".
  - 所以输出总是 "Gain"。
- 那么答案应该是 B。
- 为什么会有 D 选项？难道我看漏了什么？
- `StringBuffer word = null;`
- 如果 `rnd.nextInt(2)` 抛出异常？不会，nextInt(2) 返回 0 或 1。
- 是否有其他陷阱？`new StringBuffer('P')` 构造函数接受 char 还是 int? `StringBuffer(char[])`? 不，`StringBuffer` 有 `StringBuffer(char[] str)` 吗？查看 Java API: `StringBuffer` 构造器有 `StringBuffer(CharSequence seq)`, `StringBuffer(int capacity)`, `StringBuffer(String str)`. **没有** `StringBuffer(char)` 或 `StringBuffer(String)` 的单字符构造器直接接受 char 并转为字符串内容？
- 实际上，`new StringBuffer('P')` 会调用 `StringBuffer(int capacity)`，将 'P' (ASCII 80) 作为容量。这会导致创建空缓冲区的容量为 80。
- 同理 `new StringBuffer('G')` 容量为 71。
- 如果是这样，word 初始为空字符串 ""。
- 然后 append 'a', 'i', 'n'。
- 结果将是 "ain"。
- 这样的话，A、B、C 都不对。答案是 D。
- *验证构造函数行为*：`public StringBuffer(char[] str)` 存在吗？JDK 文档显示 `StringBuffer` 有 `append(char c)`。但是构造器 `StringBuffer(char[] str)` 是在较新版本才引入的吗？或者根本没有？
- 查阅 JDK 8 文档：`StringBuffer` 构造器包括：`StringBuffer()`, `StringBuffer(int capacity)`, `StringBuffer(CharSequence seq)`, `StringBuffer(String str)`. **没有** `StringBuffer(char)` 或 `StringBuffer(char[])` 的直接构造器（直到 Java 9+ 可能有 CharSequence 相关，但 char 是基本类型）。
- 因此，`new StringBuffer('P')` 中的 'P' 会被自动提升为 int，调用 `StringBuffer(int capacity)`。
- 所以 word 的内容是空的。
- 后续 append 得到 "ain"。
- 所以 A (Pain/Gain), B (Gain), C (Pain) 都是错的。
- 正确答案是 D。

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
参考解答：
- `int p;` 声明了局部变量 p，但未初始化。
- `j = p;` 尝试使用未初始化的局部变量 p，这在 Java 中是编译错误（Variable 'p' might not have been initialized）。
- `int j = 10;` 是合法的。
- 总共只有这一处编译错误。
- 因此选 A。

知识点：[成员变量与局部变量的作用范围、默认值及final终止变量](../../../topics/Java开发/变量的作用域与初始化.md)、[Java平台、JVM定义及编译解释执行原理](../../../topics/Java开发/Java平台与JVM.md)
