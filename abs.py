# from abc import ABC,abstractmethod
#
# class A(ABC):
#     def func(self):
#         pass
# class B(A):
# #     def func(self):
#         print("this is abstract method")
#
#
x =10

try:
    y=x/0
except Exception as e:
    print(e)
else:
    print(y)
finally:
    print("thanlss")
class myexp(Exception):
    pass

def fune():
    balance = 1000
    withdraw = int(input("enter the number"))
    if(balance<withdraw):
        raise myexp("insufficent balance")
fune()
