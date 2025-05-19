import re


class StrExtension:

    @staticmethod
    def remove_vowels(string: str) -> str:
        """Удаление всех гласных букв из строки"""
        not_vowel_string = re.sub(
            pattern=r"[aeiouyAEIOUY]", 
            repl="",
            string=string,
        )
        return not_vowel_string

    @staticmethod
    def leave_alpha(string: str) -> str:
        """Удаление всех символов, не являющиеся латинскими буквами"""
        only_alpha_string = re.sub(
            pattern=r"[\W\d_]", 
            repl="",
            string=string,
        )
        return only_alpha_string

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        """Заменяет в строке string все символы из chars на char"""
        replacing_string = re.sub(
            pattern=f"[{chars}]", 
            repl=char,
            string=string,
        )
        return replacing_string


strex = StrExtension()
print(strex.remove_vowels("Python"))
print(strex.replace_all("Python", "Ptn", "-"))
print(strex.leave_alpha(r"__Stepik__() 345,+"))
