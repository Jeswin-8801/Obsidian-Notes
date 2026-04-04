
**Given:**

A set of vectors $S = \{v_1, v_2, v_3, v_4\} \subset \mathbb{R}^3$ forming the columns of matrix $A$:

$$A = \begin{pmatrix} 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \end{pmatrix}$$

**Objective:**

Construct an orthonormal basis $\{e_1, e_2, e_3\}$ for $\mathcal{C}(A)$ by performing row reduction on the augmented matrix $[A^T A \mid A^T]$.

---

### I. Matrix Construction

**Gram Matrix $G = A^T A$:**

$$A^T A = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 & 1 & 2 \\ 1 & 2 & 1 & 2 \\ 1 & 1 & 2 & 2 \\ 2 & 2 & 2 & 3 \end{pmatrix}$$

**Augmented Matrix $M = [G \mid A^T]$:**

$$M = \left[ \begin{array}{cccc|ccc} 2 & 1 & 1 & 2 & 1 & 1 & 0 \\ 1 & 2 & 1 & 2 & 1 & 0 & 1 \\ 1 & 1 & 2 & 2 & 0 & 1 & 1 \\ 2 & 2 & 2 & 3 & 1 & 1 & 1 \end{array} \right]$$

---

### II. Gaussian Elimination $\text{ref}(M)$

1. $R_2 \to R_2 - \frac{1}{2}R_1, \quad R_3 \to R_3 - \frac{1}{2}R_1, \quad R_4 \to R_4 - R_1$:
    
    $$\left[ \begin{array}{cccc|ccc} 2 & 1 & 1 & 2 & 1 & 1 & 0 \\ 0 & \frac{3}{2} & \frac{1}{2} & 1 & \frac{1}{2} & -\frac{1}{2} & 1 \\ 0 & \frac{1}{2} & \frac{3}{2} & 1 & -\frac{1}{2} & \frac{1}{2} & 1 \\ 0 & 1 & 1 & 1 & 0 & 0 & 1 \end{array} \right]$$
    
2. $R_3 \to R_3 - \frac{1}{3}R_2, \quad R_4 \to R_4 - \frac{2}{3}R_2$:
    
    $$\left[ \begin{array}{cccc|ccc} 2 & 1 & 1 & 2 & 1 & 1 & 0 \\ 0 & \frac{3}{2} & \frac{1}{2} & 1 & \frac{1}{2} & -\frac{1}{2} & 1 \\ 0 & 0 & \frac{4}{3} & \frac{2}{3} & -\frac{2}{3} & \frac{2}{3} & \frac{2}{3} \\ 0 & 0 & \frac{2}{3} & \frac{1}{3} & -\frac{1}{3} & \frac{1}{3} & \frac{1}{3} \end{array} \right]$$
    
3. $R_4 \to R_4 - \frac{1}{2}R_3$:
    
    $$\left[ \begin{array}{cccc|ccc} 2 & 1 & 1 & 2 & 1 & 1 & 0 \\ 0 & \frac{3}{2} & \frac{1}{2} & 1 & \frac{1}{2} & -\frac{1}{2} & 1 \\ 0 & 0 & \frac{4}{3} & \frac{2}{3} & -\frac{2}{3} & \frac{2}{3} & \frac{2}{3} \\ 0 & 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right]$$
    

---

### III. Extraction and Normalization

**Orthogonal Vectors $\{u_i\}$ (Rows of Right-Side Matrix):**

$$u_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, \quad u_2 = \begin{pmatrix} 1/2 \\ -1/2 \\ 1 \end{pmatrix}, \quad u_3 = \begin{pmatrix} -2/3 \\ 2/3 \\ 2/3 \end{pmatrix}$$

**Normalization $e_i = \frac{u_i}{\|u_i\|}$:**

- $\|u_1\| = \sqrt{1^2 + 1^2 + 0^2} = \sqrt{2}$
    
- $\|u_2\| = \sqrt{(1/2)^2 + (-1/2)^2 + 1^2} = \sqrt{3/2} = \frac{\sqrt{6}}{2}$
    
- $\|u_3\| = \sqrt{(-2/3)^2 + (2/3)^2 + (2/3)^2} = \sqrt{12/9} = \frac{2\sqrt{3}}{3}$
    

---

### IV. Final Orthonormal Basis

**Orthonormal Matrix $Q$:**

$$Q = \begin{pmatrix} 1/\sqrt{2} & 1/\sqrt{6} & -1/\sqrt{3} \\ 1/\sqrt{2} & -1/\sqrt{6} & 1/\sqrt{3} \\ 0 & 2/\sqrt{6} & 1/\sqrt{3} \end{pmatrix}$$

**Orthogonal Vectors obtained:**

1. $u_1 = [1, 1, 0]^T$
    
2. $u_2 = [0.5, -0.5, 1]^T$
    
3. $u_3 = [-2/3, 2/3, 2/3]^T$