
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            result = max(result, right-left+1)

        return result


len_str = Solution()
print(len_str.lengthOfLongestSubstring("abcabcbb"))
