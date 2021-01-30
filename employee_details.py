import json
office={
    "emp1":{
        "name":"neelam",
        "designation":"programer",
        "age":23,
        "salary" :2400},
    "emp2 ":{
        "name":"komal",
        "designation":"trainer",
        "age":24,
        "salary" :20000},
    "emp3":{
        "name":"anuradha",
        "designation":"HR",
        "age":True,
        "salary" :40000},
    "emp4":{
        "name":"abhishek",
        "designation":"manager",
        "age":29,
        "salary" :63000},
    "emp5":{
        "name":"SAPNA DESHMUKH",
        "designation":"senior software engineer",
        "age":23,
        "isBf": False

    }

}

with open("employee_details.json","w")as f:
    json.dump(office,f,indent=4)
