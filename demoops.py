class Book:
    category = "it"

    def __init__(self, name, price, author):
        self.name = name
        self.price = price
        self.author = author

    def cp(self):
        print(self.name)
        self.price = 10


caters = Book("a",3,"b")

caters.cp()
print(caters.price)
