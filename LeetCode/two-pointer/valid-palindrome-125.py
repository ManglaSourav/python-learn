

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:
            left_char = s[left].lower()
            right_char = s[right].lower()
            if not left_char.isalnum():
                left += 1
            elif not right_char.isalnum():
                right -= 1
            elif left_char == right_char:
                left += 1
                right -= 1
            else:
                return False

        return True


is_pal = Solution()
print(is_pal.isPalindrome("A man, a plan, a canal: Panama"))
