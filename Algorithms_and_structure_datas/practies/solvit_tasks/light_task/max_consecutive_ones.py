from itertools import groupby


class Solution:
    def find_max_consecutive_ones(self, nums: list[int]) -> int:
        group = groupby(nums)
        return max(
            (sum(_ for _ in g) for k, g in group if k == 1),
            default=0    
        )