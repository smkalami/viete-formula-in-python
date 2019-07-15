# Simulating Viete Formula for Approximation of pi

import numpy as np
import matplotlib.pyplot as plt

# Number of Terms
N = 20

# Initialize Sequence
x = np.empty(N + 1)
x[0] = 1
x[1] = 2

# Denominator
d = np.sqrt(2)

# Calculate the Sequence Terms
for i in range(2, N + 1):
    x[i] = x[i-1] * 2/d
    d = np.sqrt(2 + d)

# Plot Terms
plt.subplot(1, 2, 1)
plt.plot(x)
plt.plot([0, N], [np.pi, np.pi], 'r:')
plt.title('Viete Sequence')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)
plt.xlim(0, N)

# Plot Errors
plt.subplot(1, 2, 2)
plt.semilogy(np.pi - x)
plt.title('Approximation Error')
plt.xlabel('n')
plt.ylabel('Error')
plt.grid(True)
plt.xlim(0, N)

# Show Plots
plt.show()
