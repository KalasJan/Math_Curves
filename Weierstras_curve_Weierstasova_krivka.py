# plot the Weierstrass curve
# for N = 1, 2 .. 5
# x(t) = sum (n=0 to N) (1/2)**n * cos(3**n * t)
# y(t) = sum (n=0 to N) (1/2)**n * sin(3**n * t)

import numpy as np
import matplotlib.pyplot as plt

# parameters
Num = [1, 2, 3, 4, 5]
t = np.linspace (0, 4 * np.pi, 2000)

# subgraphs
fig, axs = plt.subplots(2, 3, figsize=(15, 5), sharex=True, sharey=True)
fig.suptitle('Weierstrass Parametric Curves for Different N', fontsize=16)

axs_flat = axs.flatten() # Flatten 2D array to 1D for easier iteration

# definition
for i, N in enumerate(Num):
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    
    for k in range (N+1):
        x += (1/2)**k * np.cos(3**k * t)
        y += (1/2)**k * np.sin(3**k * t)

    ax = axs_flat[i]

    # 1 curve
    ax.plot(x, y, color='crimson', linewidth=1.0)

    # details
    ax.set_title(f'N = {N}', fontsize=12)
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.6, 1.6)
    ax.set_aspect('equal')  
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_xlabel('x(t)', fontsize=12)
    ax.set_ylabel('y(t)', fontsize=12)
    
# empty place - write the equations
empty_ax = axs_flat[5]
empty_ax.axis('off') # need only 5 graphs, not 6

# equation
equation = (
    r"$x(t) = \sum_{n=0}^{N} \left(\frac{1}{2}\right)^n \cos(3^n t)$"
    "\n\n"
    r"$y(t) = \sum_{n=0}^{N} \left(\frac{1}{2}\right)^n \sin(3^n t)$"
)

empty_ax.text(0.5, 0.5, equation, fontsize=14, ha="center", va="center",
    transform=empty_ax.transAxes,  # Center in the subplot
    bbox=dict(
        boxstyle="round,pad=1",
        facecolor="whitesmoke",
        edgecolor="lightgray",
        linewidth=1,),)
    
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # space for title

plt.show()