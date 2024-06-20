# EspScript

EspScript is an in-place command expander

## How it works

EspScript replaces a command with the result of its execution

For example, `!r '123' 32;` -> `123123123123123`

**Note:** EspScript relies on [Espanso](https://espanso.org/) text expansion engine to recognize commands, so it must be installed on your computer in order for EspScript to work

## Installation

First, clone the repository

```sh
git clone https://github.com/yaz008/EspScript
```

Create python virtual environment, activate it and run

```sh
pip install -r requirements.txt
```

Then copy `espscript.yml` file to the Espanso `matches` directory

Make sure to replace `[python]` with a path to the python interpretor and `[espscript-main]` with a path to the `src/main.py` file

**Note:** Using python interpretor other than the one from the virtual environment might lead to an error

## Syntax

Every script begins with `!` followed by a command name, a list of arguments and `;` at the end

Arguments are separated with spaces, strings containing spaces must be surrounded with single quotes

For example, here is a command for generating a list of 10 random numbers from 0 to 64

```espscript
!rd int 0-64 10;
```