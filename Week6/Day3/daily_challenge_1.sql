-- create table customer (
-- 	id serial primary key not null,
-- 	fname varchar (20) not null,
-- 	lname varchar (20) not null
-- );

-- create table customer_profile (
-- 	id serial primary key not null,
-- 	isLoggedIn boolean DEFAULT false,
-- 	customer_id int not null,
-- 	foreign key (customer_id) references customer(id)
-- );



-- insert into customer (fname, lname)
-- values 
-- 	('John','Doe'),
-- 	('Jerome','Lalu'),
-- 	('Lea','Rive');


insert into customer_profile (isLoggedIn, customer_id)
select 'false', id from customer where fname ILIKE 'Jerome';


select customer_id, fname 
from customer 
join customer_profile
on customer.id = customer_profile.customer_id;

select customer_id, isLoggedIn, fname 
from customer 
left join customer_profile
on customer.id = customer_profile.customer_id;

select count(*) from customer_profile where isLoggedIn = 'false'
