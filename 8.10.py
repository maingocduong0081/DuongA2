Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #bai 8.10
>>> n=3
>>> int_num=n
>>> x=4
>>> float_num=x
>>> print("S" = ,(x*x+1)^1)
SyntaxError: invalid syntax
>>> print("S" = (x*x+1)^1)
SyntaxError: keyword can't be an expression
>>> S=(x*x+1)^1
>>> n=3
>>> int_num=n
>>> x=4
>>> float_num=x
SyntaxError: multiple statements found while compiling a single statement
>>> n=3
>>> x=4
>>> A=(x*x+1)^n
>>> print("A = ", A)
A =  18
>>> n=3
int_num=n
>>> x=4
float_num=x
>>> A=(x*x+1)^n
>>> print("A = ", A)
SyntaxError: multiple statements found while compiling a single statement
>>> n=3
>>> x=4
>>> A=(x*x+1)^n
>>> print("A = ", A)
SyntaxError: multiple statements found while compiling a single statement
>>> n=3
>>> int_num=n
>>> x=4
>>> float_num=x
>>> print("A=",A)-``
A= 18
>>> 
