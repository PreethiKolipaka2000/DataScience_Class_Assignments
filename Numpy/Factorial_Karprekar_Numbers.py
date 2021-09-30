# PROGRAM        :  CREATE  A JSON FILE COMPRISING OF NUMPY ARRAYS WHICH CONSISTS OF FACTORIAL 
#                   AND KARPEREKAR NUMBERS  RANGE FROM 1 to 10 and 1 to 1000
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 28-SEP-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

import numpy as np 
import json 
import math 
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

class JSON_API:
    def create_json(self,data):
        with open("task1_karprekar.json","w") as file:
            return json.dump(data,file)
    def read_json(self,file):
        with open(file) as file:
            return json.load(file)

j=JSON_API()

f=[]
k=[]
for x in range(1,10):
    f.append(math.factorial(x))
for x in range(1,10000):
    n=x**2
    s=str(n)
    for i in range(1,len(s)):
        l,r="".join(s[:i]),"".join(s[i:])
        l,r=int(l),int(r)
        if(l+r==x):
            k.append(x)
fact=np.array(f)
print(fact)
kaprekar=np.array(k)
dict_json={"FACTORIAL":fact," KARPREKAR ":kaprekar}

print("-------------SERIALIZING Numpy array To JSON and Writing It to FILE-----------------")
with open("numpy_data.json", "w") as write_file:
    json.dump(dict_json, write_file, cls=NumpyArrayEncoder)

print("-------------DESERIALIZING Converting JSON encoded data into Numpy array-----------------")
with open("numpy_data.json", "r") as read_file:
    decoded_numpy_array = json.load(read_file)
    print(decoded_numpy_array)
