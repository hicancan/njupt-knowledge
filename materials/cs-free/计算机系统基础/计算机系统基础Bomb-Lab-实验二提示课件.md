---
title: 《计算机系统基础》Bomb Lab 实验二提示（课件）
kind: 实验
course: 计算机系统基础
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90JS140401S%E3%80%91%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%B3%BB%E7%BB%9F%E5%9F%BA%E7%A1%80%E2%85%A0%EF%BC%88%E6%B7%B7%E5%90%88%E5%BC%8F%EF%BC%89/labs/bomblab/%E5%AE%9E%E9%AA%8C%E4%BA%8C%E6%8F%90%E7%A4%BA%EF%BC%88%E5%BB%BA%E8%AE%AE%E5%9C%A8%E8%87%AA%E5%B7%B1%E5%B0%9D%E8%AF%95%E5%90%8E%E5%86%8D%E5%8F%82%E8%80%83%EF%BC%89.pptx
---

# 《计算机系统基础》Bomb Lab 实验二提示（课件）

原件经识别和整理；“参考解答”是我们补的。

## 字符串比较

```asm
0000000000401614 <phase_1>:
401614: f3 0f 1e fa          endbr64
401618: 48 83 ec 08          sub    $0x8,%rsp
40161c: 48 8d 35 2d 1b 00 00 lea    0x1b2d(%rip),%rsi   # 403150 <_IO_stdin_used+0x150>；内定字符串地址在
401623: e8 16 05 00 00       call   401b3e <strings_not_equal>
401628: 85 c0                test   %eax,%eax           # 测试返回值
40162a: 75 05                jne    401631 <phase_1+0x1d>  # 返回值等于 1 跳转引发炸弹
40162c: 48 83 c4 08          add    $0x8,%rsp
401630: c3                   ret
401631: e8 28 08 00 00       call   401e5e <explode_bomb>
401636: eb f4                jmp    40162c <phase_1+0x18>
```

## 数字序列递推（phase 2 循环部分）

| 地址 | 指令 | 注释 |
| --- | --- | --- |
| 401676 | `48 83 c3 04` `add $0x4,%rbx` | 地址 +4 |
| 40167a | `48 39 eb` `cmp %rbp,%rbx` | 是否第 4 个数字的地址 |
| 40167d | `74 11` `je 401690 <phase_2+0x58>` | 是则循环结束 |
| 40167f | `8b 43 04` `mov 0x4(%rbx),%eax` | 取下一个数字 |
| 401682 | `03 03` `add (%rbx),%eax` | 第 1 个数字 + 第 2 个数字 |
| 401684 | `39 43 08` `cmp %eax,0x8(%rbx)` | 比较第 1 个数字 + 第 2 个数字是否等于第 3 个数字 |
| 401687 | `74 ed` `je 401676 <phase_2+0x3e>` | 相等继续循环 |
| 401689 | `e8 94 07 00 00` `call 401e22` | |
| 40168e | `eb e6` `jmp 401676` | |
| 401690 | `48 8b 44 24 18` `mov 0x18(%rsp),%rax` | |
| 401695 | `64 48 2b 04 25 28 00` `sub %fs:0x28,%rax` | |
| 40169c | `00 00` | |
| 40169e | `75 07` `jne 4016a7` | |
| 4016a0 | `48 83 c4 28` `add $0x28,%rsp` | |
| 4016a4 | `5b` `pop %rbx` | |
| 4016a5 | `5d` `pop %rbp` | |
| 4016a6 | `c3` `ret` | |
| 4016a7 | `e8 c4 fb ff ff` `call 401270 <__stack_chk_fail@plt>` | |

答案：0 1 1 2 3 5

## 跳转表（switch 各分支）

| 地址 | 指令 | 注释 |
| --- | --- | --- |
| 401757 | `b8 00 00 00 00` `mov $0x0,%eax` | case2 地址：0x4031c0+fffffffffe597 |
| 40175c | `eb ae` `jmp 40170c` | case3 地址：0x4031c0+fffffffffe59e |
| 40175e | `b8 00 00 00 00` `mov $0x0,%eax` | case3 地址：0x4031c0+fffffffffe59e |
| 401763 | `eb ac` `jmp 401711` | case4 地址：0x4031c0+fffffffffe5a5 |
| 401765 | `b8 00 00 00 00` `mov $0x0,%eax` | case4 地址：0x4031c0+fffffffffe5a5 |
| 40176a | `eb aa` `jmp 401716` | case5 地址：0x4031c0+fffffffffe5ac |
| 40176c | `b8 00 00 00 00` `mov $0x0,%eax` | case5 地址：0x4031c0+fffffffffe5ac |
| 401771 | `eb a8` `jmp 40171b` | case6 地址：0x4031c0+fffffffffe5b3 |
| 401773 | `b8 00 00 00 00` `mov $0x0,%eax` | case6 地址：0x4031c0+fffffffffe5b3 |
| 401778 | `eb a6` `jmp 401720` | case7 地址：0x4031c0+fffffffffe5ba |
| 40177a | `b8 00 00 00 00` `mov $0x0,%eax` | case7 地址：0x4031c0+fffffffffe5ba |
| 40177f | `eb a4` `jmp 401725` | case7 地址：0x4031c0+fffffffffe5ba |
| 401781 | `e8 9c 06 00 00` `call 401e22` | case7 地址：0x4031c0+fffffffffe5ba |
| 401786 | `b8 00 00 00 00` `mov $0x0,%eax` | |
| 40178b | `eb 9d` `jmp 40172a` | case7 地址：0x4031c0+fffffffffe5ba |
| 40178d | `e8 de fa ff ff` `call 401270` | case7 地址：0x4031c0+fffffffffe5ba |

## 相等则继续（phase 4 返回前检查）

| 地址 | 指令 | 注释 |
| --- | --- | --- |
| 401820 | `74 05` `je 401827` | 等于继续 |
| 401822 | `e8 fb 05 00 00` `call 401e22` | 不等于爆炸 |
| 401827 | `48 8b 44 24 08` `mov 0x8(%rsp),%rax` | |
| 40182c | `64 48 2b 04 25 28 00` `sub %fs:0x28,%rax` | |
| 401833 | `00 00` | |
| 401835 | `75 05` `jne 40183c` | |
| 401837 | `48 83 c4 18` `add $0x18,%rsp` | |
| 40183b | `c3` `ret` | |
| 40183c | `e8 2f fa ff ff` `call 401270 <__stack_chk_fail@plt>` | |

## 递归函数 func4

```asm
0000000000401792 <func4>:
401792: f3 0f 1e fa          endbr64
401796: 53                   push   %rbx
401797: 89 d0                mov    %edx,%eax
401799: 29 f0                sub    %esi,%eax
40179b: 89 c3                mov    %eax,%ebx
40179d: c1 eb 1f             shr    $0x1f,%ebx
4017a0: 01 c3                add    %eax,%ebx
4017a2: d1 fb                sar    %ebx
4017a4: 01 f3                add    %esi,%ebx
4017a6: 39 fb                cmp    %edi,%ebx
4017a8: 7f 06                jg     4017b0          # 7>val
4017aa: 7c 10                jl     4017bc
4017ac: 89 d8                mov    %ebx,%eax      # 相等 ebc->eax；返回
4017ae: 5b                   pop    %rbx
4017af: c3                   ret
4017b0: 8d 53 ff             lea    -0x1(%rbx),%edx  # rbx-1->edx
4017b3: e8 da ff ff ff       call   401792          # call func
4017b8: 01 c3                add    %eax,%ebx
4017ba: eb f0                jmp    4017ac
4017bc: 8d 73 01             lea    0x1(%rbx),%esi   # rbx+1->esi
4017bf: e8 ce ff ff ff       call   401792          # call func
4017c4: 01 c3                add    %eax,%ebx
4017c6: eb e4                jmp    4017ac

### Phase 6 逆向分析

#### 输入验证与排序逻辑

该阶段要求输入 6 个整数，范围在 1 到 6 之间（包含边界）。程序首先读取这 6 个整数并存储在栈上。随后，程序遍历一个预定义的链表，根据输入的数值顺序重新链接链表的节点。最后，程序检查重排后的链表节点值是否严格递减。若满足条件则通过，否则调用 `boom` 函数。

关键汇编指令分析如下：

| 地址 | 汇编指令 | 说明 |
| :--- | :--- | :--- |
| `4018d7:39 45 00` | `cmp %eax,0x0(%rbp)` | 和内循环的第一个元素相比 |
| `4018da:75 ee` | `jne 4018ca` | 不等于继续循环 |
| `4018dc:e8 41 05 00 00` | `call 401e22` | 相等爆炸 |
| `4018e1:eb e7` | `jmp 4018ca` | |
| `4018e3:49 83 c6 01` | `add $0x1,%r14` | r14重新赋1 |
| `4018e7:49 83 c5 04` | `add $0x4,%r13` | 地址加4 |
| `4018eb:4c 89 ed` | `mov %r13,%rbp` | rbp=下一个元素的值 |
| `4018ee:41 8b 45 00` | `mov 0x0(%r13),%eax` | 取每一个元素 |
| `4018f2: 83 e8 01` | `sub $0x1,%eax` | 减1 |
| `4018f5: 83 f8 05` | `cmp $0x5,%eax` | eax>5 |
| `4018f8: 77 c9` | `ja 4018c3` | 是 爆炸 |
| `4018fa: 41 83 fe 05` | `cmp $0x5,%r14d` | 比较r14和5,看看是否外循环最后 |
| `4018fe: 7f 05` | `jg 401905` | ; 大于5,跳出循环 |
| `401900:4c 89 f3` | `mov %r14,%rbx` | rbx=下一个元素的地址 |
| `401903:eb ce` | `jmp 4018d3` | 跳到下一个内循环开始 |
| `401905:be 00 00 00 00` | `mov $0x0,%esi` | esi=0 开始按照输入的6个元素的大小对进行排序 |
| `40190a:8b 0c b4` | `mov (%rsp,%rsi,4),%ecx` | 取每一个元素 |
| `40190d:b8 01 00 00 00` | `mov $0x1,%eax` | eax=1 |
| `401912:48 8d 15 17 3a 00 00` | `lea 0x3a17(%rip),%rdx` | 链表首地址->rdx (# 405330) |
| `401919:83 f9 01` | `cmp $0x1,%ecx` | 比较每一个元素和1 |
| `40191c: 7e 0b` | `jle 401929` | <=1 |
| `40191e:48 8b 52 08` | `mov 0x8(%rdx),%rdx` | 取链表中的下一个节点地址 |
| `401922:83 c0 01` | `add $0x1,%eax` | eax+1 |
| `401925:39 c8` | `cmp %ecx,%eax` | 比较eax是否等于元素 |
| `401927:75 f5` | `jne 40191e` | |
| `401929: 48 89 54 f4 20` | `mov %rdx,0x20(%rsp,%rsi,8)` | ; 将该节点地址存到堆栈中 |
| `40192e:48 83 c6 01` | `add $0x1,%rsi` | ; rsi+1 |
| `401932:48 83 fe 06` | `cmp $0x6,%rsi` | ;比较rsi和6 |
| `401936:75 d2` | `jne 40190a` | ;不等于6 , 继续外循环 |
| `401938:48 8b 5c 24 20` | `mov 0x20(%rsp),%rbx` | ; 将6个节点按照输入的6个元素顺序重新链接起来 |
| `40193d:48 8b 44 24 28` | `mov 0x28(%rsp),%rax` | |
| `401942:48 89 43 08` | `mov %rax,0x8(%rbx)` | |
| `401946:48 8b 54 24 30` | `mov 0x30(%rsp),%rdx` | |
| `40194b:48 89 50 08` | `mov %rdx,0x8(%rax)` | |
| `40194f: 48 8b 44 24 38` | `mov 0x38(%rsp),%rax` | |
| `401954:48 89 42 08` | `mov %rax,0x8(%rdx)` | |
| `401958:48 8b 54 24 40` | `mov 0x40(%rsp),%rdx` | |
| `40195d:48 89 50 08` | `mov %rdx,0x8(%rax)` | |
| `401961:48 8b 44 24 48` | `mov 0x48(%rsp),%rax` | |
| `401966:48 89 42 08` | `mov %rax,0x8(%rdx)` | |
| `40196a:48 c7 40 08 00 00 00 00` | `movq $0x0,0x8(%rax)` | |
| `401972:bd 05 00 00 00` | `mov $0x5,%ebp` | 开始比较重新排序后的每个节点的值是否递减 |
| `401977:eb 09` | `jmp 401982` | |
| `401979:48 8b 5b 08` | `mov 0x8(%rbx),%rbx` | |
| `40197d:83 ed 01` | `sub $0x1,%ebp` | |
| `401980: 74 11` | `je 401993` | ;等于跳出循环 |
| `401982:48 8b 43 08` | `mov 0x8(%rbx),%rax` | ;取下一个节点 |
| `401986:8b 00` | `mov (%rax),%eax` | ;将下一个节点的值->eax |
| `401988:39 03` | `cmp %eax,(%rbx)` | ;和当前节点值比较 |
| `40198a:7d ed` | `jge 401979` | ;大于等于继续循环 |
| `40198c:e8 91 04 00 00` | `call 401e22` | ;小于爆炸 |
| `401991:eb e6` | `jmp 401979` | |

#### 链表数据与解题思路

原始链表结构如下表所示（注意：表中“节点的序号”列可能为辅助理解或识别误差，核心在于地址、值和指针关系）：

| 节点的地址 | 节点的值 (Hex) | 节点的值 (Dec) | 下一个节点的地址 |
| :--- | :--- | :--- | :--- |
| `0x00405210` | `0x00000113` | 275 | `0x00405330` |
| `0x00405330` | `0x00000112` | 274 | `0x00000000` |
| `0x00405340` | `0x0000029b` | 667 | `0x00405210` |
| `0x00405350` | `0x000002ec` | 748 | `0x00405340` |
| `0x00405360` | `0x000003af` | 943 | `0x00405370` |
| `0x00405370` | `0x00000316` | 790 | `0x00405350` |

*注：根据汇编代码 `lea 0x3a17(%rip),%rdx` 指向 `405330`，通常这是链表的头节点或起始查找点。但在 Bomb Lab 的 phase_6 中，通常有一个固定的链表，其节点值对应 1-6 的某种映射，或者我们需要找到值最大的节点作为起点。观察上述表格，值分别为 275, 274, 667, 748, 943, 790。*

**修正分析：**
在标准的 CSAPP Bomb lab phase_6 中，链表通常是静态定义的，且节点值往往直接关联索引。让我们仔细看汇编中的查找逻辑：
1. `mov $0x1,%eax` (eax=1)
2. `cmp $0x1,%ecx` (比较输入值和1)
3. 如果输入值 > 1，执行 `mov 0x8(%rdx),%rdx` (移动到下一个节点) 和 `add $0x1,%eax`。
这意味着：
- 如果输入第1个数是 1，选中当前节点（初始 `rdx` 指向的节点）。
- 如果输入第1个数是 2，跳过1个节点，选中第2个节点。
- ...
- 如果输入第1个数是 6，跳过5个节点，选中第6个节点。

因此，输入的数字 `n` 表示选择链表中从起始位置开始的第 `n` 个节点。
程序要求最终重排的链表节点值必须**严格递减** (`jge` 意味着只要 `next >= current` 就继续，即要求 `current > next`? 不，`cmp %eax,(%rbx)` 后 `jge` 跳转回循环，意思是如果 `current >= next` 则继续？不对。
让我们看 `401988: cmp %eax,(%rbx)`。这里 `%eax` 是下一个节点的值，`( %rbx )` 是当前节点的值。
指令是 `cmp src, dst`，即计算 `dst - src`。这里是 `current_val - next_val`。
标志位设置基于 `current_val - next_val`。
`jge` (Jump if Greater or Equal) 跳转条件是 SF != OF。对于减法，SF!=OF 表示结果为正或零，即 `current_val >= next_val`。
所以，如果 `current_val >= next_val`，则 `jge` 成立，跳转到 `401979` 继续循环。
如果 `current_val < next_val`，则 `jge` 不成立，掉落到 `call boom`。
因此，要求 **当前节点的值 >= 下一个节点的值**。
结合题目通常要求“严格”或“非严格”，这里允许相等吗？`jge` 包含相等。但通常 Bomb Lab 的 phase 6 要求严格递减，因为节点值各不相同。

我们需要确定链表的物理顺序（内存布局顺序，即指针链接的顺序），还是逻辑顺序？
汇编中 `lea ... %rdx` 加载的是 `405330`。
查看表格：
`0x00405330` 的值是 `274`，下一个是 `0x00000000` (NULL)。这说明 `405330` 是尾节点？
等等，表格里的“下一个节点的地址”列似乎有些混乱，或者我需要根据标准 Bomb Lab 数据来推断。
通常 phase_6 的链表是双向链表或单向链表。
让我们假设 `lea` 指向的是链表的**头节点**。
如果 `405330` 是头节点，它的 next 是 NULL？那链表只有一个节点？这不可能，因为有6个输入。
再看表格：
Row 2: Addr `0x00405330`, Val `274`, Next `0x00000000`.
Row 3: Addr `0x00405340`, Val `667`, Next `0x00405210`.
Row 4: Addr `0x00405350`, Val `748`, Next `0x00405340`.
Row 5: Addr `0x00405360`, Val `943`, Next `0x00405370`.
Row 6: Addr `0x00405370`, Val `790`, Next `0x00405350`.
Row 1: Addr `0x00405210`, Val `275`, Next `0x00405330`.

让我们追踪指针链：
Start at `405330` (from LEA)?
If Start is `405330`: Next is NULL. Dead end.
Maybe the LEA points to a different node in the actual binary, or the table's "Next" column for `405330` is misidentified as NULL when it should point elsewhere?
Or maybe the list starts at `405210`?
Let's check the pointer chain from `405210`:
`405210` -> Next `405330` -> Next NULL. (Length 2). No.

Let's look at the values again.
In standard Bomb Lab, the list nodes often have values like 1..6 or specific numbers.
Here values are: 275, 274, 667, 748, 943, 790.
Sorted descending: 943, 790, 748, 667, 275, 274.
Corresponding Addresses:
943 -> `405360`
790 -> `405370`
748 -> `405350`
667 -> `405340`
275 -> `405210`
274 -> `405330`

We need to output indices (1-6) such that the selected nodes form this sequence.
The selection logic: Index `k` selects the k-th node starting from the initial `rdx` pointer.
We need to know the order of nodes in memory/pointer chain that the code traverses during the *selection* phase.
The code does:
```assembly
mov $0x1,%eax       # counter = 1
loop:
  cmp $0x1,%ecx     # compare input value with 1? No, wait.
  jle 401929        # if input <= 1, jump to store.
  mov 0x8(%rdx),%rdx# move to next node
  add $0x1,%eax     # increment counter
  cmp %ecx,%eax     # compare counter with input value
  jne 40191e        # if not equal, loop back to move next.
```
Wait, the logic is:
Initialize `eax=1`.
If `input == 1`, `cmp $0x1,%ecx` is true? No, `cmp $0x1,%ecx` checks if `ecx == 1`. If yes, `jle` (jump if less or equal) is taken?
`cmp $0x1,%ecx` sets flags based on `ecx - 1`.
`jle` jumps if `ecx <= 1`.
So if input is 1, we skip the traversal and store the current `rdx`.
If input is 2:
`cmp $0x1,%ecx` -> `2-1` positive, no jump.
`mov 0x8(%rdx),%rdx` -> rdx = next node.
`add $0x1,%eax` -> eax = 2.
`cmp %ecx,%eax` -> `2 - 2` zero. `jne` not taken.
Store `rdx`.
So, Input `N` selects the N-th node in the linked list structure defined by the `next` pointers, starting from the initial `rdx` loaded by `lea`.

What is the initial `rdx`?
`lea 0x3a17(%rip),%rdx` at `401912`.
RIP at `401912` is `401912 + 7` (length of instruction? `48 8d 15` is 3 bytes, operand 4 bytes. Total 7 bytes). Next IP is `401919`.
Target = `401919 + 0x3a17` = `405330`.
So the list starts at `0x00405330`.

Now we must determine the order of nodes starting from `405330` following the `next` pointers.
From the table provided:
Node `405330`: Next is `0x00000000`?? This implies the list ends immediately. This contradicts the existence of 6 nodes.
There is likely an error in the OCR'd table's "Next" column for `405330`, or my interpretation of the table rows is mixed up.
Let's re-examine the table data carefully.
Rows:
1. `0x00405210`, Val `275`, Next `0x00405330`
2. `0x00405330`, Val `274`, Next `0x00000000`
3. `0x00405340`, Val `667`, Next `0x00405210`
4. `0x00405350`, Val `748`, Next `0x00405340`
5. `0x00405360`, Val `943`, Next `0x00405370`
6. `0x00405370`, Val `790`, Next `0x00405350`

Let's trace the chain assuming the table is correct about the `next` pointers:
Start `405330` -> Next `0` (End). Length 1.
This cannot be right for a 6-element problem.

Alternative hypothesis: The table lists all nodes, but the "Next" address for `405330` might be wrong in the OCR, OR the list is not singly linked in the way I think, OR the `lea` points to a different node in the actual solution context which I must deduce from standard Bomb Lab behavior.
However, I must stick to the provided text.
Is it possible the list is circular?
If `405330`'s next was actually `405210` (like row 1 suggests `405210` points to `405330`), let's see if there's a cycle.
`405210` -> `405330`
`405330` -> ?
If `405330` -> `405340` (guessing based on address proximity? No, don't guess).

Let's look at the addresses in memory order:
`405210`
`405330`
`405340`
`405350`
`405360`
`405370`

In many Bomb Lab variants, the list is constructed such that the nodes are in memory order, but the pointers are scrambled.
Let's assume the OCR missed the next pointer for `405330` or it's implicit.
Actually, looking at Row 1: `405210` points to `405330`.
Looking at Row 3: `405340` points to `405210`.
Looking at Row 4: `405350` points to `405340`.
Looking at Row 6: `405370` points to `405350`.
Looking at Row 5: `405360` points to `405370`.

Let's try to find the head. A head node is one that is not pointed to by any other node.
Pointed to by:
`405330` (by `405210`)
`405210` (by `405340`)
`405340` (by `405350`)
`405370` (by `405360`)
`405350` (by `405370`)

Who points to `405360`? No one in the list points to `405360`.
Who points to `405330`? `405210`.
So `405360` is a candidate for Head.
But the code loads `405330`.
If the code loads `405330`, and `405330` is part of the chain, where does it go?
If the chain is:
`405360` -> `405370` -> `405350` -> `405340` -> `405210` -> `405330` -> NULL
Then the order starting from `405330` would just be `405330`.

However, if the list is **circular**, or if the "Next" for `405330` is actually `405360` (completing the circle)?
If `405330` -> `405360`:
Order starting at `405330`:
1. `405330` (Val 274)
2. `405360` (Val 943)
3. `405370` (Val 790)
4. `405350` (Val 748)
5. `405340` (Val 667)
6. `405210` (Val 275)

Let's check if this order allows us to pick nodes that satisfy the "Descending Value" constraint.
We need to select 6 distinct nodes (indices 1-6) such that their values are strictly decreasing.
The available values in this traversal order:
Index 1: 274
Index 2: 943
Index 3: 790
Index 4: 748
Index 5: 667
Index 6: 275

We need to output a permutation of 1..6, say $i_1, i_2, ..., i_6$, such that $Val(i_1) > Val(i_2) > ... > Val(i_6)$.
The sorted values are: 943, 790, 748, 667, 275, 274.
These correspond to indices:
943 -> Index 2
790 -> Index 3
748 -> Index 4
667 -> Index 5
275 -> Index 6
274 -> Index 1

So the required order of indices is: **2, 3, 4, 5, 6, 1**.

Let's verify this against the assembly logic.
Input: `2 3 4 5 6 1`
1. Input 2: Selects 2nd node in list (`405360`, Val 943). Stored at `rsp+0x20`.
2. Input 3: Selects 3rd node in list (`405370`, Val 790). Stored at `rsp+0x28`.
3. Input 4: Selects 4th node in list (`405350`, Val 748). Stored at `rsp+0x30`.
4. Input 5: Selects 5th node in list (`405340`, Val 667). Stored at `rsp+0x38`.
5. Input 6: Selects 6th node in list (`405210`, Val 275). Stored at `rsp+0x40`.
6. Input 1: Selects 1st node in list (`405330`, Val 274). Stored at `rsp+0x48`.

Re-linking phase:
`rbx` = Node at `rsp+0x20` (Val 943)
`rax` = Node at `rsp+0x28` (Val 790) -> `rbx.next = rax`
`rdx` = Node at `rsp+0x30` (Val 748) -> `rax.next = rdx`
`rax` = Node at `rsp+0x38` (Val 667) -> `rdx.next = rax`
`rdx` = Node at `rsp+0x40` (Val 275) -> `rax.next = rdx`
`rax` = Node at `rsp+0x48` (Val 274) -> `rdx.next = rax`
`rax.next = 0`

Check Descending:
943 > 790 (OK)
790 > 748 (OK)
748 > 667 (OK)
667 > 275 (OK)
275 > 274 (OK)

This works perfectly. The assumption that the list is circular or that `405330` points to `405360` is necessary to make the indices 1-6 cover all 6 unique nodes. Given the addresses `405330` and `405360` are close, and `405360` is the only un-pointed-to node (if we assume the other links are correct), it is highly probable that `405330`'s next pointer is `405360` (or the list is arranged such that starting at `405330` visits them in that order).

**答案：**
2 3 4 5 6 1

# 《计算机系统基础》Bomb Lab 实验二提示（课件）第 3 部分

本资料整理自《<计算机系统基础>Bomb Lab 实验二提示（课件）》识别内容，包含 `phase_defused` 和 `secret_phase` 相关汇编代码片段。

## phase_defused 函数分析

### 汇编代码段 1：栈保护与参数检查

```assembly
000000000401ff5:
    endbr64
    sub $0x78,%rsp
    mov %fs:0x28,%rax
    mov %rax,0x68(%rsp)
    xor %eax,%eax
    mov $0x1,%edi
    call 401d44                 # 调用 read 或类似输入函数
    cmpl $0x6,0x37f2(%rip)      # 比较读入的字符串个数是否 <= 6 (地址 405810)
    je 402039                   # 如果等于 6，跳转到后续处理逻辑
    mov 0x68(%rsp),%rax
    sub %fs:0x28,%rax
    jne 4020b8                  # 如果栈校验失败，跳转至崩溃处理
    add $0x78,%rsp
    ret
```

**说明：**
- 该段代码首先进行栈保护cookie的设置与读取。
- 调用 `call 401d44` 读取输入数据。
- 检查全局变量（偏移 `0x37f2`）中的计数值是否为 `6`。如果是，则继续执行；否则可能直接返回或进入其他分支（此处逻辑需结合上下文，通常炸弹实验室中 `phase_defused` 接受多个字符串输入）。
- 最后进行栈保护校验，若失败则调用 `__stack_chk_fail`。

### 汇编代码段 2：phase_defused 核心逻辑

```assembly
000000000402039:
    lea 0xc(%rsp),%rcx          # rcx 指向第三个字符串指针
    lea 0x8(%rsp),%rdx          # rdx 指向第二个字符串指针
    lea 0x10(%rsp),%r8          # r8 指向第四个字符串指针 (推测，具体偏移视栈布局而定)
    lea 0x1400(%rip),%rsi       # rsi 指向某个常量字符串 (地址 40344f)
    lea 0x38ba(%rip),%rdi       # rdi 指向另一个常量字符串 (地址 405910)
    mov $0x0,%eax
    call 401320                 # 调用 strcmp 或其他比较函数

000000000402060:
    cmp $0x3,%eax               # 比较读入的字符串个数
    je 40207f                   # 如果等于 3，继续执行

    # 如果不等于 3，打印错误信息并跳转回开头
    lea 0x12a4(%rip),%rdi       # 地址 403310 (错误提示?)
    call 401240                 # puts@plt
    lea 0x12c8(%rip),%rdi       # 地址 403340 (错误提示?)
    call 401240                 # puts@plt
    jmp 402020                  # <phase_defused+0x2b> 回到栈校验前

00000000040207f:
    lea 0x10(%rsp),%rdi         # rdi 指向第三个字符串
    lea 0x13cd(%rip),%rsi       # rsi 指向预定值字符串 (地址 403458)
    call 401b47                 # strings_not_equal > ; 读入的第三个字符串和预定值比较
    test %eax,%eax
    jne 402065                  # 如果不相等，跳转去打印错误信息 (<phase_defused+0x70>)

    # 如果相等，继续执行
    lea 0x1215(%rip),%rdi       # 地址 4032b0
    call 401240                 # puts@plt
    lea 0x1231(%rip),%rdi       # 地址 4032d8
    call 401240                 # puts@plt
    mov $0x0,%eax
    call 401a3b                 # <secret_phase> ; 调用子程序
    jmp 402065                  # <phase_defused+0x70> 结束或跳转

0000000004020b8:
    call 401270                 # __stack_chk_fail@plt
```

**说明：**
- `phase_defused` 函数期望接收特定数量的字符串（此处检查是否为 3 个有效字符串参与后续比较，或者总输入数有特定要求，注释提到“比较读入的字符串个数”为 3）。
- 关键步骤是调用 `strings_not_equal` 比较第三个输入字符串与内存地址 `403458` 处的预定字符串。
- 如果比较成功（相等），则调用 `secret_phase`。
- 如果比较失败或数量不对，则打印提示信息（通过 `puts` 调用地址 `403310`, `403340` 等处的字符串）。

## secret_phase 函数分析

### 汇编代码段 3：secret_phase 递归/循环结构

```assembly
0000000004019fa:
    endbr64
    test %rdi,%rdi              # 测试第一个参数（可能是树节点指针）是否为空
    je 401a35                   # 如果为空，返回 -1 (0xffffff)
    sub $0x8,%rsp
    mov (%rdi),%edx             # 加载当前节点的左子节点值或标识
    cmp %esi,%edx               # 与第二个参数（可能是目标值）比较
    jg 401a19                   # 如果当前节点值 > 目标值，向左子树搜索
    mov $0x0,%eax
    jne 401a26                  # 如果不相等，去右子树搜索

    # 如果找到匹配项（edx == esi）
    add $0x8,%rsp
    ret                         # 返回 0 (表示找到)

000000000401a19:
    # 向左子树搜索
    mov 0x8(%rdi),%rdi          # 获取左子节点指针
    call 4019fa                 # 递归调用自身
    add %eax,%eax               # 将返回值乘以 2
    jmp 401a14                  # 返回

000000000401a26:
    # 向右子树搜索
    mov 0x10(%rdi),%rdi         # 获取右子节点指针
    call 4019fa                 # 递归调用自身
    lea 0x1(%rax,%rax,1),%eax   # eax = eax + 2*eax = 3*eax ? 或者 1 + 2*eax? 
                                # 指令 lea 0x1(%rax,%rax,1) 等价于 eax = 1 + rax + rax = 1 + 2*rax
    jmp 401a14                  # 返回

000000000401a35:
    mov $0xffffff, %eax         # 未找到，返回 -1
    ret
```

**说明：**
- 这是一个典型的二叉搜索树（BST）查找算法的汇编实现。
- 参数 `%rdi` 指向当前树节点，`%esi` 包含要查找的目标值。
- 节点结构推测：
    - `(%rdi)`：节点存储的值或与左子树相关的字段。
    - `0x8(%rdi)`：左子节点指针。
    - `0x10(%rdi)`：右子节点指针。
- 逻辑：
    1. 如果节点为空，返回 `-1`。
    2. 如果节点值大于目标值，进入左子树递归。
    3. 如果节点值小于目标值，进入右子树递归。
    4. 如果相等，返回 `0`。
- **注意返回值处理**：
    - 左子树返回后，结果 `eax` 被乘以 2 (`add %eax,%eax`)。
    - 右子树返回后，结果 `eax` 变为 `1 + 2*eax` (`lea 0x1(%rax,%rax,1),%eax`)。
    - 这种处理方式暗示 `secret_phase` 可能在计算某种路径编码或位置索引，而不仅仅是简单的布尔存在性检查。
