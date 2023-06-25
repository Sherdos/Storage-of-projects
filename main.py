from database.models import Project

line = '-----------\n'


while True:
    print(f'{line}All comand:\n1 - add project,\n2 - get all projects\n{line}')
    comand = input('Choose camand - ')
    if comand == '1':
        text = input('Write name project - ')
        description = input('Descrip project - ')
        project = Project(text, description)
        project.add_project()
    elif comand == '2':
        Project.all_objects()


    
    