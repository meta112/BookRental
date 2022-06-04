import sqlite3
from sqlite3 import Error
def dbconnection():
    conn = None
    try:
        conn = sqlite3.connect(r"D:\My Code\DB\sqlitestudio-3.3.3\SQLiteStudio\bookrental.db")
    except Error as e:
        print("label ", e)
    finally:
        return conn


if __name__ == "__main__":
    dbconnection()