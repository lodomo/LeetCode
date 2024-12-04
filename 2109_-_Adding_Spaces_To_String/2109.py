class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        """
        Turn each word into it's own string and add to a list.
        Join the list with a space.

        Much MUCH faster than concatenating strings.
        """
        string_as_list = []

        string_as_list.append(s[:spaces[0]])

        for i in range(len(spaces) - 1):
            string_as_list.append(s[spaces[i]:spaces[i + 1]])

        string_as_list.append(s[spaces[-1]:])

        return " ".join(string_as_list)
