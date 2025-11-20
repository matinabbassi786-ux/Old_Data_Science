select @@autocommit;

-- SET autocommit = 1;

-- select * from harry.students;

-- use harry;
-- describe harry.students;

-- alter  table harry.students drop column addmisson_data;
-- alter table harry.students modify column id int auto_increment;

-- insert into harry.students (id,Name,age,Email) value(2,"jone",20,"jone@gmail.com");




start transaction;
update students set age = 0 where id = 1; 
rollback;
commit;
select * from harry.students;

 