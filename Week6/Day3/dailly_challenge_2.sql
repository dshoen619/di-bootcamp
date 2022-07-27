

-- select name, title from library 
-- join book on book.book_id = library.book_fk_id
-- join student on student.student_id = library.student_fk_id;

-- select avg(age) from library 
-- join student on library.student_fk_id = student.student_id

delete from student where student_id = 1;
select * from library