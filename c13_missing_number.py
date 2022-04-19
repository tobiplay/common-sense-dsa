def missing_number(array: list[int]) -> int | None:
    sorted_array = array
    sorted_array.sort()

    # When we sort the array, each number
    # should sit at its corresponding index.
    for i in range(0, len(array)):
        if array[i] != i:
            return i

    return None


print(missing_number([0, 3, 2, 5, 1]))
