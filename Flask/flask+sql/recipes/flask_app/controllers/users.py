from flask_app import app
from flask import request, render_template, redirect, flash, session
from flask_app.models.user_model import User
from flask_app.models.recipe_model import Recipe
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods = ["POST"])
def register_user():
    if not User.validator(request.form):
        return redirect('/')
    if User.get_by_email(request.form):
        flash('Email already used', 'email')
        return redirect('/')
    data = {
        **request.form,
        'password' : bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.create(data)
    return redirect(f"/welcome/{session['user_id']}")

@app.route('/welcome/<int:id>')
def welcome(id):
    if not 'user_id' in session:
        return redirect('/')
    return render_template('user_show.html', user = User.get_by_id({'id' : id}), recipes = Recipe.get_all())

@app.route('/login', methods = ["POST"])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash('Invalid Email/Password', 'log')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash('Invalid Email/Password*', 'log')
        return redirect('/')
    session['user_id'] = user.id
    return redirect(f'/welcome/{user.id}')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')