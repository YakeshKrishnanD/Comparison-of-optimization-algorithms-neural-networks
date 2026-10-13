import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the pre-calculated results from the Colab runs
try:
    df_summary = pd.read_csv('optimizer_results.csv')
    df_curves = pd.read_csv('loss_curves.csv')
except FileNotFoundError:
    print("Error: Please make sure 'optimizer_results.csv' and 'loss_curves.csv' are in this directory.")
    exit()

# 2. Display the Comparison Table
print("\n" + "="*60)
print("       NEURAL NETWORK OPTIMIZATION COMPARISON TABLE")
print("="*60)
print(df_summary.to_string(index=False))
print("="*60 + "\n")

# 3. Plot Loss Curves Side-by-Side
plt.figure(figsize=(14, 6))

# Training Loss Plot
plt.subplot(1, 2, 1)
for col in df_curves.columns:
    if 'train_loss' in col:
        plt.plot(df_curves['Epoch'], df_curves[col], marker='o', label=col.replace('_train_loss', ''))
plt.title('Training Loss Convergence Journey')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

# Validation Loss Plot
plt.subplot(1, 2, 2)
for col in df_curves.columns:
    if 'val_loss' in col:
        plt.plot(df_curves['Epoch'], df_curves[col], marker='s', label=col.replace('_val_loss', ''))
plt.title('Validation Loss Stability')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.tight_layout()
plt.show()