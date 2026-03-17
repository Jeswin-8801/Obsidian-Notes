

# 3-Nearest Neighbors (3-NN)

This note outlines the process of predicting a Patient Risk Factor using the 3-NN model with Manhattan distance.

## I. 3-Nearest Neighbors (3-NN) Model

The 3-NN model predicts the Risk Factor for a query instance by finding its three nearest neighbors in the training data and aggregating their risk factors.

**Query Instance (q):** Eye=5, Verbal=5, Motor=5

**Training Data:**

| Training Point (i) | Eye ($x_1$) | Verbal ($x_2$) | Motor ($x_3$) | Risk (y) |
| :----------------- | :---------- | :------------- | :------------ | :------- |
| P1                 | 10          | 3              | 5             | 5        |
| P2                 | 5           | 2              | 3             | 2        |
| P3                 | 5           | 1              | 5             | 8        |
| P4                 | 6           | 9              | 2             | 6        |

### Step 1: Calculate Manhattan Distance

The Manhattan distance ($d$) between the query instance ($q$) and each training instance ($i$) is calculated using the formula:

$$\Huge d(q, i) = \sum_{j=1}^{n} |q_j - i_j| $$

Where $n$ is the number of features (Eye, Verbal, Motor).


| Training Point (i) | Calculation: $(5-x_1) + (5-x_2) + (5-x_3)$ | Distance (d) |
| :----------------- | :---------------------------------------- | :----------- |
| P1                 | $(5-10) + (5-3) + (5-5) = 5 + 2 + 0$       | ==7==        |
| P2                 | $(5-5) + (5-2) + (5-3) = 0 + 3 + 2$       | ==5==            |
| P3                 | $(5-5) + (5-1) + (5-5) = 0 + 4 + 0$       | ==4==            |
| P4                 | $(5-6) + (5-9) + (5-2) = 1 + 4 + 3$       | 8            |

### Step 2: Identify the 3-Nearest Neighbors

Sorting the training points by distance (smallest to largest):

1.  P3 (d = 4)
2.  P2 (d = 5)
3.  P1 (d = 7)

### Step 3: Aggregate the Risk Factors

Using the average as the aggregation function for the 3-NN:

Predicted Risk = $\frac{\text{Risk(P3)} + \text{Risk(P2)} + \text{Risk(P1)}}{3} = \frac{8 + 2 + 5}{3} = \frac{15}{3} = 5$




