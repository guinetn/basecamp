## COVARIANCE / CONTRAVARIANCE


Covariance preserves assignment compatibility and contravariance reverses it.
Implicit arguments conversion for array types, delegate types, generic type
Class hierarchy flexibility by adding polymorphism features to arrays, delegate types, generic types. 
Provide flexibility for matching a delegate type with a method signature.
Polymorphism extensions to array types, delegate types, generic type



## TERMINOLOGY

co and contra-variances refer to how an object is handled.
"variance": property of operators that act on specified types (ordering of operators)
"co prefix": "along with" and indicates that the operator retains the ordering of types. 
"contra prefix": "against" something and indicates that the operator reverses the ordering of types.






### BEFORE .NET 4


* INVARIANCE: childs are too young to do what parents' are allowed to do

Variable assignments/function arguments can use only the type originally specified: so an invariant generic type parameter is neither covariant nor contravariant.
You can't assign an instance of List<Base> to a variable of type List<Derived> or vice versa.
Generic was not covariant

Invariant types are not able to convert (Invariance)
They are their own type and not related to anything else in the hierarchy.

```c#
IEnumerable<Derived> d = new List<Derived>();
IEnumerable<Base> b = d;  // ❌ failed

List<A> = new List<B>();  // ❌ failed
```

Before c#4 Generic was not covariant (A ← B then T<A> ← T<B>)
Lack of covariance hinder reusability
```c#
class Animals {}    
class Bear : Animal {}
Stack<Bear> bears = new Stack<Bear>();
Stack<Animal> animals = bears; // ❌ compil time error with .net 3.5

void wash(Stack<Animal> animals) {...}
wash(bears); → ❌ compil time error, so:
void wash(Stack<T> animals) where T: Animal {}
```




### WITH .NET 4

covariance for generics and delegate types using in and out key words
	upcast:  Fruit ← Apple
	dncast:  Fruit → Apple

* VARIANCE
Base class and other derived classes are considered to be the same kind of class that adds extra functionalities to the base type. 
.net 4.0 implements variance for generic interfaces and delegates using in and out key words

Variant type are able to convert:	A ← B

Assume a base class named 'Base' and a derived class named 'Derived'

* COVARIANCE: please accept my child

Allows you to use a derived class where a base class is expected
You can use either the type you specified or any type that is more derived
Ability to be more specific by using a more derived type with than initially specified 
Enables variable assignments/function arguments to be more derived type than originally specified.
Method can have more derived arguments/return type: allow to pass a derived type where a base type is expected
Allow to assign an instance of IEnumerable<Derived> to a variable of type IEnumerable<Base>
Allow methods to have a return type that is more derived than that defined in the delegate. 
Can be applied on delegate, generic, array, interface, etc
Preserves assignment compatibility between parent and Child relationship during dynamic polymorphism
covariant types convert from a wider type to narrower type. (ex: from double to float) 

```c#
IEnumerable<Derived> d = new List<Derived>();
IEnumerable<Base> b = d; ✔️ 
```

```c#
using System;
public class Covariance
{
    static void Main()
    {
        object[] langs = {"C#", "Python", "PHP", "Java"}; // covar: accept a more specific type
        Console.WriteLine(langs[0]);
    }
}
```
```c#
interface IElement<out T> {}
class Elements<T>: IElement<T> {}
class a {}
class b:a {}

IElement<b> bs = new Elements<b>();
IElement<a> as = bs;
IElement<object> o = bs;   // covariance: a ← b   List<a> ← List<b>
```

* CONTRAVARIANCE: please accept my parent, i'm like my parent

Ability to be less specific by using a less derived type than initially specified 
Allow to use a more generic (less derived) type than originally specified.
Allow a method with parameters types that are less derived than those in the delegate type.
You can assign an instance of Action<Base> to a variable of type Action<Derived>
Contravariant types convert from a narrower type to a wider type. (ex: short to int) 

C# 4.0: interface IEnumerable<T> is changed to interface IEnumerable<out T> to allow
List<string> sl = new List<string>();
List<object> ol = sl;


```c#
Action<Base> b = (target) => { Console.WriteLine(target.GetType().Name); };
Action<Derived> d = b; ✔️
d(new Derived());
```

```c#

using System;
using System.Collections.Generic;
public class Contravariance
{
    static void Main()
    { 
        Action<string> del = ShowMessage; // contrav: accept a less derived type
        del("Proximity alert");         
    }

    static void ShowMessage(object message) 
    { 
        Console.WriteLine(message);
    }
}		
```


Variance modifiers: out, in
	Allow to mark type parameters as contravariant or covariant
 	Adding in or out whenever you define a type parameter gives you free extra conversions.
	.net 4.0 implements variance for generic interfaces and delegates using in and out key words
	interface System.Collections.Generic.IEnumerable<out T> T is covariant

	'in' word allow generic contravariance (works on parameters)
		object ← string
		List<object> → List<string>

	'out' specifies that the IEnumerable interface is covariant
		public delegate TResult Func<in T, out TResult>(T args);
		Func<object, string> f1 = s=>s.ToString();
		Func<string, object> f2 = s=>s.ToString();


|   HIERARCHY        |     INVARIANCE     |     COVARIANCE      |   CONTRAVARIANCE   |
|--------------------|--------------------|---------------------|--------------------|
|                    |      .Net 4  <     |     .Net 4 >=       |     .Net 4 >=      |   
|                    |                    |                     |                    |   
| Number is derived  |                    |         A ← B       |         A ← B      |   
|      from int:     |                    |      T<A> ← T<B>    |      T<A> → T<B>   |   
|                    |    class Box<T>    |    class Box<out T> |   class Box<in T>  |   
|    Number          |    Box<Number>     |      Box<Number>    |     Box<Number>    |
|      ↑             |       ↑❌↓         |          ↑ ✔️      |         ↓ ✔️       |  
|     int            |    Box<int>        |       Box<int>      |      Box<int>       | 
|                    |                    | accept more derived | accept less derived |   
|                    |                    |  preserves assignment compatibility | accept less derived |   


```c#

// CONTRAVARIANCE (APPLIED TO PARAMETERS): ENABLES TO USE A MORE GENERIC (LESS DERIVED) TYPE THAN ORIGINALLY SPECIFIED
Action<object> broadAction = (object data) => { Console.WriteLine(data); };
Action<string> narrowAction = broadAction;

// COVARIANCE: USE A MORE DERIVED TYPE THAN ORIGINALLY SPECIFIED
Func<string> narrowFunction = () => Console.ReadLine();
Func<object> broadFunction = narrowFunction;

void PrintAnimals(IEnumerabLe<Animal> animals) {
    for (var animal in animals)
        Console.WriteLine(animal.Name);
}

// CONTRAVARIANCE AND COVARIANCE COMBINED
Func<object, string?> func1 = (object data) => data.ToString();
Func<string, object?> func2 = func1;
```



## SAMPLE 

	XMLFile1.xml
	```xml
	<?xml version="1.0" encoding="utf-8" ?>
	<root>
	  <!-- comment 1 -->
	  <foo>foo 1</foo>
	  <bar>bar 1</bar>
	  <!-- comment 2 -->
	  <foo>foo 2</foo>
	  <bar>2</bar>
	  <!-- comment 3 -->
	</root>
	```

	Want to remove all <bar> elements of 'root':

	```xml
	<?xml version="1.0" encoding="utf-8" ?>
	<root>
	  <!-- comment 1 -->
	  <foo>foo 1</foo>
	  <!-- comment 2 -->
	  <foo>foo 2</foo>
	  <!-- comment 3 -->
	</root>
	```

	```cs
	XDocument doc1 = XDocument.Load(@"XMLFile1.xml");
	XDocument doc2 = new XDocument(
	    new XElement(doc1.Root.Name, 
	                 doc1.Root.Nodes().Except(doc1.Root.Elements("bar").Cast<XNode>())));
	doc2.Save(Console.Out);
	```

	***Before .Net 4.0, generic interfaces were invariant:***
	Inheritance: Object → XObject → XNode → XContainer → XElement
	***Error: Cannot convert 
	    from 'System.Collections.Generic.IEnumerable<System.Xml.Linq.XElement>' 
	    to   'System.Collections.Generic.IEnumerable<System.Xml.Linq.XNode>'***
	Reason:                 
	- Nodes() returns an IEnumerable<XNode> 
	- Except() needs an IEnumerable<XNode>
	- Elements("bar") gives IEnumerable<XElement>
	With generic interfaces being invariant in .NET 3.5 we can't pass that IEnumerable<XElement> in for an IEnumerable<XNode>, although XElement is a class derived from XNode.
	It seems desirable that you would not need that Cast<XNode>() call.

	With .NET 4.0 the type parameter T of IEnumerable<T> is covariant meaning where an IEnumerable<T> of a certain type T is expected we can always pass in an IEnumerable<T2> where T2 is type derived from T, as in our example where XElement is a subclass of XNode (or subsubclass to be precise).
	Thus with .NET 4.0 the following compiles and works fine:
	XDocument doc2 = new XDocument(
	    new XElement(doc1.Root.Name, 
	                 doc1.Root.Nodes().Except(doc1.Root.Elements("bar")));
		
		Covariance preserves assignment compatibility
		No need that to Cast<XNode>() = Implicit conversion for array types, delegate types, generic type arguments


* GENERIC VARIANCE

```c#

	object ← string 					// yes, but...
	List<object> ← List<string>			// failed
	List<object> = new List<string>();  // failed. ex:  object[] langs = {"C#", "Python", "PHP", "Java"};
```
Generic variance is solved in C# 4.0



* ARRAY COVARIANCE

This is nothing but implicit conversion of an array of a more derived type to an array of a less derived type.
Unfortunately this is not type safe.
```c#
object[] strArray = new string[10];
strArray[0] = 1; // throw runtime exception, not compile time exception
```
In above example, our object array is of string type but we are assigning integer value to one of its element,
it will not throw any compile-time exception but, it will throw runtime exception.



* DELEGATE COVARIANCE (METHOD GROUP VARIANCE)

you can assign to delegates not only methods that have matching signatures, but also methods that return more derived types (covariance)
or that accept parameters that have less derived types (contravariance) than that specified by the delegate type.
This includes both generic and non-generic delegates.
```c#

static string Parental() { return "Grandfather name is: Lala Bhagwan Das"; }

Func<object> parentalLambda = () => Parental(); //lambda expression
Func<object> parentalFunc = Parental; //Grouped

static string ParentalObject(object obj) {	//method signature }
Contravariance. A delegate specifies a parameter type as string, but can assign a method that takes an object.
Action<String> parentalDel = ParentalObject;
```

Delegates have two more important concepts:
Covariance
Contravariance
A delegate can refer to a method with the same return type and signature, however, variance eases this requirement. 
Covariance and contravariance provide flexibility for matching a delegate type with a method signature.
Covariance permits a method to have a return type that is more derived than that defined in the delegate. 
                    an IEnumerable<T> of a certain type T is expected we can always pass in an IEnumerable<T2> where T2 is type derived from T
Contravariance permits a method that has parameter types that are less derived than those in the delegate type.

	public class Animal
    {
        protected int age;
        protected void displayAge(int age)
        {
            this.age = age;
            Console.WriteLine(this.age);
        }
    }
    public class Dog : Animal
    {
        public string color;
        public void displayColor()
        {
            displayAge(99);
            Console.WriteLine(this.color);
        }
    }
}

The Dog class inherits the Animal class. So using covariance, a delegate with type Animal can refer to the Dog type. 
We are creating a delegate with return type of Animal and assigning a reference of Dog type below
This is possible due to the covariance feature of delegates.

public delegate Animal AnimalDelegate();
static void Main(string[] args)
{
    AnimalDelegate an = newDog;
    an();
    Console.ReadKey(true);
}
static Dog newDog()
{
    Dog d = new Dog();
    d.color = "white";
    d.displayColor();
    return d;
}


### Sample 1

```c#

class  Animal {}
class  Dog:Animal {} 	// derived
class  Cat:Animal {} 	// derived

Animal objAninal = new Dog(); // valid statetement 
objAninal 		 = new Cat(); // valid statetement 

// .net 3.5: Can a group of Animals point to a group of dogs?
IEnumerable<Animal> animals = new List<Dog>>(); 	  
```
❌ Error Cannot convert type to 'System.Collections.Generic.List<Dog>' to 'System.Colleections.Generic.List<Animal>'
  Switch from 3.5 to .Net 4.0 -> Error disapeard
  .net 4.0 implements variance for generic interfaces and delegates using in and out key words
interface System.Collections.Generic.IEnumerable<out T>. T is covariant
Covariance preserves assignment compatibility between parent and Child relationship during dynamic polymorphism


### Sample 2

```c#
public interface ICovariant<out T> { }             remark <out ...>   used in dotnet core ILogger<MyClass>
public interface IContravariant<in T> { }          remark <in  ...>

public class Covariant<T> : ICovariant<T> { }
public class Contravariant<T> : IContravariant<T> { }

public class Fruit { }
public class Apple : Fruit { }

public class TheInsAndOuts
{
    public void Covariance()
    {
        ICovariant<Fruit> fruit = new Covariant<Fruit>();
        ICovariant<Apple> apple = new Covariant<Apple>();

        Covariant(fruit);
        Covariant(apple); //apple is being upcasted to fruit, without the 'out' keyword this will not compile
    }

    public void Contravariance()
    {
        IContravariant<Fruit> fruit = new Contravariant<Fruit>();
        IContravariant<Apple> apple = new Contravariant<Apple>();

        Contravariant(fruit); //fruit is being downcasted to apple, without the 'in' keyword this will not compile
        Contravariant(apple);
    }

    public void Covariant(ICovariant<Fruit> fruit)
    {}

    public void Contravariant(IContravariant<Apple> apple)
    {}
}
ICovariant<Fruit> apple = new Covariant<Apple>(); //bc it's covariant
IContravariant<Apple> fruit = new Contravariant<Fruit>(); //bc it's contravariant
```

 
 ## More
 
- https://docs.microsoft.com/en-us/dotnet/standard/generics/covariance-and-contravariance
- http://www.tutorialsteacher.com/csharp/csharp-covariance-and-contravariance
- http://zetcode.com/lang/csharp/csharp4/
- https://www.i-programmer.info/programming/other-languages/12478.html


