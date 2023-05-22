from collections import deque



class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()
        offset = len(senate)
        for i, s in enumerate(senate):
            if s == "R":
                R.append(i)
            else:
                D.append(i)
        while R and D:
            r = R.popleft()
            d = D.popleft()
            
            if r < d:
                R.append(r+offset)
            else:
                D.append(d+offset)
            
        if R:
            return "Radiant"
        else:
            return "Dire"
            
        
print(Solution().predictPartyVictory('DDRRR'))