from crypt import methods
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninja/add')
def new_ninja():
    return render_template("add_ninja.html", dojos = Dojo.get_all())

@app.route('/ninja/create', methods = ["POST"])
def create():
    Ninja.create(request.form)
    return redirect("/")