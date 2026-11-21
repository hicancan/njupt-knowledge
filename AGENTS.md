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
- Exploit the full native rendering arsenal of `docstream` (`hicancan/docstream`) and co-evolve it when needed:
  every document is parsed and rendered natively across Web, Android, and Windows by `docstream`, so explanations
  should actively use its rich visual and typographic primitives rather than plain text walls:
  - **11 native Mermaid diagram engines (`docstream-diagram`)**: `flowchart` (with nested `subgraph` boxes, `<br>`,
    `<b>`), `stateDiagram-v2` (composite states, transitions, protocols, sequential logic), `sequenceDiagram`
    (`note`, `loop`, `alt`, `opt`, `par`), `xychart-beta` (axes, bars, and curves for signal responses, asymptotic
    trends, probability/Monte Carlo curves), `quadrantChart` (2×2 orthogonal concept comparisons), `mindmap`,
    `classDiagram`, `erDiagram` (compartments, multiplicities, UML/crow's-foot markers), `timeline`, `gantt`, `pie`.
    Every Mermaid block must return a valid layout from `docstream.diagram(source)`.
  - **Rich block & inline semantics (`docstream-core`)**: GitHub alerts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`,
    `> [!WARNING]`, `> [!CAUTION]`) for misconception vaccines, boundary traps, and metacognitive triggers; Typora
    `==highlight==` for key problem-solving cues, `^sup^`, `~sub^`, `<kbd>`; Markdown tables and HTML `<table>` with
    `rowspan`/`colspan` (whose cell contents are parsed as full Markdown and TeX) for multi-dimensional comparisons.
  - **Native TeX math (`docstream-math`)**: every formula must pass `docstream.unknown(tex)` with zero unknown TeX
    commands. If a subject needs a general TeX macro, diagram capability, or layout primitive that `docstream` lacks,
    evolve `hicancan/docstream` cleanly rather than degrading the explanation.
