from collections import Counter

class Solution:
    def longest_palindrome(self, s: str) -> int:
        # one_exists = False
        # count = 0 
        # for value in Counter(s).values():
        #     if value == 1 :
        #         if not one_exists:
        #             one_exists = True
        #             count += 1
        #     else:
        #         count += value
        # return count  
        counts = Counter(s)
        return sum(v // 2 * 2 for v in counts.values()) + (any(v % 2 for v in counts.values()))  
    
solution = Solution()
print(solution.longest_palindrome("bananas"))  # Output: 7
    

