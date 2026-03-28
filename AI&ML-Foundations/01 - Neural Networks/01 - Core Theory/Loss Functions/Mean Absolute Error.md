## Mean Absolute Error (MAE) Loss

### 1. Definition
Mean Absolute Error is the average of the absolute differences between the actual values $y$ and the predicted values $\hat{y}$:
$$\large L = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$$

For a single observation, the loss is:
$$L^{(i)} = |y_i - \hat{y}_i|$$


---

### 2. Derivation of the Gradient
The absolute value function $f(u) = |u|$ is a piecewise function. To find the derivative with respect to the prediction $\hat{y}_i$, we look at the two cases of the error $u = (y_i - \hat{y}_i)$.

--- start-multi-column: Piecewise Gradient
number of columns: 2

**Case 1: $y_i > \hat{y}_i$ (Underestimation)**
$L = y_i - \hat{y}_i$
$$\frac{\partial L}{\partial \hat{y}_i} = -1$$

--- end-column ---

**Case 2: $y_i < \hat{y}_i$ (Overestimation)**
$L = -(y_i - \hat{y}_i) = \hat{y}_i - y_i$
$$\frac{\partial L}{\partial \hat{y}_i} = 1$$

--- end-multi-column

**Note on $y_i = \hat{y}_i$:**
Like ReLU, the MAE loss is not differentiable at exactly zero error (the "v-shape" corner). In optimization, the gradient is typically undefined or set to $0$ at this point.

> [!abstract] Final Closed Form
> $$\large \frac{\partial L}{\partial \hat{y}_i} = -\text{sign}(y_i - \hat{y}_i)$$

---

### 3. Properties vs. MSE
* **Robustness:** MAE is more robust to outliers. In MSE, an error of $10$ becomes a loss of $100$; in MAE, it remains $10$.
* **Constant Gradient:** The gradient is always $\pm 1$ regardless of the error magnitude. This can make convergence unstable near the minimum because the steps don't naturally get smaller (unlike MSE).
* **Median Estimator:** While MSE learns the **mean** of the data, MAE learns the **median**.

---

### 4. Plotly Visualization

```plotly
{
  "data": [
    {
      "x": [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
      "y": [5.0, 4.0, 3.0, 2.0, 1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
      "type": "scatter",
      "mode": "lines",
      "name": "MAE Loss (y=0)",
      "line": { "color": "#ff7f0e", "width": 3 }
    },
    {
      "x": [-5.0, -0.01, 0, 0.01, 5.0],
      "y": [-1, -1, 0, 1, 1],
      "type": "scatter",
      "mode": "lines",
      "name": "Gradient (-sign(error))",
      "line": { "color": "#7f7f7f", "width": 2, "dash": "dot" }
    }
  ],
  "layout": {
    "title": "MAE Loss and its Constant Gradient",
    "xaxis": { "title": "Predicted Value (target = 0)" },
    "yaxis": { "title": "Loss / Gradient", "range": [-1.5, 5.5] },
    "template": "plotly_white",
    "legend": { "orientation": "h", "y": -0.2 }
  }
}
```
