# plot the Fibonacci pattern (sunflower)

import numpy as np
import matplotlib.pyplot as plt

N = 1000 # max radius of the circle

fi = (1 + np.sqrt(5)) / 2 # golden ratio

i = np.arange(N) # indexes of points

r = np.sqrt(i / N) # growing radius

angle = 2 * np.pi * i / (fi**2) # golden angle (137.5 deg) in rad

# system
ox = r * np.cos(angle)
oy = r * np.sin(angle)

# plot
plt.figure(figsize=(8, 8))

plt.scatter(ox, oy, c=r, cmap='YlOrBr', s=40, edgecolor='saddlebrown', linewidth=0.5)

plt.axis('off')
plt.title(r'Fibonacci pattern / Sunflower with Golden Ratio: $\varphi = \frac{1 + \sqrt{5}}{2}$', fontsize=14)
plt.axis('equal')
plt.tight_layout()
plt.show()