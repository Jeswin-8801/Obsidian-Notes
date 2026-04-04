LU Decomposition factors a square matrix $A$ into the product of a **Lower Triangular** matrix $L$ and an **Upper Triangular** matrix $U$. It is essentially the algebraic "recording" of the Gaussian Elimination process.

---

### Prerequisites

To perform or understand LU decomposition, the following must be true:

- **Square Matrix:** $A$ must be $n \times n$.
- **Invertibility:** $A$ should ideally be non-singular (determinant $\neq 0$).
- **Pivoting Knowledge:** Understanding of elementary row operations.
- **Non-zero Minors:** For a basic $A = LU$ (without row swaps), all leading principal minors of $A$ must be non-zero.

---

### Computational Complexity

The cost of LU decomposition is dominated by the elimination steps:

- **Total FLOPs:** $\approx \frac{2}{3}n^3$
- **Big-O Notation:** $O(n^3)$
- **Back/Forward Substitution:** Once $L$ and $U$ are found, solving for a specific $b$ vector costs only $O(n^2)$.

---

### When is LU Decomposition Preferred?

- **Multiple Right-Hand Sides:** When you need to solve $Ax = b$ for many different $b$ vectors but the same $A$. You decompose $A$ once ($O(n^3)$) and solve each $b$ in $O(n^2)$.
- **Iterative Refinement:** Used to improve the precision of a solution to a linear system.
- **Matrix Inversion:** LU is the standard method for computing $A^{-1}$ by solving $Ax = e_i$ for each standard basis vector.
- **Determinant Calculation:** $\det(A) = \det(L)\det(U)$. Since $\det(L)=1$ (by convention) and $U$ is triangular, $\det(A) = \prod u_{ii}$.

---

### Example: $A = LU$

#### **The Matrix**

$$A = \begin{pmatrix} 2 & 3 & 1 \\ 4 & 7 & 5 \\ 0 & -2 & 2 \end{pmatrix}$$

#### **Step 1: Eliminate $a_{21}$**

- **Operation:** $R_2 - 2R_1 \to R_2$
- **Multiplier ($l_{21}$):** $2$
- **Resulting Matrix:**
$$\begin{pmatrix} 2 & 3 & 1 \\ 0 & 1 & 3 \\ 0 & -2 & 2 \end{pmatrix}$$
#### **Step 2: Eliminate $a_{32}$**

- **Operation:** $R_3 - (-2)R_2 \to R_3$
- **Multiplier ($l_{32}$):** $-2$
- **Resulting Matrix ($U$):**
$$\begin{pmatrix} 2 & 3 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 8 \end{pmatrix}$$
#### **Step 3: Construct $L$ and $U$**

$L$ contains the multipliers in the lower triangle and $1$s on the diagonal. $U$ is the final upper triangular form.

$$L = \begin{pmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 0 & -2 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 2 & 3 & 1 \\ 0 & 1 & 3 \\ 0 & 0 & 8 \end{pmatrix}$$

---

#LinearAlgebra #LUDecomposition #MatrixAlgorithms #Optimization