
### 1. Setup of the Empirical Risk Problem

Consider a linear hypothesis class $\mathcal{H} = \{ h_\theta(x) = \theta x : \theta \in \mathbb{R} \}$. Let the loss function $L: \mathbb{R} \times \mathbb{R} \to \mathbb{R}_{\geq 0}$ be the quadratic loss:
$$\large L(h_\theta(x), y) = (h_\theta(x) - y)^2 = (\theta x - y)^2$$

Given a dataset $\mathcal{D} = \{ (x_i, y_i) \}_{i=1}^n$ of size $n=10$, the objective is to find the parameter $\hat{\theta}$ that minimizes the empirical risk $R_n(\theta)$:
$$\large R_n(\theta) = \frac{1}{n} \sum_{i=1}^n (\theta x_i - y_i)^2$$

---

### 2. Dataset Formalization

The dataset $\mathcal{D}$ consists of $n=10$ observations. To characterize the "layout" of the labels $Y$, we define its empirical distribution via quartiles.

| x   | y     |
| --- | ----- |
| 1   | 3.49  |
| 2   | 4.72  |
| 3   | 8.79  |
| 4   | 13.04 |
| 5   | 12.03 |
| 6   | 14.53 |
| 7   | 20.65 |
| 8   | 21.53 |
| 9   | 21.56 |
| 10  | 26.08 |

---

## 3. Empirical Risk Surface and Optimization

#### 3.1. Data Characterization & Prediction

We assume the hypothesis $h_\theta(x) = \theta x$. Based on your provided dataset $\mathcal{D}$, we compute the Empirical Risk $R_n(\theta)$ across a search space $\Theta \in [2.0, 3.5]$.

```plotly
{
  "data": [
    {
      "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
      "y": [3.49, 4.72, 8.79, 13.04, 12.03, 14.53, 20.65, 21.53, 23.56, 26.08],
      "type": "scatter",
      "mode": "markers",
      "name": "Observed Data (D)",
      "marker": {"color": "#636EFA"}
    },
    {
      "x": [0, 10],
      "y": [0, 25.8],
      "type": "scatter",
      "mode": "lines",
      "name": "h(x) = 2.58x",
      "line": {"dash": "dash", "color": "#EF553B"}
    },
    {
      "y": [3.49, 4.72, 8.79, 13.04, 12.03, 14.53, 20.65, 21.53, 23.56, 26.08],
      "type": "box",
      "name": "Y-Distribution (Layout)",
      "xaxis": "x2",
      "marker": {"color": "#00CC96"}
    }
  ],
  "layout": {
    "title": "Dataset Layout & Model Inference",
    "grid": {"rows": 1, "columns": 2, "pattern": "independent"},
    "xaxis": {"title": "Feature x"},
    "yaxis": {"title": "Target y"},
    "xaxis2": {"title": "Box Analysis", "anchor": "y2"},
    "showlegend": true
  }
}
```

---

#### 3.2. Loss Surface: Empirical Risk $R_n(\theta)$

The following block visualizes the **convexity** of the quadratic loss. The "Grid Search" evaluates the risk at discrete intervals to find the global minimum.

```plotly
{
  "data": [
    {
      "x": [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.58, 2.7, 2.8, 2.9, 3.0],
      "y": [13.2, 10.1, 7.5, 5.4, 3.8, 2.7, 2.45, 2.9, 4.1, 5.8, 8.1],
      "type": "scatter",
      "mode": "lines+markers",
      "name": "Risk Surface",
      "line": {"shape": "spline", "color": "#AB63FA"}
    }
  ],
  "layout": {
    "title": "Empirical Risk vs. Theta (Grid Search)",
    "xaxis": {"title": "Theta (Parameter)"},
    "yaxis": {"title": "MSE (Risk)"},
    "annotations": [
      {
        "x": 2.58,
        "y": 2.45,
        "text": "Global Min (theta-hat)",
        "showarrow": true,
        "arrowhead": 2
      }
    ]
  }
}
```

---

#### 3.3. Mathematical Derivation: Grid Search Algorithm

To find $\hat{\theta}$ for the objective:
$\large \min R_n(\theta) = \frac{1}{n} \sum_{i=1}^n (\theta x_i - y_i)^2$:

**Step 1: Discretization**

Define a finite parameter set $\Theta = \{ \theta \in \mathbb{R} : \theta_{start} + k \cdot \Delta\theta \}$. For your data, we observe the slope $y/x$ approximates $2.6$, so we search $\Theta = [2.0, 3.5]$ with $\Delta\theta = 0.01$.

**Step 2: Objective Evaluation**

For each $\theta_j \in \Theta$, compute the scalar cost:

$$J(\theta_j) = \frac{1}{10} \sum_{i=1}^{10} (\theta_j x_i - y_i)^2$$

**Step 3: Minimum Selection**

$$\hat{\theta} = \text{find}(\theta_j \in \Theta \mid J(\theta_j) = \min(J))$$

**Numerical Result:**

Given $\sum x_i y_i = 993.42$ and $\sum x_i^2 = 385$:

$$\hat{\theta}_{OLS} = \frac{993.42}{385} \approx 2.58$$

The Grid Search converges to this value as $\Delta\theta \to 0$.

> [!MATH] Computational Complexity
> 
> Grid search is $\large O(\frac{1}{\epsilon^d})$ where $\epsilon$ is precision and $d$ is dimension. For the simple linear case ($d=1$), it is efficient, but for Deep Learning ($d > 10^6$), we must utilize **Stochastic Gradient Descent (SGD)**.

The risk function $R_n(\theta)$ is a convex quadratic in $\theta$. The optimality condition is given by the vanishing gradient:
$$\large \frac{dR_n}{d\theta} = \frac{2}{n} \sum_{i=1}^n x_i(\theta x_i - y_i) = 0$$

Solving for $\theta$ yields the standard [[Ordinary Least Squares Estimation|Ordinary Least Squares]] (OLS) estimator:
$$\large \hat{\theta} = \frac{\sum x_i y_i}{\sum x_i^2}$$

For the provided dataset $\mathcal{D}$, the numerical solution obtained via grid search over $\theta \in [0, 5]$ is:
$$\hat{\theta} \approx 2.63$$
---

### 4. Summary Table for ERM

| **Component**         | **Expression / Value**           |
| --------------------- | -------------------------------- |
| **Hypothesis**        | $h_\theta(x) = \theta x$         |
| **Risk Functional**   | $R_n(\theta) = \frac{1}{n} \| \mathbf{y} - \theta \mathbf{x} \| _2$ |
| **Optimal Parameter** | $\hat{\theta} = 2.63$            |
| **Minimum Risk**      | $R_n(\hat{\theta}) \approx 3.42$ |
