1 #integer
1.0 #float 64bit precision
"string"
[1, 2, 3] #list
{1, 2, 3} #tuple

div(10, 2) #return a float
div 10, 2 #return an int
rem 10, 2 #return remainder

a = 1.0e-10 #valid scientific notation

b = false
is_boolean(b) #true

:atom # atom/symbol
:hello == :world #false
#an atom is a const whose name is its own value
#(true and false are atoms)
is_atom(true) #true

Hello #aliases. Start with upper case
is_atom(Hello) #truemax_int