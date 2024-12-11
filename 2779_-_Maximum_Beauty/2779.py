class List(list):
    pass


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = 1
        max_beauty = 0

        while right < len(nums):
            lpk = nums[left] + k
            rmk = nums[right] - k
            if lpk >= rmk:
                right += 1
            else:
                max_beauty = max(max_beauty, right - left)
                left += 1

        max_beauty = max(max_beauty, right - left)
        return max_beauty


nums = [4, 6, 1, 2]
k = 2
print(Solution().maximumBeauty(nums, k))
