import json


# with open("/Users/arunkumarmargam/Desktop/MyWSPython/day6/person.json",'r') as fp:
#     # data =fp.read()#retuns string
#     data=json.load(fp)#returns dictionary
# print(data)

# write operation

# citizen ={
#     "name":"Peter",
#     "Profession":"Hotelier",
#     "Cars":["RAM","VV","MB"]
# }
# with open("person.json",'w') as fp:
#     json.dump(citizen,fp)

# append

citizen ={
    "Profession":"Manager",
    "Cars":"Audi"
}
with open("person.json",'a') as fp:
    fp.write('/n')
    json.dump(citizen,fp)

# with open("/Users/arunkumarmargam/Desktop/MyWSPython/person.json",'r') as fp:
#     data=json.load(fp)
# print(data)