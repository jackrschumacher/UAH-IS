-- Select all vendorid from the product table
SELECT vendorid
FROM product;

-- Select distinct vendorid from the product table
SELECT DISTINCT vendorid
FROM product;

-- Get all products in FW category, sort by price
SELECT productid, productname, productprice, categoryid
FROM product 
WHERE categoryid = 'FW'
ORDER BY productprice;

-- Same query, desc price
SELECT productid, productname, productprice, categoryid
FROM product 
WHERE categoryid = 'FW'
ORDER BY productprice DESC;

-- Order by Category ID and Product prices
SELECT productid, productname, productprice, categoryid
FROM product
ORDER BY categoryid, productprice;

-- Get productnames like boot using wildcard syntax
SELECT * 
FROM product
WHERE productname LIKE'%Boot%'

-- Get productnames where the name ends with 'a'
SELECT productid, productname
FROM product
WHERE productname LIKE '%a';

-- Get store info when store zip does not end with 'o'
SELECT storeid, storezip, regionid
FROM store
WHERE storezip NOT LIKE '%o'

-- Find average product price
SELECT AVG(productprice)
FROM product;

-- Find number of products offered for sale
SELECT COUNT(*)
FROM product;

-- Find number of distinct vendorid/vendors
SELECT COUNT(DISTINCT vendorid)
FROM product;

-- Find product info in the CP category
SELECT COUNT(*) AS "Count*",
AVG(productprice) AS "AVGproductprice",
MIN(productprice) AS "MINproductprice",
MAX(productprice) AS "MAXproductprice"
FROM product
WHERE categoryid = 'CP';
