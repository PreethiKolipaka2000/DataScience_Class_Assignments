
# PROGRAM        : Routing Static And Dynamically Using RENDERING TEMPLATE
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 20-SEP-2021 
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

from flask import Flask 
from flask import render_template
from flask import redirect
from flask import url_for 

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index1.html")
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

'''
def index():
    return "-----Welcome to Python Track------"
@app.route('/preethi')
def preethi():
    return "Welcome to Preethi"

#Route Dynamically
@app.route('/author/<name>')
def author(name):
    return("The author of the web page is ",name)
'''
if __name__=="__main__":
    app.run(debug=True,port=5000)
