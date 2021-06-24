import numpy as np
import matplotlib.pyplot as pl

a = np.linspace(1, 5, 6)
b = np.log(a)
pl.plot(a, b)
pl.plot(a-1,b-1,'r')
pl.plot(a+1,b+1,linewidth=2,linestyle='dashed')
pl.plot(a+2,b+2,'bd',linestyle="dashdot",
marker='d',markersize=4,markeredgecolor='red')
pl.xlabel("X AXIS")
pl.ylabel("Y AXIS")
pl.show()
