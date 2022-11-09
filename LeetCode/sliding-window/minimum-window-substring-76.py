

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1+countT.get(c, 0)

        have, need = 0, len(countT)
        result, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result

                if (r-l+1) < res_len:
                    result = [l, r]
                    res_len = r-l+1
                window[s[l]] -= 1
                # pop from the left of our window
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l:r+1] if res_len != float("infinity") else ""


min_window = Solution()
print(min_window.minWindow("ADOBECODEBANC", "ABC"))
