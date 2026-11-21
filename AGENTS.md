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
- Explanations are judged solely by whether they form a coherent knowledge system and make every concept and worked
  example genuinely transparent: derive the generative motivation from the real problem, base facts, and physical or
  engineering constraints (first-principles reasoning—why simpler designs fail); ask focused Socratic questions at
  conceptual turning points; test invariants and failure boundaries by varying conditions (variation theory); contrast
  competing concepts along orthogonal dimensions and map structural isomorphisms across subjects; translate fluently
  between formal symbols, physical/engineering intuition, diagrams, and concrete exam examples; make metacognitive
  problem-solving triggers explicit in worked examples and proofs (Polya heuristics—what cue in the problem signals
  which tool and why); and inoculate against common misconceptions with minimal counterexamples. These are internal
  cognitive operators to be woven naturally into prose as needed—never force terms like "First Principles", "Socratic
  Question", or "Metacognition" into rigid section headings or boilerplate templates.
- Course codes and names come from the teaching system; a subject's `codes` must be courses taught now,
  older codes go in `former`.
