import sqlite3
import os

import driver
from driver import *

def create_database():
    con = sqlite3.connect("./data.db")

    con.execute("""
        create table if not exists files (file_id text primary key, filename text, 
        question text, answer text, encrypted boolean, file_location text
    )""",[])

def get_all_filenames():
    con = sqlite3.connect("./data.db")
    cur = con.cursor()
    cur.execute("SELECT filename FROM files")
    rows = cur.fetchall()
    return rows;

def get_text_from_file_by_name(filename):
    con = sqlite3.connect("./data.db")
    cur = con.cursor()
    cur.execute("SELECT file_location FROM files WHERE filename == '" + filename+"'")
    rows = cur.fetchall()

    with open(rows.pop()[0], "r") as f:
        data = f.read()

    return data


def upload_file_to_db(file, question, answer):
    file_path = file.name
    file_name = file_path.rsplit('/', 1)[-1]
    file_location = "files/{}".format(file_name)

    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    encryptFile(file_path, file_name)
    sqlite_insert_with_param = """INSERT INTO files (filename, question, answer, encrypted, file_location) 
        VALUES (?,?,?,?,?);"""
    data_tuple = (file_name, question, answer, 1, file_location)
    cur.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    cur.close()

def get_file_question_answer(filename):
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("SELECT filename, question, answer, encrypted, file_location FROM files WHERE filename == '" + filename+"'")
    rows = cur.fetchall()
    for row in rows:
        print(row)


    return rows[0][0], rows[0][1].strip(), rows[0][2].strip(), rows[0][3], rows[0][4]


def update_file(file_data):
    delete_file(file_data[0], False)
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    sqlite_insert_with_param = """INSERT INTO files (filename, question, answer, encrypted, file_location) 
        VALUES (?,?,?,?,?);"""

    if file_data[3] == 0:
        # Encrypt
        data_tuple = (file_data[0], file_data[1], file_data[2], 1, file_data[4])
        driver.encryptFile(file_data[4], file_data[0])
    else:
        # Decrypt
        data_tuple = (file_data[0], file_data[1], file_data[2], 0, file_data[4])
        driver.decryptFile(file_data[4], file_data[0])

    cur.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()
    cur.close()


def delete_file(filename, hard_delete):
    conn = sqlite3.connect("./data.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM files WHERE filename == '" + filename + "'")
    conn.commit()
    cur.close()
    if hard_delete:
        os.remove("files/" + filename)

