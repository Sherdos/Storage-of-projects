from desktop.views import home
import flet as ft

command = [
    'run',
    'migrate'
]      

def execute_from_command_line(argv=None):
    if argv[1] == 'run':
        ft.app(target=home)

    
    