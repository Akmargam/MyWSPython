class Book:
    def __init__(self,author,book,price):#constructor
        self.author=author
        self.book=book
        self.__price=price
        self.__discount=None #__ makes it private(Encapsulation)
        
        
    def __repr__(self):#
        return f"Author: {self.author}, Book: {self.book},{self.__price}"
    
    #setting a variable
    def setDiscount(self,discount):
        self.__discount=discount

    def getPrice(self):
        if self.__discount:
            return self.__price*((100-self.__discount)/100)
        return self.__price
    
book1=Book("MK","Truth",100)
book2=Book("CB","2S",200)
book2.setDiscount(10)
print(book2.getPrice())

print(book1)