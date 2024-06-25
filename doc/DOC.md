# Documentation

## Table Of Contents

* [Intruduction](#introduction)
* [Engine](#engine)
  * [Espanso](#espanso)
  * [Runtime](#runtime)
* [Grammar](#grammar)

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