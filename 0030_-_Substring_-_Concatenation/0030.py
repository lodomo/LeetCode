class List(list):
    pass

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        map = {}

        all_same_char = True
        for word in words:
            for char in word:
                if char != words[0][0]:
                    all_same_char = False
                    break

        if all_same_char:
            words = ["".join(words)]

        for word in words:
            if word not in map:
                map[word] = 0
            map[word] += 1
        word_len = len(words[0])
        string_len = len(s)
        indexes = []

        MAX_LEFT = string_len
        MAX_RIGHT = string_len
        left = 0

        while left < MAX_LEFT:
            map_clone = map.copy()
            right = left

            while right < MAX_RIGHT:
                checking = s[right: right + word_len]
                if checking in map_clone and map_clone[checking] > 0:
                    map_clone[s[right: right + word_len]] -= 1
                    right += word_len
                else:
                    break

            if all(value == 0 for value in map_clone.values()):
                indexes.append(left)

            left += 1

        return indexes
