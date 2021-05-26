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

#

## Project Structure 
```bash
.
├── poetry.lock
├── pyproject.toml
├── README.md
├── llm
│   └── __init__.py
│   └── main.py
└── tests
    ├── __init__.py
    └── llm.py
```


