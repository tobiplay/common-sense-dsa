def mean_average_even_numbers(array: list) -> float:
    sum: float = 0
    count_of_even_numbers: int = 0

    for number in array:
        if number % 2 == 0:
            sum += number 
            count_of_even_numbers += 1

    return sum / count_of_even_numbers

print(mean_average_even_numbers([2, 4, 6, 8, 3, 7, 5, 1]))