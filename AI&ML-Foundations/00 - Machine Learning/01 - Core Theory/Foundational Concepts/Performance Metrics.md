
# Classification Performance Metrics

Let $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^n$ be a dataset where $y_i \in \{0, 1\}$ denotes the ground truth. Let $f: \mathcal{X} \to \{0, 1\}$ be a binary classifier such that $\hat{y}_i = f(x_i)$.

## 1. Cardinality of Outcomes
The performance of $f$ is partitioned into four disjoint subsets of $\mathcal{D}$ based on the indicator function $\mathbb{1}(\cdot)$:

*   **True Positives ($TP$):** $\sum_{i=1}^n \mathbb{1}(\hat{y}_i = 1 \land y_i = 1)$
*   **True Negatives ($TN$):** $\sum_{i=1}^n \mathbb{1}(\hat{y}_i = 0 \land y_i = 0)$
*   **False Positives ($FP$):** $\sum_{i=1}^n \mathbb{1}(\hat{y}_i = 1 \land y_i = 0)$ (Type I Error)
*   **False Negatives ($FN$):** $\sum_{i=1}^n \mathbb{1}(\hat{y}_i = 0 \land y_i = 1)$ (Type II Error)

---

## 2. Mathematical Formalization of Metrics

### A. Accuracy ($\mathcal{A}$)
The global probability of correct classification:
$$\mathcal{A} = \frac{TP + TN}{TP + TN + FP + FN}$$

### B. Precision ($\mathcal{P}$)
The conditional probability $P(y=1 \mid \hat{y}=1)$, measuring the fidelity of positive predictions:
$$\mathcal{P} = \frac{TP}{TP + FP}$$

### C. Recall ($\mathcal{R}$)
The conditional probability $P(\hat{y}=1 \mid y=1)$, also termed sensitivity or hit rate:
$$\mathcal{R} = \frac{TP}{TP + FN}$$

### D. $F_1$ Score
The harmonic mean of precision and recall, providing a robust measure under class imbalance $\pi_1 \neq \pi_0$:
$$F_1 = 2 \cdot \frac{\mathcal{P} \cdot \mathcal{R}}{\mathcal{P} + \mathcal{R}} = \frac{TP}{TP + \frac{1}{2}(FP + FN)}$$

---

## 3. Decision Heuristics

> [!ABSTRACT] Metric Optimization
> | Objective | Optimization Target | Domain Example |
> | :--- | :--- | :--- |
> | Minimize Type I Error | $\max \mathcal{P}$ | Spam detection |
> | Minimize Type II Error | $\max \mathcal{R}$ | Pathological diagnosis |
> | Class Imbalance | $\max F_1$ | Fraud detection |

---

## Example Problem

> Refer: [[(Example) Performance Metrics]]