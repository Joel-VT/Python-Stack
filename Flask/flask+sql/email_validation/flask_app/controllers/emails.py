from crypt import methods
from flask_app import app
from flask import request, render_template, redirect, flash
from flask_app.models.email_model import Email

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/email/create', methods = ["POST"])
def create_email():
    if not Email.validator(request.form):
        return redirect('/')
    elif Email.get_one_by_email(request.form):
        flash('*Email already exists')
        return redirect('/')
    Email.create(request.form)
    return redirect('/email/show/all')

@app.route('/email/show/all')
def show_all():
    return render_template("show_all.html", emails = Email.get_all())

@app.route('/email/<int:id>/delete')
def delete_email(id):
    Email.delete({'id': id})
    return redirect('/email/show/all')