### KEY-VALUE STORES 
Hash table on the network
Simple, efficient
Key 	→ Hash function → index
Value	→ anyhing

Data is stored in an array of key-value pairs. The ‘key’ is an attribute name that is linked to a ‘value’.
Well-known key-value stores include Redis, Voldemort, and Dynamo.

No language possible → CRUD only: 
- Create (key,value)
- Read (key)
- Update (key,value)
- Delete (key) 

**Applications**
Realtime fraud detection
IoT
E-commerce
Cache
Fast transactions
Logs
Chat

**Who?**
- Redis (VMWare) : Vodafone, Trip Advisor, Nokia, Samsung, Docker
- Memcached (Danga) : LiveJournal, Wikipédia, Flickr, Wordpress
- Azure Cosmos DB (Microsoft) : Real Madrid, Orange tribes, MSN, LG, Schneider Electric
- SimpleDB (Amazon)



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