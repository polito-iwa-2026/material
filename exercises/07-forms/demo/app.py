from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/users")
def users_page():
    return render_template("users.html", pusers=users)


@app.route("/new_user", methods=["POST"])
def handle_form():

    name = request.form.get("name")
    email = request.form.get("email")
    size = request.form.get("t-shirt")

    new_user = {"name": name, "email": email, "tshirt": size}

    profile_img = request.files["profile_img"]
    profile_img.save(profile_img.filename)

    users.append(new_user)

    return redirect(url_for("users_page"))
