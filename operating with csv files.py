import csv
a=open(r'aman dhattarwal\tanish.csv','r+')
b=csv.reader(a,delimiter=',')
for i in b:
    print(i)
a.close()
