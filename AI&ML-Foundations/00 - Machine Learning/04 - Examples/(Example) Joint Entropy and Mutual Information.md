
Consider a dataset $\mathcal{D}$ with $n=5$ samples. Let $X$ be a binary feature and $Y$ be the target.

$\mathbf{X} = [1, 0, 1, 1, 0]^\top$

$\mathbf{Y} = [1, 1, 1, 0, 0]^\top$

**Step 1: Joint Probability Distribution $p(x, y)$**

Count occurrences $n_{x,y}$:

- $(0,0): 1$ (index 5) $\implies p(0,0) = 0.2$
    
- $(0,1): 1$ (index 2) $\implies p(0,1) = 0.2$
    
- $(1,0): 1$ (index 4) $\implies p(1,0) = 0.2$
    
- $(1,1): 2$ (indices 1, 3) $\implies p(1,1) = 0.4$
    

**Step 2: Marginal Probabilities**

$p(X=0) = 0.4, \quad p(X=1) = 0.6$

$p(Y=0) = 0.4, \quad p(Y=1) = 0.6$

**Step 3: Entropy Calculations ($b=2$)**

- $H(X) = -(0.4 \log_2 0.4 + 0.6 \log_2 0.6) \approx 0.971$
    
- $H(Y) = -(0.4 \log_2 0.4 + 0.6 \log_2 0.6) \approx 0.971$
    
- **Joint Entropy:**
    
    $$H(X, Y) = - [3(0.2 \log_2 0.2) + 0.4 \log_2 0.4]$$
    
    $$H(X, Y) = - [3(-0.464) - 0.529] = 1.921 \text{ bits}$$
    

**Step 4: Mutual Information**

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

$$I(X; Y) = 0.971 + 0.971 - 1.921 = 0.021 \text{ bits}$$