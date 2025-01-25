class Solution:
    def countAndSay(self, n: int) -> str:
        result = '1'
        for _ in range(n - 1):
            result = self.rle(result)
        return result


    def rle(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            result.append(str(j - i))
            result.append(s[i])
            i = j
        return ''.join(result)
