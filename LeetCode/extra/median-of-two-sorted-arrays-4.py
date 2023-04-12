from typing import List

# O(log (m+n)).
class Solution:
    def findMedianSortedArrays_simple(self, nums1: List[int], nums2: List[int]) -> float:
        n = []
        i, j=0,0 
        while (i < len(nums1)) and (j < len(nums2)):
            if (nums1[i] >= nums2[j]):
                   n.append(nums2[j]) 
                   j+=1
            else:
                n.append(nums1[i]) 
                i+=1

        if i < len(nums1):
            n.extend(nums1[i:len(nums1)])
        if j < len(nums2):
            n.extend(nums2[j:len(nums2)])
        
        if len(n)%2==0:
            return (n[len(n)//2] + n[(len(n)//2)-1])/ 2
        
        return n[len(n)//2] 

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

            
        
        
        
    
print(Solution().findMedianSortedArrays([1,2], nums2 = [3,4]))

