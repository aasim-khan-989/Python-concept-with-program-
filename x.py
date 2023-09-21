class Enc:
    _a=10 #protected
    __b=11 #private
    p = 199
    def func(self):
        print(self._a)
        print(self.__b)
obj = Enc()

obj.func()
print(obj._a)
# print(obj.__b)
print(obj.p)