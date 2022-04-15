def count_the_ones(array_of_arrays: list[list[int]]) -> int:
    count_of_ones: int = 0

    for array in array_of_arrays:
        for number in array:
            if number == 1:
                count_of_ones += 1

    return count_of_ones

print(count_the_ones(
    [
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1], 
        [1, 0]
    ]
))
