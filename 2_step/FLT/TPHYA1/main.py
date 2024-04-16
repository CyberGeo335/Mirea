def symbol(token): 
    if token == '*' or token == '/':  
        return 3
    elif token == '+' or token == '-':
        return 2
    elif token == '(':
        return 1
    elif token == ')':  
        return -1
    else:  
        return 0


def ToRPN(expr):  
    stack = []  
    str = ''  
    for i in range(len(expr)):  
        priority = symbol(expr[i])  
        if priority == 0: 
            str += expr[i]  
        elif priority == 1: 
            stack.append(expr[i])  
        elif priority > 1:  
            str += " "
            while len(stack) != 0: 
                if symbol(stack[-1]) >= priority:  
                    str += stack.pop()  
                else:
                    break  
            stack.append(expr[i])  
        elif priority == -1:  
            str += " "
            while symbol(stack[-1]) != 1: 
                str += stack.pop()
            stack.pop()
    while len(stack):
        str += stack.pop()
    return str 


def RPNtoAnswer(rpn):  
    operand = ""
    answerstack = [] 
    for i in range(len(rpn)):  
        if rpn[i] == ' ': 
            continue 
        elif symbol(rpn[i]) == 0: 
            while rpn[i] != ' ' and symbol(rpn[i]) == 0: 
                operand += rpn[i]
                i += 1
                if i == len(rpn):
                    break
                answerstack.append(int(operand)) 
            operand = " "
        elif symbol(rpn[i]) > 1: #
            a = answerstack.pop() 
            b = answerstack.pop() 
            if rpn[i] == '+':
                answerstack.append(int(b) + int(a)) 
            elif rpn[i] == '-':
                answerstack.append(int(b) - int(a)) 
            elif rpn[i] == '*':
                answerstack.append(int(b) * int(a)) 
            elif rpn[i] == '/':
                answerstack.append(int(b) / int(a)) 
    return answerstack.pop() 


if __name__ == "__main__": 
    print("Enter your expression: ")
    enter = input()
    print("Your expression is: ")
    print(ToRPN(enter))  
    print("Your result is: ")

    print(RPNtoAnswer(ToRPN(enter))) 


