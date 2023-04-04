from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        
        left = 0
        right = len(people) - 1
        
        while left <= right:
            print(left, right)
            if people[left] + people[right] <= limit:
                left +=1
                right -= 1
            elif people[left] + people[right] > limit:
                right -= 1
            boats += 1

        return boats 
    
    
print(Solution().numRescueBoats(people = [2,2,2,3,3], limit = 6))