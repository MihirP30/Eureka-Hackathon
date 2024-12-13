from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
  # we can reach this page from entering the url (GET) or clicking submit on the form (POST)
  if request.method == "POST":
    name = request.form["nm"] # get the value in the nm box in the form
    return redirect(url_for("user", usr=name))
  else:
    return render_template("login.html")

@app.route("/<usr>")
def user(usr):
  return f"<h1>{usr}</h1>"

if __name__ == "__main__":
  app.run(debug=True)