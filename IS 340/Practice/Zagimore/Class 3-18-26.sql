-- Group by product vendorid
SELECT vendorid,
COUNT(*) AS "numberOfProducts",
AVG(productprice) AS "avergeProductPrice"
FROM product 
GROUP BY vendorid;

SELECT COUNT(*),
AVG(productprice ) AS "averageProductPrice"
FROM product 
GROUP BY vendorid

-- Get count of products over $100
SELECT vendorid,
COUNT(*) AS "over100Count"
FROM product
WHERE productprice >= 100
GROUP BY vendorid

SELECT vendorid,
categoryid,
COUNT(*), 
AVG(productprice) AS "avergageProductPrice"
FROM product
GROUP BY vendorid, categoryid;

SELECT productid, SUM(quantity) AS "sumQuantity"
FROM includes
GROUP BY productid;