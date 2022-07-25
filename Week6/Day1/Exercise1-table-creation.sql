CREATE TABLE items(
item_id SERIAL PRIMARY KEY,
item VARCHAR (50) NOT NULL,
price integer NOT NULL);

INSERT INTO items (item, price)
VALUES ('small desk',100);

INSERT INTO items (item, price)
VALUES ('large desk',300);

INSERT INTO items (item, price)
VALUES ('fan',80);



-- CREATE TABLE customers(
-- customer_id SERIAL PRIMARY KEY,
-- f_name VARCHAR(50) NOT NULL,
-- l_name VARCHAR(50) NOT NULL);


-- INSERT INTO customers(f_name, l_name)
-- VALUES('Greg', 'Jones');

-- INSERT INTO customers(f_name, l_name)
-- VALUES('Sandra', 'Jones');

-- INSERT INTO customers(f_name, l_name)
-- VALUES('Scott', 'Scott');

-- INSERT INTO customers(f_name, l_name)
-- VALUES('Trevor', 'Green');

-- INSERT INTO customers(f_name, l_name)
-- VALUES('Melanie', 'Johnson');


