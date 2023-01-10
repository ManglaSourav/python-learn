

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
         return False

        return str(x) == str(x)[::-1]
    
pal = Solution()
print(pal.isPalindrome(121))
