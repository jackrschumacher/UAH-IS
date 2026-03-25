select vendorName, vendorID
FROM Vendors
ORDER BY VendorName asc;

SELECT vendorID
FROM Invoices
ORDER BY VendorID asc;

-- Returns matched and unmatched records from the Vendors - therefore returns some null values
SELECT VendorName, InvoiceNumber, InvoiceTotal 
FROM Vendors LEFT JOIN Invoices
	ON Vendors.VendorID = Invoices.VendorID 
ORDER BY VendorName;

-- Returns matched records
SELECT VendorName, InvoiceNumber, InvoiceTotal 
FROM Vendors RIGHT JOIN Invoices
	ON Vendors.VendorID = Invoices.VendorID 
ORDER BY VendorName;


SELECT VendorName, InvoiceNumber, InvoiceTotal 
FROM Vendors FULL JOIN Invoices
	ON Vendors.VendorID = Invoices.VendorID 
ORDER BY VendorName;