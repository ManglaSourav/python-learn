

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        i = 0
        res = ""
        while i < l1 and i < l2:
            res = res + word1[i] + word2[i]
            i+=1
        print(i)
        if i <= l1 - 1:
            res += word1[i:l1]
        if i <= l2 - 1:
            res += word2[i:l2]
        return res
    
print(Solution().mergeAlternately("cf", "eee"))