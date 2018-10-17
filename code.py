import csv
import sqlite3
from sqlite3 import Error


def readFiles(filename):
    first_names = []
    last_names = []
    dob = []
    favorite_colors = []
    cat = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            first_names.append(row[0])
            last_names.append(row[1])
            dob.append(row[2])
            favorite_colors.append(row[3])
            cat.append(row[4])

        return first_names, last_names, dob, favorite_colors, cat


first_names, last_names, dob, favorite_colors, cat = readFiles('roster.csv')

print(first_names)
print(last_names)
print(dob)
print(favorite_colors)
print(cat)


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     conn.close()
    #     print("closing")


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("creating table")
    except Error as e:
        print(e)


def main():
    database = "sqlite.db"
    print(database)

    sql_create_colors_table = """ CREATE TABLE IF NOT EXISTS colors (
        id integer PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        favorite_colors text NOT NULL
    ); """

    sql_create_cat_table = """ CREATE TABLE IF NOT EXISTS cat (
        id integer PRIMARY KEY,
        first_name text NOT NULL,
        last_name text NOT NULL,
        cat text NOT NULL
    ); """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_colors_table)
        create_table(conn, sql_create_cat_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    # create_connection('sqlite.db')
    main()
