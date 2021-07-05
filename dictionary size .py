from sys import getsizeof

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# using getsizeof

print(getsizeof(dic1), "bytes")
print(getsizeof(dic2), "bytes")
print(getsizeof(dic3), "bytes")

# inbuilt method .__sizeof__

print(dic1.__sizeof__(), "bytes")
print(dic2.__sizeof__(), "bytes")
print(dic3.__sizeof__(), "bytes")
