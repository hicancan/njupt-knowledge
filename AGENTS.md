# njupt-knowledge development rules

- The directory tree is the model: `courses/` (one file per subject, listing the current course codes that teach it), `topics/<subject>/`
  (one file per topic), `materials/<source>/<original course code>/` (one file per source document, figures in a
  sibling `.assets/`). Nothing else holds knowledge.
- Write links in one direction only. A course links its topics; a topic names what it `requires`; a material passage
  links the topics it refers to. Backlinks, counts and statistics are computed by `tools/build.py`, never written.
- Every material keeps `source` pointing at the original file. Additions are labelled: 参考解答 (ours), 订正 (fixing
  the source), 补充 (our note). Never present our answer as the source's.
- A topic note says what a student needs, in the terms NJUPT's course uses (搜索 not 查找, 对半搜索, 二叉搜索树…),
  checked against a worked example; a wrong worked example is worse than none.
- Original acquisition, OCR and historical batch drafting belong upstream in `njupt-knowledge-sources`; this repository
  holds authored knowledge and the small build that produces its index, backlinks and publication. Edit knowledge
  files directly as it evolves; batch processing is not a prerequisite for ongoing editing or product releases.
- Explanations build a reader's cognitive model: start from the problem, facts and constraints, ask focused questions
  where understanding turns, explain the mechanism and limits, compare related ideas, and verify worked examples.
  These are writing principles, not mandatory section headings or a rigid template.
- Course codes and names come from the teaching system; a subject's `codes` must be courses taught now,
  older codes go in `former`.
