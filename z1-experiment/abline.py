import matplotlib.pyplot as plt
import numpy as np

# Some dummy data
x = [1, 2]
y = [2, 3]

# Find the slope and intercept of the best fit line
slope, intercept = np.polyfit(x, y, 1)

# Create a list of values in the best fit line
ex = range(1, 10)
ey = [slope * i + intercept for i in ex]

# Plot the best fit line over the actual values
plt.plot(x, y, '--')
plt.plot(ex, ey, '*')
plt.title(slope)
plt.show()