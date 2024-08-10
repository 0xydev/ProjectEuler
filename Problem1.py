def find_multiples(number):
	three_multiples = []
	five_multiples = []
	counter = 0
	for i in range(3,number,3):
		three_multiples.append(i)
		counter +=1
	for i in range(5,number,5):
		five_multiples.append(i)
		counter +=1
	multiples = set(five_multiples + three_multiples)
	sum = 0
	for i in multiples:
		sum += i
	print(counter)
	return sum
print(find_multiples(1000))

'''
def find_multiples(number):
	sum = 0
	counter = 0
	for i in range(number):
		if (i % 3 == 0) or (i % 5 == 0) :
			sum += i
			counter +=1
	print(counter)
	return sum

print(find_multiples(1000))
'''