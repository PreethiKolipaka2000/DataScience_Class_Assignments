
# PROGRAM        : QUERYING MONGO DB COLLECTIONS USING PY MONGO
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 20-SEP-2021 
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

from pymongo import MongoClient 
import json 
import requests 

class Test:
    connection=MongoClient("mongodb://localhost:27017")
    def mongo_conn(self):
        if(self.connection):
            return True 
        return False 
    def read_json(self,file):
        with open(file) as file:
            return json.load(file)
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
    def query(self,db,coll):
        res=[]
        if(self.connection):
            # QUERYING THE COLLECTION
            #cursor = self.connection[db][coll].find({"salary":{"$gt":30000}})
            cursor = self.connection[db][coll].aggregate([ {'$match': {'mgr': {'$exists': True}}}, {'$sort': {'deptno': 1}}, {'$limit': 4}])
            # EXECUTING THE QUERY
            for d in cursor:
                for k,v in d.items():
                    print(k," : ",v)
                print("---------------------------------------------------------")
            '''for dict_ in res:
                for k,v in dict_.items():
                    print(k ," : ",v)'''
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

m=Test()
# Establishing The Connection
print(m.mongo_conn())
# Displaying All the List Of Databases
print(m.mongodb_list()) 
# Quering EMPLOYEE COLLECTION 
m.query("chubb_test","emp")