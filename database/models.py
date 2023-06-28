import sqlite3
class Project:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    @staticmethod
    def connect_db(database):
        def decorator(method):
            def wrapper(self, *args, **kwargs):
                try:
                    with sqlite3.connect(database) as conn:
                        result = method(self,conn, *args, **kwargs)
                        conn.commit()
                    return result
                except sqlite3.Error as e:
                    print(f"Ошибка при выполнении запроса: {e}")
                    return None
            return wrapper
        return decorator

    @connect_db('projects.db')
    def save_project(self, conn):
        query = "INSERT INTO project (title, description) VALUES (?, ?);"
        conn.execute(query, (self.title, self.description))
        if conn.total_changes == 1:
            print('Your project added successfully.')
        else:
            print('Failed to add the project.')

    @staticmethod
    @connect_db('projects.db')
    def all_objects(self, conn):
        query = "SELECT * FROM project;"
        result = conn.execute(query).fetchall()
        return result

    @staticmethod
    @connect_db('projects.db')
    def delete_project(self, conn, project_id):
        # Проверяем наличие проекта с указанным идентификатором
        check_query = "SELECT 1 FROM project WHERE id = ?;"
        check_result = conn.execute(check_query, (project_id,)).fetchone()
        if not check_result:
            print('Project not found.')
            return

        query = "DELETE FROM project WHERE id = ?;"
        conn.execute(query, (project_id,))
        if conn.total_changes == 1:
            print('Project deleted successfully.')
        else:
            print('Failed to delete the project.')


