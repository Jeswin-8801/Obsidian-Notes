
In an inner product space $(V, \langle \cdot, \cdot \rangle)$, the induced norm is defined as $\|v\| = \sqrt{\langle v, v \rangle}$.

---

### I. Cauchy-Schwarz Inequality

**Statement:** $|\langle u, v \rangle| \leq \|u\| \|v\|$

**Derivation:**

1. Consider a scalar $t \in \mathbb{R}$ and the non-negative property of the norm:
    
    $$\|u - tv\|^2 \geq 0$$
    
2. Expand using inner product axioms:
    
    $$\langle u - tv, u - tv \rangle \geq 0$$
    
    $$\langle u, u \rangle - 2t\langle u, v \rangle + t^2\langle v, v \rangle \geq 0$$
    
3. Let $\|u\|^2 = A$, $\langle u, v \rangle = B$, and $\|v\|^2 = C$:
    
    $$Ct^2 - 2Bt + A \geq 0$$
    
4. Since this quadratic in $t$ is always $\geq 0$, its discriminant $D$ must be $\leq 0$:
    
    $$D = (2B)^2 - 4(C)(A) \leq 0$$
    
    $$4B^2 \leq 4AC \implies B^2 \leq AC$$
    
5. Substitute back:
    
    $$\langle u, v \rangle^2 \leq \|u\|^2 \|v\|^2 \implies |\langle u, v \rangle| \leq \|u\| \|v\|$$

```mermaid
graph LR
    CS["Cauchy-Schwarz"] --> Proj["Projection Magnitude"]
    Proj --> Bound["|⟨u, v⟩| ≤ ||u|| ||v||"]
    Bound --> Unit["|⟨û, v̂⟩| ≤ 1"]
```

---

### II. Triangle Inequality

**Statement:** $\|u + v\| \leq \|u\| + \|v\|$

**Derivation:**

1. Square the LHS:
    
    $$\|u + v\|^2 = \langle u + v, u + v \rangle$$
    
2. Expand:
    
    $$\|u + v\|^2 = \|u\|^2 + 2\langle u, v \rangle + \|v\|^2$$
    
3. Apply Cauchy-Schwarz ($\langle u, v \rangle \leq |\langle u, v \rangle| \leq \|u\| \|v\|$):
    
    $$\|u + v\|^2 \leq \|u\|^2 + 2\|u\| \|v\| + \|v\|^2$$
    
4. Factor the RHS:
    
    $$\|u + v\|^2 \leq (\|u\| + \|v\|)^2$$
    
5. Take the square root:
    
    $$\|u + v\| \leq \|u\| + \|v\|$$
    

---

### III. Angle Between Vectors

The angle $\theta$ is derived via the geometric interpretation of the inner product.

**Derivation:**

1. From the Law of Cosines in $V$:
    
    $$\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\| \|v\| \cos \theta$$
    
2. From inner product expansion:
    
    $$\|u - v\|^2 = \langle u - v, u - v \rangle = \|u\|^2 + \|v\|^2 - 2\langle u, v \rangle$$
    
3. Equating the two expressions for $\|u - v\|^2$:
    
    $$\|u\|^2 + \|v\|^2 - 2\langle u, v \rangle = \|u\|^2 + \|v\|^2 - 2\|u\| \|v\| \cos \theta$$
    
4. Simplify:
    
    $$\langle u, v \rangle = \|u\| \|v\| \cos \theta$$
    
5. Solve for $\theta$:
    
    $$\theta = \arccos\left( \frac{\langle u, v \rangle}{\|u\| \|v\|} \right)$$
    

**Validity Check (via Cauchy-Schwarz):**

For $\arccos$ to be defined, the argument must satisfy:

$$-1 \leq \frac{\langle u, v \rangle}{\|u\| \|v\|} \leq 1$$

This is guaranteed by $|\langle u, v \rangle| \leq \|u\| \|v\|$.