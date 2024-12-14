class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        bad_nums = 0
        num_len = len(nums)

        while right < num_len:
            if nums[right] == val:
                bad_nums += 1
            else:
                nums[left] = nums[right]
                left += 1
            right += 1

        return num_len - bad_nums
