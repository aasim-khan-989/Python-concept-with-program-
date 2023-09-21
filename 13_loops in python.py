""" Loop in python are used to execute the statement until the value become false  """


#                              ''' While loop '''

# infinite loop

# i=0
# while i<10:
#     print(i)

# finite loop

# a=10
# while a>=0:
#     print(a)
#     a-=2

# example

# a = [1, 2, 3, 4, 5,19,21,20]
# i=0
# while i<len(a):
#     print(a[i])
#     i+=2

# i = 0
# sum=0
# while i<len(a):
#     sum+=(a[i])
#     i+=1
# print('sum of all the element of list are',sum)

# l=[11,12,12,11,12,13,1,1,2,12,18] ???
# nl=[]
# i=0
# j=0
# while i<len(l):
#     while j<len(nl):
#         if(l[i]==nl[j]):


#                                                   ''' For loop '''

# syntax
# L = [1, 2, 3, 4]
# for a in L:
#     print(a)
#
# str = "mango"
#
# for x in str:
#     print(x)

#                                                    range function

# note 0 is starting point ,11 will be n+1 number if we have to print n numbers abd 2 is step size

# for i in range(0, 11, 2):
#     print(i)
#
# for i in range (11): # note i=o increment =1 are default values
#     print(i)

#                                                for loop with else
#
# l=[1,7,8]
# for i in l:
#     print(i)
# else:
#     print('else will execute when loop will exhaust')

#                                         Break statement

# break is used to come out the loop when there the condition become true

# l=[1,7,8]
# for i in l:
#     print(i)
#     if i==7:
#         break
# else:
#     print('else will execute when loop will exhaust')
# note else will only execute when the loop is successfully executed and not when the loop is exhaust due to break
#
# for i in range(0,11,1):
#     if(i%2==0):
#         print(i)
#         if i==8:
#             break


#                                   continue statement

#  note continue statement skipp the next statement when the condition is true and only for that point

# for i in range(0,11,1):
#     if(i%2==0):
#         print(i)
#         if i==8:
#             continue

# for i in range(0,11,1):
#     if(i%2==0):
#         if i == 8:
#             continue
#         print(i)
# else:
#     print("else will execute when using continue statement ")

#                                 pass statement

# for i in range(0, 11, 1):  # note it is just a null statement without pass code will throw an error
#     pass


# examples


# list=["apple",'mango','banana','grapes']

# print the fruits present on even index of list using while loop

# i=0
# while i<len(list):
#     if(i%2!=0):
#         print(list[i])
#     i+=1

# print the fruits present on even index of list using for loop

# for i in range(1,len(list),2):
#     print(list[i])


num=[0,2,33,44,66,88,10,1]

# print the number which are even in list using while loop

# i=0
# while i<len(num):
#     if(num[i]%2==0):
#         print(num[i])
#     i+=1

# print the number which are even in list using for loop

# for i in range(0,len(num)):
#     if num[i]%2==0:
#         print(num[i])

























