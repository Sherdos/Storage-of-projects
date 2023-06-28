import sqlite3
DATABASE_NAME = 'projects.db'

def create_database():
    conn = sqlite3.connect(DATABASE_NAME)
    print ("Opened database successfully")
    conn.execute('CREATE TABLE project (ID INTEGER PRIMARY KEY AUTOINCREMENT, title CHAR(50), description text);')
    conn.close()
create_database()


