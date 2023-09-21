class parent:
    def func(self):
        print("this is parent classs function")


class child(parent):
    def func2(self):
        print("this is childern class method")


a = child()
a.func()
a.func2()
