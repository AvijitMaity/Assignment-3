# This program shows how to fit cubic spline to this data #

x= [0,1,2,3,4,5]  # These are the given data
y=[1.0,2.0,1.0,0.5,4.0,8.0]

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
f3 = interpolate.InterpolatedUnivariateSpline(x, y, k=3)

# Plotting
plt.xlabel('Data for x', size=24)
plt.ylabel('Data for y', size=24)
plt.tick_params(labelsize=18)
plt.title('Cubic spline', size=24)

xs = np.linspace(0,5,5000)

plt.scatter(x,y,color=(0.0,1.0,0.0))
plt.plot(xs,f3(xs),color=(0.0,0.0,1.0), lw=2)

plt.grid()
plt.show()