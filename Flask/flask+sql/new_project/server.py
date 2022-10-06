from flask import Flask, render_template, request, redirect
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends=friends)

@app.route("/new_friend")
def new_friend():
    return render_template("new_friend_form.html")

@app.route("/friend/create", methods = ["POST"])
def friend_create():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "occupation" : request.form["occupation"]
    }
    Friend.create(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
