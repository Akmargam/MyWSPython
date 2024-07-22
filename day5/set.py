#Intro to set
# no duplicates
# print(type(s1))
# print(len(s1))
# list1=[1,2,3,4,5,6,7,8,1,1,12,2,2,3,3,3,4,5,6,7,8,9]
# set1=set(list1)
# print(set1)
s1={1,2,3,5,6,3}
s2={4,2,6,4,8,9,1,5}
#union
# print(s1|s2)
# print(s1.union(s2))
#intersection
# print(s1&s2)
# print(s1.intersection(s2))
#not ordered
#not indexed
s1.remove(3)
print(s1)
list1=[0,4,8,3,8]
s1.update(list1)
print(s1)