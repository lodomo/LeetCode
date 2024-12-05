class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s

        max_len = len(set(s))
        best_len = 1
        prev_len = 1
        left = 0
        right = 1

        while right < len_s and best_len < max_len:
            cur_len = len(set(s[left:right + 1]))
            if cur_len > prev_len:
                best_len = max(best_len, cur_len)
                prev_len = cur_len
            else:
                left += 1
            right += 1
        return best_len
