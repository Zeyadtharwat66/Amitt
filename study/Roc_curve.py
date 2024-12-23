import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

# Actual values (1 = Yes, 0 = No)
y_actual = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1]

# Predicted probabilities
y_pred_prob = [0.20, 0.75, 0.50, 0.85, 0.70, 0.10, 0.90, 0.30, 0.40, 0.80]

# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_actual, y_pred_prob)

# Calculate AUC (Area Under the Curve)
roc_auc = auc(fpr, tpr)

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')  # Diagonal line (random guess)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
