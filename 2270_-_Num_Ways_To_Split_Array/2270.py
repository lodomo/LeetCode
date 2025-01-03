class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        total = sum(nums)
        left = 0
        result = 0

        for i in range(len_nums - 1):
            left += nums[i]
            right = total - left
            if left >= right:
                result += 1

        return result
