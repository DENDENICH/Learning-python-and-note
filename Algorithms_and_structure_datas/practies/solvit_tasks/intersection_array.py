class Solution:

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) < len(nums2):
            return self._get_intersection(set_nums=nums1, array_nums=nums2)
        else:
            return self._get_intersection(set_nums=nums2, array_nums=nums1)
    
    def _get_intersection(self, set_nums: list[int], array_nums: list[int]) -> list[int]:
        intersection = []
        for num in set_nums:
            if num in array_nums:
                intersection.append(num)
        return intersection

s = Solution()
result = s.intersect([4, 9, 5], [9, 4, 9, 8, 4])
print(result)