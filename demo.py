from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("index.html")

@app.route("/<usr>")
def user(usr):
    x = len(usr)
    return f"<h1>{x}<h1>"

if __name__ == "__main__":
    app.run(debug=True)
