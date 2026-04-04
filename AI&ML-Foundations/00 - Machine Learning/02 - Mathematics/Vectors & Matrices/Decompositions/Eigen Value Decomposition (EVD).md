**Eigenvalue Decomposition (EVD)** is the diagonalization of a linear operator $A \in \mathbb{C}^{n \times n}$ into its "natural" basis.

---

### 1. Problem Statement

Find the Eigenvalue Decomposition ($A = Q \Lambda Q^T$) for:

$$\large A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 5 \end{bmatrix}$$

---

### 2. Characteristic Equation

Solve $\det(A - \lambda I) = 0$ using cofactor expansion along the third row/column:

$$\det \begin{bmatrix} 2-\lambda & 1 & 0 \\ 1 & 2-\lambda & 0 \\ 0 & 0 & 5-\lambda \end{bmatrix} = (5-\lambda) \det \begin{bmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{bmatrix} = 0$$

$$(5-\lambda) [(2-\lambda)^2 - 1] = 0$$
$$(5-\lambda) (\lambda^2 - 4\lambda + 3) = 0$$
$$(5-\lambda) (\lambda - 3) (\lambda - 1) = 0$$
**Spectrum $\sigma(A)$:**
$$\lambda_1 = 5, \quad \lambda_2 = 3, \quad \lambda_3 = 1$$

$$\large \Lambda = \begin{bmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

---

### 3. Compute Eigenvectors ($Q$)

For each $\lambda_i$, solve the homogeneous system $(A - \lambda_i I)\mathbf{v}_i = \mathbf{0}$.

**Case $\lambda_1 = 5$:**

$$\begin{bmatrix} -3 & 1 & 0 \\ 1 & -3 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \mathbf{0} \implies x=0, y=0, z=1 \implies \mathbf{v}_1 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

**Case $\lambda_2 = 3$:**

$$\begin{bmatrix} -1 & 1 & 0 \\ 1 & -1 & 0 \\ 0 & 0 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \mathbf{0} \implies x=y, z=0 \implies \mathbf{v}_2 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix}$$

**Case $\lambda_3 = 1$:**

$$\begin{bmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \mathbf{0} \implies x=-y, z=0 \implies \mathbf{v}_3 = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$$

---

### 4. Construct the Modal Matrix $Q$

Since $A$ is symmetric and eigenvalues are distinct, $\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3$ are mutually orthogonal.

$$\large Q = \begin{bmatrix} 0 & 1/\sqrt{2} & 1/\sqrt{2} \\ 0 & 1/\sqrt{2} & -1/\sqrt{2} \\ 1 & 0 & 0 \end{bmatrix}$$

---

### 5. Decomposition Synthesis

The full EVD is given by $A = Q \Lambda Q^T$:

$$\large \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 5 \end{bmatrix} = \begin{bmatrix} 0 & 1/\sqrt{2} & 1/\sqrt{2} \\ 0 & 1/\sqrt{2} & -1/\sqrt{2} \\ 1 & 0 & 0 \end{bmatrix} \begin{bmatrix} 5 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 0 & 1 \\ 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 1/\sqrt{2} & -1/\sqrt{2} & 0 \end{bmatrix}$$

---

### EVD vs. SVD

- **EVD:** $A = Q \Lambda Q^{-1}$. Requires $A$ to be square and diagonalizable. Uses a single basis ($Q$).
- **[[Singular Value Decomposition (SVD)|SVD:]]** $A = U \Sigma V^*$. Applies to _any_ matrix. Uses two distinct orthonormal bases ($U$ and $V$).