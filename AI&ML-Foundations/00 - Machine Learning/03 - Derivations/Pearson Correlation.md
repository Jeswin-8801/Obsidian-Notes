
Measures the linear correlation between two sets of data, indicating the strength and direction of a linear relationship.
$$\large r_{xy} = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2}} $$
-   $x_i, y_i$: individual data points in two datasets $X$ and $Y$.
-   $\bar{x}, \bar{y}$: the means of datasets $X$ and $Y$.
-   $n$: the number of data points.

***

> [!NOTE] Visualizing Correlation
> 
> </br>
> 
> ```plotly
> {
>     "data": [
>         {
>             "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
>             "y": [1.1, 2.3, 2.8, 4.2, 5.1, 5.8, 7.2, 8.1, 8.9, 10.5],
>             "mode": "markers", "type": "scatter", "name": "r ≈ 1.0",
>             "xaxis": "x1", "yaxis": "y1", "marker": { "color": "#00ff88", "size": 8 }
>         },
>         {
>             "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
>             "y": [10.2, 8.8, 8.1, 7.2, 5.9, 5.1, 3.8, 3.1, 2.2, 1.1],
>             "mode": "markers", "type": "scatter", "name": "r ≈ -1.0",
>             "xaxis": "x2", "yaxis": "y2", "marker": { "color": "#ff4444", "size": 8 }
>         },
>         {
>             "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
>             "y": [5, 2, 9, 1, 7, 4, 8, 3, 6, 5],
>             "mode": "markers", "type": "scatter", "name": "r ≈ 0.0",
>             "xaxis": "x3", "yaxis": "y3", "marker": { "color": "#888888", "size": 8 }
>         }
>     ],
>     "layout": {
>         "title": { "text": "<b>Pearson Correlation Coefficients</b>", "font": { "size": 20 } },
>         "grid": { "rows": 1, "columns": 3, "pattern": "independent" },
>         "template": "plotly_dark",
>         "margin": { "l": 50, "r": 50, "t": 80, "b": 50 },
>         "xaxis":  { "showline": true, "linewidth": 2, "linecolor": "#666", "title": "X (Pos)" },
>         "yaxis":  { "showline": true, "linewidth": 2, "linecolor": "#666", "title": "Y" },
>         "xaxis2": { "showline": true, "linewidth": 2, "linecolor": "#666", "title": "X (Neg)" },
>         "yaxis2": { "showline": true, "linewidth": 2, "linecolor": "#666" },
>         "xaxis3": { "showline": true, "linewidth": 2, "linecolor": "#666", "title": "X (Null)" },
>         "yaxis3": { "showline": true, "linewidth": 2, "linecolor": "#666" }
>     }
> }
> ```

</br>

### Why is the range $[-1, 1]$? 
From a Linear Algebra perspective, the Pearson Correlation Coefficient is actually the **Cosine of the angle** between two centered vectors. 

1. **Centering:** Subtract the mean ($\bar{x}, \bar{y}$) from each data point to create centered vectors $\mathbf{a}$ and $\mathbf{b}$. 
2. **Vector Form:** $r = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|}$ 
3. **The Proof:** According to the **Cauchy-Schwarz Inequality**, the absolute value of the dot product of two vectors is always less than or equal to the product of their magnitudes: $$|\mathbf{a} \cdot \mathbf{b}| \leq \|\mathbf{a}\| \|\mathbf{b}\|$$ Dividing both sides by $\|\mathbf{a}\| \|\mathbf{b}\|$ gives: $$\frac{|\mathbf{a} \cdot \mathbf{b}|}{\|\mathbf{a}\| \|\mathbf{b}\|} \leq 1$$ This limits the result to the interval $[-1, 1]$. If $r = 1$, the vectors are perfectly aligned (parallel); if $r = -1$, they are perfectly opposed; if $r = 0$, they are **orthogonal** (perpendicular).

### Understanding the Values 

| Value ($r$) | Interpretation | Geometric Meaning |
| :--- | :--- | :--- | 
| **$+1.0$** | Perfect Positive | All points lie exactly on a line with a positive slope. | 
| **$+0.7$ to $+0.9$** | Strong Positive | High degree of linear mapping; low variance around the trend. | 
| **$+0.4$ to $+0.6$** | Moderate Positive | Clear upward trend, but significant "noise" or spread. | 
| **$0.0$** | No Linear Correlation | Random cloud of points (or a perfect non-linear shape like a circle). | 
| **$-0.5$** | Moderate Negative | Downward trend with noticeable dispersion. | 
| **$-1.0$** | Perfect Negative | All points lie exactly on a line with a negative slope. | 
