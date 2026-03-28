
### 1. Definition
The Softplus function is a smooth approximation of the Rectified Linear Unit (ReLU). It is defined as the analytic helper of the ReLU:
$$\large f(x) = \ln(1 + e^x)$$



---

### 2. Derivation (Chain Rule)
To find the derivative $f'(x)$, we apply the chain rule to the natural logarithm.

Let $u = 1 + e^x$. Then $f(x) = \ln(u)$.

$$\frac{df}{dx} = \frac{df}{du} \cdot \frac{du}{dx}$$

**Step-by-step:**
1. **Logarithmic Derivative:** $\frac{d}{du}(\ln u) = \frac{1}{u} = \frac{1}{1 + e^x}$
2. **Inner Derivative:** $\frac{d}{dx}(1 + e^x) = e^x$

**Combine the terms:**
$$f'(x) = \frac{1}{1 + e^x} \cdot e^x$$
$$f'(x) = \frac{e^x}{1 + e^x}$$

---

### 3. Relationship to Sigmoid
By dividing both the numerator and denominator by $e^x$, we reveal a fundamental relationship in Deep Learning:

--- start-multi-column: Identity
number of columns: 2

**Algebraic Step**
$$f'(x) = \frac{e^x / e^x}{(1 + e^x) / e^x}$$
$$f'(x) = \frac{1}{e^{-x} + 1}$$

--- end-column ---

**Result**
$$\large f'(x) = \sigma(x)$$
The derivative of **Softplus** is exactly the **Sigmoid** function.

--- end-multi-column

> [!abstract] Final Closed Form
> $$\large \frac{d}{dx} \text{Softplus}(x) = \frac{1}{1 + e^{-x}}$$

---

### 4. Properties
* **Range:** $(0, \infty)$. Unlike ReLU, it never reaches exactly $0$.
* **Smoothness:** It is differentiable everywhere, including at $x=0$, avoiding the "kink" found in ReLU.
* **Sparsity:** While it approximates ReLU, it does not produce true sparsity because the output is always strictly positive.

---

### 5. Visualization

```plotly
{
  "data": [
    {
      "x": [-5.0, -4.8, -4.6, -4.4, -4.2, -4.0, -3.8, -3.6, -3.4, -3.2, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0],
      "y": [0.0067, 0.0082, 0.01, 0.0122, 0.0149, 0.0181, 0.0221, 0.027, 0.0329, 0.04, 0.0486, 0.0591, 0.0718, 0.0871, 0.1055, 0.1269, 0.1525, 0.1823, 0.2172, 0.2577, 0.3133, 0.3711, 0.4352, 0.5057, 0.5822, 0.6931, 0.7973, 0.913, 1.0375, 1.1711, 1.3133, 1.4633, 1.6203, 1.7836, 1.9525, 2.1269, 2.3061, 2.4897, 2.6773, 2.8683, 3.0486, 3.24, 3.4338, 3.6295, 3.8266, 4.0181, 4.2149, 4.4122, 4.61, 4.8082, 5.0067],
      "type": "scatter",
      "mode": "lines",
      "name": "Softplus(x)",
      "line": { "color": "#9467bd", "width": 3 }
    },
    {
      "x": [-5.0, -4.8, -4.6, -4.4, -4.2, -4.0, -3.8, -3.6, -3.4, -3.2, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0],
      "y": [0.0067, 0.0082, 0.01, 0.0121, 0.0148, 0.018, 0.0219, 0.0266, 0.0323, 0.0392, 0.0474, 0.0573, 0.0691, 0.0832, 0.0998, 0.1192, 0.1419, 0.168, 0.1978, 0.2315, 0.2689, 0.31, 0.3543, 0.4013, 0.4502, 0.5, 0.5498, 0.5987, 0.6457, 0.69, 0.7311, 0.7685, 0.8022, 0.832, 0.8581, 0.8808, 0.9002, 0.9168, 0.9309, 0.9427, 0.9526, 0.9608, 0.9677, 0.9734, 0.9781, 0.982, 0.9852, 0.9879, 0.99, 0.9918, 0.9933],
      "type": "scatter",
      "mode": "lines",
      "name": "d/dx Softplus (Sigmoid)",
      "line": { "color": "#bcbd22", "width": 3, "dash": "dash" }
    }
  ],
  "layout": {
    "title": "Softplus and its Derivative",
    "xaxis": { "title": "x" },
    "yaxis": { "title": "Value" },
    "template": "plotly_white",
    "legend": { "orientation": "h", "y": -0.2 }
  }
}
```