class Solution:
    def reverse_string(self, s: list[str]) -> None:
        cursor = 0
        index_last_element = len(s) - 1
        while cursor < index_last_element:
            el = s.pop(index_last_element)
            s.insert(cursor, el) 
            cursor += 1
        print(s)



    
s = Solution()
s.reverse_string(["H","a","n","n","a","h"])