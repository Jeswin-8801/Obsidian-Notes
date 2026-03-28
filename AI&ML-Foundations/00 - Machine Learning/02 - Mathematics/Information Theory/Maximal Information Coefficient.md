## Formal Definition

The **Maximal Information Coefficient (MIC)** belongs to a class of maximal information-based nonparametric exploration (MINE) statistics. It is designed to capture a wide range of functional and non-functional relationships between two variables $X$ and $Y$ while satisfying the property of **Equitability**.

**Definition:**

For a grid $G$ of $x$ columns and $y$ rows, let $I|_{G}$ denote the mutual information of the data discretized by $G$. The characteristic matrix $M(X,Y)$ is defined as:

$$M(X,Y)_{x,y} = \frac{\max_G I|_{G}}{\log_b(\min\{x,y\})}$$

The MIC is the maximum value in the characteristic matrix over all grids satisfying $xy < B(n)$:

$$MIC(X,Y) = \max_{xy < B(n)} \{ M(X,Y)_{x,y} \}$$

Where $B(n)$ is a function of sample size $n$, typically $B(n) = n^{0.6}$.

## Properties

- **Generality:** Captures linear, exponential, periodic, and non-functional (e.g., sinusoidal or circular) relationships.
- **Equitability:** Assigns similar scores to relationships with similar noise levels, regardless of the relationship type.
- **Range:** $MIC \in [0, 1]$.
    - $MIC \to 0$: Statistical independence.
    - $MIC \to 1$: Noiseless functional relationship.

---

#### 3. Calculation Example (Non-Linear Association)

> Find the example problem at: [[(Example) Maximal Information Coefficient]]

---

#### 4. Implementation Context

In the ML pipeline, MIC is utilized for **Feature Discovery**.

- **Use Case:** When $I(X;Y)$ is sensitive to the choice of bins in discretization, MIC automates this by maximizing over all possible binnings.
    
- **Comparison:** Unlike **Pearson Correlation**, which only detects linear trends, or **Spearman**, which only detects monotonic trends, MIC detects any structure that can be represented on a 2D plane.
    

> [!TIP] Obsidian Link
> 
> Relates to: [[Mutual Information and Joint Entropy]] for the underlying MI calculation and [[Pearson Correlation]] for the linear contrast.