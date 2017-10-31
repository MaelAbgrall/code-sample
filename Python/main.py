"""module docstring:
this is a basic calculator
"""
def add(numberCurrent, numberAdd):
    """add docstring:
    return numberCurrent plus numberAdd
    """
    result = numberCurrent + numberAdd
    return result

def sub(numberCurrent, numberSub):
    """sub docstring:
    return numberCurrent minus numberSub
    """
    result = numberCurrent - numberSub
    return result

def mult(numberCurrent, numberMult):
    """mult docstring:
    return numberCurrent multiplied by numberMult
    """
    result = numberCurrent * numberMult
    return result

def div(numberCurrent, numberDiv):
    """div docstring:
    return numberCurrent divided by numberDiv
    """
    result = numberCurrent / numberDiv
    return result

def power(numberCurrent, numberPower):
    """power docstring:
    return numberCurrent exponent numberPower
    """
    result = pow(numberCurrent, numberPower)
    return result

def root(numberCurrent, numberRoot):
    """root  docstring:
    return numberCurrent root correctRoot
    numberRoot shoud be an integer, not a float!
    """
    correctroot = 1 / numberRoot
    result = pow(numberCurrent, correctroot)
    return result


HELLOMESSAGE_STR = 'I am' + 3 * ' very' + """ happy to see "you" """
print (HELLOMESSAGE_STR)

ASKNUMBER_STR = "please enter a number: "
MENU_STR = """\
Menu:
    +       Addition
    -       Substraction
    *       Multiply
    /       Divide
    rt      n RootASKNUMBER_STR
    x       Power
    hey     gradient descent       
    exit    exit

"""
result_float = 0.0

while True:
    print (MENU_STR)
    uservar = input ()

    #switch does not exist in python
    if(uservar == "+"):
        userNumber_int = int(input(ASKNUMBER_STR))
        result_float = add(result_float, userNumber_int)

    elif(uservar == "-"):
        userNumber_int = int(input(ASKNUMBER_STR))
        result_float = sub(result_float, userNumber_int)

    elif(uservar == "*"):
        userNumber_int = int(input(ASKNUMBER_STR))
        result_float = mult(result_float, userNumber_int)

    elif(uservar == "/"):
        userNumber_int = int(input(ASKNUMBER_STR))
        result_float = div(result_float, userNumber_int)

    elif(uservar == "rt"):
        userNumber_int = int(input(ASKNUMBER_STR))
        result_float = root(result_float, userNumber_int)

    elif(uservar == "x"):
        userNumber_int = int(input(ASKNUMBER_STR))
        result_float = power(result_float, userNumber_int)

    elif(uservar == "hey"):
        result_float = 1
        
    elif(uservar == "exit"):
        break