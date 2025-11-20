rename table students to collage;

DROP TABLE collage;

alter table students rename column Name to User;

alter table students drop column addmisson_data ;


alter table students add column is_pass bool default false;


alter table students modify column User varchar(50) default"" NOT null;

describe students;

