# dynamic programming problem, finds the maximum length substring between
# two input strings X and Y
X = "HelloWorld"
Y = "GoodNightWorld"
c = [[0 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]


def longest_subsequence(X, Y):
    for i in range(0, len(X) + 1):
        for j in range(0, len(Y) + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif i > 0 and j > 0 and X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif i > 0 and j > 0 and X[i - 1] != Y[j - 1]:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c[len(X)][len(Y)]


result = ""


def print_subsequence(X, Y, i, j):
    global result
    if i == 0 or j == 0:
        pass
    elif X[i - 1] == Y[j - 1]:
        print_subsequence(X, Y, i - 1, j - 1);
        result += X[i - 1]
    elif c[i][j] > c[i][j - 1]:
        print_subsequence(X, Y, i - 1, j)
    else:
        print_subsequence(X, Y, i, j - 1)

    return result


length = longest_subsequence(X, Y)
print(length)
print(print_subsequence(X, Y, len(X), len(Y)))
