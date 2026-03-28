## **Solving a $3 \times 6$ Augmented Matrix**

### **1. The System**

Let’s define a system where $A$ is $3 \times 5$ and the 6th column is the constant vector $b$.

Variables: $x_1, x_2, x_3, x_4, x_5$

**Initial Augmented Matrix $[A|b]$:**

$$\left( \begin{array}{ccccc|c} 1 & 3 & 0 & 2 & -1 & 4 \\ 2 & 6 & 1 & 1 & 0 & 10 \\ 1 & 3 & 2 & -4 & 3 & 10 \end{array} \right)$$

---

### **2. Row Echelon Form (REF) Steps**

**Step A: Eliminate below $a_{11}$**

- $R_2 - 2R_1 \to R_2$
- $R_3 - R_1 \to R_3$

$$\left( \begin{array}{ccccc|c} \mathbf{1} & 3 & 0 & 2 & -1 & 4 \\ 0 & 0 & 1 & -3 & 2 & 2 \\ 0 & 0 & 2 & -6 & 4 & 6 \end{array} \right)$$

**Step B: Eliminate below the next pivot**

The next available pivot is $a_{23} = 1$ (since column 2 is all zeros below the first row).
- $R_3 - 2R_2 \to R_3$

$$\left( \begin{array}{ccccc|c} \mathbf{1} & 3 & 0 & 2 & -1 & 4 \\ 0 & 0 & \mathbf{1} & -3 & 2 & 2 \\ 0 & 0 & 0 & 0 & 0 & 2 \end{array} \right)$$

---

### **3. Analyzing Consistency**

Look at the bottom row: $0x_1 + 0x_2 + 0x_3 + 0x_4 + 0x_5 = 2$.
This is a contradiction ($0 = 2$).

- **Conclusion:** This specific system is **inconsistent** and has **no solution**.

> [!IMPORTANT]
> 
> To find a **Null Space**, we must look at the homogeneous system $Ax = 0$. Let's assume the constants were such that the bottom row became all zeros.

---

### **4. Finding the Null Space (Assuming $b=0$)**

If the last row was $(0, 0, 0, 0, 0 | 0)$, we identify:

- **Pivots:** Columns 1 and 3.
- **Free Variables:** $x_2, x_4, x_5$. Let $x_2=r, x_4=s, x_5=t$.

**Back-substitution for $Ax=0$:**

1. $x_3 - 3x_4 + 2x_5 = 0 \implies x_3 = 3s - 2t$
2. $x_1 + 3x_2 + 2x_4 - x_5 = 0 \implies x_1 = -3r - 2s + t$

**Null Space Basis:**

Extract the coefficients for each free variable parameter:

$$\text{Null}(A) = \text{span} \left\{ \begin{pmatrix} -3 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} -2 \\ 0 \\ 3 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -2 \\ 0 \\ 1 \end{pmatrix} \right\}$$

---

### **5. Obsidian Summary Table**

|**Component**|**Value in this Example**|
|---|---|
|**Rank**|2 (Number of pivots)|
|**Nullity**|3 (Number of free variables)|
|**Dimensions**|$n = 5$ variables|
|**Verification**|$\text{Rank} + \text{Nullity} = 2 + 3 = 5$|

---

#LinearAlgebra #Matrix #UnderdeterminedSystem #NullSpace