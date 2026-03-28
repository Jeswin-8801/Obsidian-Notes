Given your interest in machine learning and deep learning, I've categorized these into the most common functions you'll encounter when building neural networks or using traditional ML models.

---

## 1. Activation Functions

Activation functions introduce **non-linearity** into the network, allowing it to learn complex patterns.

### Linear & Threshold

- **Linear:** $f(x) = x$. Used in the output layer for regression tasks.
    
- **Step Function:** $f(x) = 1$ if $x \ge 0$ else $0$. Used in the original Perceptron (rarely used in DNNs).
    

### Sigmoid & Tanh (Saturated)

- **Sigmoid (Logistic):** $\sigma(x) = \frac{1}{1 + e^{-x}}$. Maps input to $(0, 1)$. Often used for binary classification.
    
- **Hyperbolic Tangent (Tanh):** $f(x) = \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$. Maps input to $(-1, 1)$. Zero-centered, generally preferred over Sigmoid for hidden layers.
    

### ReLU & Variants (Non-Saturated)

- **ReLU (Rectified Linear Unit):** $f(x) = \max(0, x)$. The standard for hidden layers in DNNs. Solves the vanishing gradient problem for $x > 0$.
    
- **Leaky ReLU:** $f(x) = \max(0.01x, x)$. Prevents "dying ReLU" by allowing a small gradient when $x < 0$.
    
- **ELU (Exponential Linear Unit):** $f(x) = x$ if $x > 0$ else $\alpha(e^x - 1)$. Smoother transition at zero.
    
- **Softplus:** $f(x) = \ln(1 + e^x)$. A smooth approximation of ReLU.
    

### Specialized

- **Softmax:** $\sigma(\mathbf{z})_i = \frac{e^{z_i}}{\sum e^{z_j}}$. Used in the **output layer** for multi-class classification to produce a probability distribution.
    
- **Swish:** $f(x) = x \cdot \sigma(\beta x)$. Discovered via automated search; often outperforms ReLU in deep networks.
    

    

---

### Quick Reference Table

|**Task**|**Output Layer Activation**|**Loss Function**|
|---|---|---|
|**Regression**|Linear|MSE or MAE|
|**Binary Classification**|Sigmoid|Binary Cross-Entropy|
|**Multi-Class**|Softmax|Categorical Cross-Entropy|
|**Multi-Label**|Sigmoid|Binary Cross-Entropy|

Would you like me to provide the **Python/NumPy implementation** for any of these specific functions?