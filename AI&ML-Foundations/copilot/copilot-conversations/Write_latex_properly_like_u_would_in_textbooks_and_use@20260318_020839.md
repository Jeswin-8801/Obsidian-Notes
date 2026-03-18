---
epoch: 1773779919965
modelKey: "gemini-flash-latest|google"
topic: "Proper LaTeX and Markdown Formatting"



tags:
  - copilot-conversation
---

**user**: Write latex properly
like u would in textbooks
and use markdown properly
[Context: Notes: 00 - Machine Learning/02 - Mathematics/Concepts/Norms and Lp.md]
[Timestamp: 2026/03/18 02:08:39]

**ai**: In the context of [[Norms and Lp]], a norm provides a formal way to measure the "length" or "magnitude" of vectors in a vector space.

### Definition of a Norm

Formally, let $V$ be a vector space over a field $F$ (typically the real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$). A **norm** is a function $\| \cdot \|: V \to \mathbb{R}$ that assigns a real-valued length to each vector $\mathbf{x} \in V$. For a function to qualify as a norm, it must satisfy the following three axioms for all vectors $\mathbf{x}, \mathbf{y} \in V$ and all scalars $\alpha \in F$:

- **Positive Definiteness:** $\| \mathbf{x} \| \ge 0$, and $\| \mathbf{x} \| = 0$ if and only if $\mathbf{x} = \mathbf{0}$.
- **Absolute Homogeneity:** $\| \alpha \mathbf{x} \| = |\alpha| \| \mathbf{x} \|$.
- **Triangle Inequality:** $\| \mathbf{x} + \mathbf{y} \| \le \| \mathbf{x} \| + \| \mathbf{y} \|$.

---

### The $L_p$ Norm

The $L_p$ norm (also written as $\ell_p$ norm) of a vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ is defined by the general formula:

$ \| \mathbf{x} \|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p} $

The parameter $p \in [1, \infty)$ determines the geometric properties of the space and how the "size" of the vector is calculated.

#### Common $L_p$ Norms

- **$L_1$ Norm (Manhattan Norm):** Calculated as $\| \mathbf{x} \|_1 = \sum_{i=1}^n |x_i|$. It represents the distance traveled if one is restricted to a grid-like path. In Machine Learning, it is used in Lasso regression to induce sparsity.
- **$L_2$ Norm (Euclidean Norm):** Calculated as $\| \mathbf{x} \|_2 = \sqrt{\sum_{i=1}^n x_i^2}$. This is the standard "straight-line" distance. It is the basis for Ridge regression and is rotationally invariant.
- **$L_\infty$ Norm (Maximum Norm):** Calculated as $\| \mathbf{x} \|_\infty = \max_i |x_i|$. It considers only the largest absolute component of the vector.

---

### Comparison of Norms

| Parameter ($p$) | Name | Geometric Shape | ML Use Case |
| --- | --- | --- | --- |
| $L_1$ | Manhattan / Taxicab | Diamond | Feature Selection / Lasso |
| $L_2$ | Euclidean | Circle / Sphere | Weight Decay / Ridge |
| $L_\infty$ | Chebyshev / Max | Square / Cube | Robustness / Uniform Error |

---

### Mathematical Implications in Optimization

The choice of $p$ significantly impacts the behavior of optimization algorithms:

- **Sparsity ($p \le 1$):** As $p$ decreases toward 1, the "unit ball" (the set of all points where $\| \mathbf{x} \|_p \le 1$) develops sharp corners on the axes. This geometric property forces optimization solutions to hit these corners, resulting in sparse vectors where many components are exactly zero.
- **Smoothness ($p = 2$):** The $L_2$ norm is strictly convex and differentiable everywhere, making it computationally efficient for gradient-based optimization.
- **Outlier Sensitivity ($p \to \infty$):** Higher values of $p$ place more weight on the largest elements. While $L_2$ penalizes outliers quadratically, $L_\infty$ focuses exclusively on the single worst-case error.
[Timestamp: 2026/03/18 02:08:50]

**user**: Need it to be less descriptive and have more mathematical notations
like you would in a text book
us latex whereever possible
keep explanations to a minimum assuming the reader has a fairly advanced grasp on said concepts.
[Timestamp: 2026/03/18 02:15:27]

**ai**: ### The Manhattan Norm ($L_1$ Norm)

In an $n$-dimensional vector space $\mathbb{R}^n$, the $L_1$ norm (also known as the taxicab or Manhattan norm) of a vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ is defined as the sum of the absolute values of its components:

$ \|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i| $

The corresponding metric, or Manhattan distance, between two points $\mathbf{p}, \mathbf{q} \in \mathbb{R}^n$ is given by:

$ d_1(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_1 = \sum_{i=1}^n |p_i - q_i| $

---

### Geometry of the $L_1$ Unit Ball

The unit ball $B_1$ in $\mathbb{R}^n$ is the set of all points satisfying $\|\mathbf{x}\|_1 \le 1$. In $\mathbb{R}^2$, the boundary $\partial B_1$ is defined by the locus $|x| + |y| = 1$. This equation defines a convex polytope (a cross-polytope) with vertices at the standard basis vectors.

The boundary is piecewise linear, defined by the following system of equations across the four quadrants:

| Quadrant | | Condition | | Linear Equation | | Boundary Line | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **I** | | $x \ge 0, y \ge 0$ | | $x + y = 1$ | | $y = -x + 1$ | |
| **II** | | $x < 0, y \ge 0$ | | $-x + y = 1$ | | $y = x + 1$ | |
| **III** | | $x < 0, y < 0$ | | $-x - y = 1$ | | $y = -x - 1$ | |
| **IV** | | $x \ge 0, y < 0$ | | $x - y = 1$ | | $y = x - 1$ | |

The intersection of these half-spaces forms a diamond in $\mathbb{R}^2$ and an octahedron in $\mathbb{R}^3$.

---

### Optimization and Sparsity

In the context of regularized empirical risk minimization, the $L_1$ penalty is employed to induce sparsity in the solution vector $\mathbf{w}^*$. Consider the objective:

$ \min_{\mathbf{w}} \mathcal{L}(\mathbf{w}) + \lambda \|\mathbf{w}\|_1 $

- **Singularity at the Origin:** The function $f(x) = |x|$ is non-differentiable at $x=0$. Its subdifferential is given by:
  $\partial |x| = \begin{cases} \{1\} & x > 0 \\ \{-1\} & x < 0 \\ [-1, 1] & x = 0 \end{cases}$
- **Geometric Interpretation:** The level sets of a smooth loss function $\mathcal{L}(\mathbf{w})$ are typically ellipsoidal. Due to the "pointed" nature of the $L_1$ ball at the axes (where $w_i = 0$ for some $i$), the constrained optimum $\mathbf{w}^*$ is statistically likely to occur at a vertex of the $L_1$ polytope.
- **Feature Selection:** This property effectively performs automatic feature selection by driving coefficients of irrelevant features to exactly zero, distinguishing it from the $L_2$ norm which only asymptotically approaches zero.

For further details on the comparison with other norms, refer to [[Norms and Lp]].
[Timestamp: 2026/03/18 02:15:41]