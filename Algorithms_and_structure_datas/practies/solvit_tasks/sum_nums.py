class Solution:
    def missing_number(self, nums: list[int]) -> int:
        nums.sort()
        empty_num = 1
        i, max_i = 1, len(nums) - 1
        while i <= max_i:
            num = nums[i]
            if empty_num != num:
                return empty_num
            empty_num += 1
            i += 1
        return nums[max_i] + 1

s = Solution()
result = s.missing_number([0, 1, 4, 2])
print(result)
