# je dana funkce f(x,y) = 2* (x**2) + 3* (y**2)
# 1) vypocitejte derivaci implicitni fce f = 0
# 2) tecna a normala f v bode T [1, 1] + graf
# 3) tecna rovina z = f(x,y) v T [1, 1, (z0))]

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

x, y, z = sm.symbols('x y z')

def f(x,y):
    return 2* (x**2) + 3* (y**2)

# ===============================================

# 1) derivace implicitni funkce

# a) naprimo
der_A = sm.idiff(f(x,y), y, x)
print (f" Derivace napřímo je y'= {der_A} ")

# vzorcem -dx / dy
dx = sm.diff(f(x,y), x)
dy = sm.diff(f(x,y), y)

der_B = -dx / dy
print (f" Derivace vzorcem je y'= {der_B} ")

# =================================================

# 2) tecna v bode [x0, y0] = [1,1]

x0 = 1
y0 = 1
z0 = f(x0, y0)

# tecna: y = f'(x0)*(x-x0) + y0
# normala: y = -1/f'(x0)*(x-x0) + y0

der_x0 = float(der_A.subs({x: x0, y: y0}).evalf())
norm_x0 = -1/der_x0

tecna = der_x0 * (x - x0) + y0
normala = norm_x0 * (x - x0) + y0

tecna = sm.simplify(tecna).evalf(2)
normala = sm.simplify(normala).evalf(2)

print (f' Rovnice tečny v bodě [{x0}, {y0}] je y = {tecna}')
print (f' Rovnice normály v bodě [{x0}, {y0}] je y = {normala}')

# ==============================================================
# 3) vykresleni grafu, tecny a normaly

# mrizka
x_num = np.linspace(-3, 3, 500)
y_num = np.linspace(-3, 3, 500)
X, Y = np.meshgrid(x_num, y_num)

# prevod SymPy na NumPy
f_tecna = sm.lambdify(x, tecna, 'numpy')
f_normala = sm.lambdify(x, normala, 'numpy')

# y-souradnice primek
Y_tecna = f_tecna(x_num)
Y_normala = f_normala(x_num)

plt.figure(figsize=(10, 10)) # rozmery

# pomocne osy, x = 0, y = 0
plt.axhline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.4)
plt.axvline(0, color='gray', linewidth=0.8, linestyle='--', alpha=0.4)

# vykresleni krivky
plt.contour(X, Y, f(X,Y), levels=[z0], colors='black', linewidths=2.5, zorder=2)

# tecna, normala a bod
plt.plot(x_num, Y_tecna, color='limegreen', linewidth=2, label=f'Tečna: y = {tecna}', zorder=3)
plt.plot(x_num, Y_normala, color='royalblue', linewidth=2, linestyle = '--', label=f'Normála: y = {normala}', zorder=3)
plt.scatter(x0, y0, color='crimson', s=150, edgecolors='black', zorder=5, label=f'Bod dotyku P[{x0}, {y0}]')

plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.axis('equal')  # tecna a normala budou i vypadat kolme
plt.xlabel('Osa X', fontsize=12)
plt.ylabel('Osa Y', fontsize=12)
plt.title(r'Graf tečny a normály k implicitně dané funkci $f(x,y) = 2x^2 + 3y^2$', fontsize=13, weight='bold', pad=15)
plt.grid(True, linestyle=':', alpha=0.4)
plt.legend(loc='lower left', fontsize=11)

# ===================================================================

# 4) f(x,y) = 2* (x**2) + 3* (y**2), rovnice tecne roviny v [1,1,z0]

# rovnice tecne roviny: z - z0 = dx(T) * (x - x0) + dy(T) * (y - y0)

dxT = float(dx.subs({x: x0, y: y0}))
dyT = float(dy.subs({x: x0, y: y0}))


tecna_rovina = dxT * (x - x0) + dyT * (y - y0) - (z - z0)

obecna_rovina = sm.simplify(tecna_rovina)

print(f" Obecná rovnice tečné roviny v bodě T[{x0}, {y0}, {z0}] je {obecna_rovina} = 0")

# ====================================================================

# 5) 3D graf f(x,y) spolu s tecnou rovinou

x_3d = np.linspace(-2, 2, 100)
y_3d = np.linspace(-2, 2, 100)
X3D, Y3D = np.meshgrid(x_3d, y_3d)

Z3D = f(X3D, Y3D) # 3D graf f(x,y)

rovina_3D = sm.solve(tecna_rovina, z)[0] # z = ... 

#prevod SymPy na NumPy
f_rov = sm.lambdify((x, y), rovina_3D, 'numpy')

Z_rov = f_rov(X3D, Y3D) # matice vysek v jednotlivych bodech

# vykresleni

# zaklad - rozmery, 3D, uhel
fig = plt.figure(figsize=(12, 10))
ax3d = fig.add_subplot(111, projection='3d')
ax3d.view_init(elev=45, azim=50)

# funkce
ax3d.plot_surface(X3D, Y3D, Z3D, cmap='ocean', alpha=0.5, zorder=1)

# rovina
ax3d.plot_surface(X3D, Y3D, Z_rov, color='orange', alpha=0.4, zorder=2)

# bod dotyku
ax3d.scatter(x0, y0, float(z0), color='red', s=100, zorder=5, 
             label=f'Bod dotyku $T[{x0}, {y0}, {float(z0):.0f}]$')

ax3d.set_xlabel('Osa X', fontsize=11)
ax3d.set_ylabel('Osa Y', fontsize=11)
ax3d.set_zlabel('Osa Z', fontsize=11)
ax3d.set_title(r'3D Geometrie: Tečná rovina k ploše $z = 2x^2 + 3y^2$', fontsize=13, weight='bold', pad=15)
ax3d.legend(loc='upper right')

plt.tight_layout()

# ======================================================

# 6) vektor normalovych rovin

nx = -dxT
ny = -dyT
nz = 1

norm = np.sqrt(nx**2 + ny**2 + nz**2)

# normalizace (delka je 1)
nx0 = nx / norm
ny0 = ny / norm
nz0 = nz / norm

print(f" Jednotkový normálový vektor všech rovin normál má souřadnice ({nx0:.2f}, {ny0:.2f}, {nz0:.2f})")

# vykresleni vektoru
ax3d.quiver(x0, y0, float(z0), nx0, ny0, nz0, 
            color='royalblue', linewidth=3, arrow_length_ratio=0.3, zorder=6,
            label=r'Jednotková normála $\vec{n}_0$')

ax3d.set_xlabel('Osa X', fontsize=11)
ax3d.set_ylabel('Osa Y', fontsize=11)
ax3d.set_zlabel('Osa Z (Výška)', fontsize=11)
ax3d.set_title(r'3D Geometrie: Tečná rovina a jednotkový vektor $\vec{n}_0$', fontsize=13, weight='bold', pad=15)
ax3d.legend(loc='upper right')

plt.tight_layout()
plt.show()