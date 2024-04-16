import re  # регулярки
from typing import Tuple
from enum import Enum  # ПЕРЕЧИСЛЕНИЕ



# Класс Лексемы
class Lexems(Enum):

    BEGIN_OBJECT = '{'  # НАЧАЛО ОБЪЕКТА

    END_OBJECT = '}'  # КОНЕЦ ОБЪЕКТА

    BEGIN_ARRAY = '[' # НАЧАЛО МАССИВА

    END_ARRAY = ']'  # КОНЕЦ МАССИВА

    COMMA = ','

    COLON = ':'

    # это метод, который получает класс в качестве неявного первого аргумента
    @classmethod
    def HasKey(cls, item):
        return any(x for x in cls if x.value == item)


def SolveString(string: str) -> Tuple[str, str]:
    # Стринговый парсер
    # переменная которую мы возвращаем
    output = ''

    # Symbols cycle
    while string[0] != '"':

        # We found protected closing qu?
        # МЫ НАШЛИ ЗАКРЫВАЮЩИЕ КАВЫЧКИ
        if string[0] == '\\' and string[1] == '"':
            # Yes

            #добавляем в output
            output += "\""

            # удаляем их строки
            string = string[2:]
            continue


        # Добавляем символ в output
        output += string[0]

        # Removing this char from string
        string = string[1:]

    # Return string
    return output, string[1:]


def JsonAnalyzer(file_name: str):

    # Reading file
    with open("data.json", mode='r+', encoding='UTF-8') as f:
        data = f.read()

    # Начало вывода
    print("Лист токенов: ")

    # Line counter (for error output, if any)
    line_no = 1

    # Цикл будет выполняться до тех пор пока не станет пустым
    while data:

        if data[0] == '\n': # если у нас \n
            line_no += 1
            data = data[1:] # происходит срез
            continue

        elif data[0] == ' ': # если у нас ' '
            data = data[1:] # происходит срез
            continue

        # One-char lexemes
        elif Lexems.HasKey(data[0]):
            lexem = Lexems(data[0])
            print(f"({lexem.name}, ‘{lexem.value}’)")
            data = data[1:]

        # true
        elif data.startswith('true'):
            print("(LITERAL, ‘true’)")
            data = data[4:]

        # false
        elif data.startswith('false'):
            print("(LITERAL, ‘false’)")
            data = data[5:]

        # null
        elif data.startswith('null'):
            print("(LITERAL, ‘null’)")
            data = data[4:]

        # string
        elif data[0] == '"':

            # Deleting " char
            data = data[1:]

            # Finding string
            string, data = SolveString(data)

            # Printing string token
            print(f'(STRING, ‘{string}’)')

        elif data[0].isdigit() or data[0] == '-' or data[0] == '+':
            for string in re.finditer('-?[0-9]+.?e?\d+', data): # РЕГУЛЯРНОЕ ВЫРАЖЕНИЕ
                string = string.group(0)
                break
            else:
                raise RuntimeWarning(f"Can't understand number at line {line_no}")
            data = data[len(string):]

            print(f'(НОМЕР, {string})')

        # Если найден неизвестный символ
        else:
            raise RuntimeWarning(f'Неизвестный символ "{data[0]}" на строке № {line_no}')


def main():
    JsonAnalyzer('translations.json')


if __name__ == '__main__':
    main()
