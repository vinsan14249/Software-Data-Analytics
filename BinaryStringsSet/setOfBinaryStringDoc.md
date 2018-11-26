# Requirement :

 Write a program that takes two arguments n and k and prints all binary strings of length n that contain k zero bits, one per line. The program:
 ·         Must be called binary.py
 ·         Must provide a function called bits(n, k) that returns a set of strings
 ·         Must contain adequate comments and documentation
 ·         Don’t use python any library like iterables.
 Run the following tests to ensure that the program is correct.
 import binary
 assert binary.zbits(4, 3) == {'0100', '0001', '0010', '1000'}
 assert binary.zbits(4, 1) == {'0111', '1011', '1101', '1110'}
 assert binary.zbits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}


# Solution & Design

##Structure :
 *Two modules :
	- binary.py
		- functions : 
			* bits
			* permutate
	- unitTestBinary.py

###binary.py :

bits(n,k)
{
	Validates arguments passed as per requirement
	calls function permutate for getting permutation of binary string
	returns the array from permutate into set to the function call
}

permutate(n,k)
{
	creates range for loop to start : 2^n
	creates binary string till the range of loop : length
	iterate and create binary string along with prexfing with zero's
	create array for strings that have k no. of zero's in it and return the array

}

