---
title: 《数学实验B》实验内容：函数图形与空间曲线作图
kind: 实验
course: 数学实验B
source: batch-2:数学实验/数学实验(1).zip/IMG_20170517_105328.jpg
---

# 《数学实验B》实验内容：函数图形与空间曲线作图

原件经识别和整理；“参考解答”是我们补的。

## 1.7 函数图形作图

作出如下函数的图形（注：先用 M 文件定义函数保存起来，再用 fplot 进行函数作图）：

$$
f(x)=\begin{cases}
2x, & 0\le x\le \dfrac{1}{2};\\[6pt]
2(1-x), & \dfrac{1}{2}<x\le 1.
\end{cases}
$$

M 文件为：

```matlab
function y = f(x)
if x >= 0 & x <= 1/2
    y = 2 * x;
elseif 1/2 < x & x <= 1
    y = 2 * (1 - x);
end
```

画图命令为：

```matlab
fplot(@f, [0, 1])
```

## 1.8 空间曲线作图

作出下面两条空间曲线的图像。

第一条曲线：

$$
\begin{cases}
x=\dfrac{m}{20}\cos t\\[6pt]
y=\dfrac{m}{20}\sin t\\[6pt]
z=t
\end{cases}
$$

第二条曲线：

$$
\begin{cases}
x=\cos t+t\sin t\\
y=\sin t-t\cos t\\
z=-t
\end{cases}
\qquad \left(-\dfrac{m}{10}\le t\le \dfrac{m}{10}\right)
$$

代码为：

```matlab
ezplot3('331/20.*cos(t)', '331/20.*sin(t)', 't', [-331/10, 331/10])
ezplot3('cos(t)+t.*sin(t)', 'sin(t)-t.*cos(t)', '-t', [-331/10, 331/10])
