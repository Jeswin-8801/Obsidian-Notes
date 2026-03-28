# Locally Weighted Regression (LWR) with 2-NN and Gradient Descent

**Query Instance (q):** Eye=5, Verbal=5, Motor=5

**Training Data:**

| Training Point (i) | Eye ($x_1$) | Verbal ($x_2$) | Motor ($x_3$) | Risk (y) |
| :----------------- | :---------- | :------------- | :------------ | :------- |
| P1                 | 10          | 3              | 5             | 5        |
| P2                 | 5           | 2              | 3             | 2        |
| P3                 | 5           | 1              | 5             | 8        |
| P4                 | 6           | 9              | 2             | 6        |


This section applies a locally weighted regression approach, focusing on the 2-nearest neighbors and using a single iteration of gradient descent to refine the prediction.

### Step 1: Initial Estimation ($\theta_0$)

Using the provided formula for initial risk estimation:

$\text{Risk} = 10 - 0.1(\text{Verbal}) - 0.1(\text{Motor})$

For the query instance (Verbal=5, Motor=5):
Initial Prediction = $10 - 0.1(5) - 0.1(5) = 10 - 0.5 - 0.5 = 9$

### Step 2: Identify 2-Nearest Neighbors

From our previous distance calculations, the 2-nearest neighbors are:

*   P3 (d = 4)
*   P2 (d = 5)

### Step 3: Calculate Kernel Weights

Using the kernel function $K(d(q, x_i)) = -1 / d(q, x_i)$:

*   Weight for P3 ($w_1$): $-1 / 4 = -0.2500$
*   Weight for P2 ($w_2$): $-1 / 5 = -0.2000$

### Step 4: Gradient Descent (One Iteration)

The update rule for weighted regression, in this context, refines the prediction based on the weighted errors of the nearest neighbors.

*   **Errors:**
>	**Error P3**: $(\text{Initial Prediction} - \text{Actual Risk P3}) = (9 - 8) = 1$
>	**Error P2**: $(\text{Initial Prediction} - \text{Actual Risk P2}) = (9 - 2) = 7$

*   **Weighted Gradient Sum:**

    The weighted gradient sum is calculated as: $$ \sum w_i(y_{\text{pred}} - y_{\text{actual}}) = w_1 \cdot \text{Error P3} + w_2 \cdot \text{Error P2} $$
    Where:
    *   $w_i$: The kernel weight for training instance $i$.
    *   $y_{\text{pred}}$: The initial predicted risk for the query instance (from Step 1).
    *   $y_{\text{actual}}$: The actual risk factor of the training instance $i$.
	
    Substituting the values: 
    $= (-0.2500)(1) + (-0.2000)(7)$
    $= -0.25 - 1.4 = -1.65$

*   **Update with learning rate $\alpha = 0.1$:**

    The prediction is updated using the formula:    $$ \text{Prediction}_{\text{new}} = \text{Prediction}_{\text{old}} - \alpha \cdot \text{Weighted Gradient Sum} $$
    Where:
    *   $\text{Prediction}_{\text{new}}$:  The updated risk prediction after one iteration.
    *   $\text{Prediction}_{\text{old}}$: The initial risk prediction (9, from Step 1).
    *   $\alpha$: The learning rate, which controls the step size during the update.
    *   $\text{Weighted Gradient Sum}$: The value calculated above (-1.65).
	
    Substituting the values:
	$\text{Prediction}_{\text{new}} = 9 - 0.1 \cdot (-1.65)$
    $= 9 + 0.165 = 9.165$

**Final Prediction: ==9.1650==**