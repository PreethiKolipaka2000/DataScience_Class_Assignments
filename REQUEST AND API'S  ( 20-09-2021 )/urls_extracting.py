# PROGRAM        : FETCHING Data(URL,BreedGroup) FROM URL  
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 20-SEP-2021  ( DAY -3 )
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

import requests 
import json 
import urllib 

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
d={}

# Checking If Url Exists 
if(j.check(url)):
    # Reading Data from Url 
    t=j.read_data(url)    
    for i in t:
        # Inserting The Data Where Both Breed Group and Url If Exists For that Breed
        if("breed_group" in i and 'image' in i):
            d[i['breed_group']]=i['image']['url']
    for k , v in d.items():
        print(k, " : ",v)
else:
    print(" URL DOESNT EXIST")