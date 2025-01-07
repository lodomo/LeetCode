class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        wordlen = len(words)
        results = set()

        for i in range(wordlen):
            for j in range(wordlen):
                if i == j:
                    continue
                if words[i] in words[j]:
                    results.add(words[i])

        return list(results)
