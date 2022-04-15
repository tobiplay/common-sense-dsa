from math import floor

def binary_search(ordered_array: list[int], search_value: int) -> None | int | str:
    lower_boundary = 0
    upper_boundary = len(ordered_array)

    while lower_boundary < upper_boundary:
        # Calculate the left-most middle entry via floor
        left_middlepoint_index = floor((upper_boundary + lower_boundary) / 2)
        value_at_middlepoint = ordered_array[left_middlepoint_index]
        
        # If the value at the middle is the one we're searching for -> return it
        # If it's lower than the one we're searching for, we can advance to the right and
        # eliminate the left to it
        # If it's higher, we can limit the range to all items to the left of it

        if value_at_middlepoint == search_value:
            return search_value
        elif value_at_middlepoint < search_value:
            lower_boundary = left_middlepoint_index + 1
        elif value_at_middlepoint > search_value:
            upper_boundary = left_middlepoint_index - 1

    return f"Could not find {search_value}"



print(binary_search([0, 1, 5, 6, 7, 12, 15], 15))