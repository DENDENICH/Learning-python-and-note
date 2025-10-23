from collections import Counter

class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        counter = Counter(nums)
        return not all(c == 1 for c in counter.values())
    
