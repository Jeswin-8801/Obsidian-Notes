
The derivation of $\delta^{[2]} = \mathbf{a}^{[2]} - \mathbf{y}$ is a classic result in deep learning that occurs specifically when **Binary Cross-Entropy (BCE) Loss** is paired with a **Sigmoid** activation function. The beauty of this pairing is that the complex terms in their individual derivatives cancel each other out perfectly.

---

### 1. Define the Components

First, we identify the two functions involved in the chain rule for the output layer $L=2$.

##### **A. Binary Cross-Entropy Loss ($L$):**
For a single output neuron:

$$L = -(y \ln(a^{[2]}) + (1 - y) \ln(1 - a^{[2]}))$$

##### **B. Sigmoid Activation ($a^{[2]}$):**

The activation is a function of the logit $z^{[2]}$:

$$a^{[2]} = \sigma(z^{[2]}) = \frac{1}{1 + e^{-z^{[2]}}}$$

---

### 2. Apply the Chain Rule

To find the gradient of the loss with respect to the pre-activation $z^{[2]}$, we apply the multivariate chain rule:

$$\large \frac{\partial L}{\partial z^{[2]}} = \frac{\partial L}{\partial a^{[2]}} \cdot \frac{\partial a^{[2]}}{\partial z^{[2]}}$$

---

### 3. Compute Individual Derivatives

#### Part I: $\frac{\partial L}{\partial a^{[2]}}$ (Derivative of BCE)

$$\frac{\partial L}{\partial a^{[2]}} = -\left( \frac{y}{a^{[2]}} - \frac{1 - y}{1 - a^{[2]}} \right)$$

To simplify, find a common denominator:

$$\frac{\partial L}{\partial a^{[2]}} = -\left( \frac{y(1 - a^{[2]}) - a^{[2]}(1 - y)}{a^{[2]}(1 - a^{[2]})} \right) = \frac{a^{[2]} - y}{a^{[2]}(1 - a^{[2]})}$$

#### Part II: $\frac{\partial a^{[2]}}{\partial z^{[2]}}$ (Derivative of Sigmoid)

As derived previously, the derivative of the sigmoid function is:

$$\frac{\partial a^{[2]}}{\partial z^{[2]}} = a^{[2]}(1 - a^{[2]})$$

---

### 4. Combine and Cancel

Now, substitute both parts back into the chain rule equation:

$$\frac{\partial L}{\partial z^{[2]}} = \left[ \frac{a^{[2]} - y}{a^{[2]}(1 - a^{[2]})} \right] \cdot \left[ a^{[2]}(1 - a^{[2]}) \right]$$

Notice that the term $a^{[2]}(1 - a^{[2]})$ appears in both the numerator and the denominator. They cancel out completely:

$$\large \frac{\partial L}{\partial z^{[2]}} = a^{[2]} - y$$

---

### 5. Final Result

In vector notation for the entire layer:

$$\large \delta^{[2]} = \mathbf{a}^{[2]} - \mathbf{y}$$

|**Variable**|**Dimension**|**Set**|
|---|---|---|
|$\delta^{[2]}$|$n^{[2]} \times 1$|$\mathbb{R}^{n^{[2]}}$|
|$\mathbf{a}^{[2]}$|$n^{[2]} \times 1$|$(0, 1)^{n^{[2]}}$|
|$\mathbf{y}$|$n^{[2]} \times 1$|$\{0, 1\}^{n^{[2]}}$|
