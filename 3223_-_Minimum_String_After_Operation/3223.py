class Solution:
    def minimumLength(self, s: str) -> int:
        counter = 0

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet:
            char_count = s.count(char)
            if char_count == 0:
                continue

            if char_count % 2 == 1:
                counter += 1
            else:
                counter += 2

        return counter


s = "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"

print(Solution().minimumLength(s))
