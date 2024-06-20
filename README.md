# EspScript

EspScript is a in-place command expander

## How it works

EspScript replaces a command with the result of its execution

For example, `!r '123' 32;` -> `123123123123123`

**Note:** EspScript relies on [Espanso](https://espanso.org/) text expansion engine to recognize commands, so it must be installed on your computer in order for EspScript to work properly

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

**Note:** Use python interpretor from the virtual environment

## Syntax

Every script begins with `!` followed by a command name, a list of arguments and `;` at the end

Arguments are separated with spaces, strings containing spaces must be surrounded with single quotes

Double quotes must be escaped with `\`

```espscript
!cmd-name 'string \"arg\"' arg;
```