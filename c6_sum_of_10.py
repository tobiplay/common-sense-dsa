def sum_of_ten(array: list) -> bool:
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] + array[j] == 10:
                return True
    return False

print(sum_of_ten([2, 5, 6, 7]))