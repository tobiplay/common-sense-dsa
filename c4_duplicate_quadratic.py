def has_duplicate_value(array: list) -> bool:
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                return True
    return False


print(has_duplicate_value([0, 1, 3, 5, 9, 4]))
