To derive $\delta^{[1]}$, we calculate how the loss $L$ changes with respect to the hidden pre-activations $\mathbf{z}^{[1]}$.

---

### 1. The Path of the Gradient

Using the **Multivariate Chain Rule**, we trace the dependency of the Loss $L$ on $\mathbf{z}^{[1]}$ through the subsequent layers:

$$L \rightarrow \mathbf{a}^{[2]} \rightarrow \mathbf{z}^{[2]} \rightarrow \mathbf{a}^{[1]} \rightarrow \mathbf{z}^{[1]}$$

Mathematically, this is expressed as:

$$\large \frac{\partial L}{\partial \mathbf{z}^{[1]}} = \left( \frac{\partial L}{\partial \mathbf{z}^{[2]}} \cdot \frac{\partial \mathbf{z}^{[2]}}{\partial \mathbf{a}^{[1]}} \right) \cdot \frac{\partial \mathbf{a}^{[1]}}{\partial \mathbf{z}^{[1]}}$$

---

### 2. Computing the Partial Derivatives

#### Part I: The Output Error ($\delta^{[2]}$)

We already know from the previous layer's derivation that:

$$\frac{\partial L}{\partial \mathbf{z}^{[2]}} = \delta^{[2]}$$

#### Part II: The Weight Path ($\frac{\partial \mathbf{z}^{[2]}}{\partial \mathbf{a}^{[1]}}$)

Look at the linear equation for the output layer:

$$\mathbf{z}^{[2]} = \mathbf{W}^{[2]} \mathbf{a}^{[1]} + \mathbf{b}^{[2]}$$

When we differentiate $\mathbf{z}^{[2]}$ with respect to the vector $\mathbf{a}^{[1]}$, the result is the weight matrix itself. However, because we are propagating the error _backward_ into the dimensions of $\mathbf{a}^{[1]}$, we use the **transpose**:

$$\frac{\partial \mathbf{z}^{[2]}}{\partial \mathbf{a}^{[1]}} = (\mathbf{W}^{[2]})^T$$

#### Part III: The Local Activation Derivative ($\frac{\partial \mathbf{a}^{[1]}}{\partial \mathbf{z}^{[1]}}$)

This is the derivative of the hidden activation function (ReLU) with respect to its input:

$$\frac{\partial \mathbf{a}^{[1]}}{\partial \mathbf{z}^{[1]}} = g'(\mathbf{z}^{[1]})$$

---

### 3. Combining and Vectorizing

Now we substitute these three parts back into our chain rule equation.

1. First, we compute the "pushed back" error:
    
    $$\text{Error at } \mathbf{a}^{[1]} = (\mathbf{W}^{[2]})^T \delta^{[2]}$$
    
2. Then, we apply the local gradient of the activation function. Since each neuron's activation only depends on its own pre-activation, this is an **element-wise multiplication** ($\odot$):
    

> [!abstract] Final Derivation
> 
> $$\large \delta^{[1]} = \left( (\mathbf{W}^{[2]})^T \delta^{[2]} \right) \odot g'(\mathbf{z}^{[1]})$$

---

### 4. Dimensionality Verification

For our **[2, 3, 2]** architecture, let's ensure the matrix math holds up:

|**Operation**|**Dimensions**|**Resulting Shape**|**Match δ[1]?**|
|---|---|---|---|
|$(\mathbf{W}^{[2]})^T \in \mathbb{R}^{3 \times 2}$|$(3 \times 2)$|—|—|
|$\delta^{[2]} \in \mathbb{R}^{2 \times 1}$|$(2 \times 1)$|—|—|
|**Matrix Product**|$(3 \times 2) \times (2 \times 1)$|$3 \times 1$|—|
|**Element-wise $\odot$**|$(3 \times 1) \odot (3 \times 1)$|**$3 \times 1$**|**Yes**|

---

### Implementation Note

In your code, the term $g'(\mathbf{z}^{[1]})$ for **ReLU** is computed as:

```python
# ReLU derivative: 1 if z > 0, else 0
d_relu = (z1 > 0).astype(float)
delta1 = np.dot(W2.T, delta2) * d_relu
```
