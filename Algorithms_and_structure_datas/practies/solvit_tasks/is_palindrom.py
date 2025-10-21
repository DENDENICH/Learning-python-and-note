import string
import re

re_punctuation = rf"[{string.punctuation}\\ ]" # with space

class Solution:
    def is_palindrome(self, s: str) -> bool:
        s_handlering = re.sub(re_punctuation, "", s).lower()
        return s_handlering == s_handlering[::-1]


s = Solution()
print(s.is_palindrome(r"Was it\ a rat I saw?"))