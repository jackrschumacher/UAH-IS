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

