# some more functions of list=----
a = ['a', 'b']
lst = [1, 2, 3, 4, 5]

# .extend() appends all the items from a iterator to other iterator --[1, 2, 3, 4, 5, 'a', 'b']
lst.extend(a)
print(lst)
d = {"name": "tanish", "class": "10"}
lst.extend(d.values())  # ---- [1, 2, 3, 4, 5, 'a', 'b']
print(lst)

lst.extend(d.items())
# [1, 2, 3, 4, 5, 'a', 'b', 'tanish', '10', ('name', 'tanish'), ('class', '10')]
print(lst)


counter = lst.count(1)  # Return the number of times x appears in the list.
print(counter)  # 1

lst.extend([1, 2, 2, 1, 1])
counter2 = lst.count(1)
print(counter2)  # 4

lst.pop(0)  # pops the 0 th index item
print(lst)
