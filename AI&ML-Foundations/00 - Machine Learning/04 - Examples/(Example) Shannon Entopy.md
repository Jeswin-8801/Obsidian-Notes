
> Use the dataset: [[Binary Classification Dataset with 3 Features]]

Consider a target vector $\mathbf{y}$ from a dataset $\mathcal{D}$ with $n=5$ samples:

$$\mathbf{y} = [1, 0, 1, 1, 0]^\top$$

**Step 1: Compute Empirical Probabilities**

Let $n_1$ be the count of class 1 and $n_0$ be the count of class 0.

$$p(1) = \frac{n_1}{n} = \frac{3}{5} = 0.6$$

$$p(0) = \frac{n_0}{n} = \frac{2}{5} = 0.4$$

**Step 2: Apply Entropy Formula**

Using base $b=2$:

$$H(\mathbf{y}) = - \sum_{i \in \{0, 1\}} p(i) \log_2 p(i)$$

$$H(\mathbf{y}) = - [0.6 \log_2(0.6) + 0.4 \log_2(0.4)]$$

**Numerical Approximation:**

$$\log_2(0.6) \approx -0.737, \quad \log_2(0.4) \approx -1.322$$

$$H(\mathbf{y}) \approx - [0.6(-0.737) + 0.4(-1.322)]$$

$$H(\mathbf{y}) \approx - [-0.4422 - 0.5288] = 0.971 \text{ bits}$$
