use firs_databases;

show tables;


create table students (
id int auto_increment primary key,
Name  Varchar(100) not null default "No Name",
Age int,
Email varchar(100) unique,
addmisson_data date
)

select * from students;

describe students;