from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://durgaprasad007y_db_user:Prasad@cluster0.jzwjc5z.mongodb.net/")
db = client["MastanIT"]     #databse name
collection = db["emplyee"]  #collection name


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/registration")
def home1():
    return render_template("registration.html")

@app.route("/register", methods=["POST"])
def register1():
    email = request.form["email"]
    password = request.form["password"]

    existing_user = collection.find({"email":email})

    if existing_user:
        return render_template('registration.html',message="Registration already done!....")
    else:
        collection.insert_one({
                "email":email,
                "password":password
        })
        return render_template("registration.html", message="Details Submited successfully...")



if __name__ == "__main__":
    app.run()