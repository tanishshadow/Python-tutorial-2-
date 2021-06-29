import numpy as np
import matplotlib.pyplot as pl
a=np.array(["Apple","Banana","Guava","Orange"])
b=np.array([10,20,30,40])
pl.bar(a,b,width=0.5,color=['g','r','b','black'],label="a")
pl.legend(loc="upper right")

pl.show()
