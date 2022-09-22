-- select name, film.language_id from film 
-- join language on language.language_id = film.language_id

-- select title, description, name from film 
-- LEFT join language on language.language_id = film.language_id

-- select title, description, name from film 
-- right join language on language.language_id = film.language_id

-- create table new_film (
-- 	id serial primary key,
-- 	name varchar (50) not null
-- );

-- insert into new_film (name)
-- Values('Saving Private Ryan'),
-- ('Shawshank Redemption'),
-- ('Goodfellas'),
-- ('First Man'),
-- ('My Cousin Vinny');

-- create table customer_review (
-- 	review_id serial primary key,
-- 	film_id int,
-- 	language_id int,
-- 	title varchar (20) not null,
-- 	score smallint not null,
-- 	review_text text not null,
-- 	last_update date not null,
-- 	foreign key (film_id ) references new_film(id) ON DELETE CASCADE,
-- 	foreign key (language_id) references language(language_id) ON DELETE CASCADE
-- )

-- insert into customer_review (film_id, language_id, title, score, review_text, last_update)
-- values(1,1,'Saving Private Ryan',9,'Amazing war film','2022-07-26'),
-- (2,1,'Shawshank Redemption',9,'Epic Tale','2022-07-26'),
-- (3,1,'Goodfellas',9,'Wonderful Mob movie','2022-07-26'),
-- (4,1,'First Man',7,'The myth, the man, the legend','2022-07-26'),
-- (5,1,'My Cousin Vinny',9,'Comedy for the ages','2022-07-26');



-- insert into customer_review(film_id, language_id, title, score, review_text, last_update)
-- select film_id, film.language_id, title, 5, 'Good', '2022-07-26' from film
-- join language on film.language_id=language.language_id
-- join new_film on new_film.id=film.film_id
-- where new_film.id=1

-- insert into customer_review(film_id, language_id, title, score, review_text, last_update)
-- select film_id, film.language_id, title, 5, 'Good', '2022-07-26' from film
-- join language on film.language_id=language.language_id
-- join new_film on new_film.id=film.film_id
-- where new_film.id=2

-- delete from new_film where id = 1;










