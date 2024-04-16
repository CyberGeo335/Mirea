import Menu


"""
ЛЕКСИЧЕСКИЙ АНАЛИЗАТОР
СИНТАКСИЧЕСКИЙ АНАЛИЗАТОР
СЕМАНТИЧЕСКИЙ АНАЛИЗАТОР
"""
# ГЛОБАЛЬНЫЕ МАССИВЫ И ПЕРЕМЕННЫЕ

# СТРИНГОВЫЙ МАССИВ РАЗДЕЛИТЕЛЕЙ
Delimeters = []

# СТРИНГОВЫЙ МАССИВ КЛЮЧЕВЫХ СЛОВ
KeyWord = []

# СТРИНГОВЫЙ МАССИВ ИДЕНТИФИКАТОРОВ
Identificators = []


# СЧЁТЧИКИ
CurID, CurNum = 0, 0

# СТРИНГОВЫЙ МАССИВ ЧИСЕЛ
Numbers = []

# ЭКСПОНЕНТА, СИМВОЛ И ЕСЛИБУКВА
Exponent, Symbol, IsLetter = False, False, False

# СОСТОЯНИЕ
Sost = False

#
Word = ""

WordChar = []

# ПОЗИЦИЯ АВТОМАТА Current condition position
CurPosition = 0

# МАССИВ ДЛЯ HEX
Hex = ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']

CurLexLexemWord = ""

# !!!!
CurLexemNumber = 0

# !!!!!!
CurLexLexem = 0


if __name__ == "__main__":
    Menu.Menu()
