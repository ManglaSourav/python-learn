from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        s2_dict = {}
        left = 0
        right = len(s1)-1

        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        while right < len(s2)-1:
            if s1_dict == s2_dict:
                return True
            # remove left value from window and s2_dict and increment the left side of window
            s2_dict[s2[left]] -= 1
            if s2_dict[s2[left]] < 1:
                del s2_dict[s2[left]]
            left += 1
            # increment the right side of window and insert the value to s2_dict
            right += 1
            s2_dict[s2[right]] = s2_dict.get(s2[right], 0)+1
        if s1_dict == s2_dict:
            return True
        return False


check = Solution()
print(check.checkInclusion("ab", "eidbaooo"))
