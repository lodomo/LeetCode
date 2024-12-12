class List(list):
    pass


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = set()
        print(nums)

        for i in range(n - 3):
            min = i + 1
            max = n - 1
            while min < max:
                left = min + 1
                right = max - 1
                success = False
                while left <= right:
                    mid = (left + right) // 2
                    sum = nums[i] + nums[min] + nums[mid] + nums[max]
                    # print(f"Checking {nums[i]}, {nums[min]}, {nums[mid]}, {nums[max]}")
                    if sum == target:
                        # print(f"found {nums[i]}, {nums[min]}, {nums[mid]}, {nums[max]}")
                        results.add((nums[i], nums[min], nums[mid], nums[max]))
                        max -= 1
                        success = True
                        break
                    elif sum < target:
                        left = mid + 1
                    else:
                        right = mid - 1

                if not success:
                    min += 1

        final_results = []
        for result in results:
            final_results.append(list(result))
        return final_results


nums = [-1,0,1,2,-1,-4]
target = -1 
print(Solution().fourSum(nums, target))
