
# AirBnB Clone Project - Console
---

The console is the first part of the AirBnB project assigned to the second sprint for ALX SE Students. It a clone of the AirBnb website and its content in backend and frontend.

The objective of this project is to cover up the basics and fundamental topics of higher programming languages and its applicability in the deployment of webservers.

In this segment we will have the opportunity of creating a command line interpreter with the module `cmd` and respond to it.

# Table of content 
---

* [AirBnB Clone Project - Console](https://github.com/robertokoba7/AirBnB_clone#airbnb-clone-project---console)
    * [Prerequisite](https://github.com/robertokoba7/AirBnB_clone#prerequisites)
    * [Environment](https://github.com/robertokoba7/AirBnB_clone#environment)
    * [Installation](https://github.com/robertokoba7/AirBnB_clone#installation)
    * [Functionality and contents](https://github.com/robertokoba7/AirBnB_clone#functionalities-and-contents)
    * [Tests](https://github.com/robertokoba7/AirBnB_clone#tests)
    * [Examples](https://github.com/robertokoba7/AirBnB_clone#examples)
    * [All instances by class name](https://github.com/robertokoba7/AirBnB_clone#all-instances-by-class-name)
    * [Built with...](https://github.com/robertokoba7/AirBnB_clone#built-with)
    * [Authors](https://github.com/robertokoba7/AirBnB_clone#authors)

# Prerequisites
---
For further installation is necessary to set this program on Ubuntu 20.04 LTS using Ubuntu in VirtualBox.

# Environment
---
The console was developed in Ubuntu 20.04LTS using python3 (version 3.8.5)

# Installation
---
Follow the following instructions to get a copy of the program and run in your local machine.
* Clone the following repository.

    `https://github.com/robertokoba7/AirBnB_clone`

* Run the program

    `./console.py`
# Functionalities and contents 
---
File                    | Method                       | Description
------------------------|------------------------------|----------------------
[console.py](https://github.com/robertokoba7/AirBnB_clone/blob/master/console.py) | command interpreter  | The starting point of the console functionality
|                       |  `quit`                      | It terminates the console and exit the program
|                       |  `help`                      | It gives information about a command line
|                       |  `<emptyline>`               | It loops the console when the user presses enter
|                       |  `create`                    | It creates a new instance of the BaseModel and saves it to JSON file
|                       |  `show`                      | It shows and prints the string representation of the instances created
|                       |  `destroy`                   | It deletes an instance based on the class name and id
|                       |  `all`                       | It prints all the string representation of all instances
|                       |  `update`                    | It updates an instance based on the class name and id by adding or updating an attribute
|                       |  `precmd`                    | fixes the command line to be interpretable for the console
|                       |  `prepare_dict`              | prepare a string to update an instance usign dictionaries
|                       |  `prepare_line`              | prepare the string to return an interpretable command line
| [base_model.py](https://github.com/robertokoba7/AirBnB_clone/blob/master/models/base_model.py) |  `Instanciator`  | The BaseModel defines all common attributes/methos for other classes
