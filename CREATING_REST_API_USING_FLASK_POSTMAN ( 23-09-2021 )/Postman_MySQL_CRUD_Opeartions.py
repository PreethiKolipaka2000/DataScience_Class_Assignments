# PROGRAM        : CRETING API USER MODEL (POSTMAN [FRONTEND]  +  MONGO DB [BACK END] ) and PERFORMING CRUD OPERATIONS 
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 24-SEP-2021 
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

from flask import Flask 
from flask import render_template
#from flask import redirect
from flask import url_for 
from flask import request
from flask import jsonify 
from flask_sqlalchemy import SQLAlchemy 


app=Flask(__name__)

# CONFIGURING DATABASE CONNECTIVITY
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:preethi@localhost:3307/guvi"
app.config['SECRET_KEY']='preethi@kzp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


# CREATING A TABLE INSIDE THE GUVI DATABASE
class APIUser(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(20))
    email=db.Column(db.String(20))
    password=db.Column(db.String(20))

#INSERTING DATA TO MYSQL SERVER

@app.route('/write',methods=['POST'])
def write():
    name=request.get_json()["name"]
    email=request.get_json()["email"]
    password=request.get_json()["password"]
    api_user_model=APIUser(name=name,email=email,password=password)
    save_to_database=db.session()
    try:
        save_to_database.add(api_user_model)
        save_to_database.commit()
    except:
        save_to_database.rollback()
        save_to_database.flush()
    return jsonify({"message":"success"})

# FETCH DATA FROM SERVER
@app.route('/',methods=["GET"])
def fetch_all():
    data=APIUser.query.all()
    res=[]
    for i in data:
        res.append({"id":i.id,"name":i.name,"email":i.email,"password":i.password})
    return jsonify(res)

# FETCH DATA BASED ON ID
@app.route('/display/<int:id>',methods=["GET"])
def fetch_by_id(id):
    try:
        data=APIUser.query.filter_by(id=id).first()
        return jsonify({"id":data.id,"name":data.name,"email":data.email,"password":data.password})
    except:
        return jsonify({"message":"error"})

# UPDATE DATA
@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    # update = insert + fetch by id 
    # Fetching the first id details which matches to the given id
    a = APIUser.query.filter_by(id=id).first()
    r1 ={"id":a.id,"name":a.name,"email":a.email,"password":a.password}
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    password=request.get_json()["password"]
    
    #Creating a Session
    save_to_database = db.session
    try:
        # Updating the Values
        api_user_model = APIUser.query.filter_by(id=id).first()
        api_user_model.name = name
        api_user_model.email = email
        api_user_model.password=password 
        save_to_database.commit()
    except:
        return jsonify({"message":"error in updating data"})
        save_to_database.rollback()
        save_to_database.flush()
    id=api_user_model.id
    data=APIUser.query.filter_by(id=id).first()
    # Displaying to Frontend
    return jsonify([r1,{"update":"to"},{"id":data.id, "name":data.name, "email":data.email,"password":data.password}])

# DELETE DATA BY ID 
@app.route('/delete/<int:id>',methods=["DELETE"])
def delete(id):
    try:
        # Creating Session
        save_to_database=db.session
        data=APIUser.query.filter_by(id=id).first()
        # Deleting Data of given Id
        APIUser.query.filter_by(id=id).delete()
        save_to_database.commit()
        return jsonify({"DELETED : ":"DATA "},{"id":data.id,"name":data.name,"email":data.email,"password":data.password})
    except:
        return jsonify({"message":"---- !!!!!  error in deleting data"})
if __name__=="__main__":
    db.create_all()
    app.run(debug=True,port=5000)
