Cholesky decomposition is a specialized, highly efficient version of LU decomposition designed specifically for **Symmetric Positive-Definite (SPD)** matrices. It factorizes a matrix into the product of a lower triangular matrix and its transpose.

---
### Prerequisites

To perform Cholesky decomposition, the matrix $A$ must satisfy:

- **Square:** $A$ is $n \times n$.
- **Symmetric:** $A = A^T$ (for complex matrices, it must be Hermitian: $A = A^H$).
- **Positive-Definite:** For any non-zero vector $x$, $x^T A x > 0$.
    - _Practical Check:_ All eigenvalues must be strictly positive, and all diagonal elements must be positive.

---

### Computational Complexity

Cholesky is the gold standard for speed when its prerequisites are met.

- **Total FLOPs:** $\approx \frac{1}{3}n^3$
- **Big-O Notation:** $O(n^3)$
- **Efficiency:** It requires exactly **half** the additions and multiplications of standard LU decomposition because it exploits the symmetry of the matrix.

---

### When is Cholesky Decomposition Preferred?

- **Optimization:** Solving Normal Equations in Linear Least Squares ($A^T A x = A^T b$).
- **Monte Carlo Simulations:** To transform a vector of uncorrelated random variables into a vector with a specific covariance matrix.
- **Kalman Filters:** Used in robotics and navigation for state estimation.
- **Memory Efficiency:** Since $A$ is symmetric, you only need to store the lower triangle, and the decomposition only produces one triangular matrix $L$.

---

### Example: $A = LL^T$

#### **The Matrix (SPD)**

$$A = \begin{pmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{pmatrix}$$

#### **The Algorithm (Cholesky-Banachiewicz)**

We find the elements of $L$ column by column:

1. **$l_{11} = \sqrt{a_{11}} = \sqrt{4} = 2$**
2. **$l_{21} = \frac{a_{21}}{l_{11}} = \frac{12}{2} = 6$**
3. **$l_{31} = \frac{a_{31}}{l_{11}} = \frac{-16}{2} = -8$**
4. **$l_{22} = \sqrt{a_{22} - l_{21}^2} = \sqrt{37 - 6^2} = \sqrt{1} = 1$**
5. **$l_{32} = \frac{1}{l_{22}}(a_{32} - l_{31}l_{21}) = \frac{1}{1}(-43 - (-8)(6)) = -43 + 48 = 5$**
6. **$l_{33} = \sqrt{a_{33} - (l_{31}^2 + l_{32}^2)} = \sqrt{98 - ((-8)^2 + 5^2)} = \sqrt{98 - (64 + 25)} = \sqrt{9} = 3$**

#### **The Resulting Factor**

$$L = \begin{pmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{pmatrix}$$

Verification: $L \times L^T$ will return original matrix $A$.

---

#LinearAlgebra #Cholesky #Optimization #NumericalMethods
