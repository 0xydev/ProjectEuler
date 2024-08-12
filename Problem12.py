import math

def count_divisors(number):
    count = 0
    root = int(math.sqrt(number))
    for i in range(1, root + 1):
        if number % i == 0:
            count += 2 if i != number // i else 1
    return count

def triangle_numbers(divisors_number):
    n = 1
    while True:
        triangle_num = n * (n + 1) // 2
        if count_divisors(triangle_num) > divisors_number:
            return triangle_num
        n += 1

print(triangle_numbers(501))
