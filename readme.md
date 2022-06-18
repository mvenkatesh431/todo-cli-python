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

> You can use alias `python main.py` as `todo`, So that we can save few keystroke.
> use - `alias todo="python main.py"`

> We are going to use above `todo` alias throughout this readme. 

## `add` Command:

The `add` command used to add a `todo` to the ToDo List. 
You can get the command help using the `--help` with `add` command like below.

```
$ todo add --help
Usage: main.py add [OPTIONS]

Options:
  -n, --name TEXT         [required]
  -c, --category TEXT     [required]
  -p, --priority INTEGER  [default: 3]
  --help                  Show this message and exit.
$
```

As you can see, `add` command takes three options. `name` (Todo Name), `category` and `priority`
The Todo `Name` and `Category` are mandatory options. `priority` is optional by default the `priority` is `3`

To add a Todo to Todolist use

```
$ todo add -n "Finish To-Do Project" -c "Tech" -p 2
                                              📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech     │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │     None     │
└────────┴──────────────────────┴──────────┴──────────┴────────┴────────────────────────────┴──────────────┘
$

```
As you can see it will create a Todo and marks the status as not completed and displays a beautiful table like above.
Lets add few more `todos` to the todolist.

```
$ todo add -n "Buy Milk" -c "Household" -p 3
                                              📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category  ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech      │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │     None     │
│   2    │ Buy Milk             │ Household │    3     │   ❌   │ 2022-06-19 00:02:11.940757 │     None     │
└────────┴──────────────────────┴───────────┴──────────┴────────┴────────────────────────────┴──────────────┘
$
```

## `list` command:

You can list all the todos using the `list` command. 
```
$ todo list
                                                📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │     None     │
│   2    │ Buy Milk             │ Household     │    3     │   ❌   │ 2022-06-19 00:02:11.940757 │     None     │
│   3    │ Go for a Walk        │ Health        │    1     │   ❌   │ 2022-06-19 00:03:16.649111 │     None     │
│   4    │ Watch TV             │ Entertainment │    5     │   ❌   │ 2022-06-19 00:03:30.540819 │     None     │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │     None     │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │     None     │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴──────────────┘
$

```

## `complete` command:

We can mark any `todo` by using the `complete` command. We need to pass the serial number of the `todo` to the `complete` command.

**Usage**
```
$ todo complete --help
Usage: main.py complete [OPTIONS] POSITION

Arguments:
  POSITION  [required]

Options:
  --help  Show this message and exit.
$
```

To mark any todo as complete, use `todo complete <position>`

```
$ todo list
                                                📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │     None     │
│   2    │ Buy Milk             │ Household     │    3     │   ❌   │ 2022-06-19 00:02:11.940757 │     None     │
│   3    │ Go for a Walk        │ Health        │    1     │   ❌   │ 2022-06-19 00:03:16.649111 │     None     │
│   4    │ Watch TV             │ Entertainment │    5     │   ❌   │ 2022-06-19 00:03:30.540819 │     None     │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │     None     │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │     None     │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴──────────────┘
$
$ todo complete 2     
                                                       📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃        Completed at        ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │            None            │
│   2    │ Buy Milk             │ Household     │    3     │   ✅   │ 2022-06-19 00:02:11.940757 │ 2022-06-19 00:10:05.040789 │
│   3    │ Go for a Walk        │ Health        │    1     │   ❌   │ 2022-06-19 00:03:16.649111 │            None            │
│   4    │ Watch TV             │ Entertainment │    5     │   ❌   │ 2022-06-19 00:03:30.540819 │            None            │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │            None            │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │            None            │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴────────────────────────────┘
$ todo complete 4
                                                       📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃        Completed at        ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │            None            │
│   2    │ Buy Milk             │ Household     │    3     │   ✅   │ 2022-06-19 00:02:11.940757 │ 2022-06-19 00:10:05.040789 │
│   3    │ Go for a Walk        │ Health        │    1     │   ❌   │ 2022-06-19 00:03:16.649111 │            None            │
│   4    │ Watch TV             │ Entertainment │    5     │   ✅   │ 2022-06-19 00:03:30.540819 │ 2022-06-19 00:10:10.319548 │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │            None            │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │            None            │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴────────────────────────────┘
$
```
We also update the `Completed at` feild based on the completion time.

## `update` command:

We can update any `todo` using the `update` command. We need to pass the `position` of the todo item to update for the `update` command. 
We can update todo iteam `name`, `category` and `priority`. 

**Usage**:
```
$ todo update --help
Usage: main.py update [OPTIONS] POSITION

  ex: python main.py update 4 --name="Complete To-do project"
  --category='Python'  --priority=1

Arguments:
  POSITION  [required]

Options:
  -n, --name TEXT
  -c, --category TEXT
  -p, --priority INTEGER
  --help                  Show this message and exit.
$
```

As you can see the `position` is the mandatory argument and remaining options are Optional.
Lets update a todo task using the `update` command.

```
$ todo list
                                                       📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃        Completed at        ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │            None            │
│   2    │ Buy Milk             │ Household     │    3     │   ✅   │ 2022-06-19 00:02:11.940757 │ 2022-06-19 00:10:05.040789 │
│   3    │ Go for a Walk        │ Health        │    1     │   ❌   │ 2022-06-19 00:03:16.649111 │            None            │
│   4    │ Watch TV             │ Entertainment │    5     │   ✅   │ 2022-06-19 00:03:30.540819 │ 2022-06-19 00:10:10.319548 │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │            None            │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │            None            │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴────────────────────────────┘
$
$ todo update 3 --name "Go for a Run" -p 2
                                                       📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃        Completed at        ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │            None            │
│   2    │ Buy Milk             │ Household     │    3     │   ✅   │ 2022-06-19 00:02:11.940757 │ 2022-06-19 00:10:05.040789 │
│   3    │ Go for a Run         │ Health        │    2     │   ❌   │ 2022-06-19 00:03:16.649111 │            None            │
│   4    │ Watch TV             │ Entertainment │    5     │   ✅   │ 2022-06-19 00:03:30.540819 │ 2022-06-19 00:10:10.319548 │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │            None            │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │            None            │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴────────────────────────────┘
$
```

> As you can see We have updated the `todo task` at position `3` and changed the `name` and `priority`.

## `delete` command:
We can delete a `todo` using the `delete` command. We need to pass the `position` of the item to `delete` command.

**Usage**
```
$ todo delete --help
Usage: main.py delete [OPTIONS] POSITION

Arguments:
  POSITION  [required]

Options:
  --help  Show this message and exit.
$
```

Let's delete the completed `todos` using the `delete` command.

```
$ todo list
                                                       📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃        Completed at        ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │            None            │
│   2    │ Buy Milk             │ Household     │    3     │   ✅   │ 2022-06-19 00:02:11.940757 │ 2022-06-19 00:10:05.040789 │
│   3    │ Go for a Run         │ Health        │    2     │   ❌   │ 2022-06-19 00:03:16.649111 │            None            │
│   4    │ Watch TV             │ Entertainment │    5     │   ✅   │ 2022-06-19 00:03:30.540819 │ 2022-06-19 00:10:10.319548 │
│   5    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │            None            │
│   6    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │            None            │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴────────────────────────────┘
$
$ todo delete 2     
                                                       📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category      ┃ Priority ┃ Status ┃         Created at         ┃        Completed at        ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech          │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │            None            │
│   2    │ Go for a Run         │ Health        │    2     │   ❌   │ 2022-06-19 00:03:16.649111 │            None            │
│   3    │ Watch TV             │ Entertainment │    5     │   ✅   │ 2022-06-19 00:03:30.540819 │ 2022-06-19 00:10:10.319548 │
│   4    │ Grab Dinner          │ Household     │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │            None            │
│   5    │ Start New Project    │ Tech          │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │            None            │
└────────┴──────────────────────┴───────────────┴──────────┴────────┴────────────────────────────┴────────────────────────────┘
$ todo delete 3
                                              📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category  ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech      │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │     None     │
│   2    │ Go for a Run         │ Health    │    2     │   ❌   │ 2022-06-19 00:03:16.649111 │     None     │
│   3    │ Grab Dinner          │ Household │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │     None     │
│   4    │ Start New Project    │ Tech      │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │     None     │
└────────┴──────────────────────┴───────────┴──────────┴────────┴────────────────────────────┴──────────────┘
$
```

As you can see the two todo items are deleted from the todo list.

## `version` command:
We can check the version of the `todo list` using the `version` command.
```
$ python main.py version 
Version: 1.0.0
$
```

## `clear` command:
We can **delete** all todo tasks from the Todo list using the `clear` command. 
We are going to display the warning and ask for confirmation from the user before deleting all Todos. User can `abort` the operation by pressing `N/n`.

```
$ todo list
                                              📝 Todo List ! 🗒️
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ S. No. ┃ Name                 ┃ Category  ┃ Priority ┃ Status ┃         Created at         ┃ Completed at ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│   1    │ Finish To-Do Project │ Tech      │    2     │   ❌   │ 2022-06-18 14:33:20.534046 │     None     │
│   2    │ Go for a Run         │ Health    │    2     │   ❌   │ 2022-06-19 00:03:16.649111 │     None     │
│   3    │ Grab Dinner          │ Household │    2     │   ❌   │ 2022-06-19 00:03:40.064016 │     None     │
│   4    │ Start New Project    │ Tech      │    4     │   ❌   │ 2022-06-19 00:03:52.490584 │     None     │
└────────┴──────────────────────┴───────────┴──────────┴────────┴────────────────────────────┴──────────────┘
$
$ todo clear
Deleting all To-do's !!!
Are you sure you want to delete all To-Dos? [y/N]: n
Aborted!
$ todo clear
Deleting all To-do's !!!
Are you sure you want to delete all To-Dos? [y/N]: y
All To-Dos were removed
$ todo list
There are no tasks in the to-do list yet
$
```

## License:
GPL-2.0 license - @mvenkatesh431