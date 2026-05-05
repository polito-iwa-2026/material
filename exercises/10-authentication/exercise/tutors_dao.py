import sqlite3, users_dao


def get_tutors():
    tutors_query = "SELECT * FROM tutors"
    conn = sqlite3.connect("imparato.db")
    cursor = conn.cursor()

    cursor.execute(tutors_query)

    db_tutors = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()

    return db_tutors



def new_tutor(p_email, p_bio):
    
    id = users_dao.get_id_by_email(p_email)