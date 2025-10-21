

class Solution:
    def insert_search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # не учитывая mid
            else: 
                right = mid - 1 # учитывая mid
        return left


s = Solution()
result = s.insert_search([1,3,5,6], 2)
print(result)
        
