-- Show Vendor Cities and Vendor States from Vendors table
SELECT DISTINCT VendorCity, VendorState
FROM Vendors;

-- Get top 5 invoice total and also return VendorID from Invoices table
SELECT TOP 5 VendorID, InvoiceTotal
FROM Invoices
ORDER BY InvoiceTotal DESC;

-- Get top 5% rows and also return VendorID from Invoices table
SELECT TOP 5 PERCENT VendorID, InvoiceTotal
FROM Invoices
ORDER BY InvoiceTotal DESC;

-- Gets additional rows whose value is the same
SELECT TOP 5 WITH TIES VendorID, InvoiceDate 
FROM Invoices
ORDER BY InvoiceDate ASC;

-- No offset, only 5 rows, order by Total invoice amount in descending order
SELECT VendorID, InvoiceTotal 
FROM Invoices 
ORDER BY InvoiceTotal DESC
OFFSET 0 Rows
FETCH FIRST 5 ROWS ONLY;

-- Get rows 10-20, skipped first 10 rows and only fetched up to 20 where vendor state is California, ordered by vendor city
SELECT VendorName , VendorCity , VendorState , VendorZipCode 
FROM Vendors
WHERE VendorState = 'CA'
ORDER BY VendorCity 
OFFSET 10 ROWS
FETCH NEXT 10 ROWS ONLY;


-- Using Distinct statement for invoices after specified date
SELECT COUNT(DISTINCT VendorID) AS DistinctNumberOfVendors,
COUNT(VendorID) AS EveryVendorInTable,
AVG(InvoiceTotal) AS AverageInvoiceAmount,
SUM(InvoiceTotal) AS TotalInvoiceAmount
FROM Invoices
WHERE InvoiceDate > '2019-07-01';

-- Count total number of unpaid invoices and calculate the total amount due (Only if >0)
SELECT COUNT(*) AS NumberOfInvoices,
SUM(InvoiceTotal - PaymentTotal - CreditTotal) AS TotalDue
FROM Invoices
WHERE InvoiceTotal - PaymentTotal - CreditTotal > 0;

-- Count number of rows in invoice table after specified date
SELECT 'After 7/1/2019' AS SelectionDate,
COUNT(*) AS NumberOfInvoices,
AVG(InvoiceTotal) AS AverageInvoiceAmount,
SUM(InvoiceTotal) AS TotalInvoiceAmount
FROM Invoices
WHERE InvoiceDate > '2019-07-01'

-- Return low/high in the sort sequence (in this case alphabetical) and also count of vendors
SELECT MIN(VendorName) AS FirstVendor,
MAX(VendorName ) AS LastVendor,
COUNT(VendorName) AS NumberOfVendors
FROM Vendors;