def greatest_product(array: list) -> int:
    # Keep track of the greates product so far
    previous_greates_product = array[0] * array[1]
    # Enumerate -> index, value -> Example for 2: i = 1, i_val = 2
    for i, i_val in enumerate(array):
        for j, j_val in enumerate(array):
            if i != j and i_val * j_val > previous_greates_product:
                previous_greates_product = i_val * j_val

    # Once we've calculated all possible products, return it
    return previous_greates_product

print(greatest_product([1, 2, 3, 4]))