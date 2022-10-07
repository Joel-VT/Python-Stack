from crypt import methods
from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo

@app.route('/')
def show_all_dojos():
    return render_template("index.html", dojos = Dojo.get_all())

@app.route('/dojo/new', methods=["POST"])
def new_dojo():
    Dojo.create(request.form)
    return redirect('/')

@app.route('/dojo/one/<int:id>')
def show_one_dojo(id):
    return render_template("one_dojo.html", one_dojo = Dojo.get_one({'id':id}))