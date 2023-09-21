from flask import Flask

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


if __name__ == '__main__':
    app.run(debug=True)
