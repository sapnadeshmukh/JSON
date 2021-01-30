import json
data={"name": "David",
     "class":"I",
     "age": 6  
 }
with open("python_json.json","w") as file:
    json.dump(data,file)

