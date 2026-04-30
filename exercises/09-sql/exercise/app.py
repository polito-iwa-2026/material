from flask import Flask, render_template, request, redirect, url_for

import users_dao, tutors_dao

app = Flask(__name__)

tutors_list = [
    {
        "id": 0,
        "name": "Juan Pablo",
        "surname": "Sáenz",
        "presentation": "Hi! I'm Juan!",
        "subject": "Introduction to Web Applications",
        "img": "images/juan.jpg",
        "reviews_number": 3,
    },
    {
        "id": 1,
        "name": "Luigi",
        "surname": "De Russis",
        "presentation": "Hi! I'm Luigi!",
        "subject": "Introduction to Web Applications",
        "img": "images/luigi.jpg",
        "reviews_number": 1,
    },
    {
        "id": 2,
        "name": "Alberto",
        "surname": "Monge",
        "presentation": "Hi! I'm Alberto!",
        "subject": "Calculus",
        "img": "images/alberto.jpg",
        "reviews_number": 4,
    },
]


@app.route("/")
def home():
    popular = [t for t in tutors_list if t["reviews_number"] > 1]
    are_we_in_home = True
    return render_template("index.html", ptutors=popular, phome=are_we_in_home)


@app.route("/myhistory")
def history():
    return render_template("history.html")


@app.route("/tutors")
def tutors():
    db_tutors = tutors_dao.get_tutors()

    return render_template("tutors.html", ptutors=tutors_list)

@app.route("/new_tutor")
def new_tutor():
    return render_template("new_tutor.html")

@app.route("/register_tutor", methods=["POST"])
def register_tutor():
    email = request.form.get("txt_email")
    bio = request.form.get("txt_bio")

    users_dao.get_id_by_email(p_email=email)

    return redirect(url_for("home"))

@app.route("/single_tutor/<int:id_tutor>")
def single_tutor(id_tutor):
    selected_tutor = tutors_list[id_tutor]
    parent_link = "tutors"
    return render_template("tutor.html", ptutor=selected_tutor, plink=parent_link)


@app.route("/signup")
def signup():
    return render_template("registration.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("txt_name")
    surname = request.form.get("txt_surname")
    email = request.form.get("txt_email")
    password = request.form.get("txt_password")

    img_name = ""

    profile_img = request.files["profile_img"]
    if profile_img:
        img_name = profile_img.filename
        profile_img.save("static/images/profile_imgs/" + profile_img.filename)

    users_dao.new_user(name, surname, email, password, img_name)

    return redirect(url_for("home"))
