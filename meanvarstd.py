import numpy as np

nm = list(input()[::2])
n = int(nm[0])
m = int(nm[1])

lists = [list(input()[::2]) for _ in range(n)]
my_array = np.array(lists, dtype="int64")

print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print(round(np.std(my_array), 11))
