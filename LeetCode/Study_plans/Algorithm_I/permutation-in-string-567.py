
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        table = {}
        for s in s1:
            table[s] = table.get(s,0)+1
        
        window_size = len(s1)
        s2_table = {}
        for i in range(0, window_size):
            s2_table[s2[i]] = s2_table.get(s2[i],0) + 1
        
        if table == s2_table:
            return True
        
        left = 0
        
        for right in range(window_size, len(s2)):
        #remove left side from s2_table and insert from right side and then compare
            s2_table[s2[left]] = s2_table.get(s2[left]) - 1
            if s2_table[s2[left]] == 0:
                del s2_table[s2[left]] 
                
            s2_table[s2[right]] = s2_table.get(s2[right], 0) + 1
            left+=1
            if table == s2_table:
                return True
        
        return False
            
                
        
print(Solution().checkInclusion(s1 = "ab", s2 = "a"))

print(ord("b")-ord("a"))