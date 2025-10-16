from time import time
from random import randint

class Solution:

    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        set_nums = set(nums1)
        for num in set_nums:
            c_n_in_1, c_n_in_2 = nums1.count(num), nums2.count(num)
            if (count := min(c_n_in_1, c_n_in_2)) > 0:
                intersection.extend(
                    [num for _ in range(count)]
                )
        return intersection

s = Solution()

### TEST 1 ###
start = time()
nums1 = [randint(0, 10) for _ in range(20)]
nums2 = [randint(0, 10) for _ in range(20)]
for _ in range(5_000_000):
    result = s.intersect(nums1, nums2)
print(f"Test is complete! Time - {time() - start}")