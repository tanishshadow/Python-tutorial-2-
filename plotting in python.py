import numpy as np
import matplotlib.pyplot as pl

a=np.linspace(1,5,6)
b=np.log(a)
pl.plot(a,b)
pl.xlabel("X AXIS")
pl.ylabel("Y AXIS")
pl.show()
