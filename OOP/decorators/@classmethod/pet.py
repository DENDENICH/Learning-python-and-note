
# Класс для представления животных

class Pet:
    # Список для хранения экземпляров класса
    __instance = list()

    def __new__(cls,*args,**kwargs):
        # Создание нового экземпляра класса и добавление его в список экземпляров
        cls.__instance.append(super().__new__(cls))
        return cls.__instance[-1]

    def __init__(self, name):
        self.name = name

    @classmethod
    def first_pet(cls):
        """Возвращает первый добавленный экземпляр класса"""
        try:
            return cls.__instance[0]
        except IndexError:
            return None

    @classmethod
    def last_pet(cls):
        """Возвращает последний добавленный экземпляр класса"""
        try:
            return cls.__instance[-1]
        except IndexError:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.__instance)

    def __repr__(self):
        return f'Class Pet: {self.name}'


pet1 = Pet('Kitty')
pet2 = Pet('Jerry')
print(Pet.num_of_pets())
print(Pet.last_pet())
