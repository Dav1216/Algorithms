# given an cellular automaton state, find out if it has a
# pre-image (a state that when applied a trasnformation apply_function
# on each element of it, it results in the initial cellular automaton state)
# this is a brute force approach

function_map = {
    0: [(1, 1, 1), (0, 0, 0), (1, 0, 1), (1, 1, 0)],
    1: [(0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0)]
}


def has_pre_image(arr, i, left, middle, right):
    # base case
    if i == len(arr) - 1:
        if (left, middle, right) == (2, 2, 2):
            return True
        else:
            for (el1, el2, el3) in function_map[arr[i]]:
                print((el1, el2, el3))
                if el1 == left and el2 == middle and el3 == 0:

                    return True
            return False
    # inductive case
    else:
        for (el1, el2, el3) in function_map[arr[i]]:

            if (left, middle, right) == (2, 2, 2):
                if el1 == 0:
                    result1 = has_pre_image(arr, i + 1, el2, el3, 2)

                    if result1 is True:
                        return True

            elif el1 == left and el2 == middle:
                result2 = has_pre_image(arr, i + 1, el2, el3, 2)

                if result2 is True:
                    return True

        return False


# array that results in true answer
array = [1, 0, 1, 1, 0]
# array that results in false answer
array2 = [0, 0, 1, 0, 0]
print(has_pre_image(array, 0, 2, 2, 2))
