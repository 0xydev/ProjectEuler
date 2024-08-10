def isPrime(number):
    checkPrime = True
    if number == 2 or number == 3:
        return True
    else:
        for i in range(2,int(number/2)+1):
            if number % i == 0:
                checkPrime = False
    return checkPrime

def stPrimeNumber(st):
    counter = 0
    number = 1
    while counter <= st:
        if isPrime(number):
            counter +=1
        number +=1
    return number - 1

print(stPrimeNumber(10001))
