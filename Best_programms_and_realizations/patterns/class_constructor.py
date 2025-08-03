
class InvalidRole(Exception):
    pass


class EmployRecord:
    def __init__(self, role: str, name: str):
        self.name = name
        self.role = role


class Employ:
    """Базовый класс сотрудника"""
    pass


class Manager(Employ):
    pass


class Admin(Employ):
    pass


class EmployFactory:
    """Класс-контруктор, позволяющий создать сотрудника"""
    @classmethod
    def make_employ(cls, r: EmployRecord):
        """
        Создание определенного сотрудника, 
        взависимость от данных EmployRecord (r)
        """
        match r.role:
            case "manager":
                return Manager()
            case "admin":
                return Admin()
            case _:
                raise InvalidRole()