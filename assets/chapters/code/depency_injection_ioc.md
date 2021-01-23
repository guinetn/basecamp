# DEPENCY INJECTION - IoC

Software application design rule: loosely coupled = greater reusability, maintainability,  testability. 

Dependency Injection (DI) reduces the coupling between classes and moves the binding of abstraction and concrete implementation out of the dependent class. 

DI creates loosely coupled classes. The Dependency Injection (DI) pattern uses a builder object to initialize objects and provide the required dependencies to the object, meaning that it allows developers to "inject" a dependency from outside the class. There are four ways of achieving the Dependency Injection.

![](assets/chapters/code/assets/di.jpg)
 
## Dependency Injection Design Pattern

A dependency describes the relationship among entities
To remove the dependencies between the objects: class decoupling

technique in which an object receives other objects that it depends on. These other objects are called dependencies. ... The "injection" refers to the passing of a dependency (a service) into the object (a client) that would use it.

A design pattern used to implement IoC
Moves the dependencies to the interface of components.
Reduce the cohesion or coupling amongst the components in an application.

Makes a class independent of its dependencies by decoupling the usage of an object from its creation
Move the creation and binding of the dependent objects outside of the class that depends on them

allows a service to be used/injected in a way that is completely independent of any client consumption. ... Dependency injection separates the creation of a client's dependencies from the client's behavior, which allows program designs to be loosely coupled

* When: if tight coupling of object implementations

* Benefits
Injections reduce the amount you have to code (and hence, debug), facilitating the creation of better apps and a smoother development process

Helps class decoupling. 
make simple to manage dependencies between objects that makes it easier to break coherent functionality off into its own contract. Code become more modularized. 
Increases reusability of the code and improves code maintainability and testing.

* Downsides 
increases code complexity, usually by increasing the number of classes, which is not always beneficial. Generally, the benefit of decoupling makes each task simpler to read and understand, but increases the complexity of orchestrating the more complex tasks.
a higher learning curve. To understand how a project uses dependency injection, a developer needs to understand both the dependency injection pattern and the specific framework.

* Types of dependency injection

### constructor injection
https://dotnettutorials.net/lesson/dependency-injection-design-pattern-csharp/

### method injection
### property/setter injection
https://dotnettutorials.net/lesson/setter-dependency-injection-design-pattern-csharp/

### Interface-based injection

## IOC - Inversion of control 

Normal control sequence would be the object finds the objects it depends on by itself and then calls them.
Implementations are passed into an object through constructors/setters/service lookups

Program delegates control to someone else who will drive the flow IOC (Inversion of control) is a general parent term while DI (Dependency injection) is a subset of IOC
 
## C#  Dependency Injection containers
#### Spring.NET
Spring.NET is one of the popular open source frameworks for Dependency Injection. Spring.NET supports .NET 4.0, .NET Client Profile 3.5 and 4.0, Silverlight 4.0 and 5.0, and Windows Phone 7.0 and 7.1
#### Castle Windsor
Castle Windsor is a mature Inversion of Control Container available for .NET and Silverlight. The current version is 4.0, released in July 2017. Castle Windsor could be downloaded from GitHub or NuGet. The advantages of using Castle Windsor is that it is completem it understands decorators, and its very well documented.
#### Unity
The Unity Application Block (Unity) is a lightweight, extensible dependency injection container which is relatively more complicated and obtrusive code. Unity uses a container and XML data. It has strong XML support and works with WPF applications. It's free under the Microsoft public license. Unity addresses the issues faced by developers engaged in component-based software engineering. Unity also includes the Interception container extension, which allows developers to inject exception management, logging, or even your own custom code between the caller and the called.
#### Structure Map
StructureMap is a Dependency Injection tool for .NET that can be used to improve the architectural qualities of an object-oriented system by reducing the mechanical costs of good design techniques. It's released under the permissive Apache 2 OSS license. It's free, and a developer can download, modify, or redistribute StructureMap.
#### Autofac: https://autofaccn.readthedocs.io/en/latest/
Autofac is an Inversion of Control (IOC) container for Microsoft .NET C#, versions 3.0 and above. Licensed under MIT, it manages the dependencies among classes so that applications stay easy to change as they grow in size and complexity.
#### Ninject
An open source, ultra-lightweight, and universal dependency injection framework for .NET, Mono, .NET Compact Framework, and Silverlight. It is licensed under Apache 2. Ninject helps you use the technique of dependency injection to break your applications into loosely coupled, highly-cohesive components, and then glue them back together in a flexible manner.

## Service Locator design pattern 
Allows decoupling clients of services (described by a public interface) from the concrete class implementing those services. 

The Service Locator is a pattern by which we can reduce the dependency of one object on another that we will see shortly and Dependency injection (DI) is another smart solution for the same problem.


* strongly typed
the service locator class will return a known type. 

```cs
using System;  
using System.Collections.Generic;  
using System.Linq;  
namespace Client  
{  
    public interface IService  
    {  
        void ExecuteService();  
    }  
    public class LoggingService : IService  
    {  
        public void ExecuteService()  
        {  
            Console.WriteLine("Executing Log Service");  
        }  
    }  
  
    public static class ServiceLocator  
    {  
        public static IService ObjService = null;  
          
        //Service locator function returning strong type   
        public static IService SetLocation(IService tmpser)  
        {  
            if (ObjService == null) return new LoggingService();  
            return ObjService;  
        }  
          
        //Execute service  
        public static void ExecuteService()  
        {  
            ObjService.ExecuteService();  
        }  
    }  
  
    class Program  
    {  
        static void Main(string[] args)  
         {  
           IService svr =  ServiceLocator.SetLocation(new LoggingService());  
           svr.ExecuteService();  
           Console.ReadLine();  
        }  
    }  
} 
```


* Generic type service locator
Can deal with various types since this is generic in nature

```c#
using System;  
using System.Collections.Generic;  
using System.Text;  
namespace Client  
{  
    public interface IServiceA  
    {  
        void Execute();  
    }  
  
    public class ServiceA : IServiceA  
    {  
        public void Execute()  
        {  
            Console.WriteLine("A service called.");  
        }  
    }  
  
    public interface IServiceB  
    {  
        void Execute();  
    }  
  
    public class ServiceB : IServiceB  
    {  
        public void Execute()  
        {  
            Console.WriteLine("B service called.");  
        }  
    }  
  
    public interface IService  
    {  
        T GetService<T>();  
    }  
    public class ServiceLocator : IService  
    {  
        public Dictionary<object, object> servicecontainer = null;  
        public ServiceLocator()  
        {  
            servicecontainer = new Dictionary<object, object>();  
            servicecontainer.Add(typeof(IServiceA), new ServiceA());  
            servicecontainer.Add(typeof(IServiceB), new ServiceB());  
        }  
        public T GetService<T>()  
        {  
            try  
            {  
                return (T)servicecontainer[typeof(T)];  
            }  
            catch (Exception ex)  
            {  
                throw new NotImplementedException("Service not available.");  
            }  
        }  
    }  
    class Program  
    {  
        static void Main(string[] args)  
         {  
            ServiceLocator loc = new ServiceLocator();  
            IServiceA Aservice =  loc.GetService<IServiceA>();  
            Aservice.Execute();  
  
            IServiceB Bservice = loc.GetService<IServiceB>();  
            Bservice.Execute();  
  
           Console.ReadLine();  
         }  
    }  
} 
```
## More

- https://github.com/unitycontainer