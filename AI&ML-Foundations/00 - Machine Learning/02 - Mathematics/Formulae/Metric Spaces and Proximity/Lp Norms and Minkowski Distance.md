
**Proximity/Distance (L1​,L2​):** Measures the **magnitude of the gap** between two points. It is sensitive to the length (magnitude) of the vectors.

> Refer: [[Similarity Metrics]]

## Manhattan Distance (L1 Norm)
Calculates the sum of the absolute differences of their Cartesian coordinates.
$$\large d(p, q) = \sum_{i=1}^{n} |q_i - p_i| $$
-   $p, q$: two points (vectors) in $n$-dimensional space.
-   $p_i, q_i$: the $i$-th coordinate of points $p$ and $q$.
-   $n$: the number of dimensions.

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