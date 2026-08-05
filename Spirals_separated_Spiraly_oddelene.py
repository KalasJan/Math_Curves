# Nakresli všechny Spirály v polárních  souřadnicích
# Archimedova, Hyperbolicka, Logaritmicka, Fermatova, Lituus

import numpy as np
import matplotlib.pyplot as plt

# parametry
a = 0.5 # u vsech
b = 0.1 # jen logaritmicka

uhel = np.linspace(0.1, 10*np.pi, 1000)
# 0.1 kvuli deleni nulou u nekterych spiral, vice jak 2 pi, aby byla delsi

# 1) Archimedova
r_arc = a * uhel

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
# ax - vykreslenii soustrednych kruznic
ax.plot(uhel, r_arc, color='darkcyan', linewidth=2)
ax.grid(True, linestyle=':', alpha=0.6)
plt.title(rf'Archimedova spirala: $r = a \cdot \varphi$, kde $a = {a}$', fontsize=12)
plt.show()

# -----------------------------------------------------------------------------

# 2) Hyperbolicka
r_hyp = a / uhel

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
# ax - vykreslenii soustrednych kruznic
ax.plot(uhel, r_hyp, color='blue', linewidth=2)
ax.grid(True, linestyle=':', alpha=0.6)
plt.title(rf'Hyperbolická spirála: $r = \frac{{{a}}}{{\varphi}}$, kde $a = {a}$', fontsize=12)
plt.show()

# -----------------------------------------------------------------------------

# 3) Logaritmicka
r_log = a * np.exp(b * uhel)

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
# ax - vykreslenii soustrednych kruznic
ax.plot(uhel, r_log, color='blue', linewidth=2)
ax.grid(True, linestyle=':', alpha=0.6)
plt.title(rf'Logaritmicka spirala: $r = a \cdot e^{{b \cdot \varphi}}$, kde $a = {a}, b = {b}$', fontsize=12)
plt.show()

# -----------------------------------------------------------------------------

# 4) Fermatova
r_fer = a * np.sqrt(uhel)

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
# ax - vykreslenii soustrednych kruznic
ax.plot(uhel, r_fer, color='blue', linewidth=2)
ax.grid(True, linestyle=':', alpha=0.6)
plt.title(rf'Fermatova spirala: $r = a \cdot \sqrt{{\varphi}}$, kde $a = {a}$', fontsize=12)
plt.show()

# -----------------------------------------------------------------------------

# 5) Lituus
r_lit = a / np.sqrt(uhel)

plt.figure(figsize=(7, 7))
ax = plt.subplot(111, projection='polar')
# ax - vykreslenii soustrednych kruznic
ax.plot(uhel, r_lit, color='blue', linewidth=2)
ax.grid(True, linestyle=':', alpha=0.6)
plt.title(rf'Lituus spirala: $r = \frac{{a}}{{\sqrt{{\varphi}}}}$, kde $a = {a}$', fontsize=12)
plt.show()

