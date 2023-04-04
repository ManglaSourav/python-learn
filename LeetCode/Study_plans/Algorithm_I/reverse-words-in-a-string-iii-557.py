

class Solution:
    def reverseWords(self, s: str) -> str:
        
        start = 0
        result = ""
        for i in range(len(s)):
            if s[i] == " ":
                result += self.reverse(s[start:i]) + " "
                start = i + 1
        
        if i == len(s) - 1:
           result += self.reverse(s[start:i+1])
        return result
        
    def reverse(self, s):
        return s[::-1]
                
                            
        
        
    
    
    
print(Solution().reverseWords("God Ding"))
    
# print(' '.join([x[::-1] for x in "God Ding".split(" ")]))
