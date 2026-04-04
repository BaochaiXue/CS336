# Neuroscience Analogy Policy

## Purpose

Analogies from neuroscience and brain science provide students with concrete, intuitive hooks for understanding abstract ML concepts. However, all analogies are imperfect. This policy ensures we use them honestly and effectively.

## The Three-Section Format

Every neuroscience analogy box must contain exactly three sections:

### 1. Where the Analogy Helps
- What structural or functional similarity exists?
- Why is this analogy useful for building intuition?
- What prediction or expectation does the analogy correctly set up?

### 2. Where the Analogy Breaks
- What key differences exist between the biological and artificial systems?
- What would be misleading if taken literally?
- What biological details have no counterpart in the artificial system (and vice versa)?

### 3. What Intuition to Keep
- One or two sentences summarizing the useful takeaway
- A clear statement of what the student should remember from this analogy
- Framed as: "Think of X as Y, but remember that Z"

## LaTeX Environment

```latex
\begin{analogybox}{Title: Brain Concept → ML Concept}
  \paragraph{Where the analogy helps.}
  Text explaining the similarity...

  \paragraph{Where the analogy breaks.}
  Text explaining the differences...

  \paragraph{What intuition to keep.}
  Text summarizing the takeaway...
\end{analogybox}
```

## Approved Analogy Domains

The following neuroscience topics are approved as analogy sources. Each is well-established science and maps to specific ML concepts:

| Brain Concept | ML Concept | Chapter(s) |
|--------------|------------|------------|
| Neurons and synapses | Artificial neurons and weights | Ch 8 |
| Hebbian learning ("fire together, wire together") | Gradient descent / weight updates | Ch 8, 12 |
| Cortical columns and hierarchical processing | Transformer layers | Ch 10 |
| Selective attention (cocktail party effect) | Attention mechanism | Ch 9 |
| Working memory (prefrontal cortex) | KV cache / context window | Ch 18 |
| Predictive coding | Next-token prediction | Ch 6 |
| Neural population coding | Embedding vectors | Ch 8 |
| Sparse coding in visual cortex | Mixture of Experts routing | Ch 13 |
| Brain energy efficiency | MFU and compute efficiency | Ch 14–15 |
| Myelination and axon diameter | Bandwidth and latency in memory hierarchy | Ch 15 |
| Sleep / memory consolidation | Training data replay / deduplication | Ch 22–23 |
| Reward prediction error (dopamine) | Reward signal in RLHF | Ch 25 |
| Dual process theory (System 1 / System 2) | Fast inference vs. chain-of-thought reasoning | Ch 18, 25 |

## Anti-Patterns (Things to Avoid)

1. **"The model thinks..."** — LLMs do not think. Use "the model computes" or "the model predicts."
2. **"Neural networks work like brains"** — They share loose structural analogies but differ in mechanism, scale, learning rules, energy, and substrate.
3. **Implying consciousness or understanding** — Stay descriptive: "the model produces output that..." not "the model understands that..."
4. **Unsourced neuroscience claims** — All brain science facts should be well-established. Cite a neuroscience textbook if making a specific biological claim.
5. **Over-extending analogies** — One analogy per box. Don't chain multiple brain metaphors into an extended narrative.

## Frequency

- **Minimum**: One analogy box per chapter
- **Maximum**: Three analogy boxes per chapter (more dilutes their impact)
- **Placement**: After the main conceptual introduction of the topic being analogized, before worked examples
