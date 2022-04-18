def reverse_string(string: str) -> str:
    # The subproblem of "abcde" would be "bcde".
    # Imagine if the function would already work,
    # we'd just invert "bcde" and add the "a" to
    # the end of the reversed string.

    if len(string) == 1:
        return string[0]

    return reverse_string(string[1:len((string))]) + string[0]


print(reverse_string("abcde"))
