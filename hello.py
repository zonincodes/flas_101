from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello World</h1>"


@app.route("/moji/")
def moji():
    return "Moji shorti Baba is "


@app.route("/hello/<name>")
def hello_name(name):
    return "Life will be okay %s!" % name


@app.route("/guest/<guest>")
def hello_guest(guest):
    return "Hello %s" % guest


@app.route("/admin/")
def hello_admin():
    return "Hello admin"


@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest", guest=name))


if __name__ == '__main__':
    app.run(debug=True)
