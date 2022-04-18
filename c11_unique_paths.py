from re import T


def unique_shortest_paths(rows: int, cols: int) -> int:
    # We want to get from the left-most square
    # to the one in the bottom right -- and that with
    # the smallest amount of steps.

    # We want to find the *number of shortest paths* from
    # S to F. We can either step one field down, or one
    # to the right.

    # We can *only* step down or to the right, once every
    # step on the way. That means that we can't take any
    # of the steps, that was previously jumped on.

    # Assume that our recursive function is already
    # implemented.

    # The base case would be standing either one to the
    # left, or one to the top. If we stand one to the left,
    # there is no col left. If we stand one to the top,
    # there is no row left to traverse.

    if rows == 0 or cols == 0:
        return 0
    if rows == 1 or cols == 1:
        return 1

    # The subproblem would be us already standing one
    # to the left, or one to the top of the finish.

    # That makes every path viable, that leads to the
    # steps just before our current step:

    return unique_shortest_paths(rows - 1, cols) + unique_shortest_paths(rows, cols - 1)


print(unique_shortest_paths(4, 3))
