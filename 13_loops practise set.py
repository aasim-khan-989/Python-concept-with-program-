# 01 write a program to print multiplication table of a given number

# x=int(input('enter the number '))
# i=0
# while i <= 10:
#     print(x, '*', i, '=', x*i)
#     i=i+1
# i+=1
# print(i)
#
# for i in range(0,11,1):
#     print(f"{x}*{i}={x*i}")

# 02 write a program to greet all the person names stored in a list l1 and start with s

# l1 = ['harry', 'sohan', 'sachin', 'rahul','Sara','sana','sama']

# for string in l1:
#     string=string.lower()
#     if string.startswith('s'):
#         print('hello',string)

# string = 0
# while(string <len(l1)):
#     l1[string]=l1[string].lower()
#     if l1[string].startswith('s'):
#         print('hello',l1[string])
#     string+=1

# 03 write a program to find whether the number is composite or prime

# n=int(input('enter the number '))
#
# i = 2
# if(n<=1):
#     print('prime numbers a                  re always integer greater than 1')
# else:
#     while(i<n):
#         if(n%i==0):
#             print('number is composite')
#             break
#         i+=1
#     else:
#         print('number is prime')

# for i in range(2,n):
#     if(n%2==0):
#         print(n,': number is composite')
#         break
# else:
#         print(n,'number is prime')

# prime=True
# for i in range(2,x):
#     if(x%i==0):
#         prime=False
#         break
#     else:
#         prime=True
# if(prime==True):
#     print(f'{x} is prime')
# else:
#     print(f"{x} is composite")

# w.r.t a program to print all prime numbers between two numbers provided by user

# num1 = int(input("Input a number: "))
# num2 = int(input("Input another number: "))

# for x in range(num1,num2):
#     prime = True
#     for i in range(2,x):
#         if (x%i==0):
#             prime = False
#     if prime == True:
#        print(x)
# print("Done......")
# s=0
# for x in range(num1,num2):
#     for i in range(2,x):
#         if(x%i==0):
#             break
#     else:
#         print(x)
#         s=s+x
#
# print(F"sum of all the prime number in the given range is\n{s}")

# write a program to find the sum of first n natural numbers
#
# i = 1
# n = int(input('enter the number '))
# sum = 0
# while(i<=n):
#     sum = sum+i
#     i +=1

# using for loop

# sum = 0
# for i in range(1,n+1):
#     sum = sum+i


# print('sum of the first n natural number is :', sum)

''' STAR PATTERN PROBLEM '''

# for n = 4

# i = 1
# while(i<5):
#     print(i*("*"))
#     i += 1

# for i in range(1,5):
#     print(i*('*'))

# for i in range(1,5):
#     print(i*('*'))

# n=4
#
# for i in range(1,5):
#     print(" "*(n-i),((2*i)-1)*('*'))

# i = 1
# while(i<4):
#     print(" " * (n - i), ((2 * i) - 1) * ('*'))
#     i +=1

# x = int(input('enter the number of rows '))
#
# for i in range(1,x+1):
#     print(' '*(x-i),('*')*((2*i)-1))

# n=3
# for i in range(3):
#     print(' '*(n-(i+1)),end = '')
#     print('x'*((2*i)+1))

# for i in range(1,4):
#     print(3*('*'))

# for i in range(1,4):
#     print('x',end='')
#     for j in range(1,3):
#         print('x')

#square
#
# n=3
# for i in range(3):
#     for j in range(3):
#         print('x',end=' ')
#     print()

# increasing triangle

# n=4
# for i in range(n):
#     for j in range(i+1):
#         print('x',end=' ')
#     print()
# print()

# decreasing triangle
#
# n=4
# for i in range(n):
#     for j in range(i,n):
#         print('x',end=' ')
#     print()

# right sided triangle

# n = 15
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for k in range(i+1):
#         print("*",end=' ')
#     print()

# '''heart shape '''
#
# for row in range(6):
#     for col in range(7):
#         if((row==0 and col%3!=0) or(row==1 and col%3==0) or (row-col==2) or(row+col==8)):
#             print('x',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# hill shape

# n=4
#
# for i in range(n):
#     for j in range(i,n):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('x',end=' ')
#     for j in range(i ):
#             print('x', end=' ')
#     print()

# hollow box

# n=3
# for row in range(3):
#     for col in range(3):
#         if(row==1& col==1):
#             print(' ',end=' ')
#         else:
#             print('x',end=' ')
#     print()

# downward hill
#
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(' ',end='')
#     for j in range(i,n):
#          print('x',end=' ')
#     for j in range(i,n-1):
#          print('x',end=' ')
#     print()




# dimond shape

n=4
#
for i in range(n-1):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i+1):
        print('x',end=' ')
    for j in range(i ):
            print('x', end=' ')
    print()
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
         print('x',end=' ')
    for j in range(i,n-1):
         print('x',end=' ')
    print()
#

# n=int(input('enter the row'))
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))





























