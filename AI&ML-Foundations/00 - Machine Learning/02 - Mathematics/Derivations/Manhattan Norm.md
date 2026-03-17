## Manhattan Distance / L1 Norm
Calculates the sum of the absolute differences of their Cartesian coordinates.
$$\large d(p, q) = \sum_{i=1}^{n} |q_i - p_i| $$
-   $p, q$: two points (vectors) in $n$-dimensional space.
-   $p_i, q_i$: the $i \text{-th}$ coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.

***


To explain why the **Manhattan ($L_1$) Norm** creates a diamond, we have to look at the "Unit Ball"—the set of all points $(x, y)$ where the total distance from the origin is exactly $1$.

### Mathematical Derivation of the $L_1$ Diamond

In a 2D plane, the $L_1$ norm is defined as:

$$\|v\|_1 = |x| + |y|$$

To find the boundary (the shape), we set the norm to a constant $c=1$:

$$|x| + |y| = 1$$

Because of the absolute values, this equation splits into four linear equations depending on the quadrant:

|**Quadrant**|**Condition**|**Linear Equation**|**Boundary Line**|
|---|---|---|---|
|**I**|$x \ge 0, y \ge 0$|$x + y = 1$|$y = -x + 1$|
|**II**|$x < 0, y \ge 0$|$-x + y = 1$|$y = x + 1$|
|**III**|$x < 0, y < 0$|$-x - y = 1$|$y = -x - 1$|
|**IV**|$x \ge 0, y < 0$|$x - y = 1$|$y = x - 1$|

When you plot these four lines, they intersect at $(\pm 1, 0)$ and $(0, \pm 1)$, forming a **perfect diamond**.

---

### Example

If we have a [[Sparse and Dense Vectors|sparse vector]] $\mathbf{w}$ representing weights in a model, and we constrain them such that $\|\mathbf{w}\|_1 \le 1$:

- **Point A:** $(1, 0)$ → $\|A\|_1 = |1| + |0| = 1$ (On the boundary)
- **Point B:** $(0.5, 0.5)$ → $\|B\|_1 = |0.5| + |0.5| = 1$ (On the boundary)
- **Point C:** $(0.7, 0.7)$ → $\|C\|_1 = 1.4$ (**Outside** the diamond)

```plotly
{
    "data": [
        {
            "x": [1, 0, -1, 0, 1],
            "y": [0, 1, 0, -1, 0],
            "mode": "lines+markers",
            "type": "scatter",
            "name": "L1 Unit Ball (Diamond)",
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
        "title": "Mathematical Geometry of the L1 Norm",
        "xaxis": { "range": [-1.5, 1.5], "scaleanchor": "y", "scaleratio": 1, "title": "x-axis" },
        "yaxis": { "range": [-1.5, 1.5], "title": "y-axis" },
        "template": "plotly_dark",
        "showlegend": true,
        "width": 500, "height": 500
    }
}
````


### Why this matters for ML (Sparsity)
In optimization, the "corners" of this diamond sit exactly on the axes. When your loss function contour (which is usually curved) touches this diamond, it is most likely to hit a **corner** first. Because the corner is on an axis (where one coordinate is zero), the L1 norm naturally "zeros out" features, leading to the **sparsity** you see in Lasso regression.