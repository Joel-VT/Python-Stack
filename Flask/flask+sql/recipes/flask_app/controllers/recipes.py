from crypt import methods
from multiprocessing.spawn import import_main_path
from flask_app import app
from flask import request, render_template, redirect, flash, session
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from datetime import datetime


@app.route('/recipe/new')
def new_recipe():
    if not 'user_id' in session:
        return redirect('/')
    return render_template("recipe_new.html")


@app.route('/recipe/create', methods=["POST"])
def create_recipe():
    if not 'user_id' in session:
        return redirect('/')
    if not Recipe.validator(request.form):
        return redirect('/recipe/new')
    data = {
        **request.form,
        'user_id' : session['user_id']
    }
    Recipe.create(data)
    return redirect(f"/welcome/{session['user_id']}")

@app.route('/recipe/show/<int:id>')
def show_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    return render_template("recipe_show.html", recipe = Recipe.get_one({'id' : id}), user = User.get_by_id({'id' : session['user_id']}))

@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    recipe = Recipe.get_one({'id' : id})
    if session['user_id'] != recipe.user_id:
        return redirect("/logout")
    print(recipe.name)
    return render_template("recipe_edit.html", recipe = recipe)

@app.route('/recipe/update/<int:id>', methods = ["POST"])
def update_recipe(id):
    if not Recipe.validator(request.form):
        return redirect(f'/recipe/edit/{id}')
    data = {
        **request.form,
        'id' : id
    }
    Recipe.update(data)
    return redirect(f"/welcome/{session['user_id']}")

@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    if not 'user_id' in session:
        return redirect('/')
    recipe = Recipe.get_one({'id' : id})
    if session['user_id'] != recipe.user_id:
        return redirect("/logout")
    Recipe.delete({'id' : id})
    return redirect(f"/welcome/{session['user_id']}")