def intersection(first_array: list[int], second_array: list[int]) -> list[int]:
    result: list[int] = []

    for i in range(0, len(first_array) - 1):
        for j in range(0, len(second_array) - 1):
            if first_array[i] == second_array[j]:
                result.append(first_array[i])
                break

    return result

print(intersection([3, 1, 4, 2], [4, 5, 3, 6]))