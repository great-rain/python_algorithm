class Solution:
    def isPalindrome(self, s: str) -> bool:
        r, l = 0, len(s) - 1
        while r <= l:
            if not s[r].isalnum():
                r += 1
            elif not s[l].isalnum():
                l -= 1

            elif s[r].lower() != s[l].lower():
                return False
    
            else:
                r += 1
                l -= 1
        return True