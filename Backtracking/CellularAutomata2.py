import numpy as np

# given an cellular automaton state, find out if it has a
# pre-image (a state that when applied a trasnformation apply_function
# on each element of it, it results in the initial cellular automaton state)
# this is a brute force approach

function_map = {
    0: [(1, 1, 1), (0, 0, 0), (1, 0, 1), (1, 1, 0)],
    1: [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0)]
}


def has_pre_image(arr, i, S):
    # base case
    if i == len(arr) - 1:
        if (S[i - 1], S[i], S[i + 1]) == (2, 2, 2):
            return True
        else:
            for (el1, el2, el3) in function_map[arr[i]]:

                if el1 == S[i - 1] and el2 == S[i] and el3 == 0:
                    # prints the solution, if it exists
                    print(S)
                    return True
            return False
    # inductive case
    else:
        base_values_above_at_i = (S[i - 1], S[i], S[i + 1])

        for (el1, el2, el3) in function_map[arr[i]]:
            S[i - 1], S[i], S[i + 1] = base_values_above_at_i

            if (S[i - 1], S[i], S[i + 1]) == (2, 2, 2):
                if el1 == 0:
                    S[i - 1], S[i], S[i + 1] = el1, el2, el3
                    result1 = has_pre_image(arr, i + 1, S)

                    if result1 is True:
                        return True

            elif (S[i - 1] != 2 and S[i] != 2) and el1 == S[i - 1] and el2 == S[i]:
                S[i - 1], S[i], S[i + 1] = el1, el2, el3
                result2 = has_pre_image(arr, i + 1, S)

                if result2 is True:
                    return True

        return False


# array that results in true answer
array = [1, 0, 1, 1, 0]
# array that results in false answer
array2 = [0, 0, 1, 0, 0]
S = np.full(len(array) + 1, 2)
print(has_pre_image(array, 0, S))
