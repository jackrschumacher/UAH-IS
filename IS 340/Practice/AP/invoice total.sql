-- From Slideshow (Slide 25). Want to see total due by calculating from InvoiceTotal, Paymenttotal, CreditTotal

SELECT InvoiceTotal, PaymentTotal, CreditTotal, InvoiceTotal - PaymentTotal - CreditTotal AS BalanceDue
FROM Invoices;