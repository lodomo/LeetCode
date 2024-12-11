class List(list):
    pass

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        closest_diff = float('inf')

        for i in range(n):
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target

                curr_diff = abs(current_sum - target)
                if closest_diff == curr_diff:
                    closest_sum = max(current_sum, closest_sum)
                if curr_diff < closest_diff:
                    closest_diff = curr_diff
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1

                if current_sum > target:
                    right -= 1

        return closest_sum
