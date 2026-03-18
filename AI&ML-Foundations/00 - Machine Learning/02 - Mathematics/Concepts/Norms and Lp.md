A **norm** is a <mark style="background: #FFB86CA6;">function</mark> that assigns a strictly positive **length** or **size** to a vector in a vector space.

### Definition of a Norm

Formally, let $V$ be a vector space over a field $F$ (typically the real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$). A **norm** is a function $\| \cdot \|: V \to \mathbb{R}$ that assigns a real-valued length to each vector $\mathbf{x} \in V$. For a function to qualify as a norm, it must satisfy the following three axioms for all vectors $\mathbf{x}, \mathbf{y} \in V$ and all scalars $\alpha \in F$:

- **Positive Definiteness:** $\| \mathbf{x} \| \ge 0$, and $\| \mathbf{x} \| = 0$ if and only if $\mathbf{x} = \mathbf{0}$.
- **Absolute Homogeneity:** $\| \alpha \mathbf{x} \| = |\alpha| \| \mathbf{x} \|$.
- **Triangle Inequality:** $\| \mathbf{x} + \mathbf{y} \| \le \| \mathbf{x} \| + \| \mathbf{y} \|$.

---

### The $L_p$ Norm

The $L_p$ norm (also written as $\ell_p$ norm) of a vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ is defined by the general formula:

$\| \mathbf{x} \|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}$

The parameter $p \in [1, \infty)$ determines the geometric properties of the space and how the "size" of the vector is calculated.

#### Common $L_p$ Norms

- **$L_1$ Norm ([[Manhattan Distance and Norm]]):** 
	- In Machine Learning, it is used in Lasso regression to induce sparsity.
- **$L_2$ Norm (Euclidean Norm):** 
	- It is the basis for Ridge regression and is rotationally invariant.
- **$L_\infty$ Norm (Maximum Norm):** 
	- It considers only the largest absolute component of the vector.

---

### Comparison of Norms

| Parameter ($p$) | Name                                                                                 | Geometric Shape | ML Use Case                |
| --------------- | ------------------------------------------------------------------------------------ | --------------- | -------------------------- |
| $L_1$           | [[Manhattan Distance and Norm#The Manhattan Norm ($L_1$ Norm)\|Manhattan]] / Taxicab | Diamond         | Feature Selection / Lasso  |
| $L_2$           | Euclidean                                                                            | Circle / Sphere | Weight Decay / Ridge       |
| $L_\infty$      | Chebyshev / Max                                                                      | Square / Cube   | Robustness / Uniform Error |

---

### Mathematical Implications in Optimization

The choice of $p$ significantly impacts the behavior of optimization algorithms:

- **Sparsity ($p \le 1$):** 
	- As $p$ decreases toward 1, the "unit ball" (the set of all points where $\| \mathbf{x} \|_p \le 1$) develops sharp corners on the axes. This geometric property forces optimization solutions to hit these corners, resulting in sparse vectors where many components are exactly zero.
- **Smoothness ($p = 2$):** 
	- The $L_2$ norm is strictly convex and differentiable everywhere, making it computationally efficient for gradient-based optimization.
- **Outlier Sensitivity ($p \to \infty$):** 
	- Higher values of $p$ place more weight on the largest elements. While $L_2$ penalizes outliers quadratically, $L_\infty$ focuses exclusively on the single worst-case error.

### Geometry of the $L_1$ Unit Ball

The unit ball $B_1$ in $\mathbb{R}^n$ is the set of all points satisfying $\|\mathbf{x}\|_1 \le 1$. In $\mathbb{R}^2$, the boundary $\partial B_1$ is defined by the locus $|x| + |y| = 1$. This equation defines a convex polytope (a cross-polytope) with vertices at the standard basis vectors.

The boundary is piecewise linear, defined by the following system of equations across the four quadrants:

| Quadrant | Condition          | Linear Equation | Boundary Line |
| -------- | ------------------ | --------------- | ------------- |
| **I**    | $x \ge 0, y \ge 0$ | $x + y = 1$     | $y = -x + 1$  |
| **II**   | $x < 0, y \ge 0$   | $-x + y = 1$    | $y = x + 1$   |
| **III**  | $x < 0, y < 0$     | $-x - y = 1$    | $y = -x - 1$  |
| **IV**   | $x \ge 0, y < 0$   | $x - y = 1$     | $y = x - 1$   |

The intersection of these half-spaces forms a diamond in $\mathbb{R}^2$ and an octahedron in $\mathbb{R}^3$.

### 1. $p=0.5$ (Non-convex/Concave Norm)

At $p < 1$, the space is technically a **quasi-normed space**. The shape is "pinched" toward the origin. This is used in compressed sensing to find solutions that are even sparser than $L_1$.

```plotly
{
    "data": [
        {
            "x": [-1.0, -0.9, -0.7, -0.5, -0.3, -0.1, 0.0, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0, 0.9, 0.7, 0.5, 0.3, 0.1, 0.0, -0.1, -0.3, -0.5, -0.7, -0.9, -1.0],
            "y": [0.0, 0.002, 0.02, 0.08, 0.2, 0.46, 1.0, 0.46, 0.2, 0.08, 0.02, 0.002, 0.0, -0.002, -0.02, -0.08, -0.2, -0.46, -1.0, -0.46, -0.2, -0.08, -0.02, -0.002, 0.0],
            "mode": "lines", "type": "scatter", "name": "L 0.5 (Concave)",
            "fill": "toself", "fillcolor": "rgba(255, 170, 0, 0.2)",
            "line": { "color": "#ffaa00", "width": 3, "shape": "spline" }
        },
        {
            "x": [0.7], "y": [0.7], "mode": "markers", "type": "scatter",
            "name": "Out of Bounds (L0.5 ≈ 1.67)",
            "marker": { "color": "#ff4444", "symbol": "x", "size": 12 }
        }
    ],
    "layout": {
        "title": "p = 0.5: Highly Sparse / Non-Convex",
        "xaxis": { "range": [-1.5, 1.5], "scaleanchor": "y", "scaleratio": 1 },
        "yaxis": { "range": [-1.5, 1.5] },
        "template": "plotly_dark"
    }
}
```

### 2. $p=1$ (Manhattan / Taxicab Norm)

At $p=1$, the "unit ball" is a perfect **diamond**. This is the specific threshold where the geometry becomes **convex** but remains "pointy" at the axes, which is the mathematical reason it promotes sparsity in machine learning.

```plotly
{
    "data": [
        {
            "x": [1, 0, -1, 0, 1],
            "y": [0, 1, 0, -1, 0],
            "mode": "lines+markers",
            "type": "scatter",
            "name": "L1 (Diamond)",
            "fill": "toself",
            "fillcolor": "rgba(0, 255, 136, 0.2)",
            "line": { "color": "#00ff88", "width": 3 },
            "marker": { "size": 8, "color": "#ffffff" }
        },
        {
            "x": [0.7], "y": [0.7],
            "mode": "markers", "type": "scatter",
            "name": "Out of Bounds (L1=1.4)",
            "marker": { "color": "#ff4444", "symbol": "x", "size": 12 }
        }
    ],
    "layout": {
        "title": "p = 1: Manhattan (Sparsity Inducing)",
        "xaxis": { "range": [-1.5, 1.5], "scaleanchor": "y", "scaleratio": 1 },
        "yaxis": { "range": [-1.5, 1.5] },
        "template": "plotly_dark"
    }
}
````


### 3. $p=2$ (Euclidean Norm)
This is the standard circle. It is **rotationally invariant**, meaning the distance doesn't change if you rotate the coordinate system.

```plotly
{
    "data": [
        {
            "x": [1, 0.92, 0.7, 0.38, 0, -0.38, -0.7, -0.92, -1, -0.92, -0.7, -0.38, 0, 0.38, 0.7, 0.92, 1],
            "y": [0, 0.38, 0.71, 0.92, 1, 0.92, 0.71, 0.38, 0, -0.38, -0.71, -0.92, -1, -0.92, -0.71, -0.38, 0],
            "mode": "lines", "type": "scatter", "name": "L2 (Circle)",
            "fill": "toself", "fillcolor": "rgba(0, 180, 255, 0.2)",
            "line": { "color": "#00b4ff", "width": 3, "shape": "spline" }
        },
        {
            "x": [0.7], "y": [0.7], "mode": "markers", "type": "scatter",
            "name": "Inside (L2 ≈ 0.99)",
            "marker": { "color": "#00ff88", "symbol": "circle", "size": 12 }
        }
    ],
    "layout": {
        "title": "p = 2: Euclidean (Rotational Invariance)",
        "xaxis": { "range": [-1.5, 1.5], "scaleanchor": "y", "scaleratio": 1 },
        "yaxis": { "range": [-1.5, 1.5] },
        "template": "plotly_dark"
    }
}
````

### 4. $p=10$ (Approaching $L_\infty$)
As $p \to \infty$, the norm is dominated by the largest coordinate ($|x|$ or $|y|$). The shape becomes a **square**. This is why $L_\infty$ is called the "Chebyshev distance" or "Maximum norm."

```plotly
{
    "data": [
        {
            "x": [1, 0.99, 0.9, 0.5, 0, -0.5, -0.9, -0.99, -1, -0.99, -0.9, -0.5, 0, 0.5, 0.9, 0.99, 1],
            "y": [0, 0.9, 0.99, 1, 1, 1, 0.99, 0.9, 0, -0.9, -0.99, -1, -1, -1, -0.99, -0.9, 0],
            "mode": "lines", "type": "scatter", "name": "L10 (Squircle)",
            "fill": "toself", "fillcolor": "rgba(255, 0, 255, 0.2)",
            "line": { "color": "#ff00ff", "width": 3, "shape": "spline" }
        },
        {
            "x": [0.7], "y": [0.7], "mode": "markers", "type": "scatter",
            "name": "Inside (L10 ≈ 0.75)",
            "marker": { "color": "#00ff88", "symbol": "circle", "size": 12 }
        }
    ],
    "layout": {
        "title": "p = 10: Approaching L-infinity (Max Norm)",
        "xaxis": { "range": [-1.5, 1.5], "scaleanchor": "y", "scaleratio": 1 },
        "yaxis": { "range": [-1.5, 1.5] },
        "template": "plotly_dark"
    }
}
````


### Note on the Test Point $(0.7, 0.7)$:
Observe how the point $(0.7, 0.7)$ behaves across these plots:
* **$p=0.5$**: The point is **outside** (The distance is $\approx 1.67$).
* **$p=2$**: The point is **just barely inside** (The distance is $\approx 0.99$).
* **$p=10$**: The point is **deeply inside** (The distance is $\approx 0.75$).
