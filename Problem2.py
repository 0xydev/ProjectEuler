def fibonacci_sum():
    a,b = 0,1
    result = 0
    while b <= 4000000:
        a,b = b, a + b
        if b % 2 == 0:
            result += b
    return(result)
print(fibonacci_sum())