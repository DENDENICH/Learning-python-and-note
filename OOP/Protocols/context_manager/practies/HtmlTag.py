

class HtmlTag:
    _level = 0

    @classmethod
    def level(cls) -> int:
        return cls._level

    @classmethod
    def increment_level(cls) -> None:
        cls._level += 1

    @classmethod
    def decreasing_level(cls) -> None:
        cls._level -= 1

    def __init__(self, tag: str, inline: bool = False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        if self.inline:
            print('  ' * self.level() + '<' + self.tag + '>', end='')
        else:
            print('  ' * self.level() + '<' + self.tag + '>')
        self.increment_level()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            return True
        else:
            self.decreasing_level()
            if self.inline:
                print('</' + self.tag + '>')
            else:
                print('  ' * self.level() + '</' + self.tag + '>')
            return False

    def print(self, text):
        if self.inline:
            print(text, end='')
        else:
            print('  ' * self.level() + text)


with HtmlTag('body') as _:
    with HtmlTag('h1') as header:
        header.print('Поколение Python')
    with HtmlTag('p') as section:
        section.print('Cерия курсов по языку программирования Python от команды BEEGEEK')
