import sqlite3
def create_database():
    conn = sqlite3.connect('projects.db')
    print ("Opened database successfully")
    conn.execute('CREATE TABLE project (ID INTEGER PRIMARY KEY AUTOINCREMENT, title CHAR(50), description text);')
    conn.close()
create_database()


DATABASE_NAME = 'projects.db'
