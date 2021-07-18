matrix = [[1, 2, 3],
          [3, 2, 1],
          [4, 3, 5],
          [6, 4, 0]]

# transposing rows and columns

print([[row[i] for row in matrix] for i in range(3)])
# [[1, 3, 4, 6], [2, 2, 3, 4], [3, 1, 5, 0]]
# for loop---

lst = []
for i in range(0, 3):
    lst2 = []
    for r in matrix:
        lst2.append(r[i])
    lst.append(lst2)
print(lst)

# using zip function ---
print(list(zip(*matrix)))
