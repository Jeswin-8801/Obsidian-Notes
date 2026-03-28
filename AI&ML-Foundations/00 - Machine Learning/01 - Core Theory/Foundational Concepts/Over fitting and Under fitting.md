### Model Generalization: Bias-Variance Decomposition

Let $J_{train}(\theta)$ and $J_{cv}(\theta)$ denote the cost functions for the training and cross-validation sets, respectively. Model performance is characterized by the convergence properties of these functions.

## 1. Error Diagnostics

| Diagnostic | $J_{train}(\theta)$ | $J_{cv}(\theta)$ | Regime |
| :--- | :--- | :--- | :--- |
| **High Bias** | High | $J_{cv} \approx J_{train}$ | Underfitting |
| **High Variance** | Low | $J_{cv} \gg J_{train}$ | Overfitting |
| **Optimal** | Low | $J_{cv} \approx J_{train}$ | Generalization |

### 01 - Core Theory/Foundational Concepts/Bias-Variance Tradeoff.md


#### 1. Mathematical Decomposition

For a regression problem $y = f(x) + \epsilon$ where $\epsilon \sim \mathcal{N}(0, \sigma^2)$, the expected Mean Squared Error (MSE) at a point $x$ for an estimator $\hat{f}$ is:

$$\mathbb{E}[(y - \hat{f}(x))^2] = \underbrace{\text{Bias}[\hat{f}(x)]^2}_{\text{Structural Error}} + \underbrace{\text{Var}[\hat{f}(x)]}_{\text{Estimation Error}} + \underbrace{\sigma^2}_{\text{Irreducible Noise}}$$

- **Bias:** $(\mathbb{E}[\hat{f}(x)] - f(x))^2$. High bias $\implies$ **Underfitting** (Model is too simple).
    
- **Variance:** $\mathbb{E}[(\hat{f}(x) - \mathbb{E}[\hat{f}(x)])^2]$. High variance $\implies$ **Overfitting** (Model is too sensitive to noise).
    

---

#### 2. Visualizing the Tradeoff (Obsidian Plotly)

The following block visualizes how increasing model complexity (e.g., polynomial degree) affects the error components.

Code snippet

```
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

#### 3. Dataset Examples: Underfitting vs. Overfitting

We use three different hypotheses $h(x)$ on the same $n=30$ dataset to demonstrate the shift.

##### Scenario A: High Bias (Underfitting)

- **Model:** $h(x) = \theta_0$ (Constant/Horizontal line).
    
- **Behavior:** Fails to capture the trend $\implies$ High Training Error, High Test Error.
    

##### Scenario B: Optimal Balance

- **Model:** $h(x) = \theta_0 + \theta_1 x$.
    
- **Behavior:** Captures the underlying linear trend while ignoring noise.
    

##### Scenario C: High Variance (Overfitting)

- **Model:** $h(x) = \sum_{j=0}^{20} \theta_j x^j$ (High-degree polynomial).
    
- **Behavior:** "Memorizes" the noise $\epsilon$ $\implies$ Zero Training Error, Massive Test Error.
    

Code snippet

```
{
  "data": [
    {
      "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "y": [2, 5, 4, 8, 7, 12, 11, 15, 14, 19],
      "type": "scatter",
      "mode": "markers",
      "name": "Data (Noisy Linear)"
    },
    {
      "x": [1, 10],
      "y": [10, 10],
      "type": "scatter",
      "mode": "lines",
      "name": "High Bias (Deg 0)",
      "line": {"color": "red"}
    },
    {
      "x": [1, 10],
      "y": [2, 19],
      "type": "scatter",
      "mode": "lines",
      "name": "Balanced (Deg 1)",
      "line": {"color": "green"}
    },
    {
      "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "y": [2, 5.5, 3.8, 8.2, 6.8, 12.2, 10.8, 15.5, 13.5, 19],
      "type": "scatter",
      "mode": "lines",
      "name": "High Variance (Deg 9)",
      "line": {"shape": "vh", "color": "orange"}
    }
  ],
  "layout": {
    "title": "Model Comparison: Variance vs. Bias",
    "xaxis": {"title": "x"},
    "yaxis": {"title": "y"}
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

---

## 2. Analytical Methods

### A. Learning Curves
As training set size $m \to \infty$:
*   **High Bias:** $J_{train}(\theta)$ and $J_{cv}(\theta)$ converge rapidly to a high value. Increasing $m$ is non-efficacious.
*   **High Variance:** $J_{train}(\theta) < J_{cv}(\theta)$ persists. $J_{cv}(\theta)$ is monotonically decreasing with $m$.

### B. Regularization ($\lambda$) Complexity
The objective function is modified by a penalty term $P(\theta)$:
$$J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2 + \frac{\lambda}{2m} \sum_{j=1}^{n} \theta_j^2$$

> [!ABSTRACT] Regularization Sensitivity
> - $\lambda \to \infty \implies \theta_j \approx 0 \implies \text{High Bias}$
> - $\lambda \to 0 \implies \text{Overfitting} \implies \text{High Variance}$

---

## 3. Mathematical Definitions

*   **Mean Squared Error (MSE):**
    $$J(\theta) = \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2$$
*   **Ridge Regression (L2) Cost:**
    $$J(\theta) = \text{MSE}(\theta) + \frac{\lambda}{2m} \|\theta\|_2^2$$

---

## 4. Heuristics for Optimization

- [ ] **High Bias?** $\implies$ Increase complexity: $\min(\lambda)$, add polynomial features $\phi(x)$, or increase model depth.
- [ ] **High Variance?** $\implies$ Decrease complexity: $\max(\lambda)$, feature selection, or increase $m$.

> [!TIP] k-Fold Cross-Validation
> Let $\sigma^2_{fold}$ be the variance of performance across folds. A high $\sigma^2_{fold}$ indicates model instability (High Variance), whereas a consistently high $\mu_{error}$ indicates High Bias.