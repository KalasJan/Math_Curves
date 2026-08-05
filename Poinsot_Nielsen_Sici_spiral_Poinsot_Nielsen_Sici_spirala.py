# Vykresleni slozitejsich spiral
# Poinsotova a Nielsenova spirala (tzv. sici spiral)
# Evolventa / involve curve

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sici  # Nielsenovu spirálu

# 1) Poinsotova spirala
# r = a * sech(b * uhel_poi)

uhel_poi = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
a_poi = 2
b_poi = 0.3

# polomer (pres tzv. hyperbolicky sekans, sech = 1/cosh(x))
r_poi = a_poi / np.cosh(b_poi * uhel_poi)

# kartezsky
x_poi = r_poi * np.cos(uhel_poi)
y_poi = r_poi * np.sin(uhel_poi)

# kresleni 

# KRESLENÍ (Čistý způsob bez zakládání a následného mazání os)
fig1 = plt.figure(figsize=(14, 6))

# kartezsky graf
ax1_1 = fig1.add_subplot(121)
ax1_1.plot(x_poi, y_poi, color='darkorange', linewidth=2)
ax1_1.set_title("Poinsotova spirála (Kartézsky)")
ax1_1.grid(True)
ax1_1.axis('equal')

# polarne
ax1_2 = fig1.add_subplot(122, projection='polar')
ax1_2.plot(uhel_poi, r_poi, color='darkorange', linewidth=2)
ax1_2.set_title("Poinsotova spirála (Polárně)", pad=15)
ax1_2.grid(True, linestyle=':', alpha=0.6)

# hlavni nadpis
plt.suptitle("Poinsotova spirála: $r = {a_poi} \cdot \operatorname{{sech}}({b_poi}\varphi)$", fontsize=14, weight='bold')
plt.tight_layout()

# ----------------------------------------------------

# 2) Nielsenova spirala (Sici spiral)
# x = ci(t), y = si(t)

t_nie = np.linspace(0.1, 20, 10000) # nemuzeme od 0, protoze singularita
si, ci = sici(t_nie) # Sici funkce (Co/Sine integral)

# Polarizace souradnic
r_nie = np.sqrt(ci**2 + si**2)
uhel_nie = np.arctan2(si, ci)

# KRESLENÍ (Čistý způsob add_subplot)
fig2 = plt.figure(figsize=(14, 6))

# kartezsky graf
ax2_1 = fig2.add_subplot(121)
ax2_1.plot(ci, si, color='purple', linewidth=2)
ax2_1.set_title("Nielsenova spirála (Kartézsky)")
ax2_1.grid(True)
ax2_1.axis('equal')

# polarne
ax2_2 = fig2.add_subplot(122, projection='polar')
ax2_2.plot(uhel_nie, r_nie, color='purple', linewidth=2)
ax2_2.set_title("Nielsenova spirála (Polárně)", pad=15)
ax2_2.grid(True, linestyle=':', alpha=0.6)

# hlavni nadpis
plt.suptitle("Nielsenova (SiCi) spirála: $x = \operatorname{Ci}(t), y = \operatorname{Si}(t)$", fontsize=14, weight='bold')
plt.tight_layout()
plt.show()

