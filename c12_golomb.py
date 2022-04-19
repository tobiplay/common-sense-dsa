def golomb(n_th_number: int, memo: dict = {}) -> int:
    if n_th_number == 1:
        return 1

    # If we haven't already computed the Golomb sequence forr
    # the nth number, we shall add it to the memoization dict.
    if not n_th_number in memo:
        memo[n_th_number] = 1 + \
            golomb(n_th_number - golomb(golomb(n_th_number - 1, memo), memo), memo)

    # Once we've added/computed it, or found it in the memo dict,
    # we can just return it.
    return memo[n_th_number]


print(golomb(7))  # -> 4
