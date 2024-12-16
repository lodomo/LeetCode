import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        num_len = len(nums)
        final_state = [0] * num_len
        copy_nums = []

        for i, num in enumerate(nums):
            copy_nums.append([num, i])

        heapq.heapify(copy_nums)

        for _ in range(k):
            num = heapq.heappop(copy_nums)
            num[0] = num[0] * multiplier
            heapq.heappush(copy_nums, num)

        for num in copy_nums:
            final_state[num[1]] = num[0]

        return final_state
