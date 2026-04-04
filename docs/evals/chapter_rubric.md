# Chapter Evaluation Rubric

## Compilation (Pass/Fail)
- [ ] Chapter compiles with `lualatex` without errors
- [ ] No undefined references
- [ ] No missing citations
- [ ] No overfull hbox warnings > 10pt

## Structure Completeness (Pass/Fail)
- [ ] Learning goals section present (3–5 objectives)
- [ ] Big picture section present
- [ ] Formal setup and notation section present
- [ ] Main ideas sections present
- [ ] At least one worked example
- [ ] Systems/implementation consequences section present
- [ ] At least one neuroscience analogy box
- [ ] Common misconceptions section present (3–5 items)
- [ ] Exercises present in all four tiers (warmup, derivation, implementation, open-ended)
- [ ] Further reading section present (3–5 annotated refs)

## Mathematical Rigor (Scored 1–5)
- Every definition is precise and uses correct notation
- Every assumption is explicitly stated
- Every major equation has: intro sentence + symbol table + interpretation
- Derivations show intermediate steps
- Proofs are complete (or clearly marked "proof sketch" with appendix reference)

## Pedagogical Quality (Scored 1–5)
- Concepts build incrementally (simple → complex)
- Worked examples use realistic numbers
- Misconceptions section addresses genuine student confusions
- Exercises are progressive in difficulty
- Transitions between sections are smooth

## Notation Consistency (Pass/Fail)
- [ ] All symbols match `docs/notation.md`
- [ ] No conflicting symbol usage
- [ ] Custom commands used where defined
- [ ] Dimensions (T, V, d, n_h, L) used consistently

## Citation Completeness (Pass/Fail)
- [ ] Every nontrivial claim has a citation
- [ ] Citations use correct BibTeX keys
- [ ] Primary sources preferred over secondary
- [ ] All cited works appear in bibliography.bib

## Neuroscience Analogy Compliance (Pass/Fail)
- [ ] Every analogy box has three sections: helps / breaks / keep
- [ ] Anti-patterns avoided (no "thinks", no "works like brains", no implied consciousness)
- [ ] Analogy sources from approved domain list
- [ ] Maximum 3 analogy boxes per chapter

## CS336 Coverage (Pass/Fail)
- [ ] Chapter covers all topics assigned to it in the coverage matrix
- [ ] Assignment connection is explicit where applicable
- [ ] No coverage gaps for assigned lecture material
