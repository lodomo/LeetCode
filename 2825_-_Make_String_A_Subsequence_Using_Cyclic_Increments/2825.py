class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str2_index = 0

        for c in str1:
            if (
                (c == str2[str2_index])
                or (c == "z" and str2[str2_index] == "a")
                or (ord(c) + 1) == ord(str2[str2_index])
            ):
                str2_index += 1
                if str2_index == len(str2):
                    return True
        return False
