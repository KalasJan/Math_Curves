# Vykresli Brachistochronu a Tautochronu
# je dána trasa A - B. 
# Brachistochrona - krivka, po ktere bod zvladne trasu AB za co nejkratsi cas
# Tautochrona - krivka, po ktere body dorazi do cile ve stejny moment bez ohledu na zacatek

import numpy as np
import matplotlib.pyplot as plt

# Společné parametry
R = 4.0 #polomer kruznice cykloidy

# 1) Brachistochrona (Optimalizace času mezi A (start) a B(nejniz))

# definujeme funkci

uhel_brach = np.linspace(0, np.pi, 500)

def brach(R, uhel_brach):
    xb = R * (uhel_brach - np.sin(uhel_brach))
    yb = -R * (1 - np.cos(uhel_brach))
    return xb, yb

xb, yb = brach(R, uhel_brach)

# 2) Tautochrona (Izochronní pohyb z různých výšek)

# definujeme funkci

uhel_tauto = np.linspace(-np.pi, 0, 500) # kvuli posunu krivky

def tauto(R, uhel_tauto):
    xt = R * (uhel_tauto + np.sin(uhel_tauto)) + R*np.pi # posun
    yt = -R * (1 - np.cos(uhel_tauto))
    return xt, yt

xt, yt = tauto(R, uhel_tauto)

# graf
plt.figure(figsize=(5, 5))
plt.plot(xb, yb, label='Brachistochrona', color='red', linewidth=2) # Brachistochrona
plt.plot(xt, yt, label='Tautochrona', color='blue') # Tautochrona
plt.xlabel("x") # osa x
plt.ylabel("y") # osa y
plt.title("Grafy Brachistochrony a Tautochrony")
plt.axis('equal')
plt.legend()
plt.grid(True)
plt.show()