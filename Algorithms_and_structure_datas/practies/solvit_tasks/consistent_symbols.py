class Solution:
    def max_power(self, s: str) -> int:
        max_count = 1
        count = 1
        i, i_max = 0, len(s) - 1
        while i < i_max:
            if s[i] == s[i+1]:
                count += 1
                if count > max_count:
                    max_count = count
            else:
                count = 1
            i += 1
        return max_count

    
s = Solution()
result = s.max_power("tourist")
print(result)