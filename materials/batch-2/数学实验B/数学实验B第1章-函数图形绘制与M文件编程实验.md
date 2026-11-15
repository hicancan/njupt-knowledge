---
title: 《数学实验B》第1章 函数图形绘制与M文件编程（实验）
kind: 实验
course: 数学实验B
source: batch-2:数学实验/数学实验(1).zip/IMG_20170517_105332.jpg
---

# 《数学实验B》第1章 函数图形绘制与M文件编程（实验）

原件经识别和整理；“参考解答”是我们补的。

## 1.9

已知 $f(x) = \begin{cases} \frac{1}{\lambda} e^{-\lambda x}, & x > 0; \\ 0, & x \leq 0. \end{cases}$ 画出 $f(x)$ 的图形，其中 $\lambda$ 分别为 $1000/m, 500/m, 400/m, 100/m$。（在同一坐标系中用不同颜色作图）。

**M文件 f1:**
```matlab
function y = f(x)
t = 1000/331;
if x > 0
    y = 1/t * exp(-t*x);
else % x <= 0
    y = 0;
end
```

**M文件 f2:**
```matlab
function y = f(x)
t = 500/331;
if x > 0
    y = 1/t * exp(-t*x);
else % x <= 0
    y = 0;
end
```

**M文件 f3:**
```matlab
function y = f(x)
t = 400/331;
if x > 0
    y = 1/t * exp(-t*x);
else % x <= 0
    y = 0;
end
```

**M文件 f4:**
```matlab
function y = f(x)
t = 100/331;
if x > 0
    y = 1/t * exp(-t*x);
else % x <= 0
    y = 0;
end
```

**绘图脚本:**
```matlab
fplot(@f1, [-5, 20], 'r')
hold on
fplot(@f2, [-5, 20], 'b')
fplot(@f3, [-5, 20], 'c')
fplot(@f4, [-5, 20], 'g')
legend('lambda=1000', 'lambda=500', 'lambda=400', 'lambda=100')
grid on
