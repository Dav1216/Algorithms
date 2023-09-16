import numpy as np

# given an cellular automaton state, find out if it has a
# pre-image (a state that when applied a trasnformation apply_function
# on each element of it, it results in the initial cellular automaton state)
# this is a brute force approach

# Give
def apply_function(a: bool, b: bool, c: bool) -> bool:
    """This computes an element in state T + 1 based on the three elements above
    in state T"""
    if a is False and b is False and c is False:
        return False
    elif a is False and b is False and c is True:
        return True
    elif a is False and b is True and c is False:
        return True
    elif a is False and b is True and c is True:
        return True
    elif a is True and b is False and c is False:
        return True
    elif a is True and b is False and c is True:
        return False
    elif a is True and b is True and c is False:
        return False
    elif a is True and b is True and c is True:
        return False


def has_pre_image(arr, k, S):
    if k == len(arr) - 1:
        result = True

        for i in range(0, k + 1):
            result = result and (arr[i] == apply_function(bool(S[i - 1]), bool(S[i]), bool(S[i + 1])))
        return result
    else:
        S[k + 1] = 1
        result1 = has_pre_image(arr, k + 1, S)
        S[k + 1] = 0
        result2 = has_pre_image(arr, k + 1, S)

        return result1 or result2

# array that results in true answer
array = [1, 0, 1, 1, 0]
# array that results in false answer
array2 = [0, 0, 1, 0, 0]
# the solution array (the pre-image)
S = np.full(len(array2) + 1, 0)

print(has_pre_image(array2, -1, S))
