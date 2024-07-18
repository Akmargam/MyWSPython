# l1=["apple","kiwi","berry","pear"]
# l2=[]
# for ele in l1:
#     if 'a' not in ele:
#         l2.append(ele)
# print(l2)

l1=[1,2,3,4,[3,4,6,8,11],34,55]
l2=[1.1,2.2,3.3,4.4]
l3=l1+l2
l2.extend(l1)
print(l2)
print(l3)