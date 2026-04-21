from flask import Flask, render_template, request

import tutors_dao

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
    quote = request.form.get("txt_quote")

    profile_img = request.files["img_profile"]
    profile_img.save("static/images/profile_imgs/" + profile_img.filename)

    tutors_dao.new_tutor(name, surname, quote, profile_img.filename)

    return "Works!"
