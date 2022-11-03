from typing import List
from collections import defaultdict

# Sorting anagram takes m.nlogn times where m=number of values in the
# list and n = average size of the every string

# Sol2 take O(m*n)
# m = number of values in the list and n = average size of the every string


class Solution:
    def groupAnagrams_sol1(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            sorted_ana = ''.join(sorted(s))
            my_dict[sorted_ana].append(s)
        return list(my_dict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] += 1
            my_dict[tuple(count)].append(s) 
        return my_dict.values()


grp_ana = Solution()
print(grp_ana.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
