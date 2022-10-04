from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "too funny!"

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("result.html")

@app.route('/back', methods = ["POST"])
def back():
    session.clear();
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)