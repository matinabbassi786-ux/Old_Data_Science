-- select current_date();
-- select current_time();
-- select current_timestamp();
-- select now();

show tables;

alter table students add column  date_jione  datetime default(now());


select * from harry.students;