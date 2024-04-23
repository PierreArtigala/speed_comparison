"""Compare the speed of the different implementations."""
from python_lib import n_th_prime as n_th_prime_py
import sys
sys.path.append("build/")
from CPPLib import fact as fact_cpp, isPrime as is_prime_cpp, nThPrime as n_th_prime_cpp
del sys


# Wrap the function to be able to track them in the profiler.
def test_py(n: int):
    return n_th_prime_py(n)


def test_cpp(n: int):
    return n_th_prime_cpp(n)


if __name__ == "__main__":
    n = 100000
    _ = test_py(n=n)
    _ = test_cpp(n=n)
