# Plot the Lissajous curve

import numpy as np
import matplotlib.pyplot as plt
import math

# parameters
a = 7
b = 6

k = 3
delta = np.pi / k
# other: a = 6, b = 8, delta = pi/2 // a = 4, b = 5, delta = pi

t = np.linspace(-4*np.pi, 4*np.pi, 1000)

# equation
ox = np.sin(a * t + delta)
oy = np.sin(b*t)

# ratio
gcd = math.gcd(a, b) # greatest common divisor
if gcd > 1:
    ratio_str = f'a/b = {a}/{b} = {a//gcd}/{b//gcd}'
else:
    ratio_str = f'a/b = {a}/{b}'

# Plot the curve
 
plt.figure(figsize=(9,9), layout='constrained')

plt.plot(ox, oy, color='darkcyan', linewidth=2)

plt.axvline(0, color='gray', linewidth=1, linestyle='--', alpha=0.4)
plt.axhline(0, color='gray', linewidth=1, linestyle='--', alpha=0.4)

plt.xlabel('x')
plt.ylabel('y')
plt.title(
    r'Lissajous curve:' + '\n' + 
    r'$x(t) = \sin(a \cdot t + \delta)$ ; $y(t) = \sin(b \cdot t)$',
    fontsize=12)

plt.text(
    1.03, 1, # position (left upper)
    fr'$a = {a}$ ; $b = {b}$' + '\n' +
    fr'Ratio: {ratio_str}' + '\n' +
    fr'$\delta = \pi/{k}$',
    transform=plt.gca().transAxes,
    verticalalignment='top',
    fontsize=11,
    bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8, edgecolor='gray')
    )

plt.axis('equal') # ratio x:y = 1:1
plt.show()