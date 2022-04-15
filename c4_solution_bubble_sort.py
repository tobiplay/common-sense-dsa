def bubble_sort(list):
    # The list is not sorted until the very last index at the beginning 
    # with: last index = len(list) - 1
    unsorted_until_index = len(list) - 1 
    # We init with the state of 'not sorted'
    sorted = False

    while not sorted:
        # Assume the array is sorted until we encounter a swap
        sorted = True
        # Move through the array
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                # We encountered a swap -> the array is not sorted
                sorted = False 
        # Due to the nature of bubble sort,
        # the highest unordered item was 'bubbled up' to the very right
        # so now we don't have to sort that anymore
        unsorted_until_index -= 1

    return list

print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))