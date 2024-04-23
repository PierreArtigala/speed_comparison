// fact_cpp.h
#include <iostream>
#include <math.h>


// Compute the factorial of n.
int fact(int n) { 
    if (n <= 1) {
        return 1;
    }
    else {
        return n * fact(n-1);
    }
}


// Return true if n is prime
int isPrime(int n) {
    if (n <= 1) { return false; }
    int max_number = int(sqrt(n));
    for (int i = 2; i < max_number + 1; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}


// Return the n-th prime number.
int nThPrime(int n) {
    int number = 1;
    int counter = 0;
    while (counter < n) {
        if (isPrime(++number)) {
            counter++;
        }
    }
    return number;
}