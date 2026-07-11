from flask import Flask, request
import requests

app = Flask(__name__)
users = (url:="https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=YOUR_API_KEY")

@app.route("/users",methods=["GET"])
def get_users():
   response = requests.get(users[0])
   return response.json()

app.run(debug=True)