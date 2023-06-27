import sqlite3
from types import NoneType


def data_open(command, commit=False):
    def connect(func):
        def wrapper(self, *args, **kwargs):
            conn = sqlite3.connect('projects.db')
            par = func(self,*args,**kwargs)
            if commit:
                conn.execute(command,par[0])
                conn.commit()
                info = None
            else:
                print(par)
                if par  is not None:
                    info = conn.execute(command,par[0]).fetchall()
                else:
                    info = conn.execute(command).fetchall()
            conn.close()
            return info
        return wrapper
    return connect

        

print()
class Project():
    def __init__(self,  title, description):
        self.title = title
        self.description = description

    def add_project(self):
        self.__write_file(self.title, self.description)
        print('Your project added successfully.')

    @data_open("INSERT INTO project (title,description) VALUES (?,?);",True)
    def __write_file(self,text, description):
        return text, description
    
    @data_open("SELECT * FROM project;")
    def all_objects(self):
        return None
    
    @data_open("DELETE FROM project where id = ?")
    def delete_project(id):
        return id
