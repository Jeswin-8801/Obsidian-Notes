
Here is the structured markdown for your Obsidian notes. I’ve formatted the math using LaTeX so it renders perfectly with Obsidian’s Core MathJax plugin.
Classification Metrics
> Source: Machine Learning Basics
> Tags: #machine-learning #statistics #classification
> 
The Confusion Matrix
Before calculating metrics, we define the four outcomes of a binary classifier:
 * TP (True Positive): Predicted Positive, Actual Positive.
 * TN (True Negative): Predicted Negative, Actual Negative.
 * FP (False Positive): Predicted Positive, Actual Negative (Type I Error).
 * FN (False Negative): Predicted Negative, Actual Positive (Type II Error).
Core Formulas
1. Accuracy
Measures the total percentage of correct predictions.

2. Precision
Focuses on the quality of positive predictions. "Of all predicted positives, how many were correct?"

3. Recall (Sensitivity)
Focuses on the ability to find all positive instances. "Of all actual positives, how many did we catch?"

4. F1 Score
The harmonic mean of Precision and Recall. Use this when you have imbalanced classes.

Summary Table

| Metric | Focus | Best For... |
|---|---|---|
| Accuracy | Overall Correctness | Balanced datasets |
| Precision | Reliability of "Yes" | Avoiding False Positives (e.g., Spam Filters) |
| Recall | Coverage of "Yes" | Avoiding False Negatives (e.g., Cancer Detection) |
| F1 Score | Balance | When both FP and FN are costly |
Implementation (Python)
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Example labels
y_true = [0, 1, 1, 0, 1, 1]
y_pred = [0, 0, 1, 0, 1, 1]

print(f"Accuracy: {accuracy_score(y_true, y_pred):.4f}")
print(f"Precision: {precision_score(y_true, y_pred):.4f}")
print(f"Recall: {recall_score(y_true, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_true, y_pred):.4f}")

Would you like me to also format the k-NN calculation from the image into a separate Obsidian note for your "Practice Problems" folder?
