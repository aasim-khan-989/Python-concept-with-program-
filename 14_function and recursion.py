''' function is a group of instruction which can be called any time'''

#creating the function
def func1():
    # body of the function
    print("hello world ")
# calling the function
func1()



'''FUNCTION WITH ARGUMENT'''
#example:1

def func2(x): # here x is called a formal argument
    print("hellopython")
func2("x")
# here x is called actual argument

# note this function will definitely take an argument value when it will be called
# note it is not compulsory that argument should be used in the body

# example: 2

def func3(x):
    print(len(x))

# passing a str
func3("zxvbg")
# passing a list
func3([33,45,67])
# passing a variable or identifier
a="dfdxf65786578"
func3(a)

# example:3
def greet(name,sirname):
    print('happy birthday '+name, sirname)
greet("aasim", "khan")
greet("basit", "shaikh")

# note if we not pass a value of the argument then it will generate an error

'''types of argument'''

# 01 positional argument-The value changes as we change the oder of the arguments
#
# def power(x ,y):
#     print(x**y)
#
# power(2,3)
# power(3, 2)

# 02 keyword argument-A keyword argument is followed by an equal sign and an expression that gives its default value.

# note oder does not make difference

# def pw(x,y):
#     print(x**y)
# pw(x=2,y=3)
# pw(y=3, x=2)

# 03  default argument in Python functions are those arguments
# that take default values if no explicit values are passed to these arguments from the function call.

# def sum(x=2,y=3):
#     print(x+y)
#
# sum(8,10)
# sum()
# def mul(x,y=8):
#     print(x*y)
# mul(3)
# mul(3, 2)
# mul(x=3)

# 04 variable length argument - Any number of positional arguments (*args) all the argument will store in tuple
#
# def sum(*num):
#     ans = 0
#     for i in num:
#         ans=ans+i
#     print(ans)
# sum(1,2,3,4)
''' imp question
n = int(input('enter the number of element '))
list = []
for i in range(1, n + 1):
    x = int(input(f"enter the {i} element "))
    list.append(x)
def sum(*args):
    ans=0
    for i in args:
        ans=ans+i
    print(ans)
sum(*list) '''

# 05 keyword variable length argument - Any number of keyword arguments (**kwargs)

# def myprj(**dic):
#     print(dic)
# myprj(x=3,y=4)

''' 
def myPrg(**kwargs):
    for key, value in kwargs.items():
        print (key, "==" , value)

# Driver code for kwargs in python
myPrg(first ='Hello', mid ='Welcome', last='Hello') '''

# def mul(**kwargs):
#     ans=1
#     for i in kwargs.values():
#         ans=ans*i
#     print(ans)
# mul(a=2,b=3)


''' return key word'''
# it assign value to function
# def fun(a,b):
#     print(a+b)
# g=fun(2,4)
# print(g)
#
# def fun2(x,y):
#     return x+y
#
# a=fun2(2,4)
# print(type(fun2))
# print(a)
#
''' recursion in python'''

def recursive_fact(n):
    if n==1:
        return 1
    else:
        return(n*recursive_fact(n-1))
print(recursive_fact(5))

def recfeb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return recfeb(n-1)+recfeb(n-2)

'''   # printing the bebonachi series..............
def febr(n):
    pnum = 0
    cnum = 1
    print(0,end=' ')
    for i in range(1,n):
        ppnum=pnum
        pnum=cnum
        cnum=pnum+ppnum
        print(cnum,end=' ')
    print('....')
febr(5)  '''

''' special function  '''
# Python Lambda Functions are anonymous function means that the function is without a name.
# A lambda function can take any number of arguments, but can only have one expression.

a = lambda x, y: x+y
print(a(9,67))

x=lambda a:'even number'if a%2==0 else "odd number"
print(x(5))

y=lambda a:print('even')if a%2==0 else print("odd")
y(6)

# filter function

# it returns the iterator where the items are filter through a function

ages=[6,12,19,23,43,56,12]
def adult(x):
    if x<18:
        return False
    else:
        return True
x=(filter(adult,ages))
for i in x:
    print(i)

# filter using lambda

a=[12,33,45,56,67,580]
def func(a):
    if a%2==0:
        return True
    else:
        return False
x=list(filter(func,a))
print(x)


adults=list(filter(lambda x:x%2==0,a))
print(adults)
# map function

data=[1,2,3,4,5,6,7]
x=lambda x:x*x
square=list(map(x,data))
print(square)


# functools

from functools import reduce
def myfunc(a,b):
    return a+b
val=[0,1,2,3]
sum= reduce(myfunc, val)
print(sum)

list=[1,22,34,56,87,90,12,3,4]
max=reduce(lambda x,y:x if x>y else y,list)
print(max)



''' practise question  '''
# a=int(input("enter the number"))
# b=int(input("enter the 2nd number"))
# c=int(input("enter the 2nd number"))
# def func(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# p=(func(a,b))
# def max(z):
#     if z>p:
#         return z
#     else:
#         return p
#
# print(max(c))

def recsum(n):
    if n<=1:
        return 1
    else:
        return(recsum(n-1)+recsum(n-2))
print(recsum(4))

def itrsum(n):
    sum=0
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        for i in range(1,n):
            sum=sum+i
        print(sum, end=' ')
itrsum(4)




















