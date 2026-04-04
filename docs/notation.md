# Notation — Master Symbol Table

This is the canonical notation reference for the entire textbook. All chapters must use these symbols consistently.

## Scalars, Vectors, Matrices, Tensors

| Symbol | Meaning | Convention |
|--------|---------|------------|
| $x, y, z$ | Scalars | Lowercase italic |
| $\mathbf{x}, \mathbf{y}, \mathbf{z}$ | Vectors (column by default) | Lowercase bold |
| $\mathbf{W}, \mathbf{K}, \mathbf{Q}, \mathbf{V}$ | Matrices | Uppercase bold |
| $\mathcal{X}, \mathcal{V}$ | Sets | Calligraphic uppercase |
| $\mathbb{R}, \mathbb{Z}, \mathbb{N}$ | Number sets | Blackboard bold |
| $\boldsymbol{\theta}$ | Parameter vector | Bold Greek |

## Indexing

| Symbol | Meaning |
|--------|---------|
| $x_i$ | $i$-th element of vector $\mathbf{x}$ |
| $W_{ij}$ | Element at row $i$, column $j$ of matrix $\mathbf{W}$ |
| $x_t$ or $x^{(t)}$ | Element at time step $t$ (context determines sequence index) |
| $x^{(i)}$ | $i$-th training example |
| $\mathbf{x}_{1:T}$ | Sequence $(x_1, x_2, \ldots, x_T)$ |

## Dimensions

| Symbol | Meaning | Typical Range |
|--------|---------|---------------|
| $T$ | Sequence length (context window) | 512–131072 |
| $V$ | Vocabulary size | 32000–128000 |
| $d$ or $d_{\text{model}}$ | Model / embedding dimension | 512–8192 |
| $d_k$ | Key/query dimension per head | $d / n_h$ |
| $d_v$ | Value dimension per head | $d / n_h$ |
| $d_{\text{ff}}$ | Feed-forward hidden dimension | $\frac{8}{3}d$ (SwiGLU) or $4d$ (ReLU) |
| $n_h$ | Number of attention heads | 8–128 |
| $n_{\text{kv}}$ | Number of key-value heads (GQA) | 1–$n_h$ |
| $L$ | Number of Transformer layers | 12–126 |
| $N$ | Number of parameters | — |
| $D$ | Dataset size (in tokens) | — |
| $B$ | Batch size | — |

## Probability and Information Theory

| Symbol | Meaning |
|--------|---------|
| $p(x)$ | True / empirical distribution |
| $q(x)$ or $p_\theta(x)$ | Model distribution (parameterized by $\theta$) |
| $H(p)$ | Entropy of distribution $p$ |
| $H(p, q)$ | Cross-entropy between $p$ and $q$ |
| $D_{\text{KL}}(p \| q)$ | KL divergence from $p$ to $q$ |
| $\text{PPL}$ | Perplexity |
| $\mathcal{L}(\theta)$ | Loss function |
| $\mathbb{E}[\cdot]$ | Expectation |
| $\log$ | Natural logarithm ($\ln$) unless stated otherwise |
| $\log_2$ | Logarithm base 2 (information-theoretic context) |

## Transformer Specific

| Symbol | Meaning |
|--------|---------|
| $\mathbf{Q}, \mathbf{K}, \mathbf{V}$ | Query, Key, Value matrices (or per-head slices) |
| $\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V$ | Query, Key, Value projection weight matrices |
| $\mathbf{W}_O$ | Output projection matrix |
| $\text{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V})$ | Attention function |
| $\text{softmax}(\cdot)$ | Row-wise softmax |
| $\text{FFN}(\mathbf{x})$ | Feed-forward network |
| $\text{LN}(\mathbf{x})$ | Layer normalization |
| $\text{RMSNorm}(\mathbf{x})$ | RMS normalization |
| $\sigma(\cdot)$ | Activation function (context-specific: ReLU, GeLU, SiLU/Swish) |
| $\text{RoPE}(x, m)$ | Rotary positional encoding at position $m$ |

## Optimization

| Symbol | Meaning |
|--------|---------|
| $\eta$ or $\alpha$ | Learning rate |
| $\beta_1, \beta_2$ | Adam momentum coefficients |
| $\epsilon$ | Small constant for numerical stability |
| $\lambda$ | Weight decay coefficient |
| $\nabla_\theta \mathcal{L}$ | Gradient of loss w.r.t. parameters |
| $\mathbf{m}_t$ | First moment estimate (Adam) |
| $\mathbf{v}_t$ | Second moment estimate (Adam) |

## Systems

| Symbol | Meaning |
|--------|---------|
| $C$ | Compute budget (in FLOPs) |
| $F$ | Floating-point operations per token |
| $\text{MFU}$ | Model FLOPs Utilization |
| $\text{HBM}$ | High-bandwidth memory |
| $\text{SRAM}$ | On-chip static memory |
| $\text{AI}$ | Arithmetic intensity (FLOPs/byte) |

## Scaling Laws

| Symbol | Meaning |
|--------|---------|
| $L(N, D)$ | Loss as function of parameters $N$ and data $D$ |
| $L(C)$ | Loss as function of compute $C$ |
| $\alpha, \beta$ | Scaling exponents |
| $A, B, E$ | Scaling law coefficients |
| $N^*(C)$ | Compute-optimal model size |
| $D^*(C)$ | Compute-optimal dataset size |

## Alignment and RL

| Symbol | Meaning |
|--------|---------|
| $\pi_\theta$ | Policy (language model parameterized by $\theta$) |
| $\pi_{\text{ref}}$ | Reference policy |
| $r(x, y)$ | Reward function |
| $r_\phi$ | Learned reward model |
| $\mathcal{D}_{\text{pref}}$ | Preference dataset |
| $y_w, y_l$ | Preferred (winning) and dispreferred (losing) completions |
| $J(\theta)$ | RL objective |
| $\hat{A}_t$ | Advantage estimate |

## LaTeX Commands (Custom)

```latex
% Vectors and matrices
\newcommand{\vx}{\mathbf{x}}
\newcommand{\vy}{\mathbf{y}}
\newcommand{\vz}{\mathbf{z}}
\newcommand{\vW}{\mathbf{W}}
\newcommand{\vQ}{\mathbf{Q}}
\newcommand{\vK}{\mathbf{K}}
\newcommand{\vV}{\mathbf{V}}
\newcommand{\vtheta}{\boldsymbol{\theta}}

% Operators
\DeclareMathOperator{\softmax}{softmax}
\DeclareMathOperator{\ReLU}{ReLU}
\DeclareMathOperator{\GeLU}{GeLU}
\DeclareMathOperator{\SiLU}{SiLU}
\DeclareMathOperator{\SwiGLU}{SwiGLU}
\DeclareMathOperator{\LN}{LayerNorm}
\DeclareMathOperator{\RMSNorm}{RMSNorm}
\DeclareMathOperator{\FFN}{FFN}
\DeclareMathOperator{\Attn}{Attn}
\DeclareMathOperator{\RoPE}{RoPE}

% Information theory
\newcommand{\KL}[2]{D_{\text{KL}}\left(#1 \| #2\right)}
\newcommand{\Ent}[1]{H\left(#1\right)}
\newcommand{\CrossEnt}[2]{H\left(#1, #2\right)}
\DeclareMathOperator{\PPL}{PPL}
\DeclareMathOperator{\MFU}{MFU}

% Expectation
\newcommand{\E}{\mathbb{E}}
\newcommand{\R}{\mathbb{R}}
```
