-- Get productid, productname, vendor Id and product price when less than or equal to 110 and category is FW

SELECT productid, productname, vendorid, productprice
FROM product
WHERE productprice <= 110 AND categoryid = 'FW';

-- Find vendor name when name A/O


SELECT productid, productname, vendorid, productprice
FROM product
WHERE vendorid < 'p%';

-- Find product with prices between $35 and $100

SELECT productid, productname, productprice
FROM product
WHERE productprice BETWEEN 35 and 100;


-- Get fields from vendor and customer data
SELECT vendorid, vendorname
FROM vendor;

SELECT customername , customerzip 
FROM customer;

-- Get product info or products where the productprice is over 100
SELECT productid , productname , productprice
FROM product
WHERE productprice >= 100;

-- Product info for products with a category id less than M (Which is A-L)
SELECT productname , productid, categoryid 
FROM product
WHERE categoryid < 'M%';


-- Select the top 5 products, order by price in descending orders
SELECT top 5 productid, productname, productprice 
FROM product
order by productprice DESC 


