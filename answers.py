import numpy as np
from matplotlib.pylab import plt


fig, ax = plt.subplots()
plt.legend()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.grid()
plt.ylim(-5.5,5.5)
plt.xlim(-5.5,5.5)
ax.xaxis.set_ticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])
ax.yaxis.set_ticks([-5,-4,-3,-2,-1,0,1,2,3,4,5])

xs = np.linspace(-1, 1, 5)
up_ys = np.repeat(2, 5)
bottom_ys = np.repeat(-2, 5)

plt.scatter(xs ,up_ys, c="r")
plt.scatter(xs, bottom_ys, c="r")
plt.scatter(1, -5, c="r")

xs = np.concatenate((xs, xs, [1]), axis=0)
ys = np.concatenate((up_ys, bottom_ys, [-5]), axis=0)

u,s,vh = np.linalg.svd(np.array((xs, ys)).T)
v0 = vh[0]

# plt.plot([0,0], [5,-5], label="(i)", linewidth="3")
# plt.plot([-1,-1], [5,-5], label="(ii)", linewidth="3", c="g")
# plt.plot([1,1], [5,-5], linewidth="3", c="g")
# t = np.array((-5*v0, 5*v0))
# plt.plot(t[:, 0], t[:, 1], linewidth="3", label="(iii)")
# plt.legend()
plt.title("part(b)")

plt.show()	

