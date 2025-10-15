class Solution:
    def missing_number(self, nums: list[int]) -> int:
        n = len(nums)
        for empty_num in range(0, n+1):
            if not empty_num in nums:
                return empty_num
        return n

s = Solution()
result = s.missing_number([1])
print(result)
