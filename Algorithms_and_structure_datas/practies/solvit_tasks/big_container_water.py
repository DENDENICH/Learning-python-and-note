# 1 - берем i элемент, начинаем перебор до конца
    # 1.1 - перебираем все элементы от i до len(height) - 1
        # 1.2 - находим наименьший среди них элемент min и расстояние между ними distance
        # 1.3 - находим объем по формуле min * distance = v
        # 1.4 - если v > v_max -> v_max = v

class Solution:
    def max_area(self, height: list[int]) -> int:
        v_max = 0
        i, i_max = 0, len(height) - 1
        while i < i_max:
            value = height[i]
            for index in range(i+1, i_max+1):
                second_value = height[index]
                min_value = min(value, second_value)

                distance_beetwen_value = index - i
                v = min_value * distance_beetwen_value
                if v > v_max:
                    v_max = v
            i += 1
        return v_max
    

s = Solution()
result = s.max_area([1,1])
print(result)
