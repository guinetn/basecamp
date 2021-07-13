### DOCUMENTS DATABASES

Data is stored in documents (instead of rows and columns in a table) and these documents are grouped together in collections. Each document can have an entirely different structure.
Document databases include the CouchDB and MongoDB

Handle documents containing information with a complex structure (types, lists, nestings). It is based on the key/value principle, but with an extension on the fields that make up this document
Structured approach to each value, thus forming a document
Rich query languages allowing complex manipulations on each attribute of the document (and sub-documents) like in relational but in a distributed fashion.

**Applications**
Content management (digital libraries, product collections, software repositories, multimedia collections, etc.)
Framework for storing objects
Collection of complex events
Management of user histories on social networks.

**Who?**
MongoDB (MongoDB) : ADP, Adobe, Bosch, Cisco, eBay, Electronic Arts, Expedia, Foursquare
CouchBase (Apache, Hadoop) : AOL, AT&T, Comcast, Disney, PayPal, Ryanair
DynamoDB (Amazon) : BMW, Dropcam, Duolingo, Supercell, Zynga
Cassandra (Facebook -> Apache) : NY Times, eBay, Sky, Pearson Education
Cassandra is "wide-column store" = document oriented




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
