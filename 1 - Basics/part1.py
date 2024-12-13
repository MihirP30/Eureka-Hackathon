from flask import Flask, redirect, url_for

app = Flask(__name__)
banned_users = ["yojith"]
admin_users = ["a"]

@app.route("/")
def home():
  return "Home page"

@app.route("/<name>")
def user(name):
  if name in banned_users:
    return redirect(url_for("home")) #"home" looks for method called home
  elif name in admin_users:
    return redirect(url_for("user", name="admin")) #"user" needs an arg
  else:
    return "<h1>Hello " + name + "</h1>"

if __name__ == "__main__":
  app.run()