
Consider a dataset $\mathcal{D}$ with $n=5$ where $Y$ is a deterministic but non-linear function of $X$ (e.g., $y = x^2$ centered), making linear correlation ($\rho$) ineffective.

|**i**|**X**|**Y=f(X)**|
|---|---|---|
|1|-2|4|
|2|-1|1|
|3|0|0|
|4|1|1|
|5|2|4|

**Step 1: Correlation Analysis ($\rho$)**

$$\bar{X} = 0, \quad \bar{Y} = 2$$

$$\text{Cov}(X,Y) = \frac{1}{5} \sum (x_i - 0)(y_i - 2) = \frac{1}{5}[(-2)(2) + (-1)(-1) + (0)(-2) + (1)(-1) + (2)(2)] = 0$$

$$\rho_{X,Y} = 0 \implies \text{Linear correlation fails to detect the dependency.}$$

**Step 2: MIC Heuristic**

MIC searches for the optimal grid $G$ that maximizes normalized Mutual Information.

1. Partitioning $X$ and $Y$ into a $2 \times 2$ grid (thresholding at $X=0$ and $Y=1$).
    
2. The grid yields high $I|_G$ because knowing which side of the $X$-axis a point falls on (in a more complex set) or the concentration of $Y$ values significantly reduces uncertainty.
    
3. For this noiseless quadratic, as $n \to \infty$ and $G$ optimizes:
    $$\large MIC(X,Y) \to 1.0$$