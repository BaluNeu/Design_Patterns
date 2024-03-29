class Book:
    def __init__(self, title, author, quantity, price):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.__price = price
        # adding discount attribute
        self.__discount = None
    
    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price
    
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
    
class Novel(Book):
    def __init__(self, title, author, quantity, price, genre):
        super().__init__(title, author, quantity, price)
        self.genre = genre

class Academic(Book):
    def __init__(self, title, author, quantity, price, branch):
        super().__init__(title, author, quantity, price)
        self.branch = branch


    # same function in sub class return different output
    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"

novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)