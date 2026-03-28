### 1. Dataset Formalization

> Find the Dataset at: [[Binary Classification Dataset with 3 Features]]

### 2. Decision Logic (The Predictor)

We define a heuristic classifier $h(\mathbf{x})$ based on a Boolean composition and a threshold $\tau$ for the integer feature $x_C$.

Let $\tau = 40$. The indicator function for feature $C$ is defined as:

$$f(x_C) = \mathbb{1}_{x_C > \tau} = \begin{cases} 1 & \text{if } x_C > 40 \\ 0 & \text{otherwise} \end{cases}$$

The model prediction $\hat{y}$ is defined by the logical OR across features:

$$\hat{y}_i = x_{i,A} \lor x_{i,B} \lor f(x_{i,C})$$

### 3. Prediction Vector & Confusion Matrix

For each observation $\mathbf{x}_i$, we apply a vector-valued function $g(\mathbf{x}_i)$ to ensure all inputs are Boolean:
$$g(\mathbf{x}_i) = \begin{bmatrix} x_{i,A} \\ x_{i,B} \\ \mathbb{1}_{x_{i,C} > 40} \end{bmatrix}$$
The model $h(\mathbf{x})$ is defined as the supremum of the Boolean feature set:

$$h(\mathbf{x}_i) = \bigvee_{j=1}^{3} g(\mathbf{x}_i)_j = g(\mathbf{x}_i)_1 \lor g(\mathbf{x}_i)_2 \lor g(\mathbf{x}_i)_3$$
##### Observation $i=1$: $\mathbf{x}_1 = [1, 0, 45]$
1. **Transform:** $g(\mathbf{x}_1) = [1, 0, \mathbb{1}_{45 > 40}] = [1, 0, 1]$
2. **Apply Logic:** $1 \lor 0 \lor 1 = 1$
3. **Evaluate:** Actual $y_1=1$, Predicted $\hat{y}_1=1 \implies$ **True Positive (TP)**

> do the same for $i = \{2, 3, 4, 5\}$

- $\hat{y}_1 = 1 \lor 0 \lor 1 = 1$ (True Positive)
- $\hat{y}_2 = 0 \lor 1 \lor 0 = 1$ (False Positive)
- $\hat{y}_3 = 1 \lor 1 \lor 1 = 1$ (True Positive)
- $\hat{y}_4 = 0 \lor 0 \lor 0 = 0$ (True Negative)
- $\hat{y}_5 = 1 \lor 0 \lor 0 = 1$ (True Positive)

##### **Cardinality of Sets:**
- True Positives ($TP$): $|\{i : y_i=1 \land \hat{y}_i=1\}| = 3$
- False Positives ($FP$): $|\{i : y_i=0 \land \hat{y}_i=1\}| = 1$
- False Negatives ($FN$): $|\{i : y_i=1 \land \hat{y}_i=0\}| = 0$
- True Negatives ($TN$): $|\{i : y_i=0 \land \hat{y}_i=0\}| = 1$

---

### 4. Metric Derivation

##### Precision (Positive Predictive Value)
Precision $\mathcal{P}$ measures the accuracy of the positive predictions:

$$\mathcal{P} = \frac{TP}{TP + FP} = \frac{3}{3 + 1} = 0.75$$

##### Recall (Sensitivity / True Positive Rate)
Recall $\mathcal{R}$ measures the ability of the model to find all relevant cases:

$$\mathcal{R} = \frac{TP}{TP + FN} = \frac{3}{3 + 0} = 1.0$$

##### $F_1$ Score (Harmonic Mean)
The $F_1$ score provides a balanced metric between $\mathcal{P}$ and $\mathcal{R}$. We use the harmonic mean because it penalizes extreme values:

$$F_1 = 2 \cdot \frac{\mathcal{P} \cdot \mathcal{R}}{\mathcal{P} + \mathcal{R}}$$

Substituting the values:

$$F_1 = 2 \cdot \frac{0.75 \cdot 1.0}{0.75 + 1.0} = \frac{1.5}{1.75} \approx 0.857$$

|**Metric**|**Formula**|**Value**|
|---|---|---|
|**Precision**|$\frac{TP}{TP+FP}$|$0.75$|
|**Recall**|$\frac{TP}{TP+FN}$|$1.00$|
|**$F_1$ Score**|$\left(\frac{\mathcal{P}^{-1} + \mathcal{R}^{-1}}{2}\right)^{-1}$|$0.857$|

---

## Per-Feature Metric Decomposition

We evaluate the predictive power of each feature $\mathbf{x}_j$ as an independent basis for a classifier $h_j(\mathbf{x})$.

We define the set of features as $\mathcal{F} = \{A, B, C'\}$ where $C' = \mathbb{1}_{x_C > 40}$. Let the true label vector be $\mathbf{y} = [1, 0, 1, 0, 1]^\top$.

We define the prediction vector for each feature $\mathbf{p}_j$ and compute the cardinality of the confusion matrix subsets.

|**Feature (j)**|**Prediction Vector pj​**|**TP**|**FP**|**FN**|**TN**|
|---|---|---|---|---|---|
|**$x_A$**|$[1, 0, 1, 0, 1]^\top$|3|0|0|2|
|**$x_B$**|$[0, 1, 1, 0, 0]^\top$|1|1|2|1|
|**$x_{C'}$**|$[1, 0, 1, 0, 0]^\top$|2|0|1|2|

### 1.1 Local Metric Calculation

Using the standard definitions:

$$\text{Precision } (\mathcal{P}) = \frac{TP}{TP+FP}, \quad \text{Recall } (\mathcal{R}) = \frac{TP}{TP+FN}, \quad F_1 = \frac{2\mathcal{PR}}{\mathcal{P}+\mathcal{R}}$$

|**Feature**|**Precision (P)**|**Recall (R)**|**F1​ Score**|
|---|---|---|---|
|**$x_A$**|$\frac{3}{3+0} = 1.0$|$\frac{3}{3+0} = 1.0$|$1.0$|
|**$x_B$**|$\frac{1}{1+1} = 0.5$|$\frac{1}{1+2} = 0.33$|$0.40$|
|**$x_{C'}$**|$\frac{2}{2+0} = 1.0$|$\frac{2}{2+1} = 0.67$|$0.80$|

---

## 2. Ensemble Logic (All Together)

We define the global predictor $H(\mathbf{x})$ as a logical disjunction (OR gate) across the feature space:

$$H(\mathbf{x}) = \bigvee_{j \in \mathcal{F}} x_j = (x_A \lor x_B \lor x_{C'})$$

### 2.1 Resulting Vector and Cardinality

Applying the disjunction to each row $i$:

- $i=1: (1 \lor 0 \lor 1) = 1$
- $i=2: (0 \lor 1 \lor 0) = 1$
- $i=3: (1 \lor 1 \lor 1) = 1$
- $i=4: (0 \lor 0 \lor 0) = 0$
- $i=5: (1 \lor 0 \lor 0) = 1$

$\mathbf{p}_{ensemble} = [1, 1, 1, 0, 1]^\top$

### 2.2 Global Metric Computation

Comparing $\mathbf{p}_{ensemble}$ against $\mathbf{y}$:

- **$TP = 3$** (Indices 1, 3, 5)
- **$FP = 1$** (Index 2)
- **$FN = 0$** * **$TN = 1$** (Index 4)

$$\mathcal{P}_{total} = \frac{3}{3+1} = \mathbf{0.75}$$

$$\mathcal{R}_{total} = \frac{3}{3+0} = \mathbf{1.0}$$

$$F_{1, total} = \frac{2(0.75)(1.0)}{0.75+1.0} = \frac{1.5}{1.75} \approx \mathbf{0.857}$$