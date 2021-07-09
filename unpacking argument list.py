# normally we do this---

some_list = list(range(1,10)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(some_list)

# using *args

args = [1,10]
print(list(range(*args)))
