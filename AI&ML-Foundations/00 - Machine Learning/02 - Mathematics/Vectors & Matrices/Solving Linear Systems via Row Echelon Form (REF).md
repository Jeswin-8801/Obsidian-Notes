
To solve a system of equations, we represent it as an **augmented matrix** $[A | b]$ and use Gaussian Elimination to reach REF. From there, we use **back-substitution** to find the general solution and the **null space**.

---

### **1. The System of Equations**

Consider the following system (3 equations, 4 variables):
$$x_1 + 2x_2 - x_3 + 3x_4 = 4$$
$$2x_1 + 4x_2 - x_3 + 6x_4 = 7$$
$$x_1 + 2x_2 + x_3 + 3x_4 = 2$$

**Augmented Matrix Representation:**
$$[A|b] = \left( \begin{array}{cccc|c} 1 & 2 & -1 & 3 & 4 \\ 2 & 4 & -1 & 6 & 7 \\ 1 & 2 & 1 & 3 & 2 \end{array} \right)$$

---

### **2. Step-by-Step REF Transformation**

**Step A: Eliminate below the first pivot ($a_{11} = 1$)**

- $R_2 - 2R_1 \to R_2$
- $R_3 - R_1 \to R_3$

$$\left( \begin{array}{cccc|c} 1 & 2 & -1 & 3 & 4 \\ 0 & 0 & 1 & 0 & -1 \\ 0 & 0 & 2 & 0 & -2 \end{array} \right)$$

**Step B: Eliminate below the second pivot**

Our next pivot position is $a_{22}$, but it is $0$. We look to $a_{23}$, which is $1$. This is our new pivot.

- $R_3 - 2R_2 \to R_3$

$$\left( \begin{array}{cccc|c} \mathbf{1} & 2 & -1 & 3 & 4 \\ 0 & 0 & \mathbf{1} & 0 & -1 \\ 0 & 0 & 0 & 0 & 0 \end{array} \right)$$

---

### **3. Analyzing the Result**

- **Pivots:** Columns 1 and 3 ($x_1, x_3$) are **pivot variables**.
- **Free Variables:** Columns 2 and 4 ($x_2, x_4$) have no pivots. These are **free variables**. Let $x_2 = s$ and $x_4 = t$.

---

### **4. Finding the General Solution**

Translate the REF back into equations:

1. $x_3 = -1$
2. $x_1 + 2x_2 - x_3 + 3x_4 = 4 \implies x_1 + 2s - (-1) + 3t = 4$
    - $x_1 = 3 - 2s - 3t$

**General Solution (Vector Form):**

$$\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 3 - 2s - 3t \\ s \\ -1 \\ t \end{pmatrix} = \underbrace{\begin{pmatrix} 3 \\ 0 \\ -1 \\ 0 \end{pmatrix}}_{\text{Particular Sol}} + s\underbrace{\begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix}}_{\text{Vector 1}} + t\underbrace{\begin{pmatrix} -3 \\ 0 \\ 0 \\ 1 \end{pmatrix}}_{\text{Vector 2}}$$

---

### **5. Identifying the Null Space**

The **Null Space** ($\text{Null}(A)$) is the set of all solutions to $Ax = 0$. This is equivalent to the "homogeneous" part of our general solution (the parts attached to free variables $s$ and $t$).

**Basis for Null Space:**

$$\text{Null}(A) = \text{span} \left\{ \begin{pmatrix} -2 \\ 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -3 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right\}$$

> [!TIP]
> 
> **Rank-Nullity Check:** > Number of columns ($n=4$) = $\text{Rank}(2)$ + $\text{Nullity}(2)$.
> 
> Since we have 2 pivots and 2 free vectors, the math holds up!

---

#LinearAlgebra #Matrix #NullSpace #GaussianElimination