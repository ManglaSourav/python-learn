from math import prod
from array import *
import sys

'''
Problem Statement: Given an array of integers A and an integer m,
determine the maximum product of m consecutive integers in the array.(In O(N+M))
Example:
A = [3, 1, 6, 2, 8, 9, 3, 4], m = 3
Answer: 216 (which is the product of 8, 9, and 3)
'''


def max_product(a, m):
    # product = -sys.maxsize - 1
    product = 1
    if m > a.length():
        return 0

    for j in range(0, m):
        product *= a.get_val(j)

    i = m
    p = product  # to hold temp product
    while(i < a.length()):
        val = a.get_val(i-m)
        if val != 0:
            p /= val  # to calculate product of m-1 values
            p *= a.get_val(i)  # calculating product of m values
            if p > product:
                product = p
        i += 1
    return product


a1 = Array([3, 1, 6, , 8, 9, 3, 4])

print(max_product(a1, 3))
print(a1.get_acces_count())
