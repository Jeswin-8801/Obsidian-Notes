### Mathematical Decomposition

For a regression problem $y = f(x) + \epsilon$ where $\epsilon \sim \mathcal{N}(0, \sigma^2)$, the expected Mean Squared Error (MSE) at a point $x$ for an estimator $\hat{f}$ is:

$$\mathbb{E}[(y - \hat{f}(x))^2] = \underbrace{\text{Bias}[\hat{f}(x)]^2}_{\text{Structural Error}} + \underbrace{\text{Var}[\hat{f}(x)]}_{\text{Estimation Error}} + \underbrace{\sigma^2}_{\text{Irreducible Noise}}$$

- **Bias:** $(\mathbb{E}[\hat{f}(x)] - f(x))^2$. High bias $\implies$ **Underfitting** (Model is too simple).
- **Variance:** $\mathbb{E}[(\hat{f}(x) - \mathbb{E}[\hat{f}(x)])^2]$. High variance $\implies$ **Overfitting** (Model is too sensitive to noise).

---

### Visualizing the Tradeoff

The following block visualizes how increasing model complexity (e.g., polynomial degree) affects the error components.

```plotly
{
  "data": [
    {
      "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "y": [10, 6, 4, 3, 2.5, 2.2, 2.1, 2.05, 2.02, 2.01],
      "type": "scatter",
      "mode": "lines",
      "name": "Bias² (Underfitting)",
      "line": {"color": "#EF553B", "width": 3}
    },
    {
      "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "y": [0.5, 0.8, 1.5, 2.5, 4.0, 6.0, 8.5, 12.0, 16.0, 21.0],
      "type": "scatter",
      "mode": "lines",
      "name": "Variance (Overfitting)",
      "line": {"color": "#636EFA", "width": 3}
    },
    {
      "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "y": [11.5, 7.8, 6.5, 6.5, 7.5, 9.2, 11.6, 15.1, 19.0, 24.0],
      "type": "scatter",
      "mode": "lines",
      "name": "Total Error (MSE)",
      "line": {"color": "#00CC96", "width": 4}
    }
  ],
  "layout": {
    "title": "The Bias-Variance Tradeoff",
    "xaxis": {"title": "Model Complexity (e.g., Degree of Polynomial)"},
    "yaxis": {"title": "Error Magnitude"},
    "annotations": [
      {
        "x": 3.5,
        "y": 6.5,
        "text": "Optimal Complexity",
        "showarrow": true,
        "arrowhead": 2
      }
    ]
  }
}
```

---

#### 4. Summary Table

|**State**|**Complexity**|**Bias**|**Variance**|**Error Source**|
|---|---|---|---|---|
|**Underfitting**|Low|High|Low|Model too simple to learn the signal.|
|**Overfitting**|High|Low|High|Model learns noise as if it were signal.|
|**Optimal**|Medium|Low|Low|Model generalizes to unseen data.|

> [!MATH] Generalization Gap
> 
> The gap between Training Error and Test Error is a proxy for **Variance**. Regularization methods like `[[Lasso Regression]]` ($L_1$) or Ridge ($L_2$) explicitly trade a small increase in Bias for a large decrease in Variance to minimize the total expected risk.