-- update film set language_id = 2 where film_id between 1 and 20;

-- select * from film where film_id between 1 and 20

-- drop table customer_review

-- select count(*) from rental where return_date is NULL

-- select inventory.inventory_id, return_date, replacement_cost from rental
-- join inventory on rental.inventory_id = inventory.inventory_id
-- join film on film.film_id = inventory.film_id
-- where return_date is null
-- order by replacement_cost desc limit 30

-- select *,first_name,last_name from film 
-- join film_actor on film.film_id = film_actor.film_id
-- join actor on actor.actor_id = film_actor.actor_id
-- where description ilike '%sumo wrestler%' and 
-- 	first_name ilike '%penelope%' and
-- 	last_name ilike '%monroe%'


-- select *, name, film.film_id from film
-- join film_category on film.film_id=film_category.film_id
-- join category on category.category_id=film_category.category_id
-- where length <60 and rating ='R' and name='Documentary'


-- select *,  film.film_id from film
-- join inventory on  film.film_id= inventory.film_id
-- join rental on rental.inventory_id=inventory.inventory_id
-- join customer on customer.customer_id=rental.customer_id
-- where first_name='Matthew' and last_name='Mahan' and rental_rate>4 and '2005-07-28' < return_date  and return_date < '2005-08-01'


select *, film.film_id from film
join inventory on  film.film_id= inventory.film_id
join rental on rental.inventory_id=inventory.inventory_id
join customer on customer.customer_id=rental.customer_id
where title ilike '%boat%' or description ilike '%boat%' order by replacement_cost desc