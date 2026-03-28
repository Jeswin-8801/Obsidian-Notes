**Proximity/Distance:** Measures the **magnitude of the gap** between two points in a multi-dimensional space. 

Unlike [[Similarity Metrics]] that may focus on the orientation or angle between vectors, distance metrics are highly sensitive to the absolute length (magnitude) and scale of the vectors. This means that if the values of the features increase, the distance increases accordingly, even if the relative proportions remain the same.

> In addition to the absolute magnitude or scalar length of a vector, it is also important to take its spatial orientation and the resulting angular displacement between data points within [[Similarity Metrics]].

> [!NOTE] Note
> Distances and Norms ($L_p$) are not the same:
> [[Distances vs Norms]]

</br>

***
## Manhattan Distance
Calculates the sum of the absolute differences of their Cartesian coordinates.
$$\large d_1(\mathbf{p}, \mathbf{q}) = \|\mathbf{p} - \mathbf{q}\|_1 = \sum_{i=1}^n |p_i - q_i| $$
-   $\mathbf{p}, \mathbf{q} \in \mathbb{R}^n$
-   $p_i, q_i$: the $i \text{-th}$ coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.

> Checkout [[Lp Norms and its Graphical Representation#The Manhattan Norm ($L_1$ Norm)|The Manhattan Norm]]
> [[Lp Norms and its Graphical Representation#2. $p=1$ (Manhattan / Taxicab Norm)|Shape of the Manhattan Norm when plotted on a graph]]

***

## Euclidean Distance

Measures the straight-line distance between two points in Euclidean space, often referred to as the $L_2$ norm. 

$$\large d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2} $$
-   $p, q$: two points (vectors) in $n$-dimensional space.
-   $p_i, q_i$: the $i \text{-th}$ coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.

> Checkout [[Lp Norms and its Graphical Representation#3. $p=2$ (Euclidean Norm)]]

***

## Minkowski Distance
A generalized metric known as the $L_p$ norm, which provides a framework for calculating distance based on a parameter $k$. By adjusting $k$, you can change the sensitivity of the metric to large differences in individual dimensions.

$$\large d(p, q) = \left( \sum_{i=1}^{n} |q_i - p_i|^k \right)^{1/k} $$
-   $p, q$: two points (vectors) in $n$-dimensional space.
-   $p_i, q_i$: the $i$-th coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.
-   $k$: the order of the norm. 
    - When $k=1$, it is the **[[#Manhattan Distance]]** (Taxicab norm)
    - When $k=2$, it is the **[[#Euclidean Distance]]**
    - As $k \to \infty$, it becomes the **Chebyshev Distance** (**[[Lp Norms and its Graphical Representation#The Chebyshev Norm ($L_ infty$ Norm)|Chebyshev Norm]]**)


***

## Mahalanobis Distance
Measures the distance between a point and a distribution rather than just two points. It is "distribution-aware" because it accounts for the variance of each variable and the correlations between them, effectively measuring how many standard deviations a point is away from the mean.

$$\large d(x, \mu) = \sqrt{(x - \mu)^T S^{-1} (x - \mu)} $$
-   $x$: a data point (vector).
-   $\mu$: the mean vector of the distribution.
-   $S$: the covariance matrix, which captures how variables change together.
-   $T$: transpose of the vector.
-   $S^{-1}$: inverse of the covariance matrix, used to "normalize" the space and handle correlations.
- **Use Case:** Excellent for multivariate outlier detection, as it can identify points that are far from the "cloud" of data even if their individual feature values seem normal.

***


> [!NOTE] When do you use Distance?
> ##### **Use Distance (L2​) when Magnitude matters:**
   In many physical or optimization problems, the "size" of the vector is critical data.
> - **Example:** Predicting housing prices. If one house is 10× larger than another, their distance in feature space _should_ be large, even if the "ratio" of rooms-to-bathrooms is the same.
> - **K-Means Clustering:** Standard K-Means assumes Euclidean distance.

