# given an cellular automaton state, find out if it has a
# pre-image (a state that when applied a transformation of the type (0, 0, 0) -> 0 
# (pre-image[i - 1], pre-image[i], pre-image[i + 1]) -> arr[i]
# on each three consecutive elements of it), it results in the initial cellular automaton state)

function_map = {
    0: [(1, 1, 1), (0, 0, 0), (1, 0, 1), (1, 1, 0)],
    1: [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0)]
}


def has_pre_image(arr, i, left, middle):
    # base case
    if i == len(arr) - 1:
        if (left, middle) == (2, 2):
            return True
        else:
            for (el1, el2, el3) in function_map[arr[i]]:
                if el1 == left and el2 == middle and el3 == 0:

                    return True
            return False
    # inductive case
    else:
        for (el1, el2, el3) in function_map[arr[i]]:

            if (left, middle) == (2, 2):
                if el1 == 0:
                    result1 = has_pre_image(arr, i + 1, el2, el3)

                    if result1 is True:
                        return True

            elif el1 == left and el2 == middle:
                result2 = has_pre_image(arr, i + 1, el2, el3)

                if result2 is True:
                    return True

        return False


# array that results in true answer
array = [1, 0, 1, 1, 0]
# array that results in false answer
array2 = [0, 0, 1, 0, 0]
print(has_pre_image(array2, 0, 2, 2))
