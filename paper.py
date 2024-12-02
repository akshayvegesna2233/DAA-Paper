import matplotlib.pyplot as plt
import numpy as np

# Data: Number sizes and execution times (hypothetical values for demonstration)
number_sizes = [10**2, 10**4, 10**6, 10**8]  # Example input sizes
trial_division_times = [0.01, 10, 1000, 100000]  # Hypothetical times in seconds
pollards_rho_times = [0.001, 1, 100, 10000]
gnfs_times = [0.0001, 0.1, 10, 1000]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(number_sizes, trial_division_times, label="Trial Division", marker='o')
plt.plot(number_sizes, pollards_rho_times, label="Pollard's Rho", marker='s')
plt.plot(number_sizes, gnfs_times, label="GNFS", marker='^')

# Log scale for better visualization
plt.xscale('log')
plt.yscale('log')

# Labels and title
plt.title("Execution Time of Integer Factorization Algorithms", fontsize=14)
plt.xlabel("Number Size (N)", fontsize=12)
plt.ylabel("Execution Time (seconds)", fontsize=12)
plt.legend()
plt.grid(True, which="both", linestyle='--', linewidth=0.5)

# Show the plot
plt.tight_layout()
plt.show()
