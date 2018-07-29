import numpy as np
from matplotlib.pylab import plt

def getf(i):
	return lambda x:x**i
xs = np.linspace(0, 1, 5000)
fs = []
for i in range(1, 10):
	fs.append(getf(i))
yss = [[f(x) for x in xs] for f in fs]
ax = plt.subplot()
for i, ys in enumerate(yss):
	plt.plot(xs, ys, label="$x^{}$".format(i+1))
plt.legend()
plt.plot(np.repeat(1, 1000), np.linspace(0, 1, 1000), "k--")
plt.plot(0, 0, "o")
plt.plot(1, 1, "o")
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.show()