
# Neural Network Derivation: [2, 3, 2] Architecture


## 1. Notation and Set Definitions

We formalize all parameters within the field of real numbers $\mathbb{R}$.

- **Batch Size ($m$):** We assume $m=1$ for this single-pass derivation.
- **$n^{[l]}$:** Number of neurons in layer $l$.

|**Layer**|**Type**|**Count (n[l])**|**Activation Function (g)**|
|---|---|---|---|
|**$l=0$**|Input Layer|$n^{[0]} = 2$|Linear feed-through|
|**$l=1$**|Hidden Layer|$n^{[1]} = 3$|**ReLU**: $g^{(1)}(z) = \max(0, z)$|
|**$l=2$**|Output Layer|$n^{[2]} = 2$|**Sigmoid**: $g^{(2)}(z) = \sigma(z) = \frac{1}{1+e^{-z}}$|

```mermaid
graph LR
    %% Set lines to be as straight as possible
    linkStyle default interpolate linear

    %% INPUT LAYER (l=0)
    subgraph Input_Layer [Input Layer l=0]
        X1((x₁))
        X2((x₂))
        B1((1)) 
    end

    %% HIDDEN LAYER (l=1)
    subgraph Hidden_Layer [Hidden Layer l=1]
        H1((h₁))
        H2((h₂))
        H3((h₃))
        B2((1))
    end

    %% OUTPUT LAYER (l=2)
    subgraph Output_Layer [Output Layer l=2]
        O1((o₁))
        O2((o₂))
    end

    %% WEIGHTS W[1] (3x2) and Bias b[1] (3x1)
    X1 -->|"w₁₁¹"| H1
    X1 -->|"w₂₁¹"| H2
    X1 -->|"w₃₁¹"| H3
    X2 -->|"w₁₂¹"| H1
    X2 -->|"w₂₂¹"| H2
    X2 -->|"w₃₂¹"| H3
    %% Bias connections usually shown with dashed lines
    B1 -.->|"b₁¹"| H1
    B1 -.->|"b₂¹"| H2
    B1 -.->|"b₃¹"| H3

    %% WEIGHTS W[2] (2x3) and Bias b[2] (2x1)
    H1 -->|"w₁₁²"| O1
    H1 -->|"w₂₁²"| O2
    H2 -->|"w₁₂²"| O1
    H2 -->|"w₂₂²"| O2
    H3 -->|"w₁₃²"| O1
    H3 -->|"w₂₃²"| O2
    B2 -.->|"b₁²"| O1
    B2 -.->|"b₂²"| O2

    %% Styling
    style Input_Layer fill:#f5f5f5,stroke:#333
    style Hidden_Layer fill:#e1f5fe,stroke:#01579b
    style Output_Layer fill:#fff9c4,stroke:#fbc02d
    style B1 fill:#ffecb3,stroke:#ffa000
    style B2 fill:#ffecb3,stroke:#ffa000
    linkStyle default stroke:#999,stroke-width:1px
```

| **Component** | **Object**         | **Math Set**              | **Dimension**         |
| ------------- | ------------------ | ------------------------- | --------------------- |
| **Weights 1** | $\mathbf{W}^{[1]}$ | $\mathbb{R}^{3 \times 2}$ | $3$ rows, $2$ columns |
| **Bias 1**    | $\mathbf{b}^{[1]}$ | $\mathbb{R}^{3 \times 1}$ | $3$ rows, $1$ column  |
| **Weights 2** | $\mathbf{W}^{[2]}$ | $\mathbb{R}^{2 \times 3}$ | $2$ rows, $3$ columns |
| **Bias 2**    | $\mathbf{b}^{[2]}$ | $\mathbb{R}^{2 \times 1}$ | $2$ rows, $1$ column  |

---

## 2. Forward Propagation

### Step 2.1: Input to Hidden Layer ($l=1$)

The input vector $\mathbf{x}$ is transformed into the hidden state $\mathbf{a}^{[1]}$.

$$\large \mathbf{z}^{[1]} = \mathbf{W}^{[1]} \mathbf{x} + \mathbf{b}^{[1]}$$
$$\large \mathbf{a}^{[1]} = \text{ReLU}(\mathbf{z}^{[1]})$$

```mermaid
graph LR
    X((x)) -- "W⁽¹⁾, b⁽¹⁾" --> Z1[z⁽¹⁾]
    Z1 -- "ReLU" --> A1((a⁽¹⁾))
    style Z1 fill:#f9f,stroke:#333
    style A1 fill:#f9f,stroke:#333
```

|**Variable**|**Definition**|**Dimension (n[l]×n[l−1])**|**Set**|
|---|---|---|---|
|$\mathbf{x}$|Input Vector|$2 \times 1$|$\mathbf{x} \in \mathbb{R}^{2}$|
|$\mathbf{W}^{[1]}$|Layer 1 Weights|$3 \times 2$|$\mathbf{W}^{[1]} \in \mathbb{R}^{3 \times 2}$|
|$\mathbf{b}^{[1]}$|Layer 1 Bias|$3 \times 1$|$\mathbf{b}^{[1]} \in \mathbb{R}^{3}$|
|$\mathbf{z}^{[1]}$|Layer 1 Pre-activation|$3 \times 1$|$\mathbf{z}^{[1]} \in \mathbb{R}^{3}$|
|$\mathbf{a}^{[1]}$|Layer 1 Activation|$3 \times 1$|$\mathbf{a}^{[1]} \in \mathbb{R}^{3}$|

### Step 2.2: Output Layer ($l=2$)

Compute the final transformation and Sigmoid activation:

$$\large \mathbf{z}^{[2]} = \mathbf{W}^{[2]} \mathbf{a}^{[1]} + \mathbf{b}^{[2]}$$
$$\large \mathbf{a}^{[2]} = \sigma(\mathbf{z}^{[2]}) = \frac{1}{1 + e^{-\mathbf{z}^{[2]}}}$$

```mermaid
graph LR
    X((x)) --> Z1[z⁽¹⁾] --> A1((a⁽¹⁾))
    A1 -- "W⁽²⁾, b⁽²⁾" --> Z2[z⁽²⁾]
    Z2 -- "Sigmoid" --> A2((a⁽²⁾))
    style Z2 fill:#f9f,stroke:#333
    style A2 fill:#f9f,stroke:#333
```

---

## 3. Backward Propagation

### Step 3.1: Output Error ($\delta^{[2]}$)

We define the error term $\delta$ as the partial derivative of the loss $L$ with respect to the pre-activation $\mathbf{z}$.

$$\large \delta^{[2]} = \frac{\partial L}{\partial \mathbf{z}^{[2]}} = \mathbf{a}^{[2]} - \mathbf{y}$$
> Derivation for $\large \delta^{[2]}$ : [[(Subnotes) Backward Propagation Output Error]]

```mermaid
graph RL
    L[Loss L] -.->|"δ⁽²⁾ = a⁽²⁾ - y"| Z2[z⁽²⁾]
    style Z2 fill:#ffcccc,stroke:#333
```

|**Variable**|**Definition**|**Dimension**|**Set**|
|---|---|---|---|
|$\mathbf{y}$|Ground Truth Label|$2 \times 1$|$\mathbf{y} \in \{0, 1\}^{2}$|
|$\delta^{[2]}$|Output Error Gradient|$2 \times 1$|$\delta^{[2]} \in \mathbb{R}^{2}$|

### Step 3.2: Output Parameter Gradients

Calculate partial derivatives for $\mathbf{W}^{[2]}$ and $\mathbf{b}^{[2]}$:

$$\large \frac{\partial L}{\partial \mathbf{W}^{[2]}} = \delta^{[2]} (\mathbf{a}^{[1]})^T, \quad \frac{\partial L}{\partial \mathbf{b}^{[2]}} = \delta^{[2]}$$
> Derivation for $\large \frac{\partial L}{\partial \mathbf{W}^{[2]}}$ and $\large \frac{\partial L}{\partial \mathbf{b}^{[2]}}$: [[(Subnotes) Backward Propagation Output Parameter Gradients]]
```mermaid
graph RL
    Z2[z⁽²⁾] -.->|"δ⁽²⁾(a⁽¹⁾)ᵀ"| W2[[W⁽²⁾]]
    style W2 fill:#e1f5fe,stroke:#01579b
```

|**Term**|**Calculation**|**Dimensions**|**Resulting Shape**|**Match W[2]?**|
|---|---|---|---|---|
|**Weights**|$\delta^{[2]} (\mathbf{a}^{[1]})^T$|$(2 \times 1) \times (1 \times 3)$|$2 \times 3$|**Yes**|
|**Biases**|$\delta^{[2]}$|$2 \times 1$|$2 \times 1$|**Yes**|

### Step 3.3: Hidden Layer Error ($\delta^{[1]}$)

Propagate the error through the weights $\mathbf{W}^{[2]}$ and the ReLU derivative:

$$\large \delta^{[1]} = \left( (\mathbf{W}^{[2]})^T \delta^{[2]} \right) \odot g'(\mathbf{z}^{[1]})$$

_Note: $g'(z) = 1$ if $z > 0$, else $0$._

> Derivation for $\large \delta^{[1]}$: [[(Subnotes) Backward Propagation Hidden Layer Error]]

```mermaid
graph RL
    Z2[z⁽²⁾] -.->|"(W⁽²⁾)ᵀδ⁽²⁾"| A1((a⁽¹⁾))
    A1 -.->|"δ⁽¹⁾"| Z1[z⁽¹⁾]
    style A1 fill:#ffcccc,stroke:#333
    style Z1 fill:#ffcccc,stroke:#333
```

|**Variable**|**Definition**|**Dimension**|**Set**|
|---|---|---|---|
|$(\mathbf{W}^{[2]})^{T}$|Transposed Weights|$3 \times 2$|$(\mathbf{W}^{[2]})^{T} \in \mathbb{R}^{3 \times 2}$|
|$\delta^{[1]}$|Hidden Error Gradient|$3 \times 1$|$\delta^{[1]} \in \mathbb{R}^{3}$|

### Step 3.4: Hidden Parameter Gradients

Final gradients for the first layer using input $\mathbf{x}$:

$$\large \frac{\partial L}{\partial \mathbf{W}^{[1]}} = \delta^{[1]} \mathbf{x}^T, \quad \frac{\partial L}{\partial \mathbf{b}^{[1]}} = \delta^{[1]}$$

> Derivation for $\large \frac{\partial L}{\partial \mathbf{W}^{[1]}}$ and $\large \frac{\partial L}{\partial \mathbf{b}^{[1]}}$ [[(Subnotes) Backward Propagation Hidden Parameter Gradients]]

```mermaid
graph RL
    Z1[z⁽¹⁾] -.->|"δ⁽¹⁾xᵀ"| W1[[W⁽¹⁾]]
    style W1 fill:#e1f5fe,stroke:#01579b
```

---

#### Gradient Table

| **Parameter**    | **The Chain Rule (Full Path)**                                                                                                                                    | **Substituted Final Equation**                                                         | **Dimension** |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------- |
| **Output Error** | $\frac{\partial L}{\partial \mathbf{a}^{[2]}} \cdot \frac{\partial \mathbf{a}^{[2]}}{\partial \mathbf{z}^{[2]}}$                                                  | $\large \delta^{[2]} = \mathbf{a}^{[2]} - \mathbf{y}$                                  | $2 \times 1$  |
| **Weights 2**    | $\delta^{[2]} \cdot \frac{\partial \mathbf{z}^{[2]}}{\partial \mathbf{W}^{[2]}}$                                                                                  | $\large d\mathbf{W}^{[2]} = \delta^{[2]} (\mathbf{a}^{[1]})^T$                         | $2 \times 3$  |
| **Biases 2**     | $\delta^{[2]} \cdot \frac{\partial \mathbf{z}^{[2]}}{\partial \mathbf{b}^{[2]}}$                                                                                  | $\large d\mathbf{b}^{[2]} = \delta^{[2]}$                                              | $2 \times 1$  |
| **Hidden Error** | $\left( \delta^{[2]} \cdot \frac{\partial \mathbf{z}^{[2]}}{\partial \mathbf{a}^{[1]}} \right) \odot \frac{\partial \mathbf{a}^{[1]}}{\partial \mathbf{z}^{[1]}}$ | $\large \delta^{[1]} = ((\mathbf{W}^{[2]})^T \delta^{[2]}) \odot g'(\mathbf{z}^{[1]})$ | $3 \times 1$  |
| **Weights 1**    | $\delta^{[1]} \cdot \frac{\partial \mathbf{z}^{[1]}}{\partial \mathbf{W}^{[1]}}$                                                                                  | $\large d\mathbf{W}^{[1]} = \delta^{[1]} \mathbf{x}^T$                                 | $3 \times 2$  |
| **Biases 1**     | $\delta^{[1]} \cdot \frac{\partial \mathbf{z}^{[1]}}{\partial \mathbf{b}^{[1]}}$                                                                                  | $\large d\mathbf{b}^{[1]} = \delta^{[1]}$                                              | $3 \times 1$  |

> [!tip] Implementation Note
> 
> When coding this, remember that $\mathbf{W}^{[1]}$ will be of shape $(3, 2)$ and $\mathbf{W}^{[2]}$ will be $(2, 3)$. Ensure you use the dot product for linear transforms and element-wise multiplication ($\odot$) for activation derivatives.
