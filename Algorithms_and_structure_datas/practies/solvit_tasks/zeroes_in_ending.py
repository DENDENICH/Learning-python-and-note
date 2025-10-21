

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Возврат значения не требуется, все изменения выполняются на месте.
        """
        for num in nums:
            if num == 0:
                nums.append(num)
                nums.remove(num)
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])


