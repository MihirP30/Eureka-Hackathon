from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
  return render_template("index.html", greeting="hello", content=name, mylist=[1, 2, 3, 4, 5]) #finds {{content}} in index.html and replaces it with name

if __name__ == "__main__":
  app.run()