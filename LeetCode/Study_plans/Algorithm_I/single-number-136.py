



class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for s in nums:
            result ^= s
            
        return result
    
print(Solution().singleNumber([4,1,2,1,2]))
