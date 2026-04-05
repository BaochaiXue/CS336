# Evaluation Checklists

## Coverage Completeness Checklist

For each chapter, verify:
- [ ] All topics assigned in `docs/course_coverage_matrix.md` are addressed
- [ ] All relevant CS336 assignment connections are mentioned
- [ ] No coverage matrix topic is completely absent
- [ ] 2026 Update Cards present where applicable

## Notation Consistency Checklist

- [ ] All vectors use `\mathbf{}` (bold lowercase)
- [ ] All matrices use `\mathbf{}` (bold uppercase)  
- [ ] Dimensions: $T$ = sequence length, $V$ = vocabulary, $d$ = model dim, $h$ = heads, $L$ = layers
- [ ] All custom commands from textbook.tex preamble are used consistently
- [ ] No symbol collisions between chapters
- [ ] `\softmax`, `\ReLU`, `\GeLU` etc. use DeclareMathOperator forms

## Citation Completeness Checklist

- [ ] Every nontrivial claim has `\cite{}` or `\textcite{}`
- [ ] All cited keys exist in `bibliography.bib`
- [ ] Primary sources preferred over secondary
- [ ] No unresolvable citation warnings in build log
- [ ] At least 3 references in "Further Reading" per chapter

## Pedagogy Compliance Checklist

- [ ] Learning goals section: 3–5 measurable objectives
- [ ] Big picture section: 1–2 pages, no formulas
- [ ] Formal setup: all new notation defined
- [ ] At least one worked example with realistic numbers
- [ ] Systems consequences section present
- [ ] Common misconceptions: 3–5 items
- [ ] Exercises in all four tiers (warmup, derivation, implementation, open-ended)
- [ ] Further reading: 3–5 annotated references

## Neuroscience Analogy Compliance Checklist

- [ ] At least one analogy box per chapter
- [ ] Maximum three analogy boxes per chapter
- [ ] Each box has three sections: helps / breaks / keep
- [ ] No "thinks", "understands", "works like brains"
- [ ] Analogy source from approved domain list
- [ ] Biological claims are well-established
- [ ] Differences section is substantive (not token)
