


def isBadVersion(version: int) -> bool:
    return True if version >= 4 else False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        first_bad_number = -1
                
        while left <= right:
            mid = (left+right)//2
            
            is_bad = isBadVersion(mid)
            
            if is_bad:
                first_bad_number = mid
                right = mid - 1
            else:
                left = mid + 1
                        
        return first_bad_number
    
    
print(Solution().firstBadVersion(5))