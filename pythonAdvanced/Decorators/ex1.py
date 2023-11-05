from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return 'This is my HomePage'

@app.route("/contacts")
def contacts():
    return "This is my ContactPage"

if __name__ == '__main__':
    app.run()