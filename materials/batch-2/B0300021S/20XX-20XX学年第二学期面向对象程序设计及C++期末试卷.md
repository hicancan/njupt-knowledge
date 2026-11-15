---
title: 20XX/20XX学年第二学期《面向对象程序设计及C++》期末试卷
kind: 期末试卷
course: 面向对象程序设计及C++
source: batch-2:C++/c++往年样卷(1).pdf
---

# 20XX/20XX学年第二学期《面向对象程序设计及C++》期末试卷

原件经识别和整理；“参考解答”是我们补的。

# 20XX/20XX学年第二学期《面向对象程序设计及C++》期末试卷

## 一、单选题（共 20分，每题 2分）

### 选择 1

系统约定 C++源程序文件名的缺省的扩展名为（ ）

- A. bcc
- B. c++
- C. cpp
- D. vcc

答案：C。

知识点：[C++程序的开发过程与VC++6集成开发环境](../../../topics/面向对象C++/cpp开发过程.md)

### 选择 2

对于下面几个函数：

(1) `void f(int x, float y) {… … }`

(2) `int f(int a, float b){… … }`

(3) `int f(int i, int j){… … }`

(4) `float k(int x){… … }`

是重载函数。

- A. 4 个全部
- B. 1 和 2
- C. 2 和 3
- D. 3 和 4

答案：B。

知识点：[函数重载](../../../topics/面向对象C++/函数重载.md)

### 选择 3

下列关于构造函数的描述中，（ ）是正确的。

- A. 构造函数可以设置缺省参数；
- B. 构造函数可以被继承；
- C. 构造函数可以对静态数据成员进行初始化；
- D. 构造函数可以说明为虚函数；

答案：A。

知识点：[构造函数（含默认构造函数、带默认参数值的构造函数）](../../../topics/面向对象C++/构造函数.md)、[形式参数可带有默认值](../../../topics/面向对象C++/默认参数.md)

### 选择 4

有关类和对象的说法下列不正确的是( )。

- A. 对象是类的一个实例
- B. 任何一个对象只能属于一个具体的类
- C. 一个类只能有一个对象
- D. 类与对象的关系和数据类型和变量的关系相似

答案：C。

知识点：[类与对象的基本概念](../../../topics/面向对象C++/类与对象概念.md)、[继承性](../../../topics/面向对象C++/继承性.md)

### 选择 5

有以下类的说明，请指出错误的地方（）。

```cpp
Class CSample{
    int a=2.5;
    A CSample();
    B public:CSample(int val);
    C ~CSample();
    D };
```

- A. `int a=2.5;`
- B. `CSample();`
- C. `public:CSample(int val);`
- D. `~CSample();`

*(注：原题选项对应代码行，通常考察旧标准下类内初始化或构造函数声明语法，此处按常见考点推断)*

答案：A。

知识点：[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)、[构造函数（含默认构造函数、带默认参数值的构造函数）](../../../topics/面向对象C++/构造函数.md)

### 选择 6

设类 B 是基类 A 的派生类，并有语句：`A aa, * pa=&aa; B bb, * pb=&bb;` 则正确的语句是\_\_\_(6)\_\_ 。

- A. `pb=pa;`
- B. `bb=aa;`
- C. `aa=bb;`
- D. `*pb=*pa;`

答案：C。

知识点：[赋值兼容规则（派生类对象赋给基类对象/指针/引用）](../../../topics/面向对象C++/赋值兼容规则.md)、[基类与派生类、单一继承与多重继承](../../../topics/面向对象C++/继承与派生概念.md)

### 选择 7

若类X 和类Y 的定义如下：

```cpp
class X {
    int a,b;
    public: void fx ( );
}；
class Y: public X {
    int c;
    public: void fy ( );
};
void Y::fy ( ) { c=a*b; }
```

则上述代码中， (8) 是非法的语句。 *(注：题干编号可能有误，结合选项看应为问哪部分非法)*

- A. `void fx();`
- B. `k=a*b;` *(注：原题此处可能为 `c=a*b` 或其他，根据上下文 `a,b` 为私有成员，在派生类成员函数中直接访问基类私有成员是非法的，但题目问的是“非法语句”，需看具体选项指向。若选项B指代赋值语句 `c=a*b`，因a,b为private且未在Y中声明，故非法)*
- C. `void fy();`
- D. `int c;`

答案：B。

知识点：[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)、[公有继承、保护继承与私有继承及访问权限总结](../../../topics/面向对象C++/继承方式.md)、[派生类对象的构造与析构及基类构造函数的参数传递](../../../topics/面向对象C++/派生类构造与析构.md)

### 选择 8

系统在调用重载函数时，往往根据一些条件确定哪个重载函数被调用，在下列选项中，不能作为依据的是

- A. 参数的个数
- B. 参数的类型
- C. 参数的顺序
- D. 函数的类型

答案：D。

知识点：[函数重载](../../../topics/面向对象C++/函数重载.md)

### 选择 9

已知:p 是一个指向类A 数据成员m的指针,A1是类A的一个对象。如果要给 m赋值为5,( )是正确的。

- A. `A1.p=5`
- B. `A1->p=5`
- C. `A1.*p=5`
- D. `*A1.p=5`

答案：C。

知识点：[对象指针与对象引用](../../../topics/面向对象C++/对象指针与引用.md)、[定义对象及圆点访问形式与指针访问形式](../../../topics/面向对象C++/对象的定义与访问.md)、[类与对象的基本概念](../../../topics/面向对象C++/类与对象概念.md)

### 选择 10

已知:类A中一个成员函数说明如下:`void Set(A&a);` 其中,`A&a` 的含义是( )。

- A. 指向类A 的指针为a
- B. 将a的地址值赋给变量 Set
- C. a是类A的对象引用,用来作函数Set()的形参
- D. 变量A与 a按位相与作为函数Set()的参数

答案：C。

## 二、填空题（共 10分，每空 1分）

知识点：[引用的概念及使用（含引用作形参、返回值及与指针区别）](../../../topics/面向对象C++/引用.md)、[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)、[对象作为函数参数（传值、传指针、传引用）](../../../topics/面向对象C++/对象作函数参数.md)

### 填空 1

面向对象的程序设计有四大特征，它们是抽象、 **(1)** 、 **(2)** 、 **(3)** 。

答案：封装、继承、多态。（顺序可互换）

参考解答：**结论**

```cpp
date(int y = 2004, int m = 1, int d = 1);
date(const date& other);
```

**推理过程**

1.  **带默认参数的构造函数**：题目要求默认值为 2004 年 1 月 1 日，因此三个形参 `y`、`m`、`d` 的默认值分别设为 `2004`、`1`、`1`；C++ 规定默认参数必须从右向左连续提供，此处三个参数均给默认值，满足无参调用 `date()` 时自动使用 2004-1-1。
2.  **复制构造函数**：C++ 中复制构造函数的固定签名为接受一个同类型 `const` 引用参数，即 `const date&`，用于以已有对象初始化新对象；若省略 `const` 则无法绑定临时对象或右值，不符合标准语义。

知识点：[构造函数（含默认构造函数、带默认参数值的构造函数）](../../../topics/面向对象C++/构造函数.md)、[拷贝构造函数及其自动调用的3种情况](../../../topics/面向对象C++/拷贝构造函数.md)、[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)

### 填空 2

在函数说明前加关键字“inline”，则该函数被声明为 **(4)** 函数，其引入的目的是为了消除函数调用时的开销，以提高运行速度。

答案：内联

参考解答：## 填空 2

**结论**：`std::vector<T> add(const std::vector<T>& a, const std::vector<T>& b)`

```cpp
template<typename T>
std::vector<T> add(const std::vector<T>& a, const std::vector<T>& b) {
    std::vector<T> result(a.size());
    for (size_t i = 0; i < a.size(); ++i)
        result[i] = a[i] + b[i];
    return result;
}
```

**简析**：函数模板需接受两个同类型 `vector` 的常引用参数（避免拷贝且不修改原向量），返回值为新 `vector`。参数表和返回值类型均需补全，循环逐元素相加即可。


## 五、编程题 1

**结论**：

```cpp
#include <iostream>
#include <vector>
using namespace std;

template<typename T>
vector<T> add(const vector<T>& a, const vector<T>& b) {
    vector<T> result(a.size());
    for (size_t i = 0; i < a.size(); ++i)
        result[i] = a[i] + b[i];
    return result;
}

int main() {
    vector<double> v1 = {1.5, 2.5, 3.5};
    vector<double> v2 = {0.5, 0.5, 1.0};
    vector<double> v3 = add(v1, v2);
    for (auto x : v3) cout << x << " ";
    // 输出：2 3 4.5
    return 0;
}
```

**关键步骤**：
- 模板参数 `T` 需支持 `operator+`
- 结果向量的长度取参数中任一向量长度（默认二者等长）
- 用 `const` 引用传参，避免多余拷贝
- 返回的 `vector<T>` 按值返回，利用移动语义或返回值优化（NRVO）避免额外开销

知识点：[函数模板的定义与模板函数的使用](../../../topics/面向对象C++/函数模板.md)、[泛型程序设计与C++ STL简介：顺序容器vector的操作（插入、删除、capacity、size、at、front、back、赋值）](../../../topics/面向对象C++/stl容器vector.md)

### 填空 3

**(5)** 是一种特殊的成员函数，它主要用来为对象分配内存空间，对类的数据成员进行初始化并执行对象的其他内部管理操作。

答案：构造函数

知识点：[构造函数（含默认构造函数、带默认参数值的构造函数）](../../../topics/面向对象C++/构造函数.md)

### 填空 4

任何类中允许有三种访问权限的数据，这三种访问权限分别是 **(6)** 、 **(7)** 和 **(8)** 。

答案：公有(public)、保护(protected)、私有(private)。（顺序可互换）

知识点：[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)

### 填空 5

静态数据成员属于类，可以使用 **(9)** 访问静态的数据成员。

答案：类名::静态成员名 （或通过对象访问，但通常强调作用域解析运算符）

知识点：[静态数据成员的定义与初始化](../../../topics/面向对象C++/静态数据成员.md)、[域解析符::扩大全局变量的可见范围](../../../topics/面向对象C++/域解析符.md)

### 填空 6

构造函数不能被继承，因此，派生类的构造函数必须通过调用 **(10)** 构造函数进行初始化基类的对象。

答案：基类

## 三、程序阅读题（共 30 分，每题 6分）

知识点：[基类与派生类、单一继承与多重继承](../../../topics/面向对象C++/继承与派生概念.md)、[派生类对象的构造与析构及基类构造函数的参数传递](../../../topics/面向对象C++/派生类构造与析构.md)、[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)

### 阅读 1

以下程序的输出结果是

```cpp
#include <iostream.h>
// [图片缺失，无法还原完整代码]
```

*(注：原件此处仅有标题，无具体代码内容，无法作答)*

参考解答：很抱歉，根据你提供的内容，题目中的程序代码缺失，仅有一行 `#include <iostream.h>` 且注明“图片缺失，无法还原完整代码”，因此无法判断程序的逻辑结构、类定义、继承关系、虚函数使用情况等关键信息，也就无法确定输出结果。

如果能把完整的代码部分补上，我可以立刻给出结论、推理过程以及本题选项分析。

知识点：[C++用I/O流（cin/cout）实现输入/输出](../../../topics/面向对象C++/io流输入输出.md)

### 阅读 2

以下程序的执行结果是

*(注：原件此处仅有标题，无具体代码内容，无法作答)*

参考解答：**结论：** 无法作答。

**说明：** 题目未提供具体的 C++ 程序代码，缺少求解所必需的信息，因此无法给出执行结果。请补充完整代码后重新提问。

知识点：[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)、[定义对象及圆点访问形式与指针访问形式](../../../topics/面向对象C++/对象的定义与访问.md)、[C++用I/O流（cin/cout）实现输入/输出](../../../topics/面向对象C++/io流输入输出.md)

### 阅读 3

以下程序的执行结果是

*(注：原件此处仅有标题，无具体代码内容，无法作答)*

## 四、程序填空题（共16 分，每题 8分）

参考解答：**结论：无法作答。**

原题仅给出“阅读 3”的标题，缺少具体代码，无法判断程序执行结果。请补充完整代码后再进行分析。

知识点：[C++语言与C语言的关系](../../../topics/面向对象C++/cpp与c关系.md)、[C++用I/O流（cin/cout）实现输入/输出](../../../topics/面向对象C++/io流输入输出.md)、[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)

### 填空 1

定义类 date 的带默认值（为 2004 年 1 月 1日）的函数与复制构造函数。

*(注：原件此处仅有题干描述，未给出待填空的代码框架)*

参考解答：**结论**

```cpp
date(int y = 2004, int m = 1, int d = 1);
date(const date& other);
```

**推理过程**

1.  **带默认参数的构造函数**：题目要求默认值为 2004 年 1 月 1 日，因此三个形参 `y`、`m`、`d` 的默认值分别设为 `2004`、`1`、`1`；C++ 规定默认参数必须从右向左连续提供，此处三个参数均给默认值，满足无参调用 `date()` 时自动使用 2004-1-1。
2.  **复制构造函数**：C++ 中复制构造函数的固定签名为接受一个同类型 `const` 引用参数，即 `const date&`，用于以已有对象初始化新对象；若省略 `const` 则无法绑定临时对象或右值，不符合标准语义。

知识点：[构造函数（含默认构造函数、带默认参数值的构造函数）](../../../topics/面向对象C++/构造函数.md)、[拷贝构造函数及其自动调用的3种情况](../../../topics/面向对象C++/拷贝构造函数.md)、[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)

### 填空 2

下面是一个函数模板，用于计算两个向量的和。在下面横线处填上适当字句，完成函数模板定义。

*(注：原件此处仅有题干描述，未给出待填空的代码框架)*

## 五、编程题 1（12 分）

参考解答：## 填空 2

**结论**：`std::vector<T> add(const std::vector<T>& a, const std::vector<T>& b)`

```cpp
template<typename T>
std::vector<T> add(const std::vector<T>& a, const std::vector<T>& b) {
    std::vector<T> result(a.size());
    for (size_t i = 0; i < a.size(); ++i)
        result[i] = a[i] + b[i];
    return result;
}
```

**简析**：函数模板需接受两个同类型 `vector` 的常引用参数（避免拷贝且不修改原向量），返回值为新 `vector`。参数表和返回值类型均需补全，循环逐元素相加即可。


## 五、编程题 1

**结论**：

```cpp
#include <iostream>
#include <vector>
using namespace std;

template<typename T>
vector<T> add(const vector<T>& a, const vector<T>& b) {
    vector<T> result(a.size());
    for (size_t i = 0; i < a.size(); ++i)
        result[i] = a[i] + b[i];
    return result;
}

int main() {
    vector<double> v1 = {1.5, 2.5, 3.5};
    vector<double> v2 = {0.5, 0.5, 1.0};
    vector<double> v3 = add(v1, v2);
    for (auto x : v3) cout << x << " ";
    // 输出：2 3 4.5
    return 0;
}
```

**关键步骤**：
- 模板参数 `T` 需支持 `operator+`
- 结果向量的长度取参数中任一向量长度（默认二者等长）
- 用 `const` 引用传参，避免多余拷贝
- 返回的 `vector<T>` 按值返回，利用移动语义或返回值优化（NRVO）避免额外开销

知识点：[函数模板的定义与模板函数的使用](../../../topics/面向对象C++/函数模板.md)、[泛型程序设计与C++ STL简介：顺序容器vector的操作（插入、删除、capacity、size、at、front、back、赋值）](../../../topics/面向对象C++/stl容器vector.md)

### 编程 1

定义一个圆类（Circle），属性为半径（radius）、圆周长和面积，操作为输入半径并计算周长、面积，输出半径、周长和面积。要求定义构造函数（以半径为参数，缺省值为 0，周长和面积在构造函数中生成）和拷贝构造函数。

*(注：此为开放性编程题，无固定答案格式，需编写完整类定义)*

## 六、编程题 2（12 分）

参考解答：### 结论

```cpp
#include <iostream>
#include <cmath>
using namespace std;

class Circle {
private:
    double radius;
    double circumference;
    double area;

    void calculate() {
        circumference = 2 * M_PI * radius;
        area = M_PI * radius * radius;
    }

public:
    // 构造函数，半径缺省值为0，周长和面积在构造函数中生成
    Circle(double r = 0) : radius(r) {
        calculate();
    }

    // 拷贝构造函数
    Circle(const Circle& other) 
        : radius(other.radius), 
          circumference(other.circumference), 
          area(other.area) {}

    // 输入半径并重新计算周长、面积
    void inputRadius() {
        cout << "请输入半径: ";
        cin >> radius;
        calculate();
    }

    // 输出半径、周长和面积
    void display() const {
        cout << "半径: " << radius << endl;
        cout << "周长: " << circumference << endl;
        cout << "面积: " << area << endl;
    }
};
```

### 推理与关键设计说明

1. **属性存储**：`circumference` 和 `area` 作为成员变量而非实时计算，满足题目“在构造函数中生成”的要求，避免每次访问都重复运算。
2. **构造函数**：使用默认参数 `double r = 0` 实现缺省值；通过初始化列表设置 `radius` 后调用私有方法 `calculate()` 统一计算周长 $C=2\pi r$ 和面积 $S=\pi r^2$，保证构造时三个属性一致。
3. **拷贝构造函数**：显式定义以逐成员复制三个属性，确保深拷贝语义正确（虽然本类无指针成员，编译器生成的默认拷贝构造也可用，但题目明确要求定义）。
4. **输入操作**：`inputRadius()` 在读入新半径后立即调用 `calculate()` 更新周长和面积，维持数据一致性。
5. **封装性**：`calculate()` 设为 `private`，防止外部绕过输入接口直接修改派生量；`display()` 标记 `const` 保证只读安全。
6. **常量使用**：采用 `M_PI`（`<cmath>` 提供）而非硬编码 3.14，提高精度与可移植性；若编译环境不支持 `M_PI`，可自行定义 `const double PI = acos(-1.0);`。

知识点：[类的定义（成员数据、成员函数、访问属性public/private/protected）](../../../topics/面向对象C++/类的定义.md)、[构造函数（含默认构造函数、带默认参数值的构造函数）](../../../topics/面向对象C++/构造函数.md)、[拷贝构造函数及其自动调用的3种情况](../../../topics/面向对象C++/拷贝构造函数.md)

### 编程 2

在下面基类 Areaclass 的基础上建立两个派生类 Box (方形类)与Isosceles(等腰三角形类)，每个派生类包含一个函数 Area()，分别用于返回方形和等腰三角形的面积，并声明对象，进行检验。

```cpp
class Areaclass
{ 
public: 
    Areaclass (double x=0, double y=0):height(x), width(y){ } 
protected: 
    double height, width;
};
```

*(注：需基于上述基类编写派生类及主函数测试代码)*

参考解答：## 结论

可通过继承 `Areaclass` 建立两个派生类：

- `Box`：返回方形面积 $S=height\times width$。
- `Isosceles`：返回等腰三角形面积 $S=\dfrac{height\times width}{2}$，其中 `height` 表示底边长，`width` 表示腰长。

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

class Areaclass
{
public:
    Areaclass(double x = 0, double y = 0)
        : height(x), width(y) {}

protected:
    double height, width;
};

// 方形类
class Box : public Areaclass
{
public:
    Box(double side = 0, double otherSide = 0)
        : Areaclass(side, otherSide) {}

    double Area() const
    {
        return height * width;
    }
};

// 等腰三角形类
class Isosceles : public Areaclass
{
public:
    Isosceles(double base = 0, double waist = 0)
        : Areaclass(base, waist) {}

    double Area() const
    {
        return height * width / 2.0;
    }
};

int main()
{
    Box square(4, 4);
    Isosceles triangle(6, 5);

    cout << fixed << setprecision(2);
    cout << "方形面积：" << square.Area() << endl;
    cout << "等腰三角形面积：" << triangle.Area() << endl;

    // 检验计算结果
    if (square.Area() == 16.0)
        cout << "方形面积计算正确" << endl;
    else
        cout << "方形面积计算错误" << endl;

    if (triangle.Area() == 15.0)
        cout << "等腰三角形面积计算正确" << endl;
    else
        cout << "等腰三角形面积计算错误" << endl;

    return 0;
}
```

## 计算过程

### 1. 方形面积

边长为 $4$：


$$
S_{\text{方形}}=4\times 4=16
$$


### 2. 等腰三角形面积

底边长为 $6$，腰长为 $5$。由于腰长即为三角形的高：


$$
S_{\text{三角形}}=\frac{1}{2}\times 6\times 5=15
$$


程序输出：

```text
方形面积：16.00
等腰三角形面积：15.00
方形面积计算正确
等腰三角形面积计算正确
```

知识点：[虚函数的定义以实现动态多态性及虚函数的限制](../../../topics/面向对象C++/虚函数.md)、[基类与派生类、单一继承与多重继承](../../../topics/面向对象C++/继承与派生概念.md)
