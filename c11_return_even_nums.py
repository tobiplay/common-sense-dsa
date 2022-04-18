from numpy import number


def even_numbers(number_array: list[int]) -> list[int]:
    # Let's figure out the subproblem of our problem.
    # If we pass [0, 1, 2, 3, 4, 5] into the function,
    # the subproblem would be [1, 2, 3, 4, 5] for example.

    # We assume that our function already works. We then check
    # the first entry of our list and decide if we have to add it.

    # The base case would be if we have no item left. We
    # then simply return (nothing)

    if len(number_array) == 0:
        return []

    if number_array[0] % 2 == 0:
        return [number_array[0]] + even_numbers(number_array[1:])
    else:
        return even_numbers(number_array[1:])


print(even_numbers([0, 1, 2, 3, 4, 5]))  # -> [0, 2, 4]
