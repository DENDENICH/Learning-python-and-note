

# Одноразовые - те объекты протокола контекстного менеджера, которые не могут быть повторно использованы

### Пример
file = open("file.txt", "r")
with file:
  print(file.read())

with file:
  print(file.read()) # >> ERROR


