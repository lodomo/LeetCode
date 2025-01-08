class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        words_len = len(words)
        results = 0

        for i in range(words_len):
            for j in range(i + 1, words_len):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    results += 1

        return results
