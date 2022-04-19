def add_until_100(array: list[int]) -> int:
    # What's the subproblem of add_until_100([1, 2, 3, 4, 5, 6])
    # -> 6 + add_until_100([1, 2, 3, 4, 5]).

    # Now, assume that the function already works,
    # we'd just add the first entry to the sum of the rest.

    # The base case would be, when the array is empty.

    if len(array) == 0:
        return 0

    # The thing is, we're currently making 3 calls
    # of the above function. We can just save it once
    # in a variable and access it.

    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    else:
        return array[0] + add_until_100(array[1:])


def add_until_100_save(array: list[int]) -> int:
    if len(array) == 0:
        return 0

    # The thing is, we're currently making 3 calls
    # of the above function. We can just save it once
    # in a variable and access it.

    sum_remaining_nums = add_until_100(array[1:])

    if array[0] + sum_remaining_nums > 100:
        return sum_remaining_nums
    else:
        return array[0] + sum_remaining_nums


print(add_until_100_save([1, 2, 3, 4, 5]))
