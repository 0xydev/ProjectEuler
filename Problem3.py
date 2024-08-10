def findPrimes(number):
	largestPrime = 0
	for i in range(2, int(number ** 0.5)+1):
		start = 2
		if number % i == 0:
			isPrime = True
			while start < i:
				if i % start == 0:
					isPrime = False
					start +=1
					break
				start +=1
			if isPrime:
				largestPrime = i

	return largestPrime
# 46 -> 2, 3, 23 
print(findPrimes(600851475143))