from itertools import permutations, combinations


class List(list):
    pass


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = {
            0: [''],
            1: ['()'],
        }

        for i in range(2, n + 2):
            results[i] = []

            for j in range(i):
                for left in results[j]:
                    for right in results[i - j - 1]:
                        results[i].append(f'({left}){right}')

        return list(set(results[n]))

result = Solution().generateParenthesis(10)
print(result)
print(f"Solutions: {len(result)}")
