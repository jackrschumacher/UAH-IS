-- From Slideshow (Slide 27). Get age of Invoice

SELECT invoiceDate,
	GETDATE() AS "Todays' Date",
	DATEDIFF(day, InvoiceDate, GETDATE()) AS Age FROM Invoices;