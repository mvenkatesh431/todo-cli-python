Simple Todo List CLI App - To Manage and Organize your Tasks on Terminal. It is written in Python based on Rich and Typer libraries. Rich library allows us to display the beautiful Tables with different colors on the Command line. We also used Sqlite3 and Sqlalchemy ORM to make data persistence.

The following CLI sub commands are implemented.

- `add` command       - Add a Todo to the ToDo List
- `update` command    - Update a existing Todo based on the ID (TodoID)
- `complete` command  - Mark a Todo as complete 
- `delete` command    - Delete a Todo from the Todo list
- `list` command      - List all Todo's in the Todo List
- `clear` command     - Clear the Todo List by deleting all Todos.
- `version` command   - Display the version of Todo List CLI.

## Demo:
Here is a demo of the todo list app.

[![asciicast](https://asciinema.org/a/502436.svg)](https://asciinema.org/a/502436)

## How to Run:

Please clone the repo and run install the dependencies using the following command.
```
pip install -r requirements.txt
```

Run the app using the `python main.py` pass the `--help` option to see all available CLI Options. 

```
> python main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  add       Add a To-do to ToDo List
  clear     Remove all To-do's
  complete  Complete a To-do by marking it 'Done' using TODOID
  delete    Delete a To-do from ToDo List using it's TODOID
  list      List all To-do's
  update    Update a To-do(Name, category and priority) using TODOID
  version   Display the version
>
```

## Add Command:

The `add` command used to add a `todo` to the ToDo List. 
You can get the command help using the `--help` with `add` command like below.

```
> python main.py add --help
Usage: main.py add [OPTIONS]

Options:
  --name TEXT         [required]
  --category TEXT     [required]
  --priority INTEGER  [default: 3]
  --help              Show this message and exit.
>
```

As you can see, `add` command takes three options. `name` (Todo Name), `category` and `priority`
The Todo `Name` and `Category` are mandatory options. `priority` is optional by default the `priority` is `3`

To add a Todo to Todolist use
```
> python main.py add --name="Complete the Todo list Project" --category="Projects" --priority=2 
Adding 'Name:Complete the Todo list Project, Category:Projects, Priority:2' to To-Do List
   
                                                   📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                           ┃ Category ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Complete the Todo list Project │ Projects │    2     │   ❌   │ 2022-05-24T00:42:19.381913 │              │
└────────┴────────────────────────────────┴──────────┴──────────┴────────┴────────────────────────────┴──────────────┘
>

```
