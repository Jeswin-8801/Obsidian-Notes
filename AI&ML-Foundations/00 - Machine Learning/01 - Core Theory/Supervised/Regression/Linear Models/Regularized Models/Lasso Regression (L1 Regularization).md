### Regularization

**Regularization** is the introduction of an additional constraint or penalty term $\mathcal{R}(f)$ to the [[Emperical Risk Minimization]] objective function. For a model with parameters $\mathbf{w} \in \mathbb{R}^d$, the regularized objective is:
$$\large \min_{\mathbf{w}} \left\{ \mathcal{L}(\mathbf{y}, X\mathbf{w}) + \lambda \mathcal{R}(\mathbf{w}) \right\}$$
Where:
- $\mathcal{L}$ is the loss function (e.g., Mean Squared Error).
- $\lambda \in [0, \infty)$ is the hyperparameter controlling the trade-off between bias and variance.
- Purpose: To constrain the hypothesis space $\mathcal{H}$ and prevent overfitting by penalizing high-complexity parameter vectors.

---

### Lasso Regression (Least Absolute Shrinkage and Selection Operator)

Lasso is a linear regression variant utilizing a **Laplace prior** on the coefficients. It is defined as an optimization problem minimizing the Residual Sum of Squares (RSS) subject to an $\|\cdot\|_1$ constraint.

**Objective Function:**

$$\large \hat{\mathbf{w}}_{Lasso} = \underset{\mathbf{w}}{\arg \min} \left( \frac{1}{2n} \|\mathbf{y} - X\mathbf{w}\|_2^2 + \lambda \|\mathbf{w}\|_1 \right)$$
Where the $L_1$ norm is defined as:
$$\|\mathbf{w}\|_1 = \sum_{j=1}^{d} |w_j|$$

---

### The $L_1$ Regularization Identity

Lasso is termed **$L_1$ Regularization** because the penalty term is the **Taxicab Norm** (Manhattan distance) of the weight vector.

**Geometric Interpretation of Sparsity:**

Consider the constrained optimization form (Karush-Kuhn-Tucker conditions):
$$\large \min_{\mathbf{w}} \frac{1}{2n} \|\mathbf{y} - X\mathbf{w}\|_2^2 \quad \text{subject to} \quad \sum_{j=1}^{d} |w_j| \leq t$$

The constraint region $\mathcal{B}_1 = \{\mathbf{w} : \|\mathbf{w}\|_1 \leq t\}$ is a **polytope** (a diamond in $\mathbb{R}^2$).

1. The contours of the quadratic loss function are ellipsoids.
2. The solution occurs at the first point of contact between the loss ellipsoid and the $L_1$ polytope.
3. Due to the "pointy" nature of the $L_1$ ball at the axes, the intersection frequently occurs at a vertex where one or more $w_j = 0$.

---

#### 4. Calculation Example (Sparsity Induction)

Let $n=2$ and $d=2$. Assume $X = I$ (Identity matrix) and $\mathbf{y} = [y_1, y_2]^\top$.

The objective for a single coefficient $w_j$:

$$f(w_j) = \frac{1}{2}(y_j - w_j)^2 + \lambda |w_j|$$

Taking the sub-gradient $\partial_{w_j}$ and setting to zero:

$$0 \in -(y_j - w_j) + \lambda \cdot \text{sgn}(w_j)$$

**The Soft-Thresholding Operator:**

$$\hat{w}_j = S_\lambda(y_j) = \text{sgn}(y_j) \max(|y_j| - \lambda, 0)$$

**Numerical Case:**

Let $y_1 = 0.5$, $y_2 = 2.0$, and $\lambda = 1.0$.

- For $w_1$: $|0.5| < 1.0 \implies \hat{w}_1 = 0$
    
- For $w_2$: $|2.0| > 1.0 \implies \hat{w}_2 = (2.0 - 1.0) = 1.0$
    

**Result:** $\hat{\mathbf{w}} = [0, 1]^\top$. Feature $x_1$ is eliminated (Automatic Feature Selection).

---

#### 5. Implementation Context

- **Lasso:** $L_1$ penalty $\implies$ Sparse solutions (Feature Selection).
    
- **Ridge:** $L_2$ penalty $\implies$ Small weights (No sparsity).
    
- **Elastic Net:** $\lambda_1 \|\mathbf{w}\|_1 + \lambda_2 \|\mathbf{w}\|_2^2$ (Hybrid approach).
    

> [!MATH] Optimization Note
> 
> Unlike Ridge Regression, Lasso does not have a closed-form solution (like the Normal Equation) because the $L_1$ norm is non-differentiable at $w_j = 0$. It is solved via **Coordinate Descent** or **Proximal Gradient Methods**.

How should we link this to your **Optimization & Sparsity** note?