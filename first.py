# "load function"
import json
data=json.load(open("first.json"))
print(type(data))
print(data)

# "dump function"

# data=json.load(open("first.json"))
# a=json.dump(data,open("second.json","w"))
# print(a)
# print(type(a))