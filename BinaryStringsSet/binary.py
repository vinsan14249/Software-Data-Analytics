##!/usr/bin/python


# argument 'n' : length of string and set
# argument 'k' : no. of zero bit's

def bits(n,k):

# length of string cannot be less than no. of bit's required
	if(k >= n) 	:								
		print "\n * The set of binary string cannot be processed with the given arguments.\
Length of string must be '>' than the no. of zero bits\n"
	
	elif( k < n) :
		print "\nThe set of binary string is as follows :\n"
		per = set(permutate(n,k))
		print(per)
		return per
	else:
		print "\n!!Enter the valid arguments!!\n"
	return 
		
j =0
def permutate(n,k):								#func to create permutation for binary string
	arr1,arr = [],[]
	length = 1
	for i in range(n):
		length = length*2
	for j in range(length):
		s = bin(j)[2:]
		s = '0'*(n-len(s)) + s
		if s.count('0') == k  and len(arr) < n:
			arr.append(s)
	return arr

#bits(4,3)
#bits(3,3)
#bits(5,3)

