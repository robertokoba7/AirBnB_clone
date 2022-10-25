
AirBnB Clone Project - Console
---

The console is the first part of the AirBnB project assigned to the second sprint for ALX SE Students. It a clone of the AirBnb website and its content in backend and frontend.

The objective of this project is to cover up the basics and fundamental topics of higher programming languages and its applicability in the deployment of webservers.

In this segment we will have the opportunity of creating a command line interpreter with the module `cmd` and respond to it.

Table of content
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

Prerequisites
---
For further installation is necessary to set this program on Ubuntu 20.04 LTS using Ubuntu in VirtualBox.

Environment
---
The console was developed in Ubuntu 20.04LTS using python3 (version 3.8.5)

Installation
---
Follow the following instructions to get a copy of the program and run in your local machine.
   
    * Clone the following repository.
     
      `https://github.com/robertokoba/AirBnB_clone`

    * Run the program

      `./console.py`

Functionalities and contents
---
**File**                                                                                                                                |**Method**                |**Description**
----------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------
[console.py](https://github.com/robertokoba7/AirBnB_clone/blob/master/console.py)
										                                                        | command interpreter      | The starting point of the console functionality
										                                                        |   `quit`                 |  It terminates the console and exit the program
										                                                        |   `help`                 | It give information about the command line
										                                                        |   `<empty line>`         | It loops the console when the user press Enter
										                                                        |   `create`               | It creates a new instance of the BaseModel and saves it to JSON file
										                                                        |   `show`                 | It shows and prints the string representation of the instances created
                                                                                                                                        |   `destroy`              | It deletes an instance based on the class name and id
                                                                                                                                        |   `all`                  | It prints all the string representation of all instances
                                                                                                                                        |   `updates`              | It updates an instance based on the class name and id by adding or updating an attribute
                                                                                                                                        |   `precmd`               | fixes the command line to be interpretable for the console
                                                                                                                                        |   `prepare_dict`         | prepare a string to update an instance usign dictionaries                                                                                                                            |   `preapare_line`        | prepare the string to return an interpretable command line
[base_model.py] (https://github.com/angellovc/AirBnB_clone/blob/master/models/base_model.py)                                            |   Instanciator           | The BaseModel defines all common attributes/methos for other classes
                                                                                                                                        |   `def __init__(self, *args, **kwargs)` |Initialization of BaseModel receiving commands line
                                                                                                                                        |   `def save(self)`                      | It saves new instances and updates attributes to a JSON file
                                                                                                                                        |   `def to_dict(self)`                   | It returns a dictionary containing all keys/values of an instance
                                                                                                                                        |   `def __str__(self)`                   | It prints the string representation of the BaseModel class
[classes that inherits from BaseModel] (https://github.com/robertokoba7/AirBnB_clone/blob/master/models)                                | `user.py`                   | It represents the user
												                                        | `amenity.py`                | It represents the amenity that the user requires
                                                                                                                                        | `city.py`                   | The city to visit
                                                                                                                                        | `place.py`                  | The place to stay
                                                                                                                                        | `review.py`                 | The critic of the place
                                                                                                                                        | `state.py`                   | The state of the city
[file_storage.py] (https://github.com/angellovc/AirBnB_clone/blob/master/models/engine/file_storage.py)                                 | `File Storage`              | It serializes instances to JSON file and deserializes JSON file to instances
                                                                                                                                        | `all`                       | It returns a dictionary of instances and attributes
                                                                                                                                        | `new`                       | It sets the object to a new instance and key into the dictionary
                                                                                                                                        | `save`                      | It serializes the dictionary to the JSON file
                                                                                                                                        | `reload`                    | It deserializes the JSON file to a directory

Test
---
You will be able to see the different tests and emphasis on certain methods, e.g: Creation of directories, instantiation, creation of classes and attributes, etc

**File**                                                                                                                                 |**Method**                  |**Description**
-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------|--------------------------------[tests_console.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/console.py)                                          |Test for the console              | Checks how well the instantiation works
													                                 | `test_base_pep8_conformance_console` | Test that we conform to PEP8
                										                                         | `base_pep8_conformance_consoletest`  | Test that we conform to PEP8 of the test itself
[test_base_model.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_base_model.py)                     | Test for the BaseModel Instantiator | Checks how well the instantiation works
                              										                                 | `test_base_pep8_conformance_model`  | Test that we conform to PEP8
                                                                                                                                         | `base_pep8_conformance_basemodeltest` | Test that we conform to PEP8 of the test itself
                                                                                                                                         | `instances`                           | test instances creation
                                                                                                                                         | `test_time_attributes`                | it tests the attribute of time
                                                                                                                                         | `test_id_assignment`                  | it tests the id assignment
                                                                                                                                         | `test_to_dict`                        | tests dictionary instance
                                                                                                                                         | `test__str__`                         | tests the printing
                                                                                                                                         | `test_save`                           | tests the save instances
[test_models/] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models)                                              | `test for classes`                    | these tests checks for the same actions but the different attributes, they tend to be the same
[tests_city.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_city.py)                                | `test city`                           | tests Attr: name, state_id
[tests_place.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_place.py)                              | `test place`                          | tests attr: city_id,user_id, name, description, number_rooms,number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
[tests_state.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_state.py)                              | `test state`                          | test attri: name
[tests_review.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_review.py)                            | `tests review`                        | tests attr: place_id, user_id, text
[tests_user.py] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_user.py)                                | `test user`                           | tests attr: email, password, first_name, last_name
[tests_file_storage.py	] (https://github.com/robertokoba7/AirBnB_clone/blob/master/tests/test_models/test_engine/test_file_storage.py)  | `test for FileStorage class` | This test will test the storage of info in json files
																	 | `test_all_dict_returned`     | test the method all when returns dict
																	 | `test_file_storage_exist`    | Checks if methods exists
																	 | `test_new`                   | test the method new at the creation of new object
                															 | `test_User_saveStorage`      | Checks if the save function works
																	 | `test_save`                  | Test that save properly saves objects to file.json
																	 | `test_BaseModel_saveStorage`
| Checks if the save function works
																	 | `test_base_pep8_conformance_file_storage`  | Test that we conform to PEP8
																         | `test_base_pep8_conformance_filesto_test`  | Test that we conform to PEP8 of the test itself

