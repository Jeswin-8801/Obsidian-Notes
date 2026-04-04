## Prerequisites
To fully grasp SVD, the following concepts are assumed:

- **The Spectral Theorem:** Any positive semi-definite (PSD) matrix $A^*A$ is orthogonally diagonalizable with non-negative eigenvalues.
- **Rank-Nullity Theorem**
- **Inner Product Spaces:** The geometry of adjoint operators and orthogonality in $\mathbb{C}^n$ or $\mathbb{R}^n$.

---

## The Fundamental Theorem

Let $A \in \mathbb{C}^{m \times n}$ with $\text{rank}(A) = r$. There exist unitary matrices $U$ and $V$ such that:
$$\large A = U \Sigma V^*$$

### Components:

1. **$U \in \mathbb{C}^{m \times m}$:** A unitary matrix whose columns are the **left singular vectors** (eigenvectors of $AA^*$).
2. **$\Sigma \in \mathbb{R}^{m \times n}$:** A diagonal matrix (rectangular) containing $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_r > 0$, where $\sigma_i$ are the **singular values**.
3. **$V \in \mathbb{C}^{n \times n}$:** A unitary matrix whose columns are the **right singular vectors** (eigenvectors of $A^*A$).

---

## Matrix Properties via SVD

- **Rank:** The number of non-zero singular values.
- **Euclidean Norm:** $\|A\|_2 = \sigma_{\max}$.
- **Frobenius Norm:** $\|A\|_F = \sqrt{\sigma_1^2 + \dots + \sigma_r^2}$.
- **Condition Number:** $\kappa(A) = \sigma_{\max} / \sigma_{\min}$ (measures sensitivity to noise).
- **Pseudo-inverse:** $A^+ = V \Sigma^+ U^*$, where $\Sigma^+$ is the transpose of $\Sigma$ with $1/\sigma_i$ on the diagonal.\

---


> [!NOTE] Example
> [[(Example) Singular Value Decomposition (SVD)]]
