import sqlite3
from todoModel import COMPLETED, Todo
import datetime

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
            data = (todo.name, todo.category, todo.priority, todo.status, todo.position, todo.creation_time, todo.completion_time)
            c.execute(insert_query, data)
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

def update_todo(position, params):
    '''
        Update Todo Name, Category and Priority using TodoID.
    '''
    fields_to_set = []
    field_values = []
    # loop thru the params passed
    for key in params:
        if params.get(key) is not None:
            # build up the SET statement using the param keys
            fields_to_set.append(key + "=?")
            # save the values to be used with the SET statement
            field_values.append(params[key])
        
    # join the SET statement together
    set_statement = ", ".join(fields_to_set)
    field_values.append(position)
    cmd = "UPDATE todos SET "+set_statement+" WHERE position=?"
    
    # Update the db.
    #print(cmd, tuple(field_values))
    with conn:
        c.execute(cmd, field_values)

def complete_todo(position):
    '''
        Mark todo as 'COMPLETE'
    '''
    with conn:
        update_query = """Update todos set status = ?, completion_time = ? where position = ?"""
        data = (COMPLETED, datetime.datetime.now().isoformat(), position)
        c.execute(update_query, data)

def delete_todo(position):
    '''
        Delete Todo from To-Do List
    '''
    c.execute('select count(*) from todos')
    count = c.fetchone()[0]

    with conn:
        delete_query = """DELETE from todos where position = ?"""
        c.execute(delete_query, (position,))   # second argument tuple

        # Move the position of all entries after 'position' by '-1'
        for pos in range(position+1, count):
            # print("calling change_position with old_position:", pos, "new_position", pos-1)
            change_position(pos, pos-1)


def change_position(old_position, new_position):
    update_query = """Update todos set position = ? where position = ?"""
    data = (new_position, old_position)
    c.execute(update_query, data)
    conn.commit()

def remove_all_todos():
    '''
    remove_all_todos from the Todo List
    '''
    drop_query = """DROP TABLE todos;"""
    with conn:
        c.execute(drop_query)