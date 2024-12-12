class List(list):
    pass


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        print(nums)
        n = len(nums)
        results = set()

        min = 0
        while min < n - 3:
            max = min + 3
            while max < n - 1:
                result = self.twoSum(nums[min + 1:max], target - nums[min] - nums[max])
                for r in result:
                    results.add(tuple([r[0], r[1], nums[min], nums[max]]))
                print(result)
                max += 1
                while max < n - 1 and nums[max] == nums[max + 1]:
                    max += 1

            result = self.twoSum(nums[min + 1:max], target - nums[min] - nums[max])
            for r in result:
                results.add(tuple([r[0], r[1], nums[min], nums[max]]))
            print(result)
            min += 1
            while min < n - 3 and nums[min] == nums[min - 1]:
                min += 1

        final = []
        for result in results:
            final.append(list(result))
        return final

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        results = []
        for num in nums:
            if num in dic:
                if dic[num][1]:
                    continue
                results.append([dic[num][0], num])
            dic[target - num] = [num, False]
        return results


nums = [1,0,-1,0,-2,2]
target = 0 
print(Solution().fourSum(nums, target))
