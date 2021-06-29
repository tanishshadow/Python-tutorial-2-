import matplotlib.pyplot as plt

a=[10,20,50,30]
# a=[0,0,0,1]
l=['A','B','C','D']
plt.axis('equal') # this is to make the chart circular
E=[0,0,0.1,0]
# auto pct:-    '%[FLAG][WIDTH].[PRECISION]type'
plt.pie(a,labels=l,explode=E,autopct='%1.1f%%') #explode creates a gap between all the values
plt.legend(loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))
plt.show()
