# tokens in python

# tokens are the smallest individual unit of a python program

# there are 5 types of token
# 1st keywords
# 2nd identifiers
# 3rd literals
# 4th operator
# 5th punctuator

# keywords

# keywords are the reserved words which have some meaning
# importing "keyword" for keyword operations
import keyword
# printing all keywords at once using "kwlist()"
print(keyword.kwlist)

# identifier

# identifier is a name used to identify a variable,class,object,function,module

# rules for writing the name of identifier i.e variable,class,object,function,module

# A name must start with a letter or the underscore character.
# A name cannot start with a number.
# A name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# names are case-sensitive (name, Name and NAME are three different variables).
# The reserved words(keywords) cannot be used  for naming

# literals

# literals are the raw data given in a variable or constant

# there are 5 type of literals

# 01 numeric
# o2 string
# 03 boolean
# 04 special literal (none)
# 05 literal collection (list,tuple,dictionary and set)

# to know the type we used type() function

x=[1,2,3]
print(type(x))

# operator
# Operators are used to perform operations on variables and values.
# Python divides the operators in the following groups:
#
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
#
# arithmatic operator
# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y
# /	Division	x / y
# %	Modulus	x % y
# **	Exponentiation	x ** y
# //	Floor division	x // y

# for example
x=100
print(x%10)
print(x//3)

# comparison operator

# These operators compare the values on either sides of them and decide
# the relation among them. They are also called Relational operators

# == If the values of two operands are equal, then the condition becomes true
# != If values of two operands are not equal, then condition becomes true.
# <> If values of two operands are not equal, then condition becomes true
# >  If the value of left operand is greater than the value of right operand, then condition
# <	 If the value of left operand is less than the value of right operand, then condition becomes true.
# >= If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
# <= If the value of left operand is less than or equal to the value of right operand, then condition becomes true.

# for example
p=13
q=14
print(p>q,p<q,p==q)

# assignment operator

# Assignment operators are used to assign values to variables:

# Operator	Example	Same As
# =	x = 5	x = 5
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3

# for example

a = 10
b = 5;

a += b  # same as a=a+b
print("value of a+b = ", a)  # a will hold the result

# logical operator
# Logical operators are used to combine conditional statements:

# Operator	Description                                     Example
# and 	   Returns True if both statements are true	        x < 5 and  x < 10
# or	   Returns True if one of the statements is true	x < 5 or x < 4
# not	  the result, returns False if the result is true	not(x < 5 and x < 10)

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

# Identity operator
# Identity operators are used to compare the objects,
# not if they are equal, but if they are actually the same object, with the same memory location:


# Operator	Description	Example	Try it
# is 	Returns true if both variables are the same object	x is y
# is not	Returns true if both variables are not the same object	x is not y


# The Equality operator (==) is a comparison operator in Python that compare values of both the operands
# and checks for value equality. Whereas the ‘is’ operator is the  identity operator
# that checks whether both the operands refer to the same object or not (present in the same memory location).

# python3 code to
# illustrate the
# difference between
# == and is operator
# [] is an empty list
list1 = []
list2 = []
list3 = list1

if (list1 == list2):
    print("True")
else:
    print("False")

if (list1 is list2):
    print("True")
else:
    print("False")

if (list1 is list3):
    print("True")
else:
    print("False")

list3 = list3 + list2

if (list1 is list3):
    print("True")
else:
    print("False")

# membership operator

# in  Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object x not in y

# bitwise operator
#
# &	Bitwise AND	x & y
# |	Bitwise OR	x | y
# ~	Bitwise NOT	~x
# ^	Bitwise XOR	x ^ y
# >>	Bitwise right shift	x>>
# <<	Bitwise left shift	x<<

# a = 10 = 1010 (Binary)
# b = 4 =  0100 (Binary)
#
# a & b = 1010
#          &
#         0100
#       = 0000
#       = 0 (Decimal)

# These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by two respectively.
# They can be used when we have to multiply or divide a number by two.
# Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a negative number)
# as a result. Similar effect as of dividing the number with some power of two.

# Example:
#
# Example 1:
# a = 10 = 0000 1010 (Binary)
# a >> 1 = 0000 0101 = 5
#
# Example 2:
# a = -10 = 1111 0110 (Binary)
# a >> 1 = 1111 1011 = -5
# Bitwise left shift: Shifts the bits of the number to the left and fills 0 on voids right as a result. Similar effect as of multiplying the number with some power of two.
# Example:
#
# Example 1:
# a = 5 = 0000 0101 (Binary)
# a << 1 = 0000 1010 = 10
# a << 2 = 0001 0100 = 20
#
# Example 2:
# b = -10 = 1111 0110 (Binary)
# b << 1 = 1110 1100 = -20
# b << 2 = 1101 1000 = -40

