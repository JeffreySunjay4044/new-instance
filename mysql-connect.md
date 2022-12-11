### Connect to mysql db using sqlcmd or using mysql cli

Once connected create database using `CREATE DATABASE test1;`

Once database is created. Create user `CREATE USER 'harish'@'localhost' IDENTIFIED BY 'test123';`
once user is create grant privileges to the user ` GRANT ALL PRIVILEGES ON test1.* TO 'sunjay1'@'localhost';`

Once done switch to test1 database and create table

` use test1;`
`CREATE TABLE userdetails( id varchar(256), name (varchar256), email (varchar256));`
Once done add rows to the table by running these
`INSERT INTO userdetails VALUES("harish", "harish", "harish@gmail.com");`


Once done use pip3 to install mysql-connector-python by running 
`pip3 install mysql-connector-python`

once done just run the code by python3 mysqldb.py