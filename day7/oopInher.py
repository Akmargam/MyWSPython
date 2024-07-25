class Book:
    def __init__(self,author,book,price):#constructor
        self.author=author
        self.book=book
        self.__price=price
        self.__discount=None #__ makes it private(Encapsulation)
        
        
'''  def __repr__(self):#
        return f"Author: {self.author}, Book: {self.book},{self.__price}"
    
    #setting a variable
    def setDiscount(self,discount):
        self.__discount=discount

    def getPrice(self):
        if self.__discount:
            return self.__price*((100-self.__discount)/100)
        return self.__price '''

class Novel(Book):
    def __init__(self, author, book, price,genre):
        super().__init__(author, book, price)#parent class is called
        self.genre=genre

class Academic(Book):
    def __init__(self, author, book, price,subject):
        super().__init__(author, book, price)
        self.subject=subject
        
novel1=("MK","h22",200,"fic")
novel1=("AK","Joo",100,"Py")