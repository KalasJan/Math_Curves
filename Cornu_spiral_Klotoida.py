# Klotoida, Cornuova spirála / Eulerova spirála
# t2, xlim a ylim -> detail konce // t - cely graf
# scatter -> (0,0) pro celou // 0.5, 0.5 pro detail

import numpy as np
import matplotlib.pyplot as plt
import scipy.special # Fresnelovy integraly

t = np.linspace(-5, 5, 1000) # parametr na rozah spiraly
t2 = np.linspace(0,10, 2000)

# Pro zrychleni vypoctu a grafu, tzv. Fresnelovy integraly

S, C = scipy.special.fresnel(t)
S2, C2 = scipy.special.fresnel(t2)

# 2 grafy vedle sebe
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# cely graf
ax1.plot(C, S, color='darkviolet', linewidth=2, label='Klotoida')
ax1.scatter(0, 0, color='black', s=60, zorder=5, label='Inflexní bod [0,0]')

ax1.set_xlabel('x (Fresnelův kosinus)')
ax1.set_ylabel('y (Fresnelův sinus)')
ax1.set_title('Celkový pohled na křivku', fontsize=12)
ax1.axis('equal')
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left')

# detail praveho/horniho konce

ax2.plot(C2, S2, color='darkviolet', linewidth=2, label='Klotoida (Detail)')
ax2.scatter(0.5, 0.5, color='crimson', s=60, zorder=5, label='Asymptotický střed [0.5, 0.5]')

ax2.set_xlabel('x (Fresnelův kosinus)')
ax2.set_ylabel('y (Fresnelův sinus)')
ax2.set_title('Detail asymptotického středu', fontsize=12)

# Omezení viditelného rozsahu pouze pro pravý graf
ax2.set_xlim(0.35, 0.65)
ax2.set_ylim(0.35, 0.65)

ax2.axis('equal')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper left')

# titulek
plt.suptitle('Klotoida (Cornuova / Eulerova spirála)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

