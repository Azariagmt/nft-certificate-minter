from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index.html")


@app.route("/optin")
def optin_page():
    return render_template("optin.html")


# so this flask api will return a json object which interacts with the blockchain
if __name__ == "__main__":
    app.run(debug=True)
    # app.run()
