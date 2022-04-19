def greatest_number(array: list[int]) -> int:
    # Trigger a print to the console to keep track of
    # each round of recursion.
    print("RECURSION")

    # We want to find the greatest number within a list
    # of integers.

    # We assume that our function is already working properly.
    # We then look at a subproblem of our example problem:
    # The main problem could be [1, 15, 41, 16].
    # The subproblem would be checking [15, 41, 16] for the
    # biggest entry and comparing the 1 against it.

    # The base case would be something like: 1 item left?
    # -> that's by definition the biggest entry:
    if len(array) == 1:
        return array[0]

    # An easy fix for our performance problem would be
    # calculating the recursive functions once
    # and storing in a variable
    max_remainder = greatest_number(array[1:])

    # The number array[0] is the greatest number if
    # it's bigger than the greatest number from the
    # remaining array.
    # (A)
    if array[0] > max_remainder:
        return array[0]
    # If array[0] is not greater than the greatest
    # number from the remaining array, we can assume
    # that we may find the greatest number within
    # the remaining array and we want to return the
    # greatest number from there.
    # (B)
    else:
        return max_remainder


print(greatest_number([1, 2, 3, 4]))
