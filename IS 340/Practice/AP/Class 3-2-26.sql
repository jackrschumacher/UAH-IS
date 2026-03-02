-- Null value
SELECT InvoiceID, PaymentDate 
FROM Invoices;
WHERE PaymentDate IS NULL;

-- Show not null value

SELECT InvoiceID, PaymentDate
FROM Invoices; 
WHERE PaymentDate IS NOT NULL;


-- Automatically bulk update NULL values to non-null values, replacing with 1900-01-01 as date
SELECT PaymentDate,
COALESCE(PaymentDate, '1900-01-01') AS NewDate
FROM Invoices; 

-- Changing/Casting data types in results. Flexibility to convert data types to the values that you want
SELECT InvoiceDate, InvoiceTotal,
	CAST(InvoiceDate as Varchar) AS varcharDate,
	CAST(InvoiceTotal as int) AS integerTotal,
	CAST(InvoiceTotal as money) AS varcharTotal
FROM Invoices;
