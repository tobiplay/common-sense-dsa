from math import floor

def is_palindrome(string: str) -> bool:
    for letter_position in range(floor(len(string) / 2)):
        if string[letter_position] != string[-1 - letter_position]:
            return False

    return True

print(is_palindrome("kayyak"))