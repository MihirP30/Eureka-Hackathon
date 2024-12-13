from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello" # this is your encryption key, it can be anything
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent = True
    name = request.form["nm"]
    session["user"] = name
    return redirect(url_for("user"))
  else:
    if "user" in session:
      return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user")
def user():
  if "user" in session:
    name = session["user"]
    return f"<h1>{name}</h1>"
  else:
    return redirect(url_for("login")) # this redirects with a get method so it displays login.html

@app.route("/logout")
def logout():
  session.pop("user", None)
  return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True)