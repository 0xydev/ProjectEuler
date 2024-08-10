sum_squares = 0
sum = 0
for i in range(1,101):
    sum_squares += i * i
    sum +=i
square_sum = sum * sum

diff = square_sum - sum_squares
print(diff)
