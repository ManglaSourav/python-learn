

class Solution:
    def partitionString(self, s: str) -> int:
       
        
        result = 0
        table = set()
        
        for i in s:
            
            if i in table:
                table = set()
                result += 1
            table.add(i)
            
        return result+1
    

print(Solution().partitionString("abacaba"))