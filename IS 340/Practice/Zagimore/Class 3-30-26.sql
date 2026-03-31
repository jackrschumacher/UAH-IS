UPDATE product
SET productprice = 10
WHERE productid = '7x7';

ALTER TABLE product
ADD discount NUMERIC(3,2);

UPDATE product
SET discount = 0.2;

UPDATE product
SET discount = 0.3
WHERE vendorid = 'MK';

ALTER TABLE product DROP column discount;

CREATE VIEW products_more_than_3_sold AS
SELECT productid, productname, productprice
FROM product 
WHERE productid IN
	(SELECT productid
	FROM includes
	GROUP BY productid
	HAVING SUM(quantity) >3);

CREATE VIEW products_in_multiple_trnsc AS
SELECT productid, productname, productprice
FROM product
WHERE productid IN 
	(SELECT productid
	FROM includes
	GROUP BY productid
	HAVING COUNT(*) > 1);

SELECT *
FROM products_more_than_3_sold
UNION 
SELECT *
FROM products_in_multiple_trnsc;