import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np

x=np.array([1,2,3,4,5,6,7,9,10])
y=np.array([6,5,10,12,13,14,21,23,24])
mc=0
bc=0
n=5
lr=0.01
itr=100
yp=np.array([])
def plot() :
        style.use("ggplot")
        plt.scatter(x, y, marker="o")
        plt.plot(x, yp, color="g")
        plt.axis([0, 12, 0, 30])
        plt.show()
for i in range(itr) :
        yp=mc*x+bc
        cost=(1/n)*sum([val**2 for val in (y-yp)])
        md=(-2/n)*sum((y-yp)*x)
        bd=(-2/n)*sum(y-yp)
        mc=mc-lr*md
        bc=bc-lr*bd
plot()
