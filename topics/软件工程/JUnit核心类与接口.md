---
title: JUnit框架核心类及接口（TestCase、Assert、TestSuite、TestResult）
requires: [软件工程/单元测试]
---

# JUnit框架核心类及接口（TestCase、Assert、TestSuite、TestResult）

## JUnit 框架的核心类与接口

JUnit 是 Java 单元测试的事实标准。它提供了一套预定义的类与接口，让你能快速编写可自动运行的测试。理解这些核心组件，是读得懂测试报告、写得出现实工程里不会写出 Bug 的测试的前提。

### 为什么需要这些类

不靠框架，想在 `main()` 里测试一个方法，你得手写大量的 `if` 判断、`System.out.println` 以及异常捕获。一旦测试变多，不同人的打印风格不一，定位失败点就非常耗时。

JUnit 把这件事拆分成了四个职责明确的角色：

```mermaid
flowchart LR
    User["开发者编写代码"] --> TC["TestCase（测试用例）"]
    TC --> A["Assert（断言判断）"]
    TC --> TS["TestSuite（测试套件）"]
    TS --> TR["TestResult（运行结果）"]
    A --> TR
```

- **TestCase**：描述“拿一组输入，期望怎样的输出/行为”。
- **Assert**：做真正的对错判断。
- **TestSuite**：把分散的测试用例打包批量执行。
- **TestResult**：收集执行过程中的成功、失败与错误。

> [!IMPORTANT]
> 测试方法本身**不允许有业务返回值**。判定对错的唯一途径是调用 `Assert` 的静态方法。JUnit 通过 `TestResult` 对象收集断言成功或失败后的状态，失败不等于程序崩溃。

### TestCase —— 一个测试就是一个方法

一个标准的 `TestCase` 类继承 `junit.framework.TestCase`，每个测试方法命名通常以 `test` 开头以被框架自动发现。在每个测试方法运行前，`setUp()` 会被调用；运行结束后，`tearDown()` 会被调用。

```java
public class CalculatorTest extends TestCase {
    private Calculator calc;
    
    public void setUp() { calc = new Calculator(); }
    public void tearDown() { calc = null; }
    
    public void testAdd() {
        assertEquals(5, calc.add(2, 3));
    }
}
```

`setUp()` / `tearDown()` 保证了每个测试都从干净的状态开始，彼此不干扰。

> [!TIP]
> 如果多个测试方法都需要同一个初始对象，把它初始化放在 `setUp()` 里，而不要放在测试方法内部重复 new。这会让测试意图更清晰、资源更容易统一管理。

### Assert —— 你不能避开的一行

JUnit 的 `Assert` 类提供了一组静态方法，==核心只有一句逻辑：若预期值与实际值不符，抛出 `AssertionFailedError`==。常见方法有：

| 方法 | 含义 |
|---|---|
| `assertEquals(expected, actual)` | 预期与实际是否相等 |
| `assertTrue(condition)` | 条件是否为真 |
| `assertFalse(condition)` | 条件是否为假 |
| `assertNull(object)` | 对象是否为空 |
| `assertNotNull(object)` | 对象是否非空 |
| `assertSame(expected, actual)` | 是否为同一引用 |

> [!WARNING]
> `assertEquals` 对基本类型比较**值**，对引用类型使用 `equals()` 方法。如果你要判断是否为同一个对象（引用地址），必须使用 `assertSame`。很多新手在比较两个不同 `new` 出来的内容相同对象时用 `assertSame` 而导致报错，却误以为是业务逻辑错了。

### TestSuite —— 把测试打包运行

`TestSuite` 本身也实现了 `Test` 接口，它是一组测试用例（也可以是其他套件）的容器。你可以用 `addTestSuite()` 添加一个编译时已知的类，或在 `suite()` 静态方法里组装。

```java
public static Test suite() {
    TestSuite suite = new TestSuite();
    suite.addTestSuite(CalculatorTest.class);
    suite.addTestSuite(UserServiceTest.class);
    return suite;
}
```

`TestSuite` 解决了“怎么一键运行全部测试”的问题。你可以在它里面只放入本次修改涉及的那几个用例类，快速验证局部改动。

### TestResult —— 通过结果看测试全貌

测试执行完毕后，JUnit 会生成一个 `TestResult` 对象，它记录了运行了哪些测试、失败了多少、出错过多少。你不必手动构建它；当你调用 `TestSuite.run(TestResult result)` 时，框架会把所有执行反馈汇总进去。

`TestResult` 中，“失败”与“错误”有本质区别：

- **失败（Failure）**：断言不成立，即你期望的值与实际不同，是逻辑不符合预期。
- **错误（Error）**：测试方法抛出了你未捕获的异常（比如空指针、数组越界等），说明测试本身很可能有瑕疵。

> [!CAUTION]
> 看到红色条就认为代码写错了？先检查是 Failure 还是 Error。Error 通常意味着测试代码自己先崩了，被测试的方法甚至可能没执行到。

### 一个算对了的例子

假设有一个方法 `divide(int a, int b)`，需求是：当分母为 0 时返回 0 而不是抛异常。测试用例如下（JUnit 3 风格）：

```java
public void testDivideByZero() {
    int result = calc.divide(10, 0);
    assertEquals(0, result);   // 期望 0，实际 result 也是 0 → 通过
}
```

执行过程：
1. `TestCase` 实例创建 → `setUp()` 创建 `calc` 对象。
2. 调用 `testDivideByZero()`。
3. `assertEquals(0, 0)` 结果为真，不抛出 `AssertionFailedError`。
4. `TestResult` 记录该方法通过，`runCount` 加 1，`failureCount` 不变。
5. `tearDown()` 回收 `calc` 引用。

整个过程无异常，测试条变绿。

### 与类似概念的辨析

- **TestCase vs TestSuite**：用例是“一个具体的验证点”，套件是“一组测试用例的集合”。你可以把用例直接放进运行器，也可以先织成套件再运行，两者都实现了 `Test` 接口。
- **fail() vs assertFalse**：`fail()` 无条件立即让测试失败，通常用在“本不该执行到这里”的防御性位置，比如异常捕获的 `catch` 块最后必须调用 `fail()` 来保证未预期的异常也会导致测试失败。
- **传统 println 调试 vs JUnit Assert**：前者靠人眼逐行比较输出；后者由机器自动判定绿/红条。==测试的真正价值在于“可重复的自动判断”，而不是临时看一眼输出==。
