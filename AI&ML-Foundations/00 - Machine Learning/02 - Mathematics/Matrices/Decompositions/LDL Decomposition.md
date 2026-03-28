You're likely thinking of the **LDLT Decomposition**, which is essentially the "Row Echelon Form" version of Cholesky. It allows you to decompose a symmetric matrix without ever having to calculate a square root.

### Prerequisites

- **Square Matrix:** $A$ must be $n \times n$.
- **Symmetry:** $A = A^T$.
- **Invertibility:** All leading principal minors must be non-zero (it doesn't strictly have to be positive-definite, just symmetric and non-singular).

---

### Computational Complexity

- **Total FLOPs:** $\approx \frac{1}{3}n^3$
- **Big-O Notation:** $O(n^3)$
- **Advantage:** While the Big-O is the same as Cholesky, it is computationally "cheaper" on hardware because **division and multiplication** are faster than **square root** operations.

---

### Why use LDLT (The "REF" approach)?

- **Avoids Square Roots:** Ideal for matrices that are symmetric but **not** positive-definite (where Cholesky would require imaginary numbers).
- **Numerical Stability:** It maintains the exact precision of integers or rational numbers longer than Cholesky.
- **Symmetry Preservation:** Unlike standard LU, LDLT explicitly preserves and exploits the symmetry of the matrix throughout the elimination process.

---

### Example: $A = LDL^T$

We start with the same matrix $A$ but process it to keep $L$ with $1$s on the diagonal (Unit Lower Triangular) and store the pivots in a diagonal matrix $D$.

#### **The Matrix**

$$A = \begin{pmatrix} 4 & 12 & -16 \\ 12 & 37 & -43 \\ -16 & -43 & 98 \end{pmatrix}$$

#### **Step 1: First Pivot**

The first diagonal element is our first entry for $D$:

- **$d_{11} = 4$**
- To get the first column of $L$, divide the remaining entries in the first column of $A$ by $d_{11}$:
    - $l_{21} = \frac{12}{4} = 3$
    - $l_{31} = \frac{-16}{4} = -4$

#### **Step 2: Second Pivot**

Update the next diagonal element:

- **$d_{22} = a_{22} - l_{21}^2 d_{11} = 37 - (3^2 \times 4) = 37 - 36 = 1$**
- Update the next $L$ entry:
    - $l_{32} = \frac{1}{d_{22}}(a_{32} - l_{31}d_{11}l_{21}) = \frac{1}{1}(-43 - (-4 \times 4 \times 3)) = -43 + 48 = 5$

#### **Step 3: Third Pivot**

- **$d_{33} = a_{33} - (l_{31}^2 d_{11} + l_{32}^2 d_{22}) = 98 - ((-4)^2 \times 4 + 5^2 \times 1) = 98 - (64 + 25) = 9$**

---

### **5. The Resulting Factors**

$$L = \begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ -4 & 5 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 9 \end{pmatrix}$$

**Verification:** Notice that if you take the square root of $D$ ($\sqrt{D} = S$), then $L \times S$ gives you the exact $L$ matrix from the Cholesky example:

$$\begin{pmatrix} 1 & 0 & 0 \\ 3 & 1 & 0 \\ -4 & 5 & 1 \end{pmatrix} \begin{pmatrix} 2 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{pmatrix} = \begin{pmatrix} 2 & 0 & 0 \\ 6 & 1 & 0 \\ -8 & 5 & 3 \end{pmatrix}$$

---

#LinearAlgebra #LDLT #MatrixDecomposition #NumericalComputing
