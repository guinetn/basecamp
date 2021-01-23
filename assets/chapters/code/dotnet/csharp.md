# C#  #

[C# guide](https://docs.microsoft.com/en-us/dotnet/csharp/)
[C# language-reference](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/)

## Attributes

```cs
[System.AttributeUsage(System.AttributeTargets.Class |  
                       System.AttributeTargets.Struct,
                       AllowMultiple = true)  // multiuse attribute 
]  
public class AuthorAttribute : System.Attribute  
{  
    private string name;  
    public double version;  
  
    public AuthorAttribute(string name)  
    {  
        this.name = name;  
        version = 1.0;  
    }  
}  

[Author("P. Ackerman", version = 1.1)]  
class SampleClass  
{  
    // P. Ackerman's code goes here...  
}  

[Author("P. Ackerman", version = 1.1)]  
[Author("R. Koch", version = 1.2)]  
class SampleClass  
{  
    // P. Ackerman's code goes here...  
    // R. Koch's code goes here...  
}  

// or
Author anonymousAuthorObject = new Author("P. Ackerman");  
anonymousAuthorObject.version = 1.1;  

// 2. Accessing Attributes (Reflection)

var t = typeof(SampleClass);
System.Attribute[] attrs = System.Attribute.GetCustomAttributes(t);  // Reflection.  

// Displaying output.  
foreach (System.Attribute attr in attrs)  
{  
    if (attr is Author)  
    {  
        Author a = (Author)attr;  
        System.Console.WriteLine("   {0}, version {1:f}", a.GetName(), a.version);  
    }  
}  

```

## Classes

Inherit from a not sealed base class
Other classes can inherit from your class and override class virtual methods
Can implement one or more interfaces.

### abstract class
Has abstract methods: signature definition but no implementation
Abstract classes cannot be instantiated
They can only be used through derived classes that implement the abstract methods.
Class definitions can be split between different source files with 'partial'

### Finalizers / destructors

Perform any necessary final clean-up when a class instance is being collected by the garbage collector.
* Finalizers cannot be defined in structs. They are only used with classes.
* A class can only have one finalizer.
* Finalizers cannot be inherited or overloaded.
* Finalizers cannot be called. They are invoked automatically.
* A finalizer does not take modifiers or have parameters.
* Empty finalizers should not be used (performance) 

It implicitly calls Finalize() on the base class of the object. 
Finalize is called recursively for all instances in the inheritance chain, from the most-derived to the least-derived.
The programmer has no control over when the finalizer is called; the garbage collector decides when to call it. Finalizers are also called when the program exits. 
Forcing garbage collection with Collect() should be avoided for performance issues.

```cs
public class Destroyer
{
   public override string ToString() => GetType().Name;

   ~Destroyer() => Console.WriteLine($"The {ToString()} destructor is executing.");
}

protected override void Finalize()  
{  
    try  
    {  
        // Cleanup statements...  
    }  
    finally  
    {  
        base.Finalize();  
    }  
}  
```
#### IDisposable
To release unmanaged resources. The garbage collector automatically releases the memory allocated to a managed object when that object is no longer used. However, it is not possible to predict when garbage collection will occur. Furthermore, the garbage collector has no knowledge of unmanaged resources such as window handles, or open files and streams.

You can release your resources before the garbage collector frees the object
Even with this explicit control over resources, the finalizer becomes a safeguard to clean up resources if the call to the Dispose method fails.

Call Dispose() to explicitly release unmanaged resources in conjunction with the garbage collector.

```cs
class BaseClass : IDisposable
{
   // Flag: Has Dispose already been called?
   bool disposed = false;

   // Public implementation of Dispose pattern callable by consumers.
   public void Dispose()
   {
      Dispose(true);
      GC.SuppressFinalize(this);
   }

   // Protected implementation of Dispose pattern.
   protected virtual void Dispose(bool disposing)
   {
      if (disposed)
         return;

      if (disposing) {
         // Free any other managed objects here.
         //
      }

      // Free any unmanaged objects here.
      //
      disposed = true;
   }

   ~BaseClass()
   {
      Dispose(false);
   }
}
```

Subclasses should implement the disposable pattern as follows:
They must override Dispose(Boolean) and call the base class Dispose(Boolean) implementation.
They can provide a finalizer if needed. The finalizer must call Dispose(false).

### Polymorphism

When a derived class inherits from a base class, it gains all the methods, fields, properties, and events of the base class. 

Base classes can implement ***virtual*** methods that derived classes can ***override*** (their own implementation)
* Methods, properties, events, indexers can be virtual
* Fields cannot be virtual

A derived class can override a base class member only if the base class member is declared as virtual or abstract. Derived class has different choices for the behavior of virtual methods:

* Can inherit without overriding it: preserve existing behavior but enabling further derived classes to override the method.
* Can override virtual members in the base class, defining new behavior.
* Can define ***new*** non-virtual implementation of those members that ***hide*** the base class implementations`.

`When a derived class overrides a virtual member, that member is called even when an instance of that class is being accessed as an instance of the base class`
CLR looks the run-time type of the object and invokes that override of the virtual method

`Hidden BASE CLASS MEMBERS may be accessed from client code by casting the instance of the derived class to an instance of the base class`

```cs
public class BaseClass
{
    public virtual void DoWork() { }
    public virtual int WorkProperty { get { return 0; } }
}

public class DerivedClass : BaseClass
{
    public override void DoWork() { }
    public override int WorkProperty { get { return 0; } }
}

public class HideDerivedClass : BaseClass
{
    public new void DoWork() { }
    public new int WorkProperty { get { return 0; } }
}

DerivedClass B = new DerivedClass();
B.DoWork();  // Calls the new method

BaseClass A = (BaseClass)B;
A.DoWork();  // Also calls the new method

HideDerivedClass C = new HideDerivedClass();
C.DoWork();  // Calls the new method
BaseClass A2 = (BaseClass)C;
A2.DoWork();  // Calls the hidden old method
```

#### Stop virtual inheritance

Method DoWork is no longer virtual to any class derived from C. It's still virtual for instances of C, even if they're cast to type B or type A. Sealed methods can be replaced by derived classes by using the new keyword
 
```c#
public class A
{
    public virtual void DoWork() { }
}
public class B : A
{
    public override void DoWork() {
        // Access base class virtual members from derived classes
        base.DoWork();
     }
}
// Stop virtual inheritance
public class C : B
{
    public sealed override void DoWork() { }
}
public class D : C
{
    public new void DoWork() { }
}
```




## Delegates
A type (delegate name = delegate type) that encapsulate (wrap) a method 
Call him = call a function(s) that can be different
~ function pointer in C/C++ 
Object-oriented, type safe, secure 
 
A delegate is an instance of a delegate type that has references to:
- An instance method of a type and a target object assignable to that type.
    Stores a reference to the method's entry point 
    Stores a reference to an object (target) of type assignable to the type that defined the method
- An instance method of a type, with the hidden this parameter exposed in the formal parameter list (open instance delegate)
    Stores a reference to the method's entry point
    Delegate parameters signature include the hidden 'this' 
    Delegate doesn't have a reference to a target object that must be supplied at delegate invokation
- A static method
    Stores a reference to the method's entry point
- A static method and a target object assignable to the first parameter of the method (closed over its first argument)
    Stores a reference to the method's entry point
    Stores a reference to a target object assignable to the type of the method's first argument. When the delegate is invoked, the first argument of the static method receives the target object.

When a delegate is constructed to wrap an instance method
    the delegate references both the instance and the method. A delegate has no knowledge of the instance type aside from the method it wraps, so a delegate can refer to any type of object as long as there is a method on that object that matches the delegate signature
When a delegate is constructed to wrap a static method
    it only references the method

Derived from 'Delegate' class:
Represents a delegate, which is a data structure that refers to a static method or to a class instance and an instance method of that class.

CLR provides each delegate type with BeginInvoke() and EndInvoke() to enable asynchronous invocation of the delegate

```cs
// 1. DELEGATE TYPE DECLARATION
// Contract that specifies the signature of one or more methods
// A delegate named Del that can encapsulate a method having a string argument and returning void:
public delegate void Del(string message);

// 2. DELEGATE INSTANTIATION 
// * the name of the method the delegate will wrap
// * an anonymous function
public static void DelegateMethod(string message)
{
    Console.WriteLine(message);
}
Del handler = DelegateMethod;

// 3. DELEGATE INVOKATION
handler("Hello World");


public static void MethodWithCallback(int param1, int param2, Del callback)
{
    callback("The number is: " + (param1 + param2).ToString());
}
MethodWithCallback(1, 2, handler);
```

```cs

public delegate String methodDelegate( int myInt );

// Defines some methods to which the delegate can point.
public class class1  {
    // Defines an instance method.
    public String myStringMethod ( int myInt )  { }
    // Defines a static method.
    public static String mySignMethod ( int myInt )  {}
}

mySampleClass c = new class1();
var myD1 = new methodDelegate( c.myStringMethod );
var myD2 = new methodDelegate( class1.mySignMethod );
```
## MulticastDelegate
A delegate with more than one element in its invocation list (a linked list of delegates)

var obj = new MethodClass();
Del d1 = obj.Method1;
Del d2 = obj.Method2;
Del d3 = DelegateMethod;

//Both types of assignment are valid.
Del allMethodsDelegate = d1 + d2;
allMethodsDelegate += d3;

All three methods are called in order
If the delegate uses reference parameters, the reference is passed sequentially to each of the three methods in turn, and any changes by one method are visible to the next method.

//remove Method1
allMethodsDelegate -= d1;

// copy AllMethodsDelegate while removing d2
Del oneMethodDelegate = allMethodsDelegate - d2;

// Number of methods in a delegate's invocation list:
int invocationCount = d1.GetInvocationList().GetLength(0);

## Events
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/events/

A class/object can notify others classes/objects 
`Publisher*** sends (raises) an event to ***Subscribers*** that handle it

All .NET events are based on 
- ***EventHandler delegate`
public delegate void EventHandler(object sender, EventArgs e);
public delegate void EventHandler<TEventArgs>(object? sender, TEventArgs e); // Generic version
- ***EventArgs*** base class.
 
### Custom event data

```cs

public class CustomEventArgs : EventArgs
{
    public CustomEventArgs(string message)
    {
        Message = message;
    }

    public string Message { get; set; }
}
```
 
### Declare a delegate

No need with the generic version of EventHandler<TEventArgs>
Its name that ends with ***EventHandler`
Second parameter specifies your custom EventArgs type

```cs
public delegate void CustomEventHandler(object sender, CustomEventArgs args);
``*** 
### Publishing class declares the event

```cs
public event EventHandler RaiseCustomEvent;         //  no custom EventArgs class
public event CustomEventHandler RaiseCustomEvent;   // non-generic version + custom EventArgs
public event EventHandler<CustomEventArgs> RaiseCustomEvent;  // generic version don't need a custom delegate
```
### subscribe to events: Declare an event handler

```cs
// Declare an event handler
void HandleCustomEvent(object sender, CustomEventArgs a)  
{     
}  
// Attach an event handler to the event with (+=) assignment operator
// subscriber needs a reference to the publisher to subscribe to its events
publisher.RaiseCustomEvent += HandleCustomEvent;  

// lambda expression form
this.Click += (s,e) => { MessageBox.Show(((MouseEventArgs)e).Location.ToString()); };

// To subscribe to events by using an anonymous method
publisher.RaiseCustomEvent += delegate(object o, CustomEventArgs e)  
{  
  string s = o.ToString() + " " + e.ToString();    
};  
```

### unsubscribe to events
```cs
publisher.RaiseCustomEvent -= HandleCustomEvent;  
```

### Event samples

```cs
using System;

namespace DotNetEvents
{
    // Define a class to hold custom event info
    public class CustomEventArgs : EventArgs
    {
        public CustomEventArgs(string message)
        {
            Message = message;
        }

        public string Message { get; set; }
    }

    // Class that publishes an event
    class Publisher
    {
        // Declare the event using EventHandler<T>
        public event EventHandler<CustomEventArgs> RaiseCustomEvent;

        public void DoSomething()
        {
            // Write some code that does something useful here
            // then raise the event. You can also raise an event
            // before you execute a block of code.
            OnRaiseCustomEvent(new CustomEventArgs("Event triggered"));
        }

        // Wrap event invocations inside a protected virtual method
        // to allow derived classes to override the event invocation behavior
        protected virtual void OnRaiseCustomEvent(CustomEventArgs e)
        {
            // Make a temporary copy of the event to avoid possibility of
            // a race condition if the last subscriber unsubscribes
            // immediately after the null check and before the event is raised.
            EventHandler<CustomEventArgs> raiseEvent = RaiseCustomEvent;

            // Event will be null if there are no subscribers
            if (raiseEvent != null)
            {
                // Format the string to send inside the CustomEventArgs parameter
                e.Message += $" at {DateTime.Now}";

                // Call to raise the event.
                raiseEvent(this, e);
            }
        }
    }

    //Class that subscribes to an event
    class Subscriber
    {
        private readonly string _id;

        public Subscriber(string id, Publisher pub)
        {
            _id = id;

            // Subscribe to the event
            pub.RaiseCustomEvent += HandleCustomEvent;
        }

        // Define what actions to take when the event is raised.
        void HandleCustomEvent(object sender, CustomEventArgs e)
        {
            Console.WriteLine($"{_id} received this message: {e.Message}");
        }
    }

    class Program
    {
        static void Main()
        {
            var pub = new Publisher();
            var sub1 = new Subscriber("sub1", pub);
            var sub2 = new Subscriber("sub2", pub);

            // Call the method that raises the event.
            pub.DoSomething();

            // Keep the console window open
            Console.WriteLine("Press any key to continue...");
            Console.ReadLine();
        }
    }
}
```
## Covariance / Contravariance

Implicit reference conversion for array types, delegate types, generic type arguments
Covariance preserves assignment compatibility and contravariance reverses it.
 
### Covariance 
method can have more derived return type 

Covariance for arrays enables implicit conversion of an array of a more derived type to an array of a less derived type. But this operation is not type safe:
```cs
object[] array = new String[10];  
array[0] = 10; // run-time exception: implicit conversionnot type safe operation  
```

```cs
IEnumerable<string> strings = new List<string>();  
// An object that is instantiated with a more derived type argument
// is assigned to an object instantiated with a less derived type argument.
// Assignment compatibility is preserved.
IEnumerable<object> objects = strings;  
```

```cs
class Cells {}  
class Human : Cells {}  
  
class Program  
{  
    // Define the delegate.  
    public delegate Cells HandlerMethod();  
  
    public static Cells CellsHandler()  
    {  
        return null;  
    }  
  
    public static Human HumanHandler()  
    {  
        return null;  
    }  
  
    static void Test()  
    {  
        HandlerMethod handlerCells = CellsHandler;  
  
        // Covariance enables this assignment.  
        HandlerMethod handlerHuman = HumanHandler;  
    }  
}  
```
### Contravariance
method can have less derived parameter types  

```cs
// Event handler that accepts a parameter of the EventArgs type.  
private void MultiHandler(object sender, System.EventArgs e)  
{  
    label1.Text = System.DateTime.Now.ToString();  
}  
  
public Form1()  
{  
    InitializeComponent();  
  
    // You can use a method that has an EventArgs parameter,  
    // although the event expects the KeyEventArgs parameter.  
    this.button1.KeyDown += this.MultiHandler;  
  
    // You can use the same method
    // for an event that expects the MouseEventArgs parameter.  
    this.button1.MouseClick += this.MultiHandler;  
  
}  
```
 
## Interfaces
## Properties
## Operators and expressions
## Statements
## Structs

## Expression Trees
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/expression-trees/
code in a tree-like data structure, each node is an expression (method call, binary operation: x<y ...>)
Compile and run code represented by expression trees. This enables dynamic modification of executable code (linq queries)

Used in the dynamic language runtime (DLR) to provide interoperability between dynamic languages and .NET and to enable compiler writers to emit expression trees instead of Microsoft intermediate language (MSIL).

```cs
// Creating a lambda expression tree.  
Expression<Func<int, bool>> expr = num => num < 5;  
  
// Compiling the expression tree into a delegate.  
Func<int, bool> result = expr.Compile();  
  
// Invoking the delegate and writing the result to the console.  
Console.WriteLine(result(4));  // Prints True
  
// Simplified syntax to compile and run an expression tree.  
Console.WriteLine(expr.Compile()(4));  
```

```cs
using System.Linq.Expressions;  
  
// Manually build the expression tree for the lambda expression num => num < 5
ParameterExpression numParam = Expression.Parameter(typeof(int), "num");  
ConstantExpression five = Expression.Constant(5, typeof(int));  
BinaryExpression numLessThanFive = Expression.LessThan(numParam, five);  
Expression<Func<int, bool>> lambda1 =  
    Expression.Lambda<Func<int, bool>>(  
        numLessThanFive,  
        new ParameterExpression[] { numParam }); 
```


## Methods

https://docs.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/calling-synchronous-methods-asynchronously

## Lambdas

```cs
List<int> elements = new List<int>() { 10, 20, 31, 40 };
int firstOddIndex = elements.FindIndex(x => x % 2 != 0);
Console.WriteLine(firstOddIndex);

elements.Where(v => (int)v > 11).ToArray()
```

# Collections
Enumerable.Range(1, 5).Select(i => {})

# Variables
var rng = new Random();  

# Random 
var rng = new Random();  
var TemperatureC = rng.Next(-20, 55);  
var Summary = Summaries[rng.Next(100)];