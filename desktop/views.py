import flet as ft

from database.models import Project



# git config --global user.name "Sherdos"
class TodoApp(ft.UserControl):
    all_prpjects = [ft.Checkbox(label=i.name) for i in Project.object.all()]
    all_prpjects.reverse()
    
    def build(self):
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = ft.Column()
        self.tasks.controls = self.all_prpjects

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks,
            ],
        )

    def add_clicked(self, e):
        project = Project.object.create(name = self.new_task.value, description = 'Hello')
        self.tasks.controls.insert(0,ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()


def home(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()

    page.add(todo)