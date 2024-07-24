class Book:
    def __init__(self,author,book,price):#constructor
        self.author=author
        self.book=book
        self.__price=price#__make it a private variable
        
        
    def __repr__(self):#
        return f"Author: {self.author}, Book: {self.book}, Price: {self.price}"
        
book1=Book("CB","2s","100")
print(book1.author)
print(book1.price)
print(book1)