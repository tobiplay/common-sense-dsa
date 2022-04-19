def unique_paths(rows: int, cols: int, memo: dict = {}) -> int:
    '''Returns the number of unique shortest pathways
    from the start field (S) to the finish field (F). Keyword arguments:

    rows: the number of rows in our box field.
    cols: the number of cols in our box field. 
    '''

    # We want to store both the row and col in a single dict,
    # and therefore group them as arrays.

    if rows == 1 or cols == 1:
        return 1

    if not f"{rows}:{cols}" in memo:
        memo[f"{rows}:{cols}"] = unique_paths(
            rows - 1, cols, memo) + unique_paths(rows, cols - 1, memo)

    return memo[f"{rows}:{cols}"]


print(unique_paths(2, 4))
