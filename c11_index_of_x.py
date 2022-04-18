from operator import index


def index_of_x(string: str) -> int:
    # Assume the string always contains an x.

    # First, we try to figure out the subproblem:
    # the subproblem would be the whole string minus
    # the first entry, once we've checked that.

    if string[0] != "x":
        return 1 + index_of_x(string[1:])
    else:
        return 0


print(index_of_x("xafasf"))  # -> 23
