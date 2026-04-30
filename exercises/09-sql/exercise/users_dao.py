import sqlite3


def new_user(p_name, p_surname, p_email, p_password, p_profile_img):

    query = "INSERT INTO users (name, surname, email, password) VALUES (?,?,?,?)"

    if p_profile_img != "":
        query = "INSERT INTO users (name, surname, email, password, profile_img) VALUES (?,?,?,?,?)"

    conn = sqlite3.connect("imparato.db")
    cursor = conn.cursor()

    if p_profile_img != "":
        cursor.execute(query, (p_name, p_surname, p_email, p_password, p_profile_img))
    else:
        cursor.execute(query, (p_name, p_surname, p_email, p_password))

    conn.commit()
    cursor.close()
    conn.close()


def get_id_by_email(p_email):
    
    query = "SELECT id FROM users WHERE users.email = ?"

    conn = sqlite3.connect("imparato.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(query, (p_email,))

    db_user = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()

    return db_user