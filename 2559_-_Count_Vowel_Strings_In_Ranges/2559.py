class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        trues = [0]
        current = 0

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                current += 1
            trues.append(current)

        results = []

        for query in queries:
            results.append(trues[query[1] + 1] - trues[query[0]])
        return results

