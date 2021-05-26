# LLM Simple Command Line (CLI) Tool 

A command line program, written in Python with Typer, for macOS/Linux that can create/list/take an order, to simulate a very simple Lalamove.

Specific details found at [here](https://github.com/lalamove/challenge/blob/master/freshgrad.md)

## Setup 
Clone this project onto local environment

Move into project
```bash
$ cd LALAMOVE-Graduate-Tech-Challenge-21/
```

Setup virtual environment 
```bash
$ python3 -m venv ./{env_name}
$ . {env_name}/bin/activate
```

Run setup.sh to install dependencies and initialise CLI tool
```bash
$ ./setup.sh
```

Run the LLM CLI for further instructions
```bash
$ llm
```

## Usage 
`create_order [from] [to]`
returns a unique ID for this order.
from and to are required.

`list_orders`
List all the available (non-taken) orders with this format
`ID,FROM,TO\n`

`take_order [id]`
Try to take the order with the given ID, returns an error if order is already taken.
id is required.

Check out "Interaction Example" section [here](https://github.com/lalamove/challenge/blob/master/freshgrad.md)

## Project Structure 
```bash
.
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
├── setup.sh
├── llm
│   └── __init__.py
│   └── main.py
└── tests
    ├── __init__.py
    └── test_llm.py
```

## Technology Choices and Reasoning
Project is created with following libraries:
* [Poetry](https://python-poetry.org/docs/) version: 1.1.6
* [SQLAlchemy](https://www.sqlalchemy.org/) version: 1.4.15

### Poetry w/ Typer
[Poetry](https://python-poetry.org/docs/) is a easy-to-use tool to package the project and initialise the project structure.

Typer is a library to create quick CLI tools in Python and is built on top of the popular CLI building library [Click](https://click.palletsprojects.com/en/8.0.x/).
CLI commands are routed to command functions in `main.py`.

### SQLite w/ SQLAlchemy
For this simple CLI tool, SQLite is used as it's a lightweight embedded DB that requires no additional setup. When the app is launched, a `orders.db` file is created and holds all DB records to ensure data persistance.

SQLAlchemy is used as a object relationship mapper (ORM) between the app and the SQLite DB. A DB connection or session is established in `./llm/__init__.py` and  SQLAlchemy allows the app to interact with the DB using "Order" objects. 
