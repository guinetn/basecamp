# DATA

Operations: Accessing, inserting, deleting, finding, sorting 

### SCHEMA
Collection of database objects including tables, views, triggers, stored procedures, indexes, types, interfaces, enums, unions...taht make up your application data model
Organize the database objects into logical groups to make them more manageable. Also, schema can be treated as a dictionary with all the information objects of the database.
>SELECT * FROM information_schema.columns; Or we can choose to see the schema for a specific table,
>SELECT * FROM information_schema.columns WHERE table_name = 'boats';

### INDEX TYPES

Indexing is the process of associating a key with the location of a corresponding data record in a DBMS. 

* PRIMARY   unique, one per table
* UNIQUE    unique, no two rows have the same combination of the values
* INDEX     may not be unique, but improves lookup efficiency
* FULLTEXT  Create an index for each word in that column for full text search

PRIMARY KEY, UNIQUE, INDEX, and FULLTEXT are stored in B+trees
spatial data types use R-trees;

* 1970 Relational model: SQL
    Not for high volumes (slow responses, heavy and complex data distribution)
    Ex: Sql Server, Oracle, MySQL
    +
        Rules for data coherence
        Locks for concurrents access
        ACID respect (Atomic Coherent Isolation Durable)
        Tools to modelise
    -
        Less performance when volume increase
        Data distribution of a base problems

* 2000 NoSQL - Not Only SQL
    For high volumes (Google, Facebook)
    Ex: MongoDB, Cassandra, CouchDB, DynamoDB
    NoSQL is a form of unstructured storage, NoSQL databases do not have a fixed table structure like the ones found in relational databases.

|Feature|      NoSQL Databases |			Relational Databases|
|---|---|---|
|Performance| 		High|						Low|
|Reliability| 		Poor|						Good|
|Availability| 		Good|						Good|
|Consistency| 		Poor|						Good|
|DataStorage| 		Optimized for huge data|		Medium sized to large|
|Scalability| 		High|						High (but more expensive)|

----
download.md(assets/slides/data/data_structures.md)
----
download.md(assets/slides/data/sql.md)
----
download.md(assets/slides/data/db_sqlserver.md)
----
download.md(assets/slides/data/db_sybase.md)
----
download.md(assets/slides/data/db_oracle.md)
----
download.md(assets/slides/data/db_sqlite.md)
----
download.md(assets/slides/data/db_mysql.md)
----
download.md(assets/slides/data/db_postgre_sql.md)
----
download.md(assets/slides/data/no_sql.md)
----
download.md(assets/slides/data/db_mongodb.md)
----
download.md(assets/slides/data/distributed_database.md)
----
download.md(assets/slides/data/blockchain.md)
----
download.md(assets/slides/data/flux.md)
----
download.md(assets/slides/data/redux.md)
----
download.md(assets/slides/data/geodata.md)
----
download.md(assets/slides/data/infludb.md)