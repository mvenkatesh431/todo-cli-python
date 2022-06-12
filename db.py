from todoModel import OPEN, COMPLETED, Todo
import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
class TodoSQL(Base):
    """
    Todo Class defines the todos table schema.
    """
    __tablename__ = "todos"
 
    position = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    priority = Column(Integer)
    status = Column(Boolean, unique=False, default=OPEN)
    creation_time = Column(DateTime, default=datetime.datetime.now)
    completion_time = Column(DateTime)

    #----------------------------------------------------------------------
    def __init__(self, name, category, priority, creation_time):
        """"""
        self.name = name
        self.category = category
        self.priority = priority
    
    # def __repr__(self):
    #     return f"{self.position}, {self.name}, {self.category}, {self.priority}, {self.status}, {self.creation_time}, {self.completion_time}"


# 'engine' is going to communicate with the sqlite3 DB
# Engine won't connect now, It will connect whenever we submit a query to DB.
# creating an Engine through the create_engine() function usually generates a QueuePool.
# This kind of pool comes configured with some reasonable defaults, like a maximum pool size of 5 connections.
engine = create_engine('sqlite:///todos.db', echo=False)

# create tables
Base.metadata.create_all(engine)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()


def add_todo(todo: Todo):
    '''
        Add a new To-do to List 
        Takes 'Todo' Object, Inserts into 'todos.db'
    '''
    todoItem = TodoSQL(todo.name, todo.category, todo.priority, todo.creation_time)
    session.add(todoItem)
    session.commit()


def get_todo_list():
    '''
        get_todo_list - Read all todos from 'todos.db' and return it as List[Todo]
    '''
    todos = []
    for todoItem in session.query(TodoSQL).order_by(TodoSQL.position):
        todos.append(Todo(todoItem.name, todoItem.category, todoItem.priority, todoItem.status, todoItem.position, todoItem.creation_time, todoItem.completion_time))
    return todos

def update_todo(position, params):
    '''
        Update Todo Name, Category and Priority using TodoID.
    '''
    params = {k: v for k, v in params.items() if v is not None}
    print(params)
    session.query(TodoSQL).filter_by(position=position).update(params)
    session.commit()

def complete_todo(position):
    '''
        Mark todo as 'COMPLETE'
    '''
    session.query(TodoSQL).filter_by(position=position).update({"status":COMPLETED, "completion_time": datetime.datetime.now()})
    session.commit()

def delete_todo(position):
    '''
        Delete Todo from To-Do List
    '''

    # Get the number of rows.
    rowCount = session.query(TodoSQL).count()
    print("Row Count : ", rowCount)

    # session.query.filter(TodoSQL.position == position).delete()
    session.query(TodoSQL).filter_by(position=position).delete()
    session.commit()

    # Move the position of all entries after 'position' by '-1'
    for pos in range(position+1, rowCount+1):
        print("calling change_position with old_position:", pos, "new_position", pos-1)
        change_position(pos, pos-1)

def change_position(old_position, new_position):
    session.query(TodoSQL).filter_by(position=old_position).update({"position":new_position})
    session.commit()


def remove_all_todos():
    '''
    remove_all_todos from the Todo List
    '''
    # Drop the table and reset the index
    # Todo.__table__.drop(engine)
    Base.metadata.drop_all(engine, tables=[TodoSQL.__table__])
    Base.metadata.create_all(engine, tables=[TodoSQL.__table__])
