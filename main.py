import flet as ft
import sys
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(BASE_DIR)

import database


# def add_project(page,title,description):
#     project = database.Project(title.value, description.value)
#     project.save_project()
#     get_all_projects(page)
#     # page.columb_p.update()
#     title.value = ""
#     title.focus()
#     title.update()
#     description.value = ""
#     description.update()


# def get_all_projects(page):
#     all_projects = database.Project.all_objects(None)
#     list_project = []
#     for i, project in enumerate(all_projects, 1):
#         t = ft.Text()
#         t.value = f'{i}) {project[1]}: {project[2]}, ID={project[0]}'
#         list.append(t)
#     columb_p = ft.Column(list_project)
#     page.add(columb_p)
#         # time.sleep(1)


def delete_project(project_id):
    
    info = database.Project.delete_project(None,project_id)
    print(f'Project {info} deleted.')
    input('Press Enter to continue...')


# def main():
#     line = '-----------\n'
#     while True:
#         print(f'{line}Available commands:\n1 - Add project,\n2 - Get all projects\n3 - Delete project\n{line}')
#         command = input('Choose command - ')
        
#         if command == '1':
#             add_project()
            
#         elif command == '2':
#             get_all_projects()
            
#         elif command == '3':
#             delete_project()
            
#         else:
#             print('Invalid command. Please choose a valid command.')


# def main(page: ft.Page):
#      # it's a shortcut for page.controls.append(t) and then page.update()

#     get_all_projects(page)
#     def provider(e):
#         add_project(page,title,description)

#     title = ft.TextField(hint_text="Enter project name:", width=300)
#     description = ft.TextField(hint_text="Enter project description: ", width=300)  
#     greetings = ft.Column()  
#     page.add(ft.Row([title,description, ft.ElevatedButton("Add", on_click=provider)]))


# ft.app(target=main) 

# # if __name__ == '__main__':
#     main()
