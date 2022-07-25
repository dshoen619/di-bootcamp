
-- select * from customer LIMIT 0

--select first_name,last_name as full_name from customer

--select distinct create_date from customer

-- SELECT * from customer order by first_name DESC

-- SELECT film_id, title, description,release_year,rental_rate from film 
-- order by rental_rate ASC

--select address, phone from address where district='Texas'

--select * from film where film_id=15 or film_id=150

--select film_id,title,description,length,rental_rate from film where title='Saving Private Ryan'

--select film_id,title,description,length,rental_rate from film where title LIKE 'Sa%'

-- select * from film order by replacement_cost ASC LIMIT 10

-- select * from film order by replacement_cost ASC LIMIT 10 offset 10

-- select * From customer
-- INNER JOIN payment
-- ON customer.customer_id=payment.customer_id;

-- select * from film 
-- where NOT EXISTS (SELECT film_id from inventory where inventory.film_id = film.film_id)


select * from city
inner join country 
on city.country_id = country.country_id
