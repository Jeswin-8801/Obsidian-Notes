**Proximity/Distance (L1​,L2​):** Measures the **magnitude of the gap** between two points. It is sensitive to the length (magnitude) of the vectors.

> Refer: [[Similarity Metrics]]


## Euclidean Distance (L2 Norm)
Measures the straight-line distance between two points in Euclidean space.
$$\large d(p, q) = \sqrt{\sum_{i=1}^{n} (q_i - p_i)^2} $$
-   $p, q$: two points (vectors) in $n$-dimensional space.
-   $p_i, q_i$: the $i$-th coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.

## Minkowski Distance
A generalization of Euclidean and Manhattan distances, parameterized by $p$.
$$\large d(p, q) = \left( \sum_{i=1}^{n} |q_i - p_i|^k \right)^{1/k} $$
-   $p, q$: two points (vectors) in $n$-dimensional space.
-   $p_i, q_i$: the $i$-th coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.
-   $k$: the order of the norm (e.g., $k=1$ for Manhattan, $k=2$ for Euclidean).

## Mahalanobis Distance
Measures the distance between a point and a distribution, accounting for correlations between variables.
$$\large d(x, \mu) = \sqrt{(x - \mu)^T S^{-1} (x - \mu)} $$
-   $x$: a data point (vector).
-   $\mu$: the mean vector of the distribution.
-   $S$: the covariance matrix of the distribution.
-   $T$: transpose of the vector.
-   $S^{-1}$: inverse of the covariance matrix.


> [!NOTE] When do you use Distance?
> ##### **Use Distance (L2​) when Magnitude matters:**
   In many physical or optimization problems, the "size" of the vector is critical data.
> - **Example:** Predicting housing prices. If one house is 10× larger than another, their distance in feature space _should_ be large, even if the "ratio" of rooms-to-bathrooms is the same.
> - **K-Means Clustering:** Standard K-Means assumes Euclidean distance.
