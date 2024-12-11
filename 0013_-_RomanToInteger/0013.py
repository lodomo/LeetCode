class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }

        strlen = len(s)
        count = 0
        for i in range(strlen):
            if (i < strlen - 1) and (roman_dict[s[i]] < roman_dict[s[i+1]]):
                count -= roman_dict[s[i]]
            else:
                count += roman_dict[s[i]]

        return count

