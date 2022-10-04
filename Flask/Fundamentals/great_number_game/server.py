from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "lol really?"

@app.route('/')
def hello():
    session['random_value'] = random.randint(1,100)
    session['tries'] = 0
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def guess():
    session['tries'] += 1
    session['guess_value'] = int(request.form["guess_value"])
    return redirect('/result')

@app.route('/result')
def process_result():
    return render_template("result.html")

@app.route('/play_again', methods = ["POST"])
def play_again():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)