class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set_nums1, set_nums2 = set(nums1), set(nums2)
        return list(set_nums2 & set_nums1)
    

s = Solution()
result = s.intersection([2, 2], [1, 2, 2, 1])
print(result)