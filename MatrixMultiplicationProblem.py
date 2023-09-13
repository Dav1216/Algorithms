from typing import List
import numpy as np

# dynamic programming problem
# get the optimal cost to multiply 2D tensors
# the sizes of the tensors
# answer should be 3000 scalar multiplications for the following matrices' sizes
# returns inf if invalid array like [2, 10, 10] is given (we have a vector and a tensor, not a number of 2D tensors)
# It also assumes that [3, 10, 20, 50, 50, 20] is an impossible combinations, since it expects valid tensors: [3, 20,
# 20,50, 50, 20]
a = (2, 10)
b = (10, 50)
c = (50, 20)

sizes = list(a + b + c)
dynamic_table = np.full((len(sizes), len(sizes)), -np.inf)


def best_multiplication_order(array_sizes: List[int], size: int) -> int:
    for i in range(0, size + 1):
        dynamic_table[i, i] = 0

    for i in range(size - 1, -1, -1):
        for j in range(i + 1, size + 1):
            if abs(i - j) == 1:
                dynamic_table[i, j] = 0
            else:
                minimum = np.inf

                for k in range(i, j):
                    minimum = min(minimum, dynamic_table[i, k] + dynamic_table[k + 1, j] + array_sizes[i] *
                                  array_sizes[k] * array_sizes[j])
                dynamic_table[i, j] = minimum

    return dynamic_table[0, size]


print(best_multiplication_order(sizes, len(sizes) - 1))
print(dynamic_table)
