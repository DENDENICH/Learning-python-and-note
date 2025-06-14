from enum import Enum
from dataclasses import dataclass

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

@dataclass
class FilterOrganizer:
    id: int
    role: Role

r1 = FilterOrganizer(id=1, role=Role.ADMIN)
print(r1)

