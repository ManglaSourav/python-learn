

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) < 2:
            return len(s)
        
        left = 0
        right = 1
        total = 0

        myset = set()
        myset.add(s[left])
        while right < len(s):
            
            if s[right] not in myset:
                myset.add(s[right])
                total = max(total, right - left+1)  
                right += 1
            else:
                # remove from set and increament left till the current value
                while left < right and s[right] in myset:
                    myset.remove(s[left])
                    left += 1
        
        return total
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))