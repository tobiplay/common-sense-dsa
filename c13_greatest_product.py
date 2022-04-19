def greatest_product(array_of_3_nums: list[int]) -> int:
    sorted_array = array_of_3_nums
    sorted_array.sort()
    if len(sorted_array) >= 3:
        return sorted_array[-1] * sorted_array[-2] * sorted_array[-3]
    else:
        return -1


print(greatest_product([10, 5, 3, 2, 6, 9]))
