# EspScript

EspScript is an in-place command expander

## How it works

EspScript replaces a command with the result of its execution

**Note:** EspScript relies on [Espanso](https://espanso.org/) text expansion engine to recognize commands, so it must be installed on your computer in order for EspScript to work

## Installation

First, clone the repository

```sh
git clone https://github.com/yaz008/EspScript
```

Then create python virtual environment, activate it and run

```sh
pip install -r requirements.txt
```

### Windows

Copy `espscript.yml` file to the Espanso `matches` directory

Replace `[python]` with a path to the python interpreter and `[espscript-main]` with a path to the `src/main.py` file

**Note:** Using python interpreter other than the one from the virtual environment might lead to an error

### Other platforms

Follow the installation instruction for Windows but replace `shell` option with an appropriate shell and change `\"$env:ESPANSO_CMD\"` with the appropriate syntax to adress environmental variables for it