from collections import Counter

# Solution 1 : put both string into dictionar and count the occurence and then check
# space complexity O(S+T) for dict for every string or  sizes of dict or HashMap
# time complexity O(S+T)

# Solution 2: Sort the both string and just compare both strings
# space complexity O(1)
# time complexity O(nlogn) So less space but more time consuming


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)


anagram = Solution()
print(anagram.isAnagram("anagram", "nagaram"))
