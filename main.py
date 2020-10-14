from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about_me():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("/portfolio/fakebook.html")


@app.route("/portfolio/google")
def boogle():
    return render_template("/portfolio/google.html")


@app.route("/portfolio/hairdresser")
def hairsalon():
    return render_template("/portfolio/hairdresser.html")


if __name__ == '__main__':
    app.run()