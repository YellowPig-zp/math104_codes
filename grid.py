import numpy as np
from matplotlib.pylab import plt


fig, ax = plt.subplots()
plt.legend()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.grid()
plt.ylim(-4.5,4.5)
plt.xlim(-5.5,5.5)
ax.xaxis.set_ticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
plt.show()	

