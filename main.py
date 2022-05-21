import typer

app = typer.Typer()


@app.command(short_help="Add a To-do to ToDo List")
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")


@app.command(short_help="Delete a To-do from ToDo List using it's TODOID")
def delete(position: int):
    typer.echo(f"deleting {position}")


@app.command(short_help="Update a To-do using TODOID")
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")


@app.command(short_help="Complete a To-do by marking it done using TODOID")
def complete(position: int):
    typer.echo(f"complete {position}")


@app.command(short_help="List all To-do's")
def list():
    typer.echo(f"Todos")

@app.command(short_help="Remove all To-do's")
def clear():
    typer.echo(f"Remoing all To-do's")

if __name__ == "__main__":
    app()