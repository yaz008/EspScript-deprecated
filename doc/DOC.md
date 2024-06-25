# Documentation

## Table Of Contents

* [Intruduction](#introduction)
* [Engine](#engine)
  * [Espanso](#espanso)
  * [Runtime](#runtime)
* [Grammar](#grammar)
* [Semantics](#sematics)
  * [Filemanip](#filemanip)
  * [Regex](#regex)
* [Standard Library](#standard-library)
  * [Filemanip](#filemanip)
  * [Regex](#regex)
* [Packages](#packages)
  * [Conversion](#conversion)
  * [Core](#core)
  * [Math](#math)
  * [Rand](#rand)
  * [Run](#run)
  * [String](#string)

## Introduction

This document provides a technical description of the EspScript in-line command expander. It is not intended as a beginner's giude. For a step-by-step tutorial, please refer to the [Manual](MAN.md)

## Engine

### Espanso

Espanso scans any text you type and tries to find a special [regex](https://en.wikipedia.org/wiki/Regular_expression) pattern. If it finds a match, it calls EspScript via shell with the matched string as an argument

#### Pattern

A match is any string starting with an `!` followed by any *valid symbol* other than [` `, `!`, `?`], 0 to 27 any *valid symbols* and a `;` at the and

A **valid symbol** is an ASCII symbol other than `"`

*(From this point forward, all references to 'character' or 'symbol' will denote a valid symbol in the EspScript language)*

The `;` symbols in the middle of a command must be escaped with a `\`

### Runtime

A script is a sequence of commands separated by links. Not every matched is a valid script

#### Parsing

Parser divides a given string into chunks. A chunk is a *link*, a *command name* and a *list of arguments*

- **Link** is one of the symbols [`|`, `?`, `&`], it determines the way the command after it applies to the result of a previous one

- **Command Name** is a string of non-space characters

- **List Of Arguments** is a collection of arguments separated by one or more spaces where an argument might be:

  - A string of non-space characters

  - A string of any characters (including spaces) surrounded by `'`

## Grammar

EspScript grammar is pretty simple

```grammar
Script -> Command | Command Commands
Commands -> link Command | epsilon
Command -> name Args
Args -> arg Args | epsilon
```

The terminals in the grammar above are defined as follows

```grammar
Link -> '|' | '?' | '&'
Name -> '[\w]' Name | '[\w]'
Arg -> SimpleArg | QuotedArg
SimpleArg -> '[\w]' SimpleArg | '[\w]'
QuotedArg -> '\'' QuotedArgMiddle '\''
QuotedArgMiddle -> '[^\']' QuotedArgMiddle | epsilon
```

**Note:** `epsilon` denotes an empty string

## Sematics

The language includes 3 types of tokens

- **Command names:** Command names are resolved dynamically at runtime. This is the first step of chinks execution. If name is not found, the execution terminates with an error

- **Arguments:** In EspScript there are 2 types of arguments:

  - **Fixed arguments:** Fixed arguments are quite similar to the command names but they are not resolved dynamically when a script runs. Instead a table of all valid argument values is loaded when corresponding module is imported

  - **Arbitrary arguments:** Their value is being passed into a function as-is

- **Links:** Links are operators. They define how the next function will be applied to the result of a previous one in a pipeline. There are 3 types of links:

  - **Pipe link (|):** Pipe link derictly applies the next function

  - **Map link (?):** Map link appies the next function to every element of the result

  - **Reduce link (&):** Reduce link calls the `reduce` function with the next function as a reducer and the previous result as a sequence

## Standard Library

The runtime and packages both rely on standard library

Standard library includes 2 modules: filemanip and regex

### Filemanip

Filemanip includes 2 functions:

- **load_json:** takes a path relative to `./src` folder and returns a Python object constructed from the file

- **write:** takes an absolute path to the file and content to the file, writes content to the file

### Regex

Regex includes 2 files:

- **patters.json:** a json file with predefined regex patterns

- **patterns.py:** Python file with `patterns.json` loaded into `patterns` dictionary

#### Patterns

- **w:** words
- **n:** numbers
- **e:** emails
- **p:** phones
- **u:** urls
- **id:** valid C-style identifiers
- **mac:** mac adresses
- **uuid:** UUID version 4
- **ver:** semantic versions
- **ip:** IPv4
- **#:** hashtags

## Packages

Packages provide the interface and declare polymorfic functions used in scripts

### Conversion

Provides interface for casting standard types

- **lst:** convert stdin iterable to `list`
- **set:** convert stdin iterable to `set`

- **b:** convert stdin to `bool`
- **i:** convert stdin to `int`
- **fl:** convert stdin to `float`
- **str:** convert stdin to `string`

### Core

Core package includes echo, globals and predicates

#### Echo

Echo includes the `echo` function

- **e:** returns it's arguments separated by spaces

#### Global

Global includes length, minimum and maximum

- **l:** returns number of elements in stdin
- **min:** return the smallest element in stdin
- **max:** return the largest element in stdin

#### Predicates

Predicates includes binary predicates add and mul

- **+:** returns the sum of 2 numbers
- ***:** returns the product of 2 numbers

### Math

Math package includes statistics

#### Statistics

Statistics include 3 functions

- **av:** returns mean of the stdin iterable
- **md:** returns median of the stdin iterable
- **var:** returns variance of the stdin iterable

### Rand

Rand package includes choice

#### Choice

Choice includes one polymorfic function

- **ch:** polymorfic random choice function:
  - **no arguments:** returns a random element of stdin sequence
  - **number:** returns a list of `number` elements of stdin sequence

### Run

Run package allows to run code. It includes Python

#### Python

Python includes 2 functions

- **ev:** evaluates an stdin expression, allows names from Python `math` module
- **run:** runs Python code from stdin *(requires python in the PATH)*

### String

String package includes various functions for string manipulations: finding, counting and substituting patterns

- **count:** return number of matches for a given pattern
- **find:** returns a list of matches for a given pattern
- **repeat:** returns stdin repeated `number` of times. Inserts a separator inbetween if specified
- **replace:** replaces an `old` string with `new`
- **substitute:** substitutes `pattern` with a `replacement` string
