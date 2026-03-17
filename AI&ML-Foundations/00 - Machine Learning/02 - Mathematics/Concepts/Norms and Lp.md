A **norm** is a <mark style="background: #FFB86CA6;">function</mark> that assigns a strictly positive **length** or **size** to a vector in a vector space.

##### For a function to be considered a "norm", it must satisfy three strict mathematical properties:

1. **Non-negativity:** 
	$||\textbf{x}|| \ge 0$
	$||\textbf{x}|| = 0 \,\,\text{(only if x is the 0 vector)}$
	
2. **Scalar Scalability:**
	$\|\alpha \mathbf{x}\| = |\alpha|.\|\mathbf{x}\|$
	
3. **==Triangle Inequality==:**
	$\|\mathbf{x} + \mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|$
	- The shortest distance between two points is a straight line.

#### What does the "*p*" in $L_p$​ mean?

The value of p changes the **geometry of the space**. 
**p** is essentially a **sensitivity tuner**:

- **p=1 (L1 Norm):** The "Manhattan" distance. p=1 means we simply sum the absolute values. In optimization, this creates a **diamond-shaped** constraint which forces many coordinates to zero (Sparsity/Lasso).
- **p=2 (L2 Norm):** The "Euclidean" distance. p=2 squares the values before summing. This creates a **spherical** constraint. It penalizes large outliers heavily but rarely drives weights to exactly zero (Ridge).
- **p→∞ (L-infinity Norm):** Also called the "Maximum" norm. It only cares about the single largest element in the vector: ∥x∥∞​=max(∣xi​∣).

#### In practice:

- **When 0<p<1:** The "norm" (technically a quasi-norm here) becomes extremely aggressive toward small values, pushing the system toward extreme sparsity. This is used in compressed sensing.
    
- **When p=2:** The math is "smooth" and differentiable everywhere, which is why L2 is the default for most Gradient Descent algorithms.
    
- **When p>2:** The norm becomes increasingly obsessed with the largest single outlier in the dataset, eventually ignoring all other data points as p→∞.

|Parameter (p)|Name|Geometric Shape|ML Use Case|
|---|---|---|---|
|**L1​**|Manhattan / Taxicab|Diamond|Feature Selection / Lasso|
|**L2​**|Euclidean|Circle / Sphere|Weight Decay / Ridge|
|**L∞​**|Chebyshev / Max|Square / Cube|Robustness / Uniform Error|

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
```
