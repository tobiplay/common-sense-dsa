from tempfile import _TemporaryFileWrapper


def triangular_numbers(n_th_number: int) -> int:
    # If we were to pass N = 7, the subproblem would
    # be all the numbers leading up to N = 6 plus the
    # new N = 7.

    # The base case would be, that once we reach N = 1:
    # return 1

    if n_th_number == 1:
        return 1

    # Now, assume the function would already return the last
    # value before N = 7:

    return n_th_number + triangular_numbers(n_th_number - 1)


print(triangular_numbers(7))  # -> 28
