from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        count = Counter(s)

        for char in count:
            if count[char] % 2:
                k -= 1

        return k >= 0
