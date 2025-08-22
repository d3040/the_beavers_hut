*******************************************************************************
Python Basics
*******************************************************************************

.. contents::
   :depth: 1
   :local:
   :backlinks: entry

A Practical Introduction to Python 3
====================================

    
Strings
-------

* Strings contains *characters*: individual letters or symbols.
* Strings have a *length*: the number of characters conatined in a string.
* Characters in a string appear in a *sequence*: each character has a numbered position in the string.
* `PEP 8` recommends each line of Ptyhon code contain no more tha 79 characters-including spaces. For larger lines use `\\` to break into multiple lines.


Integers
--------

* Underscores can be used to make the numbers more readable eg. 1_000_000 = 1000000.
* Floating-point numbers:
	
  - Can be created in three different ways:
    
    + 1000.0
	+ 1_000.0
	+ 1e3 (E-notation)

  - The maximum float number depends on each system. When the maximum is reached Python returns a special float value: :literal:`inf`.
  - Floating-point representation error: happend due to the way a floating-point number is store in a computers memory (binary representation).

Formatting language
-------------------

To print a number with certain format use the `formatting language <https://docs.python.org/3/library/string.html#format-string-syntax>`_

Functions
---------

One of the most important properties of a function in Python is that functions are values and can be assigned to a variable.

Process of executing a funtcion:

1. the function is called, and any arguments are passed to the function as input.
2. the functions excecutes, and some action is performed with the arguments.
3. the function returns, and the original function call is replaced with the return value.

When a function changes or affects something external to the function itself, it is said to have a *side effect* (eg. print()).

If a function doesn't have a retunr statement, the returned value is :literal:`None`.

The anatomy of a function
^^^^^^^^^^^^^^^^^^^^^^^^^		

- The function signature defines the name of the function and any inputs it expects.
- The function body contains the code that runs every time the function is used.
		
.. code-block:: text

               {----}  <- Parameter list
   def multiply(x, y): <- Function signature
   '''
     Return the product of two numbers x and y.
   '''
   
   # function body
   product = x * y
   
   # Return statement
   return product 		
   

  
Tuples, Lists, and Dictionaries
-------------------------------


Python has three built-in data structures: tuples, lists, and dictionaries:

Tuples (immutable sequences)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- The name comes from mathematics, where it is used to describe a finite ordered sequence of values.
- Empty tuple: a tuple that doesn't contain any values (eg. empty_tuple = ()).
- One value tuple: x = (1,)


Tuples can only create a tuple from another sequences type, like strings. Other similarities: both are sequence types with finite lengths, support indexing and slicing, are immutable, and can be iterated over in a loop. The Main difference with strings is that tuples can be any kinf of value you like, whereas strings can only contain characters.


Lists (mutable sequences)
^^^^^^^^^^^^^^^^^^^^^^^^^

Change several values in a list at once with a slice assignment:


>>> colors = ["blue", "red", "aqua"]
>>> colors[1:3] = ["orange", "magenta"]
>>> colors
['blue', 'orange', 'magenta']


colors[1:3] selects the slots with indices 1 and 2. The list aassigned to a slice does not need to have the same lenght as the slice. When the lenght of the list being assigned to the slice is less than the lentgh of the slice, the overall length of the original list is reduced.


Methods to mutate a list:

* <list>.insert(i, x): i is de index and x the value to insert.
* <list>.pop(i): removes the value from the list at index i. The value removed is returned by the method. If you do not pass a value to .pop(), it removes the last item in the list.
* <list>.append(x): inserts x to the end of the list. append(x) alters the list in place (just like .insert(i, x)).
* <list>.extend(iterable): adds several new elements to the end of a list (also alters the list in place).
* sum([1, 2, 3, 4, 5]) equals 15
* min([1, 2, 3, 4, 5]) equals 1
* max([1, 2, 3, 4, 5]) equals 5
* <list>.sort(key): sorts all of the itmes in ascending order (alphabetical o numerical order). It sorts the list in place, so you don't need to assign it's result to anything. The key parameter can be used to adjust how the list gets sorted, is also accepts a function that based on the return value will sort the list. Important: the function that gets passed to key must only accept a single argument.

  >>> colors = ["red", "yellow", "green", "blue"]
  >>> colors.sort(key=len)
  >>> colors
  ["red", "blue", "green", "yellow"]
  

Copying:
		
- Quirk OOP, when assigning one list to another, both variables refer to the same object, so if one changes the other also changes.
- A variable name is really just a reference to a specific localtion in computer memory.
- To get an independent copy of a list, it can be used the slicing notation. This will return a new list with the same values.
	
Eg.

>>> animals = ["lion", "tiger", "frumious Bandersnatch"]
>>>	large_cats = animals[:]

 
Dictionaries
^^^^^^^^^^^^

- Key-value pairs
- To remove an item from a dictionary use :literal:`del`.
- dictionary.items() method will return a list-like object containing tuples of key-value pair (type called dict_items).
- Only immutable types can be dictionary keys.

Decorators [#]_
---------------

Are functions that take another function, and extends the behavior of that function without explicitly modifying that function.

Object-oriented programming
---------------------------

+ Objetc-oriented programming is a method of structuring a program by bundling related properties and behaviors into individual objects.
+ Classes define functions called *methods*, which identify the behaviors and actions that an object created from the class can perform with its data.
+ Python class names are written in CapitalizedWords notation by convention.
+ The first parameter in a method will always be a variable called self.
+ Attributes created in :literal:`.__init__()` are called instance attributes.
+ Instance methods are functions that are defined inside of a class and can only be called from an instance of that class.
+ When creating your own classes, it's a good idea to have a method that returns a string containing useful informatión about an instance of the class. To do this, use :literal:`__str__()` dunder method.
+ Inheritance is the process by which one class takes on the attributes and methods of another.
+ Child classes can override or extend the attributs and methods of a parent class.
+ To create a child class, you create a new class with its own name and then put the name of the parent class in parentheses.
+ :literal:`isinstance(object, class)` is a function that tells if an object is also an instance of a certain class.
+ You can acces the parent class from inside a method of a child class by using :literal:`super()`. It does much more than just search the parent class for a method or an attribute. It traverses the entire class hierarchy for a matching method or attribute. If you aren't careful, :literal:`super()` can have surprising results.
+ Managing attributes with python's :literal:`property()`:
		
  - The pythonic way to avoid getter and setter methods.
  - Convert Class attributes into properties (managed attributes).
  - built-in function.
  - implemented in C (to ensure optimal performance).
  - property() commonly referred to as a function but it is a class designed to work as a function.



Conventions
-----------

`PEP 8` recommends indenting with four spaces.

Rules for valid variable names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Avoid decorated characters (eg. é, ü, ...).
* Descriptive names are beeter tha short names, but make them less than 3 or 4 words long.
* Write variables in _snake_case_(as `PEP 8` sugests): every word is lower case and separated by an underscore. Another commonly used sintax is camelCase.

Comments
^^^^^^^^

* Begin lines with the # character. comments that start on a new line are called block comments while in-line comments, are comments that appear on the same line as some code.
* According to `PEP 8`, comments shouls always be written in complete sentences with a sigle space between de # and the first word of the comment.
* For in-lines comments, `PEP 8` recomends at least two spaces between the code and the # symbol.
* Use comments only when they add value to your code by make it easier to understand why something is done a certain way. Comments that describe *what* something does can often be avoided by using more descriptive variable names.

Operations
^^^^^^^^^^

* Hierarchy (PEMDAS):

  1. Parentheses
  2. Exponents
  3. Multiplication & Division (left to right)
  4. Addition & Subtraction (left to right)


- Addition :literal:`+`
- Substraction :literal:`-`
- Multiplication :literal:`*`
- Division :literal:`/`
- Integer division :literal:`//`
- Exponents :literal:`**`
- Modulus operator :literal:`%`

|

  If operators with different priorities are used, 
  consider adding whitespace around the operators 
  with the lowest priority(ies). Use your own judgment; 
  however, never use more than one space, and always 
  have the same amount of whitespace on both sides of a binary operator.

  -- PEP 8


Build-in functions
^^^^^^^^^^^^^^^^^^

+ :literal:`type()`: returns the data type of a variable or value.
+ :literal:`len()`: returns the length of a string or list.
+ :literal:`int()`: converts a string into integer.
+ :literal:`float()`: converts a string intp numbers with decimal point.
+ :literal:`str()`: converts a number into a string.
+ :literal:`round()`: round a number to its nearest integer. Has unexpected behavior when the number ends in .5 due Python uses the "rounding ties to even" rounding strategy.
+ :literal:`abs()`: absolute value.
+ :literal:`pow()`: different from ** because it can use a third argument computing the modulus of the result from raising a number to a certain power. i.e. ((x ** y) % z).


Build-in number data types
^^^^^^^^^^^^^^^^^^^^^^^^^^

+ integers
+ floating-point numbers
+ complex numbers


Useful Methods
^^^^^^^^^^^^^^

+ :literal:`<str>.lower()`: converts all letters from string to lower case.
+ :literal:`<str>.upper()`: converts all letters from string to upper case.
+ :literal:`<str>.rstrip()`: removes white spaces from the right side of a string.
+ :literal:`<str>.lstrip()`: removes white spaces from the left side of a string.
+ :literal:`<str>.strip()`: removes white spaces from both sides of a string.
+ :literal:`<str>.startswith(string)`: string starts with given string (this method is case sensitive).
+ :literal:`<str>.endswith(string)`: string ends with given string (this method is case sensitive).
+ :literal:`number.is_integer()`: verify if the number is integral -meaning it has no fractional part-.
+ :literal:`<str>.split(<separator>)`:
+ :literal:`random.choice(list)`: randomly select an item from the list given.

Scope
^^^^^

LEGB rule: Local, Enclosing, Global, Built-in

Logical Operators
^^^^^^^^^^^^^^^^^

+ and
+ or
+ not
  
  
Order of precedence for logical operators:

1. <, <=, ==, >=, >
2. not
3. and
4. or

Grouping expressions with  parentheses is a great way to clarify which operators belogn to which part of a compound expression.


Handling errors
^^^^^^^^^^^^^^^

Built-in exception types:

- ValueError: operation encounters an invalid value (e.g. int("not a number")).
- TypeError: operation is performed on a value of the wrong type (e.g. "1" + 2).
- NameError: using a variable name that hasn't been defined yet (e.g. print(does_not_exist)).
- ZeroDivisionError: 1 / 0.
- OverflowError: the result of an arithmetic operation is too large (e.g. pow(2.0, 1_000_000)). *note: integers in Python have unlimited precision. This means that OverflowErrors can oly occur with floating-point numbers.*

When you can predict that a certain exception might occur. Instead of letting the program crash, you can catch the error if it occurs and do something else instead, using :literal:`try` and :literal:`except`.


.. code-block:: python
		
   # one kind of exception
   try:
       number = int( input(" Enter an integer: "))
   except ValueError:
       print(" That was not an integer")
	
   # two or more kinds of exception
   try:
	   number1 = int( input(" Enter an integer: "))
	   number2 = int( input(" Enter another integer: "))
	   print(number1 / number2)
   except (ValueError, ZeroDivisionError):
  	   print("Encountered an error")
	
   # two or more kinds of exception with different explanation.
   try:
       number1 = int( input(" Enter an integer: "))
	   number2 = int( input(" Enter another integer: "))
	   print(number1 / number2)
   except ValueError:
       print(" That was not an integer")
   except ZeroDivisionError:
	   print("number2 must not be 0")



Glossary
--------

IDLE:
  Integrated Development Environment.

global:
  Tells python to look in the global scope for a certain variable. Though, the global keyword is considered bad form in general.

del:
  Used to un-assign a variable from a value.

in:
  Used to check whether or not a value is contained in a tuple.

Packing/Unpacking:
  Make multiple variable assignments in a single line. Eg. name, age, occupation = "Daniel", 32, "programmer".

Immutable:
  The values previously created cannot be changed.

Sequence:
  An ordered list of values.

Data structure:
  Models a collection of data.

Lexicographic ordering:
  Strings ordered as the would appear in a dictionary.

Refactoring:
  The process of re-writing existing code to be cleaner, easier to read and understand, or adhere to code standards set by a team.

Debugger:
  A tool that helps you hunt down bugs and understand why the are happening.

Debugging:
  Removing bugs.

Logic errors:
  Cause unexpected behaviors called bugs. Logic errors occur when an otherwise valid program doesn't do what was intended.

Pythonic:
  It is generally used to describe code that is clear, concise and uses Python's built-in features to its advantage.

Rounding ties to even:
  A tie is any number whose last digit is a 5. When you round ties to even, you first look at the digit one decimal place to the left to the last digit in the tie. If that digit is even, you round down. if the digit is odd, you round up. This is a round strategy recommended for floating-point numbers by the IEEE because it helps limit the impact rounding has on operations involving lots of numbers.

Off-by-one error:
  Forgetting that counting starts with zero and trying to access the first character in a string with the index 1.

Docstrings: 
  Triple-quoted strings used to document code or custom functions. It is a string definition which preserves whitespaces.

Delimiters:
  The quotes surrounding a string.

Fundamental data type:
  Data types that can't be broken down into smaller values of a different type.

Data type:
  The kind of data a value represents.

Fixed-point:
  A number display with the precise number of decimals places specified.

Argument:
  A value that gets passed to the function as input.

Modulus: 
  To calculate the remainder r of dividing a number x by a number y, Python uses the equation r = x - (y * (x // y)).

break:
  Tells python to break out of a loop.

continue:
  Is used to skip any remaining code in the loop body and continue on to the next iteration.

List Comprehension:
  Short-hand for a for loop. Commonly used to convert values in one list to a different type.

Nesting:
  A table is an informal way of thinking about a list o lists (or tuples). While you can use the built in list and tuple type for matrices, better alternative exists.

Class:
  A blueprint for how something should be defined.

Instance:
  An object that is built from a class and contains real data. Creating a new object from a class is called **instantiating** an object.


Useful links
------------

* `What is pip <https://realpython.com/what-is-pip/>`_
* `f-string or formatted string literals <https://realpython.com/python-f-strings/>`_
* `formatting language <https://docs.python.org/3/library/string.html#format-specification-mini-language>`_
* `Pyhton's built-in exceptions <https://docs.python.org/3/library/exceptions.html>`_
* `Finding the Perfect Python Code Editor <https://realpython.com/courses/finding-perfect-python-code-editor/>`_
* `Python args and kwargs: Demystified <https://realpython.com/courses/python-kwargs-and-args/>`_
* `Regular Expressions: Regexes in Python (Part 1) <https://realpython.com/regex-python/>`_
* `Python Inner Functions—What Are They Good For? <https://realpython.com/inner-functions-what-are-they-good-for/>`_
* `Immutability in Python <https://realpython.com/courses/immutability-python/>`_
* `Python Virtual Environments: A Primer <https://realpython.com/python-virtual-environments-a-primer/>`_
* `Setting up Python for Machine learning on Windows <https://realpython.com/python-windows-machine-learning-setup/>`_
* `Copying Python Objects <https://realpython.com/copying-python-objects/>`_

What is Pip?
------------

pip is the standard package manager for Python. It allows you to install and manage additional packages that are not part of the Python standard library. It is included with the Python installer since versions 3.4 for Python 3 and 2.7.9 for Python 2. pip is to python as npm is to JavaScript, gem to Ruby or NuGet to .NET.

Uninstalling Packages
^^^^^^^^^^^^^^^^^^^^^

Before uninstalling a package, make sure to run the `show` command for that pakage. Doing this will show the required packages for that package and required-by package info, then those can be uninstall to.

Adding a `-y` will suppress the file list and confirm the uninstall request.

.. code-block:: python
   :caption: Example

   pip uninstall urllib3 -y
   Uninstalling urllib3-1.24.1
   Successfully uninstalled urllib3-1.24.1

Alternatives to pip
^^^^^^^^^^^^^^^^^^^

1. Conda
2. Pipenv
3. Poetry


venv
----

To keep track of your project's dependencies, you can create a requirements.txt file. To generate this file, run:

.. code-block:: bash

   pip freeze > requirements.txt


To install the dependencies listed in requirements.txt in a new virtual environment, use:

.. code-block:: bash

   pip install -r requirements.txt



.. [#] https://realpython.com/courses/python-decorators-101/

