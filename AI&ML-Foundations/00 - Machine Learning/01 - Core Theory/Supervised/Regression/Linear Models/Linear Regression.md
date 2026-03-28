
***

Linear Regression models the linear relationship between a dependent variable $y$ and an independent variable $x$. The model is expressed as:

$$y = \beta_0 + \beta_1x + \epsilon$$

Where $\beta_0$ is the intercept, $\beta_1$ is the slope, and $\epsilon$ is the error term. Our objective is to estimate $\beta_0$ and $\beta_1$ from data, yielding the predicted line:

$$\hat{y} = \hat{\beta}_0 + \hat{\beta}_1x$$

### 1. Dataset

Consider the following dataset:

| x (Hours Studied) | y (Exam Scores) |
|---|---|
| 1 | 15 |
| 2 | 12 |
| 3 | 25 |
| 4 | 22 |
| 5 | 38 |
| 6 | 32 |
| 7 | 45 |
| 8 | 55 |
| 9 | 48 |
| 10 | 60 |

For this dataset, $n=10$.
Summary statistics:
$\sum x = 55$
$\sum y = 352$
$\sum x^2 = 385$
$\sum xy = 2371$
$\bar{x} = 5.5$
$\bar{y} = 35.2$

```plotly
{ "data": [ { "x": [15, 12, 25, 22, 38, 32, 45, 55, 48, 60], "type": "box", "name": "Exam Spread", "boxpoints": "all", "jitter": 0.3, "pointpos": -1.8, "marker": { "color": "#7b58ad" }, "line": { "color": "#7b58ad" }, "orientation": "h" } ], "layout": { "title": "Statistical Spread of Exam Scores", "xaxis": { "title": "Score Value" }, "yaxis": { "showticklabels": false }, "template": "plotly_dark", "height": 400 } }
```

### 2. Ordinary Least Squares (OLS) Estimators

The OLS method minimizes the Sum of Squared Residuals (SSR):

$$SSR = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \sum_{i=1}^{n} (y_i - (\hat{\beta}_0 + \hat{\beta}_1x_i))^2$$

The estimators for $\hat{\beta}_0$ and $\hat{\beta}_1$ are derived by setting the partial derivatives of $SSR$ with respect to $\hat{\beta}_0$ and $\hat{\beta}_1$ to zero.

#### Scalar Form:

The [[Ordinary Least Squares Estimation#Scalar Form|OLS Estimators]] are given by:

$$\hat{\beta}_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} = \frac{n(\sum xy) - (\sum x)(\sum y)}{n(\sum x^2) - (\sum x)^2}$$

$$\hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}$$

**Calculations:**

$$\hat{\beta}_1 = \frac{10(2371) - (55)(352)}{10(385) - (55)^2} = \frac{23710 - 19360}{3850 - 3025} = \frac{4350}{825} = \frac{58}{11} \approx 5.2727$$

$$\hat{\beta}_0 = 35.2 - \left(\frac{58}{11}\right)(5.5) = \frac{352}{10} - \frac{58}{11} \cdot \frac{55}{10} = \frac{352}{10} - \frac{290}{10} = \frac{62}{10} = 6.2$$

The fitted regression line is:

$$\hat{y} = 6.2 + \frac{58}{11}x \approx 6.2 + 5.27x$$

#### Matrix Form:

For a linear model $y = X\beta + \epsilon$, where $y$ is the $n \times 1$ response vector, $X$ is the $n \times (p+1)$ design matrix (for simple linear regression, $p=1$, so $X$ is $n \times 2$), $\beta$ is the $(p+1) \times 1$ coefficient vector, and $\epsilon$ is the $n \times 1$ error vector.

$$X = \begin{pmatrix} 1 & x_1 \\ 1 & x_2 \\ \vdots & \vdots \\ 1 & x_n \end{pmatrix}, \quad y = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix}, \quad \beta = \begin{pmatrix} \beta_0 \\ \beta_1 \end{pmatrix}$$

The [[Ordinary Least Squares Estimation#Matrix Form|OLS estimator]] for $\beta$ is:

$$\hat{\beta} = (X^T X)^{-1} X^T y$$

**Calculations:**

$$X^T X = \begin{pmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{pmatrix} = \begin{pmatrix} 10 & 55 \\ 55 & 385 \end{pmatrix}$$

$$(X^T X)^{-1} = \frac{1}{10 \cdot 385 - 55^2} \begin{pmatrix} 385 & -55 \\ -55 & 10 \end{pmatrix} = \frac{1}{825} \begin{pmatrix} 385 & -55 \\ -55 & 10 \end{pmatrix}$$

$$X^T y = \begin{pmatrix} \sum y_i \\ \sum x_i y_i \end{pmatrix} = \begin{pmatrix} 352 \\ 2371 \end{pmatrix}$$

$$\hat{\beta} = \frac{1}{825} \begin{pmatrix} 385 & -55 \\ -55 & 10 \end{pmatrix} \begin{pmatrix} 352 \\ 2371 \end{pmatrix} = \frac{1}{825} \begin{pmatrix} 385 \cdot 352 - 55 \cdot 2371 \\ -55 \cdot 352 + 10 \cdot 2371 \end{pmatrix}$$

$$\hat{\beta} = \frac{1}{825} \begin{pmatrix} 135520 - 130405 \\ -19360 + 23710 \end{pmatrix} = \frac{1}{825} \begin{pmatrix} 5115 \\ 4350 \end{pmatrix} = \begin{pmatrix} 5115/825 \\ 4350/825 \end{pmatrix} = \begin{pmatrix} 6.2 \\ 58/11 \end{pmatrix}$$

This confirms the scalar results.

### 3. Goodness of Fit: Coefficient of Determination ($R^2$)

The coefficient of determination, $R^2$, measures the proportion of the variance in the dependent variable that is predictable from the independent variable(s).

**Total Sum of Squares (SST):** Measures the total variation in $y$.
$$SST = \sum_{i=1}^{n} (y_i - \bar{y})^2$$

**Explained Sum of Squares (SSE):** Measures the variation in $y$ explained by the regression model.
$$SSE = \sum_{i=1}^{n} (\hat{y}_i - \bar{y})^2$$

**Residual Sum of Squares (SSR):** Measures the unexplained variation in $y$.
$$SSR = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

The relationship between these sums is:

$$SST = SSE + SSR$$

The $R^2$ value is defined as:

$$R^2 = 1 - \frac{SSR}{SST} = \frac{SSE}{SST}$$

**Calculations:**

$\sum y^2 = 15^2+12^2+25^2+22^2+38^2+32^2+45^2+55^2+48^2+60^2 = 14900$

$$SST = \sum y_i^2 - n\bar{y}^2 = 14900 - 10(35.2)^2 = 14900 - 10(1239.04) = 14900 - 12390.4 = 2509.6$$

$$SSR = \sum y_i^2 - \hat{\beta}_0 \sum y_i - \hat{\beta}_1 \sum x_i y_i$$
$$SSR = 14900 - (6.2)(352) - \left(\frac{58}{11}\right)(2371)$$
$$SSR = 14900 - 2182.4 - \frac{137518}{11} = 14900 - 2182.4 - 12501.63636... \approx 215.9636$$

$$R^2 = 1 - \frac{215.9636}{2509.6} \approx 1 - 0.08605 = 0.91395$$

An $R^2$ of approximately $0.914$ indicates that about $91.4\%$ of the variance in $y$ can be explained by the linear relationship with $x$.

### 4. Standard Errors of Coefficients

The standard errors of the estimated coefficients provide a measure of their precision.

**Estimated Error Variance ($\hat{\sigma}^2$):**
$$\hat{\sigma}^2 = \frac{SSR}{n-2}$$

**Calculations:**
$$\hat{\sigma}^2 = \frac{215.9636}{10-2} = \frac{215.9636}{8} \approx 26.99545$$

**Variance of $\hat{\beta}_1$:**
$$Var(\hat{\beta}_1) = \frac{\hat{\sigma}^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}$$
Note that $\sum (x_i - \bar{x})^2 = \sum x_i^2 - n\bar{x}^2 = 385 - 10(5.5)^2 = 385 - 302.5 = 82.5$.

$$Var(\hat{\beta}_1) = \frac{26.99545}{82.5} \approx 0.327217$$
$$SE(\hat{\beta}_1) = \sqrt{Var(\hat{\beta}_1)} \approx \sqrt{0.327217} \approx 0.5720$$

**Variance of $\hat{\beta}_0$:**
$$Var(\hat{\beta}_0) = \hat{\sigma}^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2} \right)$$

$$Var(\hat{\beta}_0) = 26.99545 \left( \frac{1}{10} + \frac{(5.5)^2}{82.5} \right) = 26.99545 \left( 0.1 + \frac{30.25}{82.5} \right)$$
$$Var(\hat{\beta}_0) = 26.99545 (0.1 + 0.36666...) \approx 26.99545 (0.46666) \approx 12.5978$$
$$SE(\hat{\beta}_0) = \sqrt{Var(\hat{\beta}_0)} \approx \sqrt{12.5978} \approx 3.5493$$

### 5. Graph

Here's the plot of the data points and the fitted regression line:

```plotly
{ "data": [ { "x": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [15, 12, 25, 22, 38, 32, 45, 55, 48, 60], "type": "scatter", "mode": "markers", "name": "Actual Scores", "marker": { "color": "#7b58ad", "size": 12, "opacity": 0.7 } }, { "x": [1, 10], "y": [12.03, 58.17], "type": "scatter", "mode": "lines", "name": "Fitted Regression", "line": { "color": "#ff6347", "width": 3, "dash": "dash" } } ], "layout": { "title": "Impact of Study Time on Exam Results", "xaxis": { "title": "Hours Studied" }, "yaxis": { "title": "Exam Score (%)", "range": [0, 70] }, "template": "plotly_dark" } }
```