import json 
from flask import Flask , render_template 

# THE CREATED FILE IS USED TO DISPLAY THE JSON FILE TO HTML FORMAT

headings=["Name","Country","Bred_For","Image"]
app=Flask(__name__)
class T:
    def read_json(self,file):
        with open(file) as file:
            return json.load(file)

t=T()
r=t.read_json("test2.json")
data=[]
# DETCHING DATA FROM TEST2.JSON AND RENDERING TO HTML FORMAT WITH THE REQUIRED HEADINGS
for i in r:
    #f={"name":i["name"],"origin":i["origin"],"bred_for":i["bred_for"],"image_url":i["image_url"]}
    data.append([[i['name'],i['origin'],i['bred_for']],i['image_url']])
    #data.append(f)


@app.route("/")
def table():
    return render_template("table1.html",headings=headings,data=data)
app.run(debug=True,port=5000)