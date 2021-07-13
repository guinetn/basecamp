# EVENT SOURCING

Streaming events between arbitrary sources and sinks, and it helps you make changes to the data while it’s in-flight

aka
- streaming ETL pipeline
- streaming data pipeline

Services ingesting events, transforming them, and loads them into destination storage systems
To move received data to another place as soon as you receive it, but making some changes to the data as you transfer it (enrich it by joining with data from another system., add identifiable information...)
Capture all changes to an application state as a sequence of events.
To build event-based applications



ES is persisting changes that are happening in the application as a sequence of events (a stream) that can be used to reconstruct the current state, so that any subsequent requests can be handled.

Event sourcing persists the state of a business entity such an Order or a Customer as a sequence of state-changing events. Whenever the state of a business entity changes, a new event is appended to the list of events. Since saving an event is a single operation, it is inherently atomic.

An architectural pattern that records all changes made to an application's state, in the sequence in which the changes were originally applied.

Event Sourcing deals with an event store of immutable log of events, in which each log (a state change made to an object) represents an application state. An event store is like a version control system. In a microservices architecture, we can persist aggregates as a sequence of event.
 
Event Sourcing ensures that all changes to application state are stored as a sequence of events. ... Not just can we query these events, we can also use the event log to reconstruct past states, and as a foundation to automatically adjust the state to cope with retroactive changes

Maybe you need to do something simple, like transform the events to strip out any personally . Sometimes, you may need to do something more complex, like enrich the events by  Or perhaps you want to pre-aggregate the events to reduce how much data you send to the downstream systems.

### Projections
one of the core patterns used in Event Sourcing. 
ES is persisting changes that are happening in the application as a sequence of events. Then this sequence (also called a stream) of events can be used to reconstruct the current state, so that any subsequent requests can be handled.

### Aggregate
has its internal state, which is a projection of a single fine-grained event stream. On the other hand - the Write Stack Projections can subscribe to streams containing all (or subset of all) events, and be used to create read models or support process managers

Problem
How to reliably/atomically update the database and publish messages/events?

Solution
Use event sourcing: it persists the state of a business entity such an Order or a Customer as a sequence of state-changing events. Whenever the state of a business entity changes, a new event is appended to the list of events. Since saving an event is a single operation, it is inherently atomic. The application reconstructs an entity’s current state by replaying the events.

Applications

Version control systems are good examples of event sourcing - particularly Git. Each commit is stored as an event representing a change of state - files/lines to be added/removed.  
Kafka: https://docs.ksqldb.io/en/latest/tutorials/etl


* Markov transition matrix from a streaming data source
- https://sam-black.medium.com/creating-a-markov-transition-matrix-from-a-streaming-data-source-995fcf28422


- https://docs.ksqldb.io/en/latest/tutorials/etl
- https://martinfowler.com/eaaDev/EventSourcing.html
- https://microservices.io/patterns/data/event-sourcing.html
- https://github.com/oskardudycz/EventSourcing.NetCore