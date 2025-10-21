import re

pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[_#%])[A-Za-z\d_#%]{8,}$')

class Solution:
    def is_valid_password(self, password: str) -> bool:
        if not pattern.match(password):
            return False

        lower_password = password.lower()
        if lower_password == lower_password[::-1]:
            return False

        return True
