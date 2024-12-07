"""
You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

    Take any bag of balls and divide it into two new bags with a positive number of balls.
        For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.

Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.
"""

"""
My initial intuition was a heap, but it doesn't work. I read some solutions and 
binary search works best. Here is an implementation that's OK but with some notes.
It's really complicated to wrap my head around this problem.
"""


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        """
        None of this is intuitive, and I barely understand how someone can come up with this.

        First we make a number line as long as the biggest number in the array.
        Then we assume the biggest number is the answer.

        Then we do a binary search on the number line.
        We check the midpoint of the number line and see if we can create the middle number
        with the operations we have.

        If we can, we shrink the number line to the left, and see if we can find a smaller number.
        If we can't, we shrink the number line to the right, and see if we can find a bigger number.

        With this voodoo, it finds the smallest number.
        I do not understand the practical use for this, maybe one day.
        """
        left, right = 1, max(nums)

        while left <= right:
            mid = (left + right) // 2

            if self.canSplit(nums, mid, maxOperations):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canSplit(self, nums, mid, maxOperations):
        for n in nums:
            maxOperations -= (n - 1) // mid
            if maxOperations < 0:
                return False
        return True
