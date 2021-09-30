# PROJECT WEEK 1 : 
from pymongo import MongoClient 
from json2html import *
import json 
from flask import Flask , render_template 
import json2table
import requests 
class Mongo_demo:
    connection=MongoClient("mongodb://localhost:27017")
    def create_json(self,f,data):
        with open(f,"a+") as file:
            json.dump(data,file)
            return 
    def read_json(self,file):
        with open(file) as file:
            return json.load(file)
    def check(self,url):
        try:
            url=requests.get(url)
            return True 
        except:
            return False
    def mongo_conn(self):
        if(self.connection):
            return True 
        return False 
    def read_data(self,url):
        if(self.check(url)):
            url=requests.get(url)
            return url.json()
        else:
            return "URL DOESN'T EXIST"
    def mongodb_list(self):
        if(self.mongo_conn()):
            return self.connection.list_database_names()
    def db_exists(self,db):
        if(db in self.mongodb_list()):
            return True 
        return False 
    def create_collect(self,db,new_coll):
        if(self.connection):
            db=self.connection[db]
            new_coll=db[new_coll]
            return new_coll
        else:
            return "CONNECTION FAILED"
    def insert(self,db,coll,data):
        if(self.connection):
            self.connection[db][coll].insert_one(data)
            return "SUCCEDDED TO INSERT DATA"
        else:
            return "FAILED TO GET INSERTED"
    def disp(self,db,coll):
        res=[]
        if(self.connection):
            for d in self.connection[db][coll].find():
                res.append(d)
            for dict_ in res:
                for k,v in dict_.items():
                    print(k ," : ",v)
        else:
            print("Connection Failed")
    def insert_many_rec(self,db,coll,r):
        c=0
        if(self.connection):
            for dict_  in r:
                self.insert(db,coll,dict_)
                c+=1
            print("INSERTED  ",c)
        else:
            print("CONNECTION FAILED")




j=Mongo_demo()


# URL FOR DOG BREEDS DATA 
url="https://api.thedogapi.com/v1/breeds"

# READING DATA FROM URL AND CREATING A JSON FILE AND INSERTING ENTIRE API DATA INTO IT 

t=j.read_data(url)
j.create_json("Breed_Data.json",t)

# CREATING A COLLECTION BREEDS_PROJECT1 TO STORE NECESSARY DETAILS REQUIRED IN MONGO DB

print(j.mongo_conn())
print(j.create_collect("chubb_test","Breeds_Project1"))


d=[]
d1=[]

# READING THE DATA FROM CREATED JSON FILE NAMED BREED_DATA

r=j.read_json("Breed_Data.json")
for i in r:
    f={}
    # TAKING THE REQUIRED ATTRIBUTES NEEDED TO STORE AND INITIALIZING 
    name,bredfor,orgin,img_url=" - "," - "," - "," - "
    if 'name' in i:
        name=i['name']
    if 'origin' in i:
        orgin=i['origin']
    if 'bred_for' in i:
        bredfor=i['bred_for']
    if 'image' in i and 'url' in i['image']:
        img_url=i['image']['url']
    f={"name":name,"origin":orgin,"bred_for":bredfor,"image_url":img_url}

    d.append(f)
    #d1.append([name,orgin,bredfor,img_url])
    
    # INSERTED THE SAME DATA TO TO MONGO DB 
    j.insert("chubb_test","Breeds_Project1",f)

# INSERTING THE REQUIRED  PARAMETERS INTO ANOTHER JSON NAMED TEST2
j.create_json("test2.json",d)


