num1=int(input("enter a number"))
try:
    numb2=100/num1
    print(numb2)
except ZeroDivisionError:
    print("can't divide")
