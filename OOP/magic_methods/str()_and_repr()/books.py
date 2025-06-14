

class Book:
    """Класс книги"""
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book('{self.name}', '{self.author}', {self.year})"

    def __str__(self):
        return f"{self.name} ({self.author} {self.year})"


