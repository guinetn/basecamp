# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# by convention, we give classes PascalCase names
# class: common properties to a group of object (moule) attributs method Fonction in the class First arg MUST BE 'self' (reference to the instance)

# Create class
class User:
  pass        # pass in python means "do nothing"

# creating an instance of User
egclass = FirstClass()
print( type(egclass))     # instance
print( type(User))        # classobj

# Create class
class User:

  kind = 'zzz'  # Class variable shared by all instances.
  # Constructor (magic methods)
  def __init__(self, name, email, age):   # method called when the object is created (constructor)
  # def __init__(self, name=None, email=None, age=None):
    self.name = name     # Instance variable unique to each instance.
    self.email = email
    self.age = age

  # A function inside a class is called as a "Method" of that class
  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1

  def __str__(self):   #  method called when a string representation is asked (print)
    return "User [%s, %i]" % (self.name, self.age)


joe = User('joe', 'joe@mail.com", 26)  # __init__ called
print("%s" % joe)  # __str__ called


# Define Static Method: called by an instance of a class or by the class itself
class person:
  @staticmethod
  def greet():
      print("Hello!")
person.greet()        
p1=person()
p1.greet()


# Examine a class
# dir( ) function comes very handy in looking into what the class contains and what all method it offers
dir(User)  #  ['__doc__', '__init__', '__module__']
dir(joe)  #  ['__doc__', '__init__', '__module__', 'name', 'email', 'age']


# Extend class
# class parent:
#    statements                  
# class child(parent):
#    statements

class Customer(User):
  # Constructor
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance

  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

#  Init user object
brad = User('Brad Traversy', 'brad@gmail.com', 37)
# Init customer object
janet = Customer('Janet Johnson', 'janet@yahoo.com', 25)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())



class MyCustomError(Exception):
    """Example of MyCustomError exception."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        


# Multiple Inheritance
'''
https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

Some classes may derive from multiple classes. This means that the derived class would have
its attributes, along with the attributes of all the classes that it was derived from.
'''
class CalendarClock(Clock, Calendar):
  pass

  

import threading
class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = BuckysMessenger(name='Send out messages')
y = BuckysMessenger(name='Receive messages')
x.start()
y.start()



PROPERTIES:  (@property) are much cleaner than getters and setter
GET/SET: property decorator

- code that retrieves the value of temperature will automatically call get_temperature() 
instead of a dictionary (__dict__) look-up. 
- code that assigns a value to temperature will automatically call set_temperature()
- actual temperature value is stored in the private _temperature variable. 
- The temperature attribute is a property object which provides an interface to this private variable.


class A:

  def __init__(self, some)
    self._b = some

  def get_b(self):
    return self._b

  def set_b(self, val):
    self._b = val

a = A(‘123’)
print(a.get_b())
a.set_b(“444”)

Now compare this with a code written using Python-style properties:

class A:

  def __init__(self, some)
    self._b = some

  @property
  def b(self):
    return self._b

  @b.setter
  def b_setter(self, val):
    self._b = val

A = A(‘123’)
print(a.b)
a.b = ‘123’



# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300





# @[decorator_function_name] syntax to specify a decorator (a function that receives another function as argument)
# A decorator is a function that receives another function as argument. The behaviour of the argument function is extended by the decorator without actually modifying it.
def mydecoratorfunction(some_function): # function to be decorated passed as argument
    def wrapper_function(): # wrap the some_function and extends its behaviour
        # write code to extend the behaviour of some_function()
        some_function() # call some_function. some_function is a function whose behaviour we want to extend.
        return wrapper_function # return wrapper function

def display(str):
    print(str)
def displaydecorator(fn):
    def display_wrapper(str):
        print('Output:', end=" ")  # Output: Hello World
        fn(str)
    return display_wrapper
out = displaydecorator(display)
out('Hello World')

@displaydecorator  # Apply @displaydecorator decorator: call display() function to get the extended behaviour
def display(str):
    print(str)
display('Hello World') 
#Output: Hello World
#   \___ extended behaviour applied ("Output:")


# @property built-in decorator for the property() function
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
coldest_thing = Celsius(-300)


# @classmethod decorator: to call that method using the class name instead of the object.
class person:
  totalObjects=0
  def __init__(self):
      person.totalObjects=person.totalObjects+1

  @classmethod
  def showcount(cls):  # cls parameter refers to the person class
      print("Total objects: ",cls.totalObjects)

p1=person()
p2=person()
person.showcount()
# Total objects: 2
p1.showcount()
# Total objects: 2




class Set:
  # these are the member functions
  # every one takes a first parameter "self" (another convention)
  # that refers to the particular Set object being used

  def __init__(self, values=None):
    """the constructor, called when you create a new Set.  
    s1 = Set() # empty set
    s2 = Set([1,2,2,3]) # initialize with values"""
    self.dict = {} # each instance of Set has its own dict property
    
    # which is what we'll use to track memberships
    if values is not None:
      for value in values:
        self.add(value)

  def __repr__(self):
    """this is the string representation of a Set object
    if you type it at the Python prompt or pass it to str()"""
    return "Set: " + str(self.dict.keys())

  # we'll represent membership by being a key in self.dict with value True
  def add(self, value):
    self.dict[value] = True

  # value is in the Set if it's a key in the dictionary
  def contains(self, value):
    return value in self.dict

  def remove(self, value):
  del self.dict[value]


s = Set([1,2,3])
s.add(4)
print s.contains(4) # True
s.remove(3)
print s.contains(3) # False







# COMPARE OBJECTS

compare two objects using ‘==’ operator

If a class doesn’t provide __eq__ method, Python will compare two objects and return True value only if both two objects are actually the same object:

class A:

  def __init__(self, i):
  self.i = i

a = A(1)
b = a
c = A(1)

a == b # True
a == c # False
In this example, objects a and c are False, even though they store the same value inside.

If you want to enable your own comparison logic for two objects and use a == operator, you can implement __eq__ method:

class Car(object):

  def __init__(self, horse_power, color):
    self.horse_power = power
    self.color = color

  def __eq__(self, other):
    if self.horse_power == other.horse_power and self.color == other.color:
      return True
    else:


## Type Annotations (PEP 526)
https://www.python.org/dev/peps/pep-0526

Python has dynamic types: don’t have to specify the type of a variable, you just use variables as labels for containers of data. But in bigger projects, having types is helpful.

def some_function(param_name : typename) -> return_type_name:
    ...  # whatever the function does

Type Checking:
Install mypy via pip install mypy and run it:
> mypy . --ignore-missing-imports
Success: no issues found in 1 source file

setup.cfg
  [mypy]
  ignore_missing_imports=true

The typing module adds support for type
https://docs.python.org/3/library/typing.html



from typing import TypedDict
class Movie(TypedDict):
    name: str
    year: int
movie: Movie = {'name': 'Blade Runner', 'year': 1982}




from typing import Optional
class Position:
    MIN_LATITUDE = -90
    MAX_LATITUDE = 90
    MIN_LONGITUDE = -180
    MAX_LONGITUDE = 180

    def __init__(
        self, longitude: float, latitude: float, address: Optional[str] = None
    ):
        self.longitude = longitude
        self.latitude = latitude
        self.address = address

    @property
    def latitude(self) -> float:
        """Getter for latitude."""
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        """Setter for latitude."""
        if not (Position.MIN_LATITUDE <= latitude <= Position.MAX_LATITUDE):
            raise ValueError(f"latitude was {latitude}, but has to be in [-90, 90]")
        self._latitude = latitude

    @property
    def longitude(self) -> float:
        """Getter for longitude."""
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float) -> None:
        """Setter for longitude."""
        if not (Position.MIN_LONGITUDE <= longitude <= Position.MAX_LONGITUDE):
            raise ValueError(f"longitude was {longitude}, but has to be in [-180, 180]")
        self._longitude = longitude


pos1 = Position(49.0127913, 8.4231381, "Parkstraße 17")
pos2 = Position(42.1238762, 9.1649964)


def get_distance(p1: Position, p2: Position) -> float:
    pass      