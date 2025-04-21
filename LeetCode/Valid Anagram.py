# 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


# 2
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)

        for char in s:
            d[char] += 1

        for char in t:
            d[char] -= 1

        for key in d:
            if d[key]:
                return False
        return True

# 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        return Counter(s) == Counter(t)