### The Manhattan Distance
Calculates the sum of the absolute differences of their Cartesian coordinates.
$$\large d_1(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_1 = \sum_{i=1}^n |p_i - q_i| $$
-   $\mathbf{p}, \mathbf{q} \in \mathbb{R}^n$
-   $p_i, q_i$: the $i \text{-th}$ coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.

***

### The Manhattan Norm ($L_1$ Norm)

In an $n$-dimensional vector space $\mathbb{R}^n$, the $L_1$ norm (also known as the taxicab or Manhattan norm) of a vector $\mathbf{x} = [x_1, x_2, \dots, x_n]^T$ is defined as the sum of the absolute values of its components:

$$\large \|\mathbf{x}\|_1 = \sum_{i=1}^n |x_i| $$

> Refer: [[Norms and Lp#Geometry of the $L_1$ Unit Ball|Geometry of the L1 Norm]]

---

### Optimization and Sparsity

In the context of regularized empirical risk minimization, the $L_1$ penalty is employed to induce sparsity in the solution vector $\mathbf{w}^*$. 

Consider the objective:
$$\large \min_{\mathbf{w}} \mathcal{L}(\mathbf{w}) + \lambda \|\mathbf{w}\|_1 $$

- **Singularity at the Origin:** The function $f(x) = |x|$ is non-differentiable at $x=0$. Its subdifferential is given by:
  $\partial |x| = \begin{cases} \{1\} & x > 0 \\ \{-1\} & x < 0 \\ [-1, 1] & x = 0 \end{cases}$

- **Geometric Interpretation:** The level sets of a smooth loss function $\mathcal{L}(\mathbf{w})$ are typically ellipsoidal. Due to the "pointed" nature of the $L_1$ ball at the axes (where $w_i = 0$ for some $i$), the constrained optimum $\mathbf{w}^*$ is statistically likely to occur at a vertex of the $L_1$ polytope.

- **Feature Selection:** This property effectively performs automatic feature selection by driving coefficients of irrelevant features to exactly zero, distinguishing it from the $L_2$ norm which only asymptotically approaches zero.

For further details on the comparison with other norms, refer to [[Norms and Lp]].