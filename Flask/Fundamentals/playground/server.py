from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello and welcome to my playground assignment. Please type /play extension to start"

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<color>')
def level_2(num = 3, color = "#9ec5f8"):
    return render_template("index.html", num = num, color = color)

if __name__ == "__main__":
    app.run(debug=True)