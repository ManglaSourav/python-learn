


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        memo = {}
        def lps(l,r):
            if (l,r) in memo:
                return memo[(l,r)]
            if l>r:
                return 0
            if l == r:
                return 1
            if s[r] == s[l]:
                memo[(l, r)] = lps(l+1, r-1) + 2
            else:
                memo[(l, r)] = max(lps(l+1, r), lps(l,r-1))
            return memo[(l, r)]
        return lps(0, len(s)-1)
    
    
    
print(Solution().longestPalindromeSubseq("bbbab"))