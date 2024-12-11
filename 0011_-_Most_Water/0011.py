class List(list):
    pass


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        width = right
        max_area = 0

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * width)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            width -= 1

        return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(Solution().maxArea(height))
