from numpy import random

random_ints = random.randint(100000, size=(10000))

# Function with O(N^2)
def greatestNumber(array):
    steps = 0
    for i in array:
        # Assume for now that i is the greatest: 
        isIValTheGreatest = True
        
        for j in array:
            # If we find another value that is greater than i, 
            # i is not the greatest:
            if j > i:
                steps += 1
                isIValTheGreatest = False

        # If, by the time we checked all the other numbers, i 
        # is still the greatest, it means that i is the greatest number: 
        if isIValTheGreatest:
            return i, steps


def linear_greatest_number(array) -> list[int]:
    greatest_number = array[0]
    steps = 0
    for number in array:
        steps += 1
        if number > greatest_number:
            greatest_number = number
    return [greatest_number, steps]

print(greatestNumber(random_ints))
print(linear_greatest_number(random_ints))