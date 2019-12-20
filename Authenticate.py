# Siddharth Gaikwad
# Software Development Fundamentals
# Authenticate Password 2

import json
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("Options.html")


# Run the program
# Calls display_welcome_screen() and authenticate()
'''
    mi = int(request.values.get("mi"))
    km = mi * 1.62137
    km = round(km, 5)
    return render_template("result.html", km=km, mi=mi)
'''
@app.route("/home")
def main():
    option = request.values.get("opt")
    if (option == 1):
        authenticate()
    if (option == "2"):
        return render_template("New_User.html")
    if (option == 3):
        program_exit()


# Displays program title
"""
def display_welcome_screen():
    print("*********************")
    print("Secure System Access")
    print("*********************")
    '\n'
    print("Please slect from the following options: ")
    choice = int(input("1. Login\n2. New User Account\n3. Quit\n>>>"))
    return choice
    """

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
def authenticate():
    print("***************")
    print("Login Info")
    print("***************")
    username = input('Enter username: ')
    n = 3
    while n > 0:
        password = input('Enter your password: ')
        if database(username, password) == True:
            logged_in()
            break
        else:
            print("** Username/Password incorrect. **")
            n = n - 1
    if n == 0:
        print("That was 3 invalid attempts.")
        print("You are locked out of the system.")
        exit()


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
        with open("database.json", "w") as f:
            users = json.dump(users, f, indent=2)
        return render_template("created.html", user=username)



# Exits the program if the user wants to
def program_exit():
    Quit = input('Are you sure you want to exit? (y/n) ')
    if (Quit == 'Y' or Quit == 'y'):
        exit()
    if (Quit == 'N' or Quit == 'n'):
        main()


# Prints the user that the have logged in
def logged_in():
    print("Welcome to the top secret system")


if __name__ == '__main__':
    app.run()


