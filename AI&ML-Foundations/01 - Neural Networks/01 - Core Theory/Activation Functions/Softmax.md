
### 1. Definition
For an input vector $\mathbf{z}$ of length $K$, the Softmax function $\sigma(\mathbf{z})$ is defined as:
$$\large \sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}}$$

where $i = 1, \dots, K$. The outputs are strictly positive and sum to 1, forming a valid probability distribution.



---

### 2. Derivation of the Gradient
Because the output $a_i$ depends on all $z_j$, the derivative is represented by a **Jacobian Matrix**. We find the partial derivative of the $i$-th output with respect to the $j$-th input: $\frac{\partial a_i}{\partial z_j}$.

**Case 1: When $i = j$ (Numerator and Denominator both contain $e^{z_i}$)**
Using the quotient rule $\left( \frac{f}{g} \right)' = \frac{f'g - fg'}{g^2}$:
Let $f = e^{z_i}$ and $g = \sum e^{z_k}$.
$$\frac{\partial a_i}{\partial z_i} = \frac{e^{z_i}(\sum e^{z_k}) - e^{z_i}(e^{z_i})}{(\sum e^{z_k})^2}$$
$$\frac{\partial a_i}{\partial z_i} = \frac{e^{z_i}}{\sum e^{z_k}} \cdot \frac{\sum e^{z_k} - e^{z_i}}{\sum e^{z_k}}$$
$$\large \frac{\partial a_i}{\partial z_i} = a_i(1 - a_i)$$

**Case 2: When $i \neq j$ (Only Denominator contains $e^{z_j}$)**
$$\frac{\partial a_i}{\partial z_j} = \frac{0 \cdot (\sum e^{z_k}) - e^{z_i}(e^{z_j})}{(\sum e^{z_k})^2}$$
$$\frac{\partial a_i}{\partial z_j} = - \frac{e^{z_i}}{\sum e^{z_k}} \cdot \frac{e^{z_j}}{\sum e^{z_k}}$$
$$\large \frac{\partial a_i}{\partial z_j} = -a_i a_j$$

---

### 3. The Jacobian Matrix
Combining these cases using the Kronecker delta $\delta_{ij}$ (where $\delta_{ij}=1$ if $i=j$ and $0$ otherwise):

> [!abstract] Final Closed Form
> $$\large \frac{\partial a_i}{\partial z_j} = a_i (\delta_{ij} - a_j)$$

---

### 4. Properties
* **Range:** $(0, 1)$ for every element.
* **Sum-to-one:** $\sum_{i=1}^K a_i = 1$.
* **Invariance:** Softmax is invariant to constant offsets: $\sigma(\mathbf{z}) = \sigma(\mathbf{z} + c)$. In practice, we subtract $\max(\mathbf{z})$ for numerical stability.

---

### 5. Visualization (Probabilities for 3 Classes)
This visualizes how the probability of Class 1 changes as its logit $z_1$ increases relative to two fixed classes ($z_2=0, z_3=0$).

```plotly
{
  "data": [
    {
      "x": [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
      "y": [0.0033, 0.0089, 0.0236, 0.0601, 0.1422, 0.3333, 0.5761, 0.7845, 0.9085, 0.9644, 0.9866],
      "type": "scatter",
      "mode": "lines+markers",
      "name": "P(Class 1)",
      "line": { "color": "#1f77b4", "width": 3 }
    },
    {
      "x": [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
      "y": [0.4983, 0.4955, 0.4882, 0.4699, 0.4289, 0.3333, 0.2119, 0.1077, 0.0458, 0.0178, 0.0067],
      "type": "scatter",
      "mode": "lines",
      "name": "P(Class 2)",
      "line": { "color": "#ff7f0e", "dash": "dot" }
    }
  ],
  "layout": {
    "title": "Softmax Probability Response (3-Class Example)",
    "xaxis": { "title": "Logit value of z1 (z2=0, z3=0)" },
    "yaxis": { "title": "Probability Output", "range": [0, 1.1] },
    "template": "plotly_white"
  }
}
```