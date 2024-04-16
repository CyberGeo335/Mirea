import main
import LexicalAnalysis
import SyntacticAndSemanticAnalysis


def Menu():
    print("===========================================================")
    print("Ввeдите номер команды: ")
    print("1) Ввод из файла")
    print("2) Выход из программы")
    print("===========================================================")
    print("Введите номер команды: ")
    VarMenu = int(input())

    # ОТКРЫВАЕМ ФАЙЛ С ИСХОДНЫМ КОДОМ
    if VarMenu == 1:
        main.Word = open("Code.txt", 'r')
        LexicalAnalysis.Lexer()

        print("Лексический анализ проведен успешно. Сформирован файл лексем Lexems.txt")

        SyntacticAndSemanticAnalysis.Parser()

        print("Синтаксический и семантический анализ проведены успешно.")

    else:
        print("Выход из программы")
        exit(0)