from typing import Dict
# finds the longest subsequence of three input strings
# uses memoization
X = "boatbeer"
Y = "bibliography"
Z = "abrac"

the_map = {}


def get_max_substring(X: str, Y: str, Z, the_map: Dict) -> int:
    if len(X) == 0 or len(Y) == 0 or len(Z) == 0:
        return 0
    elif X[len(X) - 1] != Y[len(Y) - 1] or X[len(X) - 1] != Z[len(Z) - 1]:
        if (X, Y, Z) in the_map.keys():
            return the_map[(X, Y, Z)]
        else:
            the_map[(X, Y, Z)] = max(
                get_max_substring(X[:-1], Y, Z, the_map),
                get_max_substring(X, Y[:-1], Z, the_map),
                get_max_substring(X, Y, Z[:-1], the_map)
            )
        return the_map[(X, Y, Z)]
    elif X[len(X) - 1] == Y[len(Y) - 1] and X[len(X) - 1] == Z[len(Z) - 1]:
        return 1 + get_max_substring(X[:-1], Y[:-1], Z[:-1], the_map)


print(get_max_substring(X, Y, Z, the_map))
