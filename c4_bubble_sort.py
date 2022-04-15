def bubble_sort(array: list[int]) -> list[int]:
    left_pointer = 0
    right_pointer = 1

    # Keep track if we swapped entries this round
    swapped = False

    while True:

        print(f"Current array: {array}")

        if right_pointer < (len(array)):
            left_val = array[left_pointer]
            right_val = array[right_pointer]
            
            print(f"Comparing {left_val} and {right_val}")
            if left_val > right_val:
                array[right_pointer], array[left_pointer] = left_val, right_val
                swapped = True

            left_pointer += 1
            right_pointer += 1

        else:
            # If we are at right_pointer >= len(array)
            # we reached the end of the array.
            # And if we did not swap until here -> it is sorted
            if swapped == False:
                return array

            left_pointer = 0
            right_pointer = 1

            swapped = False

print(bubble_sort([101, 5, 6, 12, 42, 56, 123]))
