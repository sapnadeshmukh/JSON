import json
numbers={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}


sample_data=dict(sorted(numbers.items()))
dump_data=json.dumps(sample_data,indent=2)
with open("key_sorted.json","w") as openfile:
    openfile.write(dump_data)
    

   