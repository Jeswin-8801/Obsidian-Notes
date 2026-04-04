### 1. Input Matrix

$$\large A = \begin{bmatrix} 0 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix}, \quad \text{rank}(A) = 1$$

---

### 2. Form $A^T A \in \mathbb{R}^{3 \times 3}$

$$A^T A = \begin{bmatrix} 0 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 0 \end{bmatrix} \begin{bmatrix} 0 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 2 & 2 \\ 0 & 2 & 2 \end{bmatrix}$$

---

### 3. Eigenvalues of $A^T A$ (Singular Values)

$$\det(A^T A - \lambda I) = (-\lambda) \det \begin{bmatrix} 2-\lambda & 2 \\ 2 & 2-\lambda \end{bmatrix} = -\lambda [ (2-\lambda)^2 - 4 ] = 0$$

$$\lambda(-\lambda^2 + 4\lambda) = 0 \implies \lambda_1 = 4, \lambda_2 = 0, \lambda_3 = 0$$

**Singular Values:**

$$\sigma_1 = \sqrt{4} = 2, \quad \sigma_2 = 0, \quad \sigma_3 = 0$$

$$\large \Sigma = \begin{bmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

---

### 4. Right Singular Vectors ($V \in O(3)$)

Find orthonormal eigenvectors for $\text{Spec}(A^T A)$:

- **For $\lambda_1 = 4$:** $(A^T A - 4I)\mathbf{v}_1 = 0 \implies \begin{bmatrix} -4 & 0 & 0 \\ 0 & -2 & 2 \\ 0 & 2 & -2 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = 0 \implies \mathbf{v}_1 = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$
    
- **For $\lambda_{2,3} = 0$ (Kernel):** $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \quad \mathbf{v}_3 = \frac{1}{\sqrt{2}} \begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}$
    

$$\large V = \begin{bmatrix} 0 & 1 & 0 \\ 1/\sqrt{2} & 0 & 1/\sqrt{2} \\ 1/\sqrt{2} & 0 & -1/\sqrt{2} \end{bmatrix}$$

---

### 5. Left Singular Vectors ($U \in O(3)$)

For $\sigma_1 = 2$:

$$\mathbf{u}_1 = \frac{1}{\sigma_1} A \mathbf{v}_1 = \frac{1}{2} \begin{bmatrix} 0 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0 \\ 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{bmatrix}$$

Complete $U$ by Gram-Schmidt/Inspection to form an orthonormal basis for $\mathbb{R}^3$:

$$\mathbf{u}_2 = \begin{bmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \\ 0 \end{bmatrix}, \quad \mathbf{u}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$$

$$\large U = \begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 1/\sqrt{2} & -1/\sqrt{2} & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

---

### 6. Summary Structure

$$\large A = \underbrace{\begin{bmatrix} 1/\sqrt{2} & 1/\sqrt{2} & 0 \\ 1/\sqrt{2} & -1/\sqrt{2} & 0 \\ 0 & 0 & 1 \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} 2 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} 0 & 1/\sqrt{2} & 1/\sqrt{2} \\ 1 & 0 & 0 \\ 0 & 1/\sqrt{2} & -1/\sqrt{2} \end{bmatrix}}_{V^T}$$

### Key Properties

- **Rank-1 Approximation:** $A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T$.
    
- **Subspaces:** $\text{Col}(A) = \text{span}(\mathbf{u}_1)$, $\text{Null}(A) = \text{span}(\mathbf{v}_2, \mathbf{v}_3)$.