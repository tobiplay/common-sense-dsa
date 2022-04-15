def linear_search(ordered_array: list[int], search_value: int):
    for entry in ordered_array:
        print(f"Checking {entry}")
        if entry == search_value:
            return ordered_array.index(entry)

        # We can break the for loop once the entry is greater
        # than the value we search for
        elif entry > search_value:
            print(f"Breaking at {entry}")
            break

    return f"{search_value} nicht im geordneten Array"

# Nur für geordnete Arrays gedacht!
print(linear_search([0, 1, 5, 9, 10], 7))