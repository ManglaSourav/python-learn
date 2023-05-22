class Solution:
    def numSimilarGroups(self, strs) -> int:
        #DFS 
        #Bunch of Words in the List, Need to Check which ones are VIsited 
        #in DFS 
        visited = [0 for _ in range(len(strs))]
        
        if len(strs) == 0: return 0
        
        res = 0
        
        def similar(i,j):
            cnt = 0
            for sa, sb in zip(strs[i], strs[j]):
                if sa!=sb:
                    cnt += 1
                if cnt >2: return False
                
            return True
        
        def dfs(n):
            #Check Array 
            visited[n] = 1
            for i in range( len(strs)):
                if visited[i] == 0 and similar(i, n):
                    dfs(i)
                #if
            #for

            return
        
        for j in range(len(strs)):
            if visited[j] == 0:
                dfs(j)
                res += 1
        
        return res
    
print(Solution().numSimilarGroups(["tars","rats","arts","star","sfdf"]))