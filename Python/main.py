#int i_int = 2


def my_function (number_int, max_int):
    i = 0
    while i < 10:
        print "hello"
        i = i + 1


hellomessage_str = 'I am' + 3 * ' very' + """ happy to see "you" """

print hellomessage_str

menu_str = """\
Menu:
    1.      Addition
    2.      Substraction
    3.      Multiply
    4.      Divide
"""

print menu_str

"""
if mystring and myvariable:
    print "type is " + str(type(myvariable)) #give the type of the variable
"""
uservar = input("write a number")
uservar = int(uservar) #cast

print type(uservar)

"""
for mycharacter in mystring: #for loop in pyt hon are like foreach in c#/java/pearl
    print mycharacter
"""
for x in range(0, 3):
    print "We're on time %d" % (x)