---
title: 《Java软件开发》第3次作业：多源文件与成员访问
kind: 实验
course: Java软件开发
term: 2020-2021-2
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0302281C%E3%80%91JAVA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1/Course%20Materials%20%5B2020-2021-2%5D/01%20Lectures%20Assignment/JAVA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E7%AC%AC3%E6%AC%A1%E4%BD%9C%E4%B8%9A.pdf
---

# 《Java软件开发》第3次作业：多源文件与成员访问

2021 年 3 月的原件只有一项分两次编译的练习：先让三个类各在一个文件中正常工作，再把外部直接读写四个字段的语句换成方法调用，重新编译并比较输出。第 2 页是历史提交说明，不另列为实验。下面的示例是自编参考解答，不是课件原代码。

## 第一遍：先确认三个文件能一起运行

**参考解答**：在同一目录建 `Point.java`、`Rectangle.java`、`CreateObjectDemo.java`。第一遍把前两个类分别写成下面这样，每段保存到同名文件：

```java
public class Point {
    int x;
    int y;
}
```

```java
public class Rectangle {
    int width;
    int height;
}
```

程序的入口只有一个，放在 `CreateObjectDemo.java`。先用直接字段访问，运行出一个可对照的结果：

```java
public class CreateObjectDemo {
    public static void main(String[] args) {
        Point p = new Point();
        Rectangle r = new Rectangle();
        p.x = 3;
        p.y = 4;
        r.width = 6;
        r.height = 8;
        System.out.printf("(%d,%d) %dx%d%n", p.x, p.y, r.width, r.height);
    }
}
```

有 JDK 时可以在该目录用 `javac CreateObjectDemo.java Point.java Rectangle.java` 编译，再用 `java CreateObjectDemo` 启动。IDE 项目同样只需选择 `CreateObjectDemo` 作为入口。此例的三类都在同一个包，这就是第一遍能访问未标访问修饰符字段的前提。对应[入口类与源文件](../../../topics/Java开发/HelloWorld程序结构.md)和[对象与类](../../../topics/Java开发/对象与类的概念.md)。

## 第二遍：两处写法都换，输出保持一致

把两个数据类的字段改成 `private`，并加上成对的公开方法。`this.x` 是当前对象的字段，右边的 `x` 是本次传入的参数；写成 `x = x` 只会让参数赋值给自己。

```java
public class Point {
    private int x;
    private int y;

    public int getX() { return x; }
    public int getY() { return y; }

    public void setX(int x) { this.x = x; }
    public void setY(int y) { this.y = y; }
}
```

```java
public class Rectangle {
    private int width;
    private int height;

    public int getWidth() { return width; }
    public int getHeight() { return height; }

    public void setWidth(int width) { this.width = width; }
    public void setHeight(int height) { this.height = height; }
}
```

再把入口中四处==写入==和四处==读取==都改掉。只改赋值而漏了输出，读私有字段仍然编译不通过。

```java
public class CreateObjectDemo {
    public static void main(String[] args) {
        Point p = new Point();
        Rectangle r = new Rectangle();
        p.setX(3);
        p.setY(4);
        r.setWidth(6);
        r.setHeight(8);
        System.out.printf("(%d,%d) %dx%d%n",
                p.getX(), p.getY(), r.getWidth(), r.getHeight());
    }
}
```

重新编译三个源文件，两版均输出 `(3,4) 6x8`。输出不变只是回归检查之一：单独修改一个属性，其他三个应保持原值；外部尝试直接读写私有字段应在编译时失败。参见[方法的定义](../../../topics/Java开发/方法的定义与重载.md)和[变量的作用域](../../../topics/Java开发/变量的作用域与初始化.md)。

> [!TIP]
> 找漏改处时，按对象分开检查：定位 `p.x`、`p.y`、`r.width`、`r.height`。等号左边是写入，换成 `set…(值)`；用在表达式中的是读取，换成 `get…()`。

> [!WARNING]
> 本题是更改访问接口，仍保留原来的读写行为。公开 setter 不会自动限制取值；若以后要拒绝负尺寸，应明确这是一条新增约束，再单独验证拒绝时对象状态不变。
