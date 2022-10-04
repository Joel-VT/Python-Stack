from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/funta')
def display_info():
    return "Funta Myre!"

@app.route("/<name>/<int:x>")
def display_myre(name,x):
    print(name)
    print(x)
    return f"Nee po Myre {name}"*x

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
