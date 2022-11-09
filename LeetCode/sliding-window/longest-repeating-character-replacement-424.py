from collections import Counter


class Solution:
    def characterReplacement_sol1(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0
        count = Counter()

        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1

            if ((right - left + 1) - count.most_common(1)[0][1] <= k):
                result = max((right - left + 1), result)
                right += 1
            else:
                count[s[left]] = count[s[left]] - 1
                count[s[right]] = count[s[right]] - 1
                left += 1
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        result = 0
        count = {}
        maxFreq = 0
        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            maxFreq = max(maxFreq, count[s[right]])
            
            while (right - left + 1) - maxFreq > k:
                count[s[left]] -= 1
                left += 1
            
            result = max((right - left + 1), result)
            right += 1
        return result


char_replacement = Solution()
print(char_replacement.characterReplacement("AABABBA", 1))
