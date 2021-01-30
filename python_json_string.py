import json

student={"name":"sapna",
        "age":23,
        "college":"navgurukul"}
data=json.dumps(student)
print(type(data))
