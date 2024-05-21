1. Control flow
	Patterns for code:
	* sequential
	* conditionals
	* iterations
	* store and reuse
	+ break
	+ continue
	+ try
	+ except 
	- The cathedral and the bazaar

2. Data Structures
	+ dir(x) -> shows methods that can be performed by object x.
	+ open(filename, mode) # default mode is read (modes: open, read, write, close)
		- default line reader using for.
		- file.read()
		- line.startswith('bla') 	
		- line.rstrip()
	+ dictionary:
		- get(key, return-value-if-not-found)
		+ IDIOM:
	 	```py
			counts = dict()
			names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
			for name in names:
				counts[name] = counts.get(name, 0) + 1
			print(counts)
	 	```
	 	- keys()
	 	- values()
	 	- items()
	+ tuples:
		+ traverse a sequence in key order:
		```py
			d = {'c': 10, 'b': 1, 'a': 22}
			for k, v in sorted(d.items()):
				print(k, v)
		```
	+ list comprehension!
		eg.
		```py
			c = {'a': 10, 'b': 1, 'c':22}
			print(sorted([ (v, k) for k, v in c.items()],reverse = True))
		```	
3. Regex
	```regex
	^		 		 Matches the beginning of a line
	$		 		 Matches the end of the line
	.		 		 Matches any character
	\s  	 	 Matches whitespace
	\S  	 	 Matches any non-whitespace character
	*		 		 Repeats a character zero or more times
	*?			 Repeats a chatacter zero or more times (non-greedy)
	+		 		 Repeats a character one or more times
	+?			 Repeats a character one or more times (non-greedy)
					 	-Greedy matching gets the largest match / non-greedy the shortest match.
	[aeiou]	 Matches a single character in the listed set
	[^XYZ]	 Matches a single character not in the listed set
	[a-z0-9] The set of characters can include a range (i.e. from a to z or from 0 to 9)
	(		 		 Indicates where string extractions is to start
	)		 		 Indicates where string extraction is to end
	\				 Use a special char as it normally would function (eg. \$ will search for the $ char)
	```
	More info @ https://docs.python.org/3/howto/regex.html

	Module: 
		- re (import re)
	functions:
		- re.findall


13. Data on the web
	Send data, serialize, deseralize, recieve data
	Agreeing on a "wire format"
	Serialization: changing the format of data to a Wire Format.

	+ Extensible Markup Language (XML - one of the "Wire Formats"):
		- Elements (nodes)
		- Primary purpose is to help information Systems share structured data.
		
		SCHEMA:
			XML Document -> Validator <- XML Schema Contract
			Example: https://www.w3schools.com/XML/schema_example.asp
			+ XSD:
				- World Wide Web Consortium (WC3) (https://en.wikipedia.org/wiki/ISO_8601)

				STRUCTURE:
				- xs:element:
					+ xs:tring / xs:date / xs:dateTime / xs:decimal / xs:integer
					+ It is common to represent time in UTC/GMT given that several servers are scattered around the world.
						- 1988-01-28T14:00:00Z
						1988-01-28 - Year-Month-Day
						14:00:00 - Hours:Minutes:Seconds
						Z - Timezone
						(UTC)[http://en.wikipedia.org/wiki/Coordinated_Universal_Time]

				- xs:sequence:
					+ minOccurs / maxOccurs
				- xs:complexType
		
			+ JSON:	
				JSON represents data as neested "lists" and "dictionaries".

			+ Service Oriented Applications

			+ APIs: Application Programming Interfaces
				Google Geo Localisation API
					+: space
					%: comma
					 

14. Object Oriente Definitons and terminology

   	Class - template (or pattern or blueprint) (eg. a cookie cutter)
	Attribute - a variable within a class (or an object property) 
    Method - function that lives in the object or a function whitin a class
    Object - a particular instance of a class (a.k.a. instance)
    Constructor - Code that runs when an object is created
    Inheritance - the ability to extend a class to make a new class (it is a way to reuse code and extend it).
        
    dir(class) => brings all the methods of the class.
    double underscore, is a specially named method.
    self: actual instance.
    
    OBJECT LIFE CYCLE:
	__init__(self): constructor method (initializer).
	__del__(self): destructor method (use it when the object is super complex and uses a lot of resourses).
	
    class chld(parent)

Example:

.. code-block:: python
    
   class PartyAnima:
       def __init__(self, nam):
            self.x = 0
            self.name = nam
            print(self.name, 'constructed')

        def party(self):
            self.x = self.x + 1
            print(self.name,'party count', self.x)

    class FootballFan(PartyAnimal):

        def __init__(self, nam):
            super().__init__(nam)
            self.points = 0

        def touchdown(self):
            self.points = self.points + 7
            self.party()
            print(self.name, 'points', self.ponts)

15. Relational Databases
	- Database: contains many tables
	- Relation (or table): contaings tuuples and attriibutes.
	- Tuple (or row): a set of fields that generally represents an "object" like a person or a music track.
	- Attribute (alsso column or field): one of possibly many elementss of data correspondding to the object represented by the row.

	A relation is defined as a set of tuples that have the same attributes. A tuple usually represents an object and information about that object. Objects are tipically physical objects of concepts. A relation is usually described as a table, which is organized into rows and columns. All the data_referenced by an attribute are in the same domain and conform to the same constraints.

	Database model or database schema (relation rules and attriibutes value specification): structure or format of a database	

	SQL (Structured Query Language) is the language we use to issue commands to the database

		CRUD:
			Create (a table)
			Retrieve (some data)
			Update (data)
			Delete (data)
        
        Roles:
        Data base administrator <> Developer

		DATA ANALYSIS STRUCTURE
    
		Input files ----CLEAN-----> Python <-------SQL------> Database
					   	           Programs                   File
					                   |                       |
	                                   |			           |	
		R	 <----- Output             |                       |
		Excel<-----                    |                      SQL
		D3.js<-----	Files  <-----------|                       |
                                       |                       |
                                       v                       v
                                      YOU <------------> SQLite Browser        
	
	DBA (Data Base Admnistrator)

	CREATE TABLE Users
	INSERT INTO Users ("name","email") VALUES (NULL,NULL);
	DELETE FROM Users WHERE email='aguilacanguro@gmail.com'
	UPDATE Users SET name='Daniel' WHERE email='dcp@hotmail.com'
	SELECT * FROM Users
	SELECT COUNT(*) FROM Counts #Counts the rows in the table Users

	## DESIGNIING A DATA MODEL
		- Draw a picture of the data objects for the app and then figure out how to represent the objects and their
          relationships.
            - start creating the table of the thing that is the most essential. 
            - Convert the logical model into a physical model
                Table
                - Primary key: a unique number (end point of the arrow).
                - Logical key: we might use it in a ORDER BY clause or a WHERE clause.
                - Foreing key: starting point of the arrow. Naming the object_id as the Foreing Key (FK) is a
                  convention.
        - Basic rule: don't put the same string data in twice. Use a relationship instead.
		- Is this column an object or an attribute of another object?
		- Once we define objects, we need to define the relationships between objects.

    ### Data Model
    
    * Every model starts with a schema and a contract.
    

	## Representing a Data Model in tables
		- Primary key: unique number (in all the tables), use to look up a particular row in a table very quickly 
		- Logical key: "we might use this attribute in a where/order clause"
		- Foreign key: connection to another table
		- Ruby on rails name convention (name_id)
		- Use integers as primary keys
		- Model each "object" inthe application as one or more tables
		- Never repeat string data in more than one table in a data model

	## JOIN
		- Links across several tables as part of as part of a select operation.
		- You must tell the JOIN how to use the keys that make the connection between the tables using an ON clause.
		CONSTRUCTION:
			SELECT <atributes from tables> FROM <tablex> JOIN <tabley> JOIN <tablez> ON <how the tables are linked> AND <how the tables are linked> AND...

	## INSERT OR IGNORE // INSERT OR REPLACE

	## Many to Many relationships
	JUNCTION TABLE
		- Generally avoid in a many-to-many junction table:
			* Logical key
			* Autoincrement int value


	## further study
		- indexes
		- Lookups
		- constraints
		- transactions	

sqllite3 - DB - API 2.0 nterffave for SQLite databases:
SQLite is a C library that provides a lightweight disk-based database that doesn't reequire a separatee sserver process and allows accessng the database using a nonstandard variant of the SQL query language. SSome applcatioins can use SQLite for niternal data storage. it's also possible to prototype an applicatoni using SQLte and then port code to a larger database such as PostgreSQL or Oracle.

The sqlite3 mmodule was written by Gerhard Häriing. It provides a SQL interfface commplliant wth the DB-API 2.0 specificatiion described by PEP 249.

To use the module, you mmust first create a Connection object that represents the database. Here the data wlll be stored in the example.db file:

.. code-block:: python

   import sqlite3
   conn = sqlite.connect('example.db')

Once you have a connection, you can create a cursos object and calll its execute() emthod to perform SSQLL commmands:

.. code-block:: python

   c = conn.cursor()
   # Create table
   c.execute('''CREATE table stocks (date text, trans text, symbol text, qty reall, price real)''')

