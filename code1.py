import numpy as np
import matplotlib.pyplot as plt

# Initial Parameter
r = 100  # Average revenue per visitor
gamma = 0.5  # Average environment impact per visitor
D_t = 5000  # The number of visitors
alpha = 0.2  # Environmental Reinvestment Ratio
beta = 2  # Environmental Protection Weight

# Objective function
def calculate_Z(D_t, r, gamma, alpha, beta):
    return D_t * (r * (1 - alpha) - beta * gamma)

# Calculating sensivity
def sensitivity_analysis(param_name, base_value, percentage_changes, D_t, r, gamma, alpha, beta):
    Z_values = []
    for change in percentage_changes:
        new_value = base_value * (1 + change / 100)
        if param_name == "D_t":
            Z = calculate_Z(new_value, r, gamma, alpha, beta)
        elif param_name == "r":
            Z = calculate_Z(D_t, new_value, gamma, alpha, beta)
        elif param_name == "gamma":
            Z = calculate_Z(D_t, r, new_value, alpha, beta)
        elif param_name == "alpha":
            Z = calculate_Z(D_t, r, gamma, new_value, beta)
        elif param_name == "beta":
            Z = calculate_Z(D_t, r, gamma, alpha, new_value)
        Z_values.append(Z)
    return Z_values

# Range of changes
percentage_changes = [-30, -20, -10, 0, 10, 20, 30]

# Sensitivity analysis for each parameter
params = {"D_t": D_t, "r": r, "gamma": gamma, "alpha": alpha, "beta": beta}
sensitivity_results = {}

for param, base_value in params.items():
    sensitivity_results[param] = sensitivity_analysis(param, base_value, percentage_changes, D_t, r, gamma, alpha, beta)

# Drawing graph
for param, Z_values in sensitivity_results.items():
    plt.plot(percentage_changes, Z_values, label=f"{param}")

plt.title("Sensitivity analysis of the objective function Z")
plt.xlabel("Change of parameter (%)")
plt.ylabel("Value of the objective function Z")
plt.legend()
plt.grid(True)
plt.show()