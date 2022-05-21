import typer
from todoModel import Todo
from db import add_todo, get_todo_list

# To-do App Version
__version__ = "0.5.0"

# Initialize the Typer app
app = typer.Typer()

@app.command(short_help="Add a To-do to ToDo List")
def add(name: str, category: str, priority: int = typer.Argument(3)):
    typer.echo(f"Adding 'Name:{name}, Category:{category}, Priority:{priority}' To-Do List")
    todoItem = Todo(name, category, priority)
    add_todo(todoItem)

@app.command(short_help="Update a To-do using TODOID")
def update(position: int, name: str = None, category: str = None):
    typer.echo(f"Updating Todo at {position}")

@app.command(short_help="Delete a To-do from ToDo List using it's TODOID")
def delete(position: int):
    typer.echo(f"Deleting Todo at {position}")

@app.command(short_help="Complete a To-do by marking it 'Done' using TODOID")
def complete(position: int):
    typer.echo(f"Marking Todo at {position} as 'Done'")

@app.command(short_help="List all To-do's")
def list():
    # typer.echo(f"Todos")
    todo_list = get_todo_list()

    # check if the todo_list is empty
    if len(todo_list) == 0:
        typer.secho ("There are no tasks in the to-do list yet", fg=typer.colors.RED)
        return
    
    # print(todo_list)

    typer.secho("\nTo-Do List:\n", fg=typer.colors.BLUE, bold=True)
    columns = (
        "ID.  ",
        "| Name  ",
        "| Category  ",
        "| Priority  ",
        "| Status  ",
        "| Creation Time  ",
        "| Completion Time  ",
    )
    headers = "".join(columns)
    typer.secho(headers, fg=typer.colors.BLUE, bold=True)
    typer.secho("-" * len(headers), fg=typer.colors.BLUE)

    for id, todo in enumerate(todo_list, 1):
        print(id, todo)
        


@app.command(short_help="Remove all To-do's")
def clear():
    typer.echo(f"Removing all To-do's")
    
@app.command(short_help="Display the version")
def version():
    typer.echo(f"Version: {__version__}")

if __name__ == "__main__":
    app()
