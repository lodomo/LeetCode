class List(list):
    pass


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]

        if not nums:
            return result

        if nums[0] > target:
            return result

        if nums[-1] < target:
            return result

        target_index = self.find(nums, target)

        if target_index == -1:
            return result

        if nums[0] == target:
            result[0] = 0
        else:
            result[0] = self.greatest_less_than(nums, target) + 1

        if nums[-1] == target:
            result[1] = len(nums) - 1
        else:
            result[1] = self.least_greater_than(nums, target) - 1

        if -1 in result:
            return [-1, -1]

        return result

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

    def least_greater_than(self, arr, target):
        left = 0
        right = len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result


nums = [5, 7, 7, 8, 8, 10]
target = 8

s = Solution()
print(s.searchRange(nums, target))  # [3, 4]
