## NoSQL servers
 
|           |   Storage Type|	Query Method	Interface	Programming |Language	|Open |Source Replication|
|Cassandra	|	Column Store|	Thrift API		 |Thrift		|Java		           |Yes			|Async|
|MongoDB	|	Document Store|	Mongo Query		 |TCP/|IP		|C++		           |Yes			|Async|
|HyperTable	|	Column Store|	HQL				 |Thrift		|Java		           |Yes			|Async|
|CouchDB	|	Document Store|	MapReduce		 |REST			|Erlang		           |Yes			|Async|
|BigTable	|	Column Store|	MapReduce		 |TCP/|IP		|C++		           |No			|Async|
|HBase		|	Column Store|	MapReduce		 |REST			|Java		           |Yes			|Async|

**NoSQL selection**
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


::::
download.page(data/databases/no_sql/servers/nosql_elasticsearch.md)
::::
download.page(data/databases/no_sql/servers/nosql_mongodb.md)
::::
download.page(data/databases/no_sql/servers/nosql_cassandra.md)
::::
download.page(data/databases/no_sql/servers/nosql_ravendb.md)
::::
download.page(data/databases/no_sql/servers/nosql_couchdb.md)
::::
download.page(data/databases/no_sql/servers/nosql_redis.md)
::::
download.page(data/databases/no_sql/servers/nosql_azure_cosmosdb.md)