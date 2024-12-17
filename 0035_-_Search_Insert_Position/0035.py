class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return 0

        if nums[-1] < target:
            return len(nums)

        in_array = self.find(nums, target)
        if in_array != -1:
            return in_array

        return self.greatest_less_than(nums, target) + 1

    def find(self, arr, target):
        left = 0
        right = len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                result = mid
                break
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return result

    def greatest_less_than(self, arr, target):
        left = 0
        right = len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
