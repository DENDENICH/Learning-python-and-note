

class ReadableTextFile:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return [s.replace('\n', '') for s in self.file.readlines()]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False if exc_type is None else True


with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile(open('glados_quotes.txt')) as file:
    for line in file:
        print(line.strip())

    for line in file:
        print(line.strip())