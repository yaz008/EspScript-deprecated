# EspScript Manual

## Table Of Contents

* [Introduction](#introduction)
* [Single Commands](#single-commands)
* [Pipelines](#pipelines)

## Introduction

This is a beginner's giude on writing scripts in EspScript

Copy the following text, it will be used as an example input throughout the Manual

```text
Python 2.0 was released on October 16, 2000, with many major new features, including a cycle-detecting garbage collector (in addition to reference counting) for memory management and support for Unicode, along with a change to the development process itself, with a shift to a more transparent and community-backed process
```

And open some text editor (for example, [Google Search Bar](https://www.google.com)) where you can type commands to practice

## Single Commands

To execute a command, type `!` followed by a command name and a list of arguments. Then type `;` in order for Espanso to recognize the pattern and send it to EspScript interpreter

Let's try `!f w;`: this command will give you a list of words in the text

*(`f` is a polymorphic function from `string` package, it finds all matches of given regex pattern; `w` is a regex pattern for english words)*

Let's count the words in this text. There is a special `count` function for that exact purpose: `!c w;`

Even though predefined commands are good for performing simple operations, typing them one by one gets more complicated very rapidly as the complexity of the tasks grows

## Pipelines

Pipeline is a powerful mechanism that allows you to chain together multiple commands in order to perform complex operations in a single line

In EspScript there are 3 types of links between commands. Each of them effects the result in its own special way

The first one is the `pipe` link. To demonstrate it's functionality, let's count the number of words in a different way using the `l` function: `!f w | l;`

*(`l` is a global function from `core` package, it returns the length of any `Sized` object)*

But what if we want to get a list of the lengths of each individual word instead of the length of list? Here comes the `map` link: it applies the given function to every element of the stdin iterable: `!f w ? l;`. The result is exacty the same as before

The last link is the `reduce` link, it applies a given binary predecate to the stdin iterable. For example, we might want to know the overall length of all words: `!f w ? l & +;`. In this example it adds all items in the list obtained via previous command