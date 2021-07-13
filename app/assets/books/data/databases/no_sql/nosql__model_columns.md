### COLUMNS ORIENTED
Attribut (column) focus: ignore others columns

Instead of ‘tables,’ in columnar databases we have column families, which are containers for rows. Unlike relational databases, we don’t need to know all the columns upfront and each row doesn’t have to have the same number of columns.
Columnar databases are best suited for analyzing large datasets, big names include Cassandra and HBase.

**Applications**
Analytics
Aggregations
Not for found a single value
Counter (online voting)
Journalisation
Categorie search
Large reporting 

**Who?**
BigTable (Google)
HBase (Apache, Hadoop)
Spark SQL (Apache)
Elasticsearch (elastic) -> moteur de recherche



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