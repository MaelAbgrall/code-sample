
myvariable = 10
mystring = 'a string'
mybigstring = "it's a string"
mysuperstring = """this is a "quote" """

if mystring and myvariable:
    print "type is " + str(type(myvariable)) #give the type of the variable

uservar = input("write something")
uservar = int(uservar) #cast

print type(uservar)

for mycharacter in mystring: #for loop in python are like foreach in c#/java/pearl
    print mycharacter

for x in range(0, 3):
    print "We're on time %d" % (x)