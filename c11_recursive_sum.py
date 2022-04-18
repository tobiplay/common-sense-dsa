def sum(array: list[int]) -> int:
    if len(array) == 1:
        return array[0]
    return array[0] + sum(array[1:len(array)])

print(sum([1, 2, 3, 4, 5]))