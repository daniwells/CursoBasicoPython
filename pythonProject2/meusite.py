from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/users/<name_user>")
def users(name_user):
    return render_template("users.html", name_user=name_user)

if __name__ == "__main__":
    app.run(debug=True)