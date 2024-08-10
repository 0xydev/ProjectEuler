def isPalindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True


largestPalindrome = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        if isPalindrome(product) and product > largestPalindrome:
            largestPalindrome = product
            factors = (i,j)

print(f"Largest Palindrome is : {largestPalindrome}, products = {factors}")
