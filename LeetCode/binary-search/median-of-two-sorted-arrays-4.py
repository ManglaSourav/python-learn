from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        A, B = nums1, nums2
        if len1 > len2:  # A should be smaller
            A, B = B, A
        total = len1+len2
        half = total//2

        left = 0
        right = len(A) - 1

        while True:
            mid = (left + right)//2  # A
            j = half - mid - 2  # B and -2 is for zero index in both array

            A_left = A[mid] if mid >= 0 else float("-infinity")
            A_right = A[mid+1] if (mid+1) < len(A) else float("infinity")
            B_left = B[j] if j >= 0 else float("-infinity")
            B_right = B[j+1] if(j+1) < len(B) else float("infinity")

            if A_left <= B_right and A_right >= B_left:
                if total % 2:  # odd
                    return min(A_right, B_right)
                else:
                    return (min(A_right, B_right) + max(A_left, B_left))/2
            elif A_left > B_right:
                right = mid - 1
            else:
                left = mid + 1


median = Solution()
print(median.findMedianSortedArrays([1, 2], [3, 4]))
