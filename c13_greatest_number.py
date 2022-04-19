def greatest_number_1(array: list[int]) -> int:
    # O(N):

    greatest_number_so_far = array[0]

    for i in range(0, len(array)):
        current_number = array[i]
        if current_number > greatest_number_so_far:
            greatest_number_so_far = current_number

    return greatest_number_so_far


def greatest_number_2(array: list[int]) -> int | None:
    # O(N^2):

    for i in range(0, len(array)):
        is_biggest_number = True
        for j in range(0, len(array)):
            # As soon as we find a number that's
            # bigger than the current one -> next.
            if array[i] < array[j]:
                is_biggest_number = False
        if is_biggest_number == True:
            return array[i]


def greatest_number_3(array: list[int]) -> int:
    # O(N*logN):
    sorted_array = array
    sorted_array.sort()
    return sorted_array[-1]


array = [0, 5, 12, 4, 92]

print(greatest_number_1(array))
print(greatest_number_2(array))
print(greatest_number_3(array))
