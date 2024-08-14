import math

def lattice_paths(number):
	return math.comb(2 * number,number)

print(lattice_paths(20))

'''
For a 2x2 grid, you would have to make 2 right moves and 2 down moves.

Possible paths: RRDD RDRD RDDR DRRD DRDR DDRR -> comb(4,2)



'''