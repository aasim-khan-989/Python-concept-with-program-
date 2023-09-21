# variable

# variable in python are the temporary storage space for data or values
student='john,rohan'
# here student is variable name and john and rohan are values
print(student)

# rules for writing variable name
# A variable name must start with a letter or the underscore character.
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
# Variable names are case-sensitive (name, Name and NAME are three different variables).
# The reserved words(keywords) cannot be used naming the variable.

# assigning single value to variable
x=y=z=1
print(x,y,z)
# assigning multiple values to variable
x,y,z=1,2,3
print(x,y,z)

# every variable is associate with data type to know the data type,type() function is used
print(type(x))
x='''aasim
khan'''# note multi line string is stored in triple quotes
print(x)

# type casting

abc=100
print(hex(100))
print(float(abc))

# input function

a = int(input('enter the first number :'))
b = int(input('enter the second number :'))
avg = (a+b)/2
print('avg is :' , avg)







