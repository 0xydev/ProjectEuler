def collatz_sequance(number):
	sequance = []
	max_sequance = []
	for i in range(2,number):
		sequance.append(i)
		while True:
			if i==1:
				break
			if i % 2 == 0:
				i /= 2
				sequance.append(i)
			else:
				i = 3*i + 1
				sequance.append(i)
		if len(sequance) > len(max_sequance):
			max_sequance = sequance
		sequance = []
	return max_sequance
sequance = collatz_sequance(1000000)
print(f" Starting number is : {sequance[0]}, length: {len(sequance)}.")