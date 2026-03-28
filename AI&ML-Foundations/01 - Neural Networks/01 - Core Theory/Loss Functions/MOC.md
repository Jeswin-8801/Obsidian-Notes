
## Loss Functions (Cost Functions)

The loss function quantifies the "error" between the prediction $\hat{y}$ and target $y$.

### Regression Loss

- **Mean Squared Error (MSE/L2):** $L = \frac{1}{n} \sum (y - \hat{y})^2$. Penalizes outliers heavily.
    
- **Mean Absolute Error (MAE/L1):** $L = \frac{1}{n} \sum |y - \hat{y}|$. More robust to outliers than MSE.
    
- **Huber Loss:** Combines MSE and MAE; quadratic for small errors and linear for large errors.
    

### Classification Loss

- **Binary Cross-Entropy (Log Loss):** $L = -[y \log(\hat{y}) + (1-y) \log(1-\hat{y})]$. Standard for binary classification.
    
- **Categorical Cross-Entropy:** $L = -\sum y_i \log(\hat{y}_i)$. Used for multi-class classification with one-hot encoded labels.
    
- **Sparse Categorical Cross-Entropy:** Same as above but used when labels are integers ($1, 2, 3...$) rather than one-hot vectors.
    
- **Hinge Loss:** $L = \max(0, 1 - y \cdot \hat{y})$. Primarily used for Support Vector Machines (SVMs).
