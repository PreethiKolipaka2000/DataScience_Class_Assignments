# PROGRAM        : CREATE AND READING JSON DATA USING PYTHON
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 20-SEP-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

import requests 
import json 
data={
    "Name":"Kolipaka Preethi",
    "Rollno":"B18CS148",
    "Branch":"CSE",
    "College":"KITSW"
}
class JSON_API:
    def create_json(self,data):
        with open("test.json","w") as file:
            return json.dump(data,file)
    def read_json(self,file):
        with open(file) as file:
            return json.load(file)

j=JSON_API()
j.create_json(data)
print(j.read_json("test.json"))