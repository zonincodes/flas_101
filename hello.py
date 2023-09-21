# imports
from flask import Flask, redirect, url_for, request, render_template

# Initialization
app = Flask(__name__)


# Routing
@app.route('/')
def index():
    return render_template('index.html')


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


#  Jinja templating
@app.route('/score/<int:score>')
def hello_score(score):
    return render_template("score.html", marks=score)


@app.route("/results/")
def results():
    result_dict = {'phy': 78, "math": 90, "eng": 56, 'geo': 34}
    return render_template("results.html", results=result_dict)


if __name__ == '__main__':
    app.run(debug=True)
