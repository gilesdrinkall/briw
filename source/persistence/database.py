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


def get_data_from_dictionary(db_table: str):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"SELECT * FROM {db_table}")
    results = cursor.fetchall()
    db.close()
    return results

def create_dictionary(db_table: str, dict_val: str, dict_key: str):
    dict_name = {}
    results = get_data_from_dictionary(db_table)
    for row in results:
        table_id = row[dict_val]
        item_name = row[dict_key]
        dict_name[table_id] = item_name
    return dict_name

def add_person(first_name):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"INSERT INTO Person (first_name) VALUES (\"{first_name}\");")
    db.close()

def add_drink(name):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"INSERT INTO Drink (name) VALUES (\"{name}\");")
    db.close()

def delete_person(person_id):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"DELETE FROM Person WHERE person_id = (\"{person_id}\");")
    db.close()

def delete_drink(drink_id):
    db = get_db_connection()
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute(f"DELETE FROM Drink WHERE drink_id = (\"{drink_id}\");")
    db.close()