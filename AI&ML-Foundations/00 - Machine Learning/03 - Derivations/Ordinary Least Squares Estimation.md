
## Scalar Form

### Objective Function
The Sum of Squared Residuals (SSR) is defined as:
$$\large S(\hat{\beta}_0, \hat{\beta}_1) = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i)^2 $$

### Compute Partial Derivatives
To minimize $S$, we compute the partial derivatives with respect to $\hat{\beta}_0$ and $\hat{\beta}_1$ and set them to zero:
--- start-multi-column: Compute Partial Derivative
```column-settings
number of columns:2
```

#####  $\hat{\beta}_0$

$\frac{\partial S}{\partial \hat{\beta}_0} = -2 \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$

--- end-column ---

#####  $\hat{\beta}_1$

$\frac{\partial S}{\partial \hat{\beta}_1} = -2 \sum_{i=1}^{n} x_i (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$

--- end-multi-column

### Derivation of the Normal Equations
--- start-multi-column: Derivation of Normal Equations
```column-settings
number of columns:2
```

#####  $\hat{\beta}_0$

Given:
$-2 \sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$

- *Divide by $-2$:*
$\sum_{i=1}^{n} (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$
- *Distribute the summation:*
$\sum_{i=1}^{n} y_i - \sum_{i=1}^{n} \hat{\beta}_0 - \sum_{i=1}^{n} \hat{\beta}_1 x_i = 0$
- *Apply summation properties ($\sum_{i=1}^n c = nc$):*
$\sum_{i=1}^{n} y_i - n\hat{\beta}_0 - \hat{\beta}_1 \sum_{i=1}^{n} x_i = 0$

*Rearrange terms:*
> $\large \sum_{i=1}^{n} y_i = n\hat{\beta}_0 + \hat{\beta}_1 \sum_{i=1}^{n} x_i$

--- end-column ---

#####  $\hat{\beta}_1$

Given:
$-2 \sum_{i=1}^{n} x_i (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$

- *Divide by $-2$:*
$\sum_{i=1}^{n} x_i (y_i - \hat{\beta}_0 - \hat{\beta}_1 x_i) = 0$
- *Distribute $x_i$ within the summation:*
$\sum_{i=1}^{n} (x_i y_i - \hat{\beta}_0 x_i - \hat{\beta}_1 x_i^2) = 0$
- *Distribute the summation and factor out constants:*
$\sum_{i=1}^{n} x_i y_i - \hat{\beta}_0 \sum_{i=1}^{n} x_i - \hat{\beta}_1 \sum_{i=1}^{n} x_i^2 = 0$

*Rearrange terms:*
> $\large \sum_{i=1}^{n} x_i y_i = \hat{\beta}_0 \sum_{i=1}^{n} x_i + \hat{\beta}_1 \sum_{i=1}^{n} x_i^2$

--- end-multi-column

### Rearrange to get $\hat{\beta}_0$ and $\hat{\beta}_1$
--- start-multi-column: Rearrange
```column-settings
number of columns:2
```

#####  $\hat{\beta}_0$

From the first normal equation:
$n\hat{\beta}_0 = \sum_{i=1}^{n} y_i - \hat{\beta}_1 \sum_{i=1}^{n} x_i$

- *divide by $n$*
$\hat{\beta}_0 = \frac{1}{n} \sum_{i=1}^{n} y_i - \hat{\beta}_1 \frac{1}{n} \sum_{i=1}^{n} x_i$

we know $\bar{y} = \frac{1}{n} \sum y_i$ and $\bar{x} = \frac{1}{n} \sum x_i$
> $\large \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$

--- end-column ---

#####  $\hat{\beta}_1$

Substituting $\hat{\beta}_0$ obtained to the left into the second normal equation:
$\sum x_i y_i = (\bar{y} - \hat{\beta}_1 \bar{x}) \sum x_i + \hat{\beta}_1 \sum x_i^2$
$\sum x_i y_i = \bar{y} \sum x_i - \hat{\beta}_1 \bar{x} \sum x_i + \hat{\beta}_1 \sum x_i^2$
$\sum x_i y_i - n\bar{x}\bar{y} = \hat{\beta}_1 (\sum x_i^2 - n\bar{x}^2)$

Applying the identities:
- $\sum (x_i - \bar{x})(y_i - \bar{y}) = \sum x_i y_i - n\bar{x}\bar{y}$
- $\sum (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2$

The closed-form solution for the slope is:
> $\large \hat{\beta}_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$

--- end-multi-column

> $$\large\hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x}$$

> $$\large \hat{\beta}_1 = \frac{Cov(X, Y)}{Var(X)} $$


## Matrix Form

### Matrix Form Objective Function
The cost function $S(\beta)$ is defined as the squared Euclidean norm of the residual vector:
$\large S(\beta) = \|y - X\beta\|^2 = (y - X\beta)^T (y - X\beta)$

### Parameter Definitions
- $y \in \mathbb{R}^{n \times 1}$: Vector of observed dependent variables.
- $X \in \mathbb{R}^{n \times p}$: Design matrix of independent variables, where $n$ is the number of observations and $p$ is the number of predictors (including the constant).
- $\beta \in \mathbb{R}^{p \times 1}$: Vector of unknown population parameters.
- $\hat{\beta} \in \mathbb{R}^{p \times 1}$: Vector of OLS point estimators.
- $\epsilon = y - X\beta$: Vector of stochastic disturbances or residuals.

### Expansion of the Quadratic Form
The Sum of Squared Residuals in matrix notation:
$S(\beta) = (y - X\beta)^T (y - X\beta)$
$S(\beta) = y^T y - y^T X\beta - \beta^T X^T y + \beta^T X^T X \beta$

Given that $\beta^T X^T y$ is a scalar, $\beta^T X^T y = (y^T X\beta)^T = y^T X\beta$:
$S(\beta) = y^T y - 2\beta^T X^T y + \beta^T X^T X \beta$

### First-Order Condition
The gradient with respect to the vector $\beta$ is set to the null vector:
$\large \nabla_{\beta} S(\beta) = \frac{\partial}{\partial \beta} (y^T y - 2\beta^T X^T y + \beta^T X^T X \beta) = 0$

Applying matrix differentiation identities:
- $\frac{\partial (a^T \beta)}{\partial \beta} = a$
- $\frac{\partial (\beta^T A \beta)}{\partial \beta} = (A + A^T)\beta$

$-2X^T y + (X^T X + (X^T X)^T)\beta = 0$
$-2X^T y + 2X^T X \beta = 0$

### Normal Equation
$X^T X \hat{\beta} = X^T y$

### Closed-Form Solution
Assuming $X^T X$ is non-singular (full column rank):
> $$\large \hat{\beta} = (X^T X)^{-1} X^T y$$