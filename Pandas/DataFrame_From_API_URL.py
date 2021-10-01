# PROGRAM        : CREATING DATAFRAME FROM URL ( API )
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 01-10-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 


import pandas as pd
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
d={}

# Checking If Url Exists 

if(j.check(url)):
    # Reading Data from Url 
    t=j.read_data(url)    
    id,bred_for,name,img_url=[],[],[],[]
    id1,bred_for1,name1,img_url1,orgin=[],[],[],[],[]
    for i in t:
        # Inserting The Data Where Both Breed Group and Url and id and name  If Exists For that Breed
        if("breed_group" in i and 'image' in i and 'url' in i['image']):
            id.append(i['id'])
            name.append(i['name'])
            bred_for.append(i['breed_group'])
            img_url.append(i['image']['url'])
        # Inserting ALL the values of the JSON 
        if("id" in i and "name" in i ):
            id1.append(i['id'])
            name1.append(i['name'])
        else:
            id1.append("-NONE-")
            name1.append("-NONE-")
        if("origin" in i ):
            orgin.append(i['origin'])
        else:
            orgin.append("-NONE-")
        if("bred_for" in i ):
            bred_for1.append(i['bred_for'])
        else:
            bred_for1.append("-NONE-")
        if("image" in i and 'url' in i['image'] ):
            img_url1.append(i['image']['url'])
        else:
            img_url1.append("-NONE-")


else:
    print(" URL DOESNT EXIST")
url="https://api.thedogapi.com/v1/breeds"
#df=pd.DataFrame()
#print(pd.read_json(json.dumps(j)))
dic1={"id":id,"Name":name,"Bred_for":bred_for,"Image_Url":img_url}
dic2={"id":id1,"Name":name1,"Bred_for":bred_for1,"Origin":orgin,"Image_Url":img_url1}
df1=pd.DataFrame(dic1)
df2=pd.DataFrame(dic2)
crete_zip = dict(method='zip',archive_name='Breeds1.csv')  

df1.to_csv('Test1.zip', index=False,compression=crete_zip)
df2.to_csv('Breeds2.csv')
#df.to_excel('raw_data.xls', index=False)
