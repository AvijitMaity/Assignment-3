# This program find the unique fifth order polynomial that passes through the six points using lagrange method

x= [0,1,2,3,4,5]   # These are the given data
y=[1.0,2.0,1.0,0.5,4.0,8.0]
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
f4 = interpolate.lagrange(x, y)

# Plotting
plt.xlabel('Data for x', size=24)
plt.ylabel('Data for y', size=24)
plt.tick_params(labelsize=18)
plt.title('Lagrange polynomial', size=24)

xs = np.linspace(0,5,5000)

plt.scatter(x,y,color=(0.1,0.0,0.0))
plt.plot(xs,f4(xs),color=(0.7,0.3,0.5), ls='--',lw=2)

plt.grid()
plt.show()