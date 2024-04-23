"""Full Python code."""

def fact(n: int):
    """Compute the factorial of n."""
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


def is_prime(n: int):
    """Return True if n is a prime number."""
    if n <= 1:
        return False
    else:
        for k in range(2, int(n**0.5) + 1):
            if n % k == 0:
                return False
    return True


def n_th_prime(n: int):
    """Return the n-th prime number."""
    number = 1
    counter = 0
    while counter < n:
        number += 1
        if is_prime(n=number):
            counter += 1
    return number
