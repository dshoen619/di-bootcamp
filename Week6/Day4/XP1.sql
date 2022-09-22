
-- select first_name as "First Name", last_name as "Last Name" from employees

-- select distinct department_id from employees

-- select * from employees order by first_name desc

-- select first_name, last_name, salary, 0.15*salary as "PF" from employees

-- select employee_id, first_name, last_name, salary from employees order by salary asc

-- select sum(salary) from employees

-- select min(salary), max(salary) from employees

-- select avg(salary) from employees

-- select count(first_name) from employees

-- select upper (first_name) from employees

--  select substring(first_name,1, 3) from employees

-- select concat(first_name,' ',last_name) from employees


--select first_name, last_name, length(concat(first_name,' ',last_name)) from employees

-- select first_name from employees where first_name like  '%[0-9]%'

-- select * from employees limit 10