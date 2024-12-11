class List(list):
    pass


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        for digit in digits:
            result = self.createCombinations(phone_map, digit, result)

        for i, item in enumerate(result):
            result[i] = "".join(item)

        return result

    def createCombinations(self, map: dict, digit: str, previous: list) -> list:
        combos = []

        if not previous:
            for letter in map[digit]:
                combos.append([letter])
            return combos

        for letter in map[digit]:
            for item in previous:
                new_item = item.copy()
                new_item.append(letter)
                combos.append(new_item)
        return combos
