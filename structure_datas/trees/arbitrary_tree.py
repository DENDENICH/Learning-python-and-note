

class Node:
    """Класс объекта узла в дереве"""
    def __init__(self, value):
        # свойство значения узла
        self.value = value
        # свойство списка потомков узла
        self.children = []

    def add_child(self, child):
        """Метод для добавления потомка к узлу"""
        self.children.append(child)

    def search_node_by_value(self, value):
        """Метод для поиска узла по значению"""

        # Этот метод работает благодаря рекурсии. Он ищет узел, если он есть среди потомков, то ищет среди потомков потомков и так далее

        # Если значение узла совпадает с заданным, то возвращает его
        # (self - это ссылка на узел, значение которого совпадает с тем, по которому мы ищем)
        print(f'Сравниваем {self.value} и {value}')
        if self.value == value:
            return self
        # Если нет, то ищет среди потомков
        for child in self.children:
            # У узла мы вызываем метод поиска по значению
            # Тот метод будет сравнивать и пробегаться по всем потомкам child и так далее
            # (За схемой смотри рисунок, который скинул вместе с заданием)
            result = child.search_node_by_value(value)
            if result:
                return result

    def remove_child(self, child):
        """Метод для удаления потомка из списка потомков узла"""

        # Если потомок в списке потомков, то удаляем его
        if child in self.children:
            self.children.remove(child)
            print(f'Удален потомок {child} из списка потомков узла {self.value}')
        else:
            # Если нет, то пробегаем по всем потомкам и
            # точно также рекурсивно вызываем метод удаления у всех потомков
            for child in self.children:
                child.remove_child(child)

    def get_lenght_of_tree(self):
        """Метод для получения длины дерева"""
        count_nodes = 0
        for child in self.children:
            # Также вызываем метод для получения длины дерева у всех потомков
            count_nodes += child.get_lenght_of_tree()
        return len(self.children) + count_nodes

    def get_height_of_tree(self):
        """Метод для получения высоты дерева"""
        if not self.children:
            return 1  # если у узла нет потомков, высота = 1 (только этот узел)
        else:
            # Рекурсивно находим высоту каждого поддерева и берём максимум
            heights = [child.get_height_of_tree() for child in self.children]
            return 1 + max(heights)
