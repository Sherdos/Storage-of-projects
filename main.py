import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'database.settings')
    # try:
    from logic.utils import execute_from_command_line
    # except ImportError as exc:
        # raise ImportError(
        #     "Couldn't import Django. Are you sure it's installed and "
        #     "available on your PYTHONPATH environment variable? Did you "
        #     "forget to activate a virtual environment?"
        # ) from exc
        # print(exc)
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()


# schedule = {
#     'Monday': ['Movie'],
#     'Tuesday': ['Igilik', 'blog'],
#     'Wednesday': ['my_py',],
#     'Thursday': ['tel',''],
#     'Friday': ['Movie'],
#     'Saturday': ['Igilik', 'blog'],
#     'Sunday': ['my_py','tel']
# }