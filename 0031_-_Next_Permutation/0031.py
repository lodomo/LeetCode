class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Lexicographic Permutation Algorithm
        """
        n = len(nums)
        k = n - 2

        # Step 1: Find the first decreasing element from the right
        while k >= 0 and nums[k] >= nums[k + 1]:
            k -= 1

        if k >= 0:
            # Step 2: Find the smallest element greater than nums[k] to the right
            swap_position = n - 1
            while nums[swap_position] <= nums[k]:
                swap_position -= 1
            # Swap nums[k] and nums[l]
            nums[k], nums[swap_position] = nums[swap_position], nums[k]

        # Step 3: Reverse the elements after index k
        nums[k + 1:] = reversed(nums[k + 1:])
