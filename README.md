# njupt-knowledge

南京邮电大学的课程知识：把散落的往年试卷、复习资料清洗成 Markdown，按知识点组织起来。

```text
courses/<课程代码>.md          一门课的知识目录：按讲授顺序的章节，每章链接若干知识点
topics/<学科>/<知识点>.md      一个知识点；requires 写它依赖的知识点
materials/<来源>/<原课程代码>/  一份资料整理成的 Markdown，图片放在同名 .assets/ 里
tools/                         构建与资料解析
```

- **树加双链**：课程目录是树，知识点之间的 requires 和资料里的“知识点”链接把树连成图。只写正向链接；每个知识点被哪些课程讲、被哪些题考、又支撑哪些知识点，由构建算出来。
- **原件可追溯**：每份资料的 `source` 指向原文件。原件不放进这里；“参考解答”“订正”“补充”标明是整理时加的。
- **课程身份用课程代码**：文件名是现行代码，`former` 记以前的代码，所以课程改号后往年资料仍然挂在同一门课上。

## 构建

```sh
python3 tools/build.py      # 检查所有链接，生成 build/knowledge.json 和文档
```

发布出去的文档去掉了 front matter，链接和图片都改写成从仓库根开始的路径（如 `topics/数据结构/堆栈.md`、`materials/…#选择-2`），各端用同一种方式解析。每次合入 main 都会构建并发布一个 `knowledge-YYYYMMDD-HHMM` Release。

## 资料解析

扫描件、Word、PPT 先转成 PDF（Word 文档里的绘图只有渲染成 PDF 才不会丢），再用 MinerU 云端接口批量解析：

```sh
MINERU_TOKEN=... python3 tools/mineru.py <源文件目录> <输出目录>
```

解析结果只是草稿：逐题核对文字、公式、图和答案，再按上面的格式写进 `materials/`。

## 投稿

欢迎通过 Pull Request 补充资料、订正答案、完善知识点。一份资料一个文件，每道题一个标题，题后写“知识点：”并链接到 `topics/` 里的知识点。

资料原件来自各自的来源，版权归原作者；整理内容以 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans) 共享。
