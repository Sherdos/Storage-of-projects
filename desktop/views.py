import time
import flet as ft
from database.models import *


Text = {
    'color':'green'
}

def home(page: ft.Page):

    def add_clicked(e):
        project = Project.object.create(name = pr_name.value, description = pr_description.value)
        for_all(page)
        pr_name.value = ""
        pr_description.value = ""
        pr_name.focus()
        page.update()

    pr_name = ft.TextField(label="Project name")
    pr_description = ft.TextField(label="Project description")
    page.add(
        ft.Row(controls=[
            pr_name,
            pr_description,
            ft.ElevatedButton(text="Say my name!",on_click=add_clicked)
        ])
    )
    for_all(page)
    
        # time.sleep(1)

def for_all(page):
    projects = Project.object.all()
    for index,project in enumerate(projects,1):
        db_project = ft.Text(value=f'{index}) {project.name} : {project.description}')
        page.add(db_project)


