CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
);
--Assumption: Table created with 2 columns : id,name

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')
--Assumption: 4 entries inserted. the first 3 have ids 5-7 and the last has id null.

SELECT * FROM FirstTab --Assumption: shows whole table

CREATE TABLE SecondTab (
    id integer 
)--Assumption:table created with just one column

INSERT INTO SecondTab VALUES
(5),
(NULL)--Assumption:two entries made into second table: 5 and Null


SELECT * FROM SecondTab --Assumption:show whole table

 SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
	
	--Assumption: 4

SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
	
	--Assumption: 3
	
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
	
	--Assumption: 2
	
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
	
	--Assumption: 4