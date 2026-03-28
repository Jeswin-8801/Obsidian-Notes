### **1. Starting REF Matrix**

We begin with a matrix already in **Row Echelon Form**.
$$\begin{pmatrix} \mathbf{2} & 4 & 6 & 8 \\ 0 & 0 & \mathbf{3} & 9 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

---

### **2. Step 1: Normalize Pivots**

- $\frac{1}{3}R_2 \to R_2$
$$\begin{pmatrix} \mathbf{1} & 2 & 3 & 4 \\ 0 & 0 & \mathbf{1} & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

---

### **3. Step 2: Eliminate Above Pivots**

- $R_1 - 3R_2 \to R_1$
_(Using the pivot in $R_2$ to clear the entry at $a_{13}$)_
$$\begin{pmatrix} \mathbf{1} & 2 & 0 & -5 \\ 0 & 0 & \mathbf{1} & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

---

### **4. Final RREF Criteria**

- **Leading 1s:** All pivots are scaled to **1**.
- **Column Purity:** Each pivot is the **only** non-zero entry in its column.
- **Staircase:** All zero rows remain at the bottom.

---

#LinearAlgebra #Matrix #RREF #GaussJordan