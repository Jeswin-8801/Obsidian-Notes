## Mean Squared Error (MSE) Loss

### 1. Definition
Mean Squared Error (also known as **L2 Loss**) measures the average squared difference between the estimated values $\hat{y}$ and the actual value $y$:
$$\large L = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

In the context of a single training example (often used in Stochastic Gradient Descent), the loss is:
$$L^{(i)} = (y_i - \hat{y}_i)^2$$



---

### 2. Derivation of the Gradient
To update the weights of a model, we need the derivative of the loss with respect to the prediction $\hat{y}_i$.

Applying the power rule and the chain rule:
Let $u = (y_i - \hat{y}_i)$. Then $L = u^2$.

$$\frac{\partial L}{\partial \hat{y}_i} = \frac{\partial L}{\partial u} \cdot \frac{\partial u}{\partial \hat{y}_i}$$

**Step-by-step:**
1. **Outer Derivative:** $\frac{\partial}{\partial u}(u^2) = 2u = 2(y_i - \hat{y}_i)$
2. **Inner Derivative:** $\frac{\partial}{\partial \hat{y}_i}(y_i - \hat{y}_i) = -1$

**Combine the terms:**
$$\frac{\partial L}{\partial \hat{y}_i} = 2(y_i - \hat{y}_i) \cdot (-1)$$

> [!abstract] Final Closed Form
> $$\large \frac{\partial L}{\partial \hat{y}_i} = -2(y_i - \hat{y}_i) = 2(\hat{y}_i - y_i)$$

---

### 3. Properties
* **Convexity:** MSE is a convex function, which guarantees that gradient descent will find the global minimum for linear models.
* **Sensitivity to Outliers:** Because the error is squared, large errors (outliers) have a disproportionately large impact on the total loss compared to MAE (L1 loss).
* **Units:** The units of MSE are the square of the target variable $y$.

---

### 4. Visualization (Loss Surface)
This visualizes how the loss increases quadratically as the prediction $\hat{y}$ moves away from the true target $y=0$.

```plotly
{
  "data": [
    {
      "x": [-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
      "y": [25.0, 20.25, 16.0, 12.25, 9.0, 6.25, 4.0, 2.25, 1.0, 0.25, 0.0, 0.25, 1.0, 2.25, 4.0, 6.25, 9.0, 12.25, 16.0, 20.25, 25.0],
      "type": "scatter",
      "mode": "lines",
      "name": "MSE Loss (y=0)",
      "line": { "color": "#d62728", "width": 3 }
    },
    {
      "x": [-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0],
      "y": [-10.0, -9.0, -8.0, -7.0, -6.0, -5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
      "type": "scatter",
      "mode": "lines",
      "name": "Gradient (2 * error)",
      "line": { "color": "#1f77b4", "width": 2, "dash": "dot" }
    }
  ],
  "layout": {
    "title": "MSE Loss and its Linear Gradient",
    "xaxis": { "title": "Predicted Value (target = 0)" },
    "yaxis": { "title": "Loss / Gradient" },
    "template": "plotly_white",
    "legend": { "orientation": "h", "y": -0.2 }
  }
}
```
