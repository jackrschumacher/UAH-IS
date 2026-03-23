-- For products where prive is below the average price of all products, retreive info
SELECT productid, productname, productprice
FROM product
WHERE productprice < (SELECT AVG(productprice) FROM product);

SELECT productid, productname, productprice 
FROM product
WHERE productid IN 
(SELECT productid FROM includes GROUP BY productid HAVING SUM(quantity) > 3);

-- Find num of distinct vendors in vendorid
SELECT DISTINCT vendorid
FROM product

-- Join the product and vendor tables together on vendorid
SELECT productid, productname, vendorname, productprice
FROM product, vendor
WHERE product.vendorid = vendor.vendorid