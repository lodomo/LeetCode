class List(list):
    pass

# Note to self: Sets are hash maps.


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        count = 0
        sum = 0

        for i in range(1, n+1):
            if i in banned:
                continue

            sum += i
            if sum > maxSum:
                break
            count += 1

        return count
