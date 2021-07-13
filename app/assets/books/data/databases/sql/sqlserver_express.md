## SQL Server Express

Install sql server express...fast... connect using ".\sqlexpress"

C:\Program Files\Microsoft SQL Server


## Microsoft SQL Server Express LocalDB 

LocalDB is an instance of SQL Server Express that can create and open SQL Server databases
system database files: C:\Users\<user>\AppData\Local\Microsoft\Microsoft SQL Server Local DB\Instances\LocalDBApp1\
User database files:   C:\Users\<user>\Documents\ 

[SqlLocalDb utility](https://docs.microsoft.com/en-us/sql/tools/sqllocaldb-utility)
- cli to create and manage an instance of SQL Server Express LocalDB
- create new instances of LocalDB
- start and stop an instance of LocalDB

SqlLocalDB.exe   
create   | c ] \<instance-name>  \<instance-version> [-s ]  
delete   | d ] \<instance-name>  
start    | s ] \<instance-name>  
stop     | p ] \<instance-name>  [ -i ] [ -k ]  
share    | h ] [" <user_SID> " | " <user_account> " ] " \<private-name> " " \<shared-name> "  
unshare  | u ] " \<shared-name> "  
info     | i ] \<instance-name>  
versions | v ]  
trace    | t ] [ on | off ]  
help     | -? ]  
  

Automatic instances
    public
    no need to create the instance; it just works
    name for the automatic instance is MSSQLLocalDB
named instances
    private
    owned by a single application that is responsible for creating and managing the instance. 
    isolation from other instances and can improve performance

Server=(localdb)\MSSQLLocalDB;Integrated Security=true
Server=(LocalDB)\MSSQLLocalDB;Integrated Security=true;AttachDbFileName=D:\Data\MyDB1.mdf   To connect to a specific database (by using the file name)

intended for developers
easy to install, doesn’t require complex configuration task to create an instance or to use the database. 
LocalDB installation copies a minimal set of files necessary to start the SQL Server Database Engine. Once LocalDB is installed, you can initiate a connection using a special connection string. When connecting, the necessary SQL Server infrastructure is automatically created and started, enabling the application to use the database without complex configuration tasks.



>SqlLocalDB info
    MSSQLLocalDB                      name for the automatic instance is MSSQLLocalDB
    SQLLocalDB start MSSQLLocalDB
    
>SQLLocalDB info MSSQLLocalDB
    Nom:                    	MSSQLLocalDB
    Version:                    13.1.4001.0
    Nom partagé:
    Propriétaire:               NGI5\nguin
    Création automatique:       Oui
    État:              			Arrêté
    Dernière heure de début:    29/06/2021 17:59:50
    Nom de canal de l'instance:

SqlLocalDB create LocalDBApp1
SqlLocalDB create Test 11.0
SqlLocalDB create NewInstance
SqlLocalDB start LocalDBApp1            Start the instance of LocalDB
SqlLocalDB start Test
SqlLocalDB info LocalDBApp1             Gather information about the instance of LocalDB
SqlLocalDB info Test 
SqlLocalDB stop MSSQLLocaDB
SqlLocalDB.exe create "DEPARTMENT" 12.0 -s   create + start


- https://docs.microsoft.com/en-us/sql/database-engine/configure-windows/sql-server-express-localdb?view=sql-server-ver15
- https://www.sqlshack.com/how-to-connect-and-use-microsoft-sql-server-express-localdb/
