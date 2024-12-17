class List(list):
    pass

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums)
        pivot_to_add = 0

        if nums[0] == target:
            return 0

        if nums[-1] == target:
            return len(nums) - 1

        if nums[0] > nums[-1]:
            pivot = self.lt_bn_search(nums, nums[-1])
            if target >= nums[pivot] and target <= nums[-1]:
                pivot_to_add = pivot
                nums = nums[pivot:]
            else:
                nums = nums[:pivot]

        index = self.eq_bn_search(nums, target)
        if index == -1:
            return -1
        return pivot_to_add + index

    def lt_bn_search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            val = arr[mid]
            if val < target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def eq_bn_search(self, arr: List[int], target: int) -> int:
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
