class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        This question is dumb, I stole this answer.
        """
        return list(accumulate(x-i for i, x in enumerate(arr))).count(0)
