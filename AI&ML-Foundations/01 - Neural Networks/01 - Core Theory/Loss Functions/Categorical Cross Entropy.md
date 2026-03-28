### 1. Definition
For a single training example with $K$ classes, where $\mathbf{y}$ is a one-hot encoded vector of ground truths and $\mathbf{\hat{y}}$ is the vector of predicted probabilities:
$$\large L = -\sum_{i=1}^{K} y_i \log(\hat{y}_i)$$

Since $\mathbf{y}$ is one-hot encoded, only one $y_i = 1$ (the true class $c$), while all others are $0$. Thus, the loss simplifies to:
$$L = -\log(\hat{y}_c)$$



---

### 2. Derivation of the Gradient
We calculate the partial derivative of the loss $L$ with respect to a specific predicted probability $\hat{y}_i$. 

$$\frac{\partial L}{\partial \hat{y}_i} = \frac{\partial}{\partial \hat{y}_i} \left( -\sum_{j=1}^{K} y_j \log(\hat{y}_j) \right)$$

Because each $\hat{y}_j$ is treated as an independent variable in this partial derivative (before considering the Softmax constraint):
$$\frac{\partial L}{\partial \hat{y}_i} = - \left( y_i \frac{\partial \log(\hat{y}_i)}{\partial \hat{y}_i} \right)$$

> [!abstract] Final Closed Form
> $$\large \frac{\partial L}{\partial \hat{y}_i} = -\frac{y_i}{\hat{y}_i}$$

---

### 3. Combining with Softmax (The "Magic" Cancellation)
In practice, CCE is almost always used with a **Softmax** output layer. When you derive the loss with respect to the *logits* ($z_i$) rather than the probabilities ($\hat{y}_i$), the chain rule yields a remarkably simple result:

$$\frac{\partial L}{\partial z_i} = \sum_j \frac{\partial L}{\partial \hat{y}_j} \frac{\partial \hat{y}_j}{\partial z_i}$$

Substituting the CCE gradient and the Softmax Jacobian:
$$\large \frac{\partial L}{\partial z_i} = \hat{y}_i - y_i$$

This means the gradient is simply the **difference between the predicted probability and the ground truth**.

---

### 4. Properties
* **Information Theory:** CCE measures the "surprise" or bits of information lost when using $\mathbf{\hat{y}}$ to approximate the true distribution $\mathbf{y}$.
* **Numerical Stability:** In frameworks like PyTorch or TensorFlow, `CrossEntropyLoss` usually expects raw logits because it internally combines Log-Softmax and NLL-Loss to avoid floating-point underflow.

---

### 5. Plotly Visualization (Loss Sensitivity)
This shows how the loss value changes for the "Correct Class" based on the probability assigned to it.

```plotly
{
  "data": [
    {
      "x": [0.001, 0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.999],
      "y": [6.907, 4.605, 2.302, 1.609, 1.203, 0.916, 0.693, 0.510, 0.356, 0.223, 0.105, 0.001],
      "type": "scatter",
      "mode": "lines",
      "name": "-log(P) for True Class",
      "line": { "color": "#9467bd", "width": 3 }
    }
  ],
  "layout": {
    "title": "CCE Loss vs. Predicted Probability of Correct Class",
    "xaxis": { "title": "Predicted Probability (y-hat_c)", "range": [0, 1] },
    "yaxis": { "title": "Loss Value" },
    "template": "plotly_white"
  }
}
```
