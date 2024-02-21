def count_swaps(*a):
    n0, i0, n1, i1 = 0, 0, 0, 0
    for p in range(len(a)):
        if a[p] == 0:
            n0 += p - i0  # No. of steps to move the 0 to the left
            print("n0", n0, '\n')
            i0 += 1
        else:
            n1 += p - i1  # No. of steps to move the 1 to the left
            print("n1", n1, "\n")
            i1 += 1
    return min(n0, n1)


# Example usage:
result = count_swaps(1, 0, 1, 0, 1, 1)
print(result)
