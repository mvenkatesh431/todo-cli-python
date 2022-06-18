import typer
from todoModel import *
from db import add_todo, get_todo_list, complete_todo, delete_todo, remove_all_todos, update_todo
from rich.console import Console
from rich.table import Table
import random


# To-do App Version
__version__ = "1.0.0"

# Initialize the Typer app
app = typer.Typer()

# Create console object
console = Console()

# Typer options reference - https://typer.tiangolo.com/tutorial/options/help/
@app.command(short_help="Add a To-do to ToDo List")
def add(name: str = typer.Option(..., "--name", "-n"),
            category: str = typer.Option(..., "--category", "-c"), 
            priority: int = typer.Option(3, "--priority", "-p")):
    # typer.echo(f"Adding 'Name:{name}, Category:{category}, Priority:{priority}' to To-Do List")
    todoItem = Todo(name, category, priority)
    add_todo(todoItem)
    list()

# User can update TodoName, Category and Priority.
@app.command(short_help="Update a To-do(Name, category and priority) using TODOID")
def update(position: int, name: str = typer.Option(None, "--name", "-n"),  
                category: str = typer.Option(None, "--category", "-c"),
                priority: int = typer.Option(None, "--priority", "-p")):
    '''
        ex: python main.py update 4 --name="Complete To-do project" --category='Python'  --priority=1
    '''
    # typer.echo(f"Updating Todo at {position}. (Note: 'If Position is invalid, No changes will be made.')")
    update_todo(position, {"name":name, "category":category, "priority":priority})
    list()

@app.command(short_help="Delete a To-do from ToDo List using it's TODOID")
def delete(position: int):
    # typer.echo(f"Deleting Todo at {position}")
    delete_todo(position)
    list()

@app.command(short_help="Complete a To-do by marking it 'Done' using TODOID")
def complete(position: int):
    # typer.echo(f"Marking Todo at {position} as 'Done'")
    complete_todo(position)
    list()

@app.command(short_help="List all To-do's")
def list():
    # typer.echo(f"Todos")
    todo_list = get_todo_list()

    # check if the todo_list is empty
    if len(todo_list) == 0:
        typer.secho("There are no tasks in the to-do list yet", fg=typer.colors.RED)
        return
    
    # Lets create a Table using the Rich Table
    # Table Ref - https://rich.readthedocs.io/en/stable/reference/table.html#rich.table.Table
    # Rich Color ref - https://rich.readthedocs.io/en/stable/appendix/colors.html

    table = Table(title="📝 Todo List ! 🗒️", title_style ="bold cyan", show_header=True, header_style="bold indian_red")
    table.add_column("S. No.", style="cyan", justify="center", no_wrap=True)
    table.add_column("Name", justify="Left")
    table.add_column("Category", justify="left")
    table.add_column("Priority", justify="center")
    table.add_column("Status", justify="center", style="green")
    table.add_column("Created at", justify='center')
    table.add_column("Completed at", justify='center')

    category_color_map = {}

    # Lets add the rows from the 'todo_list'
    for id, todo in enumerate(todo_list, 1):
        status = '✅' if todo.status == COMPLETED else '❌'
        clr = "white"
        # clr = category_color_map.get(todo.category, get_random_color())
        if todo.category not in category_color_map:
            clr = get_random_color()
            category_color_map[todo.category] = clr
        else:
            clr = category_color_map.get(todo.category)

        pclr = get_priority_color(todo.priority)
    
        table.add_row(str(id), todo.name, f'[{clr}]{todo.category}[/{clr}]', f'[{pclr}]{str(todo.priority)}[/{pclr}]',
                        status, str(todo.creation_time), str(todo.completion_time) )

    console.print(table)

@app.command(short_help="Remove all To-do's")
def clear():
    typer.secho(f"Deleting all To-do's !!!", fg=typer.colors.RED)
    delete = typer.confirm("Are you sure you want to delete all To-Dos?", abort=True)
    remove_all_todos()
    typer.echo("All To-Dos were removed")
    
@app.command(short_help="Display the version")
def version():
    typer.echo(f"Version: {__version__}")

def get_random_color():
    richColors = [ 'deep_pink4', 'plum2', 'dark_orange', 'magenta', 'cornflower_blue', \
                    'bright_green', 'grey50', 'light_pink3', 'violet', 'orchid', 'gold1', \
                    'white', 'magenta', 'orange4', 'yellow', 'cyan', 'red']
    return random.choice(richColors)

def get_priority_color(priority):
    p_map = {1: 'red', 2:'magenta', 3:'blue', 4:'cyan', 5:'green'}
    if priority in p_map:
        return p_map[priority]
    return 'green'

if __name__ == "__main__":
    app()
