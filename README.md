# AirBnB_clone - console
## Description

this is a project inspired by the AirBnB application and aims to carry out a complete web project which is divided into 4 steps:

* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

* A website (the front-end) that shows the final product to everybody: static and dynamic.

* A database or files that store data (data = objects).

* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).


In this project we develop the first step, Write a command interpreter to manage your AirBnB objects.

### The console
* create your data model
* manage (create, update, destroy, etc) objects via a console / command interpreter
* store and persist objects to a file (JSON file)ç

# Requirements

## Installation:
Use the  [git clone](https://github.com/moncada92/AirBnB_clone.git) to install this repository
```
git clone https://github.com/moncada92/AirBnB_clone.git

## Usage:
In the file descriptor you will find the definitions of opcode.
* Your console should work like this in interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Authors:
-   [Camilo Moncada](https://github.com/moncada92) - 1665@holbertonschool.com
-   [Andres Miranda ](https://github.com/AMIRANDA9112) - 1642@holbertonschool.com
