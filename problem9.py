def findTriplet(number):
	counter = 0
	for c in range(number):
		for b in range(c):
			for a in range(b):
				if (a*a + b*b) == c*c:
					if a + b + c== number:
						triplet = [a,b,c]
						product = a * b * c 
				counter += 1
			counter += 1
		counter += 1
	return (triplet, product, counter)
print(findTriplet(1000))