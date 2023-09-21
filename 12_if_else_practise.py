''''' w.r.t a program to find the greatest of two number from user '''

# a=int(input('enter number '))
# b=int(input('enter number '))
#
# if(a>b):
#     print('the greater number is',a)
# elif(a==b):
#     print('both number are equal')
# else:
#     print('the greater number is second',b)


'''  w.r.t a program to find the greatest among  3 number from user '''

# x = int(input('enter the number '))
# y = int(input('enter the number '))
# z = int(input('enter the number '))
#
# if(x>y>z):
#     print('x the greatest is',x)
# elif (x>z>y):
#     print('x the greatest is',x)
# elif(x>y==z):
#     print(x,'is greater and ',y,z,'are equal')
# elif(y>z>x):
#     print('y the greatest ',y)
# elif(y>x>z):
#     print('y is greatest', y)
# elif(y>x==z):
#     print(x,'is greater',y,z,'are same')
# elif(z>x>y):
#     print('z is greatest',z)
# elif(z>x==y):
#     print(z, 'is greater', x, z, 'are same')
# elif(z>y>x):
#     print('z is greatest',z)
# elif(x<y==z):
#      print(y,z,'are same and both are greater')
# elif(y<x==z):
#      print(x,z,'are same and both are greater')
# elif(z<x==y):
#      print(y,x,'are same and both are greater')
# else:
#     print(x,y,z,'all the number are equal')



'''  w.r.t a program to find the greatest among  4 number taken from user '''

#
# a = int(input('enter the number '))
# b = int(input('enter the number '))
# c = int(input('enter the number '))
# d = int(input('enter the number '))
#
# if(a>b):
#     x=a
# else:
#     x=b
# if(c>d):
#     y=c
# else:
#     y=d
# if(x>y):
#     print(x,' is greatest')
# else:
#     print(y,'is greatest')


''' w.r.t a program to find out student fails or pass if it require 40% total and 33% in each subject'''
#
# m = int(input('enter the marks of  maths  '))
# s = int(input('enter the marks of science '))
# p = int(input('enter the marks of physics  '))
#
# if(m<33 or s<33 or p<33):
#     print('you are fail since your one of the subject marks is less than 33%')
# elif(m+s+p/3<40):
#     print('your total score is less than 40% you are fail ')
# else:
#     print('congragulation you are pass')

'''  w.r.t a program to find whether the name is present in the list '''

# Names = ["aasim","basit","zayed",'ishaq','saeed','anas','siddarth','rohit','shoeb','parth']
# name=input('enter the name you want to check in list\n')
# if(name in Names):
#     print('name is present')
# else:
#     print('name is not present')

''' w.r.t a python program to check wether a word is there or not in comment 
may be it is upper case or not'''

# comment=input('enter the comment \n')
# comment=comment.lower()
# if("harry" in comment):
#     print('spam')
# elif('earn' or 'money' or 'offline' in comment ):
#     print('spam')
# else:
#     print('not spam')

''' w.r.t a program to  print the unit and tens place of 2 digit number '''

# x=int(input('enter the two digit number '))
# print("the unit's place of ", x, 'is', x % 10)
# print("the ten's place of", x, 'is', x //10)   # = print(int(x/10))


''' w.r.t a program to  print the unit and tens place of 3 digit number '''

# x=int(input('enter the 3 digit number\n '))
# # ten's place
# x=x%100
# print("the unit's place  " 'is', x % 10)
# print("the ten's place is", x //10)

''' w.r.t a program to  print the unit  tens , hundred place of 4 digit number '''

# x=int(input('enter the 4 digit number '))
# print('the first digit is',x//1000)
# x=x%1000
# print('the second digit is',x//100)
# x=x%100
# print('the third digit is ',x//10)
# x=x%10
# print('the fourth digit is',x )

''' w.r.t a program to  count the total number of notes in given amount '''

# x = int(input('enter the amount '))
#
# if(x>=2000):
#     if(x%2000==0):
#         print('number of 2000 notes:',x/2000)
#         x=x%2000
#     else:
#         print('number of 2000 notes:',x//2000)
#         x=x%2000
# if(x>=2000):
#     if(x%2000==0):
#         print('number of 200 notes:',x/200)
#         x=x%2000
#     else:
#         print('number of 200 notes:',x//200)
#         x=x%200
# if(x>=500):
#     if(x%500==0):
#         print('number of 500 notes:',x/500)
#         x=x%500
#     else:
#         print('number of 500 notes:',x//500)
#         x=x%500
# if(x>=100):
#     if(x%100==0):
#         print('number of 100 notes:',x/100)
#         x=x%100
#     else:
#         print('number of 100 notes:',x//100)
#         x=x%100
# if(x>=50):
#     if(x%50==0):
#         print('number of 50 notes:',x/50)
#         x=x%50
#     else:
#         print('number of 50 notes:',x//50)
#         x=x%50
# if(x>=20):
#     if(x%20==0):
#         print('number of 20 notes:',x/20)
#         x=x%20
#     else:
#         print('number of 20 notes:',x//20)
#         x=x%20
# if(x>=10):
#     if(x%10==0):
#         print('number of 10 notes:',x/10)
#         x=x%10
#     else:
#         print('number of 10 notes:',x//10)
#         x=x%10
# if(x>=5):
#     if(x%5==0):
#         print('number of 5 coin :',x/5)
#         x=x%5
#     else:
#         print('number of 5 coin :',x//5)
#         x=x%5
# if(x>=2):
#     if(x%2==0):
#         print('number of 2 coin:',x/2)
#         x=x%2
#     else:
#         print('number of 2 coin:',x//2)789069
#         x=x%2
# if(x == 1):
#         print('number of 1 coin :',x//1


'''
x = int(input('enter the amount '))
total=0
if(x>=2000):
    if(x%2000==0):
        print('number of 2000 notes:',x/2000)
        total = x // 2000
        x=x%2000
        print('total currency required',total)
    else:
        print('number of 2000 notes:',x//2000)
        total=x//2000
        x=x%2000

if(x>=500):
    if(x%500==0):
        print('number of 500 notes:',x/500)
        total+=x//500
        x = x % 500
        print('total currency required', total)
    else:
        print('number of 500 notes:',x//500)
        total += x // 500
        x=x%500
if(x>=200):
    if(x%200==0):
        print('number of 200 notes:',x/200,)
        total+=x//200
        x=x%200
        print('total currency required', total)
    else:
        print('number of 200 notes:',x//200)
        total+=x//200
        x=x%200


if(x>=100):
    if(x%100==0):
        print('number of 100 notes:',x/100)
        total+=x//100
        x=x%100

        print('total currency required', total)
    else:
        print('number of 100 notes:',x//100)
        total+=x//100
        x=x%100

if(x>=50):
    if(x%50==0):
        print('number of 50 notes:',x/50)
        total+=x//50
        x=x%50

        print('total currency required', total)
    else:
        print('number of 50 notes:',x//50)
        total+=x//50
        x=x%50

if(x>=20):
    if(x%20==0):
        print('number of 20 notes:',x/20)
        total+=x//20
        x=x%20

        print('total currency required', total)
    else:
        print('number of 20 notes:',x//20)
        total+=x//20
        x=x%20

if(x>=10):
    if(x%10==0):
        print('number of 10 notes:',x//10)
        total+=x//10
        x=x%10

        print('total currency required', total)
    else:
        print('number of 10 notes:',x//10)
        total+=x//10
        x=x%10

if(x>=5):
    if(x%5==0):
        print('number of 5 coin :',x//5)
        total+=x//5
        x=x%5

        print('total currency required', total)
    else:
        print('number of 5 coin :',x//5)
        total+=x//5
        x=x%5
if(x>=2):
    if(x%2==0):
        print('number of 2 coin:',x//2)
        total+=x//2
        x=x%2

        print('total currency required', total)
    else:
        print('number of 2 coin:',x//2)
        total+=x//2
        x=x%2

if(x == 1):
        print('number of 1 coin :',x//1)
        total+=x//1
        print('total currency reuired is:',total)"  
        
        '''















