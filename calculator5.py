import re

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

def input_data(M):

    while(True):
        print(msg_0)
        calc = input()
        elms = calc.split()
        if not re.match("[0-9\.M]", elms[0]):
            print(msg_1)
            continue
        if not re.match("[0-9\.M]", elms[2]):
            print(msg_1)
            continue
        if not elms[1] in "+-*/":
            print(msg_2)
            continue

        if elms[0] == "M":
            x = M[0] 
        else:
            x = float(elms[0])

        oper = elms[1]

        if elms[2] == "M":
            y = M[0] 
        else:
            y = float(elms[2])

        return x, oper, y

def calculate(x, oper, y):
    if oper == "/" and y == 0:
        print(msg_3)
        return None

    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/":
        return x / y

def confirm_store_result(result):
    if not is_one_digit(result):
        return True

    msg_index = 10
    while(True):
        if msg_index == 10: 
            print(msg_10)
        elif msg_index == 11: 
            print(msg_11)
        elif msg_index == 12: 
            print(msg_12)
        yn = input()
        if yn == "y":
            if msg_index == 13:
                return True
            msg_index += 1
        elif yn == "n":
            return False

def store_result(result, M):
    while(True):
        print(msg_4)
        yn = input()
        if yn == "y":
            if confirm_store_result(result):
                M[0] = result
        if yn in "yn":
            break 

def confirm_continue():
    while(True):
        print(msg_5)
        yn = input()
        if yn == "y":
            answer = True
        if yn == "n":
            answer = False
        if yn in "yn":
            return answer

def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7
    if (x == 0 or y == 0) and oper in ("+-*"):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)
 
def is_one_digit(n):
    if abs(n) > 9:
        return False

    if int(n) != n:
        return False

    return True

if __name__ == "__main__":
    M = [0]    
    while(True):
        x, oper, y = input_data(M)
        check(x, y, oper)
        result = calculate(x, oper, y)
        if result == None:
            continue
        print(result)
        store_result(result, M)
        if not confirm_continue():
            break