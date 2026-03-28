#### Formal Definition

Let $X$ be a discrete random variable with a finite alphabet $\mathcal{X}$ and probability mass function $p(x) = P(X=x)$. The **Shannon Entropy** $H(X)$, representing the average uncertainty or expected information content, is defined as:

$$\large H(X) = \mathbb{E}[I(X)] = -\sum_{x \in \mathcal{X}} p(x) \log_b p(x)$$

Where:

- $I(x) = -\log_b p(x)$ is the self-information (surprisal) of outcome $x$.
- If $b=2$, entropy is measured in **bits**.
- By convention, $0 \log 0 = 0$ (justified by $\lim_{p \to 0^+} p \log p = 0$).

#### Properties

- **Non-negativity:** $H(X) \geq 0$.
- **Extremality:** $H(X)$ is maximized when $p(x)$ is a uniform distribution, $p(x) = \frac{1}{|\mathcal{X}|}$, yielding $H(X) = \log |\mathcal{X}|$.
- **Concavity:** $H(p)$ is a concave function of the distribution $p$.

---

#### 3. Calculation Example (Binary Classification Dataset)

> Find the example problem at: [[(Example) Shannon Entopy]]

---

#### 4. Implementation Context

Shannon Entropy is used to compute **Information Gain** $IG(T, a)$.
