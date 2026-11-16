---
name: TCP/IP网络设计与实现（双语）
codes: [JS111602C]
former: [B0301162C]
---

# TCP/IP网络设计与实现（双语）

## Chapter 1 Introduction

- [Net/3 代码的组织层次与体系结构](../topics/TCP-IP网络/net3代码组织层次.md)
- [4.4BSD 网络支持与应用接口概述](../topics/TCP-IP网络/bsd网络支持与应用.md)
- [domaininit 等协议初始化过程](../topics/TCP-IP网络/协议初始化过程.md)
- [主机字节序与网络字节序及其转换](../topics/TCP-IP网络/字节序转换.md)
- [网络接口与地址结构概览](../topics/TCP-IP网络/接口与地址结构概览.md)

## Chapter 2 Mbufs: Memory Buffers

- [mbuf 的用途及基本结构（m_data、m_len 等）](../topics/TCP-IP网络/mbuf用途与结构.md)
- [带簇的 mbuf（M_EXT）包含的内容与使用场景](../topics/TCP-IP网络/带簇的mbuf.md)
- [m_next 与 m_nextpkt 指针的作用与区别](../topics/TCP-IP网络/mbuf链表指针.md)
- [分配 mbuf 的函数（如 m_get、m_gethdr）](../topics/TCP-IP网络/mbuf分配函数.md)
- [宏 mtod 和 dtom 的作用](../topics/TCP-IP网络/mtod与dtom宏.md)
- [收到以太网帧时设备驱动程序调用的函数及 m_devget 何时使用簇](../topics/TCP-IP网络/以太网帧接收处理.md)
- [第一个 mbuf 中数据量小于最小协议首部时的拉齐（pullup）调用](../topics/TCP-IP网络/首部拉齐机制.md)

## Chapter 3 Interface Layer

- [接口层 ifnet 结构体的作用与字段](../topics/TCP-IP网络/ifnet结构.md)
- [接口的输出队列与发送调度机制](../topics/TCP-IP网络/接口输出队列.md)
- [接口层的输入处理流程与层间通信队列](../topics/TCP-IP网络/接口输入处理.md)
- [接口的地址链表管理](../topics/TCP-IP网络/接口地址链表.md)

## Chapter 4 Interfaces: Ethernet

- [以太网帧格式与首部解析](../topics/TCP-IP网络/以太网帧格式.md)
- [CSMA/CD 介质访问控制机制](../topics/TCP-IP网络/csma_cd机制.md)
- [以太网的输入输出过程详解](../topics/TCP-IP网络/以太网输入输出.md)
- [ARP 协议在以太网接口中的地址解析作用](../topics/TCP-IP网络/arp与以太网寻址.md)

## Chapter 6 IP Addressing

- [IP 地址分类（A/B/C/D/E 类）与子网掩码](../topics/TCP-IP网络/ip地址分类.md)
- [子网划分与 CIDR 无类别域间路由](../topics/TCP-IP网络/子网划分与cidr.md)
- [特殊 IP 地址（广播、组播、环回、全零）及无 IP 地址时的广播包处理](../topics/TCP-IP网络/特殊ip地址.md)
- [IPv4 地址结构 sockaddr_in](../topics/TCP-IP网络/sockaddr_in结构.md)

## Chapter 7 Domains and Protocols

- [Net/3 域（domain）与协议族常量的定义](../topics/TCP-IP网络/域与协议族常量.md)
- [protosw 结构的分配、初始化及 inetsw 数组中的多个条目](../topics/TCP-IP网络/protosw结构.md)
- [pffindproto 和 pffindtype 函数的功能、调用示例及返回值说明](../topics/TCP-IP网络/pffindproto与pffindtype.md)
- [ip_init 初始化内容与 ip_protox 数组的作用](../topics/TCP-IP网络/ip_init初始化.md)

## Chapter 8 IP: Internet Protocol

- [IP 头部长度、字段解析与校验和错误处理](../topics/TCP-IP网络/ip头部格式.md)
- [路由器转发逻辑与 ip_forward 中的字节序转换](../topics/TCP-IP网络/ip转发逻辑.md)
- [源地址选择规则与多宿主主机源地址](../topics/TCP-IP网络/源地址选择.md)
- [TTL 递减时机与路由环路检测](../topics/TCP-IP网络/ttl递减.md)
- [IP 重定向的产生条件与 ICMP 重定向报文发送](../topics/TCP-IP网络/ip重定向.md)

## Chapter 9 IP Forwarding and Routing

- [路由表的数据结构与查找算法](../topics/TCP-IP网络/路由表结构.md)
- [IP 路由查询过程与最长前缀匹配](../topics/TCP-IP网络/路由查询过程.md)
- [路由条目的动态添加、删除与更新](../topics/TCP-IP网络/路由添加与删除.md)

## Chapter 10 IP Fragmentation and Reassembly

- [IP 分片的触发条件与 MTU 限制](../topics/TCP-IP网络/分片触发条件.md)
- [如何确定每个片段中的数据字节数（分片偏移计算）](../topics/TCP-IP网络/片段大小确定.md)
- [为何只有目的主机能重组原始数据报及重组函数实现](../topics/TCP-IP网络/目的主机重组.md)
- [IP 分片处理过程中可能遇到的错误或异常及发送的 ICMP 差错报文](../topics/TCP-IP网络/分片异常与icmp差错.md)

## Chapter 11 ICMP: Internet Control Message Protocol

- [ICMP 报文类型（差错报告与查询报文）概览](../topics/TCP-IP网络/icmp报文类型.md)
- [icmp_input 函数处理流程及过时 Information Request 传递给 rip_input 的原因](../topics/TCP-IP网络/icmp_input处理.md)
- [IP 差错与 ICMP 差错报文汇总（不可达、超时、参数问题等）](../topics/TCP-IP网络/icmp差错报文汇总.md)
- [ICMP 差错报文引用 IP 首部时的字节序](../topics/TCP-IP网络/icmp字节序细节.md)
- [为什么在特定代码路径中丢弃 ip_output 的返回值](../topics/TCP-IP网络/ip_output返回值丢弃.md)

## Chapter 22 Network Input and Output

- [网络输入和输出时层间通信用哪些队列](../topics/TCP-IP网络/网络io层间通信队列.md)
- [IP 输入（ip_input）在 4.4BSD-Lite 发行版中的处理流程](../topics/TCP-IP网络/ip输入处理.md)
- [UDP 输入（udp_input）在 4.4BSD-Lite 发行版中的处理流程](../topics/TCP-IP网络/udp输入处理.md)
- [阻塞在 recvfrom 调用中的进程存放在套接字结构的何处以便被通知](../topics/TCP-IP网络/socket阻塞通知机制.md)
- [例子程序从未为应用指定本地端口号时的自动分配机制](../topics/TCP-IP网络/应用本地端口号分配.md)

