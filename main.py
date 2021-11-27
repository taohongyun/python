from flask import Flask,jsonify,render_template
# from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/")
def index():
    return render_template("简历.html")

if __name__ == "__main__":
    app.run(debug=True)