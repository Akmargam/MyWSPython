class Book:
    def __init__(self,author,book,price,discount):#constructor
        self.author=author
        self.book=book
        self.price=price
        self.discount=discount
        
        
    def __repr__(self):#
        return f"Author: {self.author}, Book: {self.book}, Price: {self.price}, Dis: {self.discount}"

book1=Book("MK","Truth",200,30)
print(book1)