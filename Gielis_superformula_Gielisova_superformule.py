# plot the Gielis superformula
# https://www.facebook.com/reel/815585788280660

import numpy as np
import matplotlib.pyplot as plt

#parameters
m = 5 # points, corners, or symmetries (pocet cipu)
n1 = 2 # overall roundness or sharpness of the shape (zaoblenost nebo ostrost tvaru)
n2 = 7 # stretches toward the corners or curves inward (táhne k rohům nebo se prohýbá dovnitř)
n3 = 7 # stretches toward the corners or curves inward (táhne k rohům nebo se prohýbá dovnitř)
a = 4 # length of axes (delka poloosy)
b = 6 # length of axes (delka poloosy)

# other options: (m, n1, n2, n3):
# sphere: 0, 2, 2, 2
# starfish: 5, 2, 7, 7
# seashell: 8, 5, 5, 5 
# orchid: 6, 1, 4, 8
# rounded triangle: 3, 4.5, 10, 10 
# squircle: 4, 12, 15, 15
# spiked flower: 7, 3, 4, 17
# cog: 12, 15, 20, 20
# star decagon: 10, 2, 10, 10

# axis
t = np.linspace(0, 2*np.pi, 500)
k = np.linspace(-np.pi / 2, np.pi / 2, 300)
T, K = np.meshgrid(t, k)

# divide by 0, radius
def superformula(angle, m, n1, n2, n3, a, b):
    term = (
        np.abs(np.cos(m * angle / 4) / a) ** n2
        + np.abs(np.sin(m * angle / 4) / b) ** n3
    )

    with np.errstate(divide='ignore', invalid='ignore'):
        R = term ** (-1 / n1)
        R[np.isnan(R)] = 0
    return R

R1 = superformula(T, m, n1, n2, n3, a, b)
R2 = superformula(K, m, n1, n2, n3, a, b)

# polar
X = R1 * R2 * np.cos(T) * np.cos(K)
Y = R1 * R2 * np.sin(T) * np.cos(K)
Z = R2 * np.sin(K)

# plot the graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

ax.set_title(r'3D objekt s průřezem „kytky“ ($r(\varphi)$)', fontsize=14, pad=20)
ax.axis('off')

plt.show()