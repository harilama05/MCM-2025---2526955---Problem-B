import numpy as np
import matplotlib.pyplot as plt

# Example data
D_t_values = [1200, 800]  # Number of tourists before and after applying the model
r_values = [60, 80]       # Average ticket price before and after applying the model
alpha = 0.3               # Environmental reinvestment rate
beta = 2                  # Environmental protection weight
gamma = 0.3               # Environmental impact per tourist

# Calculate values
Z_values = []
E_t_values = []

for D_t, r in zip(D_t_values, r_values):
    Z = D_t * (r * (1 - alpha) - beta * gamma)  # Overal benefit
    E_t = D_t * gamma                          # Environmental impact
    Z_values.append(Z)
    E_t_values.append(E_t)

    # Print the data to the console
    print(f"Number of tourists: {D_t}, Average ticket price: {r}")
    print(f"Net revenue (Z): {Z}")
    print(f"Environmental impact (E_t): {E_t}")
    print("-" * 30)

# Data for plotting the chart
categories = ['Overal benefit (Z)', 'Environmental impact (E_t)']
before_values = [Z_values[0], E_t_values[0]]
after_values = [Z_values[1], E_t_values[1]]

# Plot the chart
x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(x - width/2, before_values, width, label='Before applying the model', color='skyblue')
bar2 = ax.bar(x + width/2, after_values, width, label='After applying the model', color='orange')

# Add labels and title
ax.set_ylabel('Value')
ax.set_title('Comparison of before and after applying the model to the tourist destination')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Display values on top of bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., 1.01*height,
                f'{int(height)}', ha='center', va='bottom', fontsize=10)

add_labels(bar1)
add_labels(bar2)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()