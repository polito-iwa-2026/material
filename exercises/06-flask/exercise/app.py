from flask import Flask, render_template

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
    return render_template("index.html", ptutors=popular)


@app.route("/tutors")
def tutors():
    return render_template("tutors.html", ptutors=tutors_list)


@app.route("/single_tutor/<int:id_tutor>")
def single_tutor(id_tutor):
    selected_tutor = tutors_list[id_tutor]
    return render_template("tutor.html", ptutor=selected_tutor)
