# 0x0D. SQL - Introduction

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/jfYCdfSeM9SClR9gWzDaLA "explain to anyone"),  **without the help of Google**:

### General

-   What’s a database
-   What’s a relational database
-   What does SQL stand for
-   What’s MySQL
-   How to create a database in MySQL
-   What does  `DDL`  and  `DML`  stand for
-   How to  `CREATE`  or  `ALTER`  a table
-   How to  `SELECT`  data from a table
-   How to  `INSERT`,  `UPDATE`  or  `DELETE`  data
-   What are  `subqueries`
-   How to use MySQL functions

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be executed on Ubuntu 14.04 LTS using  `MySQL 5.7`  (version 5.7.8-rc)
-   All your files should end with a new line
-   All your SQL queries should have a comment just before (i.e. syntax above)
-   All your files should start by a comment describing the task
-   All SQL keywords should be in uppercase (`SELECT`,  `WHERE`…)
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   The length of your files will be tested using  `wc`

## More Info

### Comments for your SQL file:

```
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

```

### Install MySQL 5.7 on Ubuntu 14.04 LTS

```
$ echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
$ sudo apt-get update
$ sudo apt-get install mysql-server-5.7
...
$ mysql --version
mysql  Ver 14.14 Distrib 5.7.8-rc, for Linux (x86_64) using  EditLine wrapper
$

```

**Don’t forget your  `root`  password**

Connect to your MySQL server:

```
$ mysql -hlocalhost -uroot -p
Password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 42
Server version: 5.7.8-rc MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> quit
Bye
$

```

If you have some issues to upgrade to 5.7, don’t hesitate to cleanup your server of any MySQL packages:  `sudo apt-get remove --purge mysql-server mysql-client mysql-common`

### Use “container-on-demand” to run MySQL

-   Ask for container  `Ubuntu 14.04 - Python 3.4`
-   Connect via SSH
-   OR connect via the Web terminal
-   In the container, you should start MySQL before playing with it:

```
$ service mysql start
 * MySQL Community Server 5.7.8-rc is started
$
$ cat 0-list_databases.sql | mysql -uroot -p my_database
Enter password: 
Database
information_schema
mysql
performance_schema
sys
$

```

**In the container, credentials are  `root/root`**

## Quiz questions

Hide

#### Question #0

What does SQL stand for?
    
-   Structured Query Language 

#### Question #1

What is a relational database? (please select all correct answers)

-   a database
    
-   a collection of data
  
-   data are organized by tables, records and columns
    
-   a table containing only one object representation
    

#### Question #2

What does DDL stand for?

-   Data Definition Language
    

#### Question #3

What does DML stand for?
    
-   Data Manipulation Language
     

#### Question #4

How do you list all  `users`  in this table?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```


    
-   SELECT * FROM users;
    
    

#### Question #5

How to you add a new record in the table  `users`?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```


-   INSERT INTO users (id, name, age) VALUES (2, “Betty”, 30);
    

    

#### Question #6

How do you delete the  `users`  record with  `id = 89`  in this table?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```

    
-   DELETE FROM users WHERE id = 89;
    

    

#### Question #7

How do you change the name of the  `users`  record with  `id = 89`  to  `Holberton`?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```

-   UPDATE users SET name = “Holberton” WHERE id = 89;
    


#### Question #8

How do you list all  `users`  records with  `age > 21`  in this table?

```
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                  |
+-------+-------------------------------------------------------------------------------------------------------------------------------+
| users | CREATE TABLE `users` (
  `id` int(11) DEFAULT NULL,
  `name` varchar(256) DEFAULT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+-------------------------------------------------------------------------------------------------------------------------------+

```

    
-   SELECT * FROM users WHERE age > 21;


## Tasks

### 0. List databases

mandatory

Write a script that lists all databases of your MySQL server.

```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `0-list_databases.sql`



### 1. Create a database

mandatory

Write a script that creates the database  `hbtn_0c_0`  in your MySQL server.

-   If the database  `hbtn_0c_0`  already exists, your script should not fail
-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements

```
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `1-create_database_if_missing.sql`



### 2. Delete a database

mandatory

Write a script that deletes the database  `hbtn_0c_0`  in your MySQL server.

-   If the database  `hbtn_0c_0`  doesn’t exist, your script should not fail
-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements

```
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
guillaume@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `2-remove_database.sql`



### 3. List tables

mandatory

Write a script that lists all the tables of a database in your MySQL server.

-   The database name will be passed as argument of  `mysql`  command (in the following example:  `mysql`  is the name of the database)

```
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `3-list_tables.sql`



### 4. First table

mandatory

Write a script that creates a table called  `first_table`  in the current database in your MySQL server.

-   `first_table`  description:
    -   `id`  INT
    -   `name`  VARCHAR(256)
-   The database name will be passed as an argument of the  `mysql`  command
-   If the table  `first_table`  already exists, your script should not fail
-   You are not allowed to use the  `SELECT`  or  `SHOW`  statements

```
guillaume@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `4-first_table.sql`



### 5. Full description

mandatory

Write a script that prints the full description of the table  `first_table`  from the database  `hbtn_0c_0`  in your MySQL server.

-   The database name will be passed as an argument of the  `mysql`  command
-   You are not allowed to use the  `DESCRIBE`  or  `EXPLAIN`  statements

```
guillaume@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `5-full_table.sql`

Done?  Help  Check your code  Get a sandbox

### 6. List all in table

mandatory

Write a script that lists all rows of the table  `first_table`  from the database  `hbtn_0c_0`  in your MySQL server.

-   All fields should be printed
-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `6-list_values.sql`


### 7. First add

mandatory

Write a script that inserts a new row in the table  `first_table`  (database  `hbtn_0c_0`) in your MySQL server.

-   New row:
    -   `id`  =  `89`
    -   `name`  =  `Holberton School`
-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
89  Holberton School
89  Holberton School
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `7-insert_value.sql`


### 8. Count 89

mandatory

Write a script that displays the number of records with  `id = 89`  in the table  `first_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `8-count_89.sql`


### 9. Full creation

mandatory

Write a script that creates a table  `second_table`  in the database  `hbtn_0c_0`  in your MySQL server and add multiples rows.

-   `second_table`  description:
    -   `id`  INT
    -   `name`  VARCHAR(256)
    -   `score`  INT
-   The database name will be passed as an argument to the  `mysql`  command
-   If the table  `second_table`  already exists, your script should not fail
-   You are not allowed to use the  `SELECT`  and  `SHOW`  statements
-   Your script should create these records:
    -   `id`  = 1,  `name`  = “John”,  `score`  = 10
    -   `id`  = 2,  `name`  = “Alex”,  `score`  = 3
    -   `id`  = 3,  `name`  = “Bob”,  `score`  = 14
    -   `id`  = 4,  `name`  = “George”,  `score`  = 8

```
guillaume@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `9-full_creation.sql`



### 10. List by best

mandatory

Write a script that lists all records of the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   Results should display both the score and the name (in this order)
-   Records should be ordered by score (top first)
-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `10-top_score.sql`



### 11. Select the best

mandatory

Write a script that lists all records with a  `score >= 10`  in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   Results should display both the score and the name (in this order)
-   Records should be ordered by score (top first)
-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `11-best_score.sql`



### 12. Cheating is bad

mandatory

Write a script that updates the score of Bob to  `10`  in the table  `second_table`.

-   You are not allowed to use Bob’s id value, only the  `name`  field
-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `12-no_cheating.sql`


### 13. Score too low

mandatory

Write a script that removes all records with a  `score <= 5`  in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
guillaume@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `13-change_class.sql`


### 14. Average

mandatory

Write a script that computes the score average of all records in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The result column name should be  `average`
-   The database name will be passed as an argument of the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `14-average.sql`



### 15. Number by score

mandatory

Write a script that lists the number of records with the same score in the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   The result should display:
    -   the  `score`
    -   the number of records for this  `score`  with the label  `number`
-   The list should be sorted by the number of records (descending)
-   The database name will be passed as an argument to the  `mysql`  command

```
guillaume@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `15-groups.sql`


### 16. Say my name

mandatory

Write a script that lists all records of the table  `second_table`  of the database  `hbtn_0c_0`  in your MySQL server.

-   Don’t list rows without a  `name`  value
-   Results should display the score and the name (in this order)
-   Records should be listed by descending score
-   The database name will be passed as an argument to the  `mysql`  command

In this example, new data have been added to the table  `second_table`.

```
guillaume@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
guillaume@ubuntu:~/$ 

```

**Repo:**

-   GitHub repository:  `holbertonschool-higher_level_programming`
-   Directory:  `0x0D-SQL_introduction`
-   File:  `16-no_link.sql`