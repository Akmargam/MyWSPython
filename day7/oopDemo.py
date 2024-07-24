class Book:
    def __init__(self,author,book,price):#constructor
        self.author=author
        self.book=book
        self.price=price
        
        
    def __repr__(self):#
        return f"Author: {self.author}, Book: {self.book}, Price: {self.price}"
        
book1=Book("CB","2s","100")
print(book1.author)
print(book1)