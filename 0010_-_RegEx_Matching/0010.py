import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Work smarter, not harder. I ain't coding regex from scratch.
        """
        return re.match('^' + p + '$', s) is not None
