class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
                1: "I",
                10: "X",
                100: "C",
                1000: "M"
                }

        order = [1000, 100, 10, 1]
        len_order = len(order)
        numerals = []

        for i in range(len_order):
            digit = num // order[i]
            num = num % order[i]

            if digit == 0:
                continue
            if digit > 0 and digit < 4:
                numerals.append(roman_dict[order[i]] * digit)
                continue
            elif digit == 4:
                match(order[i]):
                    case 100:
                        numerals.append("CD")
                    case 10:
                        numerals.append("XL")
                    case 1:
                        numerals.append("IV")
                continue
            elif digit == 5:
                match(order[i]):
                    case 100:
                        numerals.append("D")
                    case 10:
                        numerals.append("L")
                    case 1:
                        numerals.append("V")
                continue
            elif digit > 5 and digit < 9:
                match(order[i]):
                    case 100:
                        numerals.append("D" + "C" * (digit - 5))
                    case 10:
                        numerals.append("L" + "X" * (digit - 5))
                    case 1:
                        numerals.append("V" + "I" * (digit - 5))
                continue
            elif digit == 9:
                match(order[i]):
                    case 100:
                        numerals.append("CM")
                    case 10:
                        numerals.append("XC")
                    case 1:
                        numerals.append("IX")
                continue

        return "".join(numerals)
