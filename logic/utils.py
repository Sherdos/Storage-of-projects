import database.models

def main():
    line = '-----------\n'
    while True:
        print(f'{line}All comand:\n1 - add project,\n2 - get all projects\n3 - delete project\n{line}')
        comand = input('Choose camand - ')
        if comand == '1':
            text = input('Write name project - ')
            description = input('Descrip project - ')
            project = database.Project(text, description)
            project.add_project()
        elif comand == '2':
            all = database.Project.all_objects(None)
            for i,one in enumerate(all, 1):
                print(f'{i}) {one[1]}: {one[2]}, ID={one[0]}')
            input()
        elif comand == '3':
            print('Enter the id of the project you want to delete')
            project_id = input('ID - ')
            info = database.Project.delete_project(project_id)
            print(f'Project {info} delete.')
            input()
        

    
    