**Similarity (Cosine):** Measures the **alignment of the orientation** (angle) between two vectors. It is completely independent of their magnitude.

> Refer: [[Proximity Metrics]]

## Cosine Similarity
Measures the alignment of the orientation (angle) between two vectors, independent of their magnitude.
$$\large S_C(A, B) = \frac{A \cdot B}{\|A\| \|B\|} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}} $$
-   $A, B$: two vectors.
-   $A_i, B_i$: the $i$-th component of vectors $A$ and $B$.
-   $n$: the number of dimensions.
-   $\cdot$: dot product.
-   $\|\cdot\|$: Euclidean norm (magnitude).

## Jaccard Similarity (Jaccard Index)
Quantifies the similarity between finite sample sets, defined as the size of the intersection divided by the size of the union of the sample sets.
$$\large J(A, B) = \frac{|A \cap B|}{|A \cup B|} $$
-   $A, B$: two sets.
-   $|A \cap B|$: the number of elements common to both sets.
-   $|A \cup B|$: the number of elements in either set.

## Pearson Correlation Coefficient

> <mark style="background: #ABF7F7A6;">IMP</mark> Refer: [[Pearson Correlation]]

</br>

## Dice Similarity (Sørensen-Dice Coefficient)
A statistic used to gauge the similarity of two samples, often used for comparing image segmentation or text.
$$\large DSC(A, B) = \frac{2 |A \cap B|}{|A| + |B|} $$
-   $A, B$: two sets.
-   $|A \cap B|$: the number of elements common to both sets.
-   $|A|, |B|$: the number of elements in set $A$ and set $B$ respectively.

## Overlap Coefficient
Measures the overlap between two sets, defined as the size of the intersection divided by the size of the smaller of the two sets.
$$\large (A, B) = \frac{|A \cap B|}{\min(|A|, |B|)} $$
-   $A, B$: two sets.
-   $|A \cap B|$: the number of elements common to both sets.
-   $\min(|A|, |B|)$: the size of the smaller of the two sets.



## Simple Matching Coefficient (SMC)
Measures the similarity between two binary vectors by counting the number of matching attributes (both 0-0 and 1-1) and dividing by the total number of attributes.
$$\large SMC(A, B) = \frac{\text{Number of matching attributes}}{\text{Total number of attributes}} = \frac{M_{00} + M_{11}}{M_{00} + M_{01} + M_{10} + M_{11}} $$
-   $M_{00}$: number of attributes where both $A$ and $B$ are 0.
-   $M_{11}$: number of attributes where both $A$ and $B$ are 1.
-   $M_{01}$: number of attributes where $A$ is 0 and $B$ is 1.
-   $M_{10}$: number of attributes where $A$ is 1 and $B$ is 0.

> [!NOTE] When do you use similarity?
> ##### **Use Similarity (Cosine) when Direction matters:**
>
> In high-dimensional spaces like **Natural Language Processing (NLP)** or **Recommendation Systems**, the frequency of words (magnitude) is often less important than the topic (direction).
>
> - **Example:** A 10-page document about "Calculus" and a 100-page document about "Calculus" have very different L2​ distances (due to word count), but their Cosine Similarity will be near 1 because their "topic vector" points in the same direction.
>
> - **Concept:** **Normalizing for length**. Using Cosine similarity is mathematically equivalent to L2​ distance on vectors that have been normalized to unit length.
