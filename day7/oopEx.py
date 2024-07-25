class Book:
    def __init__(self,author,book,price):#constructor
        self.author=author
        self.book=book
        self.price=price
        self.__discount=None #__ makes it private(Encapsulation)
        
        
    def __repr__(self):#
        return f"Author: {self.author}, Book: {self.book}, Price: {self.price}"

book1=Book("MK","Truth",200)
print(book1)