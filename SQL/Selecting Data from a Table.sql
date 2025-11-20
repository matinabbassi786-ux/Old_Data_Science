
SELECT * FROM student;


select name,age from schooldb.student;

select * from schooldb.student where grade = "10th";

select * from schooldb.student where age <= 18;

select * from schooldb.student where grade in ("10th","11th");

select * from schooldb.student where grade not in ("10th","11th");

SELECT * FROM student WHERE grade = NULL;

SELECT * FROM student WHERE grade IS NULL;

SELECT * FROM student WHERE grade IS NOT NULL;

SELECT * FROM student ORDER BY age ASC;

SELECT * FROM student ORDER BY name DESC;

SELECT * FROM student LIMIT 5;

SELECT * FROM student LIMIT 2, 5;














