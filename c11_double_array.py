array = [1, 2, 3, 4, 5]

def double_array(array: list, index: int = 0):
    if index >= len(array):
        return
    array[index] *= 2
    # We know that the last line must be the
    # next function call, because this is a
    # problem of the type: repeatedly execute
    double_array(array, index + 1)

double_array(array)
print(array)
