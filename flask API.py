#get (user ke data ko see kar sakte hai)
from operator import index

from flask import Flask
import flask

app = Flask(__name__)

users = ["Aditi", "Rahul", "Priya"]

@app.route("/users")
def get_users():
   return {"users": users}

app.run(debug=True)
 #then go browser and adderse bar mei (http://127.0.0.1:5000/users)
 #result will be {"users": ["Aditi", "Rahul", "Priya"]}

 #post (user ke data ko add kar sakte hai)
from flask import Flask, request

app = Flask(_name_)

users = ["Aditi", "Rahul", "Priya"]

@app.route("/users", methods=["POST"])
def add_user():
    t= request.json["sneha"]
    users.append(t)
    return {"message": "User Added", "users": users}

app.run(debug=True)
# put(new user ke data ko update karne ke liye) <--- old se replace 
from flask import Flask, request
app= flask(__name__)
users = ["Aditi", "Rahul", "Sneha"]

@app.route("/users/<int:index>", methods=["PUT"])

def update_user(index):

    users[0] = request.json["tina"]

    return {"message": "User Updated", "users": users}

app.run(debug=True)

#  delete (user ko delete karne ke liye)
from flask import Flask 

app = Flask(__name__)

users = ["Aditi", "Rahul", "Berry"]

@app.route("/users/<int:index>", methods=["DELETE"])
def delete_user(index):
    users.pop(index)
    return {"message": "User Deleted", "users": users}

app.run(debug=True)

# DELETE http://127.0.0.1:5000/users/2. url mei jao and then click on send button. result will be {"message": "User Deleted", "users": ["Aditi", "Rahul"]}
# and url mei index / karke mention karna hoga ki konsa user delete karna hai. like /users/2 means 2nd index ka user delete hoga.
