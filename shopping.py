import json
data={
    "shopping_list":{ "chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",
        } 
}

customer=input("which thing do you want to buy")
del data["shopping_list"][customer]
print(data["shopping_list"])  
customer1=input("enter which item do you want to add")
num_item=input("enter ho many item do you want to buy")
data["shopping_list"][customer1]=num_item
print(data)
with open ("shopping.json","w") as json_data:
    json.dump(data,json_data)

