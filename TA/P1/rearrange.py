'''
Problem Statement: Given an array of integers A, rearrange A so that all the 0’s are
pushed to the end of the array. All other values should stay in the same relative
order. (In O(N))
Examples:
A = [2, 6, 1, 9, 0, 2]
Result: [2, 6, 1, 9, 2, 0]
A = [0, 0, 6, 1, 0, 9, 8]
Result: [6, 1, 9, 8, 0, 0, 0]
A = [3, 1, 4, 1, 5, 9, 2]
Result: [3, 1, 4, 1, 5, 9, 2]
'''

from array import *


def push_zeroes(a):
    z = 0
    i = 0
    while(i < a.length() and z < a.length()):
        val = a.get_val(i)
        if val == 0:
            i += 1
        elif i != z:
            a.swap(i, z)
            z += 1
            i += 1
        else:
            z += 1
            i += 1
    return a


a1 = Array([2, 6, 1, 0, 9, 0, 2])
push_zeroes(a1).to_string()
