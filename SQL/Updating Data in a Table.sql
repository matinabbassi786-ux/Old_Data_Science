use schooldb;
select * from schooldb.student;

UPDATE student SET grade = '12th' WHERE id = 2;

select * from student where grade = "12th";

update student set grade = 'Pass' where grade = 'done';

update student set age = age + 1 where age <= 18; 