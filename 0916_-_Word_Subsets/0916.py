class List(list):
    pass


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        patterns = {}
        max_freq = {}
        results = []
        for word in words2:
            if word not in patterns:
                patterns[word] = {}
            else:
                continue

            for char in word:
                if char not in patterns[word]:
                    patterns[word][char] = 0
                patterns[word][char] += 1

        for pattern in patterns:
            for char in patterns[pattern]:
                if char not in max_freq:
                    max_freq[char] = 0
                max_freq[char] = max(max_freq[char], patterns[pattern][char])

        for word in words1:
            word_dict = {}
            for char in word:
                if char not in word_dict:
                    word_dict[char] = 0
                word_dict[char] += 1

            is_valid = True
            for char in max_freq:
                if char not in word_dict or word_dict[char] < max_freq[char]:
                    is_valid = False
                    break

                if not is_valid:
                    break

            if is_valid:
                results.append(word)

        return results


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]

s = Solution()
s.wordSubsets(words1, words2)


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo","eo"]

s = Solution()
s.wordSubsets(words1, words2)

words1 = ["cccbb","aacbc","bbccc","baaba","acaba"]
words2 = ["cb","bc","cb"]

s = Solution()
s.wordSubsets(words1, words2)
