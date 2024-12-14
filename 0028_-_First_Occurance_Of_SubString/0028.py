class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        I know this right away. HORSPOOL BAYBEEE
        """
        TABLE_SIZE = 256
        strlen = len(needle)
        haylen = len(haystack)
        if strlen == 0:
            return 0  # Edge case: empty needle

        shift_table = [strlen] * TABLE_SIZE

        for i in range(strlen - 1):
            shift_table[ord(needle[i])] = strlen - i - 1

        rh_index = strlen - 1
        while rh_index < haylen:
            curr_index = rh_index
P
            i = strlen - 1
            while i >= 0:
                if needle[i] == haystack[curr_index]:
                    if i == 0:
                        return curr_index
                    i -= 1
                    curr_index -= 1
                else:
                    break

            # Ensure we handle overlapping cases correctly
            skip = shift_table[ord(haystack[rh_index])
                               ] if rh_index < haylen else strlen
            rh_index += max(skip, 1)

        return -1
