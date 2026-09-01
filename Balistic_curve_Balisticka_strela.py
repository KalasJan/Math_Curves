# Jak se liší dosah střely o hmotnosti (m) vystřelené pod úhlem (alpha) z výšky (h)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# 1) parametry (JEDINE MENIT)
g = 9.81 # gravitacni konstanta [m/s^2]

v0 = 10 # pocatecni rychlost [m/s]
alpha = np.radians(0) # uhel vrhu (prevod stupnu na radiany)
# 42 optimalni, 0 vodorovny vrh (nenulove h), 90 svisly vzhuru
# -90 (nebo 270) je svisly dolu (a pro v0 = 0 je volny pad)
h = 100 # vyska, ze ktere se strili [m]
m = 1 # hmotnost objektu [kg]

ro = 1.225 # hustota (vzduchu) [kg/m^3]
Cd = 0.47 # soucinitel treni

ro_material = 800 # hustota oceli (nebo jineho materialu) [kg/m^3]
# ocel 7850, drevo 650-1100, plast 900-2200
V = m / ro_material
pol = (3 * V / (4 * np.pi))**(1/3) # polomer koule
# pol = 0.033
A = np.pi * (pol**2) # celni plocha (prurez) objektu  [m^2]

k = 1/2 * ro * Cd * A # koeficient odporu

# 2) Idealni sikmy vrh (bez treni)
# y(t) = h + v0 * sin(alpha) * t - 1/2 g*t^2 // dopad: y(t) = 0

kva = -1/2 * g
kvb = v0 * np.sin(alpha)
kvc = h

idealni_let = (-kvb - np.sqrt(kvb**2 - 4 * kva * kvc)) / (2 * kva)

t_ideal = np.linspace(0, idealni_let, 500)
x_ideal = v0 * np.cos(alpha) * t_ideal
y_ideal = h + v0 * np.sin(alpha) * t_ideal - 0.5 * g * t_ideal**2

vyska_max_ideal = np.max(y_ideal) # maximalni vyska
dosah_ideal = x_ideal[-1] # maximalni vzdalenost

doba_letu_ideal = idealni_let # doba letu

# 3) Balisticka strela (vliv treni, odporu vzduchu)

def balistic (t, state):
    x, y, vx, vy = state
    v = (vx**2 + vy**2) ** (1/2)
    ax = -(k / m) * v * vx
    ay = -g - (k / m) * v * vy
    return [vx, vy, ax, ay]

# dopad (y = 0)
def dopad (t, state):
    return state[1] 
dopad.terminal = True
dopad.direction = -1 # sestup (pad) na zem

# reseni ODE
sol = solve_ivp(
    balistic,
    [0, 600], # kvuli pocatecni vysce, doba letu [sec]
    [0, h, v0 * np.cos(alpha), v0 * np.sin(alpha)], # start a smer
    events=dopad, 
    dense_output=True, 
    max_step=0.01)

x_bal = sol.y[0]
y_bal = sol.y[1]

vyska_max_real = np.max(y_bal) # maximalni vyska
dosah_max_real = x_bal[-1] # maximalni vzdalenost

doba_letu_real = sol.t[-1] # doba letu

# 4) graf
plt.figure(figsize=(10,6))

# krivky
plt.plot(x_ideal, y_ideal, label=f'Ideální vrh (bez odporu) | Dostřel: {dosah_ideal:.2f} m, Doba letu: {doba_letu_ideal:.2f} s', linestyle='--', color='blue', linewidth=2)
plt.plot(x_bal, y_bal, label=f'Balistická střela (s odporem) | Dostřel: {dosah_max_real:.2f} m, Doba letu: {doba_letu_real:.2f} s', color='red', linewidth=2)

# Zvyrazneni pocatecni vysky
plt.plot([0, 0], [0, h], color='gray', linewidth=6, label=f'Startovní výška ({h} m)')

# vrcholy (maximum strely)
# a) jak daleko od vystrelu
plt.axhline(vyska_max_ideal, color='blue', linestyle=':', alpha=0.6)
plt.axhline(vyska_max_real, color='red', linestyle=':', alpha=0.6)

# v) jak vysoko
x_vrchol_ideal = x_ideal[np.argmax(y_ideal)]
x_vrchol_real = x_bal[np.argmax(y_bal)]

plt.axvline(x_vrchol_ideal, color='blue', linestyle=':', alpha=0.6)
plt.axvline(x_vrchol_real, color='red', linestyle=':', alpha=0.6)

# rozdil
arrow = -1

plt.annotate('', xy=(dosah_ideal, arrow), 
             xytext=(dosah_max_real, arrow),
             arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
distance = dosah_ideal - dosah_max_real
plt.text((dosah_ideal + dosah_max_real)/2, arrow + 1.5, 
         f'{distance:.2f}m', 
         ha='center', fontsize=10, weight='bold')

# Zahlavi
plt.title(f"Porovnání střely tělesa o hmotnosti {m} kg" + '\n' +
          f"Šikmý vrh vs. Balistická střela ($v_0 = {v0}$ m/s, $\\alpha = {np.degrees(alpha):.1f}°$, $h = {h}$ m)", fontsize=12)
plt.xlabel("Vzdálenost [m]")
plt.ylabel("Výška [m]")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='lower left', bbox_to_anchor=(0.1, 0.05), fontsize=11)

plt.show()

# 5) Vysledky
print(f"--- VÝSLEDKY (START Z VĚŽE {h} m) ---")
print(f"Ideální vrh -> Max. výška: {vyska_max_ideal:.2f} m | Celkový dostřel: {dosah_ideal:.2f} m")
print(f"Balistická -> Max. výška: {vyska_max_real:.2f} m | Celkový dostřel: {dosah_max_real:.2f} m")
print(f"Ztráta dostřelu kvůli odporu: {distance:.2f} m")

# 6) Pod jakym uhlem strelit, aby dosah byl Dana vzdalenost
cil = 100 # cilova vzdalenost [m]

def chyba(uhel):
    a_rad = np.radians(uhel) # prevod na radiany
    
    sol = solve_ivp(
        balistic,
        [0, 600], # kvuli pocatecni vysce, doba letu [sec]
        [0, h, v0 * np.cos(a_rad), v0 * np.sin(a_rad)], # start a smer
        events=dopad, 
        dense_output=True, 
        max_step=0.01) # kopie reseni ODE z predchozi casti
    
    return sol.y[0][-1] - cil

if dosah_max_real < cil:
    print(f"CHYBA: Cíl {cil} m je pro tyto parametry fyzicky nedosažitelný! (Max dostřel je {dosah_max_real:.2f} m)")
else:
    uhel1 = brentq(chyba, 1, 45) # uhel v intervalu 1 - 45 deg
    uhel2 = brentq(chyba, 45, 89) #↔ vetsi uhel, interval 45- 90 deg
    print(f"Pro trefení {cil} m je třeba úhel {uhel1:.2f}° nebo {uhel2:.2f}°")