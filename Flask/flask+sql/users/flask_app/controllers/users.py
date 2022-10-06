from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user_model import User

@app.route('/')
def hello():
    return render_template("index.html", users = User.get_all())

@app.route('/user/one/<int:id>')
def one_user(id):
    return render_template("one_user.html", user = User.get_one({'id' : id}))

@app.route('/user/add')
def new_user():
    return render_template("new_user.html")

@app.route('/user/create', methods = ["POST"])
def user_create():
    id = User.create(request.form)
    return redirect(f"/user/one/{id}")

@app.route('/user/delete/<int:id>')
def user_delete(id):
    User.delete({'id' : id})
    return redirect("/")

@app.route('/user/update/<int:id>')
def user_edit(id):
    return render_template("user_update.html", user = User.get_one({'id' : id}))

@app.route('/user/render/<int:id>', methods = ["POST"])
def user_update(id):
    data = {
        'id' : id,
        **request.form
    }
    User.update(data)
    return redirect(f'/user/one/{id}')