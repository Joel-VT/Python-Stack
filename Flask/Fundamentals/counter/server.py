from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Not so secret"
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'visit' in session and 'count' in session:
        session['visit'] += 1
        session['count'] += 1
    else:
        session['visit'] = 1
        session['count'] = 1
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def start_count():
    return redirect('/')

@app.route('/add2', methods = ["POST"])
def add_2():
    session['count'] += 1
    return redirect('/')

@app.route('/add_user_input', methods = ["POST"])
def add_user_input():
    session['count'] += int(request.form['add_value']) - 1
    return redirect('/')


@app.route('/destroy_session', methods = ["POST"])
def reset_count():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

