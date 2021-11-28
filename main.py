# coding:utf-8
from flask import Flask,jsonify,render_template

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)