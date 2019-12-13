# This program plot the four graphs that pass through six points #

x= [0,1,2,3,4,5] # These are the given data
y=[1.0,2.0,1.0,0.5,4.0,8.0]
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
f1= interpolate.InterpolatedUnivariateSpline(x, y, k=1)
f2 = interpolate.InterpolatedUnivariateSpline(x, y, k=2)
f3= interpolate.InterpolatedUnivariateSpline(x, y, k=3)
f4 = interpolate.lagrange(x, y)

# Plotting
plt.xlabel('Data for x', size=18)
plt.ylabel('Data for y', size=18)
plt.tick_params(labelsize=18)
plt.title('Plot that shows the four curves passing through the six given points', size=24)

xs = np.linspace(0,5,5000)

plt.scatter(x,y,color='k')
plt.plot(xs,f1(xs),color=(1.0,0.0,0.0), lw=2)
plt.plot(xs,f2(xs),color=(0.0,1.0,0.0), lw=2)
plt.plot(xs,f3(xs),color=(0.0,0.0,1.0), lw=2)
plt.plot(xs,f4(xs),color=(0.7,0.3,0.5), ls='--',lw=2)
plt.legend(['Linear','Quadratic','Cubic','Lagrange'])

plt.grid()
plt.show()