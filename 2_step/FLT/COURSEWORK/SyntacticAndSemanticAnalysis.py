import main
import GenerateFiles
import LexicalAnalysis
from isHex import isHex
import numpy as np

Num = []

Val = []

NewFileNumbers = open("Numbers.txt", 'r')

NewFileIdentificators = open("Identificators.txt", 'r')

NewFileLexems = open("Lexems.txt", 'r')

DeclaredIdentificators = []


def ErrorParser(ErrorOfParser):
    if ErrorOfParser == 201:
        print("Error: ", ErrorOfParser, "ожидался оператор группы умножения")
        exit(0)
    elif ErrorOfParser == 201: # 202
        print("Error:", ErrorOfParser, "Ожидалось ';' после ключевого слова 'begin' или перенос строки до ключевого слова 'begin' или объявлен ещё один тип данных или другая ошибка")
        exit(0)
    elif ErrorOfParser == 203:
        print("Error: ", ErrorOfParser, "Ожидалось ';' или перенос строки")
        exit(0)
    elif ErrorOfParser == 201: #204
        print("Error:", ErrorOfParser, "ожидалось 'end.'")
        exit(0)
    elif ErrorOfParser == 205:
        print("Error: ", ErrorOfParser, "ожидался идентификатор")
        exit(0)
    elif ErrorOfParser == 206:
        print("Error: ", ErrorOfParser)
        exit(0)
    elif ErrorOfParser == 207:
        print("Error: ", ErrorOfParser, "ожидался тип перемнной")
        exit(0)
    elif ErrorOfParser == 208:
        print("Error: ", ErrorOfParser, "ожидалась ']'")
        exit(0)
    elif ErrorOfParser == 209:
        print("Error: ", ErrorOfParser, "ожидалось ключевое слово 'as'")
        exit(0)
    elif ErrorOfParser == 210:
        print("Error: ", ErrorOfParser, "ожидалось ключевое слово 'then'")
        exit(0)
    elif ErrorOfParser == 211:
        print("Error: ", ErrorOfParser, "ожидалось ключевое слово 'to'")
        exit(0)
    elif ErrorOfParser == 212:
        print("Error: ", ErrorOfParser, "ожидалось выражение")
        exit(0)
    elif ErrorOfParser == 213:
        print("Error: ", ErrorOfParser, "Ожидался do")
        exit(0)
    elif ErrorOfParser == 214:
        print("Error: ", ErrorOfParser, "ожидался оператор")
        exit(0)
    elif ErrorOfParser == 215:
        print("Error: ", ErrorOfParser, "ожидалась '('")
        exit(0)
    elif ErrorOfParser == 216:
        print("Error: ", ErrorOfParser, "ожидалась операция группы сложения")
        exit(0)
    elif ErrorOfParser == 217:
        print("Error: ", ErrorOfParser, "ожидалась ')'")
        exit(0)
    elif ErrorOfParser == 218:
        print("Error: ", ErrorOfParser, "Неопознанная ошибка")
        exit(0)
    elif ErrorOfParser == 219:
        print("Error: ", ErrorOfParser, "Ожидалась операция группы отношения")
        exit(0)
    elif ErrorOfParser == 220:
        print("Error: ", ErrorOfParser, "Неопознанная ошибка")
        exit(0)
    elif ErrorOfParser == 221:
        print("Error: ", ErrorOfParser, "Ожидалась унарная операция")
        exit(0)
    elif ErrorOfParser == 301:
        print("Error: ", ErrorOfParser, "повторное объявление переменной")
        exit(0)
    elif ErrorOfParser == 302:
        print("Error: ", ErrorOfParser, "использование необъявленной переменной")
        exit(0)


def Parser():
    Filling()
    Prog()


def add():

    #  print("Add: DeclaredIdentificators:", DeclaredIdentificators)

    DeclaredIdentificators.append(Val[main.CurLexLexem - 1])

    #  print("Add: DeclaredIdentificators:", DeclaredIdentificators)


def Check():

    #  print(DeclaredIdentificators)

    for i in DeclaredIdentificators:
        #  print("i", i)
        #  print("Type(Num[main.CurLexLexem-1])", type(Num[main.CurLexLexem-1]))

        #  print("main.Identificators[int(Val[main.CurLexLexem-1])-1])", type(main.Identificators[int(Val[main.CurLexLexem-1])-1]))

        #  print(main.Identificators)
        #  print(type(main.Identificators))

        if main.Identificators[int(Val[main.CurLexLexem-1])-1] == str(main.Identificators[int(i)-1]) and Num[main.CurLexLexem-1] == "3":
            return True

    return False


"""
<ОПИСАНИЕ>::= <ТИП> <ИДЕНТИФИКАТОР> {, <ИДЕНТИФИКАТОР> } 
!!!! ПРОВЕРИТЬ
"""


def Discription():
    if Equals("{"):
        Comment()

    #  print("main.CurLexLexemWord ", main.CurLexLexemWord)

    if Tipisation():

        #Get_Lexem()

        if Check():
            ErrorParser(301)
        else:
            add()

        Get_Lexem()

        if Equals("{"):
            Comment()

        #  print("144 main.CurLexLexemWord", main.CurLexLexemWord)
        #  print("145 ", Num[main.CurLexLexem - 1])

        while Equals(","):

            if Equals("{"):
                Comment()

            Get_Lexem()

            if not(ID()):
                ErrorParser(205)

            else:
                if Check():
                    ErrorParser(301)
                else:
                    add()

            Get_Lexem()

    else:
        ErrorParser(206)


def ID():

    #  print("ID: Num[main.CurLexLexem - 1]", Num[main.CurLexLexem - 1])

    if Num[main.CurLexLexem - 1] == "3":
        return True
    else:
        return False


def Numer():
    if Num[main.CurLexLexem - 1] == "4":
        return True
    else:
        return False


# StrArgument -> S; READY
def Equals(StrArgument):
    counter = 1
    #  print("номер:", main.CurLexLexem - 1)
    #  print("Equals: Num[main.CurLexLexem - 1]", Num[main.CurLexLexem - 1])

    if Num[main.CurLexLexem - 1] == "1":
        for i in main.KeyWord:
            if i == StrArgument:
                if str(counter) == Val[main.CurLexLexem - 1]:
                    #  print("Equals: Val[main.CurLexLexem - 1]", Val[main.CurLexLexem - 1])
                    return True
                else:
                    return False
            counter += 1
    elif Num[main.CurLexLexem - 1] == "2":
        for i in main.Delimeters:
            if i == StrArgument:
                if str(counter) == Val[main.CurLexLexem - 1]:
                    #  print("Equals: Val[main.CurLexLexem - 1]", Val[main.CurLexLexem - 1])
                    return True
                else:
                    return False
            counter += 1
    elif Num[main.CurLexLexem - 1] == "3":
        for i in main.Identificators:
            if i == StrArgument:
                if str(counter) == Val[main.CurLexLexem - 1]:
                    #  print("Equals: Val[main.CurLexLexem - 1]", Val[main.CurLexLexem - 1])
                    return True
                else:
                    return False
            counter += 1

    elif Num[main.CurLexLexem - 1] == "4":
        for i in main.Numbers:
            if i == StrArgument:
                if str(counter) == Val[main.CurLexLexem - 1]:
                    #  print("Equals: Val[main.CurLexLexem - 1]", Val[main.CurLexLexem - 1])
                    return True
                else:
                    return False
            counter += 1
    else:
        return False

    return False


"""
COMPAREOPERAND
<СОСТАВНОЙ>::= «[» <ОПЕРАТОР> { ( : | ПЕРЕВОД СТРОКИ) <ОПЕРАТОР> } «]»
READY
"""


def CompareOperand():
    while Equals(":") or Equals("\n"):
        if Equals("{"):
            Comment()

        Get_Lexem()

        Oper()

    if Equals("{"):
        Comment()

    if not(Equals("]")):
        ErrorParser(208)

    Get_Lexem()


"""
ASSIGNOPER
<ПРИСВАИВАНИЕ>::= <ИДЕНТИФИКАТОР> as <ВЫРАЖЕНИЕ>
READY
"""


def AssignOper():
    if Equals("{"):
        Comment()

    if not(Check()):
        ErrorParser(302)

    Get_Lexem()

    if Equals("{"):
        Comment()

    if not(Equals("as")):
        ErrorParser(209)

    #Get_Lexem()

    Expression()


"""
IFOPERAND
<ФИКСИРОВАННЫЙ_ЦИКЛ>::= for <ПРИСВАИВАНИЕ> to <ВЫРАЖЕНИЕ> do <ОПЕРАТОР>
READY
"""


def IfOperand():
    if Equals("{"):
        Comment()

    Get_Lexem()

    Expression()

    if Equals("{"):
        Comment()

    if not(Equals("then")):
        ErrorParser(210)

    Get_Lexem()

    Oper()

    if Equals("{"):
        Comment()

    if Equals("else"):
        Get_Lexem()
        Oper()


"""
FORCYCLE  
<ФИКСИРОВАННЫЙ_ЦИКЛ>::= for <ПРИСВАИВАНИЕ> to <ВЫРАЖЕНИЕ> do <ОПЕРАТОР>
READY
"""


def ForCycle():
    if Equals("{"):
        Comment()

    Get_Lexem()

    if ID():
        AssignOper()

    if Equals("{"):
        Comment()

    if not(Equals("to")):
        ErrorParser(211)

    Get_Lexem()

    if Equals("{"):
        Comment()

    if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
        if ID() and not(Check()):
            ErrorParser(302)
        Expression()
    else:
        ErrorParser(212)

    if Equals("{"):
        Comment()

    if not(Equals("do")):
        ErrorParser(213)

    Get_Lexem()

    Oper()


"""
WHILECYCLE  
<УСЛОВНЫЙ_ЦИКЛ>::= while <ВЫРАЖЕНИЕ> do <ОПЕРАТОР>
READY
"""


def WhileCycle():
    if Equals("{"):
        Comment()

    if ID() or Numer() or Equals("true") or Equals("true") or Equals("~") or Equals("("):
        if ID() and not(Check()):
            ErrorParser(302)
        Expression()
    else:
        ErrorParser(212)

    Get_Lexem()

    if Equals("{"):
        Comment()

    if not(Equals("do")):
        ErrorParser(213)

    if Equals("[") or Equals("if") or Equals("for") or Equals("while") or Equals("read") or Equals("write") or ID():
        Oper()
    else:
        ErrorParser(214)


"""
INPUT  
<ВВОД>::= read «(»<ИДЕНТИФИКАТОР> {, <ИДЕНТИФИКАТОР> } «)»
READY
"""


def Input():

    if Equals("{"):
        Comment()

    Get_Lexem()

    if not(Equals("(")):
        ErrorParser(215)

    Get_Lexem()

    if Equals("{"):
        Comment()

    if not(ID()):
        ErrorParser(205)

    Get_Lexem()

    if Equals("{"):
        Comment()

    while Equals(","):

        if Equals("{"):
            Comment()

        Get_Lexem()

        if ID() and not(Check()):
            ErrorParser(302)

        Get_Lexem()

    if not Equals(")"):
        ErrorParser(217)
    Get_Lexem()


"""
OUTPUT  
<ВЫВОД>::= write «(»<ВЫРАЖЕНИЕ> {, <ВЫРАЖЕНИЕ> } «)»
READY
"""


def Output():
    if Equals("{"):
        Comment()
    Get_Lexem()

    if Equals("{"):
        Comment()

    if not(Equals("(")):
        ErrorParser(215)
    #Get_Lexem()

    if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
        if ID() and not(Check()):
            ErrorParser(302)
        Expression()
        if Equals("{"):
            Comment()
        while Equals(","):

            if Equals("{"):
                Comment()

            Get_Lexem()

            if Equals("{"):
                Comment()

            if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
                if ID() and not(Check()):
                    ErrorParser(302)
                Expression()
            else:
                ErrorParser(212)

    else:
        ErrorParser(212)

    if Equals("{"):
        Comment()

    if not(Equals(")")):
        ErrorParser(217)

    Get_Lexem()


"""
NUMBER  
<ЧИСЛО>:: =	 <ЦЕЛОЕ> | <ДЕЙСТВИТЕЛЬНОЕ>
READY
"""


def Number():
    if Equals("{"):
        Comment()
    if not(Numer()):
        ErrorParser(219)
    Get_Lexem()


"""
TYPE
<ТИП>::= INT | FLOAT | BOOL
READY
"""


def Tipisation():
    if Equals("{"):
        Comment()
    if not(Equals("int")) and not(Equals("float")) and not(Equals("bool")):
        ErrorParser(207)
    Get_Lexem()
    return  True


"""
RATIO
<ОПЕРАЦИИ_ГРУППЫ_ОТНОШЕНИЯ>:: = NE | EQ | LT | LE | GT | GE
READY
"""


def Ratio():
    if Equals("{"):
        Comment()
    if not(Equals("NE") or Equals("EQ") or Equals("LT") or Equals("LE") or Equals("GT") or Equals("GE")):
        ErrorParser(219)
    Get_Lexem()


"""
ADDITION
<ОПЕРАЦИИ_ГРУППЫ_СЛОЖЕНИЯ>:: = PLUS | MIN | OR
READY
"""


def Addition():
    if Equals("{"):
        Comment()
    #  print("main.CurLexLexemWord", main.CurLexLexemWord)

    if not(Equals("plus") or Equals("min") or Equals("or")):
        ErrorParser(216)
    Get_Lexem()


"""
MULTIPLICATION
<ОПЕРАЦИИ_ГРУППЫ_УМНОЖЕНИЯ>::= MULT | DIV | AND
READY
"""


def Multiplicate():
    if Equals("{"):
        Comment()
    if not(Equals("mult") or Equals("div") or Equals("and")):
        ErrorParser(201)
    Get_Lexem()


"""
UNAR
<УНАРНАЯ ОПЕРАЦИЯ>::= ~
READY
"""


def Unar():
    if Equals("{"):
        Comment()
    if not (Equals("~")):
        ErrorParser(223)
    Get_Lexem()


"""
COMMENT
<КОММЕНТАРИЙ>::="{"<СИМВОЛ>"}"
READY
"""


def Comment():
    while not (Equals("}")):
        Get_Lexem()
    Get_Lexem()


"""
OPER
<ОПЕРАТОР>::= 	<СОСТАВНОЙ> | <ПРИСВАИВАНИЕ> | <УСЛОВНЫЙ> |<ФИКСИРОВАННЫЙ_ЦИКЛ> | <УСЛОВНЫЙ_ЦИКЛ> | <ВВОД> |<ВЫВОД>
"""


def Oper():
    if Equals("{"):
        Comment()

    if Equals("["):
        Comment()

    elif Equals("if"):
        IfOperand()

    elif Equals("for"):
        ForCycle()

    elif Equals("while"):
        WhileCycle()

    elif Equals("read"):
        Input()

    elif Equals("write"):
        Output()

    elif ID():
        AssignOper()


def Get_Lexem():
    counter = 1

    #  print("Get_Lexem: main.CurLexLexem", main.CurLexLexem)
    #  print("Get_Lexem: Num[main.CurLexLexem]", Num[main.CurLexLexem] )
    #  print("Get_Lexem: Val[main.CurLexLexem]", Val[main.CurLexLexem])

    if Num[main.CurLexLexem] == "1":
        for s in main.KeyWord:
            if str(counter) == Val[main.CurLexLexem]:
                main.CurLexLexemWord = s
                #  print(" main.CurLexLexemWord",  main.CurLexLexemWord)
            counter += 1
    elif Num[main.CurLexLexem] == "2":
        for s in main.Delimeters:
            if str(counter) == Val[main.CurLexLexem]:
                main.CurLexLexemWord = s
                #  print(" main.CurLexLexemWord", main.CurLexLexemWord)
            counter += 1
    elif Num[main.CurLexLexem] == "3":
        for s in main.Identificators:
            if str(counter) == Val[main.CurLexLexem]:
                main.CurLexLexemWord = s
                #  print(" main.CurLexLexemWord", main.CurLexLexemWord)
            counter += 1
    elif Num[main.CurLexLexem] == "4":
        for s in main.Numbers:
            if str(counter) == Val[main.CurLexLexem]:
                main.CurLexLexemWord = s
            counter += 1
    else:
        ErrorParser(201)
    #except:
        #ErrorParser(204)
    main.CurLexemNumber = main.CurLexLexem
    main.CurLexLexem += 1


def Filling():
    CurrentLexem = NewFileLexems.readlines()

    count = 0
    while count < len(CurrentLexem):
        CurrentLexem[count] = CurrentLexem[count][:-1]
        count += 1

    count = 0
    LenCurrentLexems = len(CurrentLexem)
    while count < LenCurrentLexems:
        tmp = CurrentLexem[count][:1]
        Num.append(tmp)

        tmp = CurrentLexem[count][2:]
        Val.append(tmp)

        count += 1

    #  print(Num)
    #  print(Val)


"""
СТРУКТУРА ПРОГРАММЫ:
//<ПРОГРАММА> = PROGRAM VAR <ОПИСАНИЕ> BEGIN <ОПЕРАТОР> {; <ОПЕРАТОР>} end.
"""


def Prog():
    Get_Lexem()

    if Equals("program"):
        Get_Lexem()

        if Equals("var"):
            Get_Lexem()

            if Equals("\n"):
                Get_Lexem()

            if Equals("{"):
                Comment()

            if Equals("int") or Equals("bool") or Equals("float"):
                Discription()

            if Equals("\n"):
                Get_Lexem()

            if Equals("begin"):
                Get_Lexem()

            if Equals("\n"):
                Get_Lexem()

            if Equals("[") or Equals("if") or Equals("for") or Equals("while") or Equals("read") or Equals("write") or ID():
                Oper()

            #Get_Lexem()

            while Equals(";"):
                Get_Lexem()

                if Equals("\n"):
                    Get_Lexem()

                if Equals("{"):
                    Comment()

                if Equals("\n"):
                    Get_Lexem()

                if Equals("[") or Equals("if") or Equals("for") or Equals("while") or Equals("read") or Equals("write") or ID():
                    Oper()

            if Equals("end."):
                print("конец программы")
            else:
                ErrorParser(202)

    if Equals("{"):
        Comment()

    if not (Equals("end.")):
        ErrorParser(204)


"""
EXPRESSION
<ВЫРАЖЕНИЕ>:: =	<ОПЕРАНД>{ <ОПЕРАЦИИ_ГРУППЫ_ОТНОШЕНИЯ> <ОПЕРАНД> }
"""


def Expression():
    Get_Lexem()

    if Equals("{"):
        Comment()

    if Numer() or ID() or Equals("true") or Equals("false") or Equals("~") or Equals("("):

        if Equals("{"):
            Comment()

        if ID() and not(Check()):
            ErrorParser()

        Operand()

    else:
        ErrorParser(214)

    if Equals("{"):
        Comment()

    if Equals("NE") or Equals("EQ") or Equals("LT") or Equals("LE") or Equals("GT") or Equals("GE"):
        Ratio()

        if Equals("{"):
            Comment()

        if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):

            if Equals("{"):
                Comment()

            if ID() and not(Check()):
                ErrorParser(302)

            Operand()

        else:
            ErrorParser(214)

    #Get_Lexem()


"""
OPERAND
<ОПЕРАНД>::= <СЛАГАЕМОЕ> {<ОПЕРАЦИИ_ГРУППЫ_СЛОЖЕНИЯ> <СЛАГАЕМОЕ>}
"""


def Operand():
    #  print("Operand main.CurLexLexemWord", main.CurLexLexemWord)

    if Equals("{"):
        Comment()

    if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
        if ID() and not(Check()):
            ErrorParser(302)
        Summand()

    else:
        ErrorParser(214)

    if Equals("{"):
        Comment()

    if Equals("plus") or Equals("min") or Equals("or"):
        Addition()

        if Equals("{"):
            Comment()

        if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
            if ID() and not(Check()):
                ErrorParser(302)
            Summand()
        else:
            ErrorParser(214)


"""
SUMMAND
<СЛАГАЕМОЕ>::= 	<МНОЖИТЕЛЬ> {<ОПЕРАЦИИ_ГРУППЫ_УМНОЖЕНИЯ> <МНОЖИТЕЛЬ>}
"""


def Summand():
    if Equals("{"):
        Comment()

    if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
        if ID() and not(Check()):
            ErrorParser(302)
        Multiply()

    else:
        ErrorParser(214)

    if Equals("{"):
        Comment()

    if Equals("mult") or Equals("div") or Equals("and"):

        Multiplicate()

        if Equals("{"):
            Comment()

        if ID() or Numer() or Equals("true") or Equals("false") or Equals("~") or Equals("("):
            if ID() and not(Check()):
                ErrorParser(302)
            Multiply()
        else:
            ErrorParser(214)


"""
MULTIPLY
<МНОЖИТЕЛЬ>::= 	<ИДЕНТИФИКАТОР> | <ЧИСЛО> | <ЛОГИЧЕСКАЯ_КОНСТАНТА> |<УНАРНАЯ_ОПЕРАЦИЯ> <МНОЖИТЕЛЬ> | «(»<ВЫРАЖЕНИЕ>«)»
"""


def Multiply():
    if Equals("{"):
        Comment()

    if Equals("("):

        Get_Lexem()

        Expression()

        if Equals("{"):
            Comment()

        if not(Equals(")")):
            ErrorParser(217)

    if Equals("{"):
        Comment()

    elif Equals("~"):
        Unar()

    Get_Lexem()