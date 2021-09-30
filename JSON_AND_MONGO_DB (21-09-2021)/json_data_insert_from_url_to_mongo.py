# PROGRAM        : PROGRAM TO DEMONSTRATE INSERTING DATA FROM URL TO JSON FILE && URL TO MONGODB
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 20-SEP-2021 
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 
from pymongo import MongoClient 
import json 
import requests 
class Mongo_demo:
    connection=MongoClient("mongodb://localhost:27017")
    def create_json(self,data):
        with open("breed_json.json","a+") as file:
            json.dump(data,file)
            file.write("\n")
            file.write("\n")
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
url="https://api.thedogapi.com/v1/breeds"
t=j.read_data(url)
j.create_json(t)
print(j.mongo_conn())
print(j.create_collect("chubb_test","Breeds11"))
d={}

# INSERTING ALL THE DOCUMENTS FROM JSON TO MONGO DB ( BREEDS11  COLLECTION)
j.insert_many_rec("chubb_test","Breeds11",t)


'''
for i in t:
    #print(i)
    #j.insert_many_rec("chubb_test","Breeds2",t)
    d={"Breed ":i['name'],"Country ":i["origin"],"Breed for ":i["bred_for"],"Image :":i['image']['url']} 
    j.insert("chubb_test","Breeds2",d)'''


