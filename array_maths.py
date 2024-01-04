import numpy as np

nos = list(input())[::2]
n = int(nos[0])
m = int(nos[1])

a_ints = [list(input())[::2] for _ in range(n)]
b_ints = [list(input())[::2] for _ in range(n)]

a_arr = np.array(a_ints, dtype="int64")
b_arr = np.array(b_ints, dtype="int64")

print(a_arr + b_arr)
print(a_arr - b_arr)
print(a_arr * b_arr)
print(a_arr // b_arr)
print(a_arr % b_arr)
print(a_arr**b_arr)
