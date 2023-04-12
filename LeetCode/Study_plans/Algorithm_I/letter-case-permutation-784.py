
from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []

        def backtrack(sub="", i=0):
            if len(sub) == len(S):
                res.append(sub)
            else:
                if S[i].isalpha():
                    backtrack(sub + S[i].swapcase(), i + 1) # with swap 
                backtrack(sub + S[i], i + 1) #without swap
                
        backtrack()
        return res

    
print(Solution().letterCasePermutation("a1b2"))