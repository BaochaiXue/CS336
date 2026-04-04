# Style Guide

## LaTeX Conventions

### Document Structure
- Engine: **LuaLaTeX** (via `lualatex` command)
- Document class: `book`
- Chapters use `\include{chapters/chXX_name}` (enables `\includeonly`)
- Sections: `\section`, `\subsection`, `\subsubsection` — no deeper nesting
- Label convention: `\label{ch:XX:sec:name}` for sections, `\label{eq:XX:name}` for equations, `\label{fig:XX:name}` for figures, `\label{tab:XX:name}` for tables

### Packages (Core)
```latex
\usepackage{amsmath, amssymb, amsthm}    % Math
\usepackage{fontspec}                      % Fonts (LuaLaTeX)
\usepackage{microtype}                     % Typography
\usepackage{graphicx}                      % Figures
\usepackage{booktabs}                      % Tables
\usepackage{algorithm2e}                   % Algorithms
\usepackage{listings}                      % Code listings
\usepackage[backend=biber]{biblatex}       % Bibliography
\usepackage{hyperref}                      % Cross-references
\usepackage{cleveref}                      % Smart refs (\cref)
\usepackage{tcolorbox}                     % Colored boxes (analogies, capsules)
\usepackage{tikz}                          % Diagrams
```

### Custom Environments
```latex
% Neuroscience analogy box
\begin{analogybox}{Title}
  \paragraph{Where the analogy helps.} ...
  \paragraph{Where the analogy breaks.} ...
  \paragraph{What intuition to keep.} ...
\end{analogybox}

% Prerequisite capsule
\begin{prereqcapsule}{Topic}
  ...
\end{prereqcapsule}

% 2026 update card
\begin{updatecard}{Topic}
  ...
\end{updatecard}

% Key definition
\begin{definition}{Name}\label{def:...}
  ...
\end{definition}

% Key theorem/proposition
\begin{proposition}{Name}\label{prop:...}
  ...
\end{proposition}
```

### Cross-References
- Always use `\cref{}` (cleveref) instead of raw `\ref{}`
- Equations: `\cref{eq:01:cross_entropy}` → "Equation 1.3"
- Figures: `\cref{fig:09:attention_matrix}` → "Figure 9.2"
- Use `\Cref{}` at sentence start

## Prose Rules

### Voice and Tone
- **Active voice preferred**: "We compute the gradient" not "The gradient is computed"
- **First-person plural**: "we" (author + reader working together)
- **Present tense for math**: "The loss function measures..." not "The loss function will measure..."
- **Direct address sparingly**: "you" only in exercises and reader-directed asides

### Equation Prose
Every displayed equation must have:
1. **Introduction sentence** before the equation (what it computes and why)
2. **Symbol table** after the equation (if new symbols appear)
3. **Interpretation sentence** after the equation (what it means in words)

Example:
> The cross-entropy loss measures how well our model's predicted distribution matches the true distribution:
> $$H(p, q) = -\sum_{x} p(x) \log q(x)$$
> where $p$ is the true distribution, $q$ is the model's predicted distribution, and the sum is over all possible tokens $x$. Intuitively, this penalizes the model more when it assigns low probability to tokens that actually appear.

### Paragraph Structure
- Topic sentence first
- One idea per paragraph
- Maximum ~8 sentences per paragraph
- Transition words between paragraphs

### Technical Terms
- **Bold** on first definition: "The **attention mechanism** computes..."
- After first definition, use normal font
- Avoid jargon without definition

## Figure Standards

- All figures in `book/figures/`
- File naming: `chXX_descriptive_name.pdf` (vector) or `.png` (raster, 300dpi+)
- Every figure has a descriptive caption (complete sentence)
- Every figure is referenced in the text with `\cref{fig:...}`
- Prefer vector graphics (TikZ, PDF) over raster

## Table Standards

- Use `booktabs` package (no vertical lines, `\toprule`, `\midrule`, `\bottomrule`)
- Every table has a descriptive caption
- Number formatting: use `siunitx` for aligned decimals
- Column headers are bold or small caps

## Citation Style

- Use `\textcite{}` for narrative citations: "Vaswani et al. (2017) introduced..."
- Use `\parencite{}` for parenthetical: "...self-attention mechanism \parencite{vaswani2017}"
- BibTeX keys follow pattern: `author_year` or `short_name_year`
- Prefer primary sources over secondary summaries

## Code Listing Style

- Language: Python (default), CUDA C, Triton
- Use `listings` or `minted` package
- Syntax highlighting with consistent color scheme
- Maximum 40 lines per listing; longer code goes to appendix
- Every listing has a caption and is referenced in text
