import json


with open("/Users/arunkumarmargam/Desktop/MyWSPython/day6/person.json",'r') as fp:
    # data =fp.read()#retuns string
    data=json.load(fp)#returns dictionary
print(data)