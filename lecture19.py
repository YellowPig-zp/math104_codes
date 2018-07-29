import numpy as np
from matplotlib.pylab import plt

def f1():
	xs = [0,2,3,5]
	ys = [1,1,0,0]
	fig, ax = plt.subplots()
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.plot(xs,ys, label="$f_n(x)$")

	plt.xticks(xs, ['', '$n-1$','$n$',''])
	plt.yticks([1], ['$1$'])

	plt.legend()
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.axis('equal')
	plt.show()	

def f2():
	xs = [0,1,2,5]
	ys = [0,1,0,0]
	fig, ax = plt.subplots()
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.plot(xs,ys, label="$f_n(x)$")

	plt.xticks(xs, ['', r'$\frac{1}{n}$',r'$\frac{2}{n}$','$2$'])
	plt.yticks([1], ['$1$'])

	plt.legend()
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.axis('equal')
	plt.show()

def f3():
	xs = [0,1,2,5]
	ys = [0,0,1,1]
	fig, ax = plt.subplots()
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.plot(xs,ys, label="$f_n(x)$")

	plt.xticks(xs, ['', r'$n-1$',r'$n$',''])
	plt.yticks([1], ['$1$'])

	plt.legend()
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.axis('equal')
	plt.show()

def f4():
	capped_xs = np.linspace(-0.94, 0.8, 1000)
	xs = np.linspace(-1, 1, 1000)
	ys = [1/(1-x) for x in capped_xs]
	def getN(N):
		def fN(x):
			total = 0.0
			for i in range(N+1):
				total += x**i
			return total
		return fN

	yss = []
	for N in range(1, 4):
		fN = getN(N)
		yss.append([fN(x) for x in xs])
	fig, ax = plt.subplots()
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.plot(capped_xs,ys, label=r"$\frac{1}{1-x}$")

	for i, ys in enumerate(yss):
		plt.plot(xs,ys, label="$N={}$".format(i+1), alpha=0.3)
	plt.plot([1,1],[0,5],"k--", alpha=0.3)
	plt.plot(-1, 0.5, 'o', markerfacecolor='None', markeredgecolor='C0', markersize=5)
	plt.xticks([-1,1], ['-1','1'])

	plt.legend()
	ax.spines['left'].set_position('zero')
	ax.spines['right'].set_color('none')
	ax.spines['bottom'].set_position('zero')
	ax.spines['top'].set_color('none')
	ax.axis('equal')
	plt.show()