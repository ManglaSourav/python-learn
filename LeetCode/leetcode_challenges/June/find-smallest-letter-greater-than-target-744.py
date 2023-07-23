from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        res = letters[0]
        
        left = 0
        right = len(letters)-1
        while left <= right:
            mid = (left+right)//2
            
            if letters[mid] > target:
                right = mid - 1
                res = letters[mid]
            else:
                left = mid + 1 
        return res
            
    
    
print(Solution().nextGreatestLetter(["c","f","j"], target = "a"))