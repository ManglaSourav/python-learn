from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
                        "2":"abc",
                        "3":"def",
                        "4":"ghi",
                        "5":"jkl",
                        "6":"mno",
                        "7":"pqrs",
                        "8":"tuv",
                        "9":"wxyz"
                        }
        
        def backtrack(i, currStr):
            if i >= len(digits):
                res.append(currStr)
                return
            
            for char in digitToChar[digits[i]]:
                backtrack(i+1, currStr + char)
        if digits:
            backtrack(0, "")
        return res
    
    
print(Solution().letterCombinations(""))