class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        I feel like dogshit on this one. I need to study this more.
        Most of this code is CheatGPT. My code didn't work.
        """
        from collections import deque

        left = 0
        count = 0
        min_deque = deque()
        max_deque = deque()

        for right in range(len(nums)):
            # Maintain min and max deques
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()

            min_deque.append(right)
            max_deque.append(right)

            # Ensure window is valid (difference ≤ 2)
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1

            # Add all subarrays ending at `right`
            count += right - left + 1

        return count
