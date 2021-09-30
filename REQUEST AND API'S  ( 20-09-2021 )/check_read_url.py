# PROGRAM        : READING DATA FROM URL 
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 20-SEP-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

import requests 
import json 

class JSON_API:
    def check(self,url):
        try:
            url=requests.get(url)
            return True 
        except:
            return False
    def read_data(self,url):
        if(self.check(url)):
            url=requests.get(url)
            return url.json()
        else:
            return "URL DOESN'T EXIST"

j=JSON_API()
url="https://api.thedogapi.com/v1/breeds"
t=j.read_data(url)
d={}
for i in t:
    if("id" in i and "breed_group" in i):
        print("ID   :",i["id"])
        print("Name :",i["name"])
        print("Breed Group :",i["breed_group"])
        print("-> IMAGE DATA  ")
        for k,v in i["image"].items():
            print(k," : ",v)
        print("-------------------------------------------------------------------------------------------------------------------------")
    print()
#print(t)