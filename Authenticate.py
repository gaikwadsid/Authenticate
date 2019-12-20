# Siddharth Gaikwad
# Software Development Fundamentals
# Authenticate Password 2

import json
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Options.html")


@app.route("/home")
def main():
    option = request.values.get("opt")
    if (option == "1" or option == "Login"):
        return render_template("Login.html")
    if (option == "2" or option == "Create New User Account"):
        return render_template("New_User.html")
    else:
        return render_template("quit.html")




# checks the password for the given username
def database(username, password):
    creditials = dict()
    with open("database.json", "r") as f:
        creditials = json.load(f)
    if (creditials[str(username)] == str(password)):
        return True
    else:
        return False


# Prompt user for the password
# Authenticates the password
@app.route("/login")
def login():
    username = request.values.get("user")
    password = request.values.get("pass")
    if database(username, password) == True:
        return render_template("secretbase.html", user=username)
    else:
        return render_template("wrongpass.html")


# Adds a new username and password to the dictionary
@app.route("/new_user")
def new_user():
    username = request.values.get("user")
    password = request.values.get("pass")
    users = dict()
    with open("database.json", "r") as f:
        users = json.load(f)
        n = 1
        while n > 0:
            if str(username in users) == 'True':
                return render_template("try_again.html", user=username)
            else:
                n = 0
        users[username] = password
        with open("database.json", "w+") as f:
            json.dump(users, f, indent=2)
        f.close()
        return render_template("created.html", user=username)





if __name__ == '__main__':
    app.run()


