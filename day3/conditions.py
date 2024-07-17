# a=int(input("Enter a number"))
# if(a<0):
#     print("It's a negative number")
# elif(a==0):

#     print("it's a zero")
# else:
#     print("It's a positive number")

# a=int(input("Enter a number"))
# if(a%2==0):
#     print("It's an even number")
# elif(a==0):

#     print("it's a zero")
# else:
#     print("It's an odd number")

while True:
    marks=int(input("Enter your marks"))
    if marks>90:
        print("Your grade is A")
    elif 80<=marks<90:
        print("Your grade is B")
    elif 60<=marks<=80:
        print("Your grade is C")
    else:
        print("Your grade is D")