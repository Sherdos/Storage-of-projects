import sqlite3

class Project():
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def add_project(self):
        self.__write_file(self.title, self.description)
        print('Your project added successfully.')

    def __write_file(self,text, description):
        conn = sqlite3.connect('projects.db')
        print ("Opened database successfully")
        conn.execute("INSERT INTO project (title,description) VALUES (?,?);", (text,description))
        conn.commit()
        conn.close()

    def all_objects():
        conn = sqlite3.connect('projects.db')
        print ("Opened database successfully")
        info = conn.execute("SELECT id, title FROM project;").fetchall()
        print(info)
        conn.close()
