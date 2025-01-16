class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        nums1_odd = len(nums1) % 2
        nums2_odd = len(nums2) % 2

        if nums1_odd:
            for num in nums2:
                result ^= num

        if nums2_odd:
            for num in nums1:
                result ^= num

        return result
