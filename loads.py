import json

with open ("loads.json", "r") as f:
    s = f.read()
    json.loads(s)

print(s)
print(type(s))