# nakreslete dolety homogenni koule, frisbee a motoroveho letadla

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1) zakladni parametry
g = 9.81 # gravitacni konstanta [m/s^2]
v0 = 25 # pocatecni rychlost [m/s]
alpha = np.radians(10) # uhel vzletu nebo vrhu [rad]
h = 2 # pocatecni vyska [m]
ro = 1.225 # hustota vzduchu [kg/m^3]

# m = hmotnost [kg]
# A = celni plocha (prurez) objektu  [m^2]
# Cd = soucinitel treni
# Cl = 0 # vzletova sila
# tah = tazna sila motoru

objekt = [
    {"nazev": "Homogenní koule", "m": 1.0,   "A": 0.01,   "Cd": 0.47, "Cl": 0.0,  "tah": 0, "barva": "crimson"},
    {"nazev": "Frisbee",         "m": 0.175, "A": 0.0572, "Cd": 0.15, "Cl": 0.35, "tah": 0, "barva": "forestgreen"},
    {"nazev": "Motorové letadlo","m": 1.3,   "A": 0.1,    "Cd": 0.08, "Cl": 0.60, "tah": 1.3, "barva": "dodgerblue"}
]

# dopad
def dopad(t, state):
    return state[1] 
dopad.terminal = True
dopad.direction = -1

plt.figure(figsize=(12, 6))

# numerika, analytika
for obj in objekt:
    m = obj["m"]
    A = obj["A"]
    Cd = obj["Cd"]
    Cl = obj["Cl"]
    tah = obj["tah"]
    
    F_hor = 1/2 * ro * Cd * A
    F_vzt = 1/2 * ro * Cl * A
    
    def model(t, state):
        x, y, vx, vy = state
        v = np.sqrt(vx**2 + vy**2)
        
        if v < 1e-5:
            return [vx, vy, tah/m - g, 0] # prilis nizka pocatecni rychlost
        
        # jednotkove vektory
        un_x = vx/v
        un_y = vy/v
        lift_x = -un_y
        lift_y = un_x # vzlety
        
        # sily (F = m*a -> a = F / m)
        # a) odpor vzduchu
        ac_x = -(F_hor / m) * v**2 * un_x
        ac_y = -(F_hor / m) * v**2 * un_y - g
        
        # b) vztlak - kolmy na rychlost
        a_lift_x = (F_vzt / m) * v**2 * lift_x
        a_lift_y = (F_vzt / m) * v**2 * lift_y
        
        # c) tah motoru
        a_pow_x = (tah / m) * un_x
        a_pow_y = (tah / m) * un_y
        
        # total: gravitace + odpor + vztlak + tah
        ax = ac_x + a_lift_x + a_pow_x
        ay = ac_y + a_lift_y + a_pow_y
        
        return [vx, vy, ax, ay]

    # dopad na zem (y = 0)
    def dopad(t, state):
        return state[1] 
    dopad.terminal = True
    dopad.direction = -1
        
    # reseni ODE
    sol = solve_ivp(
        model,
        [0, 600],
        [0, h, v0 * np.cos(alpha), v0 * np.sin(alpha)],
        events=dopad, 
        dense_output=True, 
        max_step=0.01
    )

    x_trajs = sol.y[0]
    y_trajs = sol.y[1] # trajektorie
    dosah = x_trajs[-1] # dopad
    vyska_max = np.max(y_trajs) # max vyska
    x_dal = x_trajs[np.argmax(y_trajs)] # jak daleko od startu je vrchol

# Graf
    plt.plot(x_trajs, y_trajs, color=obj["barva"], linewidth=2, 
             label=f'{obj["nazev"]} ({m} kg, plocha {A:.2f} $m^2$, tření {Cd:.2f}, Vzletová síla {Cl:.2f} N, Síla motoru {tah} N) | Dostřel: {dosah:.1f} m, Max. výška: {vyska_max:.2f} m v {x_dal:.2f} m')

# vrchol
# a) jak daleko
    plt.axvline(x_dal, color=obj["barva"], linestyle=":", alpha=0.4)

# b) jak vysoko
    plt.axhline(vyska_max, color=obj["barva"], linestyle=":", alpha=0.4)


plt.plot([0, 0], [0, h], color='gray', linewidth=4, linestyle='--', label=f'Start ({h} m)')
plt.title("Srovnání trajektorií: Koule vs. Frisbee vs. Motorové letadlo" + "\n" +
          f"(start rychlostí {v0} m/s, z výšky {h} m pod úhlem {np.degrees(alpha)}°)", fontsize=14)
plt.xlabel("Vzdálenost [m]")
plt.ylabel("Výška [m]")
plt.axhline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fontsize=11)
plt.subplots_adjust(bottom=0.3, top=0.9, left=0.1, right=0.95)

plt.show()