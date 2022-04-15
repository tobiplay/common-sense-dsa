from tracemalloc import start


def search_sort(array: list) -> list:

    # Run to the last value before the end of the array,
    # bacause it'll be sorted by then
    for starting_index in range(len(array) - 1):

        # Point to the first position in the array
        # which is currently the lowest number
        # Storing the index allows to access the value and index dependent on what we need
        index_of_lowest_number = starting_index

        # Start at the starting index + 1, because the starting value and its index are known
        for index, number in enumerate(array[starting_index + 1:], starting_index + 1):
            if number < array[index_of_lowest_number]:
                # The index of the lowest number is then the current index
                index_of_lowest_number = index

        if index_of_lowest_number != starting_index:
            # Swap the numbers
            array[starting_index], array[index_of_lowest_number] = array[index_of_lowest_number], array[starting_index]

    return array


print(search_sort([4, 2, 7, 1, 3]))
