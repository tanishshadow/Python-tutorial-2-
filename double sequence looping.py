# looping over two sequences at the same time using zip function---

list1 = ["tanish","vasu","aditya"]
list2 = ["python","python-linux","python----"]
print(list(zip(list1,list2)))

for index , item in enumerate(zip(list1,list2)):
    print(index ,":",item) 
