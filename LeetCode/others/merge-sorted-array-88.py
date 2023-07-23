from typing import List

def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    a, b, write_index = m-1, n-1, m + n - 1

    while b >= 0:
        if a >= 0 and A[a] > B[b]:
            A[write_index] = A[a]
            a -= 1
        else:
            A[write_index] = B[b]
            b -= 1
        write_index -= 1
        
        
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge_two_sorted_arrays(nums1, m, nums2, n)
print(nums1)