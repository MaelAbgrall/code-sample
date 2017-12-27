#importing a class
from model import *

#importing a module
import calculate
import numbertoascii



#main is considered as a module by python, it is useful to create packages and run tests against it
def main():
    storage = Model()
    print(storage.menuString)
    
    
    firstnumber = float(input("please enter your first number\n"))
    storage.result = firstnumber
    asciiNumber = numbertoascii.convert(firstnumber)
    storage.asciiresult = asciiNumber

    while True:
        
        uservar = input ()

        #switch does not exist in python
        if(uservar == "+"):
            userNumber_int = float(input())
            storage.result = calculate.add(storage.result, userNumber_int)
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(len(str(storage.result)))
            print(storage.asciiresult)

        elif(uservar == "-"):
            userNumber_int = float(input())
            storage.result = calculate.sub(storage.result, userNumber_int)
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(storage.asciiresult)

        elif(uservar == "*"):
            userNumber_int = float(input())
            storage.result = calculate.mult(storage.result, userNumber_int)
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(storage.asciiresult)

        elif(uservar == "/"):
            userNumber_int = float(input())
            storage.result = calculate.div(storage.result, userNumber_int)
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(storage.asciiresult)

        elif(uservar == "rt"):
            userNumber_int = float(input())
            storage.result = calculate.root(storage.result, userNumber_int)
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(storage.asciiresult)

        elif(uservar == "x"):
            userNumber_int = float(input())
            storage.result = calculate.power(storage.result, userNumber_int)
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(storage.asciiresult)

        elif(uservar == "clear"):
            storage.result = 0.0
            storage.asciiresult = numbertoascii.convert(storage.result)
            print(storage.asciiresult)
            
        elif(uservar == "exit"):
            break
        
        else:
            print(storage.warningString)

if __name__ == "__main__":
    main()
