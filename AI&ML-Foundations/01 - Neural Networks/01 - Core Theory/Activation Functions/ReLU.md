### 1. Definition
The ReLU function is a piecewise linear function that outputs the input directly if it is positive; otherwise, it outputs zero:
$$\large f(x) = \max(0, x)$$



---

### 2. Derivation
Since ReLU is piecewise, we derive it by considering the two intervals of $x$:

--- start-multi-column: Piecewise Derivative
number of columns: 2

**Case 1: $x > 0$**
$$f(x) = x$$
$$\frac{d}{dx}(x) = 1$$

--- end-column ---

**Case 2: $x < 0$**
$$f(x) = 0$$
$$\frac{d}{dx}(0) = 0$$

--- end-multi-column

**Note on $x = 0$:**
Technically, ReLU is not differentiable at exactly $x = 0$ (the "kink"). In practice, we use a **subgradient**, usually setting the derivative to either $0$ or $1$ at that point (most frameworks use $0$).

> [!abstract] Final Closed Form
> $$f'(x) = \begin{cases} 1 & \text{if } x > 0 \\ 0 & \text{if } x \le 0 \end{cases}$$

---

### 3. Properties & Trade-offs
* **Sparsity:** Any input $x \le 0$ results in a $0$ output. This leads to "sparse" activations where only a subset of neurons is active, improving computational efficiency.
* **Vanishing Gradient:** For $x > 0$, the gradient is a constant $1$, which prevents the gradient from shrinking during backpropagation in deep networks.
* **Dying ReLU Problem:** If a neuron's weights are updated such that it always receives negative inputs, its gradient becomes $0$ forever ("dies"), and it stops contributing to learning.

---

### 4. Visualization

```plotly
{
  "data": [
    {
      "x": [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],
      "y": [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5],
      "type": "scatter",
      "mode": "lines",
      "name": "ReLU(x)",
      "line": { "color": "#17becf", "width": 4 }
    },
    {
      "x": [-5, -0.001, 0, 0.001, 5],
      "y": [0, 0, 0, 1, 1],
      "type": "scatter",
      "mode": "lines",
      "name": "d/dx ReLU",
      "line": { "color": "#7f7f7f", "width": 3, "dash": "dot" }
    }
  ],
  "layout": {
    "title": "ReLU and its Step Derivative",
    "xaxis": { "title": "x" },
    "yaxis": { "title": "Value", "range": [-0.5, 5.5] },
    "template": "plotly_white",
    "legend": { "orientation": "h", "y": -0.2 }
  }
}
```
