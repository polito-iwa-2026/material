import sqlite3


def get_tutors():
    tutors_query = "SELECT * FROM Tutors"
    conn = sqlite3.connect("imparato.db")
    cursor = conn.cursor()

    cursor.execute(tutors_query)

    db_tutors = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    return db_tutors


def new_tutor(p_name, p_surname, p_quote, p_profileimg):
    query = "INSERT INTO Tutors (name, surname, presentation, profile_img) VALUES (?,?,?,?)"

    conn = sqlite3.connect("imparato.db")
    cursor = conn.cursor()

    cursor.execute(query, (p_name, p_surname, p_quote, p_profileimg))

    conn.commit()
    cursor.close()
    conn.close()
