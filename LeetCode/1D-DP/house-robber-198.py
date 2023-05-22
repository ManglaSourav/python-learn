from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        
        # [rob1, rob2, n, N+1,.....]
        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
            print(rob1, rob2)
        
        return rob2
    
    def rob2(self, nums): #this wont work
        sum1 = 0
        sum2 = 0
        
        def sum_it(i):
            sum = 0
            for i in range(i, len(nums), 2):
                sum = sum + nums[i]
            return sum
        
        sum1 = sum_it(0)
        sum2 = sum_it(1)
        return max(sum1, sum2)
    
    
print(Solution().rob([2,1,1,2]))