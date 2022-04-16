def every_other_number(low: int = 0, high: int = 10) -> None:
    '''Print every other number to the console.'''
    # The base case is once the lower boundary reaches the
    # upper boudary
    if low > high:
        return

    print(low)
    every_other_number(low + 2, high)


print(every_other_number(0, 10))
