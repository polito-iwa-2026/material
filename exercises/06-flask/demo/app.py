from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():    
  items = ["Apple", "Banana", "Cherry"]
  return render_template("index.html", pitems = items)

@app.route("/ifexample")
def conditional():   
  return render_template("conditional.html", pusername = "Juan")

@app.route("/about")
def about():    
  return render_template("about.html")

@app.route("/newuser")
def register():    
  return render_template("register.html")