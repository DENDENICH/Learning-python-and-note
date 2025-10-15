class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        lengh = len(nums)
        for i in range(0, lengh):
            for j in range(i+1, lengh):
                if nums[i] + nums[j] == target:
                    return [i, j]
        else:
            return [0, 0]

s = Solution()
result = s.two_sum([3, 2, 4], 6)
print(result)