import numpy as np

# Given a list of string lengths length_strings and a maximum row length L, this program 
# determines the least cost to arrange the words on rows of length L
# the loss function for a row is (L - (number of strings - 1 + sum of lengths of the strings on a row))) ** 3
# and total loss is the sum over all rows of applying this loss function

# lengths of strings in order
length_strings = [3, 9, 4, 1, 5, 4, 2, 4, 2, 2, 10, 7]
# maximum row width
L = 18


def get_cost_strings_on_line(i, j):
    if j == i:
        result = (L - (length_strings[i])) ** 3
        return result
    else:
        return (L - (get_width_strings_on_line(i, j))) ** 3


def get_width_strings_on_line(i, j):
    return sum(length_strings[i:j + 1]) + (len(length_strings[i:j + 1]) - 1)


def get_best_score(j):
    if j == -1:
        return 0
    else:
        the_minimum = 1000000

        for i in range(0, j + 1):
            if get_width_strings_on_line(i, j) <= L:
                calc = get_cost_strings_on_line(i, j) + get_best_score(i - 1)
                the_minimum = min(calc, the_minimum)

        return the_minimum


for i in range(0, len(length_strings)):
    print(get_best_score(i))

