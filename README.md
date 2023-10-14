# AirBnB_clone
**0x00. AirBnB clone - The console**

This project is the first step towards building my first full web application: the AirBnB clone. The project serves as a command Interpreter developed in Python.

Each task is linked in the below ways:

* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.

* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.

* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.

* Create the first abstracted storage engine of the project: File storage.

* Create all unittests to validate all our classes and storage engine.

<U> **Files** </U>

**models** directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
tests directory will contain all unit tests.

**console.py** file is the entry point of our command interpreter.

**models/base_model.py** file is the base class of all our models. It contains common elements:

attributes: id, created_at and updated_at

methods: save() and to_json()

**models/engine** directory will contain all storage classes (using the same prototype) i.e. **file_storage.py.**


**The Command Interpreter / The console**

This project serves as a command interpreter to manage the AirBnB objects. 

Command line interpreter that manipulates data and manages serialization and deserialization of objects.

