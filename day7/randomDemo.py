import random
l1=[2,45,77,34,67,334,8,99]
# print(random.choice(l1))

# print(random.random())#returns between 0-1
# print(random.randint(2,20))#returns between given numbers

# random.shuffle(l1)
# print(l1)

random.seed("project2")
print(random.random())
random.seed("project1")
print(random.random())

