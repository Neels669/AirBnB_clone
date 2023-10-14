# AirBnB_clone
<ins>**0x00. AirBnB clone - The console**<ins>

This project is the first step towards building my first full web application: the AirBnB clone. The project serves as a command Interpreter developed in Python.

Each task is linked in the below ways:

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.

* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.

* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.

* Create the first abstracted storage engine of the project: File storage.

* Create all unittests to validate all our classes and storage engine.

<ins>**Files**<ins>

**models** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.

**console.py** file is the entry point of our command interpreter.

**models/base_model.py** file is the base class of all our models. It contains common elements:

attributes: id, created_at and updated_at

methods: save() and to_json()

**models/engine** directory will contain all storage classes (using the same prototype) i.e. **file_storage.py.**


<ins>**The Command Interpreter / The console**<ins>

This project serves as a command interpreter to manage the AirBnB objects. 

Command line interpreter that manipulates data and manages serialization and deserialization of objects.

**How to Start**

* The cosole displays the prompt (hbnb) and waits for user input.

* Reads the entered command and the argument.

* Looks for the function of the command.

* Executes the function.

* If the typed command (the function) doesn't exist, the console prints an Error message.

* Quits when the user enters "quit" or "EOF" or presses Ctrl+d.

**How to Use with Examples**

* Creating a New Object e.g user, place, City, etc.

* Listing Objects. E.g Showing User.

* Updating an Object e.g name, value, etc.

* Deleting an Object e.g. a user.

* Counting instances of a class e.g count users 
