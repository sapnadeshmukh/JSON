import json
data1='{"a":  1,"a":  2,"a":  3, "a": 4,   "b": 1, "b": 2}'
data=json.loads(data1)
print(data)
print(type(data))

with open("unique.json","w" ) as openfile:
    json.dump(data,openfile)

    

   
    
