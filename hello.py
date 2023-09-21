# imports
from flask import Flask, redirect, url_for, request

# Initialization
app = Flask(__name__)


# Routing
@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"


@app.route("/moji/")
def moji():
    return "Moji short Baba is "


# Variable rules
@app.route("/hello/<name>")
def hello_name(name):
    return "Life will be okay %s!" % name


@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s" % guest


@app.route("/admin/")
def hello_admin():
    return "Hello admin"


# Url building
@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))


# Flask http methods
@app.route("/login", methods={'POST', 'GET'})
def login():
    if request.method == "POST" or request.method == "post":
        user = request.form['nm']
        return redirect(url_for('hello_name', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for("hello_guest", guest=user))


if __name__ == '__main__':
    app.run(debug=True)
