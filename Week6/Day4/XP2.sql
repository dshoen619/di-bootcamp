--select first_name, last_name, salary from employees where salary > 10000 and salary <15000

--select first_name, last_name , hire_date from employees  where hire_date>'1986-12-31' and hire_date<'1988-01-01'

--select first_name, last_name from employees where first_name LIKE '%c%' and first_name LIKE '%e%'

-- select last_name, job_title, employees.salary from employees
-- join jobs on jobs.job_id=employees.job_id
-- where job_title not like '%Programmers%' and job_title not like '%Shipping Clerks%' 
-- and salary !=4500 and salary!= 10000 and salary!= 15000

--select last_name from employees where length(last_name)=6

--select last_name from employees where last_name like '__e%'

-- select job_title from employees
-- join jobs on jobs.job_id=employees.job_id


select * from employees where last_name like '%Jones%' or last_name like '%Blake%' or last_name like '%Scott%'
 or last_name like '%King%' or last_name like '%Ford%'