
class Solution:
    def removeStars(self, s: str) -> str:
        count_stars = s.count("*")
        while count_stars > 0:
            index_left_star = s.find("*")
            deleting_symbols = s[index_left_star-1:index_left_star+1:]
            s = s.replace(deleting_symbols, "")
            count_stars -= 1
        return s
    

solution = Solution()
print(solution.removeStars("erase*****"))
