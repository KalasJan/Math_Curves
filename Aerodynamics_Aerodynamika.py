# nakreslete dolet frisbee nebo rogala

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1) zakladni parametry
g = 9.81 # gravitacni konstanta [m/s^2]
v0 = 12 # pocatecni rychlost [m/s]
alpha = np.radians(10) # uhel vzletu nebo vrhu [rad]
h = 2 # pocatecni vyska [m]
ro = 1.225 # hustota vzduchu [kg/m^3]

# 2) volba
choose = int(input("Zadej 1 (Homogenni koule), 2 (Frisbee) nebo 3 (Model motoroveho letadla):"))

if choose == 1: # homogenni koule
    m = 1 # hmotnost objektu [kg]
    A = 0.01 # celni plocha (prurez) objektu  [m^2]
    Cd = 0.47 # soucinitel treni
    Cl = 0 # vzletova sila
    tah = 0 # tazna sila motoru
elif choose == 2: # frisbee
    m = 0.175 # hmotnost objektu [kg]
    A = 0.0572 # celni plocha (prurez) objektu  [m^2]
    Cd = 0.15 # soucinitel treni
    Cl = 0.35 # vzletova sila [N]
    tah = 0 # tazna sila motoru [N]
else: # s motorem
    m = 1 # hmotnost objektu [kg]
    A = 0.1 # celni plocha (prurez) objektu  [m^2]
    Cd = 0.08 # soucinitel treni
    Cl = 0.6 # vzletova sila [N]
    tah = 3 # tazna sila motoru [N]

F_hor = 1/2 * ro * Cd * A
F_vzt = 1/2 * ro * Cl * A

# 2) Numericky model
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
    [0, 60],
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

doba = sol.t[-1] # doba letu


# 3) Graf
plt.figure(figsize=(10, 6))
plt.plot(x_trajs, y_trajs, color='forestgreen', linewidth=2, 
         label=(f'Trajektorie letu: Dostřel: {dosah:.2f} m (čas {doba:.2f} s) | Max. výška: {vyska_max:.2f} m v {x_dal:.2f} m'))

plt.plot([0, 0], [0, h], color='gray', linewidth=6, label=f'Startovní výška ({h} m)')

# title
if choose == 1: # homogenni koule
    title = "homogenní koule"
elif choose == 2:
    title = "frisbee"
else: # s motorem
    title = "modelu motorového letadla"
    
plt.title(f"Trajektorie letu {title}" + "\n" + 
          f"(m = {m} kg, $v_0$ = {v0} m/s, $\\alpha$ = {np.degrees(alpha):.2f}°, tažná síla {tah} N)", fontsize=14)

plt.xlabel("Vzdálenost [m]")
plt.ylabel("Výška [m]")

# vrchol
# a) jak daleko
plt.axhline(vyska_max, color='red', linestyle=':', alpha=0.6)

# b) jak vysoko
x_vysoko = x_trajs[np.argmax(y_trajs)]
plt.axvline(x_vysoko, color='red', linestyle=':', alpha=0.6)

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='lower left', bbox_to_anchor=(0.1, 0.05), fontsize=11)

plt.show()
