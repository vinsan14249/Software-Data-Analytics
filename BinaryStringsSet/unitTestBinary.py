#!/usr/bin/python
import binary    					# importing binary module

# Displaying happy path
# binay.bits for calling function from binary module

assert binary.bits(4,3) == {'0100', '0001', '0010', '1000'}
assert binary.bits(4, 1) == {'0111', '1011', '1101', '1110'}
assert binary.bits(5, 4) == {'00001', '00100', '01000', '10000', '00010'}

# Throwing assertion error.
assert binary.bits(1, 4) == {'00001', '00100', '01000', '10000', '00010'},"---------!!Test case Failed!!----------"

