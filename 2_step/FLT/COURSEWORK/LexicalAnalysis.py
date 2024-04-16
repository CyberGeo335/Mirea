import GenerateFiles
import main
from isHex import isHex
import numpy as np

"""
1 - KEYWORDS
2 - DELIMETERS
3 - IDENTIFICATORS
4 - NUMBERS
"""


def Lexer():
    # ЕСЛИ ЭТО ID
    IsID = True

    # БУФЕР ДЛЯ СЛОВА
    BufWord = ""

    # БУФЕР ДЛЯ ЧИСЕЛ
    BufNum = ""

    # ДВУМЕРНЫЙ МАССИВ ЛЕКСЕММ
    Lexems = np.empty((512,2), dtype="object")

    # СТРИНГОВЫЙ МАССИВ, КУДА БУДЕМ ЗАПИСЫВАТЬ КЛЮЧЕВЫЕ СЛОВА
    KeyWordRead = []

    # СТРИНГОВЫЙ МАССИВ, КУДА БУДЕМ ЗАПИСЫВАТЬ КЛЮЧЕВЫЕ РАЗДЕЛИТЕЛИ
    DelimetersRead = []

    CurrentLexem = 0  #

    # НЫНЕШНЕЕ СОСТОЯНИЕ АВТОМАТА
    CurrentCondition = "H"

    # В WORDCHAR ЗАПИСЫВАЕМ НАШ ФАЙЛ
    main.WordChar = main.Word.read()
    # ПЕРЕОПРЕДЕЛЯЕМ МАССИВ В ЛИСТ, ЧТОБЫ КАЖДЫЙ CHAR БЫЛ ОТДЕЛЬНО
    main.WordChar = list(main.WordChar)

    # print(main.WordChar) DEBUG

    # В FileKeyWords ЗАПИСЫВАЕМ ДАННЫЕ ФАЙЛА
    FileKeyWords = open("KeyWords.txt", 'r')

    # СЧИТЫВАЕМ СТРОКИ
    TempKeyWordRead = FileKeyWords.readlines()

    # ЦИКЛ WHILE ПРЕДНАЗНАЧЕН ДЛЯ ПЕРЕНОСА ЗНАЧЕНИЙ ИЗ TempKeyWordRead
    # В KeyWordRead БЕЗ \n
    count = 0
    LenTKWR = len(TempKeyWordRead) - 1
    while LenTKWR >= count:
        TempChar = TempKeyWordRead[count]
        TempChar = TempChar[0:len(TempKeyWordRead[count]) - 3]
        if TempChar[-1] == ' ':
            TempChar = TempChar[:-1]
        KeyWordRead.append(TempChar)
        count += 1

    #print(KeyWordRead)  # DEBUG

    main.KeyWord = KeyWordRead

    #print(main.KeyWord)

    # В FileDelimetersRead ЗАПИСЫВАЕМ ДАННЫЕ ФАЙЛА
    FileDelimetersRead = open("Delimeters.txt", 'r')

    # СЧИТЫВАЕМ СТРОКИ
    TempDelimetersRead = FileDelimetersRead.readlines()

    # ЦИКЛ WHILE ПРЕДНАЗНАЧЕН ДЛЯ ПЕРЕНОСА ЗНАЧЕНИЙ ИЗ TempDelimetersRead
    # В DelimetersRead БЕЗ \n
    count = 0
    LenTDR = len(TempDelimetersRead) - 1
    while LenTDR >= count:
        TempChar = TempDelimetersRead[count]
        TempChar = TempChar[0:len(TempDelimetersRead[count]) - 3]
        if TempChar[-1] == ' ':
            TempChar = TempChar[:-1]
        DelimetersRead.append(TempChar)
        count += 1

    DelimetersRead[8] = '\n'
    #print(DelimetersRead)  # DEBUG

    main.Delimeters = DelimetersRead

    #print(main.Delimeters)

    # ПОКА ПОЗИЦИЯ АВТОМАТА МЕНЬШЕ ДЛИНЫ МАССИВА, СОСТОЯЩЕГО ИЗ ЧАРОВ
    # CurrentCondition - СОСТОЯНИЕ АВТОМАТА
    # CurPosition - СОСТОЯНИЕ АВТОМАТА
    LenMainChar = len(main.WordChar)
    while main.CurPosition < LenMainChar:

        # ЕСЛИ СОСТОЯНИЕ АВТОМАТА РАВНО 'H'
        if CurrentCondition == "H":

            if main.WordChar[main.CurPosition] == '\t' or main.WordChar[main.CurPosition] == ' ' or main.WordChar[main.CurPosition] == '\r':
                main.CurPosition += 1

            elif main.WordChar[main.CurPosition] == 'e':
                # FIN
                CurrentCondition = "FINISH"

            elif main.WordChar[main.CurPosition] == '\n':
                # NewLine
                CurrentCondition = "NEWLINE"

            # ДОБАВИЛ ; надо проверить
            elif main.WordChar[main.CurPosition] == ':' or main.WordChar[main.CurPosition] == '[' or main.WordChar[main.CurPosition] == '{' or main.WordChar[main.CurPosition] == '}' or main.WordChar[main.CurPosition] == ')' or main.WordChar[main.CurPosition] == ',' or main.WordChar[main.CurPosition] == ']' or main.WordChar[main.CurPosition] == '(' or main.WordChar[main.CurPosition] == '~' or main.WordChar[main.CurPosition] == ';':
                main.Sost = False
                # DLM
                CurrentCondition = "DELIMETER"

            elif main.WordChar[main.CurPosition].isalpha():
                BufWord = ""
                # ID
                CurrentCondition = "ID"

            elif main.WordChar[main.CurPosition].isdigit():
                main.IsLetter = False
                BufNum = ""
                # NM
                CurrentCondition = "NUMBER"

            else:
                main.Sost = False
                # DLM
                CurrentCondition = "DELIMETER"

        elif CurrentCondition == "NEWLINE":

            #Lexems[CurrentLexem][0] = str(2)  # ВТОРАЯ ТАБЛИЦА - DELIMETERS
            #Lexems[CurrentLexem][1] = str(9)  # ДЕВЯТАЯ СТРОЧКА В ТАБЛИЦЕ DELIMETERS

            Lexems[CurrentLexem, 0] = str(2)
            Lexems[CurrentLexem, 1] = str(9)

            CurrentLexem += 1
            main.CurPosition += 1

            # ВОЗВРАЩАЕМСЯ В НАЧАЛЬНОЕ СОСТОЯНИЕ АВТОМАТА
            CurrentCondition = "H"

        elif CurrentCondition == "FINISH":

            #print("main.WordChar: ", main.WordChar)
            #print("len(main.WordChar): ", len(main.WordChar))
            #print("main.WordChar[main.CurPosition + 1]", main.WordChar[main.CurPosition + 1])
            #print("main.WordChar[main.CurPosition + 2]", main.WordChar[main.CurPosition + 2])
            #print("main.WordChar[main.CurPosition + 3]", main.WordChar[main.CurPosition + 3])

            if main.WordChar[main.CurPosition + 1] == 'n' and main.WordChar[main.CurPosition + 2] == 'd' and main.WordChar[main.CurPosition + 3] == '.' and len(main.WordChar) == (main.CurPosition + 4):

                #Lexems[CurrentLexem][0] = str(1)  # ПЕРВАЯ ТАБЛИЦА - KEYWORDS
                #Lexems[CurrentLexem][1] = str(16)  # ШЕСТНАДЦАТАЯ СТРОЧКА В ТАБЛИЦЕ KEYWORDS

                Lexems[CurrentLexem, 0] = str(1)
                Lexems[CurrentLexem, 1] = str(16)

                CurrentLexem += 1
                main.CurPosition = main.CurPosition + 3
                CurrentCondition = "H"  # ВОЗВРАЩАЕМСЯ В НАЧАЛЬНОЕ СОСТОЯНИЕ АВТОМАТА
                break

            else:
                ErrorLexer(102)  # ПЕРЕДАЁМ ОШИБКУ



        # ID
        elif CurrentCondition == "ID":

            if main.WordChar[main.CurPosition].isdigit() or main.WordChar[main.CurPosition].isalpha():
                BufWord += main.WordChar[main.CurPosition]

                #print(BufWord)
                #print("148: ", GetLexems(BufWord)[0])

                if GetLexems(BufWord)[0] != 0:
                    main.CurPosition += 1
                    CurrentCondition = "ID"

                    #Lexems[CurrentLexem][0] = str(GetLexems(BufWord)[0])
                    #Lexems[CurrentLexem][1] = str(GetLexems(BufWord)[1])

                    Lexems[CurrentLexem,0] = str(GetLexems(BufWord)[0])
                    Lexems[CurrentLexem,1] = str(GetLexems(BufWord)[1])

                    #print( Lexems[CurrentLexem,0])
                    #print( Lexems[CurrentLexem,1])
                    #exit(0)

                    IsID = True

                else:
                    IsID = False

                    # Lexems[CurrentLexem][0] = str(3)
                    # Lexems[CurrentLexem][1] = str(main.CurID + 1)

                    Lexems[CurrentLexem, 0] = str(3)
                    Lexems[CurrentLexem, 1] = str(main.CurID + 1)

                    main.CurPosition += 1
                    CurrentCondition = "ID"
            else:
                if not (IsID):

                    #print("BufWord: ", BufWord)
                    #print(main.CurID)

                    #main.Identificators[main.CurID] = BufWord

                    main.Identificators.append(BufWord)
                    main.CurID += 1
                CurrentLexem += 1
                CurrentCondition = "H"

        elif CurrentCondition == "NUMBER":

            if main.WordChar[main.CurPosition] == '0' or main.WordChar[main.CurPosition] == '1':
                # BIN
                CurrentCondition = "BIN"

            elif int(main.WordChar[main.CurPosition]) > 1 and int(main.WordChar[main.CurPosition]) < 8:
                # OCT
                CurrentCondition = "OCT"

            elif int(main.WordChar[main.CurPosition]) > 7 or isHex(main.WordChar[main.CurPosition]):
                CurrentCondition = "DECHEX"

            else:
                ErrorLexer(101)  # ОШИБКА

        elif CurrentCondition == "BIN":

            BufNum += main.WordChar[main.CurPosition]

            if main.WordChar[main.CurPosition] == 'O' or main.WordChar[main.CurPosition] == 'o':
                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                NumberOfSystem = "OCT"
                main.Numbers[main.CurNum] = GetNum(BufNum, NumberOfSystem)
                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'd' or main.WordChar[main.CurPosition] == 'D':

                if main.WordChar[main.CurPosition] == 'd' and main.WordChar[main.CurPosition] == 'i':
                    ErrorLexer(107)

                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                main.Numbers[main.CurNum] = BufNum[0:len(BufNum) - 1]
                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'H' or main.WordChar[main.CurPosition] == 'h':
                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                NumberOfSystem = "HEX"
                main.Numbers[main.CurNum] = GetNum(BufNum, NumberOfSystem)
                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'B' or main.WordChar[main.CurPosition] == 'b':
                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                NumberOfSystem = "BIN"

                #main.Numbers[main.CurNum] = GetNum(BufNum, NumberOfSystem)

                main.Numbers.append(GetNum(BufNum, NumberOfSystem))
                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'e' or main.WordChar[main.CurPosition] == 'E' or main.WordChar[
                main.CurPosition] == '.':
                main.CurPosition -= 1
                BufNum = BufNum[0:len(BufNum) - 1]
                CurrentCondition = "EXP"

            elif int(main.WordChar[main.CurPosition]) > 1 and int(main.WordChar[main.CurPosition]) < 8:
                CurrentCondition = "OCT"

            elif main.WordChar[main.CurPosition] == '0' or main.WordChar[main.CurPosition] == '1':
                CurrentCondition = "BIN"

            elif int(main.WordChar[main.CurPosition]) > 7 or isHex(main.WordChar[main.CurPosition]):
                CurrentCondition = "DECHEX"

            else:
                ErrorLexer(103)

            main.CurPosition += 1

        elif CurrentCondition == "OCT":

            BufNum += main.WordChar[main.CurPosition]

            if main.WordChar[main.CurPosition] == 'O' or main.WordChar[main.CurPosition] == 'o':
                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)  # ЧЕТВЁРТАЯ ТАБЛИЦА - IDENTIFICATORS
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)
                NumberOfSystem = "OCT"

                #main.Numbers[main.CurNum] = GetNum(BufNum, NumberOfSystem)

                main.Numbers.append(GetNum(BufNum, NumberOfSystem))

                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'd' or main.WordChar[main.CurPosition] == 'D':

                if main.WordChar[main.CurPosition] == 'd' and main.WordChar[main.CurPosition] == 'i':
                    ErrorLexer(107)

                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                #main.Numbers[main.CurNum] = BufNum[0:len(BufNum) - 1]

                main.Numbers.append(BufNum[0:len(BufNum) - 1])

                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'H' or main.WordChar[main.CurPosition] == 'h':
                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                NumberOfSystem = "HEX"

                #main.Numbers[main.CurNum] = GetNum(BufNum, NumberOfSystem)

                main.Numbers.append(GetNum(BufNum, NumberOfSystem))

                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'e' or main.WordChar[main.CurPosition] == 'E' or main.WordChar[
                main.CurPosition] == '.':
                main.CurPosition -= 1
                BufNum = BufNum[0:len(BufNum) - 1]
                CurrentCondition = "EXP"

            elif int(main.WordChar[main.CurPosition]) > 1 and int(main.WordChar[main.CurPosition]) < 8:
                CurrentCondition = "OCT"

            elif main.WordChar[main.CurPosition] == '0' or main.WordChar[main.CurPosition] == '1':
                CurrentCondition = "BIN"

            elif int(main.WordChar[main.CurPosition]) > 7 or isHex(main.WordChar[main.CurPosition]):
                CurrentCondition = "DECHEX"

            else:
                ErrorLexer(104)

            main.CurPosition += 1
        # ФУЛЛ ИЗУЧИТЬ И ПЕРЕПРОВЕРИТЬ
        elif CurrentCondition == "EXP":
            if main.WordChar[main.CurPosition] == 'd' or main.WordChar[main.CurPosition] == 'D' or main.WordChar[main.CurPosition] == 'h' or main.WordChar[main.CurPosition] == 'h' or main.WordChar[main.CurPosition] == 'o' or main.WordChar[main.CurPosition] == 'O' or main.WordChar[main.CurPosition] == 'b' or main.WordChar[main.CurPosition] == 'B':
                ErrorLexer(112)

            if main.WordChar[main.CurPosition] == 'e' or main.WordChar[main.CurPosition] == 'E':
                main.IsLetter = True
                BufNum += main.WordChar[main.CurPosition]
                main.Exponent = True

            elif main.WordChar[main.CurPosition] == '.' and main.Exponent == True:
                ErrorLexer(105)

            elif main.WordChar[main.CurPosition] == '.' and main.Exponent == False:
                BufNum += main.WordChar[main.CurPosition]

            elif main.WordChar[main.CurPosition].isdigit():
                BufNum += main.WordChar[main.CurPosition]

            elif (main.WordChar[main.CurPosition] == '+' or main.WordChar[
                main.CurPosition] == '-') and main.Exponent == False:
                ErrorLexer(106)

            elif main.WordChar[main.CurPosition] == '\n' or main.WordChar[main.CurPosition] == ';':
                # ЧЕТВЁРТАЯ ТАБЛИЦА - IDENTIFICATORS
                Lexems[CurrentLexem][0] = str(4)
                Lexems[CurrentLexem][1] = str(main.CurNum + 1)
                print(BufNum[0:len(BufNum)])
                #print("5.e+1")
                main.Numbers.append(BufNum[0:len(BufNum)])
                CurrentLexem += 1
                main.CurNum += 1

                if main.WordChar[main.CurPosition] == '\n':

                    #Lexems[CurrentLexem][0] = str(2)
                    #Lexems[CurrentLexem][1] = str(9)

                    Lexems[CurrentLexem, 0] = str(2)
                    Lexems[CurrentLexem, 1] = str(9)

                    CurrentLexem += 1
                CurrentCondition = "H"

            elif main.WordChar[main.CurPosition].isalpha() and (
                    main.WordChar[main.CurPosition] != 'e' or main.WordChar[main.CurPosition] != 'E'):
                ErrorLexer(113)
            else:
                BufNum += main.WordChar[main.CurPosition]
            main.CurPosition += 1

        elif CurrentCondition == "DECHEX":

            BufNum += main.WordChar[main.CurPosition]

            if main.WordChar[main.CurPosition] == 'H' or main.WordChar[main.CurPosition] == 'h':
                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)  # ЧЕТВЁРТАЯ ТАБЛИЦА - IDENTIFICATORS
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                main.Numbers[main.CurNum] = BufNum[0:len(BufNum) - 1]
                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'd' or main.WordChar[main.CurPosition] == 'D':

                if main.WordChar[main.CurPosition] == 'd' and main.WordChar[main.CurPosition] == 'i':
                    ErrorLexer(107)

                main.IsLetter = True
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(4)
                #Lexems[CurrentLexem][1] = str(main.CurNum + 1)

                Lexems[CurrentLexem, 0] = str(4)
                Lexems[CurrentLexem, 1] = str(main.CurNum + 1)

                main.Numbers[main.CurNum] = BufNum[0:len(BufNum) - 1]
                CurrentLexem += 1
                main.CurNum += 1

            elif main.WordChar[main.CurPosition] == 'e' or main.WordChar[main.CurPosition] == 'E' or main.WordChar[
                main.CurPosition] == '.':
                main.CurPosition -= 1
                BufNum = BufNum[0:len(BufNum) - 1]
                CurrentCondition = "EXP"

            else:
                ErrorLexer(108)

            main.CurPosition += 1

        elif CurrentCondition == "DELIMETER":

            if main.WordChar[main.CurPosition] == '(' or main.WordChar[main.CurPosition] == ')' or main.WordChar[main.CurPosition] == ':' or main.WordChar[main.CurPosition] == '[' or main.WordChar[main.CurPosition] == ']' or main.WordChar[main.CurPosition] == ',' or main.WordChar[main.CurPosition] == ';':
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                #Lexems[CurrentLexem][1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])

                Lexems[CurrentLexem, 0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                Lexems[CurrentLexem, 1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])

                main.CurPosition += 1
                CurrentLexem += 1

            elif main.WordChar[main.CurPosition] == '{':
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                #Lexems[CurrentLexem][1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])

                Lexems[CurrentLexem, 0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                Lexems[CurrentLexem, 1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])

                main.CurPosition += 1
                CurrentLexem += 1

            elif main.WordChar[main.CurPosition] == '}':
                CurrentCondition = "H"

                #Lexems[CurrentLexem][0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                #Lexems[CurrentLexem][1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])

                Lexems[CurrentLexem, 0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                Lexems[CurrentLexem, 1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])
                main.CurPosition += 1
                CurrentLexem += 1

            elif main.WordChar[main.CurPosition].isdigit() or main.WordChar[main.CurPosition].isalpha():

                if main.Sost == True:
                    Lexems[CurrentLexem, 0] = str(GetLexems(str(main.WordChar[main.CurPosition]))[0])
                    Lexems[CurrentLexem, 1] = str(GetLexems(str(main.WordChar[main.CurPosition]))[1])

                    #Lexems[CurrentLexem][0] = str(GetLexems(main.WordChar[main.CurPosition - 1])[0])
                    #Lexems[CurrentLexem][1] = str(GetLexems(main.WordChar[main.CurPosition - 1])[1])

                    CurrentLexem += 1

                CurrentCondition = "H"
            else:
                ErrorLexer(110)

    #print("ПОЧТИ ВСЁ ХОРОШО !")

    if main.IsLetter == False:
        ErrorLexer(111)

    CountCurLexem = 0
    while CountCurLexem < CurrentLexem:
        tmp = str(Lexems[CountCurLexem, 0]) + " " + str(Lexems[CountCurLexem, 1]) + "\n"
        GenerateFiles.FileLexems.write(tmp)
        CountCurLexem += 1
    GenerateFiles.FileLexems.close()

    CountNumbers = 0
    while CountNumbers < len(main.Numbers):
        if main.Numbers[CountNumbers] != None:
            tmp = str(main.Numbers[CountNumbers]) + " " + str(CountNumbers + 1) + "\n"
            GenerateFiles.FileNumbers.write(tmp)
        CountNumbers += 1
    GenerateFiles.FileNumbers.close()

    #print("main.Identificators: ", main.Identificators)

    CountIdentificators = 0
    while CountIdentificators < len(main.Identificators):
        if main.Identificators[CountIdentificators] != None:
            tmp = str(main.Identificators[CountIdentificators] + " " + str(CountIdentificators + 1) + "\n")
            GenerateFiles.FileIdentificators.write(tmp)
        CountIdentificators += 1
    GenerateFiles.FileIdentificators.close()

def ErrorLexer(NumOfError):
    if NumOfError == 101:
        print("Error: ", NumOfError, "Ожидалось число.")
        exit(0)
    elif NumOfError == 102:
        print("Error: ", NumOfError, "Ожидалось число 'end.'")
        exit(0)
    elif NumOfError == 103:
        print("Error: ", NumOfError, "Ожидалось число или e или E или. или b или B.")
        exit(0)
    elif NumOfError == 104:
        print("Error: ", NumOfError, "Ожидалось число или e или E или. или o или O.")
        exit(0)
    elif NumOfError == 105:
        print("Error: ", NumOfError, "Ожидалось отсутствие точки после e.")
        exit(0)
    elif NumOfError == 106:
        print("Error: ", NumOfError, "Ожидалось e или E")
        exit(0)
    elif NumOfError == 107:
        print("Error: ", NumOfError, "Ожидалось i после d.")
        exit(0)
    elif NumOfError == 108:
        print("Error: ", NumOfError, "Ожидалось число или e или E или. или d или D или h или H.")
        exit(0)
    elif NumOfError == 109:
        print("Error: ", NumOfError, "")
        exit(0)
    elif NumOfError == 110:
        print("Error: ", NumOfError, "Ожидался разделитель.")
        exit(0)
    elif NumOfError == 111:
        print("Error: ", NumOfError, "Ожидалась буква для описания сс.")
        exit(0)
    elif NumOfError == 112:
        print("Error: ", NumOfError, "Ожидалось продолжение действительного числа.")
        exit(0)
    elif NumOfError == 113:
        print("Error: ", NumOfError, "Ожидалось продолжение действительного числа.")
        exit(0)
    elif NumOfError == 114:
        print("Error: ", NumOfError, "Ожидалось D или d или B или b или H или h или O или o или . или E или e или число.")
        exit(0)


def GetNum(BufNum, NumberOfSystem):
    if BufNum[len(BufNum) - 1] == 'o' or BufNum[len(BufNum) - 1] == 'O' or BufNum[len(BufNum) - 1] == 'h' or BufNum[len(BufNum) - 1] == 'H' or BufNum[len(BufNum) - 1] == 'b' or BufNum[len(BufNum) - 1] == 'B':
        BufNum = BufNum[0:len(BufNum) - 1]
    if NumberOfSystem == "HEX":
        BufNum = int(BufNum)
        BufNum = hex(BufNum)
        return str(BufNum)
    elif NumberOfSystem == "BIN":
        BufNum = int(BufNum)
        BufNum = bin(BufNum)
        return str(BufNum)
    elif NumberOfSystem == "OCT":
        BufNum = int(BufNum)
        BufNum = oct(BufNum)
        return str(BufNum)
    return "0"

# Получаем Лексемы
def GetLexems(Word):
    cur = 1

    #print("Word", Word)
    #print(main.KeyWord)
    #print("Delimeters: ", main.Delimeters)

    for s in main.KeyWord:

        #print("word == s: ", Word, "==", s)
        #print(bool(Word == s))

        if Word == s:
            #print("Debug: ", 1, cur)
            return (1, cur)
        cur += 1
    cur = 1
    for s in main.Delimeters:

        #print("Word == s: ", Word, "==", s)
        #print(bool(Word == s))

        if Word == s:
            #print("Debug: ", 2, cur)
            return (2, cur)
        cur += 1
    return (0, 0)



