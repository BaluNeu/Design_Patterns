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
    



book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 18, 'Author 2', 220)
book2.set_discount(0.20)
book3 = Book('Book 3', 28, 'Author 3', 320)

# print(book2)

print(book2.get_price())

print(book1)
print(book2)
print(book3)