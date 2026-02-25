/* From Presentation (Slide 19) - Calculating derived attributes from a table
Want to pull up the productid, and productprice- but want to increase the product price by 10%
We want to get the original productprice as well as the productprice increased by 10%
*/

SELECT productid, productprice, productprice * 1.1 AS "productprice*1.1"
FROM product;
