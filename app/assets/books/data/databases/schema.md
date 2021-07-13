### SCHEMA
Collection of database objects including tables, views, triggers, stored procedures, indexes, types, interfaces, enums, unions...taht make up your application data model
Organize the database objects into logical groups to make them more manageable. Also, schema can be treated as a dictionary with all the information objects of the database.
>SELECT * FROM information_schema.columns; Or we can choose to see the schema for a specific table,
>SELECT * FROM information_schema.columns WHERE table_name = 'boats';
