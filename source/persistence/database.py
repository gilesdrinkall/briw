import pymysql
from os import environ


def get_db_connection():
    db = pymysql.connect(

        environ.get('DB_HOST'),
        environ.get('DB_USER'),
        environ.get('DB_PASSWORD'),
        environ.get('DB_NAME'),
        autocommit=True
    )
    return db


def get_all_data_from_db_table(db_table: str):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"SELECT * FROM {db_table};")
    results = cursor.fetchall()
    db.close()
    return results


def create_dict_with_subset_data_db(db_table: str, field_1: str, field_2: str):
    subset_dict = {}
    results = get_all_data_from_db_table(db_table)
    for row in results:
        entry_1 = row[field_1]
        entry_2 = row[field_2]
        subset_dict[entry_1] = entry_2
    return subset_dict


def add_person_to_db(first_name):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"INSERT INTO person (first_name) VALUES (\"{first_name}\");")
    db.commit()
    db.close()


def add_drink_to_db(name):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"INSERT INTO drink (name) VALUES (\"{name}\");")
    db.commit()
    db.close()


def delete_person_from_db(person_id):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"DELETE FROM person WHERE person_id = (\"{person_id}\");")
    db.commit()
    db.close()


def delete_drink_from_db(drink_id):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"DELETE FROM drink WHERE drink_id = (\"{drink_id}\");")
    db.commit()
    db.close()


def add_maker_to_db(maker_name):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"INSERT INTO round (maker_name) VALUES (\"{maker_name}\");")
    row_id = cursor.lastrowid
    db.commit()
    db.close()
    return row_id


def get_maker_name_from_db():
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT maker_name FROM round ORDER BY round_id DESC LIMIT 1;")
    result = cursor.fetchone()
    db.close()
    return result


def get_round_id_from_db():
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT round_id FROM round ORDER BY round_id DESC LIMIT 1;")
    result = cursor.fetchall()
    db.close()
    return result


def create_order(person_name, drink_name):
    db = get_db_connection()
    db_output = get_round_id_from_db()
    rnd_dict = db_output[0]
    round_id = rnd_dict['round_id']
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"INSERT INTO orders (round_id, person_name, drink_name) VALUES ({round_id}, \"{person_name}\", \"{drink_name}\");")
    db.commit()
    db.close()
