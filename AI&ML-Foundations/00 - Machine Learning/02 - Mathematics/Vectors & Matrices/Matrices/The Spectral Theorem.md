## 1. Linear Operators and Adjoints

Let $V$ be a finite-dimensional Hilbert space (over $\mathbb{F} = \mathbb{R}$ or $\mathbb{C}$) with inner product $\langle \cdot, \cdot \rangle$.
For any $T \in \mathcal{L}(V)$, there exists a unique **adjoint** $T^*$ such that:
$$\large \langle Tv, w \rangle = \langle v, T^*w \rangle, \quad \forall v, w \in V$$

---

## 2. The Complex Case: Normal Operators

An operator $T \in \mathcal{L}(V)$ is **normal** if it commutes with its adjoint:
$$\large TT^* = T^*T$$

> [!abstract] Spectral Theorem (Complex)
> 
> Let $V$ be a complex finite-dimensional Hilbert space. $T \in \mathcal{L}(V)$ is **normal** if and only if there exists an **orthonormal basis** of $V$ consisting of eigenvectors of $T$.

**Matrix Representation:** A matrix $A \in \mathbb{C}^{n \times n}$ is unitarily diagonalizable ($A = U \Lambda U^*$) iff $AA^* = A^*A$.

---

## 3. The Real Case: Self-Adjoint Operators

For real inner product spaces, normality is insufficient for a real eigenbasis (e.g., rotations in $\mathbb{R}^2$ are normal but have complex eigenvalues). We require the operator to be **self-adjoint**.

> [!abstract] Spectral Theorem (Real)
> 
> Let $V$ be a real finite-dimensional Hilbert space. $T \in \mathcal{L}(V)$ is **self-adjoint** ($T = T^*$) if and only if there exists an **orthonormal basis** of $V$ consisting of eigenvectors of $T$.

**Matrix Representation:**

A matrix $A \in \mathbb{R}^{n \times n}$ is orthogonally diagonalizable ($A = Q \Lambda Q^T$) iff $A = A^T$.

---

## 4. Spectral Decomposition (Projection Form)

The theorem provides a **Resolution of the Identity**. Let $\lambda_1, \dots, \lambda_k$ be the distinct eigenvalues of $T$. Then $V$ decomposes into an orthogonal direct sum of eigenspaces:

$$\large V = E_{\lambda_1} \oplus^\perp E_{\lambda_2} \oplus^\perp \dots \oplus^\perp E_{\lambda_k}$$

This allows $T$ to be expressed as a linear combination of **orthogonal projections** $P_i$:

$$\large T = \sum_{i=1}^k \lambda_i P_i$$

**Properties of $P_i$:**

- **Completeness:** $\sum P_i = I$
- **Orthogonality:** $P_i P_j = 0$ for $i \neq j$    
- **Idempotency:** $P_i^2 = P_i = P_i^*$

---

## 5. Functional Calculus

The spectral decomposition allows for the application of functions to operators. For any function $f$ defined on $\text{Spec}(T)$:

$$\large f(T) = \sum_{i=1}^k f(\lambda_i) P_i$$

In matrix form, if $A = U \Lambda U^*$, then $f(A) = U f(\Lambda) U^*$.

---

## 6. Summary of Matrix Classes

| **Property**                 | **Eigenvalues λi​**         | **Unitary/Orthogonal Basis?** |
| ---------------------------- | --------------------------- | ----------------------------- |
| **Self-Adjoint (Hermitian)** | $\lambda_i \in \mathbb{R}$  | Yes                           |
| **Skew-Hermitian**           | $\lambda_i \in i\mathbb{R}$ | Yes                           |
| **Normal**                   | $\lambda_i \in \mathbb{C}$  | Yes (Complex space only)      |
| **Positive Definite**        | $\lambda_i > 0$             | Yes                           |


---

## 7. Variational Characterization

For a self-adjoint matrix $A$, the eigenvalues satisfy the **Rayleigh Quotient** extremum:

$$\large \lambda_{\min} \leq \frac{\langle Ax, x \rangle}{\langle x, x \rangle} \leq \lambda_{\max}$$

The eigenvectors are the critical points of the function $f(x) = \langle Ax, x \rangle$ constrained to the unit sphere $S^{n-1}$.