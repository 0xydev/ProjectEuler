import math

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True
def summation_of_primes(number):
    sum = 0
    for i in range(2,number):
        if isPrime(i):
            sum += i
    return sum

print(summation_of_primes(2000000))