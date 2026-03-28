## Joint Entropy

Let $(X, Y)$ be a pair of discrete random variables with a joint probability mass function $p(x, y)$. The **Joint Entropy** $H(X, Y)$ measures the total uncertainty of the system $(X, Y)$.

**Formal Definition:**

$$H(X, Y) = - \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log_b p(x, y)$$

**Relation to Marginal Entropy:**

If $X$ and $Y$ are independent, $H(X, Y) = H(X) + H(Y)$.

Otherwise, $H(X, Y) \leq H(X) + H(Y)$.

---

## Mutual Information

**Mutual Information** $I(X; Y)$ quantifies the reduction in uncertainty of $X$ due to the knowledge of $Y$. It is the Kullback-Leibler divergence between the joint distribution and the product of the marginals.

**Formal Definition:**

$$I(X; Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x, y) \log_b \left( \frac{p(x, y)}{p(x)p(y)} \right)$$

**Set-Theoretic Identities:**

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

$$I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$$

---

#### 3. Calculation Example (Feature-Target Interaction)

> Find the example problem at: [[(Example) Joint Entropy and Mutual Information]]

---

#### 4. Implementation Context

In Machine Learning, $I(X; Y)$ serves as a **filter-based feature selection** metric. A high $I(X; Y)$ indicates that feature $X$ shares significant information with target $Y$, making it a candidate for predictive modeling. Unlike correlation, MI captures non-linear dependencies.