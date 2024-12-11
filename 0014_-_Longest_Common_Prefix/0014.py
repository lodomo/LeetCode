class List(list):
    pass

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_lens = [len(s) for s in strs]
        min_str_len = min(str_lens)
        result = []

        for i in range(min_str_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return ''.join(result)
            result.append(char)
        return ''.join(result)
