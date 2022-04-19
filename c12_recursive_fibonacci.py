def fibonacci(n_th_number: int, memo) -> int:
    # Assume we pass in the number 10, we'd now
    # need to figure out the next-to-last (subproblem)
    # number that is computed with fib(9), and add fib(8)
    # to get fib(10).
    print("R")

    # Assume that our function is already working:
    if n_th_number == 0 or n_th_number == 1:
        return n_th_number

    # If the n_th_number does not already have a solution
    # computed for, add it to the memoization dict.
    if not n_th_number in memo:
        # The parameter "memo" is automatically passed down
        # the call stack via the default value.
        memo[n_th_number] = fibonacci(
            n_th_number - 2, memo) + fibonacci(n_th_number - 1, memo)

    # If we alread have the n_th_number stored within
    # the dict, we can just access it and return it.
    return memo[n_th_number]


print(fibonacci(6, {}))  # -> 55
