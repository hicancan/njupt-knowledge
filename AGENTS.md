# njupt-knowledge development rules

- The directory tree is the model: `courses/` (one file per course, named by its current code), `topics/<subject>/`
  (one file per topic), `materials/<source>/<original course code>/` (one file per source document, figures in a
  sibling `.assets/`). Nothing else holds knowledge.
- Write links in one direction only. A course links its topics; a topic names what it `requires`; a question's
  `知识点：` line links what it tests. Backlinks, counts and statistics are computed by `tools/build.py`, never written.
- Every material keeps `source` pointing at the original file. Additions are labelled: 参考解答 (ours), 订正 (fixing
  the source), 补充 (our note). Never present our answer as the source's.
- A topic note says what a student needs, in the terms NJUPT's course uses (搜索 not 查找, 对半搜索, 二叉搜索树…),
  checked against a worked example; a wrong worked example is worse than none.
- Parse with MinerU only as a draft. Word documents go through PDF first so their drawings survive.
- Course codes and names come from the teaching system; a course file's `code` must be a code that is taught now,
  older codes go in `former`.
