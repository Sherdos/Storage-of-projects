import flet as ft
from database.models import *


def home(page: ft.Page):

    pr_name = ft.Ref[ft.TextField]()
    pr_description = ft.Ref[ft.TextField]()
    greetings = ft.Ref[ft.ListView]()

    def add_clicked(e):
        Project.object.create(name = pr_name.current.value, description = pr_description.current.value)
        for_all(page)
        pr_name.current.value = ""
        pr_description.current.value = ""
        page.update()
        pr_name.current.focus()
    
    def delete(e):
        project = Project.object.filter(id=e.control.data)
        project.delete()
        for_all(page)

    def for_all(page):
        projects = Project.object.all()
        con = [ft.Row(
            controls=[
                ft.Text(
                    value=f'{project.name} : {project.description}'
                ),
                ft.IconButton(
                    ft.icons.REMOVE,
                    data=project.id,
                    on_click=delete,
                )
            ]
        )
        for project in projects 
        ]
        
        greetings.current.controls = con
        page.update()

    page.add(
        ft.Row(controls=[
            ft.TextField(ref=pr_name, label='Project name'),
            ft.TextField(ref=pr_description, label='Project description'),
            ft.ElevatedButton('Add', on_click=add_clicked),
            ft.Column(controls=[
                ft.Text('Projects', size=50),
                ft.ListView(ref=greetings,height=500, spacing=10),
            ]),
        ])
    )
    for_all(page)
    


