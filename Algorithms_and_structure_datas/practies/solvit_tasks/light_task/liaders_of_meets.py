from collections import Counter

class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        return [num for num, _ in counts.most_common(k)]
    

solution = Solution()
result = solution.top_k_frequent([3, 0, 0, 1], k=2)
print(result)