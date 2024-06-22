# EspScript

EspScript is an in-place command expander designed to extend the functionality of [Espanso](https://espanso.org/)

It enables the execution of predefined commands within text fields, substituting commands with their execution results

## Table of contents

* [How It Works](#how-it-works)
* [Installation](#installation)
* [Basics](#basics)
* [Licence](#license)

## How It Works

You simply type a command using EspScript syntax in any place *(Browser, Notepad, VS Code, Word, etc.)*, and it will be replaced with the result

For example, `!rd int 0:2**64;` will be replaced with a random integer from 0 to 2^64

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

**Note:** Using a different Python interpreter than the one within the virtual environment can lead to unexpected errors

### Other Platforms

Follow the same steps as for Windows, but make the following adjustments in `espscript.yml`:

1. **Shell:** Replace the shell option with the appropriate shell for your platform

   - Linux/macOS: `bash`

2. **Environmental Variable Syntax:** Modify the \"$env:ESPANSO_CMD\" to match your shell's syntax for accessing environmental variables

   - Linux/macOS: `$ESPANSO_CMD`

## Basics

Now, when you installed EspScript successfully, it's time to type your first command!

### Syntax Basics

Every command begins with `!` followed by the name, a list of arguments and `;`. The simplest command is `echo`, it outputs whatever it gets as an argument. In EspScript `echo` is shortened to just `e`

Try some code: navigate to any place where you can insert text and type `!e 123;`. You should get `123` back.

Now let's try the classic! To input a string, enclose it in single quotes: `!e 'Hello, World!';`. Now you officially know one more programming language!

### Pipelines

The `echo` command is not completely useless as it might look at the first glance. It is essential for making pipelines. Here is how if works, but first wee need some other command to chain is with `echo` - the `repeat`: it takes an integer as an argument an outputs its `stdin` that many times.

To chain two commands type `|` between them. Try this: `!e repeat | r 10;`

The result is a bit ugly. To fix this, pass `' | '`  as a second argument: `!e repeat | r 10 ' | ';`

Now let's try it with a longer string: `!e 'It is a very long string' | r 10 ' | ';`

Hm, It doesn't do anything... This is because Espanso has a limit of 30 characters for a regex match, and we have exeeded this limit.

### Clipboard

But what if we want a long input anyway? Here comes the Clipboard. The `r` and almost any other command in EspScript takes Clipboard data as stdin by default

Simply copy the string from the previous example and type `!r 10 ' | ';`

And it wokrs! Magic... 

To learn more magical stuff and language features check out the [Manual](doc/manual/MAN.md) or read [Documentation](doc/DOC.md)

## License

EspScript is an open-source software distributed under the [MIT License](LICENSE.txt)

<img src="assets/logo.jpg" alt="Logo" style="height: 400px;"/>