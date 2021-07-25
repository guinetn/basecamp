## DATA CLASSES 

# Quickly create objects that represent data and compare them, order them, print them, freeze them 

- https://www.youtube.com/watch?v=vBH6GRJ1REM&t=328s
- https://www.youtube.com/watch?v=vRVVyl9uaZc


## BEFORE DATA CLASSES

class Person:
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(id(person2))          # 44985214552
print(id(person3))          # 44985214512
print(person1)              # <__main__.Person object at 0x14B58E5>
print(person3 == person2)   # False


## AFTER DATA CLASSES

# 1. dataclass = can remove  __init__ constructor
from dataclasses import dataclass
@dataclass
class Person:
    name: str
    job: str
    age: int
   
person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)              # Person(name='Geralt', job='Witcher', age=30)
print(id(person2))          # 44985214552
print(id(person3))          # 44985214512
print(person3 == person2)   # TRUE


# 2. Comparing
from dataclasses import dataclass
@dataclass(order=True)
class Person:    
    name: str
    job: str
    age: int
    
person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
print(person1 > person2)  # False  (clss hash)

# 3. Sorting
from dataclasses import dataclass
@dataclass(order=True)
class Person:
    sort_index: int = field(init=False)   #  Sorting
    name: str
    job: str
    age: int
    strength: int = 100   # Default values

    def __post_init__(self):
        object.sort_index = self.age

print(person1)              # Person(sort_index=30, name='Geralt', job='Witcher', age=30)
person1 = Person("Geralt", "Witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)
print(person1 > person2) # True


# repr=False to avoid to print the sort_index with the object
@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)   
print(person1)              # Person(name='Geralt', job='Witcher', age=30)


# 4. Default values
from dataclasses import dataclass
@dataclass(order=True)
class Person:
    sort_index: int = field(init=False, repr=False)   #  Sorting and comparing
    name: str
    job: str
    age: int
    strength: int = 100   # Default values

    def __post_init__(self):
        object.sort_index = self.age

person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

print(person1)
print(id(person2))
print(id(person3))
print(person3 == person2)
print(person1 > person2)

# 5. Creating read-only (frozen) objects
from dataclasses import dataclass, field

@dataclass(order=True,frozen=False)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        # ❌ object.sort_index = self.age  # cause frozen cannot be changed!
        object.__setattr__(self, 'sort_index', self.age) 

person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)
person1.age = 14 # cannot, frozen object!

print(person1)
print(id(person2))
print(id(person3))
print(person3 == person2)
print(person1 > person2)

# 6.  String representation of data

@dataclass(order=True,frozen=False)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.age) # cause frozen cannot be changed!

    def __str__(self):
        return f'{self.name}, {self.job} ({self.age})'

person1 = Person("Geralt", "Witcher", 30, 99)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)
person1.age = 14 # cannot, frozen object!

print(person1)
print(id(person2))
print(id(person3))
print(person3 == person2)
print(person1 > person2)



import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint
import attr


## 1. MANUAL

class ManualComment:
    def __init__(self, id: int, text: str):
        self.id: int = id
        self.text: str = text

    def __repr__(self):
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented

## 2. WITH DATACLASS: create le, ge,gt...

@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


@attr.s(frozen=True, order=True, slots=True)
class AttrComment:
    id: int = 0
    text: str = ""


def main():
    comment = Comment(1, "I just subscribed!")
    # comment.id = 3  # can't immutable
    print(comment)
    print(dataclasses.astuple(comment))
    print(dataclasses.asdict(comment))
    copy = dataclasses.replace(comment, id=3)
    print(copy)

    pprint(inspect.getmembers(Comment, inspect.isfunction))











              
## more

- https://medium.com/@dr-bruce-cottman/twelve-dataclass-examples-for-better-python-code-d1318f362d93?source=email-d34df8fefae2-1619917329596-digest.reader------2-71------------------18bf3841_cdb9_4fb3_8abe_774bacfcfdbe-27-62736a19_0aef_4828_ad07_c7a217634093----&sectionName=icymi