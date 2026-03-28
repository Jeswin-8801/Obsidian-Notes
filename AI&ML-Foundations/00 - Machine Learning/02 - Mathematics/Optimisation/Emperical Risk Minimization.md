### Statistical Framework

In the context of Supervised Learning, let $(\mathcal{X}, \mathcal{Y})$ be the input and output spaces. We assume an unknown joint probability distribution $P(X, Y)$ over $\mathcal{X} \times \mathcal{Y}$.

A model $h \in \mathcal{H}$ (the hypothesis space) is a function $h: \mathcal{X} \to \mathcal{Y}$. To quantify the model's performance, we define a **Loss Function** $L: \mathcal{Y} \times \mathcal{Y} \to \mathbb{R}_{\geq 0}$.

### Risk Definitions

**Expected Risk (Theoretical Risk):**
The true goal is to minimize the expected loss over the entire distribution $P$:
$$\large R(h) = \mathbb{E}_{(x, y) \sim P} [L(h(x), y)] = \int_{\mathcal{X} \times \mathcal{Y}} L(h(x), y) \, dP(x, y)$$
_Problem:_ $P(X, Y)$ is unknown, rendering $R(h)$ uncomputable.

**Empirical Risk:**
Given a training dataset $\mathcal{D} = \{ (x_i, y_i) \}_{i=1}^n$ sampled i.i.d. from $P$, we approximate the integral with a finite sum:
$$\large R_{emp}(h) = \frac{1}{n} \sum_{i=1}^n L(h(x_i), y_i)$$

### The ERM Objective

The **Empirical Risk Minimization (ERM)** principle states that the optimal hypothesis $\hat{h}$ is the one that minimizes the empirical risk on the observed data:
$$\large \hat{h}_{ERM} = \underset{h \in \mathcal{H}}{\arg \min} \left( \frac{1}{n} \sum_{i=1}^n L(h(x_i), y_i) \right)$$

---

### Examples in Machine Learning

|**Algorithm**|**Loss Function L(y^​,y)**|**ERM Objective min∑L**|
|---|---|---|
|**Linear Regression**|Squared Loss: $(\hat{y} - y)^2$|Ordinary Least Squares (OLS)|
|**Support Vector Machine**|Hinge Loss: $\max(0, 1 - y\hat{y})$|Maximum Margin Hyperplane|
|**Logistic Regression**|Log Loss: $-[y\log \hat{y} + (1-y)\log(1-\hat{y})]$|Maximum Likelihood Estimation|

### Theoretical Constraints & Structural Risk

Directly minimizing $R_{emp}$ can lead to **overfitting** (low empirical risk but high expected risk). To combat this, we utilize **Structural Risk Minimization (SRM)**, which adds a regularization penalty $\Omega(h)$:
$$\large R_{srm}(h) = R_{emp}(h) + \lambda \Omega(h)$$

> [!MATH] Generalization Bound
> 
> For a hypothesis space with Vapnik-Chervonenkis (VC) dimension $d$, the relationship between empirical and expected risk is governed by:
> 
> $$R(h) \leq R_{emp}(h) + O\left( \sqrt{\frac{d \log(n/d) + \log(1/\delta)}{n}} \right)$$
> 
> This inequality shows that as $n \to \infty$, the empirical risk converges to the expected risk.