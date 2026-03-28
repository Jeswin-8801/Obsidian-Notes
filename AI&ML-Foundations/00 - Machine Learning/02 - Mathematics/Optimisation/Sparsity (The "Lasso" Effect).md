The most critical property in machine learning is **sparsity induction**.

- **Singularity at the Axes:** The "corners" of the L1​ unit ball lie exactly on the coordinate axes.
    
- **Feature Selection:** When used as a regularization term (Lasso), the optimization process is highly likely to hit these corners. This forces some coefficients (xi​) to become **exactly zero**, effectively performing automatic feature selection.
	
- **Robustness to Outliers:** Compared to the L2​ norm, the L1​ norm is less sensitive to outliers because it does not square the error terms. 