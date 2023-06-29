import flet as ft


import database


def add_project(title,description):
    project = database.Project(title.value, description.value)
    project.save_project()

add_project_lambda = lambda title, description: database.Project(title.value, description.value).save_project()

def get_all_projects():
    info = database.Project.all_objects(None)
    return info

get_all_projects_lambda = lambda:database.Project.all_objects(None)



def delete_project(project_id):
    info = database.Project.delete_project(None,project_id)
    return info

delete_project_lambda = lambda id : database.Project.delete_project(None,   id)


# def main(page: ft.Page):

#     page.add()


# ft.app(target=main)

# schedule = {
#     'Monday': ['Movie'],
#     'Tuesday': ['Igilik', 'blog'],
#     'Wednesday': ['my_py',],
#     'Thursday': ['tel',''],
#     'Friday': ['Movie'],
#     'Saturday': ['Igilik', 'blog'],
#     'Sunday': ['my_py','tel']
# }