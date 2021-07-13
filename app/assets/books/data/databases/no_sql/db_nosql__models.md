# NoSQL - Not Only SQL

A new way to store and request data with non-relational databases

- Relational database cannot manage big data: Volume, Velocity, Variety
- NoSql relaxes some ACID constrainsts of RDBMS to allow data distribution
- Response to the scale and agility challenges that face modern applications. 
- Wide database technologies
- More data is being collected and more users are accessing this data concurrently: the way web applications deal with data has changed significantly. Scalability and performance are more of a challenge than ever for relational databases that are schema-based and therefore can be harder to scale.


## NoSQL Families

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

## NoSQL candidates
 
|           |   Storage Type|	Query Method	Interface	Programming |Language	|Open |Source Replication|
|Cassandra	|	Column Store|	Thrift API		 |Thrift		|Java		           |Yes			|Async|
|MongoDB	|	Document Store|	Mongo Query		 |TCP/|IP		|C++		           |Yes			|Async|
|HyperTable	|	Column Store|	HQL				 |Thrift		|Java		           |Yes			|Async|
|CouchDB	|	Document Store|	MapReduce		 |REST			|Erlang		           |Yes			|Async|
|BigTable	|	Column Store|	MapReduce		 |TCP/|IP		|C++		           |No			|Async|
|HBase		|	Column Store|	MapReduce		 |REST			|Java		           |Yes			|Async|

**NoSQL candidates selection**
criteria [0-5]
https://db-engines.com/en/ranking_trend

|Score|MongoDB|Cassandra|ElasticSearch|
|---|---|---|---|---|
|Cost|0.5|4|4|4|
|Consistency|1|4|2|2|
|Availability|0.5|2|4|3|
|Language|1|4|2|3|
|Functionalities|2|4|2|4|
|Total|5|19|12|16.5|

constitency + rich language → MongoDB
ElasticSearch good but bad for consistency

![](assets/books/data/assets/nosql-store-decision-flow.png)

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

