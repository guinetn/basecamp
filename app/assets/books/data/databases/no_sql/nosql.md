# NoSQL - Not Only SQL

A new way to store and request data with non-relational databases

Relational database cannot manage big data: Volume, Velocity, Variety
NoSql relaxes some ACID constrainsts of RDBMS to allow data distribution
Response to the scale and agility challenges that face modern applications. 
Wide database technologies
More data is being collected and more users are accessing this data concurrently: the way web applications deal with data has changed significantly. Scalability and performance are more of a challenge than ever for relational databases that are schema-based and therefore can be harder to scale.

|Feature|      NoSQL Databases |			Relational Databases|
|---|---|---|
|Performance| 		High|						Low|
|Reliability| 		Poor|						Good|
|Availability| 		Good|						Good|
|Consistency| 		Poor|						Good|
|DataStorage| 		Optimized for huge data|		Medium sized to large|
|Scalability| 		High|						High (but more expensive)|

download.page(data/acid.md)

## NoSQL Models/Families
- Key-Value
- Graph
- Column
- Document
- Blob stores

download.page(data/nosql/db_nosql__model_keyvalue.md)
download.page(data/nosql/db_nosql__model_columns.md)
download.page(data/nosql/db_nosql__model_document.md)
download.page(data/nosql/db_nosql__model_graph.md)
download.page(data/nosql/db_nosql__model_blob.md)



* 1970 	Relational model: SQL
	Not for high volumes (slow responses, heavy and complex data distribution)
	Ex: Sql Server
	+
		Rules for data coherence
		Locks for concurrents access
		ACID respect (Atomic Coherent Isolation Durable)
		Tools to modelise
	-
		Less performance when volume increase
		Data distribution of a base problems

* 2000	NoSQL - Not Only SQL
	For high volumes (Google, Facebook)
	Ex: MongoDB, Cassandra, CouchDB, DynamoDB
	NoSQL is a form of unstructured storage, NoSQL databases do not have a fixed table structure like the ones found in relational databases.

	First, there were proprietary (closed source) types of NoSQL databases: SQL scalability issue was recognized by Web 2.0 companies with huge, growing data and infrastructure needs, such as Google, Amazon, and Facebook
	https://cloud.google.com/bigtable/
    https://aws.amazon.com/dynamodb/

    Success of these proprietary systems initiated development of a number of similar open-source and proprietary database systems, the most popular ones being 
    Hypertable
    Cassandra   http://cassandra.apache.org/
    MongoDB
    DynamoDB
    HBase
    Redis

	+
		.Good response with high volumes			
		.Flexible when issue (partial/full availability)
		.Schema-free = simple and flexible structure
		.Based on key-value pairs. Usually, each value has a key.
		.Store types:column store, document store, key value store, graph store, object store, XML store and other data store modes.
		.Open-source NoSQL databases don’t require expensive licensing fees 
		.Easy to distribute
		.Expansion is easier and cheaper than when working with relational databases. This is because it’s done by horizontally scaling and distributing the load on all nodes, rather than the type of vertical scaling that is usually done with relational database systems, which is replacing the main host with a more powerful one.
	-	
	    .Dont support reliability features that are natively supported by relational database systems: Not full ACID, only Coherence, availability, split resistance. This also means that NoSQL databases, which don’t support those features, trade consistency for performance and scalability. To support reliability and consistency features, developers must implement their own proprietary code. This limit the number of applications that can rely on NoSQL databases for secure and reliable transactions, like banking systems.
		.No join. Client must do it: forms of complexity found in most NoSQL databases include incompatibility with SQL queries. This means that a manual or proprietary querying language is needed, adding even more time and complexity.
		.Locks are not always available for some bases




The NoSQL database movement came about to address the shortcomings of relational databases and the demands of modern 
software development. MongoDB is the leading NoSQL database 

The relational data model relies on rigid adherence to a database schema, normalization of data and joins to store 
data and perform complex queries. But changes in application, user and infrastructure characteristics have led 
application developers and architects to seek alternative distributed document database technologies like 

NoSQL (Not only SQL). As a result, relational database developers accustomed to relational data modeling must 
approach their development in new ways.

Navigating the Transition From Relational to NoSQL Technology looks at the differences between relational and 
document database technology, highlights the implications of those differences for application developers, and 
provides guidance that can ease the transition from relational to NoSQL. Specifically you will learn:

•Relational versus document-oriented models
•Scaling model, data model and why you should transition
•Document Model Rules of Thumb
•The MVC model
•Using view collation to simplify queries.
•Concurrency, Scaling and performance issues

http://www.infoq.com/vendorcontent/show.action;jsessionid=B85B21FC3FC98657E9C6EDCA72E92FF0?vcr=1739


download.page(data/databases/no_sql/nosql_internal.md)
