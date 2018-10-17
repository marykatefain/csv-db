import csv
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    create_connection('sqlite.db')


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
