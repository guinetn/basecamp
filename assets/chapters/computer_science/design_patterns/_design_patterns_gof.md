# The 23 Gang of Four Patterns

Documented solutions to commonly occurring problems in software engineering

CREATIONAL PATTERNS
Organise objects creation / manage instances
Abstract the complex logic of creating objects from the client
||||
|---|---|---|
|Abstract Factory    | objet |	Creates an instance of several families of classes without specifying their ||concrete classes|
|Builder             | objet |	Separates object construction from its representation (create complex objects step by step)|
|Factory       | class |	Creates an instance between several derived classes. Defer instantiation to ||subclasses.|
|Prototype           | objet |	To create copies/clones of objects|
|Singleton           | objet |	To have a single instance of a class|
|Object Pool         | objet |	|
|Constructor         | objet |	Method called at object creation. Assign values to instance variables|

STRUCTURAL PATTERNS
Application = multiple types of objects that must fit together to construct the app.
Objects composition: objects relationship (classes association)
Comment combiner les objets
Association de classes
Besoin d'une structure intermédiaire de classes participant à une fonction. Utilisation de librairies indépendantes.
Evolution d'une composition à l'exécution.
Ex : Puzzle, jeu de cubes.
Associer des classes pour former des structures homogènes plus grandes accessible par une classe.

• Comment les objets sont assemblés
• Les patterns sont complémentaires les uns des autres

||||
|---|---|---|
|Adapter             | class |	Common interface for different classes. Ex: json/xml apis response|
|Bridge              | objet |	Separates an object’s interface from its implementation. object can have several implementations|
|Composite           | objet |	A tree structure of simple and composite objects|
|Decorator           | objet |	Put objects in wrapper to dynamically (at run-time) add them new properties/responsibilities |
|Facade              | objet |	Use a high-level interface to abstracts underlying complexity. LOGICAL group of objects in an unified interface|
|Flyweight           | objet |	A fine-grained instance used for efficient sharing|
|Proxy               | objet |	An object representing another object|
|Module              | objet |	|

BEHAVIORAL PATTERNS
Organise objects interactions/communications
Moyen de communication
Gestion des intéractions
Des traitements différents se font en fonction d'un contexte
Ex : Contrôleur Java (sur button et checkbox)

Limiter les responsabilités des traitements à certaines classes. Contrôler les flux de traitements.
pour décrire :
• des algorithmes
• des comportements entre objets
• des formes de communication entre objet


||||
|---|---|---|
|Chain of Responsability| objet | To pass request through a chain of handlers (process+next or reject=stop propagating) = sequential checks on incoming req. (ordering system)|
|Command             | objet |	Encapsulate a command request as an object|
|Interpreter         | class |	A way to include language elements in a program|
|Iterator            | objet |	Traverse a collection (Arrays, LinkedList, Trees, Graphs… without exposing underlying implementation: sequentially access elements|
|Mediator            | objet |	Defines simplified communication between classes|
|Memento             | objet |	Capture and restore an object's internal state|
|Observer            | objet |	An object can notify a change to subscribers: notification system for updates…|
|State               | objet |	Alter an object's behavior when its state changes|
|Strategy            | objet |	Encapsulates an algorithm inside a class|
|Template Method     | class |	Defer the exact steps of an algorithm to a subclass|
|Visitor             | objet |	Defines a new operation to apply to a class without change it.|

## More

- https://itnext.io/how-we-avoided-if-else-and-wrote-extendable-code-with-strategy-pattern-256e34b90caf
- https://medium.com/@adhasmana/auth-token-management-with-node-js-observer-pattern-e51a63d945b2
- https://www.telerik.com/blogs/design-patterns-in-javascript
- https://addyosmani.com/resources/essentialjsdesignpatterns/book/

::::
download.chapter(computer_science/design_patterns/abstract_factory.md)
::::
download.chapter(computer_science/design_patterns/builder.md)
::::
download.chapter(computer_science/design_patterns/factory.md)
::::
download.chapter(computer_science/design_patterns/prototype.md)
::::
download.chapter(computer_science/design_patterns/singleton.md)
::::
download.chapter(computer_science/design_patterns/object_pool.md)
::::
download.chapter(computer_science/design_patterns/constructor.md)
::::
download.chapter(computer_science/design_patterns/adapter.md)
::::
download.chapter(computer_science/design_patterns/bridge.md)
::::
download.chapter(computer_science/design_patterns/composite.md)
::::
download.chapter(computer_science/design_patterns/decorator.md)
::::
download.chapter(computer_science/design_patterns/facade.md)
::::
download.chapter(computer_science/design_patterns/flyweight.md)
::::
download.chapter(computer_science/design_patterns/proxy.md)
::::
download.chapter(computer_science/design_patterns/module.md)
::::
download.chapter(computer_science/design_patterns/chain_of_responsability.md)
::::
download.chapter(computer_science/design_patterns/command.md)
::::
download.chapter(computer_science/design_patterns/interpreter.md)
::::
download.chapter(computer_science/design_patterns/iterator.md)
::::
download.chapter(computer_science/design_patterns/mediator.md)
::::
download.chapter(computer_science/design_patterns/memento.md)
::::
download.chapter(computer_science/design_patterns/observer.md)
::::
download.chapter(computer_science/design_patterns/state.md)
::::
download.chapter(computer_science/design_patterns/strategy.md)
::::
download.chapter(computer_science/design_patterns/template.md)
::::
download.chapter(computer_science/design_patterns/visitor.md)
::::

samples in c#: https://dotnettutorials.net/lesson/visitor-design-pattern/

https://www.tutorialspoint.com/design_pattern/index.htm