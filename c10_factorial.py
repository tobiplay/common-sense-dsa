def factorial(n: int) -> int:
    '''Return the factorial of n.'''
    if n == 1:
        return 1
    else:
        # If it was factorial(n - 2), we'd never reach the base case
        # beause n would never be equal to 1
        return n * factorial(n - 1)


print(factorial(5))
