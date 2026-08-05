# Nakresli cykloidu
# jde pouze parametricky


import numpy as np
import matplotlib.pyplot as plt

# parametry
r = 10 # polomer kruznice
x0, y0 = 0, 0 # pocatek

t = np.linspace(-4*np.pi, 4*np.pi, 1000) # uhel otoceni 

# soustava
ox = x0 + r*(t-np.sin(t))
oy = y0 + r*(1-np.cos(t)) 

# Vykresleni Cykloidy
 
plt.plot(ox, oy, color='darkcyan', linewidth=2)
plt.scatter(x0, y0, color='black', s=50)
plt.xlabel('x')
plt.ylabel('y')
plt.title(rf'Cykloida $x = x_0 + {r}(t - \sin(t))$, $y = y_0 + {r}(1 - \cos(t))$', fontsize=12)
plt.axis('equal') # jinak se graf protahne/zhusti

plt.tight_layout()
plt.show()

