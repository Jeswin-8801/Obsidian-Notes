In linear algebra and machine learning, a ==**sparse vector**== is a vector in which most of the elements are **zero**.

Conversely, a vector where most elements are non-zero is called a ==**dense vector**==. The "sparsity" of a vector is typically measured by the ratio of zero elements to the total number of elements.

***

### 1. Mathematical Representation

If we have a vector $\mathbf{v} \in \mathbb{R}^n$, it is considered sparse if:

$$\text{nnz}(\mathbf{v}) \ll n$$

_(Where $\text{nnz}$ is the count of non-zero elements)_.

**Example:**

- **Dense:** $[1.2, 0.5, -3.1, 0.8, 2.2]$
    
- **Sparse:** $[0, 0, 7.5, 0, 0, 0, 0, 0, -1.2, 0]$

---

### 2. Why Sparsity Matters in ML

Since you are working with **Machine Learning** and **Linear Algebra**, sparsity is a critical concept for three main reasons:

#### A. Efficiency
- **Compressed Storage:** Instead of storing all $n$ values, we store only the indices and values of the non-zero elements (e.g., using **Coordinate List (COO)** or **Compressed Sparse Row (CSR)** formats).
    
- **Computation:** Matrix-vector multiplication $\mathbf{Ax}$ becomes significantly faster because we can skip any operation involving a zero.

#### B. High-Dimensional Feature Spaces (NLP)

In Natural Language Processing, "One-Hot Encoding" or "Bag of Words" creates massive sparse vectors.

#### C. Interpretability (Feature Selection)

The **$L_1$ [[Manhattan Norm]], using $L_1$ regularization (Lasso) encourages the model to find a **sparse solution**.

- By forcing coefficients of "unimportant" features to exactly zero, the model effectively performs automatic feature selection, making it easier to understand which inputs actually drive the output.


---

|**Aspect**|**Dense Vector**|**Sparse Vector**|
|---|---|---|
|**Memory**|$O(n)$|$O(\text{nnz})$|
|**Common Use**|Deep Learning Weights, Audio|NLP, Recommender Systems, Genomics|
|**Regularization**|$L_2$ (Ridge)|$L_1$ (Lasso)|
