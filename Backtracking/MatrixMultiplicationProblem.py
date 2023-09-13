
from typing import List
import numpy as np

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


def best_multiplication_order(array_sizes: List[int], left: int, right: int) -> int:
    minimum = np.inf

    for k in range(left, right):
        if left == right - 1:
            return 0
        else:
            minimum = min(minimum, best_multiplication_order(array_sizes, left, k) + best_multiplication_order(
                array_sizes, k + 1, right) + array_sizes[left] * array_sizes[k] * array_sizes[right])

    return minimum


print(best_multiplication_order(sizes, 0, len(sizes) - 1))