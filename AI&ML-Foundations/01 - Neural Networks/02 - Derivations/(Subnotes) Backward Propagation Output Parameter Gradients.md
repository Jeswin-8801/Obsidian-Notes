To derive the gradients for the weights $\mathbf{W}^{[2]}$ and biases $\mathbf{b}^{[2]}$, we move from the error at the pre-activation level ($\delta^{[2]}$) to the actual parameters that we need to update.

This is the final step of the chain rule for the output layer $l=2$.

---

### 1. The Gradient of Weights ($d\mathbf{W}^{[2]}$)

We want to find how the loss $L$ changes with respect to each individual weight $w_{ij}^{[2]}$. According to the chain rule:
$$\large \frac{\partial L}{\partial w_{ij}^{[2]}} = \frac{\partial L}{\partial z_i^{[2]}} \cdot \frac{\partial z_i^{[2]}}{\partial w_{ij}^{[2]}}$$

#### Part I: The Error Term
From our previous derivation, we know that $\frac{\partial L}{\partial z_i^{[2]}}$ is the $i$-th element of our error vector $\delta^{[2]}$:

$$\frac{\partial L}{\partial z_i^{[2]}} = \delta_i^{[2]}$$

#### Part II: The Local Derivative
Now look at the linear equation for a single logit $z_i^{[2]}$:

$$z_i^{[2]} = \sum_{k=1}^{n^{[1]}} w_{ik}^{[2]} a_k^{[1]} + b_i^{[2]}$$

When we take the partial derivative with respect to a specific weight $w_{ij}^{[2]}$, all other terms in the summation (and the bias) drop out because they are constants relative to $w_{ij}^{[2]}$:

$$\frac{\partial z_i^{[2]}}{\partial w_{ij}^{[2]}} = a_j^{[1]}$$

#### Part III: Vectorization
Combining these, we get:

$$\frac{\partial L}{\partial w_{ij}^{[2]}} = \delta_i^{[2]} \cdot a_j^{[1]}$$

To represent this for the entire weight matrix, we use the **outer product** of the error vector and the transposed activation vector from the previous layer:

$$\large \frac{\partial L}{\partial \mathbf{W}^{[2]}} = \delta^{[2]} (\mathbf{a}^{[1]})^T$$

---

### 2. The Gradient of Biases ($d\mathbf{b}^{[2]}$)

For the bias $b_i^{[2]}$, the chain rule is:
$$\frac{\partial L}{\partial b_i^{[2]}} = \frac{\partial L}{\partial z_i^{[2]}} \cdot \frac{\partial z_i^{[2]}}{\partial b_i^{[2]}}$$

#### Part I: The Local Derivative
Looking again at the equation for $z_i^{[2]}$:
$$z_i^{[2]} = (\dots) + b_i^{[2]}$$
The derivative of $z_i^{[2]}$ with respect to its own bias is simply $1$:
$$\frac{\partial z_i^{[2]}}{\partial b_i^{[2]}} = 1$$

#### Part II: Result
Substituting back:
$$\frac{\partial L}{\partial b_i^{[2]}} = \delta_i^{[2]} \cdot 1 = \delta_i^{[2]}$$In vector form:
$$\large \frac{\partial L}{\partial \mathbf{b}^{[2]}} = \delta^{[2]}$$

---

> [!abstract] Key Intuition
> 
> - The **Weight Gradient** is the product of the error at the destination ($\delta^{[2]}$) and the signal coming from the source ($\mathbf{a}^{[1]}$). This is often called the "Delta Rule."
>     
> - The **Bias Gradient** is simply the error at that neuron, as the bias does not have an "incoming signal" to scale it.
>     
