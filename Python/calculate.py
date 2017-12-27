def add(numberCurrent, numberAdd):
    """add docstring:
    return numberCurrent plus numberAdd
    """
    return float(numberCurrent + numberAdd)

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