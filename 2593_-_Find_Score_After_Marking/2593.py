class List(list):
    pass


class Solution:
    def findScore(self, nums: List[int]) -> int:
        num_len = len(nums)
        for i in range(num_len):
            nums[i] = (nums[i], i)
        nums.sort(key=lambda x: x[0])
        score = 0
        banned = {}

        for i in range(num_len):
            if nums[i][1] in banned:
                continue
            score += nums[i][0]
            banned[nums[i][1] + 1] = True
            banned[nums[i][1] - 1] = True

        return score
