class Solution:
    full_corner = 360
    minimum_length = full_corner / 60 
    lenth_of_one_hour = full_corner / 12 

    def angle_clock(self, hour: int, minutes: int) -> float:
        hour_arrow_location = self._get_arrow_location_hour(hour, minutes)
        minute_arrow_location = self.minimum_length * minutes
        return min(
            self._get_down_corner(minute_arrow_location, hour_arrow_location),
            self._get_up_corner(minute_arrow_location, hour_arrow_location)
        )

    def _get_arrow_location_hour(self, hour: int, minutes: int) -> float:
        delta_by_minut = (minutes / 12) * self.minimum_length
        if 1 <= hour < 12:
            arrow_location = hour * self.lenth_of_one_hour + delta_by_minut # расположение часовой стрелки в градусах
        elif hour == 12:
            arrow_location = delta_by_minut
        else:
            raise ValueError("value 'hour' is invalid - must be range 1 to 12")
        return arrow_location
    
    def _get_down_corner(
            self, 
            minute_arrow_location: float, 
            hour_arrow_location: float
    ) -> float:
        return abs(minute_arrow_location - hour_arrow_location)
    
    def _get_up_corner(
            self, 
            minute_arrow_location: float, 
            hour_arrow_location: float
    ) -> float:
        max_value, min_value = (
            max(minute_arrow_location, hour_arrow_location),
            min(minute_arrow_location, hour_arrow_location)
        )
        return (self.full_corner - max_value) + min_value
    

s = Solution()
result = s.angle_clock(hour=1, minutes=57)
print(result)