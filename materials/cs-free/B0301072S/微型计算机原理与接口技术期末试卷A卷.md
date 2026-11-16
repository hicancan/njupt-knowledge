---
title: 《微型计算机原理与接口技术》期末试卷（A卷）
kind: 期末试卷
course: 微型计算机接口技术
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301072S%E3%80%91%E5%BE%AE%E5%9E%8B%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%8E%A5%E5%8F%A3%E6%8A%80%E6%9C%AF/%E8%AF%95%E5%8D%B7/%E5%BE%AE%E6%9C%BA%E5%8E%9F%E7%90%86%E4%B8%8E%E6%8E%A5%E5%8F%A3%E6%A0%B7%E5%8D%B71.docx
---

# 《微型计算机原理与接口技术》期末试卷（A卷）

原件经识别和整理；“参考解答”是我们补的。

## 一、选择题（每小题 2 分，共 20 分）

### 选择 1

在所有的输入/输出接口电路中，都必须包括（ ）端口。

- A. 控制
- B. 状态
- C. 数据
- D. 地址

参考解答：**结论：选 C（数据端口）**

**理由：** 输入/输出接口的核心功能是完成 CPU 与外设之间的**数据交换**，因此任何 I/O 接口都必须包含用于暂存和传输数据的数据端口（数据缓冲器）。

**其他选项简析：**
- **A. 控制端口**：仅用于可编程接口芯片，简单接口（如三态缓冲器）无需控制端口。
- **B. 状态端口**：仅当需要查询外设状态时才配置，非必需。
- **D. 地址端口**：I/O 接口通常通过地址译码电路选择，而非独立的地址端口。

知识点：[接口电路的作用和基本功能](../../../topics/微机接口/jiekou-gongneng.md)、[端口的概念与分类（数据端口、状态端口、控制端口）](../../../topics/微机接口/duankou-gainian.md)

### 选择 2

8254的每个计数器都有( )工作方式。

- A. 3 种
- B. 4 种
- C. 5 种
- D. 6 种

参考解答：**D. 6 种**

8254 的每个计数器（通道）都可独立编程，支持 6 种工作方式：

| 方式 | 名称 |
|------|------|
| 0 | 计数结束中断 |
| 1 | 可编程单稳态 |
| 2 | 频率发生器（分频器） |
| 3 | 方波发生器 |
| 4 | 软件触发选通 |
| 5 | 硬件触发选通 |

- A 错：3 种是明显偏少的干扰项。
- B 错：4 种缺少两种方式，不完整。
- C 错：5 种最接近但少一种（常见干扰项）。

知识点：[接口电路的作用和基本功能](../../../topics/微机接口/jiekou-gongneng.md)、[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 选择 3

以下方式中CPU不参与数据传送的是（ ）方式。

- A. 查询
- B. 无条件传送
- C. 中断控制
- D. DMA

参考解答：## 结论

**选 D（DMA）**

## 推理

DMA（直接存储器访问）方式由 **DMA 控制器** 接管系统总线，直接在外设与内存之间传送数据，整个数据传送过程 **CPU 不参与**，仅在传送开始前初始化参数、传送结束后处理中断。

其他选项中 CPU 均参与数据传送：

- **A. 查询**：CPU 不断读取外设状态端口，判断就绪后才执行数据传送指令，全程参与。
- **B. 无条件传送**：CPU 直接执行 I/O 指令完成数据读写，当然参与。
- **C. 中断控制**：数据传送本身仍由 CPU 执行中断服务程序中的 I/O 指令完成，CPU 参与。

知识点：[直接存储器存取（DMA）方式及其与中断方式的比较](../../../topics/微机接口/dma-fangshi.md)、[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 选择 4

地址总线的宽度决定了系统内存的最大容量。20 根地址线，能寻址的存储空间是（ ）。

- A. 640KB
- B. 1MB
- C. 4GB
- D. 64KB

参考解答：**结论：选 B. 1MB**

**推理过程：**

$n$ 根地址线可寻址的存储单元数为 $2^n$ 个（每个单元通常为 1 字节）。

$$2^{20} = 1048576 \text{ Byte} = 1024 \text{ KB} = 1 \text{ MB}$$

**选项分析：**

- **B 正确**：$2^{20} = 1\text{MB}$，计算结果完全吻合。
- **A 错误**：640KB 是早期 IBM PC/XT 中 DOS 分配给常规内存的大小，与物理寻址能力无关。
- **C 错误**：4GB 对应的是 32 根地址线（$2^{32}$），而非 20 根。
- **D 错误**：64KB 对应的是 16 根地址线（$2^{16}$），而非 20 根。

知识点：[存储器容量的表示方法](../../../topics/微机接口/cunchu-rongliang.md)、[实地址模式下物理地址的形成（段基址×10H+偏移量）](../../../topics/微机接口/wuli-dizhi.md)

### 选择 5

-89的八位二进制的补码是（ ）。

- A. B9H
- B. 89H
- C. 10100111B
- D. 00100111B

参考解答：结论：A（B9H）。

-89 的绝对值是 89，八位二进制为 01011001B。  
其反码为 10100110B，补码为反码加 1，即 10100111B。  
10100111B 写成十六进制是 A7H，不是 B9H，所以需要重新核对选项。

实际上 10100111B = A7H，而 -89 的正确补码就是 A7H。  
四个选项中只有 C 是 10100111B，因此应选 **C**，不是 A。

简算：

$$
89_{10}=01011001_2
$$

$$
\text{反码}=10100110_2
$$

$$
\text{补码}=10100110_2+1=10100111_2=A7H
$$

其他选项不对的原因：  
- A：B9H 是 -71 的补码，不是 -89。  
- B：89H 是正数 137 的无符号表示，不是补码意义下的 -89。  
- D：00100111B 是正数 39，符号位为 0，不可能是负数补码。

所以正确选项为 **C**。

知识点：[真值数与补码的相互转换及补码计算](../../../topics/微机接口/zhenzhi-buma.md)、[数制转换（二进制、十进制、十六进制互转）](../../../topics/微机接口/shuzhi-zhuanhuan.md)

### 选择 6

在下列指令的表示中，不正确的是（ ）。

- A. MOV AL, [BX+SI]
- B. JMP DONI
- C. DEC [BX]
- D. MUL CL

参考解答：**结论：选 C。**

---

### 逐项分析

- **A. `MOV AL, [BX+SI]`**  
  合法。`[BX+SI]` 是 8086 合法的基址变址寻址方式，源操作数为字节单元，目的操作数 `AL` 为 8 位寄存器，类型匹配。

- **B. `JMP DONI`**  
  合法。段内直接转移指令，`DONI` 为标号（符号地址），格式正确。

- **C. `DEC [BX]` ——不正确 ✗**  
  `DEC` 对存储器操作数进行减 1 时，汇编器无法从 `[BX]` 判断操作数是**字节**还是**字**。必须用伪指令显式指定长度，例如：
  ```asm
  DEC BYTE PTR [BX]   ; 或 DEC WORD PTR [BX]
  ```
  缺少 `BYTE PTR` / `WORD PTR` 导致操作数大小不明确，因此该指令表示不合法。

- **D. `MUL CL`**  
  合法。无符号乘法 `MUL r/m8`，8 位寄存器 `CL` 作为源操作数，隐含被乘数为 `AL`，结果存入 `AX`，符合指令格式。

知识点：[80486/8086的寻址方式（立即、寄存器、直接、间接、变址等）](../../../topics/微机接口/xunzhi-fangshi.md)、[数据传送指令（MOV、PUSH、POP、XCHG等）](../../../topics/微机接口/shuju-chuansong.md)、[算术运算与逻辑运算指令（ADD、SUB、MUL、AND、OR、NOT等）](../../../topics/微机接口/suanlu-yunsuan.md)

### 选择 7

STI指令允许CPU 响应（ ）中断。

- A. 可屏蔽
- B. 非屏蔽
- C. 软件
- D. 所有类型

参考解答：**答案：A. 可屏蔽**

STI 指令用于将中断允许标志位 IF 置 1，即允许 CPU 响应可屏蔽中断（INTR）。  
- B 错：非屏蔽中断（NMI）不受 IF 标志控制，始终可被响应。  
- C 错：软件中断由指令触发，与 IF 无关。  
- D 错：STI 只影响可屏蔽中断，并非所有类型。

知识点：[标志寄存器中的状态标志位与控制标志位](../../../topics/微机接口/zhuangtai-biaozhi.md)、[处理器控制指令（STI、CLI、HLT、NOP等）](../../../topics/微机接口/chuli-kongzhi.md)

### 选择 8

执行OUT DX, AL 指令后，AL寄存器的数据被送到（ ）。

- A. DX 寄存器
- B. 存储器
- C. DX 所指的内存单元
- D. I/O 端口

参考解答：**D. I/O 端口**

`OUT DX, AL` 是 x86 架构的 I/O 输出指令，其功能是将累加器 `AL` 中的 8 位数据写入由 `DX` 寄存器指定的 **I/O 端口地址**。

-   **A 错误**：`DX` 在此指令中仅作为端口地址指针，并非数据传输的目的操作数。
-   **B、C 错误**：`OUT` 指令专门用于访问独立的 I/O 地址空间，不能直接读写存储器（内存单元）；访问内存需使用 `MOV` 等存储指令。

知识点：[最常用的I/O指令（IN、OUT的直接寻址与DX间址）](../../../topics/微机接口/io-zhiling.md)

### 选择 9

8250芯片具有很强的中断能力，其内部 4级中断具有最高优先权的是( )中断。

- A. 接收缓冲器“满”
- B. 发送保持器“空”
- C. 接收数据错
- D. MODEM 输入状态改变

参考解答：**结论：C**

8250 内部 4 级中断的优先权从高到低为：

1. 接收数据错（最高）
2. 接收缓冲器满
3. 发送保持器空
4. MODEM 输入状态改变（最低）

因此最高优先权的是 **接收数据错**。  
其余选项虽都是 8250 的 4 级中断之一，但优先权均低于接收数据错。

知识点：[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 选择 10

8255A 的 C 口置 0/置 1 控制字应写入（ ）。

- A. A 口
- B. B 口
- C. C 口
- D. 控制端口

## 二、填空题（每空 1 分，共 20 分）

参考解答：**D. 控制端口**

8255A 的 C 口置位/复位控制字虽然操作对象是 C 口的某一位，但该控制字必须写入**控制端口**（即控制寄存器），而非 C 口数据端口。这是因为该控制字的最高位 $D_7=0$ 作为特征位，用于与方式选择控制字（$D_7=1$）区分，CPU 通过向同一控制端口写入不同特征位的字来分别完成模式配置或 C 口按位操作；若写入 A、B 或 C 口数据端口，则会被当作普通 I/O 数据处理，无法触发置位/复位功能。

知识点：[端口的概念与分类（数据端口、状态端口、控制端口）](../../../topics/微机接口/duankou-gainian.md)、[接口电路的作用和基本功能](../../../topics/微机接口/jiekou-gongneng.md)

### 填空 1

指令 `MOV [BX], AL`，源操作数的寻址方式是 **立即寻址**（注：此处原题可能有误，通常MOV目标在前源在后，若为`MOV [BX], AL`则源为寄存器寻址，目标为寄存器间接寻址；若按原题`MOV [BX]，AL`且逗号位置暗示源为目标则逻辑不通，根据常规考题推测题目意图为考察寻址方式名称。*注：原题识别文本为“指令MOV [BX]，AL，源操作数的寻址方式是 ，目标操作数的寻址方式是 C”，其中C可能是笔误或选项残留，标准答案通常为：源操作数AL为**寄存器寻址**，目标操作数[BX]为**寄存器间接寻址**。若严格按原文填空，需结合上下文，此处仅列出题干*）。

*(注：由于原题填空部分无明确答案提供，且存在排版歧义，以下为标准知识点的正确填写供参考)*
源操作数的寻址方式是 **寄存器寻址**，目标操作数的寻址方式是 **寄存器间接寻址**。

参考解答：## 填空 1

源操作数的寻址方式是 **寄存器寻址**，目标操作数的寻址方式是 **寄存器间接寻址**。

### 推理

在指令

```asm
MOV [BX], AL
```

中：

- `AL` 是源操作数，操作数直接位于寄存器 `AL` 中，因此采用**寄存器寻址**。
- `[BX]` 是目标操作数，有效地址存放在寄存器 `BX` 中，因此采用**寄存器间接寻址**。

即：

$$
\text{EA} = (\text{BX})
$$

其中 $\text{EA}$ 为有效地址。

知识点：[80486/8086的寻址方式（立即、寄存器、直接、间接、变址等）](../../../topics/微机接口/xunzhi-fangshi.md)、[80486/8086基本结构寄存器（通用、段、控制寄存器）](../../../topics/微机接口/jiben-jicunqi.md)

### 填空 2

$(147.75)_{10} = ($ **$10010011.11_2$** $)_{2} = ($ **$93.C_{16}$** $)_{16}$。

参考解答：填空 2

结论：  
$(147.75)_{10}=(10010011.11)_2=(93.C)_{16}$

推理：

整数部分：  
$147\div2=73$ 余 $1$，$73\div2=36$ 余 $1$，$36\div2=18$ 余 $0$，$18\div2=9$ 余 $0$，$9\div2=4$ 余 $1$，$4\div2=2$ 余 $0$，$2\div2=1$ 余 $0$，$1\div2=0$ 余 $1$。  
倒序得：$10010011_2$。

小数部分：  
$0.75\times2=1.5$ 取 $1$，余 $0.5$；  
$0.5\times2=1.0$ 取 $1$。  
得：$0.11_2$。

所以：  
$(147.75)_{10}=10010011.11_2$。

转十六进制：  
二进制四位一组，$1001\ 0011\ .\ 1100$  
即 $9\ 3\ .\ C$。  
所以：  
$10010011.11_2=93.C_{16}$。

知识点：[数制转换（二进制、十进制、十六进制互转）](../../../topics/微机接口/shuzhi-zhuanhuan.md)

### 填空 3

系统总线按其传送信号的类型可分为 **地址总线**、**数据总线** 和 **控制总线**。

参考解答：系统总线按其传送信号的类型可分为 **地址总线**、**数据总线** 和 **控制总线**。

- **地址总线**：传送 CPU 发出的内存或 I/O 端口地址，用于选择访问对象。
- **数据总线**：在 CPU、存储器和 I/O 接口之间传送数据。
- **控制总线**：传送读写、中断、时钟等控制与状态信号，协调各部件工作。

知识点：[总线的基本概念与分类（内部总线、系统总线、外部总线）](../../../topics/微机接口/zongxian-gainian.md)

### 填空 4

实模式下，逻辑地址为 F000H:0100H 的存储单元，其物理地址是 **F0100H**。

计算过程：$Physical Address = Segment \times 16 + Offset = F000H \times 10H + 0100H = F0000H + 0100H = F0100H$。

参考解答：**F0100H**

在 8086 实模式下，物理地址由段地址左移 4 位（即乘以 $16$ 或 $10H$）加上偏移地址得到。
计算过程如下：
$$
\begin{aligned}
\text{Physical Address} &= \text{Segment} \times 10H + \text{Offset} \\
&= F000H \times 10H + 0100H \\
&= F0000H + 0100H \\
&= F0100H
\end{aligned}
$$

知识点：[实地址模式下物理地址的形成（段基址×10H+偏移量）](../../../topics/微机接口/wuli-dizhi.md)、[存储单元和存储器地址的概念](../../../topics/微机接口/cunchu-danyuan.md)

### 填空 5

I/O 端口的编址方式有 **统一编址（存储器映射）** 和 **独立编址（I/O映射）** 。在 PC 机系统中，采用的 I/O 端口编址方式是 **独立编址**。

参考解答：PC 机采用的 I/O 端口编址方式为**独立编址（I/O 映射）**。

- 统一编址将 I/O 端口和存储器单元安排在同一地址空间，用统一的访存指令访问；
- 独立编址将 I/O 端口单独编址，独立于存储器地址空间，CPU 需通过专门的 `IN`/`OUT` 指令访问端口。
- PC/AT 兼容机使用专门的 I/O 指令及 `IOR#`/`IOW#` 控制信号，故属于**独立编址**。

知识点：[端口的编址方式（统一编址与独立编址）](../../../topics/微机接口/duankou-bianzhi.md)

### 填空 6

80X86有两个引脚可以接收外部的硬件中断请求，这两个引脚的名称分别是 **NMI**（非屏蔽中断） 和 **INTR**（可屏蔽中断）。

参考解答：**结论**
**NMI** 和 **INTR**

**推理**
80X86 的硬件中断引脚中，**NMI** 为非屏蔽中断，响应不可被 IF 标志屏蔽；**INTR** 为可屏蔽中断，响应受 IF 标志控制。它们共同构成外部硬件中断的“两线”入口。

知识点：[微型计算机的硬件基本结构](../../../topics/微机接口/weixingji-yingjian.md)、[80486/8086基本结构寄存器（通用、段、控制寄存器）](../../../topics/微机接口/jiben-jicunqi.md)

### 填空 7

PC 系列中，可屏蔽硬件中断的中断类型码由 **外设（或中断控制器如8259A）** 提供；软件中断的中断类型码由 **INT n 指令中的n** 提供。

参考解答：PC 系列中，可屏蔽硬件中断的中断类型码由 **中断控制器（如 8259A）** 提供；软件中断的中断类型码由 **中断指令的操作数 n** 提供。

**推理过程：**
- **可屏蔽硬件中断**：外设通过 INTR 线向 CPU 发出请求，CPU 响应后向中断控制器发送中断应答信号。8259A 等控制器收到应答后，将对应请求的中断类型码（由初始化编程时设定的高 5 位 + 请求端的编号组成）送上数据总线供 CPU 读取。
- **软件中断**：由 `INT n` 指令直接引发，CPU 无需外部应答，直接从指令编码中取得的 n 作为中断类型码。

知识点：[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 填空 8

异步通信一帧数据格式中，按照发送的次序，先传送 **起始位**，紧接着是数据位，数据位后为 **校验位（或停止位前的可选位，通常题目若无校验则直接接停止位，但标准帧包含校验位时在此处填校验位，若题目设定无校验则此处可能指代校验位的位置为空或题目隐含校验位存在。根据常见考题“8位数据，1位停止，无校验”，则数据位后直接为停止位。但若填空留空，通常考察标准帧结构：起始位->数据位->校验位->停止位。鉴于题目第4大题提到“无校验”，此处填空可能期望填写标准结构中的**校验位**，或者如果严格对应本题语境，可能是**校验位（若有）**。*注：根据第4题条件“无校验”，标准帧变为：起始位、数据位、停止位。但填空题通常考察通用概念，故填**校验位**更为稳妥，或者若必须严格对应无校验场景，则此空可能不存在或填“无”。但在大多数教材填空题中，此位置填**校验位**。*）

*(修正：根据常见题库，此空通常填**校验位**，即使后续题目说无校验，也是考察帧结构的组成部分)*

参考解答：**校验位**

异步串行通信的标准帧结构按发送顺序依次为：起始位 $\rightarrow$ 数据位 $\rightarrow$ **校验位** $\rightarrow$ 停止位。虽然具体通信协议可配置为无校验（此时数据位后直接接停止位），但在考察通用帧格式组成的填空题中，该位置通常指代校验位。

知识点：[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 填空 9

串行数据传输方式有 **单工**、**半双工** 和 **全双工** 三种。

![图 1](../.assets/微型计算机原理与接口技术期末试卷A卷.assets/fe88677096f10075f6fddd428b4d3b159451f707ddd69cd3d1e3ea80ff8f0408.jpg)

## 三、计算和简答题（每小题 5 分，共 20 分）

参考解答：单工、半双工、全双工

串行数据传输按数据传送方向分为三种方式：单工（数据只能单方向传输）、半双工（数据可双向传输但不能同时进行）、全双工（数据可同时双向传输）。

知识点：[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 简答 1

字长=8，X=-75,Y=+86, 求$[X]_{补}$和$[Y]_{补}$,并用补码计算 X+Y。要求有运算过程并对结果是否溢出进行分析。

**解答：**

1.  **求 $[X]_{补}$ (X = -75):**
    *   $|X| = 75 = 01001011_2$
    *   $[X]_{原} = 11001011_2$ (最高位为符号位1)
    *   $[X]_{反} = 10110100_2$ (符号位不变，数值位取反)
    *   $[X]_{补} = 10110101_2$ (反码末位加1)
    *   即 $[X]_{补} = B5H$

2.  **求 $[Y]_{补}$ (Y = +86):**
    *   $|Y| = 86 = 01010110_2$
    *   正数原码、反码、补码相同。
    *   $[Y]_{补} = 01010110_2$
    *   即 $[Y]_{补} = 56H$

3.  **计算 $X+Y$:**
    $$
    \begin{array}{r}
      10110101 \\
    + 01010110 \\
    \hline
      00001011
    \end{array}
    $$
    *   结果 $[X+Y]_{补} = 00001011_2 = 0BH = 11$

4.  **溢出分析:**
    *   采用双高位判别法或符号位进位与最高有效位进位异或判断。
    *   符号位进位 $C_s = 0$ (因为 $1+0=1$，无进位到更高位，这里看第7位向第8位的进位，实际上是 $1+0=1$，无进位？不对，让我们仔细看加法：
        *   Bit 7 (Sign): $1 + 0 = 1$, 进位 $C_7 = 0$
        *   Bit 6: $0 + 1 = 1$, 进位 $C_6 = 0$
        *   ...
        *   实际上，$10110101 + 01010110$:
            *   LSB: $1+0=1$
            *   Bit 1: $0+1=1$
            *   Bit 2: $1+1=0$, Carry=1
            *   Bit 3: $0+0+1=1$, Carry=0
            *   Bit 4: $1+1=0$, Carry=1
            *   Bit 5: $1+0+1=0$, Carry=1
            *   Bit 6: $0+1+1=0$, Carry=1
            *   Bit 7 (Sign): $1+0+1=0$, Carry=1
    *   符号位进位 $C_s = 1$ (Bit 7 向 Bit 8 的进位)
    *   最高有效位进位 $C_{s-1} = 1$ (Bit 6 向 Bit 7 的进位)
    *   $OF = C_s \oplus C_{s-1} = 1 \oplus 1 = 0$
    *   **结论：无溢出。**
    *   验证：$-75 + 86 = 11$，结果正确且在8位补码范围 $[-128, 127]$ 内。

参考解答：## 参考解答

**结论：** $[X]_{补}=10110101\text{B}$（B5H），$[Y]_{补}=01010110\text{B}$（56H），$X+Y=+11$（0BH），**无溢出**。

### 1. 求补码

- $75 = 64+8+2+1 = 01001011\text{B}$，故
  $$[X]_{补} = [X]_{反}+1 = 10110100\text{B}+1 = 10110101\text{B} = \text{B5H}$$
- $86 = 64+16+4+2 = 01010110\text{B}$，正数补码同原码：
  $$[Y]_{补} = 01010110\text{B} = 56\text{H}$$

### 2. 补码加法

$$
\begin{array}{r}
  10110101 \\
+\ 01010110 \\
\hline
\boxed{1}\,00001011
\end{array}
$$

丢弃末位进位，得
$$[X+Y]_{补} = 00001011\text{B} = 0\text{BH} = +11$$

与实际 $-75+86=11$ 一致。

### 3. 溢出分析

双高位法：

- $C_s$（符号位进位，第 7 位向第 8 位的进位）$=1$
- $C_{s-1}$（次高位向符号位的进位）$=1$
$$OF = C_s \oplus C_{s-1} = 1\oplus 1 = 0$$

**无溢出**（异号两数相加必不溢出；结果 $+11$ 也在 8 位补码范围 $[-128,127]$ 内）。

知识点：[真值数与补码的相互转换及补码计算](../../../topics/微机接口/zhenzhi-buma.md)、[算术运算与逻辑运算指令（ADD、SUB、MUL、AND、OR、NOT等）](../../../topics/微机接口/suanlu-yunsuan.md)、[数制转换（二进制、十进制、十六进制互转）](../../../topics/微机接口/shuzhi-zhuanhuan.md)

### 简答 2

简述CPU响应非屏蔽中断和可屏蔽中断的条件。

**解答：**

1.  **响应非屏蔽中断 (NMI) 的条件：**
    *   CPU 正在执行完当前指令。
    *   NMI 引脚上有有效的上升沿（或高电平，取决于具体架构，x86通常是上升沿触发）中断请求信号。
    *   *注意：NMI 不受 IF 标志位控制，只要发生即响应（除非CPU处于停机等特殊状态）。*

2.  **响应可屏蔽中断 (INTR) 的条件：**
    *   CPU 正在执行完当前指令。
    *   INTR 引脚上有有效的中断请求信号。
    *   **IF (Interrupt Flag) = 1**（即中断允许）。
    *   没有更高优先级的中断正在处理（或同级中断未被锁存/屏蔽）。
    *   CPU 发出中断响应信号 $\overline{INTA}$。

参考解答：### 简答 2

**结论：** 两者均需在**当前指令执行结束后**才采样并响应；区别在于 **NMI 不受 IF 控制**，而 **INTR 必须满足 IF=1（开中断）**且通常还受中断屏蔽/优先级管理控制。

- **非屏蔽中断 NMI 的响应条件**
  1. CPU 执行完当前指令；
  2. NMI 请求有效（x86 中通常为上升沿触发）；
  3. NMI **不受 IF 标志影响**，一般不能被软件屏蔽（特殊状态如停机除外）。

- **可屏蔽中断 INTR 的响应条件**
  1. CPU 执行完当前指令；
  2. INTR 请求有效；
  3. **IF = 1**（允许中断）；若 **IF = 0** 则不响应；
  4. 未被中断控制器屏蔽，且优先级允许（无更高优先级中断先响应）；
  5. CPU 进入中断响应周期（如发出 $\overline{INTA}$）并获取中断向量/类型号。

知识点：[微型计算机的硬件基本结构](../../../topics/微机接口/weixingji-yingjian.md)、[微处理器的工作模式（实模式、保护模式、虚拟8086模式）](../../../topics/微机接口/gongzuo-moshi.md)、[微机系统与I/O端口的信息交换方式（无条件、查询、中断、DMA）](../../../topics/微机接口/xinxi-jiaohuan.md)

### 简答 3

设 8255A的方式选择命令字为 80H，说明各个数据口的工作方式和输入/输出方向。

**解答：**

1.  **解析控制字 80H (二进制 1000 0000):**
    *   D7 = 1: 标志位，表示这是方式选择控制字。
    *   D6-D5 = 00: A口工作于方式0（基本输入输出）。
    *   D4 = 1: A口为输入。
    *   D3 = 0: B口工作于方式0（基本输入输出）。
    *   D2 = 0: B口为输出。
    *   D1 = 0: C口高4位 (PC7-PC4) 为输出。
    *   D0 = 0: C口低4位 (PC3-PC0) 为输出。

2.  **结论：**
    *   **A口：** 方式0，输入。
    *   **B口：** 方式0，输出。
    *   **C口：** 高4位输出，低4位输出。（即C口整体作为输出使用，但在方式0下通常配合A/B口使用，此处仅根据控制字定义方向）。

参考解答：**结论：** A口工作于方式0，输入；B口工作于方式0，输出；C口高4位（PC7~PC4）输出，低4位（PC3~PC0）输出。

---

**推理过程：**

8255A 的方式选择控制字为 $80\text{H} = 1000\,0000\text{B}$，各位含义如下：

| 位 | 值 | 含义 |
|:---:|:---:|:---|
| D7 | 1 | 特征位，表示此为**方式选择控制字** |
| D6D5 | 00 | A组工作方式：**方式0** |
| D4 | 0 | A口方向：**输入** |
| D3 | 0 | C口高4位方向：**输出** |
| D2 | 0 | B组工作方式：**方式0** |
| D1 | 0 | B口方向：**输出** |
| D0 | 0 | C口低4位方向：**输出** |

> **注：** 原题所附解析中 D4 误写为 1，实际 $80\text{H}$ 的 D4 = 0，对应 A口应为**输入**。此处以正确二进制展开为准。

知识点：[接口电路的作用和基本功能](../../../topics/微机接口/jiekou-gongneng.md)、[端口的概念与分类（数据端口、状态端口、控制端口）](../../../topics/微机接口/duankou-gainian.md)

### 简答 4

系统启动后，设内存地址 184H～187H的四个单元中的内容依次为 12H，34H，56H，78H，请问该四个单元存放的是哪一型中断向量？该型中断服务程序的入口物理地址是多少？

**解答：**

1.  **确定中断类型号：**
    *   中断向量表（IVT）位于内存最低端，每个中断向量占4字节。
    *   中断类型号 $n$ 对应的向量起始物理地址为 $n \times 4$。
    *   已知向量存放在 184H ~ 187H。
    *   起始地址 $184H = n \times 4$。
    *   $n = 184H / 4 = 184H / 100_2 = 184H >> 2 = 61H$。
    *   所以，这是 **61H 号** 中断向量。

2.  **确定中断服务程序入口地址：**
    *   Intel 8086/8088 的中断向量格式为：偏移地址（低两字节）在前，段地址（高两字节）在后。
    *   内存内容：
        *   184H: 12H (Offset Low)
        *   185H: 34H (Offset High)
        *   186H: 56H (Segment Low)
        *   187H: 78H (Segment High)
    *   偏移地址 IP = 3412H
    *   段地址 CS = 7856H

3.  **计算物理地址：**
    *   物理地址 = $CS \times 10H + IP$
    *   物理地址 = $7856H \times 10H + 3412H$
    *   物理地址 = $78560H + 3412H$
    *   物理地址 = $7B972H$

**答案：**
*   中断类型号：**61H**
*   入口物理地址：**7B972H**

## 四、综合应用（40 分）

参考解答：**答案：**  
中断类型号为 **61H**；中断服务程序入口物理地址为 **7B972H**。

**推理与计算：**

1. 中断向量存放在内存最低端的中断向量表中，每个中断向量占 4 字节。  
   若向量起始地址为 184H，则：

   
$$
184H = n \times 4
$$

   所以：

   
$$
n = \frac{184H}{4} = 61H
$$

   因此该四个单元存放的是 **61H 型中断向量**。

2. 8086/8088 中断向量格式为：  
   - 低两字节：偏移地址 IP  
   - 高两字节：段地址 CS  

   四个单元内容为：

   
$$
184H:12H,\quad 185H:34H,\quad 186H:56H,\quad 187H:78H
$$

   所以：

   
$$
IP = 3412H,\quad CS = 7856H
$$

3. 物理地址：

   
$$
\text{物理地址} = CS \times 10H + IP
$$

   
$$
= 7856H \times 10H + 3412H
$$

   
$$
= 78560H + 3412H = 7B972H
$$

因此：  
中断类型号：**61H**  
入口物理地址：**7B972H**

知识点：[实地址模式下物理地址的形成（段基址×10H+偏移量）](../../../topics/微机接口/wuli-dizhi.md)、[数制转换（二进制、十进制、十六进制互转）](../../../topics/微机接口/shuzhi-zhuanhuan.md)

### 综合 1

编写一程序段，把 AL 低四位和 AH 低四位拼装成一个字节（AL 低四位为拼装后的高四位）→AH。(6分)

**解答：**

```assembly
; 假设初始数据在 AL 和 AH 中
; 目标：将 AL 的低4位移到 AH 的高4位，AH 的低4位移到 AH 的低4位，结果存回 AH

    MOV BL, AL       ; 保存 AL 的值到 BL
    AND BL, 0FH      ; BL 保留 AL 的低4位 (0000xxxx)
    MOV CL, 4        ; 移位次数
    SHL BL, CL       ; BL 左移4位，变成 xxxx0000
    AND AH, 0FH      ; AH 清零高4位，只保留低4位 (0000yyyy)
    OR  AH, BL       ; 合并：AH = yyyy | xxxx0000 = xxxxyyyy
```

参考解答：**结论：**

```assembly
    AND AH, 0FH      ; 屏蔽AH高4位，保留低4位
    MOV BL, AL       ; 暂存AL
    AND BL, 0FH      ; 屏蔽BL高4位，保留AL的低4位
    MOV CL, 4
    SHL BL, CL       ; BL左移4位，使AL低4位移至高4位
    OR  AH, BL       ; 拼装：AH高4位(AL低4位) | AH低4位 → AH
```

**推理过程：**

1. **提取有效位**：用 `AND reg, 0FH`（即 `AND reg, 00001111B`）分别屏蔽掉 AL 和 AH 的高四位，只保留各自的低四位。
2. **移位对齐**：将 AL 的低四位左移 4 位（`SHL BL, CL`，其中 `CL=4`），使其占据字节的高四位位置，即从 `0000xxxx` 变为 `xxxx0000`。
3. **逻辑拼装**：用 `OR` 指令将移位后的结果与已屏蔽高四位的 AH 按位或，完成拼装：
   $$ \text{AH} = \underbrace{xxxx}_{\text{原AL低4位}} \underbrace{yyyy}_{\text{原AH低4位}} $$

> **注**：8086 中移位次数大于 1 时，必须先将移位次数送入 `CL` 寄存器，不能直接用立即数（如 `SHL BL, 4` 是 80186+ 才支持的语法）。

知识点：[移位与循环移位指令（SHL、SHR、ROL、ROR等）](../../../topics/微机接口/yiwei-xunhuan.md)、[算术运算与逻辑运算指令（ADD、SUB、MUL、AND、OR、NOT等）](../../../topics/微机接口/suanlu-yunsuan.md)、[数据传送指令（MOV、PUSH、POP、XCHG等）](../../../topics/微机接口/shuju-chuansong.md)

### 综合 2

设堆栈段寄存器SS=2000H，SP=0100H，阅读下面程序片段，完成相应空格。（4 分）

```assembly
(1) MOV AX,1234H
(2) MOV BX,5678H
(3) PUSH AX
(4) PUSH BX
(5) POP AX
(6) ADD AH,AL
(7) MOV BL,AH
```

执行完第(4)条指令后 SP= **00FE** H，执行完第(5)条指令后 AX= **5678** H，SS= **2000** H,执行完第(7)条指令后BX= **34** H。

**解析：**
1.  **初始状态：** SS=2000H, SP=0100H。
2.  **(3) PUSH AX:** AX=1234H。栈顶指针 SP 减 2，SP = 0100H - 2 = 00FEH。内存 [2000:00FE] 存入 1234H。
3.  **(4) PUSH BX:** BX=5678H。栈顶指针 SP 减 2，SP = 00FEH - 2 = **00FEH**? 不对，是 00FEH -> 00FCH。
    *   Wait, let's re-calculate carefully.
    *   Start SP = 0100H.
    *   Push AX: SP becomes 00FEH. Data at 00FEH is 1234H.
    *   Push BX: SP becomes 00FEH - 2 = **00FCH**. Data at 00FCH is 5678H.
    *   *Correction on the question prompt interpretation:* The question asks for SP after instruction (4). Instruction (4) is `PUSH BX`. So SP should be **00FCH**.
    *   Let's check the provided text again. "执行完第(4)条指令后 SP= H".
    *   Calculation: $0100H - 2 (Push AX) - 2 (Push BX) = 00FCH$.
    *   *Self-Correction*: Did I miss something? No. Standard x86 stack grows down.
    *   Let's re-read the options or standard answers if available. Usually, these questions are straightforward.
    *   SP after (4) is **00FCH**.

4.  **(5) POP AX:** 从栈顶弹出数据到 AX。栈顶当前是 00FCH 处的 5678H (因为刚才Push了BX)。
    *   所以 AX = **5678H**。
    *   SP 恢复为 00FEH。
    *   SS 保持不变，仍为 **2000H**。

5.  **(6) ADD AH, AL:**
    *   此时 AX = 5678H。
    *   AH = 56H, AL = 78H。
    *   $56H + 78H = CEH$。
    *   所以 AH = CEH, AL = 78H (ADD不影响AL，只影响AH和标志位，但在8086中ADD AH,AL只修改AH)。AX 变为 CE78H。

6.  **(7) MOV BL, AH:**
    *   AH = CEH。
    *   所以 BL = **CEH**。

**最终填空答案：**
*   SP after (4): **00FC**
*   AX after (5): **5678**
*   SS after (5): **2000**
*   BX after (7): **CE**

*(注：如果原题意图是POP之后AX变回原来的值，那是错的，POP出的是最后压入的BX。如果题目是POP BX，那AX还是1234。但题目是POP AX。)*

参考解答：执行完第(4)条指令后 SP= **00FC** H，执行完第(5)条指令后 AX= **5678** H，SS= **2000** H，执行完第(7)条指令后 BX= **56CE** H。

**推理过程：**
1. **初始状态：** SS=2000H，SP=0100H。
2. **执行(3) PUSH AX：** 栈向低地址增长，SP 减 2，SP = 0100H - 2 = 00FEH。
3. **执行(4) PUSH BX：** SP 再减 2，SP = 00FEH - 2 = **00FCH**。此时栈顶存放的是 BX 的值 5678H。
4. **执行(5) POP AX：** 将栈顶数据弹出到 AX，故 AX = **5678H**，SP 恢复为 00FEH。堆栈段寄存器 SS 始终不变，仍为 **2000H**。
5. **执行(6) ADD AH, AL：** 此时 AH=56H，AL=78H。计算 $56H + 78H = CEH$，结果存入 AH，故 AH=CEH。
6. **执行(7) MOV BL, AH：** 将 AH 的值赋给 BL，故 BL=CEH。由于 BH 未被修改，保持初值 56H，因此 BX = BH:BL = **56CEH**。

知识点：[堆栈的概念及SP指针操作](../../../topics/微机接口/duizhan-caozuo.md)、[80486/8086基本结构寄存器（通用、段、控制寄存器）](../../../topics/微机接口/jiben-jicunqi.md)、[数据传送指令（MOV、PUSH、POP、XCHG等）](../../../topics/微机接口/shuju-chuansong.md)

### 综合 3

PC系统外扩使用了一片可编程定时/计数器8254，8254的输入时钟是8MHz。（10分）

（1）下列是CPU对8254的初始化程序段，根据要求完成相关内容。
```assembly
MOV AL, 01110110B
MOV DX, 207H ;写控制字
OUT DX, AL
MOV AX, 2000 ;写计数初值
MOV DX, 205H
OUT DX, AL
MOV AL, AH
OUT DX, AL
```
由上述程序段可知，设计时使用了8254的 **2** 号计数器，其口地址是 **205** H，工作在方式 **3** ，使用了 **16** 进制计数，计数初值是 **2000** ，输出信号的频率是 **1KHz** Hz。（6分）

**解析：**
1.  **控制字解析 (01110110B = 76H):**
    *   D7D6 = 01: 选择计数器 **2**。
    *   D5D4 = 11: 先读/写低8位，再读/写高8位 (**16位计数**)。
    *   D3D2D1 = 110: 工作方式 **3** (方波发生器)。
    *   D0 = 0: 二进制计数 (**16进制** 指的是16位计数，即模65536，通常称为二进制模式，但在填空题中，“16进制计数”有时指16位宽度，或者BCD？这里D0=0是二进制。如果D0=1是BCD。题目问“使用了__进制计数”，通常对应D0位。01110110B中D0=0，所以是**二**进制。*但是*，很多教材将16位计数称为“16位二进制”。如果空里填“二”，则符合D0。如果填“16”，则指位数。结合后文“计数初值2000”，2000H是十六进制表示，但计数模式本身是二进制。通常标准答案填 **二** 进制。
    *   *Correction*: Let's look at the control word bits again. `0111 0110`.
        *   D7-D6: 01 -> Counter 2.
        *   D5-D4: 11 -> Read/Write LSB then MSB (16-bit).
        *   D3-D1: 110 -> Mode 3.
        *   D0: 0 -> Binary.
    *   So, Counter: **2**. Port: **205H** (Control is 207H, Counter 2 is typically Base+2, so 205H fits if Base is 203H? Or if Base is 205H, Control is 207H. Yes. C=Base+2, B=Base+1, A=Base. If Control=207H, then C2=205H. Correct.)
    *   Mode: **3**.
    *   Counting Format: **二** (Binary). (Note: Some contexts might ask for "16-bit", but "binary" vs "BCD" is the format choice).
    *   Initial Count: **2000H** (or decimal 8192). The program moves AX=2000. It writes low byte first (AL=00), then high byte (AH=20). So count is 2000H.
    *   Output Frequency:
        *   Input Clock $f_{in} = 8 MHz = 8 \times 10^6 Hz$.
        *   Count $N = 2000H = 8192$.
        *   $f_{out} = f_{in} / N = 8,000,000 / 8,192$.
        *   $8,000,000 / 8,192 = 1000 / 1.024$? No.
        *   $8192 = 2^{13}$.
        *   $8 MHz = 8 \times 10^6$. This is not a power of 2.
        *   Wait, $8,000,000 / 8,192 = 976.5625 Hz$.
        *   Is it possible the clock is $8.192 MHz$? Or the count is different?
        *   Let's re-read: "输入时钟是8MHz". Count "2000" (Hex 2000 is 8192).
        *   Maybe the question implies Hex 2000 as decimal? No, MOV AX, 2000 usually means hex in assembly context unless specified, but here it's just numbers. In assembly `MOV AX, 2000` loads decimal 2000 if no suffix, or hex if `2000H`. The code says `MOV AX, 2000`. In MASM/TASM, this is decimal 2000.
        *   If Count = 2000 (Decimal):
            *   $f_{out} = 8,000,000 / 2000 = 4000 Hz = 4 kHz$.
        *   If Count = 2000H (Hex, i.e., 8192 Decimal):
            *   $f_{out} = 8,000,000 / 8192 \approx 976.56 Hz$.
        *   Which one is intended? The code `MOV AX, 2000` without 'H' suffix in assembly language source code usually denotes **decimal** 2000. However, often in exam questions, they might write `2000` meaning hex if they are sloppy, or `2000H`. Given the previous question used hex notation explicitly (`12H`), and here it is `2000`, it is likely **decimal** 2000.
        *   Let's check the frequency calculation for 2000 decimal: $8MHz / 2000 = 4kHz$. This is a nice round number.
        *   Let's check the frequency calculation for 2000H: ~976Hz. Not a round number.
        *   Therefore, Count is likely **2000** (decimal).
        *   Frequency: **4000** Hz.

    *   *Re-evaluating "Used __ counting"*: If the answer for format is Binary, then it's consistent.

    **Filled Blanks:**
    *   Counter: **2**
    *   Port Address: **205**
    *   Mode: **3**
    *   Counting Format: **二** (Binary)
    *   Initial Count: **2000**
    *   Output Frequency: **4000**

（2）不改变输入时钟的频率，想使该计数器的输出信号周期变大，初始化时应采取什么措施？输出周期最大是多少？ （4分）

**解答：**
1.  **措施：** 增大计数初值 $N$。因为 $T_{out} = N \times T_{in}$，周期与计数初值成正比。
2.  **最大输出周期：**
    *   8254 是 16 位计数器，最大计数值为 $FFFFH = 65535$ (Decimal)。
    *   输入时钟周期 $T_{in} = 1 / 8 MHz = 0.125 \mu s$。
    *   最大输出周期 $T_{max} = 65535 \times T_{in} = 65535 \times 0.125 \mu s \approx 8191.875 \mu s \approx 8.19 ms$。
    *   或者用频率算：$f_{min} = 8 MHz / 65535 \approx 122.07 Hz$。
    *   $T_{max} = 1 / f_{min} \approx 8.19 ms$。

参考解答：### （1）填空题参考解答

2；205；3；二；2000；4000

**推理与计算过程：**

1.  **控制字解析**：控制字 `01110110B` ($76\text{H}$) 各位含义如下：
    -   $\text{D7D6}=01$：选择 **2** 号计数器。
    -   $\text{D5D4}=11$：先写低字节后写高字节，即 **16** 位读写。
    -   $\text{D3D2D1}=110$：工作于方式 **3**（方波发生器）。
    -   $\text{D0}=0$：采用 **二** 进制计数（$\text{D0}=1$ 为 BCD 码）。
2.  **端口地址**：控制口地址为 $207\text{H}$，8254 各计数器端口依次递增，故 2 号计数器口地址为 $207\text{H} - 2 = \mathbf{205}\text{H}$。
3.  **计数初值**：汇编指令 `MOV AX, 2000` 未带 `H` 后缀，默认为十进制数 **2000**。程序先输出 AL（低字节 $00$），再输出 AH（高字节 $07\text{D0H}$ 的低8位对应十进制2000的高字节），组合后初值 $N=2000$。
4.  **输出频率计算**：
    $$
    f_{out} = \frac{f_{clk}}{N} = \frac{8 \times 10^6}{2000} = 4000 \text{ Hz}
    $$

> **注**：若将 `2000` 误判为十六进制 $2000\text{H}$（即十进制 8192），则 $f_{out} \approx 976.56 \text{ Hz}$，非整数结果不符合出题常规；且汇编语法中无后缀即为十进制，故取 4000 Hz。

---

### （2）增大输出周期的措施及最大值

**结论：** 应 **增大计数初值 $N$**；最大输出周期为 **8.192 ms**。

**推理与计算过程：**

1.  **措施依据**：8254 方式 3 下输出周期 $T_{out} = N \cdot T_{clk}$，在输入时钟不变时，$T_{out}$ 与计数初值 $N$ 成正比，故需增大 $N$。
2.  **最大周期计算**：
    -   8254 为 16 位二进制计数器，最大计数初值 $N_{max} = 65535$（写入 $0000\text{H}$ 时等效于 65536，但方式 3 下 $N=0$ 实际产生 $N=65536$ 的计数，部分教材取 65536；此处按保守有效最大值 65535 或标准满量程 65536 均可，以下按 **65536** 计算，因写入 0 是合法操作）：
    $$
    T_{max} = \frac{N_{max}}{f_{clk}} = \frac{65536}{8 \times 10^6} = 8.192 \times 10^{-3} \text{ s} = 8.192 \text{ ms}
    $$
    -   若严格按 $N_{max}=65535$ 计算，则 $T_{max} = 65535 / (8 \times 10^6) \approx 8.1919 \text{ ms}$，两者在工程上等价，标准答案通常取 **8.192 ms**（对应 $N=65536$ 的满量程分频）。

知识点：[端口的编址方式（统一编址与独立编址）](../../../topics/微机接口/duankou-bianzhi.md)、[最常用的I/O指令（IN、OUT的直接寻址与DX间址）](../../../topics/微机接口/io-zhiling.md)、[数制转换（二进制、十进制、十六进制互转）](../../../topics/微机接口/shuzhi-zhuanhuan.md)

### 综合 4

利用甲、乙两台计算机的主串口直接相连进行单工通信。甲发送，乙接收。双方通信前约定：8位数据位，1 位停止位，无校验，通信速率为2400bps(分频系数为 0018H)，双方均采用查询方式进行数据的发送和接收。（20分）

（1）求每秒能传输多少个字符？如果需要传送一个字符‘A’，要求画出串行异步通信的一帧字符格式，并标出各部分的逻辑电平（TTL）和位数。（4分）

**解答：**
1.  **每秒传输字符数：**
    *   波特率 = 2400 bps。
    *   每帧位数 = 1 (起始位) + 8 (数据位) + 0 (校验位) + 1 (停止位) = 10 位。
    *   每秒字符数 = $2400 / 10 = 240$ 个字符/秒。

2.  **字符 'A' 的帧格式：**
    *   ASCII 'A' = 65 = $01000001_2$。
    *   低位在前 (LSB First)。
    *   数据位序列 (从低到高): 1, 0, 0, 0, 0, 0, 1, 0。
    *   空闲状态 (Idle): 高电平 (1)。
    *   起始位: 低电平 (0)。
    *   停止位: 高电平 (1)。

    **波形描述：**
    *   Idle: High (1)
    *   Start Bit: Low (0) for 1 bit time
    *   Data Bits (LSB to MSB):
        *   Bit 0: 1 (High)
        *   Bit 1: 0 (Low)
        *   Bit 2: 0 (Low)
        *   Bit 3: 0 (Low)
        *   Bit 4: 0 (Low)
        *   Bit 5: 0 (Low)
        *   Bit 6: 1 (High)
        *   Bit 7: 0 (Low)
    *   Stop Bit: High (1) for 1 bit time

    *(注：画图时需画出时序图，标明高低电平和对应的位)*

（2）请将下列甲机用查询方式发送字符‘A’的程序段补充完整。（6分）

```assembly
SCANT:
    MOV DX, ① _________
    IN  AL, DX          ; 假设原代码漏写了IN，或者TEST之前需要读取状态
    TEST AL, 3          ; 检查状态位？通常查询发送就绪是检查THRE (Transmitter Holding Register Empty)
                        ; 8250 Status Register: Bit 0 = RDRF, Bit 1 = FE, Bit 2 = PE, Bit 3 = OE, Bit 5 = THRE, Bit 6 = TEMT
                        ; 题目中 TEST AL, 3 (binary 00000011) 检查的是 Bit 0 和 Bit 1。
                        ; Bit 0 is RDRF (Receiver Data Ready). Bit 1 is Error Flag.
                        ; This seems wrong for *sending*. Sending should check THRE (Bit 5).
                        ; HOWEVER, looking at the jump: SCANT is a loop label.
                        ; If the code is `TEST AL, 3` and jumps back, it's waiting for something related to bits 0 and 1.
                        ; Perhaps the question implies checking if the receiver is ready? No, it's sending.
                        ; Let's look at standard 8250 send loop:
                        ; Loop: IN AL, StatusPort
                        ;       TEST AL, 20H (Check THRE)
                        ;       JZ Loop
                        ;       OUT DataPort, AL
                        
                        ; The provided code snippet has `TEST AL, 3`. 
                        ; Maybe the prompt implies checking for errors or receiver ready? 
                        ; But it says "Send character 'A'".
                        ; Let's assume there is a typo in the question's mask or my understanding.
                        ; If it must be `TEST AL, 3`, maybe it's checking if the line is free? No.
                        
                        ; Let's look at the blanks.
                        ; ① Port Address for Status Register.
                        ; ② Instruction missing? `IN AL, DX` is implied or missing? The text shows `TEST AL, 3`. 
                        ; There must be an `IN AL, DX` before Test.
                        
                        ; Let's fill based on typical structure:
                        
SCANT:
    MOV DX, ① **203H**  ; Assuming Base Port 200H. Status Reg is Base+3. (Or whatever base matches the init in part 3)
                        ; We need to determine the base port from Part (3).
    IN  AL, DX          ; Read Status
    TEST AL, 3          ; This mask is suspicious for TX. 
                        ; If the question insists on 3, maybe it checks for specific conditions?
                        ; Or maybe it's `TEST AL, 20H` and the OCR read 3? Unlikely.
                        ; Let's assume the question meant to check THRE (Bit 5, value 20H) but wrote 3?
                        ; Or maybe it checks if the previous transmission is done?
                        
                        ; Let's look at the Jump. `JZ SCANT`? Or `JNZ`?
                        ; If we wait for THRE, we want THRE=1. TEST AL, 20H. If ZF=0 (not zero), it's set.
                        ; If the code is `TEST AL, 3`, and we loop, we are waiting for bits 0 and 1 to be 0.
                        ; Bit 0=0 means RDRF=0 (No data received). Bit 1=0 means No Error.
                        ; This doesn't help sending.
                        
                        ; Alternative: Maybe the code is for *receiving*? No, "甲发送".
                        
                        ; Let's assume standard 8250 Send Routine:
                        ; 1. Get Status Port Addr.
                        ; 2. Loop: Read Status. Check THRE (Bit 5). If not set, loop.
                        ; 3. Write Data to Data Port.
                        
                        ; Given the constraints, I will provide the most logical addresses assuming a standard base.
                        ; If Part 3 gives the base, we use it.
                        
                        ; Let's defer address determination to Part 3 logic.
                        ; Common Base for COM1 is 3F8H. Status: 3FDH. Data: 3F8H.
                        ; But the divisor was 0018H. Divisor Latch Access Bit (DLAB) needs to be set to write divisor.
                        
                        ; Let's look at the blanks again.
                        ; ① MOV DX, [Status Port Address]
                        ; ② [Missing Instruction?] The text shows `TEST AL, 3`. 
                        ; It is highly likely `IN AL, DX` is missing between MOV DX and TEST.
                        
                        ; Let's assume the question text has `IN AL, DX` implicitly or it's blank ②?
                        ; No, ① is after MOV DX.
                        
                        ; Let's provide the answers based on COM1 standard ports if not specified, 
                        ; or generic variables.
                        
                        ; Actually, looking at the table:
                        ; Row 1: MOV DX, ①
                        ; Row 2: (Empty?) -> Probably IN AL, DX
                        ; Row 3: TEST AL, 3
                        ; Row 4: SCANT (Jump?) -> JZ SCANT or JNZ SCANT?
                        
                        ; If testing for THRE (usually 20H), we want to loop while THRE=0.
                        ; TEST AL, 20H. JZ Loop.
                        
                        ; If the mask is strictly 3, and it's a send loop, it might be checking for "Line Free" in some custom protocol? Unlikely for 8250.
                        ; I will assume a typo in the question's mask and solve for standard THRE check, 
                        ; OR fill the blanks as requested.
                        
                        ; Blank ①: Status Port Address.
                        ; Blank ④ (in the table row 4): Jump instruction. Likely `JZ` (if checking for 0) or `JNZ`.
                        
                        ; Let's look at Part 3 to fix the Port Addresses.

（3）请完成对甲计算机的 I8250初始化程序段。（10分）

**解答：**

1.  **确定端口地址：**
    *   通常 PC 主串口 (COM1) 基地址为 **3F8H**。
    *   数据寄存器 (DR): **3F8H**
    *   中断允许寄存器 (IER): **3F8H** (当 DLAB=0)
    *   线路控制寄存器 (LCR): **3FBH**
    *   调制解调器控制寄存器 (MCR): **3FCH**
    *   线路状态寄存器 (LSR): **3FDH**
    *   调制解调器状态寄存器 (MSR): **3FDH** (当 DLAB=0)
    *   除数锁存器 (DLL/DLM): **3F8H/3F9H** (当 DLAB=1)

2.  **初始化步骤：**
    *   **设置波特率分频系数：**
        *   首先置 LCR 的 DLAB=1。
        *   写入分频系数。速率 2400bps，时钟 1.8432MHz (标准) 或 8MHz (题目给定)?
        *   题目说“分频系数为 0018H”。$18H = 24$ (Decimal).
        *   如果是 1.8432MHz 时钟：$1843200 / (16 \times 2400) = 1843200 / 38400 = 48 = 30H$.
        *   如果是 8MHz 时钟：$8000000 / (16 \times 2400) = 8000000 / 38400 \approx 208.3$. Not integer.
        *   题目直接给出了分频系数 **0018H** (即 24)。我们直接使用它。
        *   注意：写入顺序是先低后高。

    *   **设置数据格式：**
        *   8位数据，1位停止，无校验。
        *   LCR = $00110011_2 = 33H$ (D7-D6=00 Normal, D5-D4=11 8 bits, D3=0 No Parity, D2=0 1 Stop Bit, D1-D0=0 DLAB=0).

    *   **设置其他寄存器：**
        *   IER: 00H (禁止中断，因为是查询方式)。
        *   MCR: 00H 或 0BH (RTS, DTR, Out1, Out2). 简单起见通常写 00H 或 03H。

**程序段：**

```assembly
; 1. Set DLAB=1 to access Divisor Latches
    MOV DX, 3FBH        ; Line Control Register
    MOV AL, 80H         ; DLAB=1, other bits 0 (or keep existing if careful, but 80H is safe reset)
    OUT DX, AL

; 2. Write Divisor (0018H)
    MOV DX, 3F8H        ; Divisor Latch (LSB)
    MOV AL, 18H         ; Low byte of 24
    OUT DX, AL
    
    MOV DX, 3F9H        ; Divisor Latch (MSB)
    MOV AL, 00H         ; High byte of 24
    OUT DX, AL

; 3. Reset DLAB=0 and Set Word Length (8 data, 1 stop, no parity)
    MOV DX, 3FBH        ; Line Control Register
    MOV AL, 03H         ; 00000011B: 8 bits, 1 stop, no parity, DLAB=0
    OUT DX, AL

; 4. Disable Interrupts (IER)
    MOV DX, 3F8H        ; Interrupt Enable Register (same addr as DR when DLAB=0)
    MOV AL, 00H
    OUT DX, AL

; 5. Set Modem Control Register (MCR) - Optional but good practice
    MOV DX, 3FCH
    MOV AL, 0BH         ; RTS, DTR, Out1, Out2 asserted
    OUT DX, AL
```

参考解答：（1）每秒传输 **240 个字符**。  
字符 ‘A’（ASCII 65，即 $01000001_2$）的一帧格式如下（LSB 先发）：

| 起始位 | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 | 停止位 |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |

空闲和停止位为高电平，起始位为低电平。

（2）  
① **3FDH**  
② **JNZ SCANT**  
③ **3F8H**  
④ **OUT DX, AL**

理由：查询发送须先检测线路状态寄存器（3FDH）的发送保持寄存器空标志位 D5（20H），若为空（结果非零）则跳出发送，否则继续查询；发送数据写入发送保持寄存器（3F8H）。  
选项 3F9H 为中断允许寄存器，3FCH 为 MODEM 控制寄存器，3FAH 为中断识别寄存器，3FBH 为线路控制寄存器，均不能用于查询发送状态或写发送数据。

知识点：[ASCII码编码规则与常用字符编码](../../../topics/微机接口/ascii-ma.md)、[最常用的I/O指令（IN、OUT的直接寻址与DX间址）](../../../topics/微机接口/io-zhiling.md)、[80486/8086的寻址方式（立即、寄存器、直接、间接、变址等）](../../../topics/微机接口/xunzhi-fangshi.md)
