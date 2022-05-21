import sqlite3
from todoModel import Todo

# connect to sqlite db
conn = sqlite3.connect("todos.db")
# create cursor object
c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos (
            name text NOT NULL,
            category text NOT NULL,
            priority integer NOT NULL,
            status integer NOT NULL,
            position integer PRIMARY KEY,
            creation_time text,
            completion_time text
            )""")

create_table()


def add_todo(todo: Todo):
    '''
        Add a new To-do to List 
        Takes 'Todo' Object, Inserts into 'todos.db'
    '''
    # count(*) will give us the number of Todos
    # Note count(*) index starts with 1.
    c.execute("select count(*) FROM todos")
    cnt = c.fetchone()[0]

    # if we already have todos use 'count' otherwise it is first todo.
    todo.position = cnt if cnt else 0

    # Insert todo at 'todo.position'
    try:
        with conn:
            insert_query = """INSERT INTO todos
                            (name, category, priority, status, position, creation_time, completion_time) 
                            VALUES (?, ?, ?, ?, ?, ?, ?);"""
            data_tuple = (todo.name, todo.category, todo.priority, todo.status, todo.position, todo.creation_time, todo.completion_time)
            c.execute(insert_query, data_tuple)
    except sqlite3.Error as error:
        print("Failed to insert to table")


def get_todo_list():
    '''
        get_todo_list - Read all todos from 'todos.db' and return it as List[Todo]
    '''
    todos = []
    c.execute("select * from todos")
    allTodos = c.fetchall()

    for item in allTodos:
        todos.append(Todo(*item))
    return todos
    