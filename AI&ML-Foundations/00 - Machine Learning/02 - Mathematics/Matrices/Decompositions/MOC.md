## **1. Eigendecomposition (Spectral Decomposition)**

Applicable to **square matrices** ($n \times n$) that are diagonalizable.
$$\large A = Q \Lambda Q^{-1}$$

- **Components:** $Q$ contains eigenvectors; $\Lambda$ is a diagonal matrix of eigenvalues.
- **Condition:** $A$ must have $n$ linearly independent eigenvectors.
- **Symmetric Case:** If $A$ is symmetric, $Q$ is orthogonal ($Q^T = Q^{-1}$), yielding $A = Q \Lambda Q^T$.

---

## **2. Singular Value Decomposition (SVD)**

The "Swiss Army Knife" of linear algebra. Applicable to **any** $m \times n$ matrix.
$$\large A = U \Sigma V^T$$

- **Components:** $U$ (left singular vectors, basis for Column Space), $\Sigma$ (singular values $\sigma_i$), $V$ (right singular vectors, basis for Row Space).
- **Utility:** Fundamental for Principal Component Analysis (PCA), Moore-Penrose pseudoinverse, and Low-Rank Approximation (Eckart–Young–Mirsky theorem).

---

## **3. LU & PLU Decomposition**

Used primarily for solving linear systems and calculating determinants.
$$\large A = LU \quad \text{or} \quad PA = LU$$

- **Components:** $L$ is lower triangular, $U$ is upper triangular (REF), and $P$ is a permutation matrix (to handle row swaps/pivoting).
- **Utility:** Replaces $Ax = b$ with two triangular systems ($Ly = Pb$ and $Ux = y$), which are solved via forward/backward substitution in $O(n^2)$.

---

## **4. QR Decomposition**

The backbone of the **QR Algorithm** for finding eigenvalues and solving least-squares problems.
$$\large A = QR$$

- **Components:** $Q$ is an orthogonal matrix ($Q^T Q = I$); $R$ is an upper triangular matrix.
- **Methods:** Typically computed via **Gram-Schmidt**, **Householder Reflections**, or **Givens Rotations**.

---

## **5. Cholesky Decomposition**

A specialized, highly efficient version of LU for **Hermitian, Positive-Definite** matrices.
$$\large A = LL^* \quad \text{or} \quad A = R^TR$$

- **Efficiency:** Takes roughly half the flops of LU decomposition because it exploits symmetry.
- **Utility:** Used in Monte Carlo simulations (correlating variables) and Kalman filters.

---

## **6. Polar & Jordan Decompositions**

- **Polar Decomposition:** $A = UP$, where $U$ is unitary and $P$ is positive semi-definite. Analogous to the complex number representation $re^{i\theta}$.
- **Jordan Normal Form:** $A = PJP^{-1}$. The generalization of eigendecomposition for **non-diagonalizable** matrices, using Jordan blocks for deficient eigenvalues.

For an advanced look at the "bread and butter" decompositions used in numerical linear algebra and optimization, these four are essential. They often serve as the preprocessing steps for more complex algorithms like SVD or the QR algorithm.

***
## **7. LDL Decomposition**

A variant of LU for symmetric matrices that avoids the square roots required by Cholesky.

$$A = LDL^T$$

- **Components:** $L$ is unit lower triangular (ones on the diagonal), and $D$ is a diagonal matrix.
- **Advantage:** Works for symmetric matrices that are not necessarily positive-definite (as long as they are non-singular).
- **Use Case:** Optimization algorithms and inertia computation in mechanics.

---
### **Comprehensive Matrix Decomposition Comparison**

| **Decomposition**         | **Form**              | **Matrix Constraints**      | **Complexity (FLOPs)**       | **Primary Use Case**                          |
| ------------------------- | --------------------- | --------------------------- | ---------------------------- | --------------------------------------------- |
| **LU (Partial Pivoting)** | $PA = LU$             | Square, non-singular        | $\frac{2}{3}n^3$             | Solving linear systems $Ax = b$, Determinants |
| **Cholesky**              | $A = LL^T$            | Symmetric Positive-Definite | $\frac{1}{3}n^3$             | Optimization, Kalman Filters, Monte Carlo     |
| **LDL**                   | $A = LDL^T$           | Symmetric                   | $\frac{1}{3}n^3$             | Avoiding square roots in symmetric systems    |
| **QR**                    | $A = QR$              | $m \ge n$ (Full rank)       | $2n^2(m - \frac{n}{3})$      | Linear Least Squares, Eigenvalue algorithms   |
| **Eigendecomposition**    | $A = Q\Lambda Q^{-1}$ | Square, diagonalizable      | $O(n^3)$                     | Powering matrices, Differential equations     |
| **SVD**                   | $A = U\Sigma V^T$     | Any $m \times n$            | $\approx 4m^2n + 8mn^2$      | PCA, Pseudoinverse, Low-rank approximation    |
| **Schur**                 | $A = QUQ^H$           | Square                      | $O(n^3)$                     | Numerical stability in eigenvalue problems    |
| **Jordan Normal Form**    | $A = PJP^{-1}$        | Square (any)                | High (Numerical instability) | Theoretical analysis of deficient matrices    |

---

### **Key Selection Heuristics**

1. **If $A$ is SPD:** Always use **Cholesky**. It is twice as fast as LU and numerically the most stable.
2. **If $A$ is Rectangular:** Use **QR** for least squares or **SVD** if you need the fundamental subspaces (Null space, Column space).
3. **If $A$ is Non-Diagonalizable:** Eigendecomposition will fail; use **Schur Decomposition** for a stable triangular form or **Jordan Normal Form** for theoretical work.
4. **For Stability:** **Householder QR** is generally more stable than LU with partial pivoting, especially for ill-conditioned matrices.

---

#LinearAlgebra #MatrixMath #ComputationalComplexity #NumericalAnalysis