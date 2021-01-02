# NoSQL

## NoSQL

NoSQL encompasses a wide variety of different database technologies that were developed in response to the scale and agility challenges that face modern applications. 

More data is being collected and more users are accessing this data concurrently: the way web applications deal with data has changed significantly. Scalability and performance are more of a challenge than ever for relational databases that are schema-based and therefore can be harder to scale.

https://www.toptal.com/database/the-definitive-guide-to-nosql-databases



|           |   Storage Type|	Query Method	Interface	Programming |Language	|Open |Source Replication|
|Cassandra	|	Column Store|	Thrift API		 |Thrift		|Java		           |Yes			|Async|
|MongoDB	|	Document Store|	Mongo Query		 |TCP/|IP		|C++		           |Yes			|Async|
|HyperTable	|	Column Store|	HQL				 |Thrift		|Java		           |Yes			|Async|
|CouchDB	|	Document Store|	MapReduce		 |REST			|Erlang		           |Yes			|Async|
|BigTable	|	Column Store|	MapReduce		 |TCP/|IP		|C++		           |No			|Async|
|HBase		|	Column Store|	MapReduce		 |REST			|Java		           |Yes			|Async|


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





|Feature|      NoSQL Databases |			Relational Databases|
|---|---|---|
|Performance| 		High|						Low|
|Reliability| 		Poor|						Good|
|Availability| 		Good|						Good|
|Consistency| 		Poor|						Good|
|DataStorage| 		Optimized for huge data|		Medium sized to large|
|Scalability| 		High|						High (but more expensive)|



## NoSQL STOCKAGE MODELS (Data Store Types)


### KEY/VALUE MODEL

A hash table is used in which a unique key points to an item.
Data is stored in a form of a string, JSON, or BLOB (Binary Large OBject).

Keys can be organized into logical groups of keys, only requiring keys to be unique within their own group. This allows for identical keys in different logical groups
Some implementations provide caching mechanisms for enhancing performance

	id <---> Value (simple or object)
	Only 4 operations: CRUD
	DataSmart is at client level

biggest flaws in this form of database is the lack of consistency at the database level. This can be added by the developers with their own code

. Amazon’s DynamoDB


### DOCUMENTARY BASE MODEL (Document Store)

Document stores are similar to key value stores in that they are schema-less and based on a key-value model. 
Values (documents) provide encoding for the data stored. Those encodings can be XML, JSON, or BSON (Binary encoded JSON).
Querying based on data can be done.

. MongoDB

	Collection: group of documents
		|
		|
		| ______	each entry is a document (a group of fields + id added by the sgbd)
															|
															|_____ each field could be a document
     -------|	doc#1	{id:"1", name:"john", age:"22" }													
	|		|	doc#2	{id:"1", name:"john", age:"22", city:"London" }   <--- structure dont have to be identical				
	|
	 ------> could be in the same collection (no strict structure to respect) 


###	COLUMNS ORIENTED MODEL (Column Store)

data is stored in columns, as opposed to being stored in rows as is done in most relational database management systems.
A Column Store is comprised of one or more Column Families that logically group certain columns in the database. A key is used to identify and point to a number of columns in the database, with a keyspace attribute that defines the scope of this key. Each column contains tuples of names and values, ordered and comma separated.

Column Stores have fast read/write access to the data stored. In a column store, rows that correspond to a single column are stored as a single disk entry. This makes for faster access during read/write operations.

. Google’s BigTable
. HBase
. Cassandra

	Add data is easy
	null are limited

	relational model: data in rows 		1. guitar, flamenco
										2. piano, classic
										3. flute, irlandais	
	in a columns oriented model:
										1,2,3
										guitar, piano, flute
										flamenco, classic, irlandais	

### GRAPH MODEL (Graph Base)

	From the "Graph Theory"
	Data are nodes with a document structure (see above)
	Arcs oriented and named links the nodes

Typically used in social networking applications: allow developers to focus more on relations between objects rather than on the objects themselves. 

A graph base database uses edges and nodes to represent and store data. These nodes are organized by some relationships with one another, which is represented by edges between the nodes. Both the nodes and the relationships have some defined properties.

A graph structure (a set of objects connected by links) comprising edges ans nodes
The interconnected objects are represented by mathematical abstractions, called vertices, and the links that connect some pairs of vertices are called edges. A set of vertices and the edges that connect them is said to be a graph.

Point = sommet = vertex. (vertices if ++)

nodes are organized by some relationships with one another, which is represented by edges between the nodes. Both the nodes and the relationships have some defined properties.

.InfoGrid
.InfiniteGraph





## INDEXING STRUCTURES FOR NOSQL DATABASES

Indexing is the process of associating a key with the location of a corresponding data record in a DBMS. There are many indexing data structures used in NoSQL databases. 

### B-Tree Indexing

B-Tree is one of the most common index structures in DBMS’s.
In B-trees, internal nodes can have a variable number of child nodes within some predefined range.
One major difference from other tree structures, such as AVL, is that B-Tree allows nodes to have a variable number of child nodes, meaning less tree balancing but more wasted space.
The B+-Tree is one of the most popular variants of B-Trees. The B+-Tree is an improvement over B-Tree that requires all keys to reside in the leaves.

### T-Tree Indexing

The data structure of T-Trees was designed by combining features from AVL-Trees and B-Trees.
AVL-Trees are a type of self-balancing binary search trees, while B-Trees are unbalanced, and each node can have a different number of children.
In a T-Tree, the structure is very similar to the AVL-Tree and the B-Tree.
Each node stores more than one {key-value, pointer} tuple. Also, binary search is utilized in combination with the multiple-tuple nodes to produce better storage and performance.
A T-Tree has three types of nodes: A T-Node that has a right and left child, a leaf node with no children, and a half-leaf node with only one child.

It is believed that T-Trees have better overall performance than AVL-Trees.

### O2-Tree Indexing

The O2-Tree is basically an improvement over Red-Black trees, a form of a Binary-Search tree, in which the leaf nodes contain the {key value, pointer} tuples.
O2-Tree was proposed to enhance the performance of current indexing methods. An O2-Tree of order m (m ≥ 2), where m is the minimum degree of the tree, satisfies the following properties:
Every node is either red or black. The root is black.
Every leaf node is colored black and consists of a block or page that holds “key value, record-pointer” pairs.
If a node is red, then both its children are black.
For each internal node, all simple paths from the node to descendant leaf-nodes contain the same number of black nodes. Each internal node holds a single key value.
Leaf-nodes are blocks that have between ⌈m/2⌉ and m “key-value, record-pointer” pairs.
If a tree has a single node, then it must be a leaf, which is the root of the tree, and it can have between 1 to m key data items.
Leaf nodes are double-linked in forward and backward directions.





# MongoDB (c++)
Document Store	
Great database which I love and is the main inspiration behind RaptorDB, although I have issues with its 32bit 4Gb database size limit and the memory map file design which could potentially corrupt easily. (Polymorphism has a workaround in mongodb if anyone wants to know).
flexible schema storage, which means stored objects are not necessarily required to have the same structure or fields. MongoDB also has some optimization features, which distributes the data collections across, resulting in overall performance improvement and a more balanced system.

schema-free, document-oriented database written in C++. The database is document store based, which means it stores values (referred to as documents) in the form of encoded data.
The choice of encoded format in MongoDB is JSON. This is powerful, because even if the data is nested inside JSON documents, it will still be queryable and indexable.


# Apache CouchDB / CouchBase (erlang)
Document Store
Another standard in document databases. The design is elegant.
Share a lot of features with MongoDB, with the exception that the database can be accessed using RESTful APIs.

# RavenDB (.net)
Document Store
Work done by Ayende which is a .net document database built on the Windows ESENT storage system.
http://ravendb.net

RavenDB is a document database for the .NET platform, offering a flexible data model design to fit the needs of real world systems.

Forget about tables, rows, mappings or complicated data-layers. RavenDB is a document-oriented database you can just dump all your objects into.
Queries are amazingly fast and flexible.

RavenDB is a document database, which stores each document in JSON format. In a document database any entity can be stored as a document.
You don’t have to define in advance the schema of your data in order to store it, all you have to do is to give RavenDB an object and RavenDB will store it. Later in this post, I’ll show you what does a document looks like.

# OrientDB (java)
The performance specs are impressive.


# Cassandra
Column Store
developed by Facebook
includes a lot of features aimed at reliability and fault tolerance.
The goal behind Cassandra was to create a DBMS that has no single point of failure and provides maximum availability.
Inspired by Google’s BigTable, which is a column store database, and Amazon’s DynamoDB, which is a key-value database.
by providing a key-value system, but the keys in Cassandra point to a set of column families, with reliance on Google’s BigTable distributed file system and Dynamo’s availability features (distributed hash table).

designed to store huge amounts of data distributed across different nodes. Cassandra is a DBMS designed to handle massive amounts of data, spread out across many servers, while providing a highly available service with no single point of failure, which is essential for a big service like Facebook.


# HyperTable
Column Store
C++ 
is based on Google’s BigTable

# BigTable
Column Store

# HBase	
Column Store