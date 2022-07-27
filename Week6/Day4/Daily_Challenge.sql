-- create table items(  
-- items_id int,
-- name varchar(30),
-- price integer,
-- primary key (items_id));


-- create table product_orders(  
-- order_id serial,
-- quantity int,
-- l_name varchar(30),
-- fk_items_id int not Null,
-- primary key (order_id),
-- Foreign Key (fk_items_id) references items(items_id) on DELETE CASCADE
-- );

--  insert into items (items_id,name,price)
--  Values(1,'chair',20),
--  (2,'couch',100),
--  (3,'table',75);
 
--  insert into product_orders(quantity, l_name, fk_items_id)
--  Values(1,'Smith',2);

 


create function find_price ()
RETURNS INTEGER AS $birthdate$
BEGIN
	RETURN(select price*quantity AS "Total Price" from product_orders
			join items on product_orders.fk_items_id=items.items_id);
END;
$birthdate$ LANGUAGE plpgsql;


Select *From find_price()