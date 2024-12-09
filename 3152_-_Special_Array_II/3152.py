class List(list):
    pass


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        num_length = len(nums)
        success = []
        successes = 0
        results = []

        if num_length == 1:
            for query in queries:
                results.append(True)
            return results

        for i in range(num_length - 1):
            if (nums[i] + nums[i + 1]) % 2 == 1:
                successes += 1
            success.append(successes)

        for query in queries:
            q0 = query[0]
            q1 = query[1]

            if q0 == q1:
                results.append(True)
                continue

            s1 = success[q1 - 1]
            s2 = success[q0 - 1] if q0 > 0 else 0
            results.append((q1 - q0) == (s1 - s2))

        return results


case1_nums = [4, 3, 1, 6]
case1_queries = [[0, 2], [2, 3]]

print(Solution().isArraySpecial(case1_nums, case1_queries))
