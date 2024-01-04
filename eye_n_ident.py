import numpy as np

np.set_printoptions(legacy="1.13")

n = list(input())[::2]
row = int(n[0])
col = int(n[1])

print(np.eye(row, col, k=0))
